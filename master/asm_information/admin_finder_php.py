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
	from httplib import HTTPConnection
	from urllib import urlopen
	from lib.check import chost,flib
	def z(host):
		try:
			return urllib.urlopen('http://'+str(host)).code
		except:
			return None
	host = raw_input(C+'[*]'+W+'asm>[admin_finder_php] Host: ') # Target
	dom = flib(host) # Bad protocot [http:// https://]
	if chost(dom) == True: # Check Host
		php = ['admin/slider.php','admin/add-slider.php','admin/add_gallery_image.php','config/','robots.txt','admin/welcome.php','admin/configration.php','admin/dashbord.php','manage_admin.php','admin/form.php','admin/my_account.php','admin/specializations.php','admin/initialadmin.php','admin/pages/home_admin.php','admin/home.php','admin/save.php','admin/enter.php','admin/userpage.php','admin/banners_report.php','admin/login-home.php','admin/category.php','admin/dashboard/index.php','admin/add_banner.php','admin/add_testimonials.php','admin/userpage.php','admin_main.html','admin/addblog.php','admin/products.php','admin/admin_management.php','admin/add.php','admin/add-room.php','admin/main_page.php','admin/adminview.php','admin/welcomepage.php','admin/index-digital.php','admin/overview.php','admin_home.php','admin/admin_users.php','admin/upload.php','admin/index_ref.php','admin/checklogin.php','admin/member_home.php','admin/banner.php','admin/manageImages.php','admin/login_success.php','admin/leads.php','admin/uhome.html','admin/AdminDashboard.php','admin/cpanel.php','admin/manage_team.php','admin/voucher.php','admin/ManageAdmin.php','admin/dashboard.php','admin/account.php','admin/change_gallery.php','admin/list_gallery.php','admin/viewblog.php','admin/main.php','admin/AdminHome.php','admin/dash.php','admin/gallery.php','admin/product.php','admin/loginsuccess.php','admin/gallery.php','admin/headline.php','admin/page_management.php','admin/index.php','admin/event.php','admin/admin-home.php','admin/myaccount.php','admin/admin_index.php','admin/viewmembers.php','admin/default.php','admin/CPhome.php','admin/control_pages/admin_home.php','admin/adminarea.php','admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php','admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html','admin/controlpanel.php','admin.php','admincp/index.php','admincp/login.php','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php','administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php','bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php','moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php','admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html','webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php','adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php','modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php','adm/index.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm.php']
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] Please White ... [*]'
			def requests(host,adm):
				for page in adm:
					page = '/'+str(page).replace('\n','')
					url = str(host)+page
					con = HTTPConnection(host) # Send Requests
					con.request('GET',page)
					res = con.getresponse().status
					recv = '\t[+]> '+url+' => '+str(res);
					if res == 200:
						print C+recv # True Request
					else:
						print R+recv
				print Y+'\t{'+str(len(adm))+' We checked the page }'
			requests(dom,php)
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