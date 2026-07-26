import pytest

from framework.pages.login_page import LoginPage

@pytest.mark.smoke

def test_user_can_login(login_page:LoginPage):
    login_page.open()
    login_page.login("nipunkohli73073@gmail.com","Nipun@123")