import threading
import json
import time


class NumComplejo():

    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def create(self, r, i):
        self.real = r
        self.imag = i

    def getOperators():
        op_a = NumComplejo()
        op_b = NumComplejo()
        (op_a.real, op_a.imag) = input('Operador a (separado por comas):').split(',')
        (op_b.real, op_b.imag) = input('Operador b (separado por comas):').split(',')
        (op_a.real, op_a.imag) = (int(op_a.real), int(op_a.imag))
        (op_b.real, op_b.imag) = (int(op_b.real), int(op_b.imag))
        return (op_a, op_b)

    def suma():
        (numa, numb) = NumComplejo.getOperators()
        result = NumComplejo()
        result.real = (numa.real + numb.real)
        result.imag = (numa.imag + numb.imag)
        NumComplejo.printResult('+', numa, numb, result)

    def resta():
        (numa, numb) = NumComplejo.getOperators()
        result = NumComplejo()
        result.real = (numa.real - numb.real)
        result.imag = (numa.imag - numb.imag)
        NumComplejo.printResult('-', numa, numb, result)

    def mult():
        (numa, numb) = NumComplejo.getOperators()
        result = NumComplejo()
        result.real = ((numa.real * numb.real) - (numa.imag * numb.imag))
        result.imag = ((numa.real * numb.imag) + (numa.imag * numb.real))
        NumComplejo.printResult('*', numa, numb, result)

    def div():
        (numa, numb) = NumComplejo.getOperators()
        result = NumComplejo()
        result.real = (((numa.real * numb.real) + (numa.imag * numb.imag)) / ((numb.real * numb.real) + (numb.imag * numb.imag)))
        result.imag = (((numa.imag * numb.real) - (numa.real * numb.imag)) / ((numb.real * numb.real) + (numb.imag * numb.imag)))
        NumComplejo.printResult('/', numa, numb, result)

    def printResult(op, opa, opb, res):
        print((' ' * 4), end='')
        opa.getData()
        print('  ', op)
        print((' ' * 4), end='')
        opb.getData()
        print((' ' * 4), end='')
        print('======')
        print((' ' * 4), end='')
        res.getData()
        input('press enter to continue')

    def getData(self):
        print('{0}+{1}i'.format(self.real, self.imag))


def f1():
	threadf1 = threading.Thread(target= parallel_f1, daemon = False, args = [], kwargs={})
	threadf1.start()
	return json.dumps("cloudbook: thread launched")


def parallel_f1():
    print('Soy la parallel')
    c1 = NumComplejo(20, 30)
    c2 = NumComplejo(10, 20)
    c1.getData()
    c2.getData()
    return invoker({'invoked_du': 'du_0', 'invoked_function': 'thread_counter', 'invoker_function': 'thread_counter', 'params': {'args': ['--'], 'kwargs': {}}})

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
