# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from . import form
from . import function
from .models import Env, File
from .form import TimestampsForm, CreateDataForm, FileForm
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect,StreamingHttpResponse
from django.http.response import StreamingHttpResponse
from django.utils.encoding import escape_uri_path
from wsgiref.util import FileWrapper
from random import Random
import mimetypes
import os


def index(request):
	try:
		env_num = Env.objects.values('env_id').order_by('-env_id').distinct()[0]['env_id']
	except IndexError:
		return render(request, 'webdriver/index.html', context={})
	context = {}
	env_list_value = []
	tab_list = []
	for i in range(1, env_num + 1):
		env_name = 'env' + str(i)
		env_value = Env.objects.filter(env_id=i)
		context[env_name] = env_value
		env_list_value.append(env_value)
		tab_list.append('测试环境' + str(i))
	context['env_num'] = env_num
	context['env_list'] = env_list_value
	context['tab_list'] = tab_list
	return render(request, 'webdriver/index.html', context=context)

def webUrls(request):

	return render(request, 'webdriver/webUrls.html', context={})

def timestamps(request):
	timestamps_now = function.get_timestamps_13()
	form = TimestampsForm(request.GET)
	if form.is_valid():
		get_timestamps = form.cleaned_data['get_timestamps']
		get_BJ_time = form.cleaned_data['get_BJ_time']
		encode_content = form.cleaned_data['get_encode_content']
		decode_content = form.cleaned_data['get_decode_content']
		return render(request, 'webdriver/timestamps.html', context={
			'timestamps_now': timestamps_now,
			'last_get_timestamps': get_timestamps,
			'BJ_time': function.format_time(get_timestamps),
			'last_BJ_time': get_BJ_time,
			'format_timestamps': function.get_timestamps_13_beta(get_BJ_time),
			'last_encode_content': encode_content,
			'encode_content': encode_content,
			'last_decode_content': decode_content,
			'decode_content': decode_content,
		})



def jsonFormat(request):
	return render(request, 'webdriver/jsonFormat.html', context ={})

def createData(request):
	form = CreateDataForm(request.POST)
	if form.is_valid():
		birthday = form.cleaned_data['birthday']
		bankName = (form.cleaned_data['bankName']).encode('utf-8')
		credit_card_flag = form.cleaned_data['credit_card']
		bankcard_length = form.cleaned_data['bankcard_length']
		credit_card_length = form.cleaned_data['credit_card_length']
		if bankcard_length == '':
			bankcard_length = 19
		if credit_card_length == '':
			credit_card_length = 13
		customer_info_list = function.create_customer_info_list(howMany=10, birthday=birthday, bankcard_lenth=bankcard_length, bankcard_name=bankName, credit_card_flag=credit_card_flag, credit_card_length=credit_card_length)
		return render(request, 'webdriver/createData.html', context={
			'customer_info_list': customer_info_list,
		})
	else:
		customer_info_list = function.create_customer_info_list(howMany=10)
		return render(request, 'webdriver/createData.html', context={
			'customer_info_list': customer_info_list,
		})

def svnSpace(request, page):
	if page is None:
		page = '1'
	else:
		page = page
	objects_list = File.objects.all()
	paginator_instance = Paginator(objects_list, 15)
	objects_sum = paginator_instance.count
	range_lenth = paginator_instance.page_range
	page_object_dict = {}
	for i in range_lenth:
		page_object_dict[str(i)] = paginator_instance.page(i).object_list
	return render(request, 'webdriver/svnSpace.html', context ={'objects_list': page_object_dict[page],
	                                                            'objects_sum': objects_sum,
	                                                            'page': str(int(page) - 1),
	                                                            })

def upload(request, page):
	if page is None:
		page = '1'
	objects_list = File.objects.all()
	paginator_instance = Paginator(objects_list, 15)
	objects_sum = paginator_instance.count
	range_lenth = paginator_instance.page_range
	page_object_dict = {}
	for i in range_lenth:
		page_object_dict[str(i)] = paginator_instance.page(i).object_list
	if request.method == 'POST':
		# 获取上传的文件,如果没有文件,则默认为None;
		file = request.FILES.get("myfile", None)
		try:
			upload_dir = os.getcwd() + '\\webdriver\\static\\svnSpace\\%s' % file.name
		except AttributeError:
			upload_dir = os.getcwd() + '\\webdriver\\svnSpace'
		if file is None:
			return render(request, 'webdriver/svnSpace.html', context={'upload_status' : "no file for upload!",
			                                                           'objects_list': page_object_dict[page],
	                                                                   'objects_sum': objects_sum,
			                                                           'page' : str(int(page) - 1),
			                                                           })
		elif os.path.exists(upload_dir):
			return render(request, 'webdriver/svnSpace.html', context={'upload_status': "%s file exists!"%file.name,
			                                                           'objects_list': page_object_dict[page],
	                                                                   'objects_sum': objects_sum,
	                                                                   'page': str(int(page) - 1),
			                                                           })
		else:
			# 打开特定的文件进行二进制的写操作;
			# upload_dir = os.getcwd() + '\\webdriver\\static\\svnSpace\\%s'%File.name
			with open(upload_dir, 'wb+') as f:
				# 分块写入文件;
				for chunk in file.chunks():
					f.write(chunk)
			form = FileForm(request.POST)
			if form.is_valid():
				file_author = form.cleaned_data['uploader']
				file_name = file.name
				file_size = function.getDocSize(upload_dir)
				file_path = upload_dir
				file_upload_time = function.format_time(function.get_timestamps_13())
				file_instance = File(file_name=file_name,file_size=file_size,file_path=file_path,file_author=file_author,file_upload_time=file_upload_time)
				file_instance.save()
				return render(request, 'webdriver/svnSpace.html', context={'upload_status': "%s  upload success!"%file.name,
			                                                               'objects_list': page_object_dict[page],
	                                                                       'objects_sum': objects_sum,
	                                                                       'page': str(int(page) - 1),
				                                                           })
			else:
				return render(request, 'webdriver/svnSpace.html', context={'upload_status': "form error!",
			                                                               'objects_list': page_object_dict[page],
	                                                                       'objects_sum': objects_sum,
	                                                                       'page': str(int(page) - 1),
				                                                           })


def translator(request):
	return render(request, 'webdriver/translator.html', context ={})

def download_file(request):
	download_path = request.POST['download_path']
	file_name = request.POST['file_name']
	clientSystem = request.META['HTTP_USER_AGENT']
	wrapper = FileWrapper(open(download_path, 'rb'))
	content_type = mimetypes.guess_type(download_path)[0]
	response = StreamingHttpResponse(wrapper, 'content_type')
	response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path(file_name))
	return response

def searchFile(request):
	file_name = request.GET['searchFileName']
	object = File.objects.filter(file_name__contains=file_name)
	return render(request, 'webdriver/svnSpace.html', context={'objects_list': object,
	                                                           'lastFileName': file_name,
	                                                           })

def apiTest(request):
	return render(request, 'webdriver/apiTest.html', context={})