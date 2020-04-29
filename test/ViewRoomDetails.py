import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class ViewHotelDetails(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_hotelslist(self):
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
        hotellist = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div/p[2]/a").click()
        assert "View Allhotels List Sucessfully"
        time.sleep(1)
        hoteldetails=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/p[12]/a").click()
        viewimagesofhotel=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[1]/div/a/img").click()
        time.sleep(1)
        viewroomdetails=driver.find_element_by_xpath("/html/body/div[2]/div[2]/p[9]/a").click()
        viewimageofroom = driver.find_element_by_xpath("/html/body/div/div[1]/div/a/img").click()
        time.sleep(1)
        assert "viewed Room Details sucessfully"
        time.sleep(1)
        clickOption = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[4]/li/a").click()
        time.sleep(1)
        logout = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[4]/li/ul/li[1]/a").click()
        # select by value

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()