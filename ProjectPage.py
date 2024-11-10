from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectPage:
    def __init__(self, wait):
        self.wait = wait
        self.videos_tab = (By.XPATH, "//android.view.MenuItem[@text='Videos']")
        self.all_titles_button = (By.XPATH, "//android.widget.TextView[@text='All Titles']")
        self.project_button = (By.XPATH, "//android.view.View[@content-desc='Title - Test automation project, ']")
        self.details_tab= (By.XPATH, "//android.view.MenuItem[@text='Details']")

    def navigate_to_project(self):
        print ("2. Navigate to the 'Test Automation Project':")
        self.wait.until(EC.element_to_be_clickable(self.all_titles_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.project_button)).click()

    def switch_to_details_tab(self):
        print ("3. Switch to the 'Details' Tab:")
        self.wait.until(EC.element_to_be_clickable(self.details_tab)).click()

    def switch_to_videos_tab(self):
        print("4. Return to the 'Videos' Tab:")
        self.wait.until(EC.element_to_be_clickable(self.videos_tab)).click()
