# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impact_functions_doc_base.ui'
#
# Created: Tue Jun 11 14:31:25 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ImpactFunctionsDocBase(object):
    def setupUi(self, ImpactFunctionsDocBase):
        ImpactFunctionsDocBase.setObjectName(_fromUtf8("ImpactFunctionsDocBase"))
        ImpactFunctionsDocBase.resize(821, 733)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/inasafe/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ImpactFunctionsDocBase.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(ImpactFunctionsDocBase)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.myButtonBox = QtGui.QDialogButtonBox(ImpactFunctionsDocBase)
        self.myButtonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.myButtonBox.setAutoFillBackground(False)
        self.myButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.myButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Reset)
        self.myButtonBox.setCenterButtons(False)
        self.myButtonBox.setObjectName(_fromUtf8("myButtonBox"))
        self.gridLayout.addWidget(self.myButtonBox, 1, 1, 1, 1)
        self.gridLayoutMain = QtGui.QGridLayout()
        self.gridLayoutMain.setHorizontalSpacing(0)
        self.gridLayoutMain.setObjectName(_fromUtf8("gridLayoutMain"))
        self.label_title = QtGui.QLabel(ImpactFunctionsDocBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.gridLayoutMain.addWidget(self.label_title, 1, 0, 1, 1)
        self.label_id = QtGui.QLabel(ImpactFunctionsDocBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_id.sizePolicy().hasHeightForWidth())
        self.label_id.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_id.setFont(font)
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.gridLayoutMain.addWidget(self.label_id, 1, 1, 1, 1)
        self.label_subcategory = QtGui.QLabel(ImpactFunctionsDocBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_subcategory.sizePolicy().hasHeightForWidth())
        self.label_subcategory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_subcategory.setFont(font)
        self.label_subcategory.setObjectName(_fromUtf8("label_subcategory"))
        self.gridLayoutMain.addWidget(self.label_subcategory, 1, 3, 1, 1)
        self.label_category = QtGui.QLabel(ImpactFunctionsDocBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_category.sizePolicy().hasHeightForWidth())
        self.label_category.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_category.setFont(font)
        self.label_category.setObjectName(_fromUtf8("label_category"))
        self.gridLayoutMain.addWidget(self.label_category, 1, 2, 1, 1)
        self.label_layertype = QtGui.QLabel(ImpactFunctionsDocBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_layertype.sizePolicy().hasHeightForWidth())
        self.label_layertype.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_layertype.setFont(font)
        self.label_layertype.setObjectName(_fromUtf8("label_layertype"))
        self.gridLayoutMain.addWidget(self.label_layertype, 1, 4, 1, 1)
        self.comboBox_id = QtGui.QComboBox(ImpactFunctionsDocBase)
        self.comboBox_id.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_id.setObjectName(_fromUtf8("comboBox_id"))
        self.gridLayoutMain.addWidget(self.comboBox_id, 3, 1, 1, 1)
        self.comboBox_title = QtGui.QComboBox(ImpactFunctionsDocBase)
        self.comboBox_title.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_title.setMinimumContentsLength(0)
        self.comboBox_title.setObjectName(_fromUtf8("comboBox_title"))
        self.gridLayoutMain.addWidget(self.comboBox_title, 3, 0, 1, 1)
        self.comboBox_category = QtGui.QComboBox(ImpactFunctionsDocBase)
        self.comboBox_category.setObjectName(_fromUtf8("comboBox_category"))
        self.gridLayoutMain.addWidget(self.comboBox_category, 3, 2, 1, 1)
        self.label_unit = QtGui.QLabel(ImpactFunctionsDocBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_unit.sizePolicy().hasHeightForWidth())
        self.label_unit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_unit.setFont(font)
        self.label_unit.setObjectName(_fromUtf8("label_unit"))
        self.gridLayoutMain.addWidget(self.label_unit, 1, 6, 1, 1)
        self.label_datatype = QtGui.QLabel(ImpactFunctionsDocBase)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_datatype.sizePolicy().hasHeightForWidth())
        self.label_datatype.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_datatype.setFont(font)
        self.label_datatype.setObjectName(_fromUtf8("label_datatype"))
        self.gridLayoutMain.addWidget(self.label_datatype, 1, 5, 1, 1)
        self.comboBox_subcategory = QtGui.QComboBox(ImpactFunctionsDocBase)
        self.comboBox_subcategory.setObjectName(_fromUtf8("comboBox_subcategory"))
        self.gridLayoutMain.addWidget(self.comboBox_subcategory, 3, 3, 1, 1)
        self.comboBox_layertype = QtGui.QComboBox(ImpactFunctionsDocBase)
        self.comboBox_layertype.setObjectName(_fromUtf8("comboBox_layertype"))
        self.gridLayoutMain.addWidget(self.comboBox_layertype, 3, 4, 1, 1)
        self.comboBox_datatype = QtGui.QComboBox(ImpactFunctionsDocBase)
        self.comboBox_datatype.setObjectName(_fromUtf8("comboBox_datatype"))
        self.gridLayoutMain.addWidget(self.comboBox_datatype, 3, 5, 1, 1)
        self.comboBox_unit = QtGui.QComboBox(ImpactFunctionsDocBase)
        self.comboBox_unit.setObjectName(_fromUtf8("comboBox_unit"))
        self.gridLayoutMain.addWidget(self.comboBox_unit, 3, 6, 1, 1)
        self.webView = QtWebKit.QWebView(ImpactFunctionsDocBase)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.gridLayoutMain.addWidget(self.webView, 4, 0, 1, 7)
        self.gridLayout.addLayout(self.gridLayoutMain, 0, 1, 1, 1)

        self.retranslateUi(ImpactFunctionsDocBase)
        QtCore.QObject.connect(self.myButtonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ImpactFunctionsDocBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ImpactFunctionsDocBase)

    def retranslateUi(self, ImpactFunctionsDocBase):
        ImpactFunctionsDocBase.setWindowTitle(_translate("ImpactFunctionsDocBase", "InaSAFE Impact Functions", None))
        self.label_title.setText(_translate("ImpactFunctionsDocBase", "Title", None))
        self.label_id.setText(_translate("ImpactFunctionsDocBase", "ID", None))
        self.label_subcategory.setText(_translate("ImpactFunctionsDocBase", "Subcategory", None))
        self.label_category.setText(_translate("ImpactFunctionsDocBase", "Category", None))
        self.label_layertype.setText(_translate("ImpactFunctionsDocBase", "Layer Type", None))
        self.label_unit.setText(_translate("ImpactFunctionsDocBase", "Unit", None))
        self.label_datatype.setText(_translate("ImpactFunctionsDocBase", "Data Type", None))

from PyQt4 import QtWebKit
import resources_rc
