from base_page import BasePage

class LoginPage(BasePage):

    id_user_name = "txtUsername"
    id_password  = "txtPassword"
    id_login_btn = "btnLogin"

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def login(self):
        self.populate_field_by_id(LoginPage.id_user_name, self.username)
        self.populate_field_by_id(LoginPage.id_password, self.password)
        self.click_btn(LoginPage.id_login_btn)

    def logout(self):
        self.click_link("Logout")