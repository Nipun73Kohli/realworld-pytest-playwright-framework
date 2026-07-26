import pytest 

from framework.pages.home_page import HomePage

@pytest.mark.smoke
    
def test_home_page_loads_successfully(home_page:HomePage) -> None:
    home_page.open()
    home_page.verify_home_page_loaded()