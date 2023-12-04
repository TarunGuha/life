import logging
from selenium import webdriver
from fake_useragent import UserAgent
from core.config import SELENIUM_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def element_finder(driver, xpath, wait_time=10):
    waiter = WebDriverWait(driver, wait_time)
    element = waiter.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    return element


def initialize_remote_client(undetected=False):
    logging.warning("Driver -> Initializing The Remote Driver")
    cloud_options = {
        "browser": "Chrome",
        "browser_version": "119.0",
        "os": "Linux",
        "browserstack.local": True,
        "browserstack.debug": True,
    }

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    logging.warning("Driver -> Chrome Options Loaded")

    options.set_capability("cloud:options", cloud_options)
    logging.warning("Driver -> Cloud Options Loaded")

    if undetected:
        logging.warning("Driver -> Loading Fake-User-Agent")
        ua = UserAgent(browsers=["chrome"])
        agent_name = ua.random
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent={agent}".format(agent=agent_name))
        logging.warning("Driver -> Fake-User-Agent Loaded")

    logging.warning("Driver -> Starting The Driver")
    driver = webdriver.Remote(
        command_executor=SELENIUM_URL + "/wd/hub", options=options
    )

    logging.warning("Driver Started Successfully\n")
    logging.warning("View Stream => {link}\n".format(link=SELENIUM_URL + "/ui"))
    return driver
