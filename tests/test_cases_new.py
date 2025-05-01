import allure

from element_objects.header import HeaderElement
from page_objects.administration_page import AdministrationPage
from page_objects.administration_products_page import ProductsPage
from page_objects.registration_page import RegistrationPage
import helpers

test_product = "Test"


@allure.title("Тест добавление нового продукта")
def test_administration_add_new_product(browser, url):
    administration_url = url + "administration"
    administration_page = AdministrationPage(browser, url=administration_url)
    administration_page.open_page()
    administration_page.administration_login()
    administration_page.administration_go_to_product_page()

    products = ProductsPage(browser, url)
    assert "Add Product" in products.products_click_add_new_item(), (
        f"'Add Product' form should be shown"
    )

    products.products_add_new_product(test_product)

    administration_page.administration_go_to_product_page()

    assert test_product in products.products_find_by_name(test_product), (
        f"{test_product} product can be founded"
    )


@allure.title("Тест удаление добавленного продукта")
def test_administration_delete_product(browser, url):
    administration_url = url + "administration"
    administration_page = AdministrationPage(browser, url=administration_url)
    administration_page.open_page()
    administration_page.administration_login()
    administration_page.administration_go_to_product_page()

    products = ProductsPage(browser, url)
    products.products_find_by_name(test_product)
    products.products_select_check_box()
    assert products.products_delete_product() == "No results!"


@allure.title("Регистрация нового пользователя")
def test_registration_new_user(browser, url):
    user_information = helpers.user_registration_information()

    registration_url = url + "/index.php?route=account/register"

    registration_page = RegistrationPage(browser, url=registration_url)
    registration_page.open_page()
    registration_page.registration_add_user(*user_information)
    assert registration_page.wait_title("Your Account Has Been Created!")


@allure.title("Тест переключение валют из верхнего меню opencart")
def test_change_currency(browser, url):
    header_element = HeaderElement(browser, url)
    header_element.open_page()
    assert header_element.header_change_currency_eur() == "€", (
        f"{header_element.header_change_currency_eur()} should be €"
    )
    assert header_element.header_change_currency_gbp() == "£", (
        f"{header_element.header_change_currency_gbp()} should be £"
    )
    assert header_element.header_change_currency_usd() == "$", (
        f"{header_element.header_change_currency_usd()} should be $"
    )
