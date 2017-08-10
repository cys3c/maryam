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
	host = raw_input(C+'[*]'+W+'asm>[admin_finder_js] Host: ') # Target
	dom = flib(host) # Bad protocot [http:// https://]
	if chost(dom) == True: # Check Host
		js = ['admin/slider.html','admin/add-slider.html','admin/add_gallery_image.html','admin/welcome.html','admin/configration.html','admin/dashbord.html','manage_admin.html','admin/form.html','admin/my_account.html','admin/specializations.html','admin/initialadmin.html','admin/pages/home_admin.html','admin/home.html','/admin/save.html','admin/enter.html','admin/userpage.html','admin/banners_report.html','admin/login-home.html','admin/category.html','admin/dashboard/index.html','admin/add_banner.html','admin/add_testimonials.html','admin/userpage.html','admin_main.html','admin/addblog.html','admin/products.html','admin/admin_management.html','admin/add.html','admin/add-room.html','admin/main_page.html','admin/adminview.html','admin/welcomepage.html','admin/index-digital.html','admin/overview.js','admin_home.js','admin/admin_users.js','/admin/upload.js','admin/index_ref.js','admin/checklogin.js','admin/member_home.js','admin/banner.js','admin/manageImages.js','admin/login_success.js','admin/leads.js','admin/uhome.html','admin/AdminDashboard.js','admin/cpanel.js','admin/manage_team.js','admin/voucher.js','admin/ManageAdmin.js','admin/dashboard.js','admin/account.js','admin/change_gallery.js','admin/list_gallery.js','admin/viewblog.js','admin/main.js','admin/AdminHome.js','admin/dash.js','admin/gallery.js','admin/product.js','admin/loginsuccess.js','admin/gallery.js','admin/headline.js','admin/page_management.js','admin/index.js','admin/event.js','admin/admin-home.js','admin/myaccount.js','admin/admin_index.js','admin/viewmembers.js','admin/default.js','admin/CPhome.js','admin/control_pages/admin_home.js','admin/adminarea.js','admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js','admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html','admin/controlpanel.js','admin.js','admincp/index.js','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js','administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js','bb-admin/index.html','bb-admin/login.html','acceso.js','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js','moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js','admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html','webadmin.js','webadmin/index.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js','adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js','modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js','adm/index.js','adm_auth.js','memberadmin.js','administratorlogin.js']
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
			requests(dom,js)
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