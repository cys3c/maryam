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
	import socket	
	from lib.check import chost,flib
	host = raw_input(C+'[*]'+W+'asm>[scanportservice] Host/ip: ') # Target
	dom = flib(host)
	if chost(dom) == True: # Check for Host
		star = raw_input(C+'[*]'+W+'asm>[scanportservice] start range: ')
		end = raw_input(C+'[*]'+W+'asm>[scanportservice] end range: ')
		file = raw_input(C+'[*]'+W+'asm>[scanportservice] show File output?y/n ') # y = Save To File n = Show Recv
		def psend(host,port,f=False):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.settimeout(8)
			try:
				send = s.connect_ex((host,port))
				try:
					serv = socket.getservbyport(port)
				except:
					serv = 'unknow'
			except:
				send = 10035
				try:
					serv = socket.getservbyport(port)
				except:
					serv = 'unknow'
			if send == 0:
				if f == False:
					return C+'\tport '+str(port)+'( '+B+serv+C+' ) is open !'
				else:
					return '\tport '+str(port)+'( '+serv+' ) is open !'

			elif send == 10035:
				if f == False:
					return R+'\tport '+str(port)+'( '+B+serv+R+' ) is close !'
				else:
					return '\tport '+str(port)+'( '+serv+' ) is close !'
			else:
				if f == False:
					return R+'\tport '+str(port)+'( '+B+serv+R+' ) is close !'
				else:
					return '\tport '+str(port)+'( '+serv+' ) is close !'
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] start range '+str(star)+' up to '+str(end)+' [*]'
			print '[*] Please White ... [*]'
			if (file == 'y' or file == 'Y'): # Save To File
				rand = str(randint(0,2000))
				fname = rand+'scanportservice_'+dom.replace('.','_')+'.html' # File Save
				for x in range(int(star),int(end)):
					recv = psend(dom,x,True)
					fsave = _fileSave.saved(recv,fname)
				if(fsave==True):
					print '[*] Saved To output/'+fname+' success [*]' # Save True
				elif(fsave==False):
					print '[*] bad to saved file [*]' # Save False
				else:
					pass
			elif(file == 'n' or file == 'N'):
				print
				for x in range(int(star),int(end)): # Show Recv
					print psend(dom,x)
				print
			else:
				print
				for x in range(int(star),int(end)):
					print psend(dom,x)
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