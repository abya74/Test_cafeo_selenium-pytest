import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def browser():
    options = Options()
    #daca vrem sa nu se deschida tabul de crom cand rulam
    # options.add_argument('--headless')
    #before tests - ce se face inainte de fiecare tests
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
    # maximaze window
    driver.maximize_window()
    #return driver - tabul pe care noi lucram
    yield driver
    #after tests - ce vrem sa facem dupa fiecare test
    driver.quit()
