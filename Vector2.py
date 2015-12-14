#William Montero
#Vector 2, wam1116
import math
from math import *

class Vector2(object):

		def __init__(self, x=0 , y=0):
			self.x = x
			self.y = y
			
		def add(self, UserInput ):
			TempVariable = Vector2()
			TempVariable.x = self.x + UserInput.x
			TempVariable.y = self.y + UserInput.y
			return TempVariable
		
		def sub(self, UserInput):
			TempVariable = Vector2()
			TempVariable.x = self.x - UserInput.x
			TempVariable.y = self.y - UserInput.y
			return TempVariable
			
		def DotPro(self,UserInput):
			total = 0
			total += self.x * UserInput.x
			total += self.y * UserInput.y
			return total
			
		def LinerIntro(self, UserInput):
			TempVariable = Vector2()
			TempVariable.x = self.x + .5 * (UserInput.x - self.x)
			TempVariable.y = self.y + .5 * (UserInput.y - self.y)
			return TempVariable
		
		def Magnitude(self):
			total = 0 
			V2XX = 0 
			V2YY = 0
			V2XX = self.x * self.x
			V2YY = self.y * self.y
			total = sqrt(V2XX + V2YY)
			return total
		
		def Normalizer(self):
			TempVariable = Vector2()
			TempVariable.x = self.x / self.Magnitude()
			TempVariable.y = self.y / self.Magnitude()
			return TempVariable
			
		def Radions(self):
			TempVariable = Vector2()
			TempVariable.x = 3.14 / 180 * self.x
			TempVariable.y = 3.14 / 180 * self.y
			return TempVariable
			
		def Degrees(self):
			TempVariable = Vector2()
			TempVariable.x = 180 / 3.14 * self.x
			TempVariable.y = 180 / 3.14 * self.y
			return TempVariable
			
			
			
		
							
			



