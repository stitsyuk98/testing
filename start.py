from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def write(driver, text):
    msg_aria = driver.find_element_by_id("im_editable0")
    msg_aria.send_keys(text)

def send(driver):
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/button').click()

def last_msg(driver):
    last_msg = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[last()]/div[2]/ul/li/div[3]')
    print(last_msg.get_attribute('innerHTML'))
    return last_msg.text.lower()

def main():
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 10)
        driver.get("https://vk.com/")
        form = driver.find_element_by_id("index_login_form")
        email = form.find_element_by_id("index_email")
        email.send_keys("*******")
        login = form.find_element_by_id("index_pass")
        login.send_keys("*************")
        form.find_element_by_id("index_login_button").click()
        name = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_class_name("top_profile_name"))
                                               # .find_element_by_id(“someId”))
        print(driver.current_url)
        # name = driver.find_element_by_class_name("top_profile_name")
        print(name.get_attribute('innerHTML'))

        #click on message
        driver.find_element_by_id("l_msg").click()
        name_pg = WebDriverWait(driver, 10).until(lambda x: x.find_elements_by_xpath('//span[contains(text(),"Павел Киселев")]'))

        #click on user
        driver.find_element_by_xpath('//span[contains(text(),"Павел Киселев")]').click()
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("im_editable0"))

        driver.implicitly_wait(10)



        # driver.find_element_by_id("im_editable0").send_keys("я готов")

        # f = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[25]/div[2]/ul/li')
        # last_msg = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[last()]/div[2]/ul/li/div[3]')
        # print(last_msg.get_attribute('innerHTML'))

        # msg_aria = driver.find_element_by_id("im_editable0")
        # msg_aria.send_keys("давай попробуем")

        # msg_text = last_msg.text.lower()
        # WebDriverWait.until(expected_conditions.text_to_be_present_in_element(By.XPATH('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[19]/div[2]/ul/li/div[3]'), ""))
        # if msg_text !="":
        #     if msg_text == "да":
        #         msg_aria.send_keys("ок")
        #     elif msg_text == "нет":
        #         msg_aria.send_keys("хорошо")

        f = 0
        fl = False
        while f<=6:
            last_msg = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[last()]/div[2]/ul/li/div[3]')
            print(last_msg.get_attribute('innerHTML'))
            m = last_msg.text.lower()
            if m == "да":
                write(driver, "ок")
                send(driver)
                fl = True
            elif m == "нет":
                write(driver, "хорошо")
                send(driver)
                fl = True
            # else:
            #     write("что?")
            time.sleep(30)
            if fl:
                f += 1

        # driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/button').click()
        # print(btn_msg.text)
        driver.implicitly_wait(10)

        # last_msg = all_msg.find_element_by_class_name("im-mess--text")
        # print(last_msg.get_attribute('innerHTML'))

        #screenshot
        #driver.save_screenshot('./image.png')



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
