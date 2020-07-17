from selenium import webdriver
import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link_list = ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1']


# link_list = ['https://stepik.org/lesson/236895/step/1']


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


@pytest.mark.parametrize('link', link_list)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)
    text_area = browser.find_element_by_css_selector('.textarea.string-quiz__textarea.ember-text-area.ember-view')
    text = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '.textarea.string-quiz__textarea.ember-text-area.ember-view'), '')
    )
    text_area.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_css_selector('.submit-submission')
    click = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.submit-submission'))
    )
    button.click()
    answer = browser.find_element_by_css_selector('.smart-hints__hint').text
    print(answer)
    assert answer == 'Correct!', f'Что то пошло не так! Получаем сообщение: {answer}'
