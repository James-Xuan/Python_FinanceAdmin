#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Models for user.
'''

import time, uuid

from transwrap.db import next_id
from transwrap.orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField

class User(Model):
	__table__ = 'users'
	
	id = IntegerField(primary_key=True, ddl='int(11)')
	email = StringField(updatable=False, ddl='varchar(255)')
	password = StringField(ddl='varchar(255)')
	name = StringField(ddl='varchar(255)')
	mobile = StringField(ddl='varchar(255)')
	status = IntegerField(ddl='int(11)')
	createtime = TextField(updatable=False, default=time.time, ddl='mediumtext')
