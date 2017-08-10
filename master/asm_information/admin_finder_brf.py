# import modules for colors
from lib.color.dtectcolors import Style,Fore,Back,init
init()
W  =   Style.BRIGHT+Fore.WHITE # white
GR =   Style.DIM+Fore.WHITE    # gray
C  =   Style.BRIGHT+Fore.GREEN # green
R  =   Fore.RED 			   # red
B  =   Fore.BLUE  			   # blue
Y  =   Fore.YELLOW			   # yellow		   # yellow
import sys
def start():
	# import
	from httplib import httpConnection
	from urllib import urllib
	from lib.check import chost,flib
	def z(host):
		try:
			return urllib.urlopen('http://'+str(host)).code
		except:
			return None
	host = raw_input(C+'[*]'+W+'asm>[admin_finder_brf] Host: ') # Target
	dom = flib(host) # Bad protocot [http:// https://]
	if chost(dom) == True:# Check Host
		brf = ['admin/slider.brf','admin/add-slider.brf','admin/add_gallery_image.brf','admin/welcome.brf','admin/configration.brf','admin/dashbord.brf','manage_admin.brf','admin/form.brf','admin/my_account.brf','admin/specializations.brf','admin/initialadmin.brf','admin/pages/home_admin.brf','admin/home.brf','/admin/save.brf','admin/enter.brf','admin/userpage.brf','admin/banners_report.brf','admin/login-home.brf','admin/category.brf','admin/dashboard/index.brf','admin/add_banner.brf','admin/add_testimonials.brf','admin/userpage.brf','admin_main.html','admin/addblog.brf','admin/products.brf','admin/admin_management.brf','admin/add.brf','admin/add-room.brf','admin/main_page.brf','admin/adminview.brf','admin/welcomepage.brf','admin/index-digital.brf','admin/overview.brf','admin_home.brf','admin/admin_users.brf','/admin/upload.brf','admin/index_ref.brf','admin/checklogin.brf','admin/member_home.brf','admin/banner.brf','admin/manageImages.brf','admin/login_success.brf','admin/leads.brf','admin/uhome.html','admin/AdminDashboard.brf','admin/cpanel.brf','admin/manage_team.brf','admin/voucher.brf','admin/ManageAdmin.brf','admin/dashboard.brf','admin/account.brf','admin/change_gallery.brf','admin/list_gallery.brf','admin/viewblog.brf','admin/main.brf','admin/AdminHome.brf','admin/dash.brf','admin/gallery.brf','admin/product.brf','admin/loginsuccess.brf','admin/gallery.brf','admin/headline.brf','admin/page_management.brf','admin/index.brf','admin/event.brf','admin/admin-home.brf','admin/myaccount.brf','admin/admin_index.brf','admin/viewmembers.brf','admin/default.brf','admin/CPhome.brf','admin/control_pages/admin_home.brf','admin/adminarea.brf','admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html','admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html','admin/controlpanel.brf','admin.brf','admincp/index.brf','admincp/login.brf','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html','webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html','admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brf','admin/admin_login.brf','admin_login.brf','administrator/account.brf','administrator.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf','bb-admin/index.html','bb-admin/login.html','acceso.brf','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf','moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf','admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html','webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html','administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html','panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf','adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf','modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf','adm/index.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf']
		try:
			print '[*] Starting ... [*]'
			print '[*] ip/host %s is Activ [*]'%dom
			print '[*] Please White ... [*]'
			def requests(host,adm):
				for page in adm:
					page = '/'+str(page).replace('\n','')
					url = str(host)+page
					con = httplib.HTTPConnection(host)# Send Requests
					con.request('GET',page)
					res = con.getresponse().status
					recv = '\t[+]> '+url+' => '+str(res);
					if res == 200:
						print C+recv # True Request
					else:
						print R+recv # False Request
				print Y+'\t{'+str(len(adm))+' We checked the page }'
			requests(dom,brf)
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