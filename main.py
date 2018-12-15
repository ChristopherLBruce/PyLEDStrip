#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
[description]

**Author:**

	Chris Bruce, chris.bruce@dsvolition.com, 12/3/2018
"""

import sys
from PyQt5.QtWidgets import QApplication

from . import gui


def run( ):
	app = QApplication( sys.argv )

	led_strip = gui.create_gui( app )

	sys.exit( app.exec_( ) )


if __name__ == '__main__':
	run( )
