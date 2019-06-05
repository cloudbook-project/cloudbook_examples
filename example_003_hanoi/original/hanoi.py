import sys

#__CLOUDBOOK:RECURSIVE__
def move_tower(height,origin, destination,intermediate):
	if height>=1:
		move_tower(height-1,origin,intermediate,destination)
		print ("move disc from "+str(origin)+" to "+str(destination))
		move_tower(height-1,intermediate,destination,origin)

def main():
	#sys.setrecursionlimit(10)#El tope de hanoi es 5 pisos con esto
	move_tower(5,1,2,3)

main()