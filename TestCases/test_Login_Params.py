import time

import allure
import pytest
from allure_commons.types import AttachmentType

from PageObjects.Login import Login
from utilities.Logger import Loggenrator
from utilities.readproperties import Readconfig


class Test_LoginPage:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    Log = Loggenrator.Logen()



    @pytest.mark.sanity
    def test_Login002(self,setup,getdataforlogin):
       self.Log.info("TestCase002 is started")
       self.driver = setup
       self.Log.info("opening browser")
       self.LP = Login(self.driver)
       self.Log.info("Going To url")
       self.driver.get(self.url)
       self.Log.info("click On make Appoinment")
       self.LP.Click_on_Make_appointment()
       self.Log.info("Enter Username")
       self.LP.Enter_Username(getdataforlogin[0])
       self.Log.info("Enter Password")
       self.LP.Enter_password(getdataforlogin[1])
       self.Log.info("Click on Login Button")
       self.LP.Click_On_Login_Button()
       self.Log.info("Titile is visible")
       status_list=[]
       if self.driver.title == "CURA Healthcare Service":
           if getdataforlogin[2]=="Pass":
             self.Log.info("Page Titile-->"+str(self.driver.title))
             self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+getdataforlogin[0]+"TestCase002_Pass.PNG")
             allure.attach(self.driver.get_screenshot_as_png(),name="Screenshot",attachment_type=AttachmentType.PNG)
             self.LP.click_On_Menu_Button()
             self.Log.info("Click On Logout Button")
             self.LP.Click_On_Logout_Button()
             status_list.append("Pass")

           elif  getdataforlogin[2]=="Fail":
                 self.Log.info("Page Titile--->"+str(self.driver.title))
                 self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+getdataforlogin[0] +"TestCase002_Fail.PNG")
                 allure.attach(self.driver.get_screenshot_as_png(), name="screenShot",attachment_type=AttachmentType.PNG)
                 status_list.append("Fail")


       else:
            if getdataforlogin[2]=="Pass":
              self.Log.info("Page Titile-->"+str(self.driver.title))
              self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+getdataforlogin[0]+"TestCase002_Pass.PNG")
              allure.attach(self.driver.get_screenshot_as_png(), name="screenShot", attachment_type=AttachmentType.PNG)
              self.Log.info("Test_case002 is Failed")
              status_list.append("Pass")


            elif getdataforlogin[2]=="Fail":
                self.Log.info("Page Titile-->"+str(self.driver.title))
                self.Log.info("Saving screenshot Test case 002")
                self.driver.save_screenshot("C:\\CuraHeathcare\\ScreenShots\\"+getdataforlogin[0]+"TestCase002_Fail.PNG")
                allure.attach(self.driver.get_screenshot_as_png(), name="screenShot",attachment_type=AttachmentType.PNG)
                self.Log.info("Test_case002 is Failed")
                status_list.append("Pass")


            if "Fail" not in status_list:
                assert True
                self.Log.info("Test case 002 is Passed")

            else:
                assert False
                self.Log.info("Test case 002 is Failed")

            self.Log.info("Test case 002 is completed")



