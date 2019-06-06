# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ChmFromLidarDialog
                                 A QGIS plugin
 This plugin creates the Canopy Height Model (CHM) from LIDAR data.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-04-29
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Gter srl
        email                : assistenzagis@gter.it
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from qgis.PyQt.QtWidgets import QDialog
#from PyQt5.QtGui import *
#from qgis.gui import QgsMessageBar

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'chm_from_lidar_dialog_base.ui'))


class ChmFromLidarDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ChmFromLidarDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        #self.comboBox_2.layerChanged.connect(self.is_something_selected)
        
    # def accept(self):
        # valid = self.inputCheck()
        # if valid:
            # self.done(1)
            
    # def inputCheck(self):
        # if len(self.unique(fi_ov)) > 1 and len(fi2_ov) > 1:
            # self.textLog.append("loooooooooooooooog")
            # return False
        # return True
        
# if __name__ == "__main__":
    # import sys
    # print('if name')
    # app = QtWidgets.QApplication(sys.argv)
    # ChmFromLidar = QtWidgets.QDialog()
    # ui = ChmFromLidarDialog()
    # ui.setupUi(ChmFromLidar)
    # ChmFromLidar.show()
    # sys.exit(app.exec_())