from playwright.sync_api import Page,expect

class LoginPage:
    def __init__(self,page:Page)-> None:
        self.page = page 
        self.email_input_locator = page.get_by_placeholder("Email")
        self.password_input_locator = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.email_not_found_text = page.locator("//ul[@class='error-messages']")
    
    def open(self):
        self.page.goto("https://conduit-realworld-example-app.fly.dev/#/login")
    
    def login(self,email:str,password:str):
        self.email_input_locator.fill(email)
        self.password_input_locator.fill(password)
        self.login_button.click()
    