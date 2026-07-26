from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self,page:Page)-> None:
        self.page = page
        self.brand_link = page.get_by_role("navigation").get_by_role("link", name="conduit")
        self.home_link = page.get_by_role("link", name="Home")
        self.sign_up_link = page.get_by_role("link", name="Sign up")
        self.sign_in_link = page.get_by_role("link", name ="Login")

    def open(self)-> None:
        self.page.goto("/")
    
    def verify_home_page_loaded(self)-> None:
        expect(self.brand_link).to_be_visible()
        expect(self.home_link).to_be_visible()
        expect(self.sign_up_link).to_be_visible()
        expect(self.sign_in_link).to_be_visible()
