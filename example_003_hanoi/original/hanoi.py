import sys

#__CLOUDBOOK:RECURSIVE__
def move_tower(height,origin, destination,intermediate,level):
	level=level+1
	print ("=====================================> DEPTH LEVEL:",level)
	if height>=1:
		move_tower(height-1,origin,intermediate,destination,level)
		print ("move disc from "+str(origin)+" to "+str(destination))
		move_tower(height-1,intermediate,destination,origin,level)

def main():
	#sys.setrecursionlimit(10)#El tope de hanoi es 5 pisos con esto
	move_tower(1500,1,2,3,0)

main()