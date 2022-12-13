from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase


class Test(TestCase):
    #se ruleaza inainte de fiecare test
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://www.phptravels.net/')
        self.chrome.maximize_window()

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # verificam URL
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/'
        self.assertEqual(expected, actual, 'Url incorect')

    # def test_search_City(self):
    #     self.chrome.implicitly_wait(2)
    #     searchbar = self.chrome.find_element(By.ID, 'select2-hotels_city-container')
    #     searchbar.click()
    #     search1 = self.chrome.find_element(By.CLASS_NAME, 'select2-search__field')
    #     search1.send_keys('Bucharest')
    #     self.chrome.implicitly_wait(2)
    #     expected_value = 'Bucharest, Romania'
    #     result = self.chrome.find_element(By.CLASS_NAME, 'select2-results__option select2-results__option--highlighted')
    #     actual = result.txt
    #     self.assertEqual(expected_value, 'Rezultat incorect')

