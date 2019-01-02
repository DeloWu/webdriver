# -*- coding:utf-8 -*-
from django import forms

class TimestampsForm(forms.Form):
	get_timestamps = forms.CharField(label='get_timestamps', max_length=30, required=False)
	get_BJ_time = forms.CharField(label='get_BJ_time',max_length=30, required=False)
	get_encode_content = forms.CharField(label='get_encode_content',required=False)
	get_decode_content = forms.CharField(label='get_decode_content', required=False)

class CreateDataForm(forms.Form):
	birthday = forms.CharField(label='birthday', max_length=8, required=False)
	bankName = forms.CharField(label='bankName', max_length=8, required=False)
	credit_card = forms.BooleanField(label='credit_card', required=False)
	bankcard_length = forms.CharField(label='bankcard_length', max_length=2, required=False)
	credit_card_length = forms.IntegerField(label='credit_card_length', required=False)

class FileForm(forms.Form):
	uploader = forms.CharField(label='uploader',max_length=20,required=True)