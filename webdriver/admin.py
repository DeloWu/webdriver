# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Env, File
from django.contrib import admin


class EnvAdmin(admin.ModelAdmin):
	list_display = ('env_name', 'env_url', 'env_ip', 'env_db',  'env_author')
	list_filter = ['env_id']
	search_fields = ['env_name']

admin.site.register(Env, EnvAdmin)

class FileAdmin(admin.ModelAdmin):
	list_display = ('file_name', 'file_size', 'file_path', 'file_author', 'file_upload_time')
	list_filter = ['file_upload_time']
	search_fields = ['file_name']

admin.site.register(File, FileAdmin)