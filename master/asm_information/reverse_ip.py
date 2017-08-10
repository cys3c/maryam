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
	from requests import post
	import json
	from random import randint
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[reverse_ip] Host/ip: ') # Target
	file = raw_input(C+'[*]'+W+'asm>[reverse_ip] show File output?y/n ') # y = Save To File n = Show Recv
	dom = flib(host) # Bad protocol [http:// https://]
	xdom = 'http://domains.yougetsignal.com/domains.php';
	if chost(dom) == True: # Check For Host
		print '[*] Starting ... [*]'
		print '[*] ip/host %s is Activ [*]'%dom
		print '[*] Please White ... [*]'
		try:
			rQx = post(xdom, {'remoteAddress':dom}) # Request Send
			print '[*] Request Send [*]'
			data = json.loads(rQx.text) # Json Load
			sors= "\tSorgulanan Site = " + data["remoteAddress"] + '\n'
			tops= "\tToplam Site = " + data["domainCount"] + '\n'
			ipas= "\tIP Adresi = " + data["remoteIpAddress"] + '\n'
			reverse = str(sors+tops+ipas) # All
			if (file == 'y' or file == 'Y'): # Save To File
				rand = str(randint(0,2000))
				fname = rand+'reverseip_'+dom.replace('.','_')+'.html' # File Name
				fsave = saved(reverse,fname)
				for domain in (data["domainArray"]):
					fsave = saved('\t'+domain[0]+'\n',fname)
				if(fsave==True):
					print '[*] Saved To output/'+fname+' success [*]' # Save True
				elif(fsave==False):
					print '[*] bad to saved file [*]' # Save False
				else:
					pass
			elif(file == 'n' or file == 'N'): # Show Recv
				print
				print C+reverse
				for domain in (data["domainArray"]):
					print(C+'\t'+domain[0]) # Show Data
				print
			else:
				print
				print C+reverse
				for domain in (data["domainArray"]):
					print(C+'\t'+domain[0]) # Show Data
				print
			print W+'[+] End [+]'
		except:
			print '[-] oops error [-]'
			print W+'[+] End [+]'
			print GR+'[Type 98 to Back]'+W
			print GR+'[Type 99 to Exit]'+W
			print GR+'[Type 100 to options]'+W
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error Host is Ofline or invalid url
		print W+'[*] END [*]'
		start() # continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)