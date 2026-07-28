import pytest

from framework.pages.login_page import LoginPage

@pytest.mark.smoke

def test_user_cannot_login_with_invalid_email(login_page:LoginPage):
    login_page.open()
    login_page.login("nipunkohli733@gmail.com","Nipun@123")
    login_page.verify_email_not_found()

@pytest.mark.smoke

def test_user_can_login(login_page:LoginPage):
    login_page.open()
    login_page.login("nipunkohli@gmail.com","Test@123")
    login_page.verify_user_is_loggedIn()