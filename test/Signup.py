import unittest
import time
from selenium import webdriver



class Signup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_signup(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://lakshmiprasannamuppineni.pythonanywhere.com/")
        signupLink = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[3]/li[2]/a").click()
        username = driver.find_element_by_id("id_username")
        username.send_keys("testuser")
        time.sleep(1)
        Email = driver.find_element_by_id("id_email")
        Email.send_keys("lpmuppineni@unomaha.edu")
        time.sleep(1)
        first_name = driver.find_element_by_id("id_first_name")
        first_name.send_keys("test First Name")
        time.sleep(1)
        last_name = driver.find_element_by_id("id_last_name")
        last_name.send_keys("test Last Name")
        time.sleep(1)
        password1 = driver.find_element_by_id("id_password1")
        password1.send_keys("test@123")
        time.sleep(1)
        password2 = driver.find_element_by_id("id_password2")
        password2.send_keys("test@123")
        time.sleep(1)
        signUpButton = driver.find_element_by_xpath(
            "/html/body/form/button").click()
        time.sleep(1)
        assert "Sucessfully user created"
        time.sleep(1)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()