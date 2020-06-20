from pages.login_page import LoginPage
from time import sleep

def main():
    page = LoginPage("Admin", "admin123")
    page.login()
    sleep(20)
    page.logout()

if __name__ == '__main__':
    main()