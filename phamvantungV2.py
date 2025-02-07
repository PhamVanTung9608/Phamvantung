
den = '[1;90m'
luc = '[1;32m'
trang = '[1;37m'
red = '[1;31m'
vang = '[1;33m'
tim = '[1;35m'
lamd = '[1;34m'
lam = '[1;36m'
purple = '\e[35m'
hong = '[1;95m'
xnhac = '[1;95m'
xduong = '[1;95m'
do = '[1;33m'
thanh_xau = trang + '' + lam + '[' + vang + 'vL' + lam + '] ' + trang + ' ' + luc
thanh_dep = trang + '' + lam + '[' + luc + 'vL' + lam + '] ' + trang + ' ' + luc
import requests
import json
import os
from sys import platform
from datetime import datetime
from time import sleep, strftime
import hashlib
import hmac
import uuid

try:
    from pystyle import Colors, Colorate
except ImportError:
    os.system('pip install pystyle')
    from pystyle import Colors, Colorate

banners = f"""        
   © Tool Auto Golike Tiktok  By phamvantung
        Zalo: 0988196974
        Telegram: @toolgolike0
         admin cod: @Dark121918
         ngân hàng: MBBank 
         STK: 3555020409
        
        
        
        ╚═╝╚══════╝╚════╝╚═╝╚══╝╚═════╝"""

thongtin = f"""
  \033[1;35m  Mua tool vip liên hệ: 0988186974
 \033[1;34m  Giá Chỉ 2k / ngày
  \033[1;33m ® Tool Gộp By Phạm Văn Tùng 
"""

def vanlong(so):
    a = '────' * (so - 1) + '─'
    for i in range(len(a)):
        sleep(0.003)
    print(a)

def clear():
    if platform.startswith('linux'):
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('[0m', end='')
    clear()
    a = Colorate.Horizontal(Colors.blue_to_green, banners)
    print(a)
    print(thongtin)
    vanlong(17)

banner()
print("\033[38;5;155m      Nhập Số \033[1;36m[1] \033[38;5;204mTOOL GOLIKE TIKTOK \033[1;33m")
chon = float(input('\033[1;31m     Nhập Số \033[1;32m: \033[1;33m'))
import requests,os,sys, time
def check_internet_connection():
    try:
        response = requests.get("https://google.com/", timeout=5)
        return True
    except requests.ConnectionError:
        return False
if not check_internet_connection():
    print("\n\033[1;39mBạn bug 1 lần nữa sẽ bị dính botnet ngay nhé")
    sys.exit(1) 
if chon == 1 :
	exec(requests.get('https://raw.githubusercontent.com/phamvantung01122007/phamvantung01122007/main/obf-golike.py').text)
exit()