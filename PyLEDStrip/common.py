#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Common functions shared by package

**Author:**

	Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
"""

import colorsys

# from colour import Color
from .const import *
from .color import Color



def gradient( color1, color2, length = 6, mirror = False ):
	"""
	Creates a color gradient between col1 and col2 of given length

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	pixels = [ color1 ] * length

	if mirror:
		half	= int( length / 2 )
		for i in range( 0, half ):
			bias				= 1.0 - ( float( i ) / half )
			pixels[ i ].blend( color2, bias = bias )
		for i in range( half, length ):
			bias				= float( i - half ) / half
			pixels[ i ].blend( color2, bias = bias )
	else:
		for i in range( length ):
			bias				= 1.0 - ( float( i ) / length )
			pixels[ i ].blend( color2, bias = bias )


	return pixels


def create_loop( end, start = 0 ):
	"""
	Geneates a loop from start -> end -> start

	**Arguments:**

		:``end``: `int` End value of the loop

	**Keword Arguments:**

		:``start``: `int` Start value of the loop. Default is 0

	**Returns:**

		:``[type]``: [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	return list( range ( start, end - 1 ) ) + list ( reversed ( range ( start + 1, end ) ) )


def wheel( pos ):
	"""
	Generate rainbow colors across 0-255 positions.

	**Arguments:**

		:``pos``: `int` Hue position on a color wheel. Valid range is 0-255

	**Keword Arguments:**

		None

	**Returns:**

		:``Color``: Color object representing RGB values of a color

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	if pos < 85:
		return Color( pos * 3, 255 - pos * 3, 0 )
	elif pos < 170:
		pos -= 85
		return Color( 255 - pos * 3, 0, pos * 3 )
	else:
		pos -= 170
		return Color( 0, pos * 3, 255 - pos * 3 )


def hsv_to_color( h, s = 1.0, v = 1.0 ):
	"""
	Converts HSV to Color

	**Arguments:**

		:``h``: `float` Hue. Range is 0.0 - 1.0

	**Keword Arguments:**

		:``s``: `float` Saturation. Range is 0.0 - 1.0. Default is 1.0
		:``v``: `float` Value. Range is 0.0 - 1.0. Default is 1.0

	**Returns:**

		:``Color``: Color object representing RGB values of a color

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""
	
	r, g, b = colorsys.hsv_to_rgb( h, 1.0, 1.0 )

	return Color( r * 255, g * 255, b* 255 )
