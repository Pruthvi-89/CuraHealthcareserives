import pytest

from PageObjects.Login import Login
from utilities.Logger import Loggenrator
from utilities.readproperties import Readconfig


class Test_LoginPagetitile():
    url = Readconfig.geturl()
    Log = Loggenrator.Logen()

    @pytest.mark.regression
    def test_LoginPagetitl001(self,setup):
        self.Log.info("Test Case 001 is started")
        self.driver = setup
        self.Log.info("Opening Browser")
        self.Log.info("Goining To url"+self.url)
        self.driver.get(self.url)
        self.Log.info("Printing Titile")
        print(self.driver.title)
        if self.driver.title=="CURA Healthcare Service":
            self.Log.info("Saving ScreenShot")
            self.driver.save_screenshot("C:\CuraHeathcare\ScreenShots\\TestCasePageTitile001_Pass.PNG")
            self.Log.info("Test case 001 is Passed")
            assert True
        else:
            self.Log.info("Saving screenshot for Failed Test case 001")
            self.driver.save_screenshot("C:\CuraHeathcare\ScreenShots\\TestCasePageTitile001_Fail.PNG")
            self.Log.info("Test Case 001 is Failed")
            assert False
            self.Log.info("Test case 001 is Completed")







