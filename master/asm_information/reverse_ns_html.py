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
	from random import randint
	from bs4 import BeautifulSoup
	from lib._fileSave import saved
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[reverse_ns] Host: ') # Target
	dom = flib(host) # Bad protocol [http:// https://]
	if chost(dom) == True: # Check For Host
		def psend(host):
			send = urlopen('http://www.viewdns.info/reversens/?ns='+host).read() # Send Request
			bs = BeautifulSoup(send,'html.parser').find('font',face="Courier") # Parser Page
			return str(bs).replace('''<script class="stripe-button" data-amount="19900" data-currency="usd" data-description="Full report for 'google.com'" data-image="/images/ok.GIF" data-key="pk_live_ey9TT0KvaFQoLWRyDYg9oqQd" data-label="Download The Full Report for $199" data-name="" src="https://checkout.stripe.com/checkout.js"></script>''','')
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] Please White ... [*]'
			rand = str(randint(0,2000))
			fname = rand+'reverse_ns_'+dom.replace('.','_')+'.html' # File Name
			recv = psend(dom)
			fsave = saved(recv,fname) # Save To File
			if(fsave==True):
				print '[*] Saved To output/'+fname+' success [*]' # Seve True
			elif(fsave==False):
				print '[*] bad to saved file [*]' # Save False
			else:
				pass
			print W+'[*] END [*]' # End process
		except:
			print '[-] oops error [-]'
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error Host is Ofline or invalid url
		print W+'[*] END [*]'
		start() # continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)