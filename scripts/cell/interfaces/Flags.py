# -*- coding: utf-8 -*-
#
"""
"""

import GlobalDefine
from KBEDebug import *
import EntityDef as Def
import Types

@Def.interface()
class Flags:
	"""
	"""
	def __init__(self):
		pass

	@Def.property(flags=Def.CELL_PUBLIC)
	def flags(self) -> Def.INT32:
		return 0

	def setFlags(self, flags):
		self.flags = flags
		self.onFlagsChanged_(flags, True)
	
	def hasFlags(self, flags):
		return self.flags & flags

	def addFlags(self, flags):
		"""
		"""
		self.flags |= flags
		self.onFlagsChanged_(flags, True)

	def removeFlags(self, flags):
		"""
		"""
		self.flags &= ~flags
		self.onFlagsChanged_(flags, False)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onFlagsChanged_(self, flags, isInc):
		"""
		virtual method.
		"""
		pass


