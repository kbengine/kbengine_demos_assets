# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from Space import Space
import d_entities
import d_spaces
import EntityDef as Def

@Def.entity()
class SpaceDuplicate(Space):
	"""
	这是一个空间的副本实体
	"""
	def __init__(self):
		Space.__init__(self)
		
