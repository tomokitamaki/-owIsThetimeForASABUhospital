#! /root/.pyenv/shims/python3.5

import requests
import re
from bs4 import BeautifulSoup
import json
import time
import sys
args = sys.argv

f = open('webhookurlfile')
webhookurl = f.read()
f.close

# 診察番号を引数で取得するようなコードを書くところから

cnt = 0
while (cnt < 5):
    r = requests.get('http://konzatsu.net/sfd-m.php?cid=17514799')
    result = re.findall(args[1], r.text)
    if not result:
        print("Empty\"r\"")
        if not cnt == 0:
             sys.exit()
    else:
        payload_dic = {
            "text":'もうすぐ診察の順番ですよ',
            "username":'sinsatu_BOT',
            "icon_emoji":':hospital:',
            "channel":'#sandbox',
            }
        cnt = cnt + 1
        requests.post(webhookurl, data=json.dumps(payload_dic))
        time.sleep(60)
