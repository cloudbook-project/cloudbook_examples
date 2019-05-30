import json
import threading

invoker=None

def f0():
	invoker(['du_0'], 'cloudbook_th_counter',"'++'")
	invoker(['du_10000'], 'f1',str(0))


	return json.dumps('cloudbook: done') 

def f1(x):
	threadf1 = threading.Thread(target= parallel_f1, daemon = False, args = [x])
	threadf1.start()
	return json.dumps("thread launched")

def parallel_f1(x):
	#if (x>994):
	#	json.dumps(return)
	
	print (x)
	invoker(['du_0'], 'cloudbook_th_counter',"'++'")
	invoker(['du_10000'], 'f1',str(x+1))


	invoker(['du_0'], 'cloudbook_th_counter',"'--'")

	return json.dumps('cloudbook: done') 

def cloudbook_print(element):
	print (element)
	return "cloudbook: done"
	
def cloudbook_th_counter(value):
	if not hasattr(cloudbook_th_counter, "val"):
		val = 0
	if value == "++":
		val += 1
	if value == "--":
		val -= 1
	return json.dumps(val)

def main():
	#f0()
	#return "cloudbook: done"
	return f0()

if __name__ == '__main__':
	f0()
			