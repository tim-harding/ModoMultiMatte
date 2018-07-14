#!/usr/bin/env python

import lx
import lxifc
import lxu.command
import modo
from multimatte_interface import Ui_Form
from PySide import QtGui, QtCore


def main():
	lx.bless(GuiCommand, 'mm.gui')


class Interface(QtGui.QWidget, Ui_Form):
	def __init__(self, parent=None):
		super(Interface, self).__init__(parent)
		self.setupUi(self)


class Gui(lxifc.CustomView):

	def customview_Init(self, pane):
		if pane is None:
			return False
		custPane = lx.object.CustomPane(pane)
		if not custPane.test():
			return False
		parent = custPane.GetParent()
		widget = lx.getQWidget(parent)
		if widget is not None:

			layout = QtGui.QVBoxLayout()
			self.form = Interface()
			layout.addWidget(self.form)
			widget.setLayout(layout)

			self.form.renderButton.clicked.connect(self.render)
			self.form.randButton.clicked.connect(self.randomize)
			self.form.mmValButton.clicked.connect(self.setVal)

			return True
		return False

	def render(self):
		anim = int(bool(self.form.animCheckBox.checkState()))
		ptag = int(bool(self.form.matRadio.isChecked()))
		lx.eval('mm.render %s %s' % (anim, ptag))

	def randomize(self):
		lx.eval('mm.rand')

	def setVal(self):
		lx.eval('mm.setval %s' % int(str(self.form.mmValBox.value())))


class GuiCommand(lxu.command.BasicCommand):
	def __init__(self):
		lxu.command.BasicCommand.__init__(self)

	def cmd_Flags(self):
		return lx.symbol.fCMD_MODEL | lx.symbol.fCMD_UNDO

	def basic_Enable(self, msg):
		return True

	def basic_Execute(self, msg, flags):
		try:
			lx.bless(Gui, 'Multimatte')
		except:
			pass
		lx.eval('layout.create width:300 height:300 style:palette')
		lx.eval('customview.view Multimatte')


main()
