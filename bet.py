from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class InstagramBot():
    def __init__(self, email, password):


        self.browser = webdriver.Chrome(executable_path='chromedriver')
        self.email = email
        self.password = password


    def get_bet_in(self):
        self.browser.get('https://www.bet365.es')
        WebDriverWait(self.browser, 10).until( EC.presence_of_element_located((By.CSS_SELECTOR, "div.lpgb a")))
        annual_link = self.browser.find_element_by_link_text('Español')
        annual_link.click()

        time.sleep(2)

    def get_money(self):

        self.browser.get('https://www.bet365.es')
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
        return (money.text)

    def closeBrowser(self):
        self.browser.close()


    def Apostar_horse(self,cursa,caball):
        self.browser.get('https://www.bet365.es')
        self.browser.get('https://www.bet365.es/#/HO/')
        time.sleep(3)
        HorseSw = self.browser.find_element_by_xpath("//div[contains(text(),'caballos')]")
        HorseSw.click()
        time.sleep(2)
        string_search = "//div[contains(text(),'" + cursa + "')]"
        HorseCursa = self.browser.find_element_by_xpath(string_search)
        HorseCursa.click()
        time.sleep(2)
        string_search = "//span[contains(text(),'" + caball + "')]"
        HorseCursa = self.browser.find_element_by_xpath(string_search)
        HorseCursa.click()

        ################################
        ## get all horse OODS
        # horse_1_odd =[]
        # horse_2_odd =[]
        # horse_1odd = self.browser.find_elements_by_css_selector("div.rcm-RacingCouponParticipantEnhanced")
        
        # for b in horse_1odd:
        #     temp_dic = {}
        #     temp_dic["horse_name"] = b.find_element_by_css_selector("span.rcm-CouponHorseTrainerJockey_HorseText").text
        #     temp_dic["odd"] = b.find_element_by_css_selector("span.rcm-RacingCouponParticipantEnhancedOddsOnly_Odds").text
        #     horse_1_odd.append(temp_dic)

        # horse_2odd = self.browser.find_elements_by_css_selector("div.rcm-RacingCouponPricePromiseEnhancedParticipant")
        # for b in horse_2odd:
        #     temp_dic = {}
        #     temp_dic["horse_name"] = b.find_element_by_css_selector("span.rcm-CouponHorseTrainerJockey_HorseText").text
        #     temp_dic["odd"] = b.find_element_by_css_selector("span.rcm-RacingCouponPricePromiseEnhancedParticipantOdds_Odds").text
        #     horse_2_odd.append(temp_dic)
        # print(horse_1_odd)
        # print("2odd")
        # print(horse_2_odd)


        ######################
        ##get horse pos odd
        iframe = self.browser.find_element_by_xpath('//*[@name="bsFrame"]')
        # do the switch
        self.browser.switch_to.frame(iframe)
        time.sleep(2)
        self.browser.find_element_by_xpath("//span[@data-inp-type='ewcb']").click()
        # get quota
        time.sleep(1)
        self.browser.find_element_by_xpath("//div[@class='bs-EachWayExtraBetType_Dropdown']").click()
        time.sleep(1)
        horse_pos_odd = []
        horse_pos_odd_data  = self.browser.find_elements_by_css_selector("div.bs-EachWayExtraBetType_MenuItemWrapper")
        a = 0
        for b in horse_pos_odd_data:
            a = a +1
            print(b)
            temp_dic = {}
            temp_dic["pos"] = b.find_element_by_css_selector("div.bs-EachWayExtraBetType_MenuItemName").text
            temp_dic["odd"] = b.find_element_by_css_selector("div.bs-EachWayExtraBetType_MenuItemOdds").text
            horse_pos_odd.append(temp_dic)
            print(horse_pos_odd)
        # print(horse_pos_odd)
        # time.sleep(2)
        # HorseCursa = self.browser.find_element_by_xpath("//span[@data-place-divider='4']")
        # HorseCursa.click()
        # wait for iframe presence by element name
        # iframe = self.browser.find_element_by_xpath('//*[@name="bsFrame"]')
        # # do the switch
        # self.browser.switch_to.frame(iframe)
        # time.sleep(2)
        # self.browser.find_element_by_xpath("//span[@data-inp-type='ewcb']").click()
        # # get quota
        # self.browser.find_element_by_xpath("//div[@class='bs-EachWayExtraBetType_Dropdown']").click()
 
        # html = self.browser.page_source
        # text = open("Output.txt", "w")
        # text.write(html)
        # text.close()

a = InstagramBot("dosnabs","Peraverda11")
a.Apostar_horse("Chelmsford City","Colada Cove")
a.closeBrowser()


