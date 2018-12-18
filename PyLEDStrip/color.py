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
		super( Color, self ).__init__( )

		self.r	= self._clamp( _r )
		self.g	= self._clamp( _g )
		self.b	= self._clamp( _b )


	def __str__( self ):
		return '( {}, {}, {} )'.format( self.r, self.g, self.b )


	def __add__( self, color ):
		if isinstance( color, Color ):
			r, g, b	= color
		elif isinstance( color, float ) or isinstance( color, int ):
			r, g, b	= [ int( 255.0 * color ) ] * 3

		r	+= self.r
		g	+= self.g
		b	+= self.b

		return Color( r, g, b )


	def __sub__( self, color ):
		if isinstance( color, Color ):
			r, g, b	= color
		elif isinstance( color, float ) or isinstance( color, int ):
			r, g, b	= [ int( 255.0 * color ) ] * 3

		r	-= self.r
		g	-= self.g
		b	-= self.b

		return Color( r, g, b )


	def __mul__( self, color ):
		if isinstance( color, Color ):
			r, g, b	= color
		elif isinstance( color, float ) or isinstance( color, int ):
			r, g, b	= [ int( 255.0 * color ) ] * 3

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

	def _clamp( self, value ):
		return sorted( ( 0, abs( int( value ) ), 255 ) )[ 1 ]


	def add( self, color ):
		if isinstance( color, Color ):
			r, g, b	= color
		elif isinstance( color, float ) or isinstance( color, int ):
			r, g, b	= [ int( 255.0 * color ) ] * 3

		self.r	= self._clamp( self.r + r )
		self.g	= self._clamp( self.g + g )
		self.b	= self._clamp( self.b + b )

		return self


	def subtract( self, color ):
		if isinstance( color, Color ):
			r, g, b	= color
		elif isinstance( color, float ) or isinstance( color, int ):
			r, g, b	= [ int( 255.0 * color ) ] * 3

		self.r	= self._clamp( self.r - r )
		self.g	= self._clamp( self.g - g )
		self.b	= self._clamp( self.b - b )

		return self


	def multiply( self, color ):
		if isinstance( color, Color ):
			r, g, b	= color
		elif isinstance( color, float ) or isinstance( color, int ):
			r, g, b	= [ int( 255.0 * color ) ] * 3

		self.r	= self._clamp( self.r * r )
		self.g	= self._clamp( self.g * g )
		self.b	= self._clamp( self.b * b )

		return self


	def blend( self, color, bias = 0.5 ):
		"""
		Blends two colors using a bias value

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		if isinstance( color, Color ):
			r, g, b	= color
		elif isinstance( color, float ) or isinstance( color, int ):
			r, g, b	= [ int( 255.0 * color ) ] * 3

		r	= ( r * ( 1 - bias ) ) + ( self.r * bias )
		g	= ( g * ( 1 - bias ) ) + ( self.g * bias )
		b	= ( b * ( 1 - bias ) ) + ( self.b * bias )

		self.r	= self._clamp( r )
		self.g	= self._clamp( g )
		self.b	= self._clamp( b )

		return self
