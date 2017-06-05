#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import subprocess
import webbrowser
import time


cmd = ["ping -c 2 8.8.8.8 -s 1272","ping6 -c 2 2001:4860:4860::8888 -s 1452","traceroute 8.8.8.8","traceroute 2001:4860:4860::8888","dig google.com A","dig google.com AAAA"]


url = ["http://www.kame.net/","http://www.amazon.co.jp/registry/wishlist/1R5ZE9A1TGDZJ"]

for n in cmd:
        subprocess.Popen(n,shell=True)
        #subprocess　command
        time.sleep(1)
        #sleep Shell or python 
for n in url:
        webbrowser.open_new(n)
        #browser controll
        #request /img/kame-noanime-small.gif" altの値を見れはﾞここも自動化出きる
