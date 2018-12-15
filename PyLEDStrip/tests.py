#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Series of pattern tests

**Author:**

	Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
"""

from .pixels import Pixels
from .color import Color



def test_patterns( strip ):
	"""
	[description]

	**Arguments:**

		:``strip``: `[type]` [description]

	**Keword Arguments:**

		None

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	# print ('Color wipe animations.')
	# pixels.colorWipe(strip, Color( 255, 0, 0 ) )  # Red wipe
	# pixels.colorWipe(strip, Color( 0, 255, 0 ) )  # Blue wipe
	# pixels.colorWipe(strip, Color( 0, 0, 255 ) )  # Green wipe

	# print ('Theater chase animations.')
	# pixels.theaterChase(strip, Color( 255, 255, 240 ) )  # White theater chase
	# pixels.theaterChase(strip, Color( 255, 0, 0 ) )  # Red theater chase
	# pixels.theaterChase(strip, Color( 48, 64, 255 ) )  # Blue theater chase

	print ('Rainbow animations.')
	# pixels.rainbow( strip )
	# pixels.rainbowCycle( strip )
	# pixels.theaterChaseRainbow( strip )

	# print( 'Pulse.')
	# strips.pulse( strip, Color( 255, 0, 0 ), length = 10 )
	# strips.pulse( strip, Color( 0, 255, 0 ), length = 10 )
	# strips.pulse( strip, Color( 0, 0, 255 ), length = 10 )

	# print( 'cylonChaser.')
	# strips.cylonChaser( strip, Color( 255, 0, 0 ), length = 5, wait_ms = 5 )
	# strips.cylonChaser( strip, Color( 255, 0, 0 ), length = 20, wait_ms = 20 )

	# print( 'cylonDoubleChaser.')
	# strips.cylonDoubleChaser( strip, Color( 255, 0, 0 ), length = 5, wait_ms = 5 )
	# strips.cylonDoubleChaser( strip, Color( 255, 0, 0 ), length = 20, wait_ms = 20 )

	# print( 'randColors.')
	# pixels.randColors( strip )

	# print( 'randFade.')
	# strips.randFade( strip, Color( 240, 250, 255 ) )

	print( 'softFade' )
	strips.softFade( strip, Color( 0, 64, 255 ), Color( 255, 64, 255 ) )
	
	print( 'done' )
