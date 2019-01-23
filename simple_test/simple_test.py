from selenium import webdriver


def simple_test():
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    expected_string = 'The Beatles - Something - YouTube'
    google_search_line = driver.find_element_by_name('q')
    google_search_line.send_keys("something")
    google_search_line.submit()
    actual_string = driver.find_element_by_xpath("//div[@class='kp-header']//h3//h3").text
    assert(actual_string == expected_string)
    driver.quit()

simple_test()