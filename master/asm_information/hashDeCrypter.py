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
	import requests
	value = raw_input('[*]asm>[hashDeCrypter]> Hash:')
	try:
		if len(value)>0:
			method = {'1':'md4','2':'md5','3':'sha1','4':'sha224','5':'sha256','6':'sha384','7':'ntlm'}
			option = '\n[1] > MD4\n[2] > MD5\n[3] > SHA1\n[4] > SHA224\n[5] > SHA256\n[6] > SHA384\n[7] > NTLM\n'
			print option
			while 1:
				algo = raw_input('[*]asm>[hashDeCrypter] algo:')
				if algo in method:
					email0 = 'proct.maryam@gmail.com'
					email1 = 'programerrphp@gmail.com'
					key0 = 'd576a7382efaa808'
					key1 = '251fed3a2905e990'
					url = 'http://md5decrypt.net/Api/api.php?hash='+value+'&hash_type='+method[algo]+'&email='+email0+'&code='+key0
					reqsend0 = requests.get(url).content
					if reqsend0 == 'CODE ERREUR : 001':
						url = 'http://md5decrypt.net/Api/api.php?hash='+value+'&hash_type='+method+'&email='+email1+'&code='+key1
						reqsend1 = requests.get(url).content
						if reqsend1 == 'CODE ERREUR : 001':
							print R+'\tYou exceeded the 400 allowed request per day'
							continue
						elif reqsend1 == 'CODE ERREUR : 003':
							print R+'\tYour request includes more than 400 hashes.'
							continue
						elif reqsend1 == 'CODE ERREUR : 004':
							print R+'\tAlgorithm Not Found.The type of hash you provide in the argument hashtype doesnt seem to be valid'
							continue
						elif reqsend1 == 'CODE ERREUR : 005':
							print R+'\tThe hash you provide doesnt seem to match with the type of hash you set.'
							continue
						elif reqsend1[0:4] != 'CODE' and reqsend1 != '':
							print C+'\t Hash is : '+str(reqsend1)
							break
						elif reqsend1[0:4] != 'CODE' and reqsend1 == '':
							print R+'\tHash Not Found !'
							break
						else:
							pass
					elif reqsend0 == 'CODE ERREUR : 003':
						print R+'\tYour request includes more than 400 hashes.'
						continue
					elif reqsend0 == 'CODE ERREUR : 004':
						print R+'\tAlgorithm Not Found.The type of hash you provide in the argument hashtype doesnt seem to be valid'
						continue
					elif reqsend0 == 'CODE ERREUR : 005':
						print R+'\tThe hash you provide doesnt seem to match with the type of hash you set.'
						continue
					elif reqsend0[0:4] != 'CODE' and reqsend0 != '':
						print C+'\t Hash is : '+str(reqsend0)
						print GR+'[Type 98 to Back]'+W
						print GR+'[Type 99 to Exit]'+W
						print GR+'[Type 100 to options]'+W
						break
					elif reqsend0 == '':
						print R+'\tHash Not Found !'
						print GR+'[Type 98 to Back]'+W
						print GR+'[Type 99 to Exit]'+W
						print GR+'[Type 100 to options]'+W
						break
					else:
						pass
				else:
					print option
					continue
		else:
			start()
	except:
		pass
if __name__ == '__main__':
	print "Let's just keep the files open only you can open the file %s and access and use these modules."%str(sys.argv[0])
	sys.exit(1)