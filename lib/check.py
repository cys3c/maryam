import httplib
def flib(xur):
	for x in ['http://','ftp://','https://']:
		if x in xur:
			xur = xur.replace(x,'')
		else:
			xur = xur
	return str(xur)

def chost(xur):
	try:
		ch = httplib.HTTPConnection(xur)
		ch.connect()
		status = True
	except:
		status = False
	return status

def cc(signal ,s):
	print '\n ENTER FOR EXIT ; Back to the Future .. :)'