#!/usr/bin/python

import datetime
import hmac
import hashlib

def hmac_sha1(k,m):
    aa = hmac.new(k.encode('utf8'),m.encode('utf8'),hashlib.sha1).digest().encode('base64').strip()
    aa = aa.replace('+','-').replace('/','_')
    return aa
def getYesterdayDate():
    t  = datetime.datetime.now()  + datetime.timedelta(days=-1)
    tt = str(t.date())
    return tt

class qiniu(object):

    def __init__(self,ak,sk):
        self.ak = ak
        self.sk = sk
    
    def sign(self,uri):
        msg = uri + "\n" 
        sig = hmac_sha1(self.sk,msg)
        return sig
 
    def token(self,sig):
        token  =  "QBox " + self.ak + ":" + sig
        return token 

