import time
import subprocess
from uiautomation import *
import win32api
import pyautogui


def AutomateNotepad():
    # 打开桌面
    ShowDesktop()
    #打开calc
    subprocess.Popen('calc')
    #查找calc， 如果name有中文，python2中要使用Unicode
    window = WindowControl(searchDepth = 3, ClassName = 'ApplicationFrameWindow', SubName = u'计算器')
    time.sleep(2)
    # pyautogui.click(845,95)
    # 查找meun
    menu = ButtonControl(searchFromControl = window, Name = u'菜单')
    menu.Click()
    # 点击科学计算器
    selic = ListItemControl(Name = u'科学 计算器')
    selic.Click()
    # 计算1.5+2*3
    ButtonControl(AutomationId = 'num1Button').Click()
    ButtonControl(AutomationId = 'decimalSeparatorButton').Click()
    ButtonControl(AutomationId = 'num5Button').Click()
    ButtonControl(AutomationId = 'plusButton').Click()
    ButtonControl(AutomationId = 'num2Button').Click()
    ButtonControl(AutomationId = 'multiplyButton').Click()
    ButtonControl(AutomationId = 'num3Button').Click()
    ButtonControl(AutomationId = 'equalButton').Click()
    

    
    

if __name__ == "__main__":
	AutomateNotepad()