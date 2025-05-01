import allure
from selenium.webdriver.common.by import By
from base_page import BasePage
from element_objects.header import HeaderElement


class CatalogPage(BasePage):
    PRODUCT = (By.CSS_SELECTOR, ".product-thumb")
    PRODUCT_COMPARE = (By.ID, "compare-total")
    SORT_BY = (By.ID, "input-sort")
    SHOW = (By.ID, "input-limit")
    SHOWING = (By.CSS_SELECTOR, ".col-sm-6.text-start")
    PAGES = (By.CSS_SELECTOR, ".col-sm-6.text-end")

    PRICE = (By.CSS_SELECTOR, ".price-new")
    CURRENCY = (By.CSS_SELECTOR, "form>.dropdown>a>.d-none.d-md-inline")
    EURO = (By.CSS_SELECTOR, "a[href='EUR']")

    @allure.step("Получить список элементов на странице Каталога (Desktops)")
    def catalog_desktops_elements(self):
        checking_elements = [
            self.PRODUCT_COMPARE,
            self.PRODUCT,
            self.SHOWING,
            self.PAGES,
            self.SORT_BY,
            self.SHOW,
        ]
        self.wait_title("Desktops")
        return self.is_elements_list_present(checking_elements)

    @allure.step("Получить цену продукта")
    def catalog_get_price(self):
        self.wait_title("Desktops")
        # self.browser.refresh()
        self.wait_element(self.PRICE, timeout=3)
        return self.get_text(self.PRICE)

    @allure.step("Поменять валюту")
    def catalog_change_currency(self):
        header = HeaderElement(self.browser, self.url)
        header.header_change_currency_gbp()
