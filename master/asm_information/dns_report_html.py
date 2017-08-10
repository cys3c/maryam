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
	# import
	from urllib import urlopen
	from lib._fileSave import saved
	from bs4 import BeautifulSoup
	from random import randint
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[dns_report] Host/ip: ') # Target
	dom = flib(host)
	if chost(dom) == True: # Check For Host
		def psend(host):
			send = urllib.urlopen('http://www.viewdns.info/dnsreport/?domain='+host).read()
			bs = bs4.BeautifulSoup(send,'html.parser').find('font',face="Courier")
			return str(bs).replace('ViewDNS.info','')
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] Please White ... [*]'
			rand = str(randint(0,2000))
			fname = rand+'dns_report_'+dom.replace('.','_')+'.html' # File Name
			recv = psend(dom)
			fsave = saved(recv,fname)
			if(fsave==True):
				print '[*] Saved To output/'+fname+' success [*]'
			elif(fsave==False):
				print '[*] bad to saved file [*]'
			else:
				pass
			print W+'[*] END [*]'
			print GR+'[Type 98 to Back]'+W
			print GR+'[Type 99 to Exit]'+W
			print GR+'[Type 100 to options]'+W
		except:
			print '[-] oops error [-]' # Error null :(
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error For Host
		print W+'[*] END [*]' # End Process
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)