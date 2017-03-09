import subprocess

def run(**args):

	print "[*] In ps_test module."
	data = subprocess.call('ps -ef',shell=False)
	
	return str(data)

