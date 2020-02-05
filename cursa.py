# get cursa


#  a = browser.find_elements_by_css_selector("div.slm-RaceMeeting")


horse_1_odd =[]
horse_2_odd =[]

horse_1odd = browser.find_elements_by_css_selector("div.rcm-RacingCouponParticipantEnhanced_Wrapper")
for b in horse_1odd:
    temp_dic = {}
    temp_dic["horse_name"] = b.find_element_by_css_selector("span.rcm-CouponHorseTrainerJockey_HorseText").text
    temp_dic["horse_name"] = b.find_element_by_css_selector("span.rcm-RacingCouponParticipantEnhancedOddsOnly_Odds").text
    horse_1_odd.append(temp_dic)

horse_2odd = browser.find_elements_by_css_selector("div.rcm-RacingCouponPricePromiseEnhancedParticipant")
for b in horse_2odd:
    temp_dic = {}
    temp_dic["horse_name"] = b.find_element_by_css_selector("span.rcm-CouponHorseTrainerJockey_HorseText").text
    temp_dic["horse_name"] = b.find_element_by_css_selector("span.rcm-RacingCouponPricePromiseEnhancedParticipantOdds_Odds").text
    horse_1_odd.append(temp_dic)



iframe = self.browser.find_element_by_xpath('//*[@name="bsFrame"]')
# do the switch
self.browser.switch_to.frame(iframe)
time.sleep(2)
self.browser.find_element_by_xpath("//span[@data-inp-type='ewcb']").click()
# get quota
self.browser.find_element_by_xpath("//div[@class='bs-EachWayExtraBetType_Dropdown']").click()
horse_1_odd =[]
horse_pos_odd  = browser.find_elements_by_css_selector("div.bs-EachWayExtraBetType_MenuItemWrapper")
for b in horse_2odd:
    temp_dic = {}
    temp_dic["horse_name"] = b.find_element_by_css_selector("div.bs-EachWayExtraBetType_MenuItemName").text
    temp_dic["odd"] = b.find_element_by_css_selector("div.bs-EachWayExtraBetType_MenuItemOdds").text
    horse_pos_odd.append(temp_dic)
