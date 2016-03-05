#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Models for user, contract.
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
	descr = StringField(ddl='text')
	updatetime = TextField(updatable=True, ddl='mediumtext')
	createtime = TextField(updatable=False, ddl='mediumtext')

class Contract(Model):
	__table__ = 'contract'

	id = IntegerField(primary_key=True, ddl='bigint')
	contract_id = StringField(ddl='varchar(255)')
	price = FloatField(ddl='double(12,2)')
	num = IntegerField(ddl='int(11)')
	starttime = TextField(updatable=True, ddl='mediumtext')
	endtime = TextField(updatable=True, ddl='mediumtext')
	signtime = TextField(updatable=True, ddl='mediumtext')
	type = IntegerField(ddl='int(11)')
	status = IntegerField(ddl='int(11)')
	descr = StringField(ddl='text')
	updatetime = TextField(updatable=True, ddl='mediumtext')
        createtime = TextField(updatable=False, ddl='mediumtext')
