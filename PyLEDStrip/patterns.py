#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
These patterns function by drawing the entire strip at once

**Author:**

	Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
"""

import time
import random
from collections import deque

from . import const, common
from .color import Color
from .pixels import Pixels


################################################################################
## These functions update LEDs direction
################################################################################

def colorWipe( strip, wait_ms = 25 ):
	"""
	Wipe color across display a pixel at a time.

	**Arguments:**

		:``strip``: `[type]` [description]
		:``color``: `[type]` [description]

	**Keword Arguments:**

		:``wait_ms``: `int` [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	while True:
		for color in [ const.red, const.green, const.blue ]:
			for pixel in range( 0, strip.numPixels( ) ):
				strip.setPixelColor( pixel, color )

				if not strip.testing:
					return True

				strip.show( )

				time.sleep( wait_ms / 1000.0 )


def theaterChase( strip, color = const.white, wait_ms = 50 ):
	"""
	Movie theater light style chaser animation.

	**Arguments:**

		:``strip``: `[type]` [description]
		:``color``: `[type]` [description]

	**Keword Arguments:**

		:``wait_ms``: `int` [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	while True:
		for q in range( 3 ):
			for i in range( 0, strip.numPixels( ), 3 ):
				strip.setPixelColor( i + q, color )

			if not strip.testing:
				return True

			strip.show( )
			time.sleep( wait_ms / 1000.0 )

			for i in range( 0, strip.numPixels( ), 3 ):
				strip.setPixelColor( i + q, 0)


def rainbow( strip, wait_ms = 10 ):
	"""
	Draw rainbow that fades across all pixels at once.

	**Arguments:**

		:``strip``: `[type]` [description]

	**Keword Arguments:**

		:``wait_ms``: `int` [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	while True:
		for i in range( 256 ):
			for pixel in range( strip.numPixels( ) ):
				strip.setPixelColor( pixel, common.wheel( ( i + pixel ) & 255 ) )

			if not strip.testing:
				return True

			strip.show( )
			time.sleep( wait_ms / 1000.0 )


def rainbowCycle( strip, wait_ms = 10 ):
	"""
	Draw rainbow that uniformly distributes itself across all pixels.

	**Arguments:**

		:``strip``: `[type]` [description]

	**Keword Arguments:**

		:``wait_ms``: `int` [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	while True:
		for i in range( 0, 256, 4 ):
			for pixel in range( strip.numPixels( ) ):
				strip.setPixelColor( pixel, common.wheel( ( int( pixel * 256 / strip.numPixels( ) ) + i ) & 255 ) )

			if not strip.testing:
				return True

			strip.show( )
			time.sleep( wait_ms / 1000.0 )


def theaterChaseRainbow( strip, wait_ms = 50 ):
	"""
	Rainbow movie theater light style chaser animation.

	**Arguments:**

		:``strip``: `[type]` [description]

	**Keword Arguments:**

		:``wait_ms``: `int` [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	while True:
		for j in range( 0, 256, 4 ):
			for q in range( 3 ):
				for pixel in range( 0, strip.numPixels( ), 3 ):
					color = common.wheel( ( pixel + j ) % 255 )
					strip.setPixelColor( pixel + q, color )		# turn ever 3rd pixel on

				if not strip.testing:
					return True

				strip.show( )
				time.sleep( wait_ms / 1000.0 )

				for pixel in range( 0, strip.numPixels( ), 3 ):
					strip.setPixelColor( pixel + q , const.black )			# turn ever 3rd pixel off


def randColors( strip, wait_ms = 50 ):
	"""
	[description]

	**Arguments:**

		:``strip``: `[type]` [description]

	**Keword Arguments:**

		:``wait_ms``: `int` [description]

	**Returns:**

		:``[type]``: [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	num_pixels		= strip.numPixels( )

	while True:
		for p in range( num_pixels ):
			rgb		= tuple( [ random.randint( 0, 255 ) for x in [ 'r', 'g', 'b' ] ] )
			strip.setPixelColor( p, Color( *rgb ) )

		if not strip.testing:
			return True

		strip.show( )

		time.sleep( wait_ms / 1000.0 )

	return True


################################################################################
## These functions utilize update the whole LED strip through a Pixels object
################################################################################

def pulse( strip, color = const.white, length = 5, wait_ms = 25 ):
	"""
	Scrolls a pulse across the strip

	**Arguments:**

		:``strip``:	`[type]` [description]

	**Keword Arguments:**

		:``color``:		`Color` [description]
		:``length``:	`int` [description]
		:``wait_ms``:	`int` [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	# Creates a pulse as an array of pixel colors
	num_pixels	= strip.numPixels( )
	pixels		= Pixels( [ const.black ] * num_pixels )

	for i in range( length ):
		fade						= 1.0 - ( float( i + 1 ) / length )
		pixels.colors[ i ]	= pixels.colors[ i ].blend( color, bias = fade )

	while True:
		if not strip.testing:
			return True

		pixels.draw( strip )
		time.sleep( wait_ms / 1000.0 )

		pixels.offset( )


def pulses( strip, color = const.white, num = 4, wait_ms = 25 ):
	"""
	Scrolls a pulse across the strip

	**Arguments:**

		:``strip``:    `[type]` [description]
		:``color``:    `[type]` [description]

	**Keword Arguments:**

		:``num``:      `int` [description]
		:``wait_ms``:  `int` [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	num_pixels	= strip.numPixels( )
	pixels		= Pixels( [ const.black ] * num_pixels )

	# Creates multiple, evenly-spaced pulses across the entire strip
	length		= int( num_pixels / num )
	for j in range( 0, num_pixels, length ):
		for i in range( length ):
			fade							= 1.0 - ( float( i ) / length )
			pixels.colors[ j + i ]	= pixels.colors[ j + i ].blend( color, bias = fade )

	while True:
		if not strip.testing:
			return True

		pixels.draw( strip )
		time.sleep( wait_ms / 1000.0 )

		pixels.offset( )


def cylon( strip, color = const.red, length = 10, wait_ms = 50 ):
	"""
	[description]

	**Arguments:**

		:``strip``:	`[type]` [description]

	**Keword Arguments:**

		:``color``:		`Color` Color object representing an rgb color
		:``length``:	`int` [description]
		:``wait_ms``:	`int` [description]

	**Returns:**

		:``[type]``: [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	num_pixels	= strip.numPixels( )
	pixels		= Pixels( [ const.black ] * num_pixels )
	fade			= 1.0 - ( 1.0 / length )
	loop			= common.create_loop( num_pixels )

	while True:
		for j in loop:
			pixels.colors[ j ] = color			# set current pixel to full color

			if not strip.testing:
				return True

			pixels.draw( strip )
			time.sleep( wait_ms / 1000.0 )

			pixels = pixels.blend( const.black, bias = fade )

	return True


def cylon2( strip, color = const.red, length = 10, wait_ms = 50 ):
	"""
	[description]

	**Arguments:**

		:``strip``:		`[type]` [description]
		:``color``:		`[type]` [description]

	**Keword Arguments:**

		:``length``:	`int` [description]
		:``wait_ms``:	`int` [description]

	**Returns:**

		:``[type]``: [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	num_pixels	= strip.numPixels( )
	pixels		= Pixels( [ const.black ] * num_pixels )
	fade			= 1.0 - ( 1.0 / length )

	while True:
		for j in range( num_pixels):
			idx						= num_pixels - j - 1
			pixels.colors[ j ]	= color		# set current pixel to color	
			pixels.colors[ idx ]	= color		# set pixel on opposite side of list

			if not strip.testing:
				return True

			pixels.draw( strip )
			time.sleep( wait_ms / 1000.0 )

			pixels = pixels.blend( const.black, bias = fade )

	return True


def randFade( strip, color1 = Color( 239, 247, 255 ), color2 = const.black,
	rate = 0.05, fade_out = 25, wait_ms = 100
	):
	"""
	[description]

	**Arguments:**

		:``strip``:		`[type]` [description]
		:``color1``:	`[type]` [description]
		:``color2``:	`[type]` [description]

	**Keword Arguments:**

		:``rate``:		`float` [description]
		:``length``:	`int` [description]
		:``wait_ms``:	`int` [description]

	**Returns:**

		:``[type]``: [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	num_pixels  = strip.numPixels( )
	pixels		= Pixels( [ color2 ] * num_pixels )
	bias			= 1.0 - ( 1.0 / fade_out )

	while True:
		for i in range( num_pixels):
			r = random.random( ) 
			if r <= rate:
				pixels.colors[ i ] = color1

		if not strip.testing:
			return True

		pixels.draw( strip )
		time.sleep( wait_ms / 1000.0 )

		pixels = pixels.blend( color2, bias = bias )

	return True


def fire( strip, color1 = const.yellow, color2 = const.red,
	rate = 0.05, fade_out = 25, wait_ms = 100
	):

	randFade( strip, color1 = color1, color2 = color2,
	rate = rate, fade_out = fade_out, wait_ms = wait_ms )

	return true

def softFade( strip, color1 = Color( 0, 63, 255 ), color2 = Color( 255, 127, 255 ), num = 4, width = None,
	fade_in = 90, fade_out = 150, wait_ms = 33.33
	):
	"""
	[description]

	**Arguments:**

		:``strip``:		`[type]` [description]
		:``color1``:	`[type]` [description]
		:``color2``:	`[type]` [description]

	**Keword Arguments:**

		:``num``:		`float` [description]
		:``width``:		`int` [description]
		:``fade_in``:	`int` [description]
		:``fade_out``:	`int` [description]
		:``wait_ms``:	`int` [description]

	**Returns:**

		:``[type]``: [description]

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	num_pixels	= strip.numPixels( )

	if not width:
		width		= num_pixels

	colors1		= Pixels( [ color1 ] * num_pixels )
	colors2		= Pixels( [ color2 ] * num_pixels )
	gradient		= common.gradient( color1, color2, width, mirror = True )
	for i, col in enumerate( gradient ):
		colors2.colors[ i ] = col
	colors2.add( colors1 )

	while True:
		pixels		= Pixels( colors1 )
		colors2.offset( random.randint( 0, num_pixels ) )

		for i in range( fade_in ):
			bias = 1.0 - ( i / fade_in )
			#print( 'fade_in {}'.format( bias ) )
			pixels.colors	= colors1.blend( colors2, bias = bias )

			if not strip.testing:
				return True
			# while strip.paused:
			# 	pass

			pixels.draw( strip )
			time.sleep( wait_ms / 1000.0 )

		for i in range( fade_out ):
			bias = 1.0 - ( i / fade_out )
			#print( 'fade_out {}'.format( bias ) )
			pixels.colors	= colors2.blend( colors1, bias = bias )

			if not strip.testing:
				return True
			# while strip.paused:
			# 	pass

			pixels.draw( strip )
			time.sleep( wait_ms / 1000.0 )

	return True
