# -*- coding:utf-8 -*-
import time
import random
from random import Random
from datetime import timedelta, date
import copy
# import demjson
import json
import random
import os
import sys
import string
import uniout


def get_timestamps_10():
	# 获取10位的时间戳
	return '{:.0f}'.format(time.time())


def get_timestamps_13(datetime=None):
	# 获取13位的时间戳
	if datetime:
		# year = datetimes[:4]
		# month = datetimes[5,7]
		# day = datetimes[8:10]

		timestamp = time.mktime(time.strptime(datetime, '%Y-%m-%d %H:%M:%S'))
		return '{:.0f}'.format(timestamp * 1000)
	else:
		return '{:.0f}'.format(time.time() * 1000)


def get_timestamps_13_beta(datetime=None):
	# 获取13位的时间戳_beta版
	if datetime:
		# year = datetime[:4]
		# month = datetime[5,7]
		# day = datetime[8:10]
		try:
			timestamp = time.mktime(time.strptime(str(datetime), '%Y-%m-%d %H:%M:%S'))
			return '{:.0f}'.format(timestamp * 1000)
		except ValueError:
			return 'datetime error!'
	else:
		return ''


def format_time(timestamps):
	# 将时间戳转换为时间格式
	if len(timestamps) == 10:
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamps)))
	elif len(timestamps) > 10:
		timestamps = int(timestamps[:10])
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamps))
	elif len(timestamps) < 10 and len(timestamps) >= 1:
		return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(timestamps)))
	else:
		return ''


def create_phone():
	# 自动生成手机号
	prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
	           "155", "156", "157", "158", "159", "186", "187", "188"]
	return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def create_phone_list(howMany):
	# 自动生成任意数量的手机号列表
	result = []
	while len(result) < int(howMany):
		result.append(create_phone())
	return result


def create_certid(birthday=None):
	# 自动生成身份证号
	areaCodeList = ["110105", "120104", "130108", "140200", "210122", "220402", "320402", "360423", "410202", "440111",
	                "500111", "542338", "530423", "610204", "632522", "652222"]
	modulus = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
	checkCodeList = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
	areaCode = areaCodeList[random.randint(0, len(areaCodeList) - 1)]
	randomCode = [str(random.randint(0, 9)) for i in range(3)]
	birthday = str(birthday)
	if birthday is None or len(birthday) != 6:
		year = str(random.choice(range(1960, 1995)))
		month = random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])
		day = str(random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09'] + range(10, 29)))
		birthday = year + month + day
	IDNo = areaCode + birthday + "".join(randomCode)
	tol = 0
	for i in range(len(IDNo)):
		temp = int(IDNo[i]) * modulus[i]
		tol = tol + temp
	checkCode = checkCodeList[tol % 11]
	return IDNo + checkCode


def create_certid_list(howMany, birthday=None):
	# 自动生成身份证号列表
	result = []
	while len(result) < int(howMany):
		result.append(create_certid(birthday))
	return result


def get_bank_card_bin(bank_name=None):
	# 获取银行卡bin
	card_bin_dict = {}
	card_bin_dict['工商银行'] = ['110610', '140210', '333332', '356879', '356881', '370246', '370248', '374739', '413520',
	                         '427018', '621226', '427028', '427039', '427064', '513685', '524091', '528856', '530990',
	                         '558360', '620403', '620405', '620407']
	card_bin_dict['农业银行'] = ['404117', '403361', '404119', '404121', '622830', '519412', '520082', '544243', '552599',
	                         '601427', '621282', '621671', '622821', '622823', '622825', '622827', '622838', '622840',
	                         '622840', '622845', '622848', '623018']
	card_bin_dict['中国银行'] = ['356833', '377677', '409666', '409668', '409670', '409672', '451291', '466245', '483519',
	                         '493898', '512316', '512412', '514957', '518377', '518379', '518475', '524864', '525745',
	                         '547766', '553131', '601382', '558869']
	card_bin_dict['建设银行'] = ['356895', '356899', '434061', '436718', '436728', '436738', '436745', '438617', '453242',
	                         '489592', '512988', '526410', '531693', '532458', '544887', '549103', '552245', '552801',
	                         '558895', '589970', '553242', '621284']
	card_bin_dict['中信银行'] = ['356391', '376966', '356392', '376969', '400360', '403391', '403393', '404157', '404159',
	                         '404171', '404172', '404174', '433666', '433668', '433669', '433671', '433680', '442730',
	                         '514906', '520108', '558916', '621768']
	card_bin_dict['光大银行'] = ['356839', '356840', '406252', '406254', '481699', '486497', '543159', '620085', '620535',
	                         '621490', '621491', '622161', '622650', '622655', '622658', '622660', '622662', '622664',
	                         '622666', '622668', '622670', '622673']
	card_bin_dict['华夏银行'] = ['431502', '523959', '528709', '539867', '539868', '621222', '622630', '622631', '622632',
	                         '622633', '622636', '622637', '623020', '623021', '623022', '625967', '625968', '625969',
	                         '628318', '623023', '431503', '528708']
	card_bin_dict['广发银行'] = ['406365', '406366', '428911', '436768', '436769', '436770', '487013', '491032', '491034',
	                         '491035', '491036', '491037', '491038', '493427', '520152', '528931', '541709', '548844',
	                         '552794', '621462', '622555', '622558']
	card_bin_dict['平安银行'] = ['356868', '356869', '526855', '528020', '602907', '621626', '622155', '622156', '622157',
	                         '622298', '622986', '623058', '623269', '625360', '625361', '625823', '625825', '627066',
	                         '627067', '627068', '627069', '628296']
	card_bin_dict['招商银行'] = ['356885', '356886', '356887', '356888', '356889', '356890', '370285', '370286', '370287',
	                         '370289', '402658', '410062', '439188', '439225', '439226', '451461', '468203', '479228',
	                         '479229', '518710', '521302', '545620']
	card_bin_dict['民生银行'] = ['356856', '356857', '356858', '356859', '377152', '377155', '407405', '415599', '421393',
	                         '421865', '421869', '421871', '427570', '427571', '464580', '472067', '472068', '512466',
	                         '517636', '528948', '545217', '545392']
	card_bin_dict['北京银行'] = ['421317', '422160', '422161', '522001', '602969', '621030', '628203', '625816', '623111',
	                         '622853', '622852', '622851', '622163', '621468', '621420']
	try:
		if bank_name:
			return (random.choice(card_bin_dict[bank_name]), bank_name)
		else:
			bank_name = random.choice(['工商银行', '农业银行', '中国银行', '建设银行', '中信银行', '光大银行', '华夏银行', '广发银行', '平安银行', '招商银行', '民生银行', '北京银行'])
			return (random.choice(card_bin_dict[bank_name]), bank_name)
	except KeyError:
		print('bank_name does not distinguish!')


def get_bankName_from_cardBin(cardBin):
	card_bin_dict = {}
	card_bin_dict['工商银行'] = ['110610', '140210', '333332', '356879', '356881', '370246', '370248', '374739', '413520',
	                         '427018', '621226', '427028', '427039', '427064', '513685', '524091', '528856', '530990',
	                         '558360', '620403', '620405', '620407']
	card_bin_dict['农业银行'] = ['404117', '403361', '404119', '404121', '622830', '519412', '520082', '544243', '552599',
	                         '601427', '621282', '621671', '622821', '622823', '622825', '622827', '622838', '622840',
	                         '622840', '622845', '622848', '623018']
	card_bin_dict['中国银行'] = ['356833', '377677', '409666', '409668', '409670', '409672', '451291', '466245', '483519',
	                         '493898', '512316', '512412', '514957', '518377', '518379', '518475', '524864', '525745',
	                         '547766', '553131', '601382', '558869']
	card_bin_dict['建设银行'] = ['356895', '356899', '434061', '436718', '436728', '436738', '436745', '438617', '453242',
	                         '489592', '512988', '526410', '531693', '532458', '544887', '549103', '552245', '552801',
	                         '558895', '589970', '553242', '621284']
	card_bin_dict['中信银行'] = ['356391', '376966', '356392', '376969', '400360', '403391', '403393', '404157', '404159',
	                         '404171', '404172', '404174', '433666', '433668', '433669', '433671', '433680', '442730',
	                         '514906', '520108', '558916', '621768']
	card_bin_dict['光大银行'] = ['356839', '356840', '406252', '406254', '481699', '486497', '543159', '620085', '620535',
	                         '621490', '621491', '622161', '622650', '622655', '622658', '622660', '622662', '622664',
	                         '622666', '622668', '622670', '622673']
	card_bin_dict['华夏银行'] = ['431502', '523959', '528709', '539867', '539868', '621222', '622630', '622631', '622632',
	                         '622633', '622636', '622637', '623020', '623021', '623022', '625967', '625968', '625969',
	                         '628318', '623023', '431503', '528708']
	card_bin_dict['广发银行'] = ['406365', '406366', '428911', '436768', '436769', '436770', '487013', '491032', '491034',
	                         '491035', '491036', '491037', '491038', '493427', '520152', '528931', '541709', '548844',
	                         '552794', '621462', '622555', '622558']
	card_bin_dict['平安银行'] = ['356868', '356869', '526855', '528020', '602907', '621626', '622155', '622156', '622157',
	                         '622298', '622986', '623058', '623269', '625360', '625361', '625823', '625825', '627066',
	                         '627067', '627068', '627069', '628296']
	card_bin_dict['招商银行'] = ['356885', '356886', '356887', '356888', '356889', '356890', '370285', '370286', '370287',
	                         '370289', '402658', '410062', '439188', '439225', '439226', '451461', '468203', '479228',
	                         '479229', '518710', '521302', '545620']
	card_bin_dict['民生银行'] = ['356856', '356857', '356858', '356859', '377152', '377155', '407405', '415599', '421393',
	                         '421865', '421869', '421871', '427570', '427571', '464580', '472067', '472068', '512466',
	                         '517636', '528948', '545217', '545392']
	card_bin_dict['北京银行'] = ['421317', '422160', '422161', '522001', '602969', '621030', '628203', '625816', '623111',
	                         '622853', '622852', '622851', '622163', '621468', '621420']
	try:
		if cardBin in card_bin_dict['工商银行']:
			return '工商银行'
		elif cardBin in card_bin_dict['农业银行']:
			return '农业银行'
		elif cardBin in card_bin_dict['中国银行']:
			return '中国银行'
		elif cardBin in card_bin_dict['建设银行']:
			return '建设银行'
		elif cardBin in card_bin_dict['中信银行']:
			return '中信银行'
		elif  cardBin in card_bin_dict['光大银行']:
			return '光大银行'
		elif cardBin in card_bin_dict['华夏银行']:
			return '华夏银行'
		elif cardBin in card_bin_dict['广发银行']:
			return '广发银行'
		elif cardBin in card_bin_dict['平安银行']:
			return '平安银行'
		elif cardBin in card_bin_dict['招商银行']:
			return '招商银行'
		elif cardBin in card_bin_dict['民生银行']:
			return '民生银行'
		elif cardBin in card_bin_dict['北京银行']:
			return '北京银行'
		else:
			return ''
	except:
		return ''


def bankcard(length=19, card_bin=None, bank_name=None):
	# 自动生成银行卡号
	if card_bin:
		gen_num = []
		for i in range(int(length) - len(card_bin) - 1):
			gen_num.append(str(random.randint(0, 9)))
		card = card_bin + "".join(gen_num)

	elif bank_name:
		gen_num = []
		for i in range(int(length) - len(get_bank_card_bin(bank_name)[0]) - 1):
			gen_num.append(str(random.randint(0, 9)))
		card = get_bank_card_bin(bank_name)[0] + "".join(gen_num)
	else:
		gen_num = []
		card_bin = get_bank_card_bin()[0]
		for i in range(int(length) - len(card_bin) - 1):
			gen_num.append(str(random.randint(0, 9)))
		card = card_bin + "".join(gen_num)
	sum_odd = 0
	sum_even = 0
	for i in range(len(card)):
		if i % 2 == 0:
			temp = int(card[-1 - i]) * 2
			if temp >= 10:
				temp = temp - 9
			sum_odd += temp
		else:
			sum_even += int(card[-1 - i])
	if bank_name:
		bank_title = bank_name
	elif card_bin:
		bank_title = get_bankName_from_cardBin(card_bin)
	else:
		bank_title = ''
	if (sum_even + sum_odd) % 10 == 0:
		return (card + '0', bank_title)
	else:
		return (card + str(10 - (sum_even + sum_odd) % 10), bank_title)


def create_bankcards(length, howMany, card_bin=None, bank_name=None):
	# 自动生成银行卡号列表
	result = []
	while len(result) < int(howMany):
		result.append(bankcard(length, card_bin, bank_name))
	return result



# 自动生成信用卡号
visaPrefixList = [
	['4', '5', '3', '9'],
	['4', '5', '5', '6'],
	['4', '9', '1', '6'],
	['4', '5', '3', '2'],
	['4', '9', '2', '9'],
	['4', '0', '2', '4', '0', '0', '7', '1'],
	['4', '4', '8', '6'],
	['4', '7', '1', '6'],
	['4']]
mastercardPrefixList = [
	['5', '1'], ['5', '2'], ['5', '3'], ['5', '4'], ['5', '5']]
amexPrefixList = [['3', '4'], ['3', '7']]
discoverPrefixList = [['6', '0', '1', '1']]
dinersPrefixList = [
	['3', '0', '0'],
	['3', '0', '1'],
	['3', '0', '2'],
	['3', '0', '3'],
	['3', '6'],
	['3', '8']]
enRoutePrefixList = [['2', '0', '1', '4'], ['2', '1', '4', '9']]
jcbPrefixList = [['3', '5']]
voyagerPrefixList = [['8', '6', '9', '9']]

def completed_number(prefix, length):
	"""
	'prefix' is the start of the CC number as a string, any number of digits.
	'length' is the length of the CC number to generate. Typically 13 or 16
	"""

	ccnumber = prefix
	# generate digits
	while len(ccnumber) < (length - 1):
		digit = str(generator.choice(range(0, 10)))
		ccnumber.append(digit)
	# Calculate sum

	sum = 0
	pos = 0

	reversedCCnumber = []
	reversedCCnumber.extend(ccnumber)
	reversedCCnumber.reverse()

	while pos < length - 1:

		odd = int(reversedCCnumber[pos]) * 2
		if odd > 9:
			odd -= 9

		sum += odd

		if pos != (length - 2):
			sum += int(reversedCCnumber[pos + 1])

		pos += 2

	# Calculate check digit

	checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
	ccnumber.append(str(checkdigit))
	return ''.join(ccnumber)

def credit_card_number(prefixList, howMany, length=16):
	result = []
	global generator
	generator = Random()
	generator.seed()
	while len(result) < howMany:
		ccnumber = copy.copy(generator.choice(prefixList))
		result.append(completed_number(ccnumber, length))
	return result


def output(title, numbers):
	#换行输入
	result = []
	result.append(title)
	result.append('-' * len(title))
	result.append('\n'.join(numbers))
	result.append('')

	return '\n'.join(result)

def create_customer_name():
	first_name_list=["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋","沈","韩","杨","朱","秦","尤","许","何","吕","施","张","孔","曹","严","华","金","魏","陶","姜","戚","谢","邹","喻","柏","水","窦","章","云","苏","潘","葛","奚","范","彭","郎","鲁","韦","昌","马","苗","凤","花","方","俞","任","袁","柳","酆","鲍","史","唐","费","廉","岑","薛","雷","贺","倪","汤","滕","殷","罗","毕","郝","邬","安","常","乐","于","时","傅","皮","卞","齐","康","伍","余","元","卜","顾","孟","平","黄","和","穆","萧","尹","姚","邵","湛","汪","祁","毛","禹","狄","米","贝","明","臧","计","伏","成","戴","谈","宋","茅","庞","熊","纪","舒","屈","项","祝","董","梁","杜","阮","蓝","闵","席","季","麻","强","贾","路","娄","危","江","童","颜","郭","梅","盛","林","刁","锺","徐","邱","骆","高","夏","蔡","田","樊","胡","凌","霍","虞","万","支","柯","昝","管","卢","莫","经","房","裘","缪","干","解","应","宗","丁","宣","贲","邓","郁","单","杭","洪","包","诸","左","石","崔","吉","钮","龚","程","嵇","邢","滑","裴","陆","荣","翁","荀","羊","於","惠","甄","麴","家","封","芮","羿","储","靳","汲","邴","糜","松","井","段","富","巫","乌","焦","巴","弓","牧","隗","山","谷","车","侯","宓","蓬","全","郗","班","仰","秋","仲","伊","宫","宁","仇","栾","暴","甘","钭","历","戎","祖","武","符","刘","景","詹","束","龙","叶","幸","司","韶","郜","黎","蓟","溥","印","宿","白","怀","蒲","邰","从","鄂","索","咸","籍","赖","卓","蔺","屠","蒙","池","乔","阳","郁","胥","能","苍","双","闻","莘","党","翟","谭","贡","劳","逄","姬","申","扶","堵","冉","宰","郦","雍","却","璩","桑","桂","濮","牛","寿","通","边","扈","燕","冀","僪","浦","尚","农","温","别","庄","晏","柴","瞿","阎","充","慕","连","茹","习","宦","艾","鱼","容","向","古","易","慎","戈","廖","庾","终","暨","居","衡","步","都","耿","满","弘","匡","国","文","寇","广","禄","阙","东","欧","殳","沃","利","蔚","越","夔","隆","师","巩","厍","聂","晁","勾","敖","融","冷","訾","辛","阚","那","简","饶","空","曾","毋","沙","乜","养","鞠","须","丰","巢","关","蒯","相","查","后","荆","红","游","竺","权","逮","盍","益","桓","公","万俟","司马","上官","欧阳","夏侯","诸葛","闻人","东方","赫连","皇甫","尉迟","公羊","澹台","公冶","宗政","濮阳","淳于","单于","太叔","申屠","公孙","仲孙","轩辕","令狐","钟离","宇文","长孙","慕容","司徒","司空","召","有","舜","叶赫那拉","丛","岳"]
	second_name_list = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
	               '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
	               '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都', '好',
	               '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开', '美',
	               '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意', '动',
	               '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯', '知',
	               '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正', '感',
	               '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果', '走',
	               '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真', '打',
	               '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界', '门',
	               '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性', '马',
	               '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让', '母',
	               '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英', '军',
	               '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快', '原',
	               '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条', '呢',
	               '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片', '罗',
	               '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合', '反',
	               '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运', '及',
	               '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司', '巴',
	               '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形', '影',
	               '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈', '容',
	               '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计', '您',
	               '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻', '统',
	               '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示', '愿',
	               '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社', '算',
	               '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息', '功',
	               '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图', '具',
	               '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引', '食',
	               '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试', '怀',
	               '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除', '跑',
	               '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳', '验',
	               '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿', '睡',
	               '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店', '否',
	               '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河', '续',
	               '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪', '索',
	               '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族', '低',
	               '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅', '街',
	               '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀', '律',
	               '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职', '属',
	               '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉', '遗',
	               '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳', '差',
	               '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府', '压',
	               '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童', '顶',
	               '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯', '巨',
	               '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层', '付',
	               '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀', '营',
	               '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊', '降',
	               '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙', '杰',
	               '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡', '预',
	               '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧', '误',
	               '乾', '坤']
	first_name = random.choice(first_name_list)
	second_name = ''
	for i in range(2):
		second_name = random.choice(second_name_list) + second_name
	return first_name + second_name

def create_customer_name_list(howMany=10):
	result = []
	while len(result) < int(howMany):
		result.append(str(create_customer_name()))
	return result

def create_customer_info(birthday=None, bankcard_lenth=19, bankcard_bin=None, bankcard_name=None, credit_card_flag=None, credit_card_length=16):
	#创建客户信息列表
	name = create_customer_name()
	certid = create_certid(birthday)
	phone = create_phone()
	if credit_card_flag:
		bankcard_number = credit_card_number(mastercardPrefixList,1, credit_card_length)[0]
		bank_name = ''
	else:
		bankcard_number = bankcard(length=bankcard_lenth,card_bin=bankcard_bin,bank_name=bankcard_name)[0]
		bank_name = get_bankName_from_cardBin(bankcard_number[:6])
	customer_info = [name, certid, phone, bankcard_number, bank_name]
	return customer_info

def create_customer_info_list(howMany=10, birthday=None, bankcard_lenth=19, bankcard_bin=None, bankcard_name=None, credit_card_flag=None, credit_card_length=None):
	result = []
	if credit_card_flag:
		while len(result) < int(howMany):
			result.append(create_customer_info(birthday,credit_card_flag=True, credit_card_length=credit_card_length))
	else:
		while len(result) < int(howMany):
			result.append(create_customer_info(birthday, bankcard_lenth, bankcard_bin, bankcard_name, credit_card_flag=False))
	return result

def file_iterator(file_name, chunk_size=102400):
	with open(file_name,'rb') as f: #如果不加‘rb’以二进制方式打开，文件流中遇到特殊字符会终止下载，下载下来的文件不完整
		while True:
			c = f.read(chunk_size)
			if c:
				yield c
			else:
				break

def formatSize(bytes):
	try:
		bytes = float(bytes)
		kb = bytes / 1024
	except:
		print("传入的字节格式不对")
		return "Error"

	if kb >= 1024:
		M = kb / 1024
		if M >= 1024:
			G = M / 1024
			return '{:.2f}'.format(G) + 'g'
		else:
			return '{:.2f}'.format(M) + 'm'
	else:
		return '{:.2f}'.format(kb) + 'k'


# 获取文件大小
def getDocSize(path):
	try:
		size = os.path.getsize(path)
		return formatSize(size)
	except Exception as err:
		print(err)

if __name__ == '__main__':
	print(sys.version)
	# print (get_timestamps_13('2017-12-12 22:22:22'))
	# print(format_time('15214392'))
	# print(create_phone())
	# print(create_phone_list(5))
	# print (create_certid())
	# print(create_certid_list(3))
	# print(create_bankcards(length=16, howMany=10 ,card_bin=None, bank_name=None))
	# print(format_time('15218844'))
	# print(get_bank_card_bin('北京银行'))
	# print( '\xe5\x8c\x97\xe4\xba\xac\xe9\x93\xb6\xe8\xa1\x8c'.decode('utf-8'))
	# print(bankcard(length=19, card_bin=None, bank_name=None))
	# print(get_timestamps_13_beta('2018-04-14 11:11:11'))
	# print(credit_card_number(mastercardPrefixList,10, 16))
	# print(bankcard(length=16))
	# print(create_customer_name_list())
	# print(create_customer_info())
	# print(create_customer_info_list())
	# print(create_customer_info_list(10,credit_card_flag=True))
	# print(create_customer_info(credit_card_flag=True,credit_card_length=13))
	# print(get_bankName_from_cardBin('539867'))
	print(get_timestamps_13())