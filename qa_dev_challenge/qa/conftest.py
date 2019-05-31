import pytest
from selenium.webdriver import Firefox, FirefoxOptions
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    # """ A browser instance which closes after the testrun. """
    
    options = webdriver.ChromeOptions()
    options.add_argument('-headless')
    browser_ = webdriver.Chrome(options=options)
    
    yield browser_

    browser_.quit()