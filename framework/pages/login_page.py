from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self,page:Page)-> None:
        self.page = page 
        self.email_input_locator = page.get_by_placeholder("Your E-mail *")
        self.password_input_locator = page.get_by_placeholder("Your Password *")
        self.login_button = page.locator("//input[@value='Login']")
        self.email_not_found_text = page.locator("//div[@data-test='login-error']")
        self.profile = page.locator("//a[@routerlink='profile']")
    
    def open(self):
        self.page.goto("https://v4.practicesoftwaretesting.com/#/auth/login")
    
    def login(self,email:str,password:str):
        self.email_input_locator.fill(email)
        self.password_input_locator.fill(password)
        self.login_button.click()
    
    def verify_user_is_loggedIn(self)->None:
           expect(self.profile).to_be_visible()
           
    def verify_email_not_found(self)->None:
        expect(self.email_not_found_text).to_contain_text("Invalid email or password")