import pymongo
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sqlite3

def init_db():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['testing']
    series_collection = db['msg_from_vk']
    return series_collection

def add_BD(series_collection, name, date, msg):
    # client = pymongo.MongoClient('localhost', 27017)
    # db = client['testing']
    # series_collection = db['msg_from_vk']
    series_collection.insert_one({"data": date, "user": name, "msg": msg}).inserted_id


def last_msg_date(l_msg):
    #time = l_msg.find_element_by_class_name("_im_mess_link")
    #print(time.text)
    date_li = l_msg.find_element_by_tag_name("li")
    date_unix = date_li.get_attribute("data-ts")
    print(date_unix)
    return date_unix

def last_msg_name(l_msg):
    text = l_msg.find_element_by_class_name("im-mess-stack--lnk")
    print(text.text)
    return text.text

def last_msg_text(l_msg):
    text = l_msg.find_element_by_class_name("im-mess--text")
    print(text.text)
    return text.text.lower()

#взвращаетэоемент содержащий текст, фото, имя, дату
def last_msg(driver):
    # WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("im_editable0"))
    last_msg = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[last()]/div[2]')
    # last_msg = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[last()]/div[2]/ul/li/div[3]')
    # print(last_msg.get_attribute('innerHTML'))
    # text = last_msg.find_element_by_class_name("im-mess--text")
    # return last_msg.text.lower()
    # print(text.text)
    return last_msg

def write(driver, text):
    msg_aria = driver.find_element_by_id("im_editable0")
    msg_aria.send_keys(text)

def send(driver):
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/button').click()

# def last_msg(driver):
#     last_msg = driver.find_element_by_xpath('/html/body/div[11]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[last()]/div[2]/ul/li/div[3]')
#     print(last_msg.get_attribute('innerHTML'))
#     return last_msg.text.lower()

def main():
    with webdriver.Chrome() as driver:
        wait = WebDriverWait(driver, 20)
        driver.get("https://vk.com/")
        form = driver.find_element_by_id("index_login_form")
        email = form.find_element_by_id("index_email")
        email.send_keys("89002819280")
        login = form.find_element_by_id("index_pass")
        login.send_keys("vozvrat1202")
        form.find_element_by_id("index_login_button").click()
        name = wait.until(lambda x: x.find_element_by_class_name("top_profile_name"))
                                               # .find_element_by_id(“someId”))
        print(driver.current_url)
        # name = driver.find_element_by_class_name("top_profile_name")
        print(name.get_attribute('innerHTML'))

        #click on message
        driver.find_element_by_id("l_msg").click()
        name_pg = wait.until(lambda x: x.find_element_by_xpath('//span[contains(text(),"Павел Киселев")]'))
        print("i put it")
        #click on user
        print(name_pg)
        time.sleep(2)
        name_pg.click()
        # webdriver.ActionChains(driver).move_to_element(name_pg).click(name_pg).perform()
        # driver.find_element_by_xpath('//span[contains(text(),"Павел Киселев")]').click()
        # driver.find_element_by_xpath('//span[contains(text(),"Павел Киселев")]').click()
        element = wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "html")))
        wait.until(lambda x: x.find_element_by_class_name("im-page--history-new-bar"))



        time.sleep(2)

        # client = pymongo.MongoClient('localhost', 27017)
        # db = client['testing']
        # series_collection = db['msg_from_vk']

        # l_msg = last_msg(driver)
        # l_name = last_msg_name(l_msg)
        # l_date_unix = last_msg_date(l_msg)
        # l_msg_text = last_msg_text(l_msg)
        print("i wait it")
        # time.sleep(2)
        # print(series_collection.insert_one({"data": l_date_unix, "user": l_name, "msg": l_msg_text}).inserted_id)
        series_collection = init_db()
        # add_BD(series_collection, l_name, l_date_unix, l_msg_text)
        # init_BD(l_name, l_date_unix, l_msg)
        # driver.implicitly_wait(10)
        write(driver, "готов")
        send(driver)
        f = 0
        fl = False
        date = 0
        while f<=200:
            l_msg = last_msg(driver)
            l_date_unix = last_msg_date(l_msg)
            l_msg_text = last_msg_text(l_msg)
            l_name = last_msg_name(l_msg)
            if date != l_date_unix & l_name != "Надежда":
                if l_msg_text == "да":
                    write(driver, "ок")
                    send(driver)
                    add_BD(series_collection, l_name, l_date_unix, l_msg_text)
                    l_msg = last_msg(driver)
                    l_name = last_msg_name(l_msg)
                    l_date_unix = last_msg_date(l_msg)
                    l_msg_text = last_msg_text(l_msg)
                    add_BD(series_collection, l_name, l_date_unix, l_msg_text)
                    fl = True
                elif l_msg_text == "нет":
                    write(driver, "хорошо")
                    send(driver)
                    add_BD(series_collection, l_name, l_date_unix, l_msg_text)
                    l_msg = last_msg(driver)
                    l_name = last_msg_name(l_msg)
                    l_date_unix = last_msg_date(l_msg)
                    l_msg_text = last_msg_text(l_msg)
                    add_BD(series_collection, l_name, l_date_unix, l_msg_text)
                    fl = True
                else:
                    add_BD(series_collection, l_name, l_date_unix, l_msg_text)
                date = l_date_unix

                # else:
                #     write("что?")
            time.sleep(2)
            if fl:
                f += 1
        #
        # driver.implicitly_wait(10)


        #screenshot
        #driver.save_screenshot('./image.png')



if __name__ == "__main__":
    main()
