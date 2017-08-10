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
	from socket import gethostbyname
	from random import randint
	sub=['news.', 'download.', '', 'cpanel.', 'ftp.','email.', 'server1.', 'cdn.', 'cdn2.', 'ns.', 'ns1.', 'mail.', 'webmail.', 'direct.', 'direct-connect.', 'record.', 'ssl.', 'dns.', 'help.', 'blog.', 'irc.', 'forum.','admin.','server.','client.','shop.','panel.','android.','dld.','adm.','map.','file.','dll.','login.','ns1.','ns2.','ns3.','ns4.','ns5.','ns6.','ns7.','ns8.','ns9.'];
	def z(host):
		try:
			return urllib.urlopen('http://'+str(host)).code # Online Host
		except:
			return None
	host = raw_input(C+'[*]'+W+'asm>[cloud_flare] Host: ') # Target
	dom = flib(host)
	if chost(dom) == True: # Check For Host
		file = raw_input(C+'[*]'+W+'asm>[cloud_flare] show File output?y/n ') # y = Save To File n = Show Recv
		def psend(host,sub,f=False):
			host = sub+host
			send = z(host) # Send Request
			if send == 200:
				ip = gethostbyname(host)
			else:
				ip = None
			if f == False:
				return C+'\t ( '+host+' ) => '+str(send)+' : '+str(ip) # Show Message
			else:
				return '\t( '+host+' ) => '+str(send)+' : '+str(ip) # Show Message
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] Please White ... [*]'
			if (file == 'y' or file == 'Y'):
				rand = str(randint(0,2000))
				fname = rand+'cloud_flare_'+dom.replace('.','_')+'.html' # File Name
				for x in sub:
					recv = psend(dom,x,True)
					fsave = saved(recv,fname) # Save To File
				if(fsave==True):
					print '[*] Saved To output/'+fname+' success [*]'
				elif(fsave==False):
					print '[*] bad to saved file [*]'
				else:
					pass
			elif(file == 'n' or file == 'N'):
				print
				for x in sub:
					print psend(dom,x,False) # Show Recv
				print
			else:
				print
				for x in sub:
					print psend(dom,x,False) # Show Recv
				print
			print W+'[*] END [*]' # End Process
			print GR+'[Type 98 to Back]'+W
			print GR+'[Type 99 to Exit]'+W
			print GR+'[Type 100 to options]'+W

		except:
			print '[-] oops error [-]' # Erro Null :(
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error Host
		print W+'[*] END [*]' # End Process
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)