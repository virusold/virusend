import requests, threading
print("""
░░░░▄██▀░░░░░░░░░░░░░░░░▀▀█▄░░░░
░░░▄█▀░░░░░░░░░░░░░░░░░░░░▀█▄░░░
░░░█▀░░░instagram : @mzo9 ░░░▀█▄░
░░██░░░░░░░░#ViRuS░░░░░░░░██░░
░░▀█▄░░░░░░░░░░░░░░░░░░░░░░░██░░
░░░██░░░░░▄▄▄▄░░░░░▄▄▄▄░░░░██░░░
░░░░█▄░░░██████░░░██████░░██░░░░
▄▄░░░██░░█████░░░░▀█████░░█░░░▄▄
▀█▄░░██░░░▀▀░░▄██▄░░▀▀▀░░▄█░░▄█▀
░▀▀████▄▄▄░░░██████░░░░▄▄████▀▀░
██▄▄░▀▀████▄░▀██▀██░▄████▀▀░▄▄██
░░▀▀██▄▄████▄▄▄▄▄▄▄▄████▄▄██▀▀░░
░░░░░░▀▀██░█░█░█░█░█░███▀▀░░░░░░
░░░░▄▄████▀█▄█▄█▄█▄█▄█████▄▄░░░░
▀███▀▀░▄▄███░█░█░█░█▄███▄░▀▀▀██▀
█▄░░▄██▀▀░▀███▄█▄█▄██▀░▀▀██▄░░░█                            
  """)
username = input("Username : ")
password = input("Password : ")
target = input("Target : ")
thread = int(input("Thread : 40 "))
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'x-csrftoken': 'xX0K5q7XikrU1LAnenqEVKqb7J3qK4S6',
        'x-ig-app-id': '936619743392459',
        'x-instagram-ajax': '0c15f4d7d44a',
        'x-requested-with': 'XMLHttpRequest'
    }
Att = 0
email = ''
phone = ''
def edit():
   global cookies, Att
   try:
    r = requests.get('https://www.instagram.com/accounts/edit/?__a=1', headers=headers, cookies=cookies)
    email = r.json()['form_data']['email']
    phone = r.json()['form_data']['phone_number']
   except:
     email = email
     phone = phone
   data = {
   'first_name': '',
   'email': email,
   'username': target,
   'phone_number': phone,
   'biography': '',
   'external_url': '',
   'chaining_enabled': 'on'
   }
   hed ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Chromium\";v=\"88\", \"Google Chrome\";v=\"88\", \";Not A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "X-Forwarded-For": "127.0.0.1",
    "cookie": f"csrftoken = lHu2G6ufrioyFae7vIoGcGp1KqQrFwsz; mid=YBKjjQABAAEPTdtEMhPWWkk2bTmt; ds_user=71oc; igfl=71oc; ds_user_id=43805713213; sessionid={cookies['sessionid']}; rur=FTW;  urlgen=""""{\""104.248.132.80\"": ""14061}:1l55ih:ZNLfYDbSXdajQO6fS7AJKWjoAbs""""; is_starred_enabled=yes",
    "x-csrftoken": "lHu2G6ufrioyFae7vIoGcGp1KqQrFwsz",
    "x-ig-app-id": "936619743392459",
    "x-ig-www-claim": "hmac.AR1bu79iGjS6uRI_mZP2RUj8pSnIBTZShHgt5Jltb_549G1Z",
    "x-instagram-ajax": "1cb44f68ffec",
    "x-requested-with": "XMLHttpRequest"
}
   while True:
    try:
     req = requests.post('https://www.instagram.com/accounts/edit/', data=data, headers=hed)
     if req.status_code == 200:
       print(f'[DN] Swapped @{target} by #ViRus ')
       print(' instagram : @mzo9 ')
       print(' Thank You ')
       break
       exit()
     elif req.status_code == 400:
       Att += 1
       print(f'\r[REQ] Request > {Att}', end='')
     elif req.status_code == 429:
       print(f'\r[BLC] Blocked @{username}', end='')
       break
       exit()
    except:
       edit()
data = {
    "username": username,
    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
    "queryParams": "{}",
    "optIntoOneTap": "false"
}
url = "https://www.instagram.com/accounts/login/ajax/"
req = requests.post(url, data=data, headers=headers)
if "Please wait a few minutes before you try again." in req.text:
    print("[PWA] Please wait a few minutes before you try again.")
elif ("checkpoint_url")  in req.text:
    ch = req.json()['checkpoint_url']
    cookies = req.cookies
    ur = 'https://www.instagram.com' + ch
    re = requests.post(ur, data="", headers=headers, cookies=cookies)
    if ("phone_number") in re.text:
        print("[PH] Phone : 0")
    if ("email") in re.text:
        print("[EM] Email : 1")
    choice = input("[ED] Enter Mode : ")
    datt = {
        "choice": choice
    }
    re = requests.post(ur, data=datt, headers=headers, cookies=cookies)
    if ("security_code") in re.text:
      if choice == "1":
        print("[DN] Done Send To Email")
      elif choice == "0":
        print("[DN] Done Send To Phone")
      Code = input("[EC] Enter Code : ")
      da = {
         "security_code": Code
      }
      r = requests.post(ur, headers=headers, data=da, cookies=cookies)
      if ("ok") in r.text:
          cookies = r.cookies
          print(f'[DN] Done Login @{username}')
          input('[AYR] Are You Ready ?')
          threads = []
          for i in range(thread):
            th = threading.Thread(target=edit)
            th.start()
            threads.append(th)
          for thread2 in threads:
            thread2.join()
      else:
          print("[EC] Code Error")
elif ("userId") in req.text:
     cookies = req.cookies
     print(f'[DN] Done Login @{username}')
     input('[AYR] Are You Ready ?')
     threads = []
     for i in range(thread):
       th = threading.Thread(target=edit)
       th.start()
       threads.append(th)
     for thread2 in threads:
       thread2.join()
elif ("two_factor") in req.text:
    ss = req.json()['two_factor_info']['two_factor_identifier']
    cookies = req.cookies
    Code = input("[EC] Enter Code : ")
    data = {
    'username': username,
    'verificationCode': Code,
    'identifier': ss,
    'queryParams': '{"next":"/"}'
    }
    re = requests.post('https://www.instagram.com/accounts/login/ajax/two_factor/', headers=headers, data=data, cookies=cookies)
    if ("userId") in re.text:
          cookies = re.cookies
          print(f'[DN] Done Login @{username}')
          input('[AYR] Are You Ready ?')
          threads = []
          for i in range(thread):
            th = threading.Thread(target=edit)
            th.start()
            threads.append(th)
          for thread2 in threads:
            thread2.join()
    elif ("Please wait a few minutes before you try again.") in re.text:
     print("[PWA] Please wait a few minutes before you try again.")
    else:
          print("[EC] Code Error")
else:
    print('[WUP] Wrong Username Or Password')
    print(' instagram @mzo9 ')
    print(' Thank you ')