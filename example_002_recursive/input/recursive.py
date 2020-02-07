import json


#__CLOUDBOOK:PARALLEL__
def recursive_function(x):
	print (x)
	recursive_function(x+1)

def main():
	recursive_function(0)

main()
