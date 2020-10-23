from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def main():
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10)
        driver.get("https://vk.com/")
        form = driver.find_element_by_id("index_login_form")
        login = form.find_element_by_id("index_email")
        
        #write your emeil or phone
        login.send_keys("*********")
        password = form.find_element_by_id("index_pass")
        
        #write your password
        password.send_keys("*********")
        form.find_element_by_id("index_login_button").click()
        name = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("top_profile_name"))
                                               # .find_element_by_id(“someId”))
        print(driver.current_url)
        # name = driver.find_element_by_class_name("top_profile_name")
        print(name.get_attribute('innerHTML'))


if __name__ == "__main__":
    main()
