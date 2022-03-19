# coding=utf-8
'''
main
@author: Shuaichi Li
@editor: qhy040404
@email: shuaichi@mail.dlut.edu.cn
@editor.email: qhy040404@mail.dlut.edu.cn
@date: 2022/03/19 15:44
'''

# import
import time
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

user_id = '学号'
password = '密码'

browser = webdriver.Chrome(executable_path='driver/chromedriver.exe')
browser.maximize_window()

'''登录'''
browser.get("https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php")
input_userid = browser.find_element_by_id('un')
input_userid.send_keys(user_id)
input_password = browser.find_element_by_id('pd')
input_password.send_keys(password)
login_button = browser.find_element_by_class_name('login_box_landing_btn')
login_button.click()

'''更改想要去的房间号，选取第二天的座位图'''
'''对应房间号：（以下均为令希）
201：180
202：181
301：207
302：208
401：205
402：206
501：203
502：204
601：201
602：202
202电子阅览区：242
'''
browser.get('http://seat.lib.dlut.edu.cn/yanxiujian/client/orderSeat.php?method=addSeat&room_id=208&area_id=32')
today_button = browser.find_element_by_id('todayBtn')
today_button.click()
tomorrow_button = browser.find_element_by_id('nextDayBtn')
tomorrow_button.click()
time.sleep(1)

'''与原作者采用了不一样的方法，可以精确定位想要的位置'''
'''在favorSeats中设定自己喜欢的位置'''
allTabs = browser.find_elements_by_css_selector("i[class='seat-label']")
for tab in allTabs:
    favorSeats = ['286', '288', '290']
    if tab.text in favorSeats:
        current_seat = tab.text
        tab.click()
        confirm_button = browser.find_element_by_id('btn_submit_addorder')
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