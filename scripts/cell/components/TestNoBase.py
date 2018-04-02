# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class TestNoBase(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		"""
		INFO_MSG("TestNoBase::onAttached(): owner=%i" % (owner.id))
		self.owner.client.component3.helloCB(888)

	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("TestNoBase::onDetached(): owner=%i" % (owner.id))

	def hello(self, x, iii):
		print("+++++++++++++++++++++++TestNoBase hello", x, iii)
