# coding=utf-8

# import
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import smtplib
from email.mime.text import MIMEText
import traceback

# initialize
area_map = {'伯川': '17', '令希': '32'}
room_map = {'17': {'301': '168', '312': '170', '401': '195',\
                   '404': '197', '409': '196', '501': '198',\
                   '504': '199', '507': '200'},\
            '32': {'301': '207', '302': '208', '401': '205',\
                   '402': '206', '501': '203', '502': '204',\
                   '601': '201', '602': '202'}
           }

# Read config
with open("config.conf","r") as config:
    configData = config.readlines()

while configData:
    configData.pop(0)
    data = configData.pop(0)
    data = data.strip('\n')
    data = data.split()

    user_id = data[0]
    password = data[1]
    area_name = data[2]
    room_name = data[3]
    area_id = area_map.get(area_name)
    room_id = room_map.get(area_id).get(room_name)

    seatData = configData.pop(0)
    seatData = seatData.strip('\n')
    favorSeats = seatData.split("-")

    def send_email(seat_id = None, successful = True):
        mailData = configData.pop(0)
        mailData = mailData.strip('\n')
        mailData = mailData.split()

        mail_user = mailData[0]
        mail_pass = mailData[1]
        sender = mailData[0]
        receiver = mailData[0]
        mail_temp_data = mail_user.split('@')
        mail_host_pre = 'smtp.'
        mail_host = mail_host_pre + mail_temp_data[1]

        print("Sending email...")

        if successful:
            context = '成功，座位位于' + area_name + '的' + room_name + '阅览室的' + seat_id + '座'
        else:
            context = '没约到，明儿再试试吧'

        message = MIMEText(context,'plain','utf-8')
        message['Subject'] = '座位预定'
        message['From'] = sender
        message['To'] = receiver

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host,465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receiver, message.as_string())
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error', e)

    url = ['http://seat.lib.dlut.edu.cn/yanxiujian/client/orderSeat.php?method=addSeat&room_id=','&area_id=']
    url.insert(1,room_id)
    url.append(area_id)
    finalUrl = ('').join(url)

    s = Service(r'driver/chromedriver.exe')
    browser = webdriver.Chrome(service=s)

    # 登录
    browser.get("https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php")
    input_userid = browser.find_element_by_id('un')
    input_userid.send_keys(user_id)
    input_password = browser.find_element_by_id('pd')
    input_password.send_keys(password)
    login_button = browser.find_element_by_class_name('login_box_landing_btn')
    login_button.click()

    # 更改想要去的房间号，选取第二天的座位图
    browser.get(finalUrl)
    today_button = browser.find_element_by_id('todayBtn')
    today_button.click()
    tomorrow_button = browser.find_element_by_id('nextDayBtn')
    tomorrow_button.click()
    time.sleep(1)

    # 与原作者采用了不一样的方法，可以精确定位想要的位置
    flag = False
    for i,item in enumerate(favorSeats):
        target = favorSeats[i]
        tab = browser.find_element_by_xpath("//table/tbody//tr//td/div[@class='seat-normal']/i[contains(text()," + target + ")]")
        tab.click()
        confirm_button = browser.find_element_by_id('btn_submit_addorder')
        try:
            time.sleep(0.5)
            confirm_button.click()
            seat_id = tab.text
            flag = True
            if configData:
                val = configData[0]
                val_list = val.split()
                if len(val_list) == 2:
                    send_email(seat_id, successful = True)
            break
        except Exception as e:
            traceback.extract_stack()
            print(e)
            continue

    if not flag:
        if configData:
            val = configData[0]
            val_list = val.split()
            if len(val_list) == 2:
                send_email(successful = False)

    time.sleep(2)
    ''
    # 注销操作并关闭窗口
    browser.get("http://seat.lib.dlut.edu.cn/yanxiujian/client/loginOut.php")
    time.sleep(1)
    browser.quit()