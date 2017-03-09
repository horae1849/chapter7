import subprocess

def run(**args):

	data = subprocess.call('ps -ef',shell=True)
	
	return str(data)

