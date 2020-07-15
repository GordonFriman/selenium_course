import re
import time

from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script(
        "document.getElementsByTagName('button')[0].classList.remove('trollface');")  # Этот метод запускает скрипт который удаляет класс trollface у элемента
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    browser.find_element_by_id('answer').send_keys(calc(browser.find_element_by_id('input_value').text))
    browser.find_element_by_css_selector('.btn.btn-primary').click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    text = re.findall("(?:Congrats, you've passed the task! Copy this code as the answer to Stepik quiz:\s)(.*)",
                      alert_text)
    print(text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта

    # закрываем браузер после всех манипуляций
    browser.quit()
