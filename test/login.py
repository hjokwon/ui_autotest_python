from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time, re, signal,unittest

import sys
sys.path.append('C:/Users/git/python_test/ui_automation')

import config.properties as sysconfig
import config.real as commonConfig
import lib.DefaultPageSetting as setting
import lib.MaitUtil as mail



# Homepage Login

class LoginMainTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(sysconfig.driverpath)
        self.config=setting.DefaultPageSetting("real")
        self.config.beforeTest(self.driver)
        self.loginid = self.config.member
        self.loginpwd = self.config.password
        self.loginid_only=self.config.loginid_only
        self.country = self.config.country

    def tearDown(self):
        driver = self.driver
        driver.quit()

    def test_member_login(self):
        driver = self.driver

        #1. 홈페이지 > GNB > 로그인 버튼 클릭
        driver.find_element_by_link_text("로그인").click()

        #2. 로그인페이지 > ID/PW 입력 후 확인
        setting.DefaultPageSetting.loginToastMember(self, driver, self.loginid, self.loginpwd)
        
        #3. 2차 인증 페이지 체크
        setting.DefaultPageSetting.ChecktwofactorPage(self, driver)

        #4. 중복 로그인 허용
        setting.DefaultPageSetting.CheckloginIP(self,driver)

        #5. 홈페이지 URL 접속 확인
        expect_url = commonConfig.url + self.country
        setting.DefaultPageSetting.checkCurrentURL(self,driver,expect_url)
             
        #6. 홈페이지 > GNB > 로그아웃
        setting.DefaultPageSetting.logoutToastMemeber(self,driver)

"""
    def test_serviceuse_login(self):
        driver = self.driver
        driver.implicitly_wait(10)
        url = ''
        driver.get(url)
        driver.maximize_window()
        first=driver.window_handles[0]

        #1. 서비스 이용하기 (DNS Plus) > 클릭
        driver.find_element_by_css_selector('.btn.btn_service_use').click()
        print("test OK")
        
        time.sleep(5)

        #2. 로그인 페이지에서 ID/PW 로그인
        chwdz=driver.window_handles[1]
        driver.switch_to_window(chwdz)
 
        driver.find_element_by_name("id").send_keys('')
        driver.find_element_by_id("password").send_keys('')
        driver.find_element_by_css_selector('.btn_area').click()

        time.sleep(1)
        #3. 동시로그인 페이지 > 확인 버튼 클릭
        driver.find_element_by_css_selector('.btn.is_full').click()
        time.sleep(4)

        #4. 콘솔 > 조직 생성 모달창 > 추가 버튼 클릭 > 조직 이름 입력 > 확인 > 생성
        # 프로젝트 자동 생성 후 생성

        driver.find_element_by_xpath('//button[contains(text(),"추가")]').click()
        
        orgname=driver.find_element_by_name("orgName")
        orgname.clear()
        orgname.send_keys('org-test2')
        driver.find_element_by_xpath('//button[contains(text(),"생성")]').click()
        time.sleep(1)
        driver.find_element_by_id('__BVID__66__BV_toggle_')
        time.sleep(3)
        driver.find_element_by_css_selector('.btn.btn-secondary.type_inquiry').click()
        #5. 서비스 페이지(DNS Plus) 확인
        time.sleep(3)
        dnsplus_name=driver.find_element_by_css_selector('.icons.icon-ic-network-dns-plus')
        if dnsplus_name:
            print("DNS Plus 활성화 완료")
"""

if __name__ == '__main__' :
    unittest.main()

