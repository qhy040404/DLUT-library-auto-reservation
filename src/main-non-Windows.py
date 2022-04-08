# coding=utf-8

# import
import sys
import reserve
import smtplib
from email.mime.text import MIMEText
import time

# initialize map
area_map = {'BC': '17', 'LX': '32'}
room_map = {'17': {'301': '168', '312': '170', '401': '195',\
                   '404': '197', '409': '196', '501': '198',\
                   '504': '199', '507': '200'},\
            '32': {'301': '207', '302': '208', '401': '205',\
                   '402': '206', '501': '203', '502': '204',\
                   '601': '201', '602': '202', '201': '180',\
                   '202': '181'}
           }

# Read config

with open("config.conf","r") as config:
    configData = config.readlines()
    if len(configData) == 1:
        print('请先按照example.conf生成配置文件')
        print('配置文件请写入config.conf')
        time.sleep(2)
        sys.exit()

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
    wanted_seats = seatData.split()

    # function email
    def send_email(seat = None, success = False, error = None):
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

        if success:
            context = '成功，座位位于' + area_name + '的' + room_name + '阅览室的' + seat + '座'
        else:
            context = '没约到，明儿再试试吧.' + error

        message = MIMEText(context,'plain','utf-8')
        message['Subject'] = '座位预定'
        message['From'] = sender
        message['To'] = receiver

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host,465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receiver, message.as_string())
            smtpObj.quit()
            print('Email succeed')
        except smtplib.SMTPException as e:
            print('Email error', e)

    # main
    finalSeat, result, err = reserve.Reserve(user_id, password, wanted_seats, room_id)
    if configData:
            val = configData[0]
            val_list = val.split()
            if len(val_list) == 2:
                if result is True:
                    send_email(seat = finalSeat, success = result)
                else:
                    send_email(success = result, error = err)