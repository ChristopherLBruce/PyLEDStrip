""" Color class for storing and manipulating RGB color values """

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


def clamp(self, value):
	"""Ensures value are between 0 and 255"""
	return sorted( ( 0, abs( int( value ) ), 255 ) )[ 1 ]


def add(self, color):
	"""Adds color to self

	Arguments:
		color {Color} -- Color value to blend with self. If a float or int is
			given instead, that is converted to r, g, b values.

	Returns:
		self -- The instance of this object
	"""

	if isinstance( color, Color ):
		r, g, b	= color
	elif isinstance( color, float ) or isinstance( color, int ):
		r, g, b	= [ int( 255.0 * color ) ] * 3

	self.r = self.clamp(self.r + r)
	self.g = self.clamp(self.g + g)
	self.b = self.clamp(self.b + b)

	return self


def subtract(self, color):
	"""Subtracts color from self"

	Arguments:
		color {Color} -- Color value to blend with self. If a float or int is
			given instead, that is converted to r, g, b values.

	Returns:
		self -- The instance of this object
	"""

	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [ int( 255.0 * color ) ] * 3

	self.r = self.clamp(self.r - r)
	self.g = self.clamp(self.g - g)
	self.b = self.clamp(self.b - b)

	return self


def multiply(self, color):
	"""Multiplies color with self

	Arguments:
		color {Color} -- Color value to blend with self. If a float or int is
			given instead, that is converted to r, g, b values.

	Returns:
		self -- The instance of this object
	"""

	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [int(255.0 * color)] * 3

	self.r = self.clamp(self.r * r)
	self.g = self.clamp(self.g * g)
	self.b = self.clamp(self.b * b)

	return self


def blend(self, color, bias = 0.5):
	"""Blends color with self

	Arguments:
		color {Color} -- Color value to blend with self. If a float or int is
			given instead, that is converted to r, g, b values.

	Keyword Arguments:
		bias {float} -- Bias value for blending color with self (default: {0.5})

	Returns:
		self -- The instance of this object
	"""
	if isinstance(color, Color):
		r, g, b = color
	elif isinstance(color, float) or isinstance(color, int):
		r, g, b = [int(255.0 * color)] * 3

	inv = 1 - bias
	r = (r * inv) + (self.r * bias)
	g = (g * inv) + (self.g * bias)
	b = (b * inv) + (self.b * bias)

	self.r = self.clamp(r)
	self.g = self.clamp(g)
	self.b = self.clamp(b)

	return self


# extend Color class methods
Color.__add__ = __add__
Color.__sub__ = __sub__
Color.__mul__ = __mul__
Color.clamp = clamp
Color.add = add
Color.subtract = subtract
Color.multiply = multiply
Color.blend = blend



# Test stuff
red = Color(255, 0, 0)
green = Color(0, 255, 0)
white = Color(255, 255, 255)
black = Color(255, 255, 255)
print(red + green)

red.blend( green, bias = 0.5 )
print( red )		# should return Color(r=127, g=127, b=0)
