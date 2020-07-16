import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_first(self):
        link = " http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('.form-control.first:required')
        input1.send_keys("Smolensk")
        input1 = browser.find_element_by_css_selector('.form-control.second:required')
        input1.send_keys("Smolensk")
        input1 = browser.find_element_by_css_selector('.form-control.third:required')
        input1.send_keys("Smolensk")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector(".btn-default.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", )

    def test_second(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('.form-control.first:required')
        input1.send_keys("Smolensk")
        input1 = browser.find_element_by_css_selector('.form-control.second:required')
        input1.send_keys("Smolensk")
        input1 = browser.find_element_by_css_selector('.form-control.third:required')
        input1.send_keys("Smolensk")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector(".btn-default.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", )


if __name__ == "__main__":
    unittest.main()