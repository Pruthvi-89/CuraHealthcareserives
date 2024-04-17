from selenium.webdriver.common.by import By


class Login():
    Text_Click_On_Make_Appoinment_XPATH=(By.XPATH,"//a[@id='btn-make-appointment']")
    Text_Enter_UserName_XPATH=(By.XPATH,"//input[@id='txt-username']")
    Text_Enter_Password_XPATH=(By.XPATH,"//input[@id='txt-password']")
    Text_CLick_On_Login_Button_XPATH=(By.XPATH,"//button[@id='btn-login']")
    Text_Click_On_Menu_Button_XPATH=(By.XPATH,"//i[@class='fa fa-bars']")
    Text_Click_On_Logout_XPATH=(By.XPATH,"//a[normalize-space()='Logout']")



    def __init__(self,driver):
        self.driver = driver


    def Click_on_Make_appointment(self):
        self.driver.find_element(*Login.Text_Click_On_Make_Appoinment_XPATH).click()

    def Enter_Username(self,username):
        self.driver.find_element(*Login.Text_Enter_UserName_XPATH).send_keys(username)


    def Enter_password(self,password):
        self.driver.find_element(*Login.Text_Enter_Password_XPATH).send_keys(password)


    def Click_On_Login_Button(self):
        self.driver.find_element(*Login.Text_CLick_On_Login_Button_XPATH).click()


    def click_On_Menu_Button(self):
        self.driver.find_element(*Login.Text_Click_On_Menu_Button_XPATH).click()

    def Click_On_Logout_Button(self):
        self.driver.find_element(*Login.Text_Click_On_Logout_XPATH).click()
