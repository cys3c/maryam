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
	import urllib
	from random import randint
	from lib.check import flib,chost
	host = raw_input(C+'[*]'+W+'asm>[dnsmap] Host/ip: ')
	dom = flib(host)
	if chost(dom) == True:
		print '[*] Starting ... [*]'
		print '[*] ip/host %s is Activ [*]'%dom
		print '[*] Please White ... [*]'
		xdom = 'https://dnsdumpster.com/static/map/'+dom+'.png';
		rand = str(randint(0,2000))
		fname = rand+'dns_map_'+dom.replace('.','_')+'.jpg' # File Name
		try:
			rQx = urllib.urlretrieve(xdom, '../../output/'+fname)
			print '[*] Request Send [*]'
			print '[*] Saved To output/'+fname+' success [*]' # Save True
			print W+'[*] END [*]' # End Process
			print GR+'[Type 98 to Back]'+W
			print GR+'[Type 99 to Exit]'+W
			print GR+'[Type 100 to options]'+W
		except:
			print '[-] oops error [-]' # Save False
	else:
		print R+'[-]'' oops Error(%s) occured; invalid URL [-]'%dom # Error Host
		print W+'[*] END [*]' # End Process
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)