from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, wait):
        self.wait = wait
        self.logout_button = (By.XPATH, "//android.view.View[@content-desc='Sign Out']/android.widget.Button")

    def logout(self):
        print ("10. Logout:")
        try:
            self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()  # wait for homepage to load
        except:
            self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
