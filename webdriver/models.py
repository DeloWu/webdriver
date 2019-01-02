# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Env(models.Model):
	# env_id 用于区分第几套环境
	env_id = models.IntegerField()
	env_name = models.CharField(max_length=20)
	env_url = models.CharField(max_length=200)
	env_ip = models.TextField(max_length=400)
	env_db = models.TextField(max_length=400)
	env_comment = models.TextField(max_length=400)
	# env_modifytime = models.DateTimeField('Latest modify time')
	env_author = models.CharField(max_length=20)

	def __str__(self):
		return 'objects:' + self.env_name
	__repr__ = __str__

class File(models.Model):
	file_name = models.CharField(max_length=50)
	file_size = models.CharField(max_length=20)
	file_path = models.CharField(max_length=100)
	file_author = models.CharField(max_length=20)
	file_upload_time = models.CharField(max_length=40)

	def __str__(self):
		return 'file:' + self.file_name
	__repr__ = __str__


if __name__ == '__main__':
	import django
	django.setup()