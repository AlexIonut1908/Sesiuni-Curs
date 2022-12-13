from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Form:
    # chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome = webdriver.Chrome()

    def __init__(self):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        self.chrome.maximize_window()

    def elementByID(self, ID):
        firstName = self.chrome.find_element(By.ID, f'{ID}')
        firstName.send_keys('Alex')
        sleep(3)

    def elementByLinkText(self, linkTxt):
        self.chrome.get('https://formy-project.herokuapp.com')
        self.chrome.find_element(By.LINK_TEXT, f'{linkTxt}').click()
        sleep(3)

    def elementByName(self, name):
        self.chrome.get('https://www.seleniumframework.com/Practiceform/')
        self.chrome.find_element(By.NAME, f'{name}').send_keys('Romania')
        sleep(3)

    def elementByCSS(self, css):
        self.chrome.get('https://formy-project.herokuapp.com/form')
        return self.chrome.find_element(By.CSS_SELECTOR, f'{css}')


test = Form()
test.elementByID('first-name')
test.elementByLinkText('Autocomplete')
test.elementByName('country')
cssSelector = test.elementByCSS('input#first-name')
sleep(2)
print(cssSelector.location)
cssSelector2 = test.elementByCSS('input.form-control')
print(cssSelector2.location)
ex = test.elementByCSS('input[placeholder="Enter last name"]').send_keys('Alex')
sleep(2)