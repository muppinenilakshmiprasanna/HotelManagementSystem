import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://lakshmiprasannamuppineni.pythonanywhere.com/")
        loginButton = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[3]/li[1]/a").click()
        user = "testuser"
        pwd = "test@123"
        loginEle = driver.find_element_by_id("id_username")
        loginEle.send_keys(user)
        loginEle = driver.find_element_by_id("id_password")
        loginEle.send_keys(pwd)
        loginEle.send_keys(Keys.RETURN)
        assert "Logged In sucessfully"
        time.sleep(1)
        clickOption = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[4]/li/a").click()
        time.sleep(1)
        logout = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[4]/li/ul/li[1]/a").click()
        # select by value

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()