from collections.abc import Generator
from typing import Any

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright

from framework.config import settings
from framework.pages.home_page import HomePage
from framework.pages.login_page import LoginPage
from framework.pages.product_catalogue_page import ProductCataloguePage

@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict[str, Any]:
    return {
        "headless": settings.headless,
        "slow_mo": settings.slow_mo,
    }


@pytest.fixture(scope="session")
def browser(
    playwright: Playwright,
    browser_type_launch_args: dict[str, Any],
) -> Generator[Browser, None, None]:
    supported_browsers = {
        "chromium": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit,
    }

    configured_browser = settings.browser_name.strip().lower()
    browser_type = supported_browsers.get(configured_browser)

    if browser_type is None:
        supported_browser_names = ", ".join(supported_browsers)

        raise ValueError(
            f"Unsupported browser '{settings.browser_name}'. "
            f"Supported browsers are: {supported_browser_names}."
        )

    browser_instance = browser_type.launch(
        **browser_type_launch_args,
    )

    yield browser_instance

    browser_instance.close()


@pytest.fixture
def context(
    browser: Browser,
) -> Generator[BrowserContext, None, None]:
    browser_context = browser.new_context(
        base_url=settings.base_url,
        viewport={
            "width": 1440,
            "height": 900,
        },
    )

    browser_context.set_default_timeout(
        settings.default_timeout_ms,
    )

    browser_context.set_default_navigation_timeout(
        settings.navigation_timeout_ms,
    )

    yield browser_context

    browser_context.close()


@pytest.fixture
def page(
    context: BrowserContext,
) -> Generator[Page, None, None]:
    browser_page = context.new_page()

    yield browser_page

    browser_page.close()


@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def product_cataloge_page(page: Page) -> ProductCataloguePage:
    return ProductCataloguePage(page)