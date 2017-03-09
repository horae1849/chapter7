import subprocess

def run(**args):

	print "[*] In ps_test module."
	cmd = ["ps","-ef"]
	fd_popen = subprocess.call(cmd,stdout=subprocess.PIPE).stdout
	data = fd_popen.read().strip()
	
	print data
	return str(data)

