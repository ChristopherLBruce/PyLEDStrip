""" Color class for storing and manipulating RGB color values """

class Color():
	"""Color class to store and manipulate RGB values """

	__slots__ = 'r', 'g', 'b'

	def __init__(self, r, g, b):
			"""Create new instance of Color(r, g, b)"""
			self.r = r
			self.g = g
			self.b = b


	def __repr__(self):
		"""Returns a nicely formatted representation string"""
		return '({}, {}, {})'.format( self.r, self.g, self.b )


	def __iter__(self):
		"""Itterator for RGB values"""
		for x in [ self.r, self.g, self.b ]:
			yield x


	def __add__(self, color):
		"""method for '+' operator"""
		if isinstance(color, Color):
			r, g, b = color.r, color.g, color.b
		elif isinstance(color, float) or isinstance(color, int):
			r, g, b = [int(255 * color)] * 3

		r = self._clamp( self.r + r )
		g = self._clamp( self.g + g )
		b = self._clamp( self.b + b )

		return Color(r, g, b)


	def __sub__(self, color):
		"""method for '-' operator"""
		if isinstance(color, Color):
			r, g, b = color.r, color.g, color.b
		elif isinstance(color, float) or isinstance(color, int):
			r, g, b = [int(255 * color)] * 3

		r = self._clamp( self.r - r )
		g = self._clamp( self.g - g )
		b = self._clamp( self.b - b )

		return Color(r, g, b)


	def __mul__(self, color):
		"""method for '*' operator"""
		if isinstance(color, Color):
			r, g, b = color.r, color.g, color.b
		elif isinstance(color, float) or isinstance(color, int):
			r, g, b = [int(255 * color)] * 3

		r = self._clamp(int((self.r / 255) * (r / 255) * 255))
		g = self._clamp(int((self.g / 255) * (g / 255) * 255))
		b = self._clamp(int((self.b / 255) * (b / 255) * 255))

		return Color(r, g, b)


	def _clamp(self, value):
		"""Ensures RGB value are between 0 and 255"""
		return sorted( ( 0, abs( int( value ) ), 255 ) )[ 1 ]


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
			r, g, b = color.r, color.g, color.b
		elif isinstance(color, float) or isinstance(color, int):
			r, g, b = [int(255 * color)] * 3

		inv = 1 - bias
		r = self._clamp(int(self.r * bias) + int(r * inv))
		g = self._clamp(int(self.g * bias) + int(g * inv))
		b = self._clamp(int(self.b * bias) + int(b * inv))

		return Color(r, g, b)
