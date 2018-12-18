"""
Wrapper for tuple class used to replicate neopixel module functionality

**Author:**

   Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
"""
# from functools import wraps
from types import MethodType
from collections import namedtuple



Color = namedtuple('Color', ('r, g, b'))



def __add__(self, color):
	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [int(255.0 * color)] * 3

	r += self.r
	g += self.g
	b += self.b

	return Color( r, g, b )


def __sub__(self, color):
	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [int(255.0 * color)] * 3

	r -= self.r
	g -= self.g
	b -= self.b

	return Color( r, g, b )


def __mul__(self, color):
	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [int(255.0 * color)] * 3

	r *= self.r
	g *= self.g
	b *= self.b

	return Color( r, g, b )



def _clamp( self, value ):
	return sorted( ( 0, abs( int( value ) ), 255 ) )[ 1 ]


def add( self, color ):
	if isinstance( color, Color ):
		r, g, b	= color
	elif isinstance( color, float ) or isinstance( color, int ):
		r, g, b	= [ int( 255.0 * color ) ] * 3

	self.r = self._clamp(self.r + r)
	self.g = self._clamp(self.g + g)
	self.b = self._clamp(self.b + b)

	return self


def subtract(self, color):
	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [ int( 255.0 * color ) ] * 3

	self.r = self._clamp(self.r - r)
	self.g = self._clamp(self.g - g)
	self.b = self._clamp(self.b - b)

	return self


def multiply(self, color):
	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [int(255.0 * color)] * 3

	self.r = self._clamp(self.r * r)
	self.g = self._clamp(self.g * g)
	self.b = self._clamp(self.b * b)

	return self


def blend(self, color, bias = 0.5):
	"""
	Blends two colors using a bias value

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [int(255.0 * color)] * 3

	inv = 1 - bias
	r = (r * inv) + (self.r * bias)
	g = (g * inv) + (self.g * bias)
	b = (b * inv) + (self.b * bias)

	self.r = self._clamp(r)
	self.g = self._clamp(g)
	self.b = self._clamp(b)

	return self


# extend Color class methods
Color.__add__ = __add__
Color.__sub__ = __sub__
Color.__mul__ = __mul__
Color._clamp = _clamp
Color.add = add
Color.subtract = subtract
Color.multiply = multiply
Color.blend = blend




red = Color(255, 0, 0)
green = Color(0, 255, 0)
white = Color(255, 255, 255)
black = Color(255, 255, 255)
print(red + green)
# red.blend( green, bias = 0.5)
red.b = 255
print( red.r )