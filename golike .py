

import os

import sys,re

import datetime

from datetime import datetime, timedelta

import json

import random

import platform

try:

  import requests

except ImportError:

  os.system('pip install requests')

  import requests

try:

  from colorama import Back, Fore, Fore, Style, init

except ImportError:

  os.system('pip install colorama')

  from colorama import Back, Fore, Fore, Style, init

try:

  from bs4 import BeautifulSoup

except ImportError:

  os.system('pip3 install beautifulsoup4')

  from bs4 import BeautifulSoup











import time

from time import sleep

import json,ast

os.system('clear')

 

init(autoreset=True)







def pr3(text):

  lines = text.split('\n')

  for line in lines:

      sys.stdout.write(line+'\n')

      sys.stdout.flush()

      sleep(0.1)

def pr(text):

  for i in range(len(text)+1):

      sys.stdout.write("\r" + text[:i])

      sys.stdout.flush()

      sleep(0.01)

  print()



def time():

  current_time = datetime.now()



  time = current_time.strftime("%M:%S")

  return time



def cint(number):

  while True:

    try:

      numbers = int(input(number))

      return numbers

    except ValueError:

      print(f'{red}Vui lòng chỉ nhập số')













def changetoken(red,green,white):

  if os.path.exists("cache_golike_auth.txt"):

    text=f'''{green}BẠN MUỐN DÙNG AUTH CŨ HAY ĐỔI AUTH

{red}[{white}1{red}] ĐỔI AUTH

{red}[{white}2{red}] DÙNG AUTH CŨ'''

    pr3(text)

    changetoken=cint(f'{red}NHẬP LỰA CHỌN: {green}')

    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

    if changetoken==1:

      file_name = 'cache_golike_auth.txt'

      if os.path.exists(file_name):

          os.remove(file_name)

    else:

      pass

      















def banner(red,green,blue,yellow,cyan,pink):

  text=f'''

Pham Van Tung 

'''

 

  pr3(text)

  text=f'''{red}            ┌───────────────────────┐ 

{red}            ║ {green}   GOLIKE - TIKTOK  {red}  ║

{red}            └───────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{red}MỌI NGƯỜI {cyan}CHÚ Ý!!!!

 ~[+]{green}TIỀN SAU KHI LÀM NVỤ SẼ ĐƯỢC CỘNG SAU VÀI PHÚT

 ~[+]{blue}KIỂM TRA KHÔNG THẤY LÊN XU KO PHẢI DO TOOL LỖI 

 ~[+]{pink}MÀ DO HỆ THỐNG GOLIKE CHƯA LOAD!!!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''

  pr3(text)























































def bes4(url):

  html_source = requests.get(url).text

  soup = BeautifulSoup(html_source, 'html.parser')

  og_description = soup.find('meta', {'property': 'og:description'})

  if og_description:

      text =og_description['content']

      return text

  else:

      print("Không tìm thấy thẻ meta với thuộc tính property='og:description'")











def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

 while True :

  while True :

    if not os.path.exists("cache_golike_auth.txt"):

      auth=str(input(f'~[+]{red}NHẬP AUTH:{green} '))

      headers ={

    'Authorization'	:auth,

    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

 }

      check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)

      if check['status']==200:

        name=check['data'][0]['username']

        hea={

'Authorization':auth,

't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

}

# Chuỗi JSON đầu vào

        data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text

        try:

          data=json.loads(data)

        except :

          break

        # Tính tổng pending coin

        total_pending_coin = 0

        for key, value in data.items():

            if isinstance(value, dict) and 'pending_coin' in value:

                total_pending_coin += value['pending_coin']

        xht=data['current_coin']

        text=f'~[+]{red}SUCCESS'

        text=f'{red}TÊN TÀI KHOẢN: {green} {name}'

        pr(text)

        text=f'{green}${red} HIỆN TẠI :{green}{xht}đ'

        pr(text)

        # In tổng pending coin

        text=f'{green}${red} CHỜ DUYỆT:{green}{total_pending_coin}đ'

        pr(text)

        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

        text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '

        pr(text)

        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]

        for i, nickname in enumerate(nicknames, start=1):

            globals()[f'{i}'] = nickname

        # In giá trị của các biến

        for i, nickname in enumerate(nicknames, start=1):

            text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'

            pr(text)

        with open("cache_golike_auth.txt", "w") as state_file:

          state_file.write(auth)

        return auth,check

      else:

        text=f'~[+]{red}FAIL AUTH KHÔNG CHÍNH XÁC>>{green}VUI LÒNG NHẬP LẠI'

        continue 

    else:

     with open('cache_golike_auth.txt') as f:

        lines = f.readlines()

        auth=lines[0]

        headers ={

      'Authorization'	:auth,

      't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

      'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

      }

        check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)

        if check['status']==200:

          name =check['data'][0]['username']

          hea={

                'Authorization':auth,

                't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                  }





          data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text

          try:

            data=json.loads(data)

          except :

            break

          # Tính tổng pending coin

          total_pending_coin = 0

          for key, value in data.items():

              if isinstance(value, dict) and 'pending_coin' in value:

                  total_pending_coin += value['pending_coin']

          xht=data['current_coin']

          text=f'{red}TÊN TÀI KHOẢN: {green} {name}'

          pr(text)

          text=f'{green}${red} HIỆN TẠI :{green}{xht}đ'

          pr(text)

          # In tổng pending coin

          text=f'{green}${red} CHỜ DUYỆT:{green}{total_pending_coin}đ'

          pr(text)

          nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]

          for i, nickname in enumerate(nicknames, start=1):

              globals()[f'{i}'] = nickname

          print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

          text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '

          pr(text)

          # In giá trị của các biến

          for i, nickname in enumerate(nicknames, start=1):

              text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'

              pr(text)

              

        return auth, check









def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

  while True :

    

    user_input=input(f'~[+]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {green}CHỌN ACC TIKTOK MUỐN CHẠY JOB:{green} ')

    try:

      n = int(user_input)

      if 'data' in check and len(check['data']) >= n:

          idtiktok = check['data'][n-1]['id']

          if idtiktok :

              text=f"{red}ID CỦA NICKNAME SỐ {n} LÀ: {green}{idtiktok}"

              pr(text)

              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

              return idtiktok 

          else:

              text=f"{red}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."

              pr(text)

      else:

          continue 

    except ValueError:

          pr(f"{red}VUI LÒNG CHỈ NHẬP SỐ.")

          continue 











def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

    startmaxjob=1

    job_success=0

    hea={

'Authorization':	auth,

't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

}

    while True:

      while True:

        try:

              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()

              break

        except:

            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")

            sleep(2)

            pass

      try:

        link=a['data']['link']

        id=a['data']['id']

        object_id=a['lock']['object_id']

        os.system(f'termux-open-url {link}')

        for k in range(delay,-1,-1):

            mau=random.choice(ranmau)

            print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{random.choice(ranmau)}LOADING{random.choice(ranmau)}>>{yellow}NVỤ MỚI SAU{random.choice(ranmau)}>>{random.choice(ranmau)}[{k}s]',end='\r')

            sleep(1)

        print(f'{green}Đang kiểm tra hành động...',end='\r')

        headers = {

            'authorization': auth,

        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                      }

      

        json_data = {

            'ads_id': id,

            'account_id': idtiktok ,

            'async': True,

            'data': None,

                      }

        while True:

            try:

                g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                break

            except:

                print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")

                sleep(2)

                pass

        if g['status']==200:

            job_success+=1

            print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')

            startmaxjob+=1

            jobloi=0

            if startmaxjob == maxjob+1:

                print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')

                return



        else:

            print(f'{green}Đang kiểm tra lại hành động...',end="\r")

            sleep(2)

            while True:

                try:

                    g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                    break

                except:

                    print(f'{red}Đang nhận lại phần thưởng...',end="\r")

                    sleep(2)

            if g['status']==200:

                job_success+=1

                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')

                startmaxjob+=1

                jobloi=0

                if startmaxjob == maxjob+1:

                    print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')

                    return

            else:

                print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')

                headers = {

                    'authorization': auth,

                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                            }

                

                json_data = {

                    'description': 'Báo cáo hoàn thành thất bại',

                    'users_advertising_id': id,

                    'type': 'ads',

                    'provider': 'tiktok',

                    'fb_id': idtiktok ,

                    'error_type': 3,

                              }

                

                requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)

            

              

                headers = {

                    'authorization': auth,

                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                          }

                

                json_data = {

                    'ads_id': id,

                    'object_id': object_id,

                    'account_id': idtiktok ,

                    'type': 'follow',

                              }

                skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)

                startmaxjob+=1

                jobloi+=1

                if startmaxjob == maxjob+1:

                    print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')

                    return

                elif jobloi==15:

                    select=input(f'{red}Lỗi nhiều ,Bạn có muốn đổi nick?(y/n):')

                    if select.lower() == 'n':

                        pass

                    else:

                        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]

                        for i, nickname in enumerate(nicknames, start=1):

                            globals()[f'{i}'] = nickname

                        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

                        text=f'~[+]{red}SELECT {green}ACC CHẠY NHIỆM VỤ '

                        pr(text)

                        # In giá trị của các biến

                        for i, nickname in enumerate(nicknames, start=1):

                            text=f'{red}[{green}{i}{red}]: {globals()[f"{i}"]}'

                            pr(text)

                        idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

                        jobloi=0



      except:

          print(f'{red}Đang nhận lại nhiệm vụ...',end='\r')

          sleep(2)



  



def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

    startmaxjob=1

    job_success=0

    jobloi=0

    hea={

'Authorization':	auth,

't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

}

    while True:

      while True:

        try:

              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()

              break

        except:

            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")

            sleep(2)

            pass

      try:

        link=a['data']['link']

        id=a['data']['id']

        object_id=a['lock']['object_id']

        if 'video' in link:

            print(f"{red}ĐANG LỌC JOB LIKE           ",end='\r')

            headers = {

                'authorization': auth,

                't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                        }

            

            json_data = {

                'description': 'Tôi không muốn làm Job này',

                'users_advertising_id': id,

                'type': 'ads',

                'provider': 'tiktok',

                'fb_id': idtiktok,

                'error_type': 0,

                        }



            response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)



            

            json_data = {

                'ads_id': id,

                'object_id': object_id,

                'account_id': idtiktok,

                'type': 'like',

                        }

            response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)

        else:  

            os.system(f'termux-open-url {link}')

            for k in range(delay,-1,-1):

                mau=random.choice(ranmau)

                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{random.choice(ranmau)}LOADING{random.choice(ranmau)}>>{yellow}NVỤ MỚI SAU{random.choice(ranmau)}>>{random.choice(ranmau)}[{k}s]',end='\r')

                sleep(1)

            print(f'{green}Đang kiểm tra hành động...',end='\r')

            headers = {

                'authorization': auth,

            't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                         }

          

            json_data = {

                'ads_id': id,

                'account_id': idtiktok ,

                'async': True,

                'data': None,

                         }

            while True:

                try:

                    g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                    break

                except:

                    print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")

                    sleep(2)

                    pass

            if g['status']==200:

                job_success+=1

                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')

                startmaxjob+=1

                jobloi=0

                if startmaxjob == maxjob+1:

                    print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')

                    return



            else:

                print(f'{green}Đang kiểm tra lại hành động...',end="\r")

                sleep(2)

                while True:

                    try:

                        g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                        break

                    except:

                        print(f'{red}Đang nhận lại phần thưởng...',end="\r")

                        sleep(2)

                if g['status']==200:

                    job_success+=1

                    print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')

                    startmaxjob+=1

                    jobloi=0

                    if startmaxjob == maxjob+1:

                        print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')

                        return

                else:

                    print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')

                    headers = {

                        'authorization': auth,

                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                                }

           