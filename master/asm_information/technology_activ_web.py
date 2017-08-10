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
	import lib.builtwith
	import sys
	host = raw_input(C+'[*]'+W+'asm>[frameworks_activ_web] Host: ') # Target
	file = raw_input(C+'[*]'+W+'asm>[frameworks_activ_web] show File output?y/n ') # y = Saved To File n = Show Recv
	dom = flib(host) # Bad protocol [http:// https://]
	# # Check for Host 
	if chost(dom) == True:
	# 	# Start
		print '[*] Starting ... [*]'
		print '[*] ip/host %s is Activ [*]'%dom
		print '[*] Please White ... [*]'
		# try:
        	results = lib.builtwith.builtwith('http://'+dom)
		if (file == 'y' or file == 'Y'):# file Save
			rand = str(randint(0,2000))
			fname = rand+'frameworks_activ_web_'+dom.replace('.','_')+'.html' # File Name
			for result in sorted(results.items()):
                                rQn =  '\t%s: %s\n' % result
				fsave = saved(rQn,fname) # Saved
			if(fsave==True):
				print '[*] Saved To output/'+fname+' success [*]' # File Save True
			elif(fsave==False):
				print '[*] bad to saved file [*]' # File Not Save
			else:
				pass
		
		elif(file == 'n' or file == 'N'):# Show Recv
			print
			for result in sorted(results.items()):
				rQn =  '\t%s: %s' % result
				print C+rQn # Show Recv
			print
		else:
			print
			for result in sorted(results.items()):
				rQn =  '\t%s: %s' % result
				print C+rQn # Show Recv
			print
		print W+'[*] END [*]' # End Process
		print GR+'[Type 98 to Back]'+W
		print GR+'[Type 99 to Exit]'+W
		print GR+'[Type 100 to options]'+W
		# except:
			# Error
			# print '[-] oops error [-]'
	else:
		print R+'[-] oops Error(%s) occured; invalid URL [-]'%dom# Error For Host
		print W+'[*] END [*]'
		start()# Continue
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)
