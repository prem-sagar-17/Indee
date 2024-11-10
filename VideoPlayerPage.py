from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class VideoPlayerPage:
    def __init__(self, wait):
        self.wait = wait
        self.play_button = (By.XPATH, "//android.widget.Button[@text='Play Video']")
        self.pause_button = (By.XPATH, "//android.widget.Button[@text='Pause']")
        self.player_controls = (By.XPATH, "//android.view.MenuItem[@text='Videos']")
        self.continue_button = (By.XPATH, "//android.widget.Button[@text='Continue Watching']")
        self.resolution_button = (By.XPATH, "///android.widget.Button[@text='Settings']")
        self.resolution_480p = (By.XPATH, "//android.view.MenuItem[@text='480p']")
        self.resolution_720p = (By.XPATH, "//android.view.MenuItem[@text='720p']")
        self.back_button = (By.XPATH, "//android.widget.Button[@text='Go Back and continue playing video']")

    def play_video(self, driver):
        print ("5. Play the Video:")
        self.wait.until(EC.element_to_be_clickable(self.play_button)).click()
        driver.implicitly_wait(10)  # wait for the 10 seconds video playback

    def pause_video(self, driver):
        try:
            self.wait.until(EC.element_to_be_clickable(self.pause_button)).click()
        except:
            driver.tap([(724, 1592)])  # tap anywhere on the screen to make the player controls visible
            self.wait.until(EC.element_to_be_clickable(self.pause_button)).click()

    def resume_video(self):
        print ("6. Replay the Video using the 'Continue Watching' button:")
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()

    def set_volume(self, driver):
        print ("7. Adjust Volume:")
        for _ in range(15):
            driver.press_keycode(24)  # set the device volume to MAX (VOLUME_UP KEY PRESS)
        for _ in range(7):
            driver.press_keycode(25)  # set the device volume to 50% (VOLUME_DOWN KEY PRESS)

    def change_resolution(self, driver):
        print ("8. Change Video Resolution:")
        try:
            self.wait.until(EC.element_to_be_clickable(self.resolution_480p)).click()
        except:
            driver.tap([(724, 1592)])  # tap anywhere on the screen to make the player controls visible
            self.wait.until(EC.element_to_be_clickable(self.resolution_button)).click() # pressing the setting button pauses the screen
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()   # pressing the continue button to resume playback
        self.wait.until(EC.element_to_be_clickable(self.resolution_480p)).click()  # press the 480p resolution button

        try:
            self.wait.until(EC.element_to_be_clickable(self.resolution_720p)).click()
        except:
            driver.tap([(724, 1592)])  # tap anywhere on the screen to make the player controls visible
            self.wait.until(EC.element_to_be_clickable(self.resolution_button)).click() # pressing the setting button pauses the screen
        self.wait.until(EC.element_to_be_clickable(self.continue_button)).click()   # pressing the continue button to resume playback
        self.wait.until(EC.element_to_be_clickable(self.resolution_720p)).click()  # press the 720p resolution button

    def navigate_back(self):
        print ("9. Pause and Exit:")
        self.wait.until(EC.element_to_be_clickable(self.back_button)).click()
