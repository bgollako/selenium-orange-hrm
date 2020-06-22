from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AddJob(BasePage):

    _field_job_title       = (By.ID, "jobTitle_jobTitle")
    _field_job_description = (By.ID, "jobTitle_jobDescription")
    _field_job_note        = (By.ID, "jobTitle_note")
    _btn_save              = (By.ID, "btnSave")

    URL = 'https://opensource-demo.orangehrmlive.com/index.php/admin/saveJobTitle'

    def __init__(self, driver):
        super().__init__(driver)
        self.load_page(AddJob.URL)


    def add_user(self, title, description, note):
        self.populate_field(AddJob._field_job_title, title)
        self.populate_field(AddJob._field_job_description, description)
        self.populate_field(AddJob._field_job_note, note)
        self.click_btn(AddJob._btn_save)

