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
	host = raw_input(C+'[*]'+W+'asm>[ip_history] Host/ip: ') # Target
	dom = flib(host) # Bad Protocol [http:// https://]
	if chost(dom) == True: # Check Domain
		print '[*] Starting ... [*]'
		print '[*] ip/host %s is Activ [*]'%dom
		print '[*] Please White ... [*]'
		# def psend(host):
		send = urlopen('http://www.viewdns.info/iphistory/?domain='+dom).read() # Send Request
		bs = BeautifulSoup(send,'html.parser').find('font',face="Courier")
		recv =str(bs).replace('ViewDNS.info','')
		try:
			rand = str(randint(0,2000))
			fname = rand+'ip_history_'+dom.replace('.','_')+'.html' # File Name
			fsave = saved(recv,fname) # Saved To File
			if(fsave==True):
				print '[*] Saved To output/'+fname+' success [*]' # Save True
			elif(fsave==False):
				print '[*] bad to saved file [*]' # Save False
			else:
				pass
			print GR+'[Type 98 to Back]'+W
			print GR+'[Type 99 to Exit]'+W
			print GR+'[Type 100 to options]'+W
			print W+'[*] END [*]' # End Process
		except:
			print '[-] oops error [-]' # Error
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error Host
		print W+'[*] END [*]'
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)