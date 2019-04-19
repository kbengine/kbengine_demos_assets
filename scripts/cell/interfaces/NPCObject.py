# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.GameObject import GameObject
import EntityDef as Def
import Types

@Def.interface()
class NPCObject(GameObject):
	"""
	所有非角色的实体接口类
	"""
	def __init__(self):
		GameObject.__init__(self)

	@Def.property(flags=Def.CELL_PRIVATE)
	def spawnID(self) -> Types.ENTITY_ID:
		pass

	@Def.property(flags=Def.CELL_PRIVATE)
	def spawnPos(self) -> Def.VECTOR3:
		return (0,0,0)

	@Def.property(flags=Def.CELL_PRIVATE)
	def entityNO(self) -> Types.ENTITY_NO:
		return 0

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onDestroy(self):
		"""
		entity销毁
		"""
		if self.spawnID > 0:
			spawner = KBEngine.entities.get(self.spawnID)
			if spawner:
				spawner.onEntityDestroyed(self.entityNO)
				
