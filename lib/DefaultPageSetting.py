from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time, re, signal,unittest
import requests

import sys
sys.path.append('C:/Users/git/python_test/ui_automation')
import config.real_kr as gUser
import lib.MaitUtil as mail



class DefaultPageSetting:
        def __init__(self, env, country):
            self.member=gUser.id
            self.password=gUser.password
            self.url=gUser.homepage_url
            self.env=gUser.env
            self.country=gUser.country
            self.loginid_only=gUser.id_only

        def beforeTest(self, driver, country):
            url=self.url + "/" + country
            print('move to URL %s',url)
            driver.get(self.url)
            driver.maximize_window()

        def loginToastMember(self, driver, id, password):
            driver.find_element_by_name("id").send_keys(id)
            driver.find_element_by_id("password").send_keys(password)
            driver.find_element_by_css_selector('.btn_area').click()

        def ChecktwofactorPage(self, driver):
            check_text = driver.find_element_by_xpath("//*[contains(text(), 'login')]")
            if check_text:
                print('second authority try')
                time.sleep(5)
                
                last_mail_prefix = mail.MaitUtil.getRestMail(self,self.loginid_only)
                login_click=requests.get(last_mail_prefix)

                if login_click.status_code==200:
                    print("second authority pass")
                else:
                    print("second authority fail")
                time.sleep(3)
                driver.find_element_by_css_selector('.btn.is_full').click()                

            else:
                print('no nee second authority')
        
        def CheckloginIP(self,driver):
            check_text = driver.find_element_by_xpath("//*[contains(text(),'같은 아이디로 로그인된')]")
            if check_text:
                print("중복 로그인")
                time.sleep(3)
                driver.find_element_by_css_selector('.btn.is_full').click()
            else:
                print("중복 로그인 없음")   

        def checkCurrentURL(self, driver, url):
            currentURL = driver.current_url
            if currentURL == url:
                print("URL 일치, 현재 URL : ", currentURL)
            else:
                print("URL 불일치, 현재 URL : ", currentURL)

        def logoutToastMemeber(self, driver):
            gnb_user=driver.find_element_by_css_selector('.btn_member_setting')
            ActionChains(driver).move_to_element(gnb_user).perform()
            driver.find_element_by_link_text("로그아웃").click()
            logintext = driver.find_element_by_css_selector('.link_item')
            assert logintext.text == "로그인"
            time.sleep(1)

        
            

