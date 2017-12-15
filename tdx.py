import time
import subprocess
from uiautomation import *
import win32api,win32gui, win32con
import win32com.client
import os

def  Auto():
	# 打开桌面
	ShowDesktop()
	# 打开同达信
	subprocess.Popen('TdxW')
	# 登录窗口
	login_window = PaneControl(searchDepth = 3, ClassName = "#32770")
	time.sleep(2)
	# 选择窗口(免费,收费)
	tab = TabControl(searchFromControl = login_window, AutomationId = '32954')
	li = tab.GetChildren()
	# 点击免费版
	li[1].Click()
	# 输入账号密码
	uname = EditControl(searchFromControl = login_window, AutomationId = '1443').SetValue('Mark1949')
	upwd = EditControl(searchFromControl = login_window, AutomationId = '1058').SetValue('1qaz2wsx')
	# 点击登录
	login = ButtonControl(searchFromControl = login_window, AutomationId = '1').Click()
	time.sleep(2)
	# 关闭广告窗口
	window = WindowControl(searchDepth = 3, ClassName = '#32770').Close()
	time.sleep(0.5)
	# 点击系统
	PaneControl(AutomationId = "1000").Click()
	# 键盘操作
	for i in range(10):
		uiautomation.Win32API.SendKey(uiautomation.Keys.VK_DOWN, waitTime=0.01)
	uiautomation.Win32API.SendKey(uiautomation.Keys.VK_ENTER, waitTime=0.01)

	# 获取CheckBox父窗口
	checkbox_father = WindowControl(searchDepth = 3, ClassName = "#32770", Name = '通讯设置')
	checkbox = checkbox_father.GetChildren()
	print(len(checkbox))
	# print(checkbox)
	
	for i in checkbox:
		li = ['登录时查找最快主站', ' 自动连接资讯主站']
		# print('8888888888',i)		
		print('Name:',i.Name,'classname:',i.ClassName,'type:',i.ControlType)
		if i.Name == '自动连接资讯主站' or i.Name == '登录时查找最快主站':
		# if i.Name in li:
			print(i)
			i.Click()

	# CheckBox
	# c = CheckBoxControl(AutomationId = '1414')
	# print(c.Name)
	# c.Click()



if __name__ == '__main__':
	Auto()