from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

class test_simple(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(chrome_options = chrome_options)

    def test(self):
        driver = self.driver
        driver.get('https://www.google.com')
        expected_string = 'The Beatles - Something - YouTube'
        google_search_line = driver.find_element_by_name('q')
        google_search_line.send_keys("something")
        google_search_line.submit()
        actual_string = driver.find_element_by_xpath("//div[@class='FGpTBd']//h3//h3").text
        assert(actual_string == expected_string)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()