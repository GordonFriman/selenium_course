# import pytest
# from selenium import webdriver
#
# link = "http://selenium1py.pythonanywhere.com/"
#
#
# @pytest.fixture
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
# @pytest.fixture(autouse=True)
# def prepare_data():
#     print()
#     print("preparing some critical data for every test")
#
#
# class TestMainPage1():
#     def test_guest_should_see_login_link(self, browser):
#         # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#
#     def test_guest_should_see_basket_link_on_the_main_page(self, browser):
#         browser.get(link)
#         browser.find_element_by_css_selector(".basket-mini .btn-group > a")


import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        pass
        # какие-то проверки

    def test_second_smiling_faces(self, prepare_faces):
        pass
        # какие-то проверки