# coding=utf-8
'''
main
@author: Shuaichi Li
@editor: qhy040404
@email: shuaichi@mail.dlut.edu.cn
@editor.email: qhy040404@mail.dlut.edu.cn
@date: 2022/03/19 19:30
'''

# import
import time
import tkinter
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Read config and seats
with open("config.txt","r") as config:
    data = config.readlines()
    rubbish1 = data.pop(0)
    del rubbish1
    data = ('').join(data)
    data.strip('\n')
    data = data.split()
    user_id = data[0]
    password = data[1]
    room_id = data[3]
    area_id = data[2]
with open("seats.txt","r") as seats:
    seatdata = seats.readlines()
    rubbish2 = seatdata.pop(0)
    del rubbish2
    seatdata = ('').join(seatdata)
    seatdata.strip('\n')
    favorSeats = seatdata.split()
url = ['http://seat.lib.dlut.edu.cn/yanxiujian/client/orderSeat.php?method=addSeat&room_id=','&area_id=']
url.insert(1,room_id)
url.append(area_id)
finalUrl = ('').join(url)

s = Service(r'driver/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.maximize_window()

'''登录'''
browser.get("https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php")
input_userid = browser.find_element(By.ID,'un')
input_userid.send_keys(user_id)
input_password = browser.find_element(By.ID,'pd')
input_password.send_keys(password)
login_button = browser.find_element(By.CLASS_NAME,'login_box_landing_btn')
login_button.click()

'''更改想要去的房间号，选取第二天的座位图'''
browser.get(finalUrl)
today_button = browser.find_element(By.ID,'todayBtn')
today_button.click()
tomorrow_button = browser.find_element(By.ID,'nextDayBtn')
tomorrow_button.click()
time.sleep(1)

'''与原作者采用了不一样的方法，可以精确定位想要的位置'''
allTabs = browser.find_elements(By.CSS_SELECTOR,"i[class='seat-label']")
for tab in allTabs:
    if tab.text in favorSeats:
        current_seat = tab.text
        tab.click()
        confirm_button = browser.find_element(By.ID,'btn_submit_addorder')
        try:
            time.sleep(0.5)
            confirm_button.click()
            top = tkinter.Tk()
            top.geometry('0x0+999999+0')
            tkinter.messagebox.showinfo("大连理工大学图书馆自动预约座位小程序","预约%s成功" % current_seat)
            top.destroy()
            break
        except:
            continue
time.sleep(2)

'''注销操作并关闭窗口'''
browser.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/loginOut.php")
time.sleep(1)
browser.close()