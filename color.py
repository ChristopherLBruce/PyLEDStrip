"""
Wrapper for tuple class used to replicate neopixel module functionality

**Author:**

   Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
"""

class Color( tuple ):
	"""
	Wrapper for tuple class used to replicate neopixel module functionality

	**Arguments:**

		:``r``: `int` Red value for color. Range is 0 - 255
		:``g``: `int` Green value for color. Range is 0 - 255
		:``b``: `int` Blue value for color. Range is 0 - 255

	**Keword Arguments:**

		None

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	def __new__ ( cls, _r, _g, _b ):
		return super( Color, cls ).__new__( cls, ( _r, _g, _b ) )


	def __init__( self, _r, _g, _b ):
		self.red		= self.r	= sorted( ( 0, abs( int( _r ) ), 255 ) )[ 1 ]
		self.green	= self.g	= sorted( ( 0, abs( int( _g ) ), 255 ) )[ 1 ]
		self.blue	= self.b	= sorted( ( 0, abs( int( _b ) ), 255 ) )[ 1 ]


	def __str__( self ):
		return '( {}, {}, {} )'.format( self.r, self.g, self.b )


	def __add__( self, color ):
		if isinstance( color, Color ):
			r	= color.r
			g	= color.g
			b	= color.b

		if isinstance( color, float ) or isinstance( color, int ):
			r	= int( 255.0 * color )
			g	= int( 255.0 * color )
			b	= int( 255.0 * color )

		r	+= self.r
		g	+= self.g
		b	+= self.b

		return Color( r, g, b )


	def __sub__( self, color ):
		if isinstance( color, Color ):
			r	= color.r
			g	= color.g
			b	= color.b

		if isinstance( color, float ) or isinstance( color, int ):
			r	= int( 255.0 * color )
			g	= int( 255.0 * color )
			b	= int( 255.0 * color )

		r	-= self.r
		g	-= self.g
		b	-= self.b

		return Color( r, g, b )


	def __mul__( self, color ):
		if isinstance( color, Color ):
			r	= color.r
			g	= color.g
			b	= color.b

		if isinstance( color, float ) or isinstance( color, int ):
			r	= int( 255.0 * color )
			g	= int( 255.0 * color )
			b	= int( 255.0 * color )

		r	= ( self.r / 255 * r / 255 ) * 255
		g	= ( self.g / 255 * g / 255 ) * 255
		b	= ( self.b / 255 * b / 255 ) * 255

		return Color( r, g, b )


	# def __div__( self, color ):
	# 	if isinstance( color, tuple ):
	# 		color		= Color( color )
	# 	elif isinstance( color, list ):
	# 		color		= Color( *color )

	# 	if isinstance( color, Color ):
	# 		return Color( self._r / color._r, self._g / color._g, self._b / color._b )


	# __truediv__ = __div__


	def blend( self, color, bias = 0.5 ):
		"""
		Blends two colors using a bias value

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		if isinstance( color, tuple ) or isinstance( color, list ):
			color	= Color( *color )

		if not isinstance( color, Color ):
			return None

		inverse	= 1.0 - bias
		color		= ( self * bias ) + ( color * inverse )

		return color
