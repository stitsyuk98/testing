from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def main():
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10)
        driver.get("https://vk.com/")
        form = driver.find_element_by_id("index_login_form")
        email = form.find_element_by_id("index_email")
        email.send_keys("89002819280")
        login = form.find_element_by_id("index_pass")
        login.send_keys("vozvrat1202")
        form.find_element_by_id("index_login_button").click()
        name = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("top_profile_name"))
                                               # .find_element_by_id(“someId”))
        print(driver.current_url)
        # name = driver.find_element_by_class_name("top_profile_name")
        print(name.get_attribute('innerHTML'))


if __name__ == "__main__":
    main()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import presence_of_element_located
#
# #This example requires Selenium WebDriver 3.13 or newer
# with webdriver.Chrome() as driver:
#     wait = WebDriverWait(driver, 10)
#     driver.get("https://google.com/ncr")
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
#     first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>span")))
#     print(first_result.get_attribute("textContent"))

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# # Navigate to url
# driver.get("http://www.google.com")
#
# # Store 'google search' button web element
# searchBtn = driver.find_element(By.LINK_TEXT, "Мне повезёт!")
#
# # Perform context-click action on the element
# webdriver.ActionChains(driver).context_click(searchBtn).perform()
