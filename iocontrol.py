import sys
import time

import numpy as np

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import ui_ioscan

from mrq.mrhe import Mrhe

class IoControl( QDialog, ui_ioscan.Ui_Dialog ):  
    def __init__( self, parent=None  ):
        super( IoControl, self ).__init__( parent )
        self.setupUi( self )

        self.hub = Mrhe("hub1")

        self.hub.configPort( 1, "out")
        self.hub.configPort( 2, "out")
        self.hub.configPort( 3, "out")
        self.hub.configPort( 4, "out")

        self.hub.configPort( 5, "in")
        self.hub.configPort( 6, "in")

        # init
        self.hub.writePort( 1, 1 )
        self.hub.writePort( 2, 1 )
        self.hub.writePort( 3, 1 )
        self.hub.writePort( 4, 1 )

        self.chkX1.setChecked( True )
        self.chkX2.setChecked( True )
        self.chkX3.setChecked( True )
        self.chkX4.setChecked( True )

        self.tick_timer = QTimer()
        self.tick_timer.timeout.connect( self.onTimeout )

        self.chkX1.clicked.connect( self.onClick1 )
        self.chkX2.clicked.connect( self.onClick2 )
        self.chkX3.clicked.connect( self.onClick3 )
        self.chkX4.clicked.connect( self.onClick4 )

        self.tick_timer.start( 500 )

    def onTimeout( self ):
        v = self.hub.readPort( 5 )
        self.radY1.setChecked( v > 0 )

        v = self.hub.readPort( 6 )
        self.radY2.setChecked( v > 0 )
        # print("time")
        pass 

    def onClick1( self, b ):
        self.hub.writePort( 1, b )
        pass 

    def onClick2( self, b ):
        self.hub.writePort( 2, b )
        pass 

    def onClick3( self, b ):
        self.hub.writePort( 3, b )
        pass 

    def onClick4( self, b ):
        self.hub.writePort( 4, b )
        pass   


# class HelloForm( QWidget, ui_helloworld.Ui_Form ):
#     def __init__( self, parent=None ):
#         super( HelloForm, self ).__init__( parent )
#         self.setupUi( self )

#         self.btnHello.clicked.connect( self.onClick )        

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    
    dlg = IoControl()

    dlg.show()
    qapp.exec_()