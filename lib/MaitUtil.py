from wsgiref import headers
from bs4 import BeautifulSoup as bs
import urllib.request as url_req
import libs.SessionHandler as sessionHandler
import requests
import json
import re

import sys
sys.path.append('C:/Users/git/python_test/ui_automation')
import config.real_kr as gUser

class MaitUtil():
    def __init__(self):
        self.restmailurl=gUser.mail_server
        self.loginmail_id=gUser.id_only

    def getRestMail(self, loginmail_id):
        url = gUser.mail_server +loginmail_id
        req = requests.get(url)
        soup =bs(req.text, 'html.parser')

        list_href = soup.select('table')
        c = len(list_href) - 1
        last_mail=list_href[c]
        href_url= last_mail.find("a")['href']

        return str(href_url)
        


        
