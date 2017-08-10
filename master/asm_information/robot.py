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
	def conch(xur):
		try:
			urlopen('http://'+str(dom))
			status = True
		except:
			status = False
		return status
	def contlib(xur):
		for x in ['http://','ftp://','https://','www.']:
			if x in xur:
				xur = xur.replace(x,'')
			else:
				xur = xur
		return str(xur)
	def _reading(html,tag,f):
		bs = BeautifulSoup(host,'html.parser').find_all(tag)
		try:
			s = open(f,'a')
			s.write('all link : '+str(len(bs)))
			save = bs
			for x in save:
				value = '\n'+str(x)+'\n\t'
				s.write(value)
			s.close()
			return True
		except:
			return False
	def _a(host,f): # A Tag find
		bs = BeautifulSoup(host,'html.parser').find_all('a',href=True)
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
	def _script(html,f): # Script Tag find
		bs = BeautifulSoup(host,'html.parser').find_all('script',src=True)
		try:
			s = open(f,'a')
			s.write('all page js : '+str(len(bs)))
			save = bs
			for x in save:
				value = '\n'+str(x.get('src'))+'\n\t'
				s.write(value)
			s.close()
			return True
		except:
			return False
	def _link(html,f): # Link Tag Find
		bs = BeautifulSoup(host,'html.parser').find_all('link',href=True)
		try:
			s = open(f,'a')
			s.write('all page css : '+str(len(bs)))
			save = bs
			for x in save:
				value = '\n'+str(x.get('href'))+'\n\t'
				s.write(value)
			s.close()
			return True
		except:
			return False
	def _img(html,f): # img Tag Find
		bs = BeautifulSoup(host,'html.parser').find_all('img',src=True)
		try:
			s = open(f,'a')
			s.write('all img file : '+str(len(bs)))
			save = bs
			for x in save:
				value = '\n'+str(x.get('src'))+'\n\t'
				s.write(value)
			s.close()
			return True
		except:
			return False
	host = raw_input(C+'[*]'+W+'asm>[robot] Host: ')
	dom = contlib(host) # Bad Protocol [http:// https://]
	option = '\n1> a\n2> meta tag\n3> input \n4> form\n5> iframe\n6> h1\n7> script\n8> img\n9> all photo link\n10> all link\n11> all script page link\n12> all css page link'
	if conch(dom) == True: # Check for host
		fname = 'output/'+str(randint(0,2000))+'robot_'+dom.replace('.','_')+'.txt' # File Name
		host = urlopen('http://'+dom).read() # Send Request
		try:
			while 1:
				print option
				what = raw_input(C+'[*]'+W+'asm>[robot]>: ') # Select Option
				if what == '1':
					recv=_reading(host,'a',fname)
					break
				elif what == '2':
					recv= _reading(host,'meta',fname)
					break
				elif what == '3':
					recv= _reading(host,'input',fname)
					break
				elif what == '4':
					recv= _reading(host,'form',fname)
					break
				elif what == '5':
					recv= _reading(host,'iframe',fname)
					break
				elif what == '6':
					recv= _reading(host,'h1',fname)
					break
				elif what == '7':
					recv= _reading(host,'script',fname)
					break
				elif what == '8':
					recv= _reading(host,'img',fname)
					break
				elif what == '9':
					recv = _img(host,fname)
					break
				elif what == '10':
					recv = _a(host,fname)
					break
				elif what == '11':
					recv = _script(host,fname)
					break
				elif what == '12':
					recv = _link(host,fname)
					break			
				else:
					continue
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] Please White ... [*]'		
			if recv==True:
				print '[*] Saved To '+fname+' success [*]' # Save True
			elif recv==False:
				print '[*] bad to saved file [*]' # Save False
			else:
				pass
			print W+'[*] END [*]' # End process
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