import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class Forgotpassword(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_resetpassword(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://lakshmiprasannamuppineni.pythonanywhere.com/")
       loginLink = driver.find_element_by_xpath ("/html/body/nav/div/div[2]/ul[3]/li[1]/a").click()
       time.sleep(1)
       forgotPwdLink = driver.find_element_by_xpath ("/html/body/p/a").click()
       time.sleep(1)
       username = driver.find_element_by_id("id_email")
       username.send_keys("lpmuppineni@unomaha.edu")
       time.sleep(1)
       sendEmailButton = driver.find_element_by_xpath("/html/body/form/p[2]/input").click()
       time.sleep(1)
       assert "Mail Sent for resetting password"

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()