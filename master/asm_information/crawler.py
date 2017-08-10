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
	from bs4 import BeautifulSoup
	from random import randint
	from lib.check import flib,chost
	def _a(host,f):
		bs = BeautifulSoup(host,'html.parser').find_all('a',href=True) # Parser Page For a
		try:
			s = open(f,'a')
			s.write('all link : '+str(len(bs)))
			save = bs
			for x in save:
				value = '\n'+str(x['href'])+'\n\t'
				s.write(value)
			s.close()
			return True
		except:
			return False
	host = raw_input(C+'[*]'+W+'asm>[crawler] Host: ') # Target
	dom = flib(host)# Bad protocot [http:// https://]
	if chost(dom) == True:
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] Please White ... [*]'
			fname = 'output/'+str(randint(0,2000))+'crawler_'+dom.replace('.','_')+'.txt' # File Name
			host = urlopen('http://'+dom).read()
			recv = _a(host,fname)
			if recv==True:
				print '[*] Saved To '+fname+' success [*]' # Save True
			elif recv==False:
				print '[*] bad to saved file [*]' # Save False
			else:
				pass

			print W+'[*] END [*]' # End Process
			print GR+'[Type 98 to Back]'+W
			print GR+'[Type 99 to Exit]'+W
			print GR+'[Type 100 to options]'+W
		except:
			print '[-] oops error [-]' # Error Null :(
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom # Error Host
		print W+'[*] END [*]' # End Process
		start() # Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)