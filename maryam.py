#!/usr/bin/python
#----------------------------------------------
# Tools Maryam for iranian and all man ; Copyright (C) 2017
# write with python programming
# write by abolfazl hajizade and saeed dehghan
# gmail proct.maryam@gmail.com
# tel @B_LACK
#----------------------------------------------
# Maryam Tool is an open source tool for collecting information with 34 different modules.
# def maryam():
__author__ = 'Black Brain'
__version__ = '0.0'
__email__ = 'proct.maryam@gmail.com'
__copyright__ = "Copyright (c) FREE"
__license__ = "MIT"
__all__ = ['Information']
_love = ['Guido van Rossum','rasmus lerdorf']
#_love[0] https://en.wikipedia.org/wiki/Guido_van_Rossum
#_love[1] https://en.wikipedia.org/wiki/Rasmus_Lerdorf

# SearchEngine => Comming Sone..
# DOS => Comming Sone..
# Back to the Future :
# import modules for struction
try:
	import bs4
	import requests
except:
	import os
	try:
		os.system('pip install bs4')
		os.system('pip install requests')
		print 'TRY AGENT'
		exit()
	except:
		print 'pip install bs4 ; no mmodule named BeautifulSoup.try agent'
		print 'pip install bs4 ; no mmodule named requests.try agent'
		exit()
import lib.banner as BANNER
BANNER.banner()
import lib.Guide as HELP
import lib.About as About
import lib.check as Signat
import signal
import sys
# import modules for work with tool
import master.asm_information as INFO
# import modules for colors
from lib.color.dtectcolors import Style,Fore,Back,init
init()
W  =   Style.BRIGHT+Fore.WHITE # white
GR =   Style.DIM+Fore.WHITE    # gray
C  =   Style.BRIGHT+Fore.GREEN # green
R  =   Fore.RED 			   # red
B  =   Fore.BLUE  			   # blue
Y  =   Fore.YELLOW			   # yellow
# Global Tool var
Information = INFO
signal.signal(signal.SIGINT,Signat.cc)
def maryam():
	def Info_function():
		info = {1:'whois',2:'trace_route',3:'scan_port_service',
		4:'scan_port_fast',5:'scan_port_auto',6:'reverse_ip',
		7:'ping',8:'ip_api',9:'http_header',
		10:'cloud_flare',11:'dnslookup',12:'domain_map',
		13:'reverse_whois_html',14:'ip_history_html',15:'dns_report_html',
		16:'find_shared_dns',17:'trace_ip',18:'reverse_ns_html',
		19:'reverse_mx_html',20:'dns_propagation_html',21:'find_records',
		22:'extract_links',23:'crawler',24:'robot',
		25:'admin_finder_asp',26:'admin_finder_php',27:'admin_finder_js',
		28:'admin_finder_cgi',29:'admin_finder_brf',30:'HashAnalyzer',
		31:'HashDeCreption',32:'technology_activ_web',98:'back',99:'exit',100:'option'}
		print Y+"\n------ INFORMATION -------"+W
		HELP.op_info()
		while True:
			CH_info = raw_input(C+'[*]'+W+'asm>info> ')
			if (CH_info == '100'): # options
				HELP.op_info()
			elif (CH_info == '99'): # exit
				sys.exit(1)
			elif (CH_info == '98'): # information
				break
			elif (CH_info == '' or CH_info == '\n'): # none value
				continue
			elif (int(CH_info) in info):
				eval('Information.'+info[int(CH_info)]+'.start()')
			else:
				continue
	# stating Tool ....
	while True:
		HELP.options()
		CH_1 = raw_input(C+'[*]'+W+'asm> ')
		if (CH_1 == '100'): # options
			HELP.options()
		elif (CH_1 == '99'): # exit
			sys.exit(1)
		elif (CH_1 == '98'):
			print R+'If you want to leave, enter 99'
		elif (CH_1 == '2'): # About
			About.About()
		elif (CH_1 == '1'): # information
			Info_function()
		elif (CH_1 == '' or CH_1 == '\n'): # none value
			continue
		else:
			continue
try:
	maryam()
except:
	pass
if __name__ == '__main__':
	pass