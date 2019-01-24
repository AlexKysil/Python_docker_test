from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="class")
def setup(request):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options = chrome_options)

        request.cls.driver = driver
        yield driver
        driver.quit()

@pytest.mark.usefixtures("setup")
class Test_simple:

    def test_one(self):
        self.driver.get('https://www.google.com')
        expected_string = 'The Beatles - Something - YouTube'
        google_search_line = self.driver.find_element_by_name('q')
        google_search_line.send_keys("something")
        google_search_line.submit()
        actual_string = self.driver.find_element_by_xpath("//div[@class='FGpTBd']//h3//h3").text
        assert(actual_string == expected_string)
