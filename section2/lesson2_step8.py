import time
from selenium import webdriver
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('Firstname')
    browser.find_element_by_name('lastname').send_keys('Lastname')
    browser.find_element_by_name('email').send_keys('email@email.ru')
    browser.find_element_by_id('file').send_keys(os.path.join(os.path.abspath(os.path.dirname(__file__)), '1.txt'))
    browser.find_element_by_css_selector('.btn.btn-primary').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
