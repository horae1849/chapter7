import subprocess

def run(**args):

	print "[*] In ps_test module."
	fd_popen = subprocess.call('ps -ef',stdout=subprocess.PIPE).stdout
	data = fd_popen.read().strip()
	
	print data
	return str(data)

