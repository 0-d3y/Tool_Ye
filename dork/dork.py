import os,re,requests,ctypes
from colorama import Fore,init
from multiprocessing.dummy import Pool
from random import choice
if os.name == "nt":
	os.system("cls")
else:
	os.system("clear")

init(convert=True)

class settings:
	y = Fore.YELLOW
	r = Fore.RED
	b = Fore.BLUE


def clean():
	lines_seen = set()
	outfile = open('sites.txt', "a")
	infile = open('sitelist.txt', "r")
	for line in infile:
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	infile.close()
	if os.name == "nt":
		os.system("del sitelist.txt")
	else:
		os.system("rm -rf sitelist.txt")
	print("[{}+{}] Duplicate sites removed successfully!".format(settings.r,settings.y))
	print("\n[{}+{}] Sites saved as {}sites.txt{}!".format(settings.r,settings.y,settings.b,settings.y))


binglist = {"http://www.bing.com/search?q=&count=50&first=1",
"http://www.bing.com/search?q=&count=50&first=51",
"http://www.bing.com/search?q=&count=50&first=101",
"http://www.bing.com/search?q=&count=50&first=151",
"http://www.bing.com/search?q=&count=50&first=201",
"http://www.bing.com.br/search?q=&count=50&first=1",
"http://www.bing.com.br/search?q=&count=50&first=51",
"http://www.bing.com.br/search?q=&count=50&first=101",
"http://www.bing.at/search?q=&count=50&first=1",
"http://www.bing.at/search?q=&count=50&first=51",
"http://www.bing.at/search?q=&count=50&first=101",
"http://www.bing.be/search?q=&count=50&first=1",
"http://www.bing.be/search?q=&count=50&first=51",
"http://www.bing.be/search?q=&count=50&first=101",
"http://www.bing.cl/search?q=&count=50&first=1",
"http://www.bing.cl/search?q=&count=50&first=51",
"http://www.bing.cl/search?q=&count=50&first=101",
"http://www.bing.co.at/search?q=&count=50&first=1",
"http://www.bing.co.at/search?q=&count=50&first=51",
"http://www.bing.co.at/search?q=&count=50&first=101",
"http://www.bing.com.au/search?q=&count=50&first=1",
"http://www.bing.com.au/search?q=&count=50&first=51",
"http://www.bing.com.au/search?q=&count=50&first=101",
"http://www.bing.com.cn/search?q=&count=50&first=1",
"http://www.bing.com.cn/search?q=&count=50&first=51",
"http://www.bing.com.cn/search?q=&count=50&first=101",
"http://www.bing.cz/search?q=&count=50&first=1",
"http://www.bing.cz/search?q=&count=50&first=51",
"http://www.bing.cz/search?q=&count=50&first=101",
"http://www.bing.de/search?q=&count=50&first=1",
"http://www.bing.de/search?q=&count=50&first=51",
"http://www.bing.de/search?q=&count=50&first=101",
"http://www.bing.dk/search?q=&count=50&first=1",
"http://www.bing.dk/search?q=&count=50&first=51",
"http://www.bing.dk/search?q=&count=50&first=101",
"http://www.bing.ca/search?q=&count=50&first=1",
"http://www.bing.ca/search?q=&count=50&first=51",
"http://www.bing.ca/search?q=&count=50&first=101",
"http://www.bing.sg/search?q=&count=50&first=1",
"http://www.bing.sg/search?q=&count=50&first=51",
"http://www.bing.sg/search?q=&count=50&first=101",
"http://www.bing.se/search?q=&count=50&first=1",
"http://www.bing.se/search?q=&count=50&first=51",
"http://www.bing.se/search?q=&count=50&first=101",
"http://www.bing.pl/search?q=&count=50&first=1",
"http://www.bing.pl/search?q=&count=50&first=51",
"http://www.bing.pl/search?q=&count=50&first=101",
"http://www.bing.no/search?q=&count=50&first=1",
"http://www.bing.no/search?q=&count=50&first=51",
"http://www.bing.no/search?q=&count=50&first=101",
"http://www.bing.nl/search?q=&count=50&first=1",
"http://www.bing.nl/search?q=&count=50&first=51",
"http://www.bing.nl/search?q=&count=50&first=101",
"http://www.bing.net.nz/search?q=&count=50&first=1",
"http://www.bing.net.nz/search?q=&count=50&first=51",
"http://www.bing.net.nz/search?q=&count=50&first=101",
"http://www.bing.lv/search?q=&count=50&first=1",
"http://www.bing.lv/search?q=&count=50&first=51",
"http://www.bing.lv/search?q=&count=50&first=101",
"http://www.bing.lt/search?q=&count=50&first=1",
"http://www.bing.lt/search?q=&count=50&first=51",
"http://www.bing.lt/search?q=&count=50&first=101",
"http://www.bing.it/search?q=&count=50&first=1",
"http://www.bing.it/search?q=&count=50&first=51",
"http://www.bing.it/search?q=&count=50&first=101",
"http://www.bing.is/search?q=&count=50&first=1",
"http://www.bing.is/search?q=&count=50&first=51",
"http://www.bing.is/search?q=&count=50&first=101",
"http://www.bing.in/search?q=&count=50&first=1",
"http://www.bing.in/search?q=&count=50&first=51",
"http://www.bing.in/search?q=&count=50&first=101",
"http://www.bing.ie/search?q=&count=50&first=1",
"http://www.bing.ie/search?q=&count=50&first=51",
"http://www.bing.ie/search?q=&count=50&first=101",
"http://www.bing.hu/search?q=&count=50&first=1",
"http://www.bing.hu/search?q=&count=50&first=51",
"http://www.bing.hu/search?q=&count=50&first=101",
"http://www.bing.fr/search?q=&count=50&first=1",
"http://www.bing.fr/search?q=&count=50&first=51",
"http://www.bing.fr/search?q=&count=50&first=101",
"http://www.bing.com.sg/search?q=&count=50&first=1",
"http://www.bing.com.sg/search?q=&count=50&first=51",
"http://www.bing.com.sg/search?q=&count=50&first=101",
"http://www.bing.co.uk/search?q=&count=50&first=1",
"http://www.bing.co.uk/search?q=&count=50&first=51",
"http://www.bing.co.uk/search?q=&count=50&first=101",
"http://www.bing.co.nz/search?q=&count=50&first=1",
"http://www.bing.co.nz/search?q=&count=50&first=51",
"http://www.bing.co.nz/search?q=&count=50&first=101",
"http://www.bing.co.jp/search?q=&count=50&first=1",
"http://www.bing.co.jp/search?q=&count=50&first=51",
"http://www.bing.co.jp/search?q=&count=50&first=101",
"http://www.bing.ch/search?q=&count=50&first=1",
"http://www.bing.ch/search?q=&count=50&first=51",
"http://www.bing.ch/search?q=&count=50&first=101",
"http://www.bing.com.tr/search?q=&count=50&first=1",
"http://www.bing.com.tr/search?q=&count=50&first=51",
"http://www.bing.com.tr/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.com.ar/search?q=&count=50&first=1",
"http://www.bing.com.ar/search?q=&count=50&first=51",
"http://www.bing.com.ar/search?q=&count=50&first=101",
"http://www.bing.com.co/search?q=&count=50&first=1",
"http://www.bing.com.co/search?q=&count=50&first=51",
"http://www.bing.com.co/search?q=&count=50&first=101",
"http://www.bing.com.es/search?q=&count=50&first=1",
"http://www.bing.com.es/search?q=&count=50&first=51",
"http://www.bing.com.es/search?q=&count=50&first=101",
"http://www.bing.fi/search?q=&count=50&first=1",
"http://www.bing.fi/search?q=&count=50&first=51",
"http://www.bing.fi/search?q=&count=50&first=101",
"http://www.bing.bo/search?q=&count=50&first=1",
"http://www.bing.bo/search?q=&count=50&first=51",
"http://www.bing.bo/search?q=&count=50&first=101",
"http://www.bing.com.do/search?q=&count=50&first=1",
"http://www.bing.com.do/search?q=&count=50&first=51",
"http://www.bing.com.do/search?q=&count=50&first=101",
"http://www.bing.gr/search?q=&count=50&first=1",
"http://www.bing.gr/search?q=&count=50&first=51",
"http://www.bing.gr/search?q=&count=50&first=101",
"http://www.bing.com.hk/search?q=&count=50&first=1",
"http://www.bing.com.hk/search?q=&count=50&first=51",
"http://www.bing.com.hk/search?q=&count=50&first=101",
"http://www.bing.com.hr/search?q=&count=50&first=1",
"http://www.bing.com.hr/search?q=&count=50&first=51",
"http://www.bing.com.hr/search?q=&count=50&first=101",
"http://www.bing.com.mx/search?q=&count=50&first=1",
"http://www.bing.com.mx/search?q=&count=50&first=51",
"http://www.bing.com.mx/search?q=&count=50&first=101",
"http://www.bing.com.my/search?q=&count=50&first=1",
"http://www.bing.com.my/search?q=&count=50&first=51",
"http://www.bing.com.my/search?q=&count=50&first=101",
"http://www.bing.ph/search?q=&count=50&first=1",
"http://www.bing.ph/search?q=&count=50&first=51",
"http://www.bing.ph/search?q=&count=50&first=101",
"http://www.bing.com.pr/search?q=&count=50&first=1",
"http://www.bing.com.pr/search?q=&count=50&first=51",
"http://www.bing.com.pr/search?q=&count=50&first=101",
"http://www.bing.pt/search?q=&count=50&first=1",
"http://www.bing.pt/search?q=&count=50&first=51",
"http://www.bing.pt/search?q=&count=50&first=101",
"http://www.bing.com.ro/search?q=&count=50&first=1",
"http://www.bing.com.ro/search?q=&count=50&first=51",
"http://www.bing.com.ro/search?q=&count=50&first=101",
"http://www.bing.ru/search?q=&count=50&first=1",
"http://www.bing.ru/search?q=&count=50&first=51",
"http://www.bing.ru/search?q=&count=50&first=101",
"http://www.bing.com.sa/search?q=&count=50&first=1",
"http://www.bing.com.sa/search?q=&count=50&first=51",
"http://www.bing.com.sa/search?q=&count=50&first=101",
"http://www.bing.si/search?q=&count=50&first=1",
"http://www.bing.si/search?q=&count=50&first=51",
"http://www.bing.si/search?q=&count=50&first=101",
"http://www.bing.sk/search?q=&count=50&first=1",
"http://www.bing.sk/search?q=&count=50&first=51",
"http://www.bing.sk/search?q=&count=50&first=101",
"http://www.bing.com.ua/search?q=&count=50&first=1",
"http://www.bing.com.ua/search?q=&count=50&first=51",
"http://www.bing.com.ua/search?q=&count=50&first=101",
"http://www.bing.com.uy/search?q=&count=50&first=1",
"http://www.bing.com.uy/search?q=&count=50&first=51",
"http://www.bing.com.uy/search?q=&count=50&first=101",
"http://www.bing.vn/search?q=&count=50&first=1",
"http://www.bing.vn/search?q=&count=50&first=51",
"http://www.bing.vn/search?q=&count=50&first=101"}
site = 0
error = 0
def dorkscan(dork):
	global site,error
	for bing in binglist:
		bingg = bing.replace("&count",dork + "&count")
		try:
		  x = requests.session()
		  r = x.get(bingg)
		  x.proxies = {'http': 'socks4://{}'.format(choice(proxy)),'https': 'socks4://{}'.format(choice(proxy))}
		  checktext = r.text
		  checktext = checktext.replace("<strong>","")
		  checktext = checktext.replace("</strong>","")
		  checktext = checktext.replace('<span dir="ltr">','')
		  checksites = re.findall('<cite>(.*?)</cite>',checktext)
		  for sites in checksites:
		  	#site = site + 1
		  	sites = sites.replace("http://","protocol1")
		  	sites = sites.replace("https://","protocol2")
		  	sites = sites + "/"
		  	site = sites[:sites.find("/")+0]
		  	site = site.replace("protocol1","http://")
		  	site = site.replace("protocol2","https://")
		  	site = site.replace('<span class="" dir="ltr">','')
		  	if "http" in site:
		  		print(site + "/")
		  	else:
		  		print("http://" + site + "/")
		  	try:
		  		with open("sitelist.txt","a") as f:
		  			if "http" in site:
		  				f.write(site + "/" + "\n")
		  			else:
		  				f.write("http://" + site + "/" + "\n")
		  	except:
		  		pass
		except:
			pass


print("""{} The Yemeni Ghost & Utchiha505 Dork Scanner
""".format(settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y,settings.r,settings.y))

dorklist = input("[{}*{}] Dorklist : ".format(settings.r,settings.y))

def ok() :
    global proxy
    #inp = input('Enter proxy : ')
    #wit = open(inp,'r',errors='ignore').read().splitlines()
    dorks = open(dorklist, 'r',errors='ignore').read().splitlines()
    pro = input('[*] Proxy Socks 4 : ')
    prox = open(pro,'r',errors='ignore').read().splitlines()
    proxy = [items.strip() for items in prox]
    print("[{}+{}] Scan started! Please wait... :)".format(settings.r,settings.y))
    pp = Pool(50)
    pr = pp.map(dorkscan,dorks)

ok()