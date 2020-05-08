import threading
import json
import time
import sys


def f1():
    invoker({'invoked_du': 'du_default', 'invoked_function': 'f0', 'invoker_function': 'f1', 'params': {'args': [1000, 'a', 'b', 'c', 0], 'kwargs': {}}})
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


def thread_counter(value):
	if not hasattr(thread_counter, "val"):
		thread_counter.val = 0
	if not hasattr(thread_counter, "cerrojo"):
		thread_counter.cerrojo = threading.Lock()
	if value == "++":
		with thread_counter.cerrojo:
			thread_counter.val += 1
	if value == "--":
		with thread_counter.cerrojo:
			thread_counter.val -= 1
	return json.dumps(thread_counter.val)


def critical_section_control(op):
	if (not hasattr(critical_section_control, 'value')):
		critical_section_control.value = "unlocked"
	if (not hasattr(critical_section_control, 'lock')):
		critical_section_control.lock = threading.Lock()
	with critical_section_control.lock:
		if op == 'lock':
			if critical_section_control.value == "unlocked":
				critical_section_control.value = "locked"
				return json.dumps("unlocked")
			else:
				critical_section_control.value = "locked"
		if op == 'unlock':
			critical_section_control.value = "unlocked"
	return json.dumps(critical_section_control.value)

def main():
	return f1()

