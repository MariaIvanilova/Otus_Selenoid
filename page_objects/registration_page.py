import time

import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class RegistrationPage(BasePage):
    FIRST_NAME = (By.ID, "input-firstname")
    LAST_NAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    POLICY = (By.CSS_SELECTOR, "[name='agree']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")

    @allure.step("Получить список элементов на странице Register Account")
    def registration_elements(self):
        self.wait_title("Register Account")
        checking_elements = [
            self.FIRST_NAME,
            self.LAST_NAME,
            self.EMAIL,
            self.PASSWORD,
            self.SUBMIT_BUTTON,
        ]
        return self.is_elements_list_present(checking_elements)

    @allure.step("Зарегистрировать нового пользователя")
    def registration_add_user(self, first_name, last_name, email, password):
        self.wait_title("Register Account")

        self.input_value_to_field(self.FIRST_NAME, first_name)
        self.input_value_to_field(self.LAST_NAME, last_name)
        self.input_value_to_field(self.EMAIL, email)
        self.input_value_to_field(self.PASSWORD, password)
        self.action_chains_click(self.POLICY)
        self.click_to_element(self.SUBMIT_BUTTON)
