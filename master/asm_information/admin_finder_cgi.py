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
	host = raw_input(C+'[*]'+W+'asm>[admin_finder_cgi] Host: ') # Target
	dom = flib(host) # Bad protocot [http:// https://]
	if chost(dom) == True: # Check Host
   		cgi = ['admin/slider.cgi','admin/add-slider.cgi','admin/add_gallery_image.cgi','admin/welcome.cgi','admin/configration.cgi','admin/dashbord.cgi','manage_admin.cgi','admin/form.cgi','admin/my_account.cgi','admin/specializations.cgi','admin/initialadmin.cgi','admin/pages/home_admin.cgi','admin/home.cgi','/admin/save.cgi','admin/enter.cgi','admin/userpage.cgi','admin/banners_report.cgi','admin/login-home.cgi','admin/category.cgi','admin/dashboard/index.cgi','admin/add_banner.cgi','admin/add_testimonials.cgi','admin/userpage.cgi','admin_main.html','admin/addblog.cgi','admin/products.cgi','admin/admin_management.cgi','admin/add.cgi','admin/add-room.cgi','admin/main_page.cgi','admin/adminview.cgi','admin/welcomepage.cgi','admin/index-digital.cgi','admin/overview.cgi','admin_home.cgi','admin/admin_users.cgi','/admin/upload.cgi','admin/index_ref.cgi','admin/checklogin.cgi','admin/member_home.cgi','admin/banner.cgi','admin/manageImages.cgi','admin/login_success.cgi','admin/leads.cgi','admin/uhome.html','admin/AdminDashboard.cgi','admin/cpanel.cgi','admin/manage_team.cgi','admin/voucher.cgi','admin/ManageAdmin.cgi','admin/dashboard.cgi','admin/account.cgi','admin/change_gallery.cgi','admin/list_gallery.cgi','admin/viewblog.cgi','admin/main.cgi','admin/AdminHome.cgi','admin/dash.cgi','admin/gallery.cgi','admin/product.cgi','admin/loginsuccess.cgi','admin/gallery.cgi','admin/headline.cgi','admin/page_management.cgi','admin/index.cgi','admin/event.cgi','admin/admin-home.cgi','admin/myaccount.cgi','admin/admin_index.cgi','admin/viewmembers.cgi','admin/default.cgi','admin/CPhome.cgi','admin/control_pages/admin_home.cgi','admin/adminarea.cgi','admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','account.cgi','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin_area/admin.cgi','admin_area/login.cgi','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html','moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html','admin/home.cgi','admin/controlpanel.cgi','admin.cgi','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi','admin/cp.cgi','cp.cgi','administrator/account.cgi','administrator.cgi','acceso.cgi','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi','administrator/login.cgi','moderator/admin.cgi','controlpanel.cgi','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.cgi','user.html','admincp/index.cgi','admincp/login.cgi','admincp/index.html','admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html','admincontrol/login.html','adm/index.html','adm.html','admincontrol.cgi','admin/account.cgi','adminpanel.cgi','webadmin.cgi','webadmin/index.cgi','webadmin/admin.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi','panel-administracion/login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi','adminarea/admin.cgi','adminarea/login.cgi','admin-login.html','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi','modelsearch/admin.cgi','administrator/index.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html'] # page list
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
			requests(dom,cgi)
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