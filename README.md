 这是一个KBEngine服务端demos资产库
========

## 开始

请将kbengine_demos_assets整个文件夹放置于服务端引擎根目录中，通常是这样:

![demo_configure](http://kbengine.github.io/assets/img/screenshots/demo_copy_kbengine.jpg)


## 启动服务端

使用固定参数来启动：(参数的意义:http://www.kbengine.org/cn/docs/startup_shutdown.html)
	
	首先进入对应的资产库kbengine/kbengine_demos_assets目录中，然后在命令行执行如下命令：

	Linux:
		start_server.sh

	Windows:
		start_server.bat


## 关闭服务端

快速杀死服务端进程:

	首先进入对应的资产库kbengine/kbengine_demos_assets目录中，然后在命令行执行如下命令： 

	Linux:
		kill_server.sh

	Windows:
		kill_server.bat


	(注意：如果是正式运营环境，应该使用安全的关闭方式，这种方式能够确保数据安全的存档，安全的告诉用户下线等等)

	Linux:
		safe_kill.sh

	Windows:
		safe_kill.bat

## 在代码中定义实体的方法和属性

首先需要导入EntityDef引擎的实体定义模块

	import EntityDef as Def

使用@Def.entity定义实体，hasClient告诉引擎，该实体包含客户端部分，如果不填写改选项默认为False。

	@Def.entity(hasClient=True)
	class Monster(KBEngine.Entity):
		def __init__(self):
			KBEngine.Entity.__init__(self)

	# Cell和Base上的方法以及属性请定义在各自的进程脚本文件中。
	# flags参数是必选的，其他是可选参数
	# persistent默认为False，表示该属性在实体允许存档时是否持久化
	#  “-> Def.UINT32” 是新版本python的语法，表示返回值类型，这里用于描述属性的类型
	# “return 0” 返回值被应用于属性的默认值，注意：如果不清楚该类型应该用什么默认值可以直接返回None，引擎将自动给一个初始默认值。
	@Def.property(flags=Def.ALL_CLIENTS, persistent=True)
	def myID(self) -> Def.UINT32:
		return 0

	@Def.property(flags=Def.ALL_CLIENTS)
	def myID1(self) -> Def.UINT8:
		pass

	# index表示该属性是一个索引，索引类型为Def.UNIQUE和Def.INDEX具体查mysql文档
	# 对于字符串类型可以使用databaseLength设置持久化该字段允许的字符串最大长度
	@Def.property(flags=Def.ALL_CLIENTS, persistent=True, index=Def.UNIQUE, databaseLength=32)
	def name(self) -> Def.UNICODE:
		return None

	# 定义可远程访问的方法，如果该方法需要被客户端调用，需要明确使用exposed选项告诉引擎这个方法允许被暴露给客户端访问
	# 方法的每个参数必须有类型的描述，否则引擎无法将数据打包和解包
	@Def.method(exposed=True)
	def test(self, type : Def.UINT8, name : Def.UNICODE):
		pass

	# 直接在服务器上定义客户端的方法描述。注意：客户端需要实现这个方法，服务器上如 entity.client.test1(1)就可以调用到客户端上了。
	@Def.clientmethod()
	def test1(self, type : Def.UINT8):
		pass

	# @Def.component给实体挂载一个组件。
	# persistent=True描述该组件是否参与持久化。注意：仅仅持久化组件内部属性定义为persistent=True的属性数据。
	# “-> Test” Test是demo中的组件脚本，参考base/Avatar.py中定义的用法。
	# 组件以实体属性的形式存在，component1为组件属性名称，可以通过self.component1来访问。
	# 注意：组件的挂在是全局的，在base、或者cell脚本上挂在组件，如果组件本身存在其他进程的部分则会自动创建该组件属性。
	@Def.component(persistent=True)
	def component1(self) -> Test:
		return None

## 在代码中直接定义数据类型

参考demo中scripts\user_type\Types.py的写法。

定义基础数据类型有二种方法:

	1: 简单注册一个类型， IDE可能无法自动提示
		Def.rename(OBJECT_ID=Def.INT32) 

	2: 使用装饰器注册，IDE可以自动提示OBJECT_ID
		@Def.rename()
		def OBJECT_ID() -> Def.INT32: pass

定义数组类型：

	@Def.fixed_array()
	def ID_LIST() -> Def.INT32: pass

定义字典类型：

	@Def.fixed_dict()
	class FIXEDDICT_DATA(dict):
		@Def.fixed_item()
			def param1(self) -> Def.INT8:
			return None

	# 如果实现了createObjFromDict、getDictFromObj、isSameType引擎将会把序列化和反序列化改数据类型的工作交给脚本处理，否则底层按默认格式处理
	@staticmethod
	def createObjFromDict(dct):
		self.param1 = dct["param1"]

	@staticmethod
	def getDictFromObj(obj):
		return {"param1" : obj.param1}

	@staticmethod
	def isSameType(obj):
		return isinstance(obj, FIXEDDICT_DATA)
