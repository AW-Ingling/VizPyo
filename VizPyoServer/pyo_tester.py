# pyo_tester.py
#
#

# Install python 3.6 from python.org
# Install wxpython: /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 -m pip install -U wxPython
# Install pyo


# References:
#
# Installing Pyo with Anaconda Python:
# https://github.com/lupyanlab/lab-computer/wiki/Installing-pyo  <- does not work
# https://gist.github.com/pwalsh/5691534
#
# How to make it actually work, use this line: s = Server(duplex=0).boot()
# https://github.com/belangeo/pyo/issues/61



from pyo import *

# Creates and boots the server.
# The user should send the "start" command from the GUI.

#s = Server().boot()

s = Server(duplex=0).boot()
# Drops the gain by 20 dB.
s.amp = 0.1

# Creates a sine wave player.
# The out() method starts the processing
# and sends the signal to the output.
a = Sine().out()

# Opens the server graphical interface.
s.gui(locals())


