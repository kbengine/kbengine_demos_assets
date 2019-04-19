# -*- coding: utf-8 -*-
import KBEngine
import SpaceContext
from KBEDebug import * 
import EntityDef as Def
import Types

@Def.interface()
class Teleport:
	def __init__(self):
		pass
		
	@Def.property(flags=Def.CELL_PUBLIC_AND_OWN, persistent=True)
	def spaceUType(self) -> Def.UINT32:
		return None

	@Def.method()
	def teleportSpace(self, spaceUType : Types.ENTITY_UTYPE, position : Types.POSITION3D, direction : Types.DIRECTION3D, context : Def.PYTHON):
		"""
		defined.
		传送到某场景
		"""
		assert self.base != None
		self.lastSpaceUType = self.spaceUType
		
		inputContext = SpaceContext.createContext(self, spaceUType)
		if type(context) == dict:
			inputContext.update(context)

		self.getSpaces().teleportSpace(self.base, spaceUType, position, direction, inputContext)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	@Def.method()
	def onTeleportSpaceCB(self, spaceCellEntityCall : Def.ENTITYCALL, spaceUType : Types.ENTITY_UTYPE, position : Types.POSITION3D, direction : Types.DIRECTION3D):
		"""
		defined.
		baseapp返回teleportSpace的回调
		"""
		DEBUG_MSG("Teleport::onTeleportSpaceCB: %i spaceID=%s, spaceUType=%i, pos=%s, dir=%s." % \
					(self.id, spaceCellEntityCall.id, spaceUType, position, direction))
		
		
		self.getCurrSpaceBase().onLeave(self.id)
		self.teleport(spaceCellEntityCall, position, direction)
	
	def onTeleportSuccess(self, nearbyEntity):
		"""
		KBEngine method.
		"""
		DEBUG_MSG("Teleport::onTeleportSuccess: %s" % (nearbyEntity))
		self.getCurrSpaceBase().onEnter(self.base)
		self.spaceUType = self.getCurrSpace().spaceUType
		
	def onDestroy(self):
		"""
		entity销毁
		"""
		self.getCurrSpaceBase().logoutSpace(self.id)
