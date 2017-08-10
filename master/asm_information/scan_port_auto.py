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
	from random import randint
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[scan_port_auto] Host/ip: ') # Target
	file = raw_input(C+'[*]'+W+'asm>[scan_port_auto] show File output?y/n ') # y = Save To File n = Show Recv
	dom = flib(host)
	xdom = 'https://api.hackertarget.com/nmap/?q='+dom
	if chost(dom) == True: # Check For Host
		print '[*] Starting ... [*]'
		print '[*] ip/host %s is Activ [*]'%dom
		print '[*] Please White ... [*]'
		try:
			rQx = urlopen(xdom).read() # Send Request
			print '[*] Request Send [*]'
			if (file == 'y' or file == 'Y'):
				rand = str(randint(0,2000))
				fname = rand+'scan_port_auto_'+dom.replace('.','_')+'.html' # File Name
				fsave = saved(rQx,fname) # Save To File
				if(fsave==True):
					print '[*] Saved To output/'+fname+' success [*]' # Save True
				elif(fsave==False):
					print '[*] bad to saved file [*]' # Save False
				else:
					pass
			elif(file == 'n' or file == 'N'):
				print
				print C+rQx # Show Recv
				print
			else:
				print
				print '\t'+C+rQx # Show Recv
				print
			print W+'[*] END [*]' # End Process
		except:
			print '[-] oops error [-]' # Error Null :(
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error Host
		print W+'[*] END [*]' # End Process
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)