from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

bot_timeout = time.time() + 60 * 5  # x minutes from now

while True:
    available_item_list = []
    # Click on the cookie for 5 seconds
    click_timeout = time.time() + 5
    cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")
    while time.time() < click_timeout:
        cookie.click()
    # Check the store item and add available items to a list
    store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
    available_item_list = [item for item in store_items if item.text != "" and item.get_attribute("class") != "grayed"]

    # Get the most expensive item in store that is the last one on the list
    available_item_list[-1].click()

    if time.time() > bot_timeout:
        break

cps = driver.find_element(by=By.ID, value="cps")
print(f"Cookie per second: {cps.text}")