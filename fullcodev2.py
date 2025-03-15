import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys

try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('Vui Lòng Chạy Lại Tool')
  
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""
 © Tool Gộp Vip  By phamvantung
        Zalo: 0988196974
        Telegram: @toolgolike0
         admin cod: @Dark121918
         ngân hàng: MBBank 
         STK: 3555020409  
\033[1;97mTool By: \033[1;32mVan Tung            \033[1;97mPhiên Bản: \033[1;32m2.2     
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)

while True:
 os.system('cls' if os.name == 'nt' else 'clear')
 banner()
 print("\033[1;37m╔══════════════════════╗         ")
 print("\033[1;37m║  \033[1;32mTool Auto Golike    \033[1;37m║          ")
 print("\033[1;37m╚══════════════════════╝           ")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.1 \033[1;97m: \033[1;34mTool Auto TikTok \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.2 \033[1;97m: \033[1;34mTool Auto Instagram \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.3 \033[1;97m: \033[1;34mTool Auto Twitter \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.4 \033[1;97m: \033[1;34mTool Auto Youtube \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.5 \033[1;97m: \033[1;34mTool Auto Thread \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.6 \033[1;97m: \033[1;34mTool Auto Linkedin \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.7 \033[1;97m: \033[1;34mTool Snapchat By HuongDev \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.8 \033[1;97m: \033[1;34mTool By HD \033[1;32m[Online]")
 print("\033[1;37m╔══════════════════════╗         ")
 print("\033[1;37m║  \033[1;32mTool Tương Tác Chéo \033[1;37m║          ")
 print("\033[1;37m╚══════════════════════╝           ")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.1 \033[1;97m: \033[1;34mTool TTC Facebook \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.2 \033[1;97m: \033[1;34mTool TTC Pro5 \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.3 \033[1;97m: \033[1;34mTool TTC Pro5v1 \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.4 \033[1;97m: \033[1;34mTool TTC TikTok \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.5 \033[1;97m: \033[1;34mTool TTC Instagram \033[1;32m[Online]")
 print("\033[1;37m╔══════════════════════╗         ")
 print("\033[1;37m║  \033[1;32mTool TraoDoiSub.com \033[1;37m║          ")
 print("\033[1;37m╚══════════════════════╝           ")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.1 \033[1;97m: \033[1;34mTool TDS Facebook \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.2 \033[1;97m: \033[1;34mTool TDS pro5 \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.3 \033[1;97m: \033[1;34mTool TDS pro5v1 \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.4 \033[1;97m: \033[1;34mTool TDS tik tok\033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.5 \033[1;97m: \033[1;34mTool TDS ig \033[1;32m[Online]")
 print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.6 \033[1;97m: \033[1;34mTool TDS full job \033[1;32m[Online]")
 print(f"\033[97m════════════════════════════════════════════════════════")
 chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
 print('\033[1;39m─────────────────────────────────────────────────────────── ')
  # Thành Công
 if chon == '1.1':
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/92db0a82035b809978e8bb7ec4a2799ad25d54b7/test.py').text)
 elif chon == '1.2':
  exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/6b1b907c21eb1da7ebbbbb6bcad82f0ae308a437/Full%20Golike/AutoIG.py').text)
 elif chon == '1.3':
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/bcffa501ba994b563cfe32d6a944f5326b5e24a1/AutoX.py').text)
 elif chon == '1.4':
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/bcffa501ba994b563cfe32d6a944f5326b5e24a1/AutoYTB.py').text)
 elif chon == '1.5':
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/21b91f419cfb390e3657c39dd3e19225c43007a0/AutoTheads.py').text)
 elif chon == '1.6':
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/57eee451357b8e50c9f101debe2a1db03a107733/AutoLinkedin.py').text)
 elif chon == '1.7':
     exec(requests.get('https://raw.githubusercontent.com/PhamVanTung960/Phamvantung/9e3c88faf40448721c60e9773f79ecd152e69b3e/dhtool4.2.php').text)
 
  # TTC
 elif chon == '2.1':
  exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCFB.py').text)
 elif chon == '2.2':
  exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCPro5.py').text)
 elif chon == '2.3':
  exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCPro5v1.py').text)
 elif chon == '2.4':
  exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCTikTok.py').text)
 elif chon == '2.5':
  exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCIG.py').text)
  # TDS
 elif chon == '3.1':
  # Thanh Công
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/c2d21f6dd757d6c41164aec36cb1edda8541cb5d/ToolTDSFb.py').text)
 elif chon == '3.2':
  # Thanh Công
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/c2d21f6dd757d6c41164aec36cb1edda8541cb5d/ToolTDSPro5.py').text)
 elif chon == '3.3':
  # Thanh Công
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/c2d21f6dd757d6c41164aec36cb1edda8541cb5d/ToolTDSPro5.py').text)
 elif chon == '3.4':
  # Thanh Công
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/c2d21f6dd757d6c41164aec36cb1edda8541cb5d/ToolTDSTikTok.py').text)
 elif chon == '3.5':
  # Thanh Công
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/c2d21f6dd757d6c41164aec36cb1edda8541cb5d/TDSIG.py').text)
 elif chon == '3.6':
  # Thanh Công
  exec(requests.get('https://raw.githubusercontent.com/PhamVanTung9608/Phamvantung/c2d21f6dd757d6c41164aec36cb1edda8541cb5d/ToolTDSFullJob.py').text) 
 else:
  sys.exit("")