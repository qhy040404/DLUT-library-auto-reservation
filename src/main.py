# coding=utf-8

# import
import os
import platform
import sys
import time
from email.mime.text import MIMEText

import reserve
from mail import Mail, mails, send_all
from utils import has_more

# pre-define
ver = '3.1.0.2'

# initialize
reserve.logging.info('Welcome to DLUT-library-auto-reservation ' + ver)
reserve.logging.info(platform.platform() + ' ' + platform.machine())
reserve.logging.info('Python version: ' + platform.python_version())

# Wait for server
reserve.logging.info('Sleep 0.5s to avoid incorrect server time')
time.sleep(0.5)

# initialize map
reserve.logging.info('Initializing maps')
area_map = {'BC': '17', 'LX': '32'}
area_map_chs = {'BC': '伯川', 'LX': '令希'}
room_map = {'17': {'301': '168', '312': '170', '401': '195',
                   '404': '197', '409': '196', '501': '198',
                   '504': '199', '507': '200'},
            '32': {'301': '207', '302': '208', '401': '205',
                   '402': '206', '501': '203', '502': '204',
                   '601': '201', '602': '202', '201': '180',
                   '202': '181'}
            }


def send_and_exit():
    send_all()
    reserve.logging.info('Exiting...')


# Read config
reserve.logging.info('Importing data from config.conf')
with open("config.conf", "r") as config:
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

while has_more(configData):
    reserve.logging.info(configData.pop(0).strip('\n'))
    reserve.logging.info('Splitting data')
    data = configData.pop(0).strip('\n').split()

    reserve.logging.info('Processing basic data.')
    user_id, password, area_name, room_name = data[0], data[1], data[2], data[3]
    area_id = area_map.get(area_name)
    room_id = room_map.get(area_id).get(room_name)
    area_name_chs = area_map_chs.get(area_name)

    reserve.logging.info('Processing seat data.')
    seatData = configData.pop(0).strip('\n')
    wanted_seats = seatData.split('-')


    # function email
    def send_email(seat=None, success=False, error=None):
        reserve.logging.info('Processing and deleting mail data.')
        mail_data = configData.pop(0).strip('\n').split()

        mail_user, mail_pass = mail_data[0], mail_data[1]
        mail_host = f"smtp.{mail_user.split('@')[1]}"

        print('Generating email...')
        reserve.logging.info('Generating email...')

        if success:
            reserve.logging.info('Success = \'True\'')
            context = '成功，座位位于' + area_name_chs + '的' + room_name + '阅览室的' + seat + '座'
        else:
            reserve.logging.info('Success = \'False\'')
            context = '没约到，明儿再试试吧.' + error

        message = MIMEText(context, 'plain', 'utf-8')
        message['Subject'] = '座位预定'
        message['From'] = mail_user
        message['To'] = mail_user

        mails.append(Mail(mail_host, mail_user, mail_pass, message.as_string()))


    # main
    finalSeat, result, err = reserve.Reserve(user_id, password, wanted_seats, room_id)
    reserve.logging.info('Detecting more data')
    if has_more(configData):
        reserve.logging.info('Detected. Detecting if maildata.')
        more_data = configData[0].strip('\n').split()
        if more_data[0].startswith('#'):
            reserve.logging.info('Detected multi-person data. Returning...')
            reserve.logging.info('')
        else:
            reserve.logging.info('maildata detected. ')
            send_email(seat=finalSeat, success=result, error=err)
            reserve.logging.info('Detecting if moredata')
            if has_more(configData):
                reserve.logging.info('Detected. Returning...')
                reserve.logging.info('')
            else:
                send_and_exit()
    else:
        send_and_exit()
