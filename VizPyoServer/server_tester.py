# server_tester.py


# REFERENCES:
#
# The trick to getting the server to run in a separate process is to turn off the reloader
# https://stackoverflow.com/questions/31264826/start-a-flask-application-in-separate-thread
#
#


#stuff
import time
from multiprocessing import Process
import requests
#our stuff
import viz_server
import pyowrap

_server_process = None


def start_server():
    global _server_process
    if _server_process:
        _server_process.terminate()
    _server_process = Process(target=viz_server.start)
    _server_process.start()

# def stop_server():
#     global _server_process
#     if _server_process:
#         _server_process.terminate()
#         _server_process = None

def stop_server():
    requests.post('http://localhost:5000/shutdown')


start_server()

time.sleep(5)

# Test that all the classes are present by comparing the classes fetched from the server with those declared
print("Testing that list of Pyo classes fetched from server matches classes defined for server...")
server_classes = requests.get('http://localhost:5000/classes').json()
print("Fetched %d classes from server" % len(server_classes))
declared_classes = pyowrap.get_declared_class_names()
print("Found %d classes defined for server" % len(server_classes))
match = server_classes == declared_classes
if match:
    print("The server class set matches the defined class set")
else:
    print("ERROR: The server class set does not match the defined class set")
    server_extras = server_classes - declared_classes
    declared_extras = declared_classes - server_classes
    if server_extras:
        print("The server is server undeclared classes: %s" % server_extras)
    if declared_extras:
        print("The server is not serving declard classes: %s" % declared_extras)


# Test that all arguments have defaults

# Create instances of each element with defaults

# Inventory all elements

# Delete all elements






stop_server()




