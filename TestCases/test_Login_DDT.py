import pytest

from PageObjects.Login import Login
from utilities import xlutiles
from utilities.Logger import Loggenrator
from utilities.readproperties import Readconfig
import allure
from allure_commons.types import AttachmentType


class Test_LoginPage:
    url = Readconfig.geturl()
    Log = Loggenrator.Logen()
    path = "C:\\CuraHeathcare\\TestCases\\TestData\\Logindata.xlsx"


    @pytest.mark.sanity
    @allure.link("https://katalon-demo-cura.herokuapp.com/")
    @allure.description("This test case performing functionality of login test case")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login002(self,setup):
       self.Log.info("TestCase002 is started")
       self.driver = setup
       self.Log.info("opening browser")
       self.LP = Login(self.driver)
       self.Log.info("Going To url")
       self.driver.get(self.url)
       self.Rows = xlutiles.getrowcount(self.path, "Sheet1")
       print("No of Rows--->" + str(self.Rows))

       status_list=[]
       for r in range(2,self.Rows+1):
           self.username=xlutiles.readdata(self.path,"Sheet1", r , 2)
           self.password=xlutiles.readdata(self.path,"Sheet1", r , 3)
           self.Expected_Result = xlutiles.readdata(self.path,"Sheet1",r,4)
           self.Log.info("click On make Appoinment")
           self.LP.Click_on_Make_appointment()
           self.Log.info("Enter Username")
           self.LP.Enter_Username(self.username)
           self.Log.info("Enter Password")
           self.LP.Enter_password(self.password)
           self.Log.info("Click on Login Button")
           self.LP.Click_On_Login_Button()
           if self.driver.title == "CURA Healthcare Service":
               if  self.Expected_Result == "Pass":
                   self.Log.info("Page Titile-->" + str(self.driver.title))
                   self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+self.username+self.password+"ScreenShotTestCase002_Pass.PNG")
                   # allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",AttachmentType=AttachmentType.PNG)
                   self.LP.click_On_Menu_Button()
                   self.Log.info("Click On Logout Button")
                   self.LP.Click_On_Logout_Button()
                   status_list.append("Pass")
                   xlutiles.writedata(self.path,"Sheet1",r,5,"Pass")

               elif self.Expected_Result == "Fail":
                   self.Log.info("Page Titile--->" + str(self.driver.title))
                   self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+self.username+self.password+"ScreenShotTestCase002_Fail.PNG")
                   # allure.attach(self.driver.get_screenshot_as_png(),name="Screenshot",attachment_type=AttachmentType.PNG)
                   status_list.append("Fail")
                   xlutiles.writedata(self.path,"Sheet1",r,5,"Pass")



           else:
               if  self.Expected_Result == "Pass":
                   self.Log.info("Page Titile-->" + str(self.driver.title))
                   self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+self.username+self.password+"ScreenShot_TestCase002_Pass.PNG")
                   # allure.attach(self.driver.get_screenshot_as_png(),name="Screenshot",AttachmentType=AttachmentType.PNG)
                   self.Log.info("Test_case002 is Failed")
                   status_list.append("Pass")
                   xlutiles.writedata(self.path,"Sheet1",r,5,"Pass")



               elif self.Expected_Result == "Fail":
                   self.Log.info("Page Titile-->" + str(self.driver.title))
                   self.Log.info("Saving screenshot Test case 002")
                   self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+self.username+self.password+"ScreenShoTestCase002_Fail.PNG")
                   # allure.attach(self.driver.get_screenshot_as_png(),name="screenshot",AttachmentType=AttachmentType.PNG)
                   self.Log.info("Test_case002 is Failed")
                   status_list.append("Pass")
                   xlutiles.writedata(self.path,"Sheet1",r,5,"Pass")

               if "Fail" not in status_list:
                   assert True
                   self.Log.info("Test case 002 is Passed")

               else:
                   assert False
                   self.Log.info("Test case 002 is Failed")

               self.Log.info("Test case 002 is completed")




        


