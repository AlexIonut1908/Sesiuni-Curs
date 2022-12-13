from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from unittest import TestCase


class Test(TestCase):
    #se ruleaza inainte de fiecare test
    def setUp(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.maximize_window()

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

    # verificam URL
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://phptravels.net/'
        self.assertEqual(expected, actual, 'Url incorect')

    def test_addremovelinktxt_url(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/add_remove_elements/'
        self.assertEqual(expected, actual, 'Url incorect')

    def test_header_addremoveelement(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'h3')
        actual = self.chrome.find_element(By.CSS_SELECTOR, 'h3').text
        expected = 'Add/Remove Elements'
        self.assertEqual(expected, actual, 'text incorect')

    def test_press_addelementbutton(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        actual = self.chrome.find_element(By.ID, 'elements').text
        expected = 'Delete'
        self.assertEqual(expected, actual, 'text incorect')

    def test_compareaddelement_delete(self):
        self.chrome.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        self.chrome.find_element(By.CSS_SELECTOR, 'button').click()
        actual = self.chrome.find_elements(By.CSS_SELECTOR, 'button.added-manually')
        expected = 3
        self.assertEqual(expected, len(actual), 'numarul de elemente nu corespunde')