import threading
import json
import time
import time
clientes = 8

def f0():
	threadf0 = threading.Thread(target= parallel_f0, daemon = False, args = [], kwargs={})
	threadf0.start()
	return json.dumps("cloudbook: thread launched")


def parallel_f0():
    if (not hasattr(f0, 'client_appears')):
        f0.client_appears = None
    if (not hasattr(f0, 'ver_client_appears')):
        f0.ver_client_appears = 0
    try:
        (aux_client_appears, aux_ver) = invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f0', 'params': {'args': [f0.ver_client_appears, 'None'], 'kwargs': {}}})
    except:
        (aux_client_appears, aux_ver) = json.loads(invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f0', 'params': {'args': [f0.ver_client_appears, 'None'], 'kwargs': {}}}))
    if (aux_client_appears != 'None'):
        f0.client_appears = aux_client_appears
    client_appears = f0.client_appears
    f0.ver_client_appears = aux_ver
    ver_client_appears = f0.ver_client_appears
    todos_cortados = 0
    while (todos_cortados < clientes):
        updated_client = f2()
        if updated_client:
            CLOUDBOOK_LOCK()
            client_appears = False
            invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f0', 'params': {'args': [0, '=', client_appears], 'kwargs': {'index': []}}})
            print('Barbero', __CLOUDBOOK__()['agent']['id'], ': Barbero ha cortado el pelo al cliente, lleva', (todos_cortados + 1))
            todos_cortados += 1
            CLOUDBOOK_UNLOCK()
    return invoker({'invoked_du': 'du_0', 'invoked_function': 'thread_counter', 'invoker_function': 'thread_counter', 'params': {'args': ['--'], 'kwargs': {}}})

def f1():
	threadf1 = threading.Thread(target= nonblocking_f1, daemon = False, args = [], kwargs={})
	threadf1.start()
	return json.dumps("cloudbook: thread launched")


def nonblocking_f1():
    if (not hasattr(f1, 'client_appears')):
        f1.client_appears = None
    if (not hasattr(f1, 'ver_client_appears')):
        f1.ver_client_appears = 0
    try:
        (aux_client_appears, aux_ver) = invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f1', 'params': {'args': [f1.ver_client_appears, 'None'], 'kwargs': {}}})
    except:
        (aux_client_appears, aux_ver) = json.loads(invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f1', 'params': {'args': [f1.ver_client_appears, 'None'], 'kwargs': {}}}))
    if (aux_client_appears != 'None'):
        f1.client_appears = aux_client_appears
    client_appears = f1.client_appears
    f1.ver_client_appears = aux_ver
    ver_client_appears = f1.ver_client_appears
    cortado = False
    while (not cortado):
        updated_client = f2()
        if updated_client:
            continue
        else:
            CLOUDBOOK_LOCK()
            updated_client = f2()
            if (not updated_client):
                client_appears = True
                invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f1', 'params': {'args': [0, '=', client_appears], 'kwargs': {'index': []}}})
                print('Cliente', __CLOUDBOOK__()['agent']['id'], ': cliente se va a cortar el pelo, esta libre el barbero')
                cortado = True
            CLOUDBOOK_UNLOCK()
    return json.dumps('Cloudbook: Done')


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

