#simple apoximation to nbody problem
from random import randint
import time
import math
import json

#global vars
body_list = [(10, 12, 76, -10, -7), (10, -71, -57, -4, 5), (10, 81, -52, 6, -10), (10, 30, 32, -9, 4), (10, -94, 20, -10, 0), (10, 65, -70, 9, -9), (10, 12, 1, -10, 10), (10, 4, 88, 7, -5), (10, 16, -73, 1, 8), (10, 4, -35, 1, 10), (10, -32, 80, -9, 4), (10, 33, -69, 8, -3), (10, -6, -94, 5, -9), (10, -81, 68, 6, -8), (10, -52, -33, 5, 4), (10, 37, 48, 5, -6), (10, 59, 46, 5, 10), (10, -40, 11, 4, 1), (10, -43, 4, 0, 1), (10, -80, 97, -10, -3), (10, 59, 33, 9, 6), (10, 88, -14, 1, -6), (10, -69, 72, -9, 5), (10, -62, 65, 5, -7), (10, 17, -39, 9, 1), (10, 65, -75, -8, 4), (10, -16, 52, 2, -8), (10, -77, 65, -1, -9), (10, -65, -74, -8, -2), (10, 82, -98, 6, -10), (10, 39, 56, 8, -6), (10, 63, -100, -8, -9), (10, -41, 26, -2, -8), (10, 44, -47, -1, -9), (10, -5, 63, 10, 10), (10, -18, -48, 10, 8), (10, 72, 42, 2, -2), (10, -56, -14, -8, -7), (10, 1, -20, 8, 7), (10, 38, -64, 4, 6), (10, 89, -78, -10, 1), (10, -73, 58, -9, -1), (10, -56, -66, 8, -3), (10, 12, -68, -5, 5), (10, 9, -85, 9, -5), (10, -75, -89, -9, 4), (10, 10, -7, -8, 10), (10, -30, -83, 0, 7), (10, -21, 0, -3, -7), (10, -63, 93, -4, -1), (10, 73, 66, 3, -7), (10, 20, 37, -3, 5), (10, -95, 16, 7, 7), (10, -8, -54, 4, 2), (10, 72, 49, -9, -10), (10, -94, -98, -6, -8), (10, 95, 17, -3, 7), (10, -95, 39, -2, -2), (10, 19, 21, -7, 8), (10, -97, 55, 6, 3), (10, 70, 100, 7, -9), (10, 99, -4, 8, -7), (10, -13, 66, 2, -1), (10, 49, 38, 10, 9), (10, 40, 62, -9, 3), (10, 15, 85, -5, 1), (10, -80, 51, 7, -8), (10, -72, 35, 6, -4), (10, 22, -90, -9, 7), (10, 58, -40, -7, 3), (10, -66, -44, 9, -8), (10, 17, -67, -9, -4), (10, -87, 13, -10, -6), (10, -33, 11, 6, 4), (10, -61, 93, -3, -2), (10, 71, 77, -8, -5), (10, -30, 23, 2, 3), (10, 80, -73, 5, -6), (10, -61, 43, -6, 1), (10, -85, -68, -3, 8), (10, -24, 99, -1, 6), (10, -28, 70, 0, 2), (10, -66, -95, 10, 10), (10, 21, -83, -2, 6), (10, 19, 34, 2, -2), (10, -20, 63, 1, 9), (10, -55, 81, -5, 4), (10, 7, 76, 3, -7), (10, -62, 42, 1, 8), (10, 56, 78, 2, 2), (10, 47, -61, -6, -4), (10, -66, 43, 7, 6), (10, -95, 69, 3, 1), (10, -18, 50, 9, 10), (10, 29, 81, -3, -7), (10, -61, -66, 5, 5), (10, 9, 23, -1, 1), (10, 47, -28, -4, 8), (10, -68, -84, -3, -2), (10, -8, 26, 0, -2)]
body_new = []
CONST_N = 100

#__CLOUDBOOK:PARALLEL__
def compute_body(single_body, iteration):
	global body_list
	global body_new
	
	fx=0.0
	fy=0.0
	for i in body_list:
		#print("i",i)
		delta_f = compute_contribution_force(single_body,i)
		fx = fx+delta_f[0]
		fy = fy+delta_f[1]
	ax = fx/float(single_body[0])
	ay = fy/float(single_body[0])
	vx = float(single_body[3])+ax
	vy = float(single_body[4])+ay
	x = float(single_body[1])+vx
	y = float(single_body[2])+vy	
	
	new_single_body = (single_body[0],x,y,vx,vy)
	body_new.append(new_single_body)
	#print("Exit from computebody")

#__IDEMPOTENT__
def compute_contribution_force(bodyA, bodyB):
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
	dx = math.sqrt((x1-x2)**2)
	if dx != 0:
		fx = (m1*m2)/(dx**2)
	else:
		fx=0
	if x2<x1:
		fx = -fx
	dy = math.sqrt((y1-y2)**2)
	if dy!=0:
		fy = (m1*m2)/(dy**2)
	else:
		fy=0
	if y2<y1:
		fy = -fy
	return (fx,fy)

def main():
	global body_list
	MAX_ITERATIONS = 10	
	start = time.time()
	
	for j in range(MAX_ITERATIONS):
		print(j,"==>",body_list)
		print("starting iteration", j)
		for i in body_list:
			compute_body(i,j)
		#SYNC
		global body_new
		body_list = body_new
		global body_list
		body_new = []
		print("iteration ", j, " executed")
	end = time.time()
	print("duration: ", end-start)
	return body_list

main()