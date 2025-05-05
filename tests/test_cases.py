import allure

from page_objects.administration_page import AdministrationPage
from page_objects.catalog_page import CatalogPage
from page_objects.main_page import MainPage


@allure.title("Страница 'Administration'. Тест логин и выход из аккаунта")
def test_administration_login_logout(browser, url):
    administration_url = url + "administration"
    administration_page = AdministrationPage(browser, url=administration_url)
    administration_page.open_page()
    assert administration_page.administration_login(), (
        f"login should be successful - logout button should be present"
    )
    assert administration_page.administration_logout(), (
        f"Expected action: after logout - go to Administration page"
    )


@allure.title("Тест добавления продукта в корзину с главной страницы")
def test_main_page_add_to_cart(browser, url):
    main_page = MainPage(browser, url)

    main_page.open_page()
    text_added_product = main_page.main_page_get_description_product()
    text_product_in_cart = main_page.main_page_add_product_to_cart()

    assert text_product_in_cart == text_added_product, (
        f"{text_product_in_cart} should be {text_added_product}"
    )


@allure.title("Тест изменения цены при изменении валюты с главной страницы")
def test_main_page_change_currency(browser, url):
    main_page = MainPage(browser, url)

    main_page.open_page()
    first_price = main_page.main_get_price()
    main_page.main_change_currency()
    second_price = main_page.main_get_price()
    assert first_price != second_price, (
        f"price should be changed, initial price {first_price}, price after changing {second_price}"
    )


@allure.title("Тест изменения цены при изменении валюты на странице каталога")
def test_catalog_page_change_currency(browser, url):
    catalog_url = url + "catalog/desktops"
    catalog_page = CatalogPage(browser, url=catalog_url)

    catalog_page.open_page()
    first_price = catalog_page.catalog_get_price()
    catalog_page.catalog_change_currency()
    second_price = catalog_page.catalog_get_price()
    assert first_price != second_price, (
        f"price should be changed, initial price {first_price}, price after changing {second_price}"
    )
