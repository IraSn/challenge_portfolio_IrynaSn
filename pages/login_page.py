# from pages.base_page import BasePage
#
#
# class LoginPage(BasePage):
 login_field_xpath ="//*[@id='login']"
//input[@name='login']
//input[@type="text"]
//*[@name='login']
//*[@type='text']
  password_field_xpath =
//*[@id="password"]
//*[@name="password"]
//*[@type="password"]

 sign_in_button_xpath = 'next' //*[@id="__next"]/form/div/div[2]/button/span[1]
//*[@class="MuiButton-label"]
//*[contains(@class,"MuiTouchRipple-root")]
Language dropdown x-path
//*[@class="MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input" ]
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
