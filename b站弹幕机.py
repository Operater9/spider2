#!/usr/bin/env python
# coding:utf8
# author:Z time:2018/1/17
import requests
import time
import random

class SendLiveRoll():
    #会先一步其他函数执行，初始化函数
    def __init__(self,roomid):
        #直播的房间号
        self.roomid=roomid

        #真实网址
        self.url_1='https://api.live.bilibili.com/ajax/msg'
        self.form1={
            'roomid': self.roomid,
            'token':'',
            'csrf_token':'8edb06879e841313937990af043cdcd2',
        }
        self.url_2='https://api.live.bilibili.com/msg/send'
        self.cookie={'cookie':'l=v; sid=bh1572ea; fts=1514775841; pgv_pvi=4869667840; buvid3=DC48EB45-15CE-4849-9CF0-3290990C643D31000infoc; UM_distinctid=160afad1365a2-0db36860127bef-5d4e231d-100200-160afad13668b; rpdid=mxwwsipxmdosopmmsqpw; finger=edc6ecda; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516193847; _jct=7dc07400fb8b11e7b83e0242ac123ee4; LIVE_BUVID=f95bcc3e77be752320f16074c8a8b673; LIVE_BUVID__ckMd5=a1950fa39efc481b; _dfcaptcha=28975893be8e4f9c8581be489f4ef25a; DedeUserID=148853081; DedeUserID__ckMd5=5e146562450ab2b0; SESSDATA=dc5079ba%2C1518788786%2C002a9b98; bili_jct=6e3900ba06687eeae4e00fc968208246; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1516196802'}
    #获取弹幕的函数
    def getDanMu(self):

        #获取弹幕
        html_1=requests.post(self.url_1,data=self.form1)

        #提取弹幕
        self.danmu=html_1.json()['data']['room'][random.randint(7,9)]['text']
        print(self.danmu)
    def postDanMu(self):
        form_2={'color':'16777215',
                'fontsize':'25',
                'mode':'1',
                'msg':self.danmu,
                'rnd':'1516196799',
                'roomid':self.roomid}
        #发送弹幕
        requests.post(self.url_2,data=form_2,cookies=self.cookie)
if __name__ == '__main__':
    while 1:
        time.sleep(random.randint(2,5))
        danmu=SendLiveRoll(81697)
        danmu.getDanMu()
        danmu.postDanMu()