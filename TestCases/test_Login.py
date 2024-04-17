import allure
import pytest

from PageObjects.Login import Login
from utilities.Logger import Loggenrator
from utilities.readproperties import Readconfig


class Test_LoginPage:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    Log = Loggenrator.Logen()


    @pytest.mark.Regression
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("https://katalon-demo-cura.herokuapp.com/")
    @allure.description("These Funtionality perofrm login functionality of webpage")
    @allure.story("Valid credetial")
    @allure.title("Login page Titile")
    def test_Login002(self,setup):
       self.Log.info("TestCase002 is started")
       self.driver = setup
       self.Log.info("opening browser")
       self.LP = Login(self.driver)
       self.Log.info("Going To url")
       self.driver.get(self.url)
       self.Log.info("click On make Appoinment")
       self.LP.Click_on_Make_appointment()
       self.Log.info("Enter Username")
       self.LP.Enter_Username(self.username)
       self.Log.info("Enter Password")
       self.LP.Enter_password(self.password)
       self.Log.info("Click on Login Button")
       self.LP.Click_On_Login_Button()
       self.Log.info("Titile is visible")
       if self.driver.title == "CURA Healthcare Service":
           self.Log.info("Saving screenshot for passed Test case002")
           self.driver.save_screenshot("C:\CuraHeathcare\ScreenShots\\"+self.username+self.password+"TestCaseLogin002_Pass.PNG")
           self.Log.info("click On Menu Button")
           self.LP.click_On_Menu_Button()
           self.Log.info("Click On Logout Button")
           self.LP.Click_On_Logout_Button()
           assert True
           self.Log.info("Test case 002 Is passed")
       else:
           self.Log.info("Saving screenshot Test case 002")
           self.driver.get_screenshot_as_png("C:\CuraHeathcare\ScreenShots\\"+self.username+self.password+"TestCasePageLogine002_Fail.PNG")
           self.Log.info("Test_case002 is Failed")
           assert False
           self.Log.info("Test case 002 is completed")



        


