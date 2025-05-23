import allure
from selenium.webdriver.common.by import By
from base_page import BasePage
import time

from element_objects.header import HeaderElement


class MainPage(BasePage):
    LOGO = (By.ID, "logo")
    MENU = (By.ID, "menu")
    CAROUSEL_UPPER = (By.CSS_SELECTOR, "#carousel-banner-0.slide")
    CAROUSEL_LOWER = (By.CSS_SELECTOR, "#carousel-banner-1.slide")
    ITEM = (By.CSS_SELECTOR, ".product-thumb")

    DESCRIPTION_ITEM = (By.CSS_SELECTOR, ".content>div[class='description']>h4>a")

    ADD_BUTTON = (By.CSS_SELECTOR, ".content>form>div>button")

    SHOPPING_CART = (By.CSS_SELECTOR, "a[title='Shopping Cart']")

    SHOPPING_CART_TEXT_ELEMENT = (By.CSS_SELECTOR, ".text-start.text-wrap>a")

    PRICE = (By.CSS_SELECTOR, ".price-new")
    CURRENCY = (By.CSS_SELECTOR, "form>.dropdown>a>.d-none.d-md-inline")
    EURO = (By.CSS_SELECTOR, "a[href='EUR']")

    @allure.step("Получить список элементов на странице Main")
    def main_page_elements(self):
        checking_elements = [
            self.LOGO,
            self.MENU,
            self.CAROUSEL_UPPER,
            self.CAROUSEL_LOWER,
            self.ITEM,
        ]
        self.wait_title("Your Store")
        return self.is_elements_list_present(checking_elements)

    @allure.step("Получить название продукта с главной страницы")
    def main_page_get_description_product(self):
        return self.get_text(self.DESCRIPTION_ITEM)

    @allure.step(
        "Добавить продукт в корзину, вернуть название добавленного продукта в корзине"
    )
    def main_page_add_product_to_cart(self):
        self.wait_title("Your Store")
        self.scroll_to_element(self.ADD_BUTTON)
        self.action_chains_click(self.ADD_BUTTON)
        self.scroll_to_up()
        time.sleep(6)  # waiting for disappearing alert window
        self.action_chains_click(self.SHOPPING_CART)
        self.wait_element(self.SHOPPING_CART_TEXT_ELEMENT)
        return self.get_text(self.SHOPPING_CART_TEXT_ELEMENT)

    @allure.step("Получить цену продукта")
    def main_get_price(self):
        self.wait_title("Your Store")
        self.wait_element(self.PRICE, timeout=3)
        return self.get_text(self.PRICE)

    @allure.step("Изменить валюту")
    def main_change_currency(self):
        header = HeaderElement(self.browser, self.url)
        header.header_change_currency_eur()
