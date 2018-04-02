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

		if self.owner.base is None:
			return

		self.owner.base.component1.say(000)

	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("Test::onDetached(): owner=%i" % (owner.id))

	def helloCB(self, id):
		print("++++++++++++", id)