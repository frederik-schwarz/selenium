from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# text_box.send_keys("this is awsome")
# submit_button.click()

# driver.implicitly_wait(20)

# driver.quit()


def kawsXnike():
    driver.get("https://skyhighfarmuniverse.com/collections/footwear")
    find_shoes = driver.find_element(
        by=By.XPATH, value="//img[contains(@alt, 'CONVERSE')]"
    )
    actions = ActionChains(driver)
    actions.move_to_element(find_shoes)
    actions.click(find_shoes)
    actions.perform()


if __name__ == "__main__":
    kawsXnike()
