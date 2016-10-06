基于树莓派、esp8266硬件模块
通过Python、Django、lua、mqtt消息队列协议、mjpg_streamer
构建web远程控制平台：可控制小车移动、可视频实时查看
Github地址:https://github.com/haogeoyes/wificar.git

流程访问：手机访问树莓派Django地址,网页调用mjpg视频控件。点击按钮通过ajax发送请求mqtt将消息转发至小车client以实现控制,页面记录访问ip地址,访问次数,点击控制次数

结构目录说明：
server.py	mqtt Server 消息接收端口1833端口
client.py	mqtt client 消息发送端
xiaoche.html	web端控制界面
views.py	Django控制代码
init.lua	esp8266模块小车启动程序
application.lua	esp8266模块控制代码

