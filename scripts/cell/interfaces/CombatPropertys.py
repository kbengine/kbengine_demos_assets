# -*- coding: utf-8 -*-
import KBEngine
import GlobalDefine
from KBEDebug import * 
import EntityDef as Def
import Types

@Def.interface()
class CombatPropertys:
	"""
	所有关于战斗的属性
	完善的话可以根据策划excel表来直接生成这个模块
	"""
	def __init__(self):
		self.HP_Max = 100
		self.MP_Max = 100
		
		# 非死亡状态才需要补满
		if not self.isState(GlobalDefine.ENTITY_STATE_DEAD) and self.HP == 0 and self.MP == 0:
			self.fullPower()
	
	@Def.property(flags=Def.ALL_CLIENTS, utype=47001, persistent=True)
	def HP(self) -> Types.HP:
		return 0

	@Def.property(flags=Def.ALL_CLIENTS, utype=47002, persistent=True)
	def HP_Max(self) -> Types.HP:
		return 0

	@Def.property(flags=Def.ALL_CLIENTS, utype=47003, persistent=True)
	def MP(self) -> Types.MP:
		return 0

	@Def.property(flags=Def.ALL_CLIENTS, utype=47004, persistent=True)
	def MP_Max(self) -> Types.MP:
		return 0

	def fullPower(self):
		"""
		"""
		self.setHP(self.HP_Max)
		self.setMP(self.MP_Max)
		
	@Def.method()
	def addHP(self, val : Types.HP):
		"""
		defined.
		"""
		v = self.HP + int(val)
		if v < 0:
			v = 0
			
		if self.HP == v:
			return
			
		self.HP = v

	@Def.method()	
	def addMP(self, val : Types.MP):
		"""
		defined.
		"""
		v = self.MP + int(val)
		if v < 0:
			v = 0
			
		if self.MP == v:
			return
			
		self.MP = v
	
	@Def.method()
	def setHP(self, hp : Types.HP):
		"""
		defined
		"""
		hp = int(hp)
		if hp < 0:
			hp = 0
		
		if self.HP == hp:
			return
			
		self.HP = hp

	@Def.method()
	def setMP(self, mp : Types.MP):
		"""
		defined
		"""
		hp = int(mp)
		if mp < 0:
			mp = 0

		if self.MP == mp:
			return
			
		self.MP = mp

	@Def.method()
	def setHPMax(self, hpmax : Types.HP):
		"""
		defined
		"""
		hpmax = int(hpmax)
		self.HP_Max = hpmax
	
	@Def.method()
	def setMPMax(self, mpmax : Types.MP):
		"""
		defined
		"""
		mpmax = int(mpmax)
		self.MP_Max = mpmax
		

