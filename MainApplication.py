# Import pages
from LoginPage import LoginPage
from ProjectPage import ProjectPage
from VideoPlayerPage import VideoPlayerPage
from LogoutPage import LogoutPage

# Import necessary libraries
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",                                # Platform name
	"appium:platformVersion": "13.0",                         # Version of the Android device
	"appium:deviceName": "emulator-5554",                     # physical/emulator device name
	"appium:automationName": "UIAutomator2",                  # Automation name
	"appium:app": "hfiPevjjJ1DgrIGU5G3n.apk",                 # path to the APK 
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options) # connect to appium server

wait = WebDriverWait(driver, 30)

# Initialize page objects
login_page = LoginPage(wait)
project_page = ProjectPage(wait)
video_player_page = VideoPlayerPage(wait)
logout_page = LogoutPage(wait)

# Perform actions
login_page.enter_pin("WVMVHWBS")
login_page.click_login()

project_page.navigate_to_project()
project_page.switch_to_details_tab()
project_page.switch_to_videos_tab()

video_player_page.play_video()
video_player_page.pause_video(driver)
video_player_page.resume_video()
video_player_page.set_volume(driver)
video_player_page.change_resolution(driver)
video_player_page.pause_video(driver)
video_player_page.navigate_back()

logout_page.logout()
driver.quit()
