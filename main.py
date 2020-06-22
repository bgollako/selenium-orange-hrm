from pages.login_page import LoginPage
from pages.add_job import AddJob
from selenium.webdriver import Chrome
from test_data import credentials, job_details, invalid_credentials
from time import sleep

def main():
    driver = Chrome()
    loginPage = LoginPage(driver)
    loginPage.invalid_login(**invalid_credentials)
    loginPage.valid_login(**credentials)
    loginPage.logout()

if __name__ == '__main__':
    main()