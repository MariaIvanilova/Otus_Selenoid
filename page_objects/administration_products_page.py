import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class ProductsPage(BasePage):
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, ".float-end>.btn.btn-primary")
    HEADER_ADD_PRODUCT = (By.CSS_SELECTOR, ".card-header")

    PRODUCT_NAME = (By.ID, "input-name-1")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".float-end>.btn.btn-primary")
    META_TAG_TITLE = (By.ID, "input-meta-title-1")
    DATA_TAB = (By.CSS_SELECTOR, ".nav.nav-tabs>.nav-item:nth-child(2)")
    MODEL = (By.ID, "input-model")
    SEO_TAB = (By.CSS_SELECTOR, ".nav.nav-tabs>.nav-item:nth-child(11)")
    KEY_WORD = (By.ID, "input-keyword-0-1")

    FILTER_NAME_PRODUCT = (By.CSS_SELECTOR, ".mb-3>#input-name")
    FIlTER_BUTTON = (By.CSS_SELECTOR, ".text-end>#button-filter")
    CHECK_BOX_PRODUCT = (By.CSS_SELECTOR, "tbody>tr>td>input.form-check-input")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-danger")

    NAME_PRODUCT_IN_FINDING = (By.CSS_SELECTOR, "tbody>tr>.text-start")

    LIST = (By.CSS_SELECTOR, "tbody>tr>td.text-center")

    @allure.step("Кликнуть добавить новый продукт")
    def products_click_add_new_item(self):
        self.wait_element(self.ADD_NEW_PRODUCT)
        self.click_to_element(self.ADD_NEW_PRODUCT)
        self.wait_element(self.HEADER_ADD_PRODUCT, timeout=2)
        return self.get_text(self.HEADER_ADD_PRODUCT)

    @allure.step("Добавить новый продукт")
    def products_add_new_product(self, product_name):
        self.input_value_to_field(self.PRODUCT_NAME, product_name)
        self.scroll_to_element(self.META_TAG_TITLE)
        self.input_value_to_field(self.META_TAG_TITLE, product_name)
        self.scroll_to_up()
        self.click_to_element(self.DATA_TAB)
        self.input_value_to_field(self.MODEL, "test_model")
        self.click_to_element(self.SEO_TAB)
        self.input_value_to_field(self.KEY_WORD, "test_key_word")
        self.click_to_element(self.SAVE_BUTTON)

    @allure.step("Найти продукт по имени")
    def products_find_by_name(self, product_name):
        self.wait_element(self.FILTER_NAME_PRODUCT)
        self.input_value_to_field(self.FILTER_NAME_PRODUCT, product_name)
        self.click_to_element(self.FIlTER_BUTTON)
        self.wait_text(self.NAME_PRODUCT_IN_FINDING, product_name)
        return self.get_text(self.NAME_PRODUCT_IN_FINDING)

    @allure.step("Выделить продукт (нажать чек-бокс)")
    def products_select_check_box(self):
        self.wait_element(self.CHECK_BOX_PRODUCT)
        self.click_to_element(self.CHECK_BOX_PRODUCT)

    @allure.step("Удалить продукт")
    def products_delete_product(self):
        self.click_to_element(self.DELETE_BUTTON)
        self.alert_confirm()
        self.wait_text(self.LIST, "No results!", timeout=2)
        return self.get_text(self.LIST)
