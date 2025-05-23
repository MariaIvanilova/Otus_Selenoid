import pytest
import datetime
from selenium import webdriver
import logging

default_url = "http://192.168.100.20:8081/"
default_executor = "192.168.100.20"
log_level = "DEBUG"


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser for tests"
    )
    parser.addoption("--bv", action="store", help="browser version")
    parser.addoption("--headless", action="store_true")
    parser.addoption(
        "--mode",
        action="store",
        default="local",
        help="by default local mode, 'remote' - remote mode",
    )
    parser.addoption("--url", action="store", default=default_url)
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--executor", action="store", default=default_executor)


@pytest.fixture
def browser(request):
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test started at %s" % datetime.datetime.now())
    logger.info("===> Test name: %s" % request.node.name)

    mode = request.config.getoption("mode")
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")  # True - False
    browser_version = request.config.getoption("bv")
    vnc = request.config.getoption("vnc")
    executor = request.config.getoption("executor")
    executor_url = f"http://{executor}:4444/wd/hub"

    options = None
    driver = None

    if mode == "remote":
        if browser_name in ["chrome", "ch"]:
            options = webdriver.ChromeOptions()
        elif browser_name in ["firefox", "ff"]:
            options = webdriver.FirefoxOptions()
        elif browser_name in ["edge", "ed"]:
            options = webdriver.EdgeOptions()

        options.set_capability("browserVersion", browser_version)
        options.set_capability("selenoid:options", {"name": request.node.name})
        if vnc:
            options.set_capability("selenoid:options", {"enableVNC": True})

        driver = webdriver.Remote(command_executor=executor_url, options=options)

    else:
        if browser_name in ["chrome", "ch"]:
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless=new")

            driver = webdriver.Chrome(options=options)

        elif browser_name in ["firefox", "ff"]:
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)
        elif browser_name in ["edge", "ed"]:
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Edge(options=options)

    driver.maximize_window()

    driver.logger = logger

    yield driver
    driver.quit()


@pytest.fixture
def url(request):
    return request.config.getoption("--url")
