#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
[description]

**Author:**

	Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
"""

from os import name, system
import sys
from importlib import reload

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout		#, QSizePolicy
from PyQt5.QtWidgets import QWidget, QComboBox, QFrame, QPushButton, QSpinBox, QLabel, QDesktopWidget
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QColor

from .color import Color
from .pixels import Pixels
from . import const, common, main, patterns
#from . import tests



tests = {
	'Wipe'					: patterns.colorWipe,
	'Rainbow'				: patterns.rainbow,
	'Theater'				: patterns.theaterChase,
	'Rainbow Chase'		: patterns.theaterChaseRainbow,
	'Pulse'					: patterns.pulse,
	'Pulse2'					: patterns.pulses,
	'Rainbow2'				: patterns.rainbowCycle,
	'Cylon'					: patterns.cylon,
	'Cylon2'					: patterns.cylon2,
	'Random'					: patterns.randColors,
	'Random Fade'			: patterns.randFade,
	'Soft Fade'				: patterns.softFade,
	'fire'					: patterns.fire,
}


class ledStrip( QWidget ):
	"""
	[description]

	**Arguments:**

		None

	**Keword Arguments:**

		None

	**Author:**

		Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
	"""

	TITLE				= "LED Strip Simluation"
	VERSION			= 1.0
	SIZE				= [ 300, 400 ]

	LED_MIN			= 8
	LED_MAX			= 256
	LED_NUM			= 32

	LED_SIZE_MIN	= 8
	LED_SIZE_MAX	= 64

	STRIP_COLOR		= const.grey # default RGB value for the strip
	LED_COLOR		= Color( 12, 12, 12 ) # default RGB value for LED pixel

	#STYLE_SHEET			= "QWidget{ background-color: rgb{} };".format( str( STRIP_COLOR ) )
	STYLE_SHEET		= "QWidget{ background-color:white};"



	def __init__( self, app ):
		super( ledStrip, self ).__init__( )

		self.app				= app

		self.leds			= [ ]		# array of LED pixels
		self.led_size		= 32		# size of each LED pixel
		self.led_space		= 16		# size of space between each LED pixel

		self.paused				= False
		self.testing			= False

		self._init_gui( )


	def _init_gui( self ):
		"""
		[description]

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		self.setWindowTitle( '{} - ver. {}'.format( self.TITLE, self.VERSION ) )
		self.main_layout = QVBoxLayout( )
		self.main_layout.setSpacing( self.led_space )
		self.setLayout( self.main_layout )

		self.setAutoFillBackground( True )
		self._set_strip_color( )

		# size_policy = QSizePolicy( )
		# size_policy.setHorizontalPolicy( QSizePolicy.Minimum )
		# self.setSizePolicy( size_policy )

		self.main_layout.addWidget( self._create_strip( ) )
		self.main_layout.addWidget( self._create_controls( ) )

		self._update_gui( )


	def _create_controls( self ):
		"""
		[description]

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		widget	= QWidget( )		#QGroupBox( 'Settings:' )
		layout	= QHBoxLayout( )
		widget.setLayout( layout )

		label_num	= QLabel( 'LEDs:' )
		spin_num		= QSpinBox( )
		spin_num.setRange( self.LED_MIN, self.LED_MAX )
		spin_num.setFixedWidth( 64 )
		spin_num.setValue( self.LED_NUM )
		spin_num.valueChanged.connect( self._on_spin_num_changed )

		label_size	= QLabel( 'Size:' )
		spin_size	= QSpinBox( )
		spin_size.setRange( self.LED_SIZE_MIN, self.LED_SIZE_MAX )
		spin_size.setFixedWidth( 64 )
		spin_size.setValue( self.led_size )
		spin_size.valueChanged.connect( self._on_spin_size_changed )

		label_space	= QLabel( 'Space:' )
		spin_space	= QSpinBox( )
		spin_space.setRange( 0, 256 )
		spin_space.setFixedWidth( 64 )
		spin_space.setValue( self.led_space )
		spin_space.valueChanged.connect( self._on_spin_space_changed )

		self.tests	= QComboBox( )
		for test in sorted( tests.keys( ) ):
			self.tests.addItem( test )
		# self.tests.setCurrentText( 'Soft Fade' )

		btn_start	= QPushButton( 'Start' )
		btn_start.pressed.connect( self._on_btn_start_pressed )

		btn_pause	= QPushButton( 'Pause' )
		btn_pause.pressed.connect( self._on_btn_pause_pressed )

		btn_stop		= QPushButton( 'Stop' )
		btn_stop.pressed.connect( self._on_btn_stop_pressed )

		btn_query		= QPushButton( '??' )
		btn_query.pressed.connect( self._on_btn_query_pressed )

		layout.addStretch( )
		layout.addWidget( label_num )
		layout.addWidget( spin_num )
		layout.addWidget( label_size )
		layout.addWidget( spin_size )
		layout.addWidget( label_space )
		layout.addWidget( spin_space )
		layout.addWidget( self.tests )
		layout.addWidget( btn_start )
		layout.addWidget( btn_pause )
		layout.addWidget( btn_stop )
		layout.addWidget( btn_query )
		layout.addStretch( )

		return widget


	def _create_led( self, color ):
		"""
		[description]

		**Arguments:**

			:``color``: `[type]` [description]

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		led = QFrame( )
		led.setFixedSize( QSize( self.led_size, self.led_size ) )
		led.setFrameShape( QFrame.Box )
		led.setFrameShadow( QFrame.Raised )
		led.setLineWidth( 0 )
		led.setMidLineWidth ( self.led_size / 8 )

		led.setStyleSheet( "background-color: rgb{}".format( color ) )

		return led


	def _create_strip( self ):
		"""
		[description]

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		self.strip_widget		= QWidget( )
		self.strip_layout		= QHBoxLayout( )
		self.strip_layout.setSpacing( self.led_space )
		self.strip_widget.setLayout( self.strip_layout )

		for i in range( self.LED_NUM ):
			led = self._create_led( self.LED_COLOR )
			self.leds.append( led )
			self.strip_layout.addWidget( led )

		return self.strip_widget


	def _set_strip_color( self, color = STRIP_COLOR ):
		"""
		Change the color of the strip

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		p = self.palette( )
		p.setColor( self.backgroundRole( ), QColor( *color ) )
		self.setPalette( p )

		return color


	def _update_size( self ):
		self.strip_widget.setFixedSize( self.strip_layout.sizeHint( ) )
		self.setFixedSize( self.main_layout.sizeHint( ) )

		self._center( )

		return True


	def _center( self ):
		qtRectangle		= self.frameGeometry( )
		centerPoint		= QDesktopWidget( ).availableGeometry( ).center( )
		qtRectangle.moveCenter( centerPoint )
		self.move( qtRectangle.topLeft( ) )

		return qtRectangle.topLeft( )


	def _update_gui( self ):
		self._update_size( )
		self._center( )

		return True



	def _on_spin_num_changed( self, value ):
		"""
		Change the color of the strip

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		num_leds = self.get_num_leds( )

		if value > num_leds :
			for _ in range( value - num_leds ):
				led = self._create_led( self.LED_COLOR )
				self.leds.append( led )
				self.strip_layout.addWidget( led )
		elif value < len( self.leds ):
			for _ in range( num_leds - value ):
				led = self.leds[ -1 ]
				self.strip_layout.removeWidget( led )
				self.leds.pop( )
				led.deleteLater( )

		self._update_gui( )


	def _on_spin_size_changed( self, value ):
		"""
		Change the color of the strip

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		for led in self.leds:
			self.led_size = value
			led.setFixedSize( QSize( self.led_size, self.led_size ) )
			led.setMidLineWidth ( self.led_size / 8 )

		self._update_gui( )


	def _on_spin_space_changed( self, value ):
		"""
		Change the color of the strip

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""
		
		self.led_space = value
		self.strip_layout.setSpacing( self.led_space )

		self._update_gui( )


	def _on_btn_start_pressed( self ):
		self.testing	= True
		sel_test			= self.tests.currentText( )
		test_func		= tests[ sel_test ]

		return test_func( self )


	def _on_btn_pause_pressed( self ):
		self.paused		= not self.paused	

		return True


	def _on_btn_stop_pressed( self ):
		self.testing	= False

		return True


	def _on_btn_query_pressed( self ):
		print( 'self.leds( {} ) :\n'.format( type( self.leds ) ) )

		for i, p in enumerate( self.leds ):
			print( '[ {} ] : {}'.format( i, p.styleSheet( ) ) )

		print( 'self.testing : {} '.format( self.testing ) )


	def get_num_leds( self ):
		"""
		[description]

		**Arguments:**

			None

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		return len( self.leds )


	def set_led_color( self, i, color ):
		"""
		[description]

		**Arguments:**

			:``i``: `[type]` [description]
			:``color``: `[type]` [description]

		**Keword Arguments:**

			None

		**Returns:**

			:``[type]``: [description]

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		if color == 0:
			color = self.LED_COLOR

		if i > ( self.get_num_leds( ) - 1 ):
			i -= self.get_num_leds( )

		led = self.leds[ i ]
		led.setStyleSheet( "background-color: rgb{}".format( str( color ) ) )

		return True


	def show( self ):
		"""
		Extends QWidget's .show( ) so it can function similuarly as NeoPixel calls

		**Author:**

			Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
		"""

		super( ledStrip, self ).show( )

		# extended functionality
		self.app.processEvents( )


	def closeEvent( self, event ):
		print( "Closing" )
		self._on_btn_stop_pressed( )
		self.destroy( )
		self.app.exit( )



def create_gui( app ):
	led_strip	= ledStrip( app )
	led_strip.show( )

	return led_strip



if __name__ == '__main__':
	app = QApplication( sys.argv )
	os.system( 'cls' if os.name == 'nt' else 'clear' )

	led_strip	= ledStrip( )
	led_strip.show( )

	sys.exit( app.exec_( ) )
