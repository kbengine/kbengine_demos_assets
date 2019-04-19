# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import EntityDef as Def

@Def.component()
class TestNoBase(KBEngine.EntityComponent):
	def __init__(self):
		KBEngine.EntityComponent.__init__(self)

	@Def.property(flags=Def.ALL_CLIENTS, persistent=True)
	def state(self) -> Def.INT32:
		return 100

	@Def.property(flags=Def.CELL_PUBLIC_AND_OWN, persistent=True)
	def own(self) -> Def.INT32:
		return 1001

	@Def.property(flags=Def.CELL_PUBLIC)
	def cc(self) -> Def.INT32:
		return 1001

	def onAttached(self, owner):
		"""
		"""
		INFO_MSG("TestNoBase::onAttached(): owner=%i" % (owner.id))
		self.owner.client.component3.helloCB(888)

	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("TestNoBase::onDetached(): owner=%i" % (owner.id))

	@Def.method(exposed=True)
	def hello(self, x : Def.CALLER_ID, iii : Def.INT32):
		print("+++++++++++++++++++++++TestNoBase hello", x, iii)

	@Def.clientmethod()
	def helloCB(self, v : Def.INT32):
		pass

