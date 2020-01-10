from selenium import webdriver
import time

url = 'https://meta.ua'
handle = open("test.txt", "r")
data = handle.readline()
while data:   
    print(data)
    parsed_list = data.split(' ')
    print(parsed_list)
    first_name = parsed_list[0]
    last_name = parsed_list[1]
    login = parsed_list[2]
    password = parsed_list[3]
    birth_date = parsed_list[4]
    print("first name = " + first_name + "\n" + "last name = " + last_name + "\n" + "login = " + login + "\n" + "password " + password + "\n" + "date = " + birth_date)
    data = handle.readline()
    driver = webdriver.Chrome(executable_path='C:\Windows\chromedriver.exe')
    driver.get(url)
    driver.find_element_by_class_name('mail-sign-up').click()
    time.sleep(0)
    driver.find_element_by_name('46b81dfd31f4880e80cb891168ed0a8f').send_keys(first_name)
    time.sleep(0)
    driver.find_element_by_name('406712c1882e6ef726db1283b6d777d2').send_keys(last_name)
    time.sleep(0)
    driver.find_element_by_name('d7e358025935718766b34974a5a52162').send_keys(login)
    time.sleep(0)
    driver.find_element_by_name('dea167d18dd51ea2853d23d095779ee1').send_keys(password)
    time.sleep(0)
    driver.find_element_by_name('ac5760dde5ec8d4f8447d094e02fb879').send_keys(password)
    time.sleep(0)
    driver.find_element_by_id('register_btn').click()
    time.sleep(1)
    driver.find_element_by_id('birthday').send_keys(birth_date)
    driver.find_element_by_class_name('ui-datepicker-trigger').click()
    time.sleep(1)
    driver.find_element_by_name('register_email').click()
    time.sleep(0)
    driver.find_element_by_id('second_email').send_keys('olegklimov@ukr.net')
    time.sleep(0)
    driver.find_element_by_id('own_check_quest').send_keys('ДІВОЧЕ ПРІЗВИЩЕ МАТЕРІ')
    time.sleep(0)
    driver.find_element_by_id('check_answer').send_keys('клімук')
    time.sleep(0)
    driver.find_element_by_id('register_btn').click()
    time.sleep(2)
    driver.quit()
handle.close()
