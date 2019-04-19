# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 
import dialogmgr
import EntityDef as Def
import Types

@Def.interface()
class Dialog:
	"""
	与NPC对话模块，客户端通过调用dialog来驱动对话协议
	"""
	def __init__(self):
		pass

	#--------------------------------------------------------------------------------------------
	#                              defined
	#--------------------------------------------------------------------------------------------
	@Def.method(exposed=True, utype=11003)
	def dialog(self, srcEntityID : Def.CALLER_ID, targetID : Types.ENTITY_ID, dialogID : Def.UINT32):
		"""
		exposed.
		对一个目标entity施放一个技能
		"""
		if srcEntityID != self.id:
			return
			
		if not KBEngine.entities.has_key(targetID):
			DEBUG_MSG("Dialog::dialog: %i not found targetID:%i" % (self.id, dialogID))
			return
			
		dialogmgr.onGossip(dialogID, self, KBEngine.entities[targetID])

	@Def.clientmethod(utype=10101)
	def dialog_addOption(self, dialogType : Def.UINT8, dialogKey : Def.UINT32, title : Def.UNICODE, extra : Def.INT32):
		"""
		defined method.
		简单的在服务器声明客户端接口
		"""
		pass

	@Def.clientmethod(utype=10102)
	def dialog_setText(self, body : Def.UNICODE, isPlayer : Types.BOOL, headID : Def.UINT32, sayname : Def.UNICODE):
		"""
		defined method.
		"""
		pass
	
	@Def.clientmethod(utype=10104)
	def dialog_close(self):
		"""
		defined method.
		"""
		pass


