# -*- coding: utf-8 -*-

import webhookurlfile
import requests
from bs4 import BeautifulSoup
import json
import time
import sys
args = sys.argv

payload_dic = {
    "text": 'もうすぐ診察の順番ですよ',
    "username": 'sinsatu_BOT',
    "icon_emoji": ':hospital:',
    "channel": '#general',
}

hospital_url = "https://www.shimafukurou.net/shimafukuro/sfd-m.php?cid=17514799"
while True:
    result = requests.get(hospital_url)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, "lxml")
        all_waiting_num = soup.find_all("font", attrs={"class": "nakamachi_num_text"})
        if len(all_waiting_num) != 0:
            for i in all_waiting_num:
                if str(args[1]) in i.text:
                    requests.post(webhookurlfile.slack_url,
                                data=json.dumps(payload_dic))
        else:
            print("none")
            pass
    else:
        pass
    time.sleep(300)
    
