from collections.abc import Generator # this imports the genrator type becuase we our brwoser fixture uses yield.
from typing import Any 

import pytest 
from playwright.sync_api import Browser,BrowserContext,BrowserType,Page, Playwright

from framework.config import settings 

@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict[str,Any]:
    """
        Return the browser launch configuration.    
        This fixture runs once for the complete test session.
    """
    return {
        "headless":settings.headless,
        "slow_mo":settings.slow_mo,
    }
@pytest.fixture(scope="session")
def browser(playwright:Playwright,
            browser_type_launch_args: dict[str,Any],
            )-> Generator[Browser,None,None]:
    """
    Launch the browser configured in framework/config.py.

    The browser is launched once before the tests start and closed after the complete test session finishes.
    
    """
    supported_browsers = {
         "chromium":playwright.chromium,
         "firefox": playwright.firefox,
         "webkit": playwright.webkit,
    }
    configured_browser = settings.browser_name.strip().lower()

    browser_type = supported_browsers.get(configured_browser)

    if browser_type is None:
        supported_browser_name =", ".join(supported_browsers)

        raise ValueError(
            f"Unsupprted browser '{settings.browser_name}'."
            f"Supported browsers are: {supported_browsers}."
        )
    browser_instance = browser_type.launch(
        **browser_type_launch_args,
    )
    yield browser_instance
    browser_instance.close()

@pytest.fixture
def context(
    browser:  Browser,
    ) -> Generator[BrowserContext,None,None]:
    """
    creates a fresh isolated browser context for every test.
    A Browser context behaves like a new incognito browser session.
    """    
    browser_context = browser.new_context(
        base_url = settings.base_url,
        viewport={
            "width":1440,
            "height":900,
        },
    )
    browser_context.set_default_timeout(
        settings.navigation_timeout_ms,
    )
    yield browser_context

    browser_context.close()

@pytest.fixture
def page(
    context: BrowserContext,
)-> Generator[page,None,None]:
    """
    Creates a fresh browser page for every test.
    This page is closed automatically after the test finishes.
    
    """
    browser_page = context.new_page()
    yield browser_page

    browser_page.close()