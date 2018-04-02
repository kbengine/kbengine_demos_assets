# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Test(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	def onAttached(self, owner):
		"""
		"""
		INFO_MSG("Test::onAttached(): owner=%i" % (owner.id))
		self.owner.client.component1.helloCB(111)

	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("Test::onDetached(): owner=%i" % (owner.id))

	def hello(self, x, iii):
		print("+++++++++++++++++++++++hello", x, iii)
		self.allClients.helloCB(7770)