from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome(executable_path='chromedriver')
        self.email = email
        self.password = password

    def signIn(self):

        self.browser.get('https://www.instagram.com/accounts/login/')
        self.browser.implicitly_wait(10) # seconds
        time.sleep(2)
        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def closeBrowser(self):
        self.browser.close()
    

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(2) # not necessary
        followButton = self.browser.find_element_by_css_selector('button')
        followButton.click()

a = InstagramBot("thebosssoley","peraverda11")
a.signIn()
a.followWithUsername("niuboxnatura")
a.closeBrowser()