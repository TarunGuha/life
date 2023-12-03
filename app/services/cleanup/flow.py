import time
import enum
import logging
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.selenium_webdriver.wedriver import element_finder, initialize_remote_client
from core.config import CLEAN_USER, CLEAN_PASS, LOGIN_PAGE, HOME_PAGE


class Login(enum.Enum):
    USERNAME = '//input[@name="username"]'
    PASSWORD = '//input[@name="password"]'


class Logout(enum.Enum):
    OPTIONS = '//*[@id="mount_0_0_{}"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[3]/span/div/a/div'
    LOGOUT = '//*[@id="mount_0_0_{}"]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[6]/div[1]/div/div/div/div/div'


class Followers(enum.Enum):
    FOLLOWERS = '//*[@id="mount_0_0_{}"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/span/span'
    REMOVE_FOLLOWER = "/html/body/div[{}]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{}]/div/div/div/div[3]/div/div"
    CONFIRM = "/html/body/div[{}]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]"


async def start_cleanup():
    try:
        driver = initialize_remote_client(undetected=False)
        logging.warning("Starting Login Flow")
        driver = await login_user(driver)
        driver = start_removal(driver)
        driver = logout_user(driver)
        driver.quit()
    except:
        logging.warning("Flow -> Error Encountered")
        try:
            driver.quit()
        except:
            pass


async def login_user(driver):
    logging.warning("Login -> Opening Login Page")
    driver.get(LOGIN_PAGE)

    logging.warning("Login -> Entering Username")
    username = element_finder(driver, Login.USERNAME.value)
    username.send_keys(CLEAN_USER)

    logging.warning("Login -> Entering Password")
    password = element_finder(driver, Login.PASSWORD.value)
    password.send_keys(CLEAN_PASS)
    password.send_keys(Keys.ENTER)

    time.sleep(20)
    driver.get(HOME_PAGE)

    time.sleep(10)
    logging.warning("Login -> Login Complete")

    return driver


def div_name_finder(html):
    soup = BeautifulSoup(html, "html.parser")
    divs_by_id = soup.find_all("div", id=True)

    divs = [div["id"] for div in divs_by_id]

    for div in divs:
        if div[0:5] == "mount":
            return div[-2:]

    return False


def start_removal(driver):
    while True:
        divname = div_name_finder(driver.page_source)
        if bool(divname):
            break

    followers = element_finder(driver, Followers.FOLLOWERS.value.format(divname), 60)
    followers.click()

    try:
        for index in range(1, 11, 1):
            unfollow = element_finder(
                driver, Followers.REMOVE_FOLLOWER.value.format(6, index), 60
            )
            unfollow.click()
            confirm = element_finder(driver, Followers.CONFIRM.value.format(6))
            confirm.click()
    except:
        try:
            for index in range(1, 11, 1):
                unfollow = element_finder(
                    driver, Followers.REMOVE_FOLLOWER.value.format(7, index), 60
                )
                unfollow.click()
                confirm = element_finder(driver, Followers.CONFIRM.value.format(7))
                confirm.click()
        except:
            pass

    time.sleep(10)
    return driver


def logout_user(driver):
    logging.warning("Logout -> Starting Logout")
    driver.get(HOME_PAGE)
    time.sleep(5)

    while True:
        divname = div_name_finder(driver.page_source)
        if bool(divname):
            break

    logging.warning("Logout -> Logout Options")
    options = element_finder(driver, Logout.OPTIONS.value.format(divname))
    options.click()
    time.sleep(5)

    logging.warning("Logout -> Logging Out")
    logout = driver.find_element(By.XPATH, Logout.LOGOUT.value.format(divname))
    logout.click()
    time.sleep(10)
    logging.warning("Logout -> Closing Driver")

    return driver
