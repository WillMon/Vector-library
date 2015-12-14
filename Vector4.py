#william montero
# Vector4, wam 1116

import math 
from math import *

class Vector4(object):
	def __init__(self, r=0,g=0,b=0,a=0, array = []):
		self.r = r
		self.g = g
		self.b = b
		self.a = a
	
	def add(self, UserInput ):
		TempVariable = Vector4()
		TempVariable.r = self.r + UserInput.r
		TempVariable.g = self.g + UserInput.g
		TempVariable.b = self.b + UserInput.b
		TempVariable.b = self.b + UserInput.b
		return TempVariable
		
	def sub(self, UserInput):
		TempVariable = Vector4()
		TempVariable.r = self.r - UserInput.r
		TempVariable.g = self.g - UserInput.g
		TempVariable.b = self.b - UserInput.b
		TempVariable.b = self.a - UserInput.a
		return TempVariable
		
	def DotPro(self, UserInput):
		total = 0
		total += self.r * UserInput.r
		total += self.g * UserInput.g
		total += self.b * UserInput.b
		total += self.a * UserInput.a
		return total
		
	def CrossPro(self, UserInput):
		TempVariable = Vector4()
		TempVariable.r = (self.g * UserInput.b) - (self.b * UserInput.g)
		TempVariable.g = (self.b * UserInput.a) - (self.a * UserInput.b)
		TempVariable.b = (self.a * UserInput.r) - (self.r * UserInput.a)
		TempVariable.a = (self.r * UserInput.g) - (self.g * UserInput.r)
		return TempVariable
		
	def LinerIntro(self, UserInput):
		TempVariable = Vector4()
		TempVariable.r = self.r + .5 * (UserInput.r - self.r)
		TempVariable.g = self.g + .5 * (UserInput.g - self.g)
		TempVariable.b = self.b + .5 * (UserInput.b - self.b)
		TempVariable.a = self.a + .5 * (UserInput.a - self.a)
		return TempVariable
		
	def Magnitude(self):
		V4RR =+ self.r * self.r
		V4GG =+ self.g * self.g 
		V4BB =+ self.b * self.b 
		V4AA =+ self.a * self.a
		total = sqrt(V4RR + V4BB + V4GG + V4AA)
		return total
		
	def Normalizer(self):
		TempVariable = Vector4()
		TempVariable.r = self.r / self.Magnitude()
		TempVariable.g = self.g / self.Magnitude()
		TempVariable.b = self.b / self.Magnitude()
		TempVariable.a = self.a / self.Magnitude()
		return TempVariable
		
	"""def Hexadecimal(UserInput):
		if(UserInput[0] == '#'):
			TempArray[6]
			TempVariable = Vector4()
			for i in xrang(6):
				TempArray[i - 1] = ord(UserInput[i])
				if(TempArray[j] / 10 == 4 | TempArray[j] / 10 == 5):
					TempArray[j] = TempArray[j] - 48;
				elif (TempArray[j] / 10 == 6 | TempArray[j] / 10 == 7):
					TempArray[j] = TempArray[j] - 55;
				else:
					TempArray[j] = TempArray[j];"""
		