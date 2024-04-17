import time

import pytest

from PageObjects.Book_Appoinment import Book_Appoinment
from PageObjects.Login import Login
from utilities.Logger import Loggenrator
from utilities.readproperties import Readconfig


class Test_Book_Appoinment:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    Log= Loggenrator.Logen()

    @pytest.mark.sanity
    def test_Book_Appoinment003(self,setup):
        self.Log.info("Test case 003 is started")
        self.driver = setup
        self.Log.info("Opening browser")
        self.driver.get(self.url)
        self.Log.info("Going to url"+self.url)
        self.LP = Login(self.driver)
        self.Log.info("click on make appoinment")
        self.LP.Click_on_Make_appointment()
        self.Log.info("Entering username"+self.username)
        self.LP.Enter_Username(self.username)
        self.Log.info("Entering password"+self.password)
        self.LP.Enter_password(self.password)
        self.Log.info("click on Login Button")
        self.LP.Click_On_Login_Button()
        self.Log.info("Book Appoinment")
        self.BA = Book_Appoinment(self.driver)
        self.Log.info("Entering Center Name")
        self.BA.select_DropDown("Hongkong CURA Healthcare Center")
        self.Log.info("Entering Facility")
        self.BA.select_Facilities("Medicare")
        self.Log.info("Entering Date")
        self.BA.Enter_Date("16/4/2024")
        self.Log.info("Entering Comment")
        self.BA.Add_Comment("Book Appoinment Sucessfully")
        self.Log.info("Clic on Book Appoinment")
        self.BA.click_On_Bookappoinment()
        if self.driver.title=="CURA Healthcare Service":
            self.Log.info("Saving ScreenShot Pass Test case 003")
            self.driver.save_screenshot("C:\CuraHeathcare\ScreenShots\\"+self.username+self.password+"TestCasePageTitile003_Pass.PNG")
            self.Log.info("Click on HomePage Button")
            self.BA.click_On_HomePage()
            self.Log.info("click On Menu Button")
            self.LP.click_On_Menu_Button()
            self.Log.info("click On Logout Button")
            self.LP.Click_On_Logout_Button()
            assert True
            self.Log.info("Test case 003 is passed")

        else:
            self.Log.info("save Screenshot For Fail test case003")
            self.driver.save_screenshot("C:\CuraHeathcare\ScreenShots\\"+self.username+self.password+"TestCasePageTitile003_Fail.PNG")
            self.Log.info("Test case 003 is Failed")
            assert False
            self.Log.info("Test case 003 is completed")


