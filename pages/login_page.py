from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):

    _field_user_name = (By.ID,"txtUsername")
    _field_password  = (By.ID, "txtPassword")
    _field_login = (By.ID, "btnLogin")
    _link_logout = (By.LINK_TEXT, "Logout")
    _invalid_creds_banner = (By.ID, "spanMessage")

    _invalid_login_url = "https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials"
    _invalid_login_msg = "Invalid credentials"

    _valid_login_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"
    _valid_menu = (By.ID, "mainMenu")

    URL = "https://opensource-demo.orangehrmlive.com/"


    def __init__(self, driver):
        super().__init__(driver)
        self.load_page(LoginPage.URL)

    def invalid_login(self, username, password):
        self.populate_field(LoginPage._field_user_name, username)
        self.populate_field(LoginPage._field_password, password)
        self.click_btn(LoginPage._field_login)
        span_element = EC.presence_of_element_located(LoginPage._invalid_creds_banner)
        WebDriverWait(self.driver, 10).until(span_element)
        assert self.get_page_url() == LoginPage._invalid_login_url
        assert self.get_field(LoginPage._invalid_creds_banner).text == LoginPage._invalid_login_msg

    def valid_login(self, username, password):
        self.populate_field(LoginPage._field_user_name, username)
        self.populate_field(LoginPage._field_password, password)
        self.click_btn(LoginPage._field_login)
        wait_element = EC.presence_of_element_located(LoginPage._valid_menu)
        WebDriverWait(self.driver, 10).until(wait_element)
        assert self.get_page_url() == LoginPage._valid_login_url

    def logout(self):
        self.click_link(LoginPage._link_logout)