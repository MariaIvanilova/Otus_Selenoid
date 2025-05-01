import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class AdministrationPage(BasePage):
    USER_NAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    LINK_TO_OPENCART = (By.CSS_SELECTOR, 'a[href="https://www.opencart.com"]')
    HEADER = (By.CSS_SELECTOR, ".card-header")

    LOGOUT = (By.ID, "nav-logout")

    CATALOG = (By.CSS_SELECTOR, "#menu-catalog>a")
    PRODUCTS = (By.CSS_SELECTOR, "#collapse-1>li:nth-child(2)")

    @allure.step("Получить список элементов на странице Administration")
    def administration_elements(self):
        checking_elements = [
            self.USER_NAME,
            self.PASSWORD,
            self.LOGIN_BUTTON,
            self.LINK_TO_OPENCART,
            self.HEADER,
        ]
        self.wait_title("Administration")
        return self.is_elements_list_present(checking_elements)

    @allure.step("Логин")
    def administration_login(self):
        self.wait_title("Administration")

        self.input_value_to_field(self.USER_NAME, "user")
        self.input_value_to_field(self.PASSWORD, "bitnami")
        self.click_to_element(self.LOGIN_BUTTON)
        self.wait_title("Dashboard")
        return self.is_element_present(self.LOGOUT)

    @allure.step("Логаут")
    def administration_logout(self):
        self.click_to_element(self.LOGOUT)
        return self.wait_title("Administration")

    @allure.step("В меню выбрать Products")
    def administration_go_to_product_page(self):
        self.click_to_element(self.CATALOG)
        self.wait_element(self.PRODUCTS)
        self.click_to_element(self.PRODUCTS)
