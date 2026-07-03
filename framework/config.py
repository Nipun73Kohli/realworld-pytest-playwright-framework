from dataclasses import dataclass 
""" A dataclass is usefull when a class in mainly used to store values. 
    In our case the Settings class stores framework configuration such as 
    - base URL 
    - browser name
    - headless mode
    - timeouts"""
@ dataclass(frozen=True) 
# frozen = True means that these value cannot change accidnetally while the tests are running
class Settings:
    base_url:str ="https://demo.realworld.show"
    api_url: str = "https://api.realworld.show/api"

    browser_name: str = "chromium"
    headless: bool = False
    slow_mo: int = 300

    default_timeout_ms: int = 10_000 # This sets the maximum time Playwright should wait for regular actions.
    navigation_timeout_ms: int = 30_000 #This sets the maximum time for page navigation.

settings = Settings() #This creates an object from the Settings class. Other files can import it like this: from framework.config import settings
# Then access values:
# settings.base_url
# settings.browser_name
# settings.headless
# settings.default_timeout_ms