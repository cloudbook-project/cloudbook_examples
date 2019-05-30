import json
import threading

invoker=None

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

