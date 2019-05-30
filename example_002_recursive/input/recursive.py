import json


#__CLOUDBOOK:PARALLEL__
def recursive_function(x):
	#if (x>994):
	#	return
	
	print (x)
	recursive_function(x+1)

def main():
	recursive_function(0)

main()