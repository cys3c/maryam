def saved(value=None,fname=None):
	try:
		saveTo = str('output/'+fname)
		f = open(saveTo,'a')
		f.write(value)
		return True
	except:
		return False