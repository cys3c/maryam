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
	from lib._fileSave import saved
	from random import randint
	from requests import post
	from bs4 import BeautifulSoup
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[traceroute] Host/ip: ') # Target
	file = raw_input(C+'[*]'+W+'asm>[traceroute] show File output?y/n ') # y = Save To File
	dom = flib(host) # Bad protocol [http:// https://]
	if chost(dom) == True: # Check For Host
		print '[*] Starting ... [*]'
		print '[*] ip/host %s is Activ [*]'%dom
		print '[*] Please White ... [*]'
		try:
			rQx = post('http://www.ipaddressguide.com/traceroute',{'host':dom}).content # Request Send
			bs = BeautifulSoup(rQx,'html.parser').code.text # Parser Page
			print '[*] Request Send [*]'
			if (file == 'y' or file == 'Y'):# Save To File
				rand = str(randint(0,2000))
				fname = rand+'traceroute_'+dom.replace('.','_')+'.html' # FileName
				fsave = _fileSave.saved(bs,fname)
				if(fsave==True):
					print '[*] Saved To output/'+fname+' success [*]' # Save True
				elif(fsave==False):
					print '[*] bad to saved file [*]' # Save False
				else:
					pass
			elif(file == 'n' or file == 'N'): # show recv
				print
				print C+bs
				print
			else:
				print
				print C+bs
				print

			print W+'[*] END [*]' # End Process
		except:
			print '[-] oops error [-]' # Error
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error Host
		print W+'[*] END [*]' # End Process
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)