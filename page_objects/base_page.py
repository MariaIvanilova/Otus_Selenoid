import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = browser.logger
        self.class_name = type(self).__name__

    def open_page(self):
        self.logger.info("| Class: %s | Opening url: %s" % (self.class_name, self.url))
        self.browser.get(url=self.url)

    def is_element_present(self, locator: tuple):
        self.logger.info(
            (
                "| Class: %s | Check if elements %s is present"
                % (self.class_name, str(locator))
            )
        )
        try:
            return self.browser.find_element(*locator)
        except NoSuchElementException:
            # self.browser.save_screenshot(f"{self.browser.session_id}.png")
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot.png",
                attachment_type=allure.attachment_type.PNG,
            )
            raise AssertionError(
                f"Element with locator:{locator} is absent on pade {self.browser.current_url}"
            )

    def is_elements_list_present(self, elements: list):
        self.logger.info(
            (
                "| Class: %s | Check if list of elements %s are present"
                % (self.class_name, str(elements))
            )
        )
        for locator in elements:
            try:
                self.browser.find_element(*locator)
            except NoSuchElementException:
                # self.browser.save_screenshot(f"{self.browser.session_id}.png")
                allure.attach(
                    body=self.browser.get_screenshot_as_png(),
                    name=f"{self.browser.session_id}.png",
                    attachment_type=allure.attachment_type.PNG,
                )
                raise AssertionError(
                    f"Element with locator:{locator} is absent on pade {self.browser.current_url}"
                )
        return True

    def wait_title(self, title, timeout=3):
        self.logger.debug(
            "| Class: %s | Wait %s sec for title: %s"
            % (self.class_name, str(timeout), title)
        )
        try:
            return WebDriverWait(self.browser, timeout).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError(
                f"Expected title is {title}, but title is {self.browser.title}"
            )

    def wait_element(self, locator, timeout=1):
        self.logger.debug(
            "| Class: %s | Wait %s sec for element: %s"
            % (self.class_name, str(timeout), str(locator))
        )
        try:
            return WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            self.browser.save_screenshot(f"{self.browser.session_id}.png")
            raise AssertionError(f"Didn't wait for: {locator}")

    def wait_text(self, locator, text, timeout=1):
        self.logger.debug(
            "| Class: %s | Wait %s sec for text: %s on element: %s"
            % (self.class_name, str(timeout), text, str(locator))
        )
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
        except TimeoutException:
            raise AssertionError(f"Didn't wait for text: {text} in locator: {locator}")

    def input_value_to_field(self, locator: tuple, key_value: str):
        self.logger.debug(
            "| Class: %s | Set value: %s to element: %s"
            % (self.class_name, key_value, str(locator))
        )
        self.browser.find_element(*locator).send_keys(key_value)

    def click_to_element(self, locator: tuple):
        self.logger.debug("%s: Clicking element: %s" % (self.class_name, str(locator)))
        self.browser.find_element(*locator).click()

    def action_chains_click(self, locator: tuple):
        self.logger.debug("ActionChains.move_to_element.click to %s" % str(locator))
        element = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable(locator)
        )
        ActionChains(self.browser).move_to_element(element).pause(1).click().pause(
            1
        ).perform()

    def get_text(self, locator: tuple):
        self.logger.debug("Get text from element: %s" % str(locator))
        return self.browser.find_element(*locator).text

    def scroll_to_element(self, locator: tuple):
        self.logger.debug("Scroll to element: %s" % str(locator))
        self.browser.execute_script(
            "arguments[0].scrollIntoView(true);", self.browser.find_element(*locator)
        )
        time.sleep(1)

    def scroll_to_up(self):
        self.logger.debug("Scroll to page up")
        self.browser.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)

    def alert_confirm(self):
        self.logger.info("Accept alert")
        self.browser.switch_to.alert.accept()

    def scroll_to_down(self):
        self.logger.debug("Scroll to page down")
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
