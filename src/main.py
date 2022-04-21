# coding=utf-8

# import
import time
import sys
import os
import platform
import reserve
import smtplib
from email.mime.text import MIMEText

# pre-define
ver = '3.0.1.2'

# initialize
reserve.logging.info('Welcome to DLUT-library-auto-reservation ' + ver)
reserve.logging.info(platform.platform() + ' ' + platform.machine())
reserve.logging.info('Python version: ' + platform.python_version())

# Wait for server
time.sleep(0.5)
reserve.logging.info('sleep 0.5s to avoid incorrect server time')

# initialize map
reserve.logging.info('Initializing maps')
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
reserve.logging.info('Importing data from config.conf')
with open("config.conf","r") as config:
    configData = config.readlines()
    if len(configData) == 1:
        reserve.logging.warning('No data detected in config.conf. Moving to ConfigGenerator.')
        print('配置文件无数据，正在打开配置生成器...')
        if platform.system() == 'Windows':
            os.system('timeout 1 >nul && start ConfigGenerator.exe')
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            os.system('sleep 1 && ./ConfigGenerator')
        reserve.logging.info('Exiting...')
        sys.exit()
    configData.pop(0)

while configData:
    reserve.logging.info('Spliting data')
    configData.pop(0)
    data = configData.pop(0)
    data = data.strip('\n')
    data = data.split()

    reserve.logging.info('Processing basic data.')
    user_id = data[0]
    password = data[1]
    area_name = data[2]
    room_name = data[3]
    area_id = area_map.get(area_name)
    room_id = room_map.get(area_id).get(room_name)

    reserve.logging.info('Processing seat data.')
    seatData = configData.pop(0)
    seatData = seatData.strip('\n')
    wanted_seats = seatData.split('-')

    # function email
    def send_email(seat = None, success = False, error = None):
        reserve.logging.info('Processing mail data.')
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

        print('Sending email...')
        reserve.logging.info('Sending email...')

        if success:
            reserve.logging.info('Success = True')
            context = '成功，座位位于' + area_name + '的' + room_name + '阅览室的' + seat + '座'
        else:
            reserve.logging.info('Success = False')
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
            reserve.logging.info('Email succeed')
        except smtplib.SMTPException as e:
            print('Email error', e)
            reserve.logging.error('Email error. ' + str(e))

    # main
    finalSeat, result, err = reserve.Reserve(user_id, password, wanted_seats, room_id)
    reserve.logging.info('Detecting more data')
    if configData:
        reserve.logging.info('Detected. Detecting if maildata.')
        val = configData[0]
        val_list = val.split()
        if len(val_list) == 2:
            reserve.logging.info('maildata detected.')
            if result is True:
                send_email(seat = finalSeat, success = result)
                reserve.logging.info('Detecting if moredata')
                if configData:
                    reserve.logging.info('Detected. Deleting maildata')
                    configData.pop(0)
                else:
                    reserve.logging.info('Exiting...')
            else:
                send_email(success = result, error = err)
                reserve.logging.info('Detecting if moredata')
                if configData:
                    reserve.logging.info('Detected. Deleting maildata')
                    configData.pop(0)
                else:
                    reserve.logging.info('Exiting...')
        else:
            reserve.logging.info('Detected multi-person data. Returning...')
            reserve.logging.info('')