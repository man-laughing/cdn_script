#!/usr/bin/python

import requests
import json
import datetime
import time
import hmac
import hashlib

URL = "http://fusion.qiniuapi.com/v2/tune/log/list"
AK = 'YOUR_ACCESS_KEY'
SK = 'YOUR_SECRET_KEY'

def hmac_sha1(k,m):
    aa = hmac.new(k.encode('utf8'),m.encode('utf8'),hashlib.sha1).digest().encode('base64').strip()
    aa = aa.replace('+','-').replace('/','_')
    return aa
def getYesterdayDate():
    t  = datetime.datetime.now()  + datetime.timedelta(days=-1)
    tt = str(t.date())
    return tt

headers = { "Content-Type": "application/json" }
body    = { "Day": getYesterdayDate() ,"domains":"a.b.com;c.d.cn" }
msg   = "/v2/tune/log/list" + "\n" 
sig   = hmac_sha1(SK,msg)
token =  AK+":"+sig
headers['Authorization'] = 'QBox ' + token

##########################################################

resp = requests.post(URL,headers=headers,json=body)
print resp.status_code
print resp.content
resp.close()
