# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Test(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)
		print("+++++++++++++++++++++++name=%s, bb=%i" % (self.name, self.bb))

		if hasattr(self.owner, "cellData"):
			print("+++++++++++++++++++++++cellData=%s" % self.owner.cellData[self.name])

	def onAttached(self, owner):
		"""
		"""
		INFO_MSG("Test::onAttached(): owner=%i" % (owner.id))
		
	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("Test::onDetached(): owner=%i" % (owner.id))

	def say(self, iii):
		print("+++++++++++++++++++++++say", iii)
		if self.owner.cell is not None:
			self.cell.hello(33321)

	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("Test[%i]::onClientEnabled:entities enable." % (self.ownerID))
		self.tid = self.addTimer(10, 0, 123)

	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Test[%i].onClientDeath:" % self.ownerID)

		if self.tid > 0:
			self.delTimer(self.tid)

	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.name, self.ownerID, tid, userArg))

		if self.tid == tid:
			self.tid = 0