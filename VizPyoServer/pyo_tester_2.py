

from pyo import *
import time
s = Server(duplex=0).boot()
a = Sine(261.6, 0, 0.1).out()
s.start()
time.sleep(5)
s.stop()