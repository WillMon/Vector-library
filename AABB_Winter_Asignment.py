#will mon
#AABB Winter asignment

import math
import Vector4
import Vector2

from math import *
from Vector4 import *
from Vector2 import *

AxesList = []
"""for index in range(8):
		PreUserInput = eval(input("Place varialbe: "))

		AxesList.append(PreUserInput) 
		AxesList.sort()
	
	print("Enough input")"""
def AABBlist():
	
	x_axes_pares = Vector4()
	x_axes_list = []
	x_axes_sort = []
	
	for i in range(4):
		min_userInput = eval(input("Enter in the min: "))
		max_userInput = eval(input("Enter in the max: "))
		x_axes_list.append(min_userInput)
		x_axes_list.append(max_userInput)
	x_axes_sort.extend(sorted(x_axes_list))
	print(x_axes_sort)
	print(x_axes_list)	
	

AABBlist()