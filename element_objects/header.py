import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class HeaderElement(BasePage):
    CURRENCY = (By.CSS_SELECTOR, "form>.dropdown>a>.d-none.d-md-inline")
    EURO = (By.CSS_SELECTOR, "a[href='EUR']")
    POUND = (By.CSS_SELECTOR, "a[href='GBP']")
    USD = (By.CSS_SELECTOR, "a[href='USD']")
    CURRENCY_SIGN = (By.CSS_SELECTOR, ".dropdown>a>strong")

    @allure.step("Изменить валюту на EURO")
    def header_change_currency_eur(self):
        self.click_to_element(self.CURRENCY)
        self.wait_element(self.EURO, timeout=3)
        self.click_to_element(self.EURO)
        self.wait_element(self.CURRENCY_SIGN, timeout=3)
        self.browser.refresh()
        return self.get_text(self.CURRENCY_SIGN)

    @allure.step("Изменить валюту на POUND")
    def header_change_currency_gbp(self):
        self.click_to_element(self.CURRENCY)
        self.wait_element(self.POUND, timeout=3)
        self.click_to_element(self.POUND)
        self.wait_element(self.CURRENCY_SIGN, timeout=3)
        self.browser.refresh()
        return self.get_text(self.CURRENCY_SIGN)

    @allure.step("Изменить валюту на USD")
    def header_change_currency_usd(self):
        self.click_to_element(self.CURRENCY)
        self.wait_element(self.USD, timeout=3)
        self.click_to_element(self.USD)
        self.wait_element(self.CURRENCY_SIGN, timeout=3)
        self.browser.refresh()
        return self.get_text(self.CURRENCY_SIGN)
