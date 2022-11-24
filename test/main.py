import subprocess
import threading

def worker():
    proc = subprocess.Popen(['animate', 'parrot.gif'])
    proc.communicate()

t = threading.Thread(target = worker)
t.daemon = True
t.start()
t.join()