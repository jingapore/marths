import numpy as np
import matplotlib.pyplot as plt
import math

def plot_threeVectors(a_1=1.0, a_2=0.0, b_1=-0.5, b_2=math.sqrt(3)/2, c_1=-0.5, c_2=-math.sqrt(3)/2):
		
	arg_dict = locals()

	fig, ax = plt.subplots(1, 1)
	ax.grid(True, which='Major')
	sorted_args = sorted(arg_dict.items(), key=lambda kv: kv[0]) #sorted by key, i.e. a_1, a_2 ... z_1, z_2.
	sorted_vals = [kv[1] for kv in sorted_args]
	sorted_vals = iter(sorted_vals) #convert to iterator, so that zip will pass next method, resulting in (1st_val, 2nd_val) instead of (1st_val, 1st_val)
	sorted_tuples = zip(sorted_vals, sorted_vals)
	
	#Set up plots.
	ax.set_xlim(left=-2, right=2)
	ax.set_ylim(bottom=-2, top=2)

	for vector in sorted_tuples:
		ax.arrow(x=0, y=0, dx=vector[0], dy=vector[1], head_width=0.15, head_length=0.15)
	
#     plt.show()
	
	return ax


def get_point_on2DPlane(a, b, c, d):
	'''
	Purpose: Get point from a,b, or c, whichever is non-zero.
	'''
	
	for idx, val in list(enumerate(np.array([a,b,c]))):
		if val != 0:
			point_coords = np.zeros(3)
			point_coords[idx] = -d/val
			break
		else:
			pass
	
	return point_coords
	
def plot_2Dplane_in3D(coefficient_array, d, n):
	'''
	Purpose:
	A plane is a*x+b*y+c*z+d=0. [a,b,c] is the normal.
	Output arrays that can be plotted as 3D plane in MPL.
	
	Params:
	n: Size of meshfield to calculate. Field will be defined as nxn.
	
	Output:
	Arrays of x, y, z. Each array has dim nxn. z[i,j] is calculated from x[i,j], y[i,j], with hints of a Rank 2 outcome.
	'''
	
	a, b, c = coefficient_array
	
	normal = np.array([a,b,c])
	point = get_point_on2DPlane(a, b, c, d)
	x, y = np.meshgrid(range(n), range(n))
	
	if normal[2] != 0:
		# z = np.copy(x)
		# x = (-normal[1]*y-normal[2]*z-d)/(normal[0]) #normal multiplied by val + d
		z = (-normal[0]*x-normal[1]*y-d)/(normal[2]) #normal multiplied by val + d
	elif normal[2] ==0:
		z = np.copy(y)
		y = (-normal[0]*x-d)/(normal[1])
			
	return x, y, z, point
