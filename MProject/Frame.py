import unittest
from appium import webdriver
import base64
import os
import time

class FlipkartTest(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": "D:/Olga/prog/flipkart.apk",
            "appPackage": "com.flipkart.android",
            "appWaitActivity": "com.flipkart.android.activity.MSignupActivity"
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        self.driver.implicitly_wait(30)
        self.driver.start_recording_screen()

    def test_Login(self):
        driver = self.driver

        driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()
        driver.find_element_by_id("com.flipkart.android:id/mobileNo").click()
        driver.implicitly_wait(60)
        driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("1")
        driver.find_element_by_id("com.flipkart.android:id/mobileNo").clear()
        driver.implicitly_wait(30)
        driver.find_element_by_id("com.flipkart.android:id/country_code_info").click()
        driver.find_element_by_id("com.flipkart.android:id/search_country_name").send_keys("canada")
        driver.implicitly_wait(60)
        driver.find_element_by_id("com.flipkart.android:id/country_row_item_full_name").click()
        driver.implicitly_wait(60)
        driver.find_element_by_id("com.flipkart.android:id/mobileNo").clear()
        driver.find_element_by_id("com.flipkart.android:id/mobileNo").send_keys("6475210050")
        driver.implicitly_wait(60)
        driver.find_element_by_id("com.flipkart.android:id/et_password").click()
        driver.find_element_by_id("com.flipkart.android:id/et_password").send_keys("11111o")
        driver.find_element_by_id("com.flipkart.android:id/btn_mlogin").click()
        ts = (time.strftime("%Y_%m_%d_%H%M%S"))
        activityname = driver.current_activity
        filename = activityname+ts

        driver.save_screenshot("D:/Olga/PycharmProjects/Appium1/MProject/Screenshots/" + filename + ".png")

    def tearDown(self):

        video_rawdata = self.driver.stop_recording_screen()
        video_name = self.driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")
        filepath = os.path.join("D:\Olga\PycharmProjects\Appium1\MProject/Video/", video_name + ".mp4")
        with open(filepath, "wb") as vd:
            vd.write(base64.b64decode(video_rawdata))

        #self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
