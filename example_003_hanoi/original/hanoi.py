

#__CLOUDBOOK:PARALLEL__
def move_tower(height,origin, destination,intermediate):
	if height>=1:
		move_tower(height-1,origin,intermediate, destination)
		print ("@ move disc from "+origin+" to "+destination)
		move_tower(height-1,intermediate, destination,origin)

move_tower(1000,"A","B","C")