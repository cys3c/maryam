# import modules for colors
from lib.color.dtectcolors import Style,Fore,Back,init
init()
W  =   Style.BRIGHT+Fore.WHITE # white
GR =   Style.DIM+Fore.WHITE    # gray
C  =   Style.BRIGHT+Fore.GREEN # green
R  =   Fore.RED 			   # red
B  =   Fore.BLUE  			   # blue
Y  =   Fore.YELLOW			   # yellow
import sys
def start():
	import requests
	from bs4 import BeautifulSoup
	value = raw_input(C+'[*]'+W+'asm>[hashAnalyzer]> Hash:')
	try:
		if len(value)>0:
			reqsend = requests.post('http://md5decrypt.net/en/HashFinder/',{'hash':value,'crypt':'Search'}).content
			if reqsend == None:
				print R+'[*] ERROR NULL [*]'
			else:
				bs = BeautifulSoup(reqsend,'html.parser')
				print C+str(bs.find('fieldset',{'class':"trouve"}).text).replace('|','\n')
				print GR+'[Type 98 to Back]'+W
				print GR+'[Type 99 to Exit]'+W
				print GR+'[Type 100 to options]'+W
		else:
			start()
	except:
		print R+'[*] ERROR NULL [*]'
		start()
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)