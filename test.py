from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
    select_element = driver.find_element(
        by=By.XPATH, value="//select[contains(@name, 'options')]"
    )
    actions.move_to_element(select_element)
    select = Select(select_element)
    select.select_by_index(3)
    # select.select_by_value(" MEN'S 10 / WOMAN'S 12 ")
    # print(size)
    actions.perform()
    find_add_to_cart = driver.find_element(
        by=By.XPATH, value="//button[contains(@name, 'add')]"
    )
    actions.move_to_element(find_add_to_cart)
    actions.click(find_add_to_cart)
    actions.perform()

    go_to_cart = driver.find_element(by=By.XPATH, value="//a[contains(@id, 'cart')]")
    actions.move_to_element(go_to_cart)
    actions.click(go_to_cart)
    actions.perform()


if __name__ == "__main__":
    kawsXnike()
