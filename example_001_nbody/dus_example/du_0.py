import threading
import json
import time
from random import randint
import time
import math
import json
CONST_N = 100


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


def f2():
    if (not hasattr(f2, 'body_list')):
        f2.body_list = None
    if (not hasattr(f2, 'ver_body_list')):
        f2.ver_body_list = 0
    try:
        (aux_body_list, aux_ver) = invoker({'invoked_du': 'du_0', 'invoked_function': 'f3', 'invoker_function': 'f2', 'params': {'args': [f2.ver_body_list, 'None'], 'kwargs': {}}})
    except:
        (aux_body_list, aux_ver) = json.loads(invoker({'invoked_du': 'du_0', 'invoked_function': 'f3', 'invoker_function': 'f2', 'params': {'args': [f2.ver_body_list, 'None'], 'kwargs': {}}}))
    if (aux_body_list != 'None'):
        f2.body_list = aux_body_list
    body_list = f2.body_list
    f2.ver_body_list = aux_ver
    ver_body_list = f2.ver_body_list
    MAX_ITERATIONS = 3
    start = time.time()
    for j in range(MAX_ITERATIONS):
        print(j, '==>', body_list)
        print('starting iteration', j)
        for i in body_list:
            invoker({'invoked_du': 'du_0', 'invoked_function': 'thread_counter', 'invoker_function': 'thread_counter', 'params': {'args': ['++'], 'kwargs': {}}})
            invoker({'invoked_du': 'du_default', 'invoked_function': 'f0', 'invoker_function': 'f2', 'params': {'args': [i, j], 'kwargs': {}}})
        CLOUDBOOK_SYNC()
        if (not hasattr(f2, 'body_new')):
            f2.body_new = None
        if (not hasattr(f2, 'ver_body_new')):
            f2.ver_body_new = 0
        try:
            (aux_body_new, aux_ver) = invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f2', 'params': {'args': [f2.ver_body_new, 'None'], 'kwargs': {}}})
        except:
            (aux_body_new, aux_ver) = json.loads(invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f2', 'params': {'args': [f2.ver_body_new, 'None'], 'kwargs': {}}}))
        if (aux_body_new != 'None'):
            f2.body_new = aux_body_new
        body_new = f2.body_new
        f2.ver_body_new = aux_ver
        ver_body_new = f2.ver_body_new
        body_list = body_new
        invoker({'invoked_du': 'du_0', 'invoked_function': 'f3', 'invoker_function': 'f2', 'params': {'args': [0, '=', body_list], 'kwargs': {'index': []}}})
        body_new = []
        invoker({'invoked_du': 'du_0', 'invoked_function': 'f4', 'invoker_function': 'f2', 'params': {'args': [0, '=', body_new], 'kwargs': {'index': []}}})
        print('iteration ', j, ' executed')
    end = time.time()
    print('duration: ', (end - start))
    return json.dumps(body_list)

def f3(old_ver, op, *args, index=[]):
	if not hasattr(f3, "body_list"):
		f3.body_list = [(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0),(10,12,76,(-10),(-7)),(10,(-71),(-57),(-4),5),(10,81,(-52),6,(-10)),(10,30,32,(-9),4),(10,(-94),20,(-10),0)]
	if not hasattr(f3, "ver_body_list"):
		f3.ver_body_list = 1
	if not hasattr(f3, "lock_body_list"):
		f3.lock_body_list = threading.Lock()
	if op == "None":
		if old_ver == f3.ver_body_list:
			return json.dumps(("None",old_ver))
		else:
			try:
				return json.dumps((f3.body_list,f3.ver_body_list))
			except:
				return json.dumps((str(f3.body_list) ,f3.ver_body_list))
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
			op = "f3.body_list"+op+new_args[0] #only 1 value in global_var = something
		else:
			op = "f3.body_list"+op+"("
			for i in new_args:
				op = op+i+","
			op = op + ")"
		try:
			f3.ver_body_list += 1
			return json.dumps((eval(op),f3.ver_body_list))
		except:
			with f3.lock_body_list:
				exec(op)
				f3.ver_body_list += 1
			return json.dumps(("done",f3.ver_body_list))
	return json.dumps('cloudbook: done') 

def f4(old_ver, op, *args, index=[]):
	if not hasattr(f4, "body_new"):
		f4.body_new = []
	if not hasattr(f4, "ver_body_new"):
		f4.ver_body_new = 1
	if not hasattr(f4, "lock_body_new"):
		f4.lock_body_new = threading.Lock()
	if op == "None":
		if old_ver == f4.ver_body_new:
			return json.dumps(("None",old_ver))
		else:
			try:
				return json.dumps((f4.body_new,f4.ver_body_new))
			except:
				return json.dumps((str(f4.body_new) ,f4.ver_body_new))
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
			op = "f4.body_new"+op+new_args[0] #only 1 value in global_var = something
		else:
			op = "f4.body_new"+op+"("
			for i in new_args:
				op = op+i+","
			op = op + ")"
		try:
			f4.ver_body_new += 1
			return json.dumps((eval(op),f4.ver_body_new))
		except:
			with f4.lock_body_new:
				exec(op)
				f4.ver_body_new += 1
			return json.dumps(("done",f4.ver_body_new))
	return json.dumps('cloudbook: done') 

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
	return f2()

