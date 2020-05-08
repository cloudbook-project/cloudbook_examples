import threading
import json
import time
import sys


def f0(height, origin, destination, intermediate, level):
    level = (level + 1)
    print('=====================================> DEPTH LEVEL:', level)
    if (height >= 1):
        invoker({'invoked_du': 'du_default', 'invoked_function': 'f0', 'invoker_function': 'f0', 'params': {'args': [(height - 1), origin, intermediate, destination, level], 'kwargs': {}}})
        print(((('move disc from ' + str(origin)) + ' to ') + str(destination)))
        invoker({'invoked_du': 'du_default', 'invoked_function': 'f0', 'invoker_function': 'f0', 'params': {'args': [(height - 1), intermediate, destination, origin, level], 'kwargs': {}}})
    return json.dumps('Cloudbook: Done')

def CLOUDBOOK_SYNC(t=None):
	invoker_dict = {'invoked_du':'du_0', 'invoked_function': 'thread_counter', 'invoker_function': 'thread_counter', 'params': {'args': [''], 'kwargs': {}}}
	#value = json.loads(invoker(invoker_dict))
	value = invoker(invoker_dict)
	temp = 0
	timeout = True
	if t != None:
		while value > 0 and timeout:
			if temp>t:
				#thread failure
				timeout = False
			time.sleep(0.01)
			temp+=1
			value = invoker(invoker_dict)
	else:
		while value>0:
			time.sleep(0.01)
			value = invoker(invoker_dict)

def CLOUDBOOK_LOCK():
	lock_dict = {'invoked_du':'du_0', 'invoked_function': 'critical_section_control', 'invoker_function': 'critical_section_control', 'params': {'args': ['lock'], 'kwargs': {}}}
	value = invoker(lock_dict)
	#print("value:",value)
	while value != "unlocked":
		#print("no entro")
		value = invoker(lock_dict)
		time.sleep(0.1)

def CLOUDBOOK_UNLOCK():
	unlock_dict = {'invoked_du':'du_0', 'invoked_function': 'critical_section_control', 'invoker_function': 'critical_section_control', 'params': {'args': ['unlock'], 'kwargs': {}}}
	invoker(unlock_dict)

