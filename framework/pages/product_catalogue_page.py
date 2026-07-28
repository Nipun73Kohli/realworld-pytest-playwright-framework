from playwright.sync_api import Page,expect

class ProductCataloguePage:

    def __init__(self,page:Page)-> None:
        self.page = page

    def open(self)->None:
        self.page.go.to("/")