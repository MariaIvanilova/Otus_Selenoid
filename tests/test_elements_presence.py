import allure

from page_objects.main_page import MainPage
from page_objects.catalog_page import CatalogPage
from page_objects.product_page import ProductPage
from page_objects.administration_page import AdministrationPage
from page_objects.registration_page import RegistrationPage


@allure.title("Проверка наличия элементов на главной странице -  Main")
def test_main_page_elements(browser, url):
    main_page = MainPage(browser, url)
    main_page.open_page()
    assert main_page.main_page_elements()


@allure.title("Проверка наличия элементов на странице: catalog/desktops")
def test_catalog_desktop_elements(browser, url):
    catalog_url = url + "catalog/desktops"
    catalog_page = CatalogPage(browser, url=catalog_url)
    catalog_page.open_page()
    assert catalog_page.catalog_desktops_elements()


@allure.title(
    "Проверка наличия элементов на странице продукта: product/tablet/samsung-galaxy-tab-10-1"
)
def test_product_elements(browser, url):
    product_url = url + "product/tablet/samsung-galaxy-tab-10-1"
    product_page = ProductPage(browser, url=product_url)
    product_page.open_page()
    assert product_page.product_page_elements()


@allure.title("Проверка наличия элементов на странице Administration")
def test_administration_elements(browser, url):
    administration_url = url + "administration"
    administration_page = AdministrationPage(browser, url=administration_url)
    administration_page.open_page()
    assert administration_page.administration_elements()


@allure.title("Проверка наличия элементов на странице регистрации: Registration")
def test_registration_elements(browser, url):
    registration_url = url + "/index.php?route=account/register"
    registration_page = RegistrationPage(browser, url=registration_url)
    registration_page.open_page()
    assert registration_page.registration_elements()
