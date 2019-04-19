# -*- coding: utf-8 -*-
import KBEngine
import Functor
import d_spaces
import GlobalDefine
import Watcher
from KBEDebug import *
from SpaceAlloc import *
from interfaces.GameObject import GameObject
import EntityDef as Def
import Types

@Def.entity()
class Spaces(KBEngine.Entity, GameObject):
	"""
	这是一个脚本层封装的空间管理器
	KBEngine的space是一个抽象空间的概念，一个空间可以被脚本层视为游戏场景、游戏房间、甚至是一个宇宙。
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)
		
		# 初始化空间分配器
		self.initAlloc()
		
		# 向全局共享数据中注册这个管理器的entityCall以便在所有逻辑进程中可以方便的访问
		KBEngine.globalData["Spaces"] = self
	
	def initAlloc(self):
		# 注册一个定时器，在这个定时器中我们每个周期都创建出一些NPC，直到创建完所有
		self._spaceAllocs = {}
		self.addTimer(3, 1, GlobalDefine.TIMER_TYPE_CREATE_SPACES)
		
		self._tmpDatas = list(d_spaces.datas.keys())
		for utype in self._tmpDatas:
			spaceData = d_spaces.datas.get(utype)
			if spaceData["entityType"] == "SpaceDuplicate":
				self._spaceAllocs[utype] = SpaceAllocDuplicate(utype)
			else:
				self._spaceAllocs[utype] = SpaceAlloc(utype)
	
	def getSpaceAllocs(self):
		return self._spaceAllocs
		
	def createSpaceOnTimer(self, tid):
		"""
		创建space
		"""
		if len(self._tmpDatas) > 0:
			spaceUType = self._tmpDatas.pop(0)
			self._spaceAllocs[spaceUType].init()
			
		if len(self._tmpDatas) <= 0:
			del self._tmpDatas
			self.delTimer(tid)
	
	@Def.method()
	def loginToSpace(self, avatarEntity : Def.ENTITYCALL, spaceUType : Types.ENTITY_UTYPE, context : Def.PYTHON):
		"""
		defined method.
		某个玩家请求登陆到某个space中
		"""
		self._spaceAllocs[spaceUType].loginToSpace(avatarEntity, context)
	
	@Def.method()
	def logoutSpace(self, avatarID : Types.ENTITY_ID, spaceKey : Types.SPACE_ID):
		"""
		defined method.
		某个玩家请求登出这个space
		"""
		for spaceAlloc in self._spaceAllocs.values():
			space = spaceAlloc.getSpaces().get(spaceKey)
			if space:
				space.logoutSpace(avatarID)

	@Def.method()		
	def teleportSpace(self, entityCall : Def.ENTITYCALL, spaceUType : Types.ENTITY_UTYPE, position : Types.POSITION3D, direction : Types.POSITION3D, context : Def.PYTHON):
		"""
		defined method.
		请求进入某个space中
		"""
		self._spaceAllocs[spaceUType].teleportSpace(entityCall, position, direction, context)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		if GlobalDefine.TIMER_TYPE_CREATE_SPACES == userArg:
			self.createSpaceOnTimer(tid)
		
		GameObject.onTimer(self, tid, userArg)
		
	@Def.method()
	def onSpaceLoseCell(self, spaceUType : Types.ENTITY_UTYPE, spaceKey : Types.DBID):
		"""
		defined method.
		space的cell创建好了
		"""
		self._spaceAllocs[spaceUType].onSpaceLoseCell(spaceKey)
		
	@Def.method()
	def onSpaceGetCell(self, spaceUType : Types.ENTITY_UTYPE, spaceEntityCall : Def.ENTITYCALL, spaceKey : Types.DBID):
		"""
		defined method.
		space的cell创建好了
		"""
		self._spaceAllocs[spaceUType].onSpaceGetCell(spaceEntityCall, spaceKey)

