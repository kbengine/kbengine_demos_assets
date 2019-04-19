# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import EntityDef as Def

@Def.component()
class Test(KBEngine.EntityComponent):
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
		return 1002

	def onAttached(self, owner):
		"""
		"""
		INFO_MSG("Test::onAttached(): owner=%i" % (owner.id))
		self.owner.client.component1.helloCB(111)

	def onDetached(self, owner):
		"""
		"""
		INFO_MSG("Test::onDetached(): owner=%i" % (owner.id))

	@Def.method(exposed=True)
	def hello(self, x : Def.CALLER_ID, iii : Def.INT32):
		print("+++++++++++++++++++++++hello", x, iii)
		self.allClients.helloCB(7770)

	@Def.clientmethod()
	def helloCB(self, v : Def.INT32):
		pass
