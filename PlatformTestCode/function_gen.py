import os

def gen_function(index,file):
	fun_name = "function_"+str(index)+"()"
	with open(file,"a") as f:
		f.write('''
def '''+fun_name+''':
	return 0
''')
	return 0

def gen_main_function(index,file):
	invocations = "\n"
	for i in range(index):
		invocations = invocations + "\t "+"function_"+str(i)+"()\n"
	with open(file,"a") as f:
		f.write('''
#__CLOUDBOOK:MAIN__
def main():
	'''+invocations+'''
	return 0
''')
	return 0

#generate files for 2,10,100 and 1000 functions
for i in (2,10,100,1000):
	filename = "test_"+str(i)+".py"
	if os.path.exists(filename):
  		os.remove(filename)
	#file = open(filename,"w")
	for j in range(i):
		if j == i-1:
			gen_main_function(j,filename)
		else:
			gen_function(j,filename)