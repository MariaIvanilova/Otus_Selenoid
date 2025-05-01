import pytest
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logging

default_url = "http://192.168.100.4:8081/"
log_level = "DEBUG"


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="browser for tests")
    parser.addoption("--url", default=default_url)


@pytest.fixture
def browser(request):
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test started at %s" % datetime.datetime.now())
    logger.info("===> Test name: %s" % request.node.name)

    browser_name = request.config.getoption("browser")
    driver = None
    if browser_name in ["chrome", "ch"]:
        driver = webdriver.Chrome()
    elif browser_name in ["firefox", "ff"]:
        driver = webdriver.Firefox()
    elif browser_name in ["yandex", "ya"]:
        service = Service(
            executable_path=os.path.expanduser("~/Otus/drivers/yandexdriver.exe")
        )
        options = webdriver.ChromeOptions()
        options.binary_location = os.path.expanduser(
            "~/AppData/Local/Yandex/YandexBrowser/Application/browser.exe"
        )
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    driver.logger = logger

    yield driver
    driver.quit()


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
