from selenium.webdriver.common.by import By


def test_example_ya(browser):
    browser.get("https://www.google.com/")
    browser.find_element(By.XPATH, '(//input[contains(@aria-label, "Мне повезёт")])[2]').click()
    assert browser.current_url == "https://doodles.google/"
