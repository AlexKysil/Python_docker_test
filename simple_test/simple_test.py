from selenium import webdriver
import unittest

class test_simple(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test(self):
        driver = self.driver
        driver.get('https://www.google.com')
        expected_string = 'The Beatles - Something - YouTube'
        google_search_line = driver.find_element_by_name('q')
        google_search_line.send_keys("something")
        google_search_line.submit()
        actual_string = driver.find_element_by_xpath("//div[@class='kp-header']//h3//h3").text
        assert(actual_string == expected_string)

    def teardown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()