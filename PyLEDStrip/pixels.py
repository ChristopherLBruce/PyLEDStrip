"""[summary]

Returns:
	[type] -- [description]
"""

import time
from collections import deque

from .color import Color



class Pixels( ):
	"""
	Ordered collection of pixel Colors

	**Arguments:**

		:``r``: `int` Red value for color. Range is 0 - 255
		:``g``: `int` Green value for color. Range is 0 - 255
		:``b``: `int` Blue value for color. Range is 0 - 255

	**Keword Arguments:**

		None

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	# def __new__ ( cls ):
	# 	return super( Pixels, cls ).__new__( cls, ( _colors ) )


	def __init__( self, _colors ):
		if isinstance( _colors, Pixels ):
			self.colors	= [ c for c in _colors.colors ]
		else:
			self.colors	= _colors


	def __str__( self ):
		_colors = [ p for p in self.colors ]
		print( _colors )

		return _colors


	def __add__( self, other ):
		if isinstance( other, Color ):
			other = Pixels( [ other ] * len( self.colors ) )

		if not isinstance( other, Pixels ):
			return None

		return Pixels( [ c1 + c2 for c1, c2 in zip( self.colors, other.colors ) ] )


	def __sub__( self, other ):
		if isinstance( other, Color ):
			other = Pixels( [ other ] * len( self.colors ) )

		if not isinstance( other, Pixels ):
			return None

		return Pixels( [ c1 - c2 for c1, c2 in zip( self.colors, other.colors ) ] )


	def __mul__( self, others ):
		if isinstance( other, Color ):
			other = Pixels( [ other ] * len( self.colors ) )

		if not isinstance( other, Pixels ):
			return None

		return Pixels( [ c1 * c2 for c1, c2 in zip( self.colors, other.colors ) ] )


	def add( self, other ):
		if isinstance( other, Color ):
			for c1, c2 in zip ( self.colors, [ other ] * len( self.colors ) ):
				c1.add( c2 )
		if isinstance( other, Pixels ):
			for c1, c2 in zip ( self.colors, other.colors ):
				c1.add( c2 )

		return self


	def subtract( self, other ):
		if isinstance( other, Color ):
			for c1, c2 in zip( self.colors, [ other ] * len( self.colors ) ):
				c1.subtract( c2 )
		if isinstance( other, Pixels ):
			for c1, c2 in zip ( self.colors, other.colors ):
				c1.subtract( c2 )

		return self


	def multiply( self, other ):
		if isinstance( other, Color ):
			for c1, c2 in zip( self.colors, [ other ] * len( self.colors ) ):
				c1.multiply( c2 )
		if isinstance( other, Pixels ):
			for c1, c2 in zip( self.colors, other.colors ):
				c1.multiply( c2 )

		return self


	def blend( self, other, bias = 0.5 ):
		if isinstance( other, Color ):
			colors = [ other ] * len( self.colors )
		if isinstance( other, Pixels ):
			colors = other.colors

		for c1, c2 in zip( self.colors, colors ):
			c1.blend( c2, bias )

		return self


	def draw( self, strip ):
		"""
		Draws the strip

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		for i, color in enumerate( self.colors ):
			strip.set_led_color( i, color )

		strip.show( )

		return True


	def offset( self, offset = 1 ):
		"""
		Offsets the array of pixel colors

		**Arguments:**

			None

		**Keword Arguments:**

			:``offset``:	`int` Amount to offset the list. Positive values offset left to right. Negative values are reversed. Default is 1.

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		self.colors	= deque( self.colors )
		self.colors.rotate( offset )
		self.colors	= list( self.colors )

		return self.colors


	def scroll( self, strip, offset = 1, wait_ms = 10 ):
		"""
		Scrolls an array of pixels across the strip

		**Arguments:**

			None

		**Keword Arguments:**

			:``offset``:	`int` Amount to offset the list. Positive values offset left to right. Negative values are reversed. Default is 1.
			:``wait_ms``:	`int` Amount of time in miliseconds between each step

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		while True:
			for _pixel in range( len( self.colors ) ):
				if not strip.testing:
					return True

				self.draw( strip )
				time.sleep( wait_ms / 1000.0 )

				self.offset( offset = offset )

		return self
