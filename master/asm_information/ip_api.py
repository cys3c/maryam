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
	from requests import get
	from socket import gethostbyname
	from random import randint
	from lib._fileSave import saved
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[ipapi] Host/ip: ') # Target
	file = raw_input(C+'[*]'+W+'asm>[ipapi] show File output?y/n ') # y = Save To File n = Show Recv
	dom = flib(host)
	if chost(dom) == True: # Check For Host
		print '[*] Starting ... [*]'
		print '[*] ip/host %s is Activ [*]'%dom
		print '[*] Please White ... [*]'
		url = gethostbyname(dom)
		xdom = 'https://ipapi.co/'+url+'/json';
		index = ['ip', 'city', 'region', 'country','country_name', 'postal','latitude', 'longitude', 'timezone', 'asn','org'] # Option
		usage = {'user-agent': 'ipapi/ipapi-python/0.5.1'} # User Agent
		try:
			rQx = get(xdom,headers=usage).json() # Request Send
			print '[*] Request Send [*]'
			if (file == 'y' or file == 'Y'):# Save To File
				rand =str(randint(0,2000))
				fname = '../../../output/'+rand+'ipapi_'+dom.replace('.','_')+'.html' # File Name
				for x in index:
					output = str(x)+' : '+str(rQx[x])+'\n'
					fsave = saved(output,fname)
				if(fsave==True):
					print '[*] Saved To output/'+fname+' success [*]' # Save True
				elif(fsave==False):
					print '[*] bad to saved file [*]' # Save False
				else:
					pass
			elif(file == 'n' or file == 'N'): # Show Recv
				print
				for x in index:
					output = C+str(x)+' : '+str(rQx[x])
					print '\t'+output
				print
			else:
				print
				for x in index:
					output = C+str(x)+' : '+str(rQx[x])
					print '\t'+output
				print
			print W+'[*] END [*]'# End Process
			print GR+'[Type 98 to Back]'+W
			print GR+'[Type 99 to Exit]'+W
			print GR+'[Type 100 to options]'+W
		except:
			print '[-] oops error [-]' # Error Null :(
	else:
		print R+'[-]'' oops Error(%s) occured; Server offline or invalid URL [-]'%dom # Error Host
		print W+'[*] END [*]'
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)