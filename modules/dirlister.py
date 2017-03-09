import os

def run(**args):
    
    print "[*] In dirLister module."
    files = os.listdir(".")
    
    return str(files)
