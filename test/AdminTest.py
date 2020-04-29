import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys



class Admintest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://lakshmiprasannamuppineni.pythonanywhere.com/")
       loginButton = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[3]/li[1]/a").click()
       loginEle = driver.find_element_by_id("id_username")
       loginEle.send_keys(user)
       loginEle = driver.find_element_by_id("id_password")
       loginEle.send_keys(pwd)
       loginEle.send_keys(Keys.RETURN)
       assert "Logged In sucessfully"
       time.sleep(1)
       assert "Logged In"
       driver.get("http://lakshmiprasannamuppineni.pythonanywhere.com/admin")
       hotels=driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/th").click()
       time.sleep(1)
       addhotel=driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
       hotelele=driver.find_element_by_id("id_Name")
       hotelele.send_keys("Hotel Lakewood")
       hotelele = driver.find_element_by_id("id_Description")
       hotelele.send_keys("It is located at 120 the Dodge street, it is sorrounded by beautiful candlewood lake")
       hotelele=driver.find_element_by_id("id_Amenities")
       hotelele.send_keys("WiFi,24-hours Room Service,Parking,Fridge,Air conditioner,King Sized Bed ,Parking")
       hotelele=driver.find_element_by_id("id_Address")
       hotelele.send_keys("121 Rose lane ")
       hotelele = driver.find_element_by_id("id_City")
       hotelele.send_keys("Omaha")
       hotelele = driver.find_element_by_id("id_Country")
       hotelele.send_keys("USA")
       hotelele = driver.find_element_by_id("id_state")
       hotelele.send_keys("Nebraska")
       hotelele = driver.find_element_by_id("id_zipcode")
       hotelele.send_keys("68154")
       hotelele=driver.find_element_by_id("id_TelephoneNumber")
       hotelele.send_keys("4029064789")
       savebutton=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div[2]/input[1]").click()
       assert "Hotel Added sucessfully"
       time.sleep(1)
       driver.get("http://lakshmiprasannamuppineni.pythonanywhere.com/admin")
       hotels = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/th").click()
       time.sleep(1)
       addroom=driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
       roomele=driver.find_element_by_id("id_hotel")
       roomele.select_by_visible_text('Hotel Lakewood')
       roomele=driver.find_element_by_id("id_RoomNumber")
       roomele.send_keys("101")
       roomele = driver.find_element_by_id("id_RoomType")
       roomele.send_keys("Single King Bed")
       roomele = driver.find_element_by_id("id_Capacity")
       roomele.send_keys("2")
       roomele = driver.find_element_by_id("id_BedOption")
       roomele.send_keys("King Bed")
       roomele = driver.find_element_by_id("id_Amenities")
       roomele.send_keys("Wifi,Fridge,Air Conditioner,TV,Attached Bathroom")
       roomele = driver.find_element_by_id("id_Price")
       roomele.send_keys("60")
       save=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       assert "Room Added sucessfully"
       time.sleep(1)
       driver.get("http://lakshmiprasannamuppineni.pythonanywhere.com/admin")
       logoutoption=driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a[3]").click()
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()