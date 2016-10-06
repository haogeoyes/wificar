# -*- coding:utf-8 -*-
from django.shortcuts import render
from app.models import realtime_zzl_new 
from app.models import realtime_zhang
from django.shortcuts import render_to_response
import re
import json
import os
import sys
import time
import MySQLdb
import datetime

# Create your views here.
#coding:utf-8
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from realtime import * 
#from load_jiage import * 
#from ltest import * 
#from load_jichu import * 
from xiaoche import * 		#stop front back left right
from led import *  		#ledout ledhigh ledlow
from esp_led import *		#esp_led_check([1|0])



from django.http.response import HttpResponse,HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import (TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, EventMessage, ShortVideoMessage)


def xiaoche(request):
        ip = open('/home/pi/niuniu/ip.log','rb').read()
        if 'HTTP_X_FORWARDED_FOR' in request.META:
                getip=request.META['HTTP_X_FORWARDED_FOR']
        else:
                getip=request.META['REMOTE_ADDR']
        #追加pv到文件
        pv_log = open('/home/pi/niuniu/demo/django/hi/app/static/pv.log','a')
        nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pv_log.write(nowtime+" "+getip+"\n")
        #计算online
        pv_log.close
	os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/pv.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/pv_num.log')

        pv_log = open('/home/pi/niuniu/demo/django/hi/app/static/pv.log','r')
        nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #计算online
        r=r'%s'%(nowtime[0:13])
        hour_pv=len(re.findall(r,pv_log.read()))
        pv_log.close

	#os.system("fswebcam --no-banner -r 640x480 /home/pi/niuniu/demo/django/hi/app/static/images/image.jpg")
	return render(request,'xiaoche.html',{'ip':ip,'getip':getip,'hour_pv':hour_pv})





def home(request):
	if request.method=='GET':
		tmpdata=request.GET
	else:
		tmpdata="NA"
	db = MySQLdb.connect(user='root',db='iot',passwd='dabingjiayiqie',host='localhost')
	cursor=db.cursor()
	cursor.execute('select data from nodemcu')
	json_data=str(cursor.fetchall())
	json_data=json_data.split('\'')[1]
	db.close()
    	return HttpResponse(json_data)

def check_data(request):
	ip = open('/home/pi/niuniu/ip.log','rb').read()
    	if 'HTTP_X_FORWARDED_FOR' in request.META:
        	getip=request.META['HTTP_X_FORWARDED_FOR']
    	else:
        	getip=request.META['REMOTE_ADDR']
	#追加pv到文件
	pv_log = open('/home/pi/niuniu/demo/django/hi/app/static/pv.log','a')
	nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	pv_log.write(nowtime+" "+getip+"\n")
	#计算online
	pv_log.close


	pv_log = open('/home/pi/niuniu/demo/django/hi/app/static/pv.log','r')
	nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#计算online
	r=r'%s'%(nowtime[0:13])
	hour_pv=len(re.findall(r,pv_log.read()))
	pv_log.close
	
	#return HttpResponse(ip)
	return render(request,'index.html',{'ip':ip,'getip':getip,'hour_pv':hour_pv})
'''

def home(request):
	ip = open('/home/pi/niuniu/ip.log','rb').read()
	return render(request,'index.html',{'ip':ip})

def check_data_esp(request,param1):
	pv_log = open('/home/pi/niuniu/demo/django/hi/app/static/checkdata.log','a')
	nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	pv_log.write(nowtime+" "+param1+"\n")
	pv_log.close
	if param1=="led_on":
		esp_led_check(1)
		os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/checkdata.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/checkdata_num.log')	
	elif param1=="led_off":
		esp_led_check(0)
		os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/checkdata.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/checkdata_num.log')	
	elif param1=="front":
		esp_led_check("front")
		os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/checkdata.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/checkdata_num.log')	
	elif param1=="back":
		esp_led_check("back")
		os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/checkdata.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/checkdata_num.log')	
	elif param1=="left":
		esp_led_check("left")
		os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/checkdata.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/checkdata_num.log')	
	elif param1=="right":
		esp_led_check("right")
		os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/checkdata.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/checkdata_num.log')	
	else:
		esp_led_check(param1)
		os.system(' cat /home/pi/niuniu/demo/django/hi/app/static/checkdata.log  | wc -l >  /home/pi/niuniu/demo/django/hi/app/static/checkdata_num.log')	
	return HttpResponse("data:"+param1)
def led(request):
	ip=1
	return render(request,'led.html',{'ip':ip})

