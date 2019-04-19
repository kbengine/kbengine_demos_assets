# -*- coding: utf-8 -*-

"""
"""
import EntityDef as Def

# ------------------------------------------------------------------------------
# 定义数据类型， 类似types.xml的定义功能
# 定义数据类型有二种方法:
# 	1: 简单注册一个类型， IDE可能无法自动提示
# 		Def.rename(OBJECT_ID=Def.INT32) 
#	2: 使用装饰器注册，IDE可以自动提示OBJECT_ID
# 		@Def.rename()
#		def OBJECT_ID() -> Def.INT32: pass
# ------------------------------------------------------------------------------
@Def.rename()
def OBJECT_ID() -> Def.INT32: pass

@Def.rename()
def BOOL() -> Def.UINT8: pass

@Def.rename()
def CONTROLLER_ID() -> Def.INT32: pass

@Def.rename()
def EXPERIENCE() -> Def.INT32: pass

@Def.rename()
def ITEM_ID() -> Def.INT32: pass

@Def.rename()
def SKILLID() -> Def.INT32: pass

@Def.fixed_array()
def SKILLID_LIST() -> SKILLID: pass

@Def.rename()
def QUESTID() -> Def.INT32: pass

@Def.rename()
def DBID() -> Def.UINT64: pass

@Def.rename()
def UID() -> Def.UINT64: pass

@Def.rename()
def UID1() -> Def.PYTHON: pass

@Def.rename()
def ENTITY_ID() -> Def.INT32: pass

@Def.rename()
def ENTITY_NO() -> Def.UINT32: pass

@Def.rename()
def SPACE_ID() -> Def.UINT32: pass

@Def.rename()
def POSITION3D() -> Def.VECTOR3: pass

@Def.rename()
def DIRECTION3D() -> Def.VECTOR3: pass

@Def.rename()
def ENTITY_UTYPE() -> Def.UINT32: pass

@Def.rename()
def DAMAGE_TYPE() -> Def.INT32: pass

@Def.rename()
def ENMITY() -> DAMAGE_TYPE: pass

@Def.rename()
def HP() -> Def.INT32: pass

@Def.rename()
def MP() -> Def.INT32: pass

@Def.rename()
def ENTITY_STATE() -> Def.INT8: pass

@Def.rename()
def ENTITY_SUBSTATE() -> Def.UINT8: pass

@Def.rename()
def ENTITY_FORBIDS() -> Def.INT32: pass

@Def.fixed_array()
def ENTITY_FORBID_COUNTER() -> Def.INT8: pass

@Def.fixed_array()
def ENTITYID_LIST() -> ENTITY_ID: pass


#---------------------------------------------------------------------------------------------------
@Def.fixed_dict()
class AVATAR_DATA(dict):
	@Def.fixed_item()
	def param1(self) -> Def.INT8:
		return None

	@Def.fixed_item()
	def param2(self) -> Def.BLOB:
		return None

	def asDict(self):
		for key, val in self.items():
			return {"param1" : val[0], "param2" : val[1]}

	def createFromDict(self, dictData):
		self[dictData["param1"]] = [dictData["param1"], dictData["param2"]]
		return self

	# 如果实现了createObjFromDict、getDictFromObj、isSameType引擎将会把序列化和反序列化改数据类型的工作交给脚本处理，否则底层按默认格式处理
	@staticmethod
	def createObjFromDict(dct):
		"""
		该方法由引擎调用
		"""
		return AVATAR_DATA().createFromDict(dct)

	@staticmethod
	def getDictFromObj(obj):
		"""
		该方法由引擎调用
		"""
		return obj.asDict()

	@staticmethod
	def isSameType(obj):
		"""  
		该方法由引擎调用
		"""
		return isinstance(obj, AVATAR_DATA)

#---------------------------------------------------------------------------------------------------
@Def.fixed_dict()
class AVATAR_INFOS(list):
	@Def.fixed_item()
	def dbid(self) -> DBID:
		return 0

	@Def.fixed_item(databaseLength=256)
	def name(self) -> Def.UNICODE:
		return None # 如果返回None，则底层使用默认的初始值进行初始化，数字通常是0，字符串通常是空

	@Def.fixed_item()
	def roleType(self) -> Def.UINT8:
		return None

	@Def.fixed_item()
	def level(self) -> Def.UINT16:
		return None

	@Def.fixed_item()
	def data(self) -> AVATAR_DATA:
		return None

	def asDict(self):
		data = {
			"dbid"			: self[0],
			"name"			: self[1],
			"roleType"		: self[2],
			"level"			: self[3],
			"data"			: self[4],
		}
		
		return data

	def createFromDict(self, dictData):
		self.extend([dictData["dbid"], dictData["name"], dictData["roleType"], dictData["level"], dictData["data"]])
		return self

	@staticmethod
	def createObjFromDict(dct):
		"""
		该方法由引擎调用
		"""
		return AVATAR_INFOS().createFromDict(dct)

	@staticmethod
	def getDictFromObj(obj):
		"""
		该方法由引擎调用
		"""
		return obj.asDict()

	@staticmethod
	def isSameType(obj):
		"""  
		该方法由引擎调用
		"""
		return isinstance(obj, AVATAR_INFOS)

#---------------------------------------------------------------------------------------------------
@Def.fixed_array()
def AVATAR_INFOS_LIST_CHILD() -> AVATAR_INFOS: pass

@Def.fixed_dict()
class AVATAR_INFOS_LIST(dict):
	@Def.fixed_item()
	def values(self) -> AVATAR_INFOS_LIST_CHILD: # <values> <Type>	ARRAY <of> AVATAR_INFOS </of>	</Type> </values>
		return 0

	def asDict(self):
		datas = []
		dct = {"values" : datas}

		for key, val in self.items():
			datas.append(val)
			
		return dct

	def createFromDict(self, dictData):
		for data in dictData["values"]:
			self[data[0]] = data
		return self

	@staticmethod
	def createObjFromDict(dct):
		"""
		该方法由引擎调用
		"""
		return AVATAR_INFOS_LIST().createFromDict(dct)

	@staticmethod
	def getDictFromObj(obj):
		"""
		该方法由引擎调用
		"""
		return obj.asDict()

	@staticmethod
	def isSameType(obj):
		"""  
		该方法由引擎调用
		"""
		return isinstance(obj, AVATAR_INFOS_LIST)

#---------------------------------------------------------------------------------------------------
@Def.fixed_array()
def BAG_ITEM_ARRAY() -> Def.INT64: pass

@Def.fixed_array()
def BAG_ITEM_ARRAY_ARRAY() -> BAG_ITEM_ARRAY: pass

@Def.fixed_dict()
class BAG(dict):
	@Def.fixed_item()
	def values22(self) -> BAG_ITEM_ARRAY_ARRAY: # <values22> <Type>	ARRAY <of> ARRAY <of>INT64 </of></of>	</Type> </values22>
		return 0

#---------------------------------------------------------------------------------------------------
@Def.fixed_dict()
class EXAMPLES(dict):
	@Def.fixed_item(persistent=False)
	def k1(self) -> Def.INT64:
		return None

	@Def.fixed_item()
	def k2(self) -> Def.INT64:
		return None