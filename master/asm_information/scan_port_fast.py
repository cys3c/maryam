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
	import socket
	from lib._fileSave import saved
	from random import randint
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[scan_port_fast] Host/ip: ') # Target
	dom = flib(host) # Bad Value Protocol [http:// https://]
	# Check For host
	if chost(dom) == True:
		star = raw_input(C+'[*]'+W+'asm>[scan_port_fast] start range: ')
		end = raw_input(C+'[*]'+W+'asm>[scan_port_fast] end range: ')
		file = raw_input(C+'[*]'+W+'asm>[scan_port_fast] show File output?y/n ')
		def psend(host,port,f=False):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(8)
			try:
				send = s.connect_ex((host,port))
			except:
				send = 10035
			if send == 0:
				if f == False:
					return C+'\tport '+str(port)+' is open !'
				else:
					return '\tport '+str(port)+' is open !\n'

			elif send == 10035:
				if f == False:
					return R+'\tport '+str(port)+' is close !'
				else:
					return '\tport '+str(port)+' is close !\n'
			else:
				if f == False:
					return R+'\tport '+str(port)+' is close !'
				else:
					return '\tport '+str(port)+' is close !\n'
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] start range '+str(star)+' up to '+str(end)+' [*]'
			print '[*] Please White ... [*]'
			rand = str(randint(0,2000))
			fname = rand+'scan_port_fast_'+dom.replace('.','_')+'.html' # File Name
			if (file == 'y' or file == 'Y'): # Save File
				for x in range(int(star),int(end)):
					recv = psend(dom,x,True)
					fsave = saved(recv,fname)
				if(fsave==True):
					print '[*] Saved To output/'+fname+' success [*]' # File Save True
				elif(fsave==False):
					print '[*] bad to saved file [*]' # File Save False
				else:
					pass
			elif(file == 'n' or file == 'N'): # Show Recv
				print
				for x in range(int(star),int(end)):
					print psend(dom,x)
				print
			else:
				print
				for x in range(int(star),int(end)):
					print psend(dom,x)
				print
			print W+'[*] END [*]' # End Process
		except:
			print '[-] oops error [-]' # Error :(
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom# Error For Host
		print W+'[*] END [*]'
		start()# Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)