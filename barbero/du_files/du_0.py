import threading
import json
import time
import time
clientes = 8

def f4(old_ver, op, *args, index=[]):
	if not hasattr(f4, "client_appears"):
		f4.client_appears = False
	if not hasattr(f4, "ver_client_appears"):
		f4.ver_client_appears = 1
	if not hasattr(f4, "lock_client_appears"):
		f4.lock_client_appears = threading.Lock()
	if op == "None":
		if old_ver == f4.ver_client_appears:
			return json.dumps(("None",old_ver))
		else:
			try:
				return json.dumps((f4.client_appears,f4.ver_client_appears))
			except:
				return json.dumps((str(f4.client_appears) ,f4.ver_client_appears))
	else:
		new_args = []
		for i in args:
			if isinstance(i,str):
				new_args.append("'"+i+"'")
			else:
				new_args.append(str(i))
		for i in index:
			if isinstance(i,str):
				op = "['"+i+"']" + op
			else:
				op = "["+str(i)+"]" + op
		if "=" in op:
			op = "f4.client_appears"+op+new_args[0] #only 1 value in global_var = something
		else:
			op = "f4.client_appears"+op+"("
			for i in new_args:
				op = op+i+","
			op = op + ")"
		try:
			f4.ver_client_appears += 1
			return json.dumps((eval(op),f4.ver_client_appears))
		except:
			with f4.lock_client_appears:
				exec(op)
				f4.ver_client_appears += 1
			return json.dumps(("done",f4.ver_client_appears))
	return json.dumps('cloudbook: done') 


def f2():
    if (not hasattr(f2, 'client_appears')):
        f2.client_appears = None
    if (not hasattr(f2, 'ver_client_appears')):
        f2.ver_client_appears = 0
    try:
        (aux_client_appears, aux_ver) = invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f2', 'params': {'args': [f2.ver_client_appears, 'None'], 'kwargs': {}}})
    except:
        (aux_client_appears, aux_ver) = json.loads(invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f2', 'params': {'args': [f2.ver_client_appears, 'None'], 'kwargs': {}}}))
    if (aux_client_appears != 'None'):
        f2.client_appears = aux_client_appears
    client_appears = f2.client_appears
    f2.ver_client_appears = aux_ver
    ver_client_appears = f2.ver_client_appears
    x = client_appears
    return x


def f3():
    print('Empieza el dia en la barberia')
    print('llamo al barbero')
    invoker({'invoked_du': 'du_0', 'invoked_function': 'thread_counter', 'invoker_function': 'thread_counter', 'params': {'args': ['++'], 'kwargs': {}}})
    invoker({'invoked_du': 'du_default', 'invoked_function': 'f0', 'invoker_function': 'f3', 'params': {'args': [], 'kwargs': {}}})
    for i in range(clientes):
        print('Llega el cliente', i)
        invoker({'invoked_du': 'du_default', 'invoked_function': 'f1', 'invoker_function': 'f3', 'params': {'args': [], 'kwargs': {}}})
    print('Ya no llegan mas clientes')
    CLOUDBOOK_SYNC()
    print('Cerramos la barberia, hasta mañana')
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
	return f3()

