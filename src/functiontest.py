# coding=gbk
import time
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome(executable_path='driver/chromedriver.exe')
browser.maximize_window()

browser.get('http://seat.lib.dlut.edu.cn/yanxiujian/client/orderSeat.php?method=addSeat&room_id=208&area_id=32')
today_button = browser.find_element_by_id('todayBtn')
today_button.click()
tomorrow_button = browser.find_element_by_id('nextDayBtn')
tomorrow_button.click()
time.sleep(1)

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
