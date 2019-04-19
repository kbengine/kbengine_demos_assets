# -*- coding: utf-8 -*-
import KBEngine
import skills
import GlobalConst
import GlobalDefine
from KBEDebug import * 
import EntityDef as Def
import Types

@Def.interface()
class SkillBox:
	def __init__(self):
		# 如果玩家没有学习技能，默认添加这些技能
		if len(self.skills) == 0:
			self.skills.append(1)
			self.skills.append(1000101)
			self.skills.append(2000101)
			self.skills.append(3000101)
			self.skills.append(4000101)
			self.skills.append(5000101)
			self.skills.append(6000101)

	@Def.property(flags=Def.CELL_PRIVATE, persistent=True)
	def skills(self) -> Types.SKILLID_LIST:
		pass

	def hasSkill(self, skillID):
		"""
		"""
		return skillID in self.skills

	#--------------------------------------------------------------------------------------------
	#                              defined
	#--------------------------------------------------------------------------------------------
	@Def.method(exposed=True)
	def requestPull(self, exposed : Def.CALLER_ID):
		"""
		exposed
		"""
		if self.id != exposed:
			return
		
		DEBUG_MSG("SkillBox::requestPull: %i skills=%i" % (self.id, len(self.skills)))
		for skillID in self.skills:
			self.client.onAddSkill(skillID)
	
	@Def.method()
	def addSkill(self, skillID : Types.SKILLID):
		"""
		defined method.
		"""
		self.skills.append(skillID)

	@Def.method()
	def removeSkill(self, skillID : Types.SKILLID):
		"""
		defined method.
		"""
		self.skills.remove(skillID)
	
	@Def.method(exposed=True)
	def useTargetSkill(self, srcEntityID : Def.CALLER_ID, skillID : Types.SKILLID, targetID : Types.ENTITY_ID):
		"""
		exposed.
		对一个目标entity施放一个技能
		"""
		if srcEntityID != self.id:
			return
		
		self.spellTarget(skillID, targetID)

	@Def.clientmethod()
	def onAddSkill(self, skillID : Types.SKILLID):
		pass

	@Def.clientmethod()
	def onRemoveSkill(self, skillID : Types.SKILLID):
		pass
	