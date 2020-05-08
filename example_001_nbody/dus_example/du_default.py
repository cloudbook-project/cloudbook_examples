import threading
import json
import time
from random import randint
import time
import math
import json
CONST_N = 100

def f0(single_body, iteration):
	threadf0 = threading.Thread(target= parallel_f0, daemon = False, args = [single_body, iteration], kwargs={})
	threadf0.start()
	return json.dumps("cloudbook: thread launched")


def parallel_f0(single_body, iteration):
    if (not hasattr(f0, 'body_list')):
        f0.body_list = None
    if (not hasattr(f0, 'ver_body_list')):
        f0.ver_body_list = 0
    try:
        (aux_body_list, aux_ver) = invoker({'invoked_du': 'du_0', 'invoked_function': 'f3', 'invoker_function': 'f0', 'params': {'args': [f0.ver_body_list, 'None'], 'kwargs': {}}})
    except:
        (aux_body_list, aux_ver) = json.loads(invoker({'invoked_du': 'du_0', 'invoked_function': 'f3', 'invoker_function': 'f0', 'params': {'args': [f0.ver_body_list, 'None'], 'kwargs': {}}}))
    if (aux_body_list != 'None'):
        f0.body_list = aux_body_list
    body_list = f0.body_list
    f0.ver_body_list = aux_ver
    ver_body_list = f0.ver_body_list
    if (not hasattr(f0, 'body_new')):
        f0.body_new = None
    if (not hasattr(f0, 'ver_body_new')):
        f0.ver_body_new = 0
    try:
        (aux_body_new, aux_ver) = invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f0', 'params': {'args': [f0.ver_body_new, 'None'], 'kwargs': {}}})
    except:
        (aux_body_new, aux_ver) = json.loads(invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f0', 'params': {'args': [f0.ver_body_new, 'None'], 'kwargs': {}}}))
    if (aux_body_new != 'None'):
        f0.body_new = aux_body_new
    body_new = f0.body_new
    f0.ver_body_new = aux_ver
    ver_body_new = f0.ver_body_new
    fx = 0.0
    fy = 0.0
    for i in body_list:
        delta_f = f1(single_body, i)
        fx = (fx + delta_f[0])
        fy = (fy + delta_f[1])
    ax = (fx / single_body[0])
    ay = (fy / single_body[0])
    vx = (single_body[3] + ax)
    vy = (single_body[4] + ay)
    x = (single_body[1] + vx)
    y = (single_body[2] + vy)
    new_single_body = (single_body[0], x, y, vx, vy)
    body_new.append(new_single_body)
    invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f0', 'params': {'args': [0, '.append', new_single_body], 'kwargs': {}}})
    return invoker({'invoked_du': 'du_0', 'invoked_function': 'thread_counter', 'invoker_function': 'thread_counter', 'params': {'args': ['--'], 'kwargs': {}}})


def f1(bodyA, bodyB):
    m1 = bodyA[0]
    x1 = bodyA[1]
    y1 = bodyA[2]
    vx1 = bodyA[3]
    vy1 = bodyA[4]
    m2 = bodyB[0]
    x2 = bodyB[1]
    y2 = bodyB[2]
    vx2 = bodyB[3]
    vy2 = bodyB[4]
    dx = math.sqrt(((x1 - x2) ** 2))
    if (dx != 0):
        fx = ((m1 * m2) / (dx ** 2))
    else:
        fx = 0
    if (x2 < x1):
        fx = (- fx)
    dy = math.sqrt(((y1 - y2) ** 2))
    if (dy != 0):
        fy = ((m1 * m2) / (dy ** 2))
    else:
        fy = 0
    if (y2 < y1):
        fy = (- fy)
    return (fx, fy)

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

