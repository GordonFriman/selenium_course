import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # num1 = browser.find_element_by_id('num1').text
    # num2 = browser.find_element_by_id('num2').text
    # summ = str(int(num1) + int(num2))
    # select = Select(browser.find_element_by_id('dropdown'))
    # select.select_by_value(summ)
    # browser.find_element_by_css_selector('.btn.btn-default').click()
    browser.execute_script("alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


