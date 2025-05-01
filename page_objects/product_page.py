import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_PHOTOS = (By.CSS_SELECTOR, ".image.magnific-popup")
    ADD_TO_WISH_LIST_BUTTON = (By.CSS_SELECTOR, "button[title='Add to Wish List']")
    COMPARE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[title='Compare this Product']")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    QUANTITY = (By.ID, "input-quantity")

    @allure.step(
        "Получить список элементов на странице продукта (Samsung Galaxy Tab 10.1)"
    )
    def product_page_elements(self):
        checking_elements = [
            self.PRODUCT_PHOTOS,
            self.ADD_TO_WISH_LIST_BUTTON,
            self.COMPARE_PRODUCT_BUTTON,
            self.ADD_TO_CART_BUTTON,
            self.QUANTITY,
        ]

        self.wait_title("Samsung Galaxy Tab 10.1")
        return self.is_elements_list_present(checking_elements)
