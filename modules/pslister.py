import os

def run(**args):
    
    print "[*] In psLister module."
    files = os.listdir(".")
    
    return str(files)
