# Will Mon
# Vector 3, wam1116

import math
from math import *

class Vector3(object):
	
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y 
		self.z = z
	def add(self, UserInput ):
		TempVariable = Vector3()
		TempVariable.x = self.x + UserInput.x
		TempVariable.y = self.y + UserInput.y
		TempVariable.z = self.z + UserInput.z
		return TempVariable
		
	def sub(self, UserInput):
		TempVariable = Vector3()
		TempVariable.x = self.x - UserInput.x
		TempVariable.y = self.y - UserInput.y
		TempVariable.z = self.z - UserInput.z
		return TempVariable
		
	def DotPro(self, UserInput):
		total = 0
		total += self.x * UserInput.x
		total += self.y * UserInput.y
		total += self.z * UserInput.z
		return total
		
	def CrossPro(self, UserInput):
		TempVariable = Vector3()
		TempVariable.x = (self.y * UserInput.z) - (self.z * UserInput.y)
		TempVariable.y = (self.z * UserInput.x) - (self.x * UserInput.z)
		TempVariable.z = (self.x * UserInput.y) - (self.y * UserInput.x)
		return TempVariable
		
	def LinerIntro(self, UserInput):
		TempVariable = Vector3()
		TempVariable.x = self.x + .5 * (UserInput.x - self.x)
		TempVariable.y = self.y + .5 * (UserInput.y - self.y)
		TempVariable.z = self.z + .5 * (UserInput.z - self.z)
		return TempVariable
		
	def Magnitude(self):
		total = 0 
		V3XX = 0 
		V3YY = 0
		V3ZZ = 0
		V3XX =+ self.x * self.x
		V3YY =+ self.y * self.y 
		V3ZZ =+ self.z * self.z 
		total = sqrt(V3XX + V3YY + V3ZZ)
		return total
		
	def Normalizer(self):
		TempVariable = Vector3()
		TempVariable.x = self.x / self.Magnitude()
		TempVariable.y = self.y / self.Magnitude()
		TempVariable.z = self.z / self.Magnitude()
		return TempVariable
		
		
		
	
		
	
	