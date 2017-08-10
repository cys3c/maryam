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
	host = raw_input(C+'[*]'+W+'asm>[admin_finder_asp] Host: ') # Target
	dom = flib(host) # Bad protocot [http:// https://]
	if chost(dom) == True: # Check Host
   		asp = ['admin/slider.asp','admin/add-slider.asp','admin/add_gallery_image.asp','admin/welcome.asp','admin/configration.asp','admin/dashbord.asp','manage_admin.asp','admin/form.asp','admin/my_account.asp','admin/specializations.asp','admin/initialadmin.asp','admin/pages/home_admin.asp','admin/home.asp','/admin/save.asp','admin/enter.asp','admin/userpage.asp','admin/banners_report.asp','admin/login-home.asp','admin/category.asp','admin/dashboard/index.asp','admin/add_banner.asp','admin/add_testimonials.asp','admin/userpage.asp','admin_main.html','admin/addblog.asp','admin/products.asp','admin/admin_management.asp','admin/add.asp','admin/add-room.asp','admin/main_page.asp','admin/adminview.asp','admin/welcomepage.asp','admin/index-digital.asp','admin/overview.asp','admin_home.asp','admin/admin_users.asp','/admin/upload.asp','admin/index_ref.asp','admin/checklogin.asp','admin/member_home.asp','admin/banner.asp','admin/manageImages.asp','admin/login_success.asp','admin/leads.asp','admin/uhome.html','admin/AdminDashboard.asp','admin/cpanel.asp','admin/manage_team.asp','admin/voucher.asp','admin/ManageAdmin.asp','admin/dashboard.asp','admin/account.asp','admin/change_gallery.asp','admin/list_gallery.asp','admin/viewblog.asp','admin/main.asp','admin/AdminHome.asp','admin/dash.asp','admin/gallery.asp','admin/product.asp','admin/loginsuccess.asp','admin/gallery.asp','admin/headline.asp','admin/page_management.asp','admin/index.asp','admin/event.asp','admin/admin-home.asp','admin/myaccount.asp','admin/admin_index.asp','admin/viewmembers.asp','admin/default.asp','admin/CPhome.asp','admin/control_pages/admin_home.asp','admin/adminarea.asp','admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp','bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html','moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html','admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp','administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp','moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html','admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp','webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp','admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html','panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp','admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp','adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html'] # page list
		try:
			print '\n[*] Starting ... [*]'
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
			requests(dom,asp)
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