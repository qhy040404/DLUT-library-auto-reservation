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
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# input data
user_id = str(input("请输入学号："))
password = str(input("请输入密码："))
while True:
    area = input("请输入地区（令希/伯川）：")
    if area == '令希':
        area_id = '32'
        while True:
            room = input("请输入房间：")
            if room == '201':
                room_id = '180'
                break
            elif room == '202':
                room_id = '181'
                break
            elif room == '301':
                room_id = '207'
                break
            elif room == '302':
                room_id = '208'
                break
            elif room == '401':
                room_id = '205'
                break
            elif room == '402':
                room_id = '206'
                break
            elif room == '501':
                room_id = '203'
                break
            elif room == '502':
                room_id = '204'
                break
            elif room == '601':
                room_id = '201'
                break
            elif room == '602':
                room_id = '202'
                break
            else:
                print("错误")
        break
    elif area == '伯川':
        area_id = '17'
        while True:
            room = input("请输入房间(三楼大厅请输入300)：")
            if room == '300':
                room_id = '212'
                break
            elif room == '301':
                room_id = '168'
                break
            elif room == '312':
                room_id = '170'
                break
            elif room == '401':
                room_id = '195'
                break
            elif room == '404':
                room_id = '197'
                break
            elif room == '409':
                room_id = '196'
                break
            elif room == '501':
                room_id = '198'
                break
            elif room == '504':
                room_id = '199'
                break
            elif room == '507':
                room_id = '200'
                break
            elif room == '111':
                room_id = '241'
                break
            else:
                print("错误")
        break
    else:
        print("错误")
url = ['http://seat.lib.dlut.edu.cn/yanxiujian/client/orderSeat.php?method=addSeat&room_id=', '&area_id=']
url.insert(1,room_id)
url.append(area_id)
favorSeats = str(input("请输入你想要的座位（单个，完整座位号）："))
temp = favorSeats
favorSeats = list()
favorSeats.append(temp)
while True:
    validate = str(input("如果还有想要的，请继续输入（单个），如果没有了请输入no："))
    if validate == 'no':
        break
    else:
        favorSeats.append(validate)

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
finalUrl = ('').join(url)
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
             tkinter.messagebox.showinfo("大连理工大学图书馆自动预约座位小程序","预约%s成功" % current_seat)
             break
         except:
             continue
time.sleep(2)

'''注销操作并关闭窗口'''
browser.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/loginOut.php")
time.sleep(2)
browser.close()