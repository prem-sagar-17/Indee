from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, wait):
        self.wait = wait
        self.pin_field = (By.XPATH, "//android.widget.EditText")
        self.login_button = (By.XPATH, "//android.widget.Button[@text='Sign In']")

    def enter_pin(self, pin):
        print ("1. Sign in to the Platform.")
        self.wait.until(EC.presence_of_element_located(self.pin_field)).send_keys(pin)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()