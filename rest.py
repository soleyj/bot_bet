from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
import re

app = FlaskAPI(__name__)


@app.route("/money", methods=['GET', 'POST'])
def notes_list():
    money = a.get_money()
    money = re.sub('€', '', money)
    money = re.sub(',', '.', money)
    data = {"money":float(money)}
    return json.dumps(data)


class InstagramBot():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_money(self):
        self.browser = webdriver.Chrome(executable_path='chromedriver')
        print("in")
        self.browser.get('https://www.bet365.es/#/HO/')
        self.browser.get('https://www.bet365.es/#/HO/')
        WebDriverWait(self.browser, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, "input.hm-Login_InputField")))

        emailInput = self.browser.find_elements_by_css_selector("input.hm-Login_InputField")[0]
        passwordInput = self.browser.find_elements_by_css_selector("input.hm-Login_InputField")[1]
        passwordInput2 = self.browser.find_elements_by_css_selector("input")[2]
        emailInput.send_keys(self.email)
        passwordInput.click()
        passwordInput2.send_keys(self.password)
        followButton = self.browser.find_element_by_css_selector('button')
        followButton.click()
        time.sleep(3)
        money = self.browser.find_element_by_css_selector('div.hm-Balance')
        money = money.text
        self.browser.close()
        return (money)

        
    def closeBrowser(self):
        self.browser.close()

a = InstagramBot("dosnabs","Peraverda11")




if __name__ == "__main__":
    app.run(debug=True)