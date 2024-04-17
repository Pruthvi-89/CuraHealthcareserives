from select import select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Book_Appoinment():

    Text_Select_Center_XPATH=(By.XPATH,"(//select[@id='combo_facility'])[1]")
    Text_Click_On_Apply_For_Hospital_XPATH=(By.XPATH,"//input[@id='chk_hospotal_readmission']")
    Text_Click_On_Medicare_Facility_XPATH=(By.XPATH,"//input[@id='radio_program_medicare']")
    Text_Click_On_Medicaid_Facility_XPATH=(By.XPATH,"//label[normalize-space()='Medicaid']")
    Text_Click_On_None_XPATH=(By.XPATH,"//input[@id='radio_program_none']")
    Text_Enter_Date_XPATH=(By.XPATH,"//input[@id='txt_visit_date']")
    Text_Add_Comment_XPATH=(By.XPATH,"//textarea[@id='txt_comment']")
    Text_Click_On_BookAppoinment_XPATH=(By.XPATH,"//button[@id='btn-book-appointment']")
    Go_To_HomePage_XPATH=(By.XPATH,"//a[@class='btn btn-default']")




    def __init__(self,driver):
        self.driver =driver

    def select_DropDown(self,Facility):
        self.driver.find_element(*Book_Appoinment.Text_Select_Center_XPATH).send_keys(Facility)


    def click_On_DropDown(self):
        self.driver.find_element(*Book_Appoinment.Text_Click_On_Apply_For_Hospital_XPATH).click()


    def select_Facilities(self,facilities):
        if facilities == "Medicare":
            self.driver.find_element(*Book_Appoinment.Text_Click_On_Medicare_Facility_XPATH).click()

        elif facilities == "Medicaid":
            self.driver.find_element(*Book_Appoinment.Text_Click_On_Medicaid_Facility_XPATH).click()

        else:
            self.driver.find_element(*Book_Appoinment.Text_Click_On_None_XPATH).click()


    def Enter_Date(self,Date):
        self.driver.find_element(*Book_Appoinment.Text_Enter_Date_XPATH).send_keys(Date)


    def Add_Comment(self,comment):
        self.driver.find_element(*Book_Appoinment.Text_Add_Comment_XPATH).send_keys(comment)


    def click_On_Bookappoinment(self):
         self.driver.find_element(*Book_Appoinment.Text_Click_On_BookAppoinment_XPATH).click()


    def click_On_HomePage(self):
        self.driver.find_element(*Book_Appoinment.Go_To_HomePage_XPATH).click()



