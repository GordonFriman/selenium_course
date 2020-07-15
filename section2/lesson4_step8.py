import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_id('book')
    cost = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    button.click()
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    print(browser.find_element_by_id('input_value').text)
    print(calc(browser.find_element_by_id('input_value').text))
    button1 = browser.find_element_by_id('solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)",
                      alert_text)
    print(text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


