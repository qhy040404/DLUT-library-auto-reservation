# coding=utf-8

# import
import sso
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    filename='./access.log',
                    filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# pre-define
logging.info('Defining consts')
session_stat = 'http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=checkSession'
room_available_map_url = ['http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=querySeatMap&order_date=', '&room_id=']
get_addCode_url = 'http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=seatChoose'
addSeat_url = 'http://seat.lib.dlut.edu.cn/yanxiujian/client/orderRoomAction.php?action=addSeatOrder'
logout_url = 'http://seat.lib.dlut.edu.cn/yanxiujian/client/loginOut.php'
today = datetime.date.today()
year = str(today.year)
month = str(today.month)
day = str(today.day + 1)
order_date = year + '%2F' + month + '%2F' + day

# function
def constructParaForAddCode(seat_id, order_date):
    logging.info('Preparing POST data for AddCode')
    al = {
        'seat_id': seat_id,
        'order_date': order_date,
    }
    return '&'.join([i+'='+j for i, j in al.items()])

def constructParaForAddSeat(addCode):
    logging.info('Preparing POST data for AddSeat')
    al = {
        'addCode': addCode,
        'method': 'addSeat',
    }
    return '&'.join([i+'='+j for i, j in al.items()])

def Reserve(user_id, password, wanted_seats, room_id):
    logging.info('Arrived at reserve.py')

    # define result
    nice = False
    logging.info('Defining default result')

    # login and check session
    online = False
    logCount = 0
    while online is not True:
        logging.info('Logging in')
        s = sso.login(id=user_id, passwd=password)
        logging.info('Check session')
        ifLogin = s.get(session_stat).text
        if 'user_id' in ifLogin:
            online = True
            logging.info('Session is ' + str(online))
        else:
            logCount = logCount + 1
            print('Login error.', logCount)
            logging.error('Login error. ' + str(logCount))
            del s
            if logCount>=3:
                print('Failed 3 times. Check your username and password. Exiting.')
                logging.critical('Failed 3 times. Check your username and password. Exiting.')

    while True:
        # get seats status
        logging.info('Getting seats status')
        room_available_map = s.get(room_available_map_url[0] + order_date + room_available_map_url[1] + room_id).text
        room_available_map = room_available_map.strip('\ufeff\r\n\r\n[[{}]]\r\n\r\n\r\n\r\n')
        room_available_map = room_available_map.split('},{')
        room_available_map = (',').join(room_available_map)
        room_available_map = room_available_map.split(',')

        # check if available, get seat_id
        isASeat = False
        if type(wanted_seats) == str:
            logging.info('Data only includes 1 seat, mode 1')
            seat_label_num = wanted_seats
            seat_label = '"seat_label":"' + wanted_seats + '"'
            logging.info('Seat label data is ' + seat_label)
            while seat_label in room_available_map:
                j = room_available_map.index(seat_label)
                seat_type = int(room_available_map[j + 4].strip('"seat_type":"'))
                logging.info('Seat type data is ' + str(seat_type))
                if seat_type == 1:
                    isASeat = True
                    logging.info('Seat valid and setted')
                    print('Seat setted.')
                    break
                elif seat_type == 2 or seat_type == 3:
                    logging.error('Seat is not available. Type: ' + str(seat_type) + '. Seat: ' + str(seat_label_num))
                    print(seat_label_num + ' Seat unavailable.(Type)')
                    break
                else:
                    logging.warning('Seat invalid. Removing invalid data and switch to a valid seat.')
                    print('Not a seat. Switching...')
                    room_available_map.remove(seat_label)
        else:
            logging.info('Data includes multiple seats, mode 2')
            for i, seat_label_num in enumerate(wanted_seats):
                seat_label = '"seat_label":"' + seat_label_num + '"'
                logging.info('Current seat label: ' + seat_label)
                while seat_label in room_available_map:
                    j = room_available_map.index(seat_label)
                    seat_type = int(room_available_map[j + 4].strip('"seat_type":"'))
                    logging.info('Seat type data is ' + str(seat_type))
                    if seat_type == 1:
                        logging.info('Seat valid and setted')
                        isASeat = True
                        print('Seat setted.')
                        break
                    elif seat_type == 2 or seat_type == 3:
                        logging.error('Seat is not available. Type: ' + str(seat_type) + 'Seat: ' + str(seat_label_num))
                        print(seat_label_num + ' Seat unavailable.(Type)')
                        break
                    else:
                        logging.warning('Seat invalid. Removing invalid data and switch to a valid seat.')
                        print('Not a seat. Switching...')
                        room_available_map.remove(seat_label)
                if isASeat is True:
                    break

        if isASeat is not True:
            logging.error('Seat unavailable or invalid. Check logs above.')
            print('Failed. Seat unavailable.')
            return None, nice, 'Type Error.'

        status = int(room_available_map[j + 5].lstrip('"seat_order_status":'))
        logging.info('Checking another data to confirm seat status.')
        if status == 1:
            logging.info('Success')
        else:
            logging.error('Failed. Status is ' + str(status))
            print('Seat Unavailable.(status)')
            return None, nice, 'Status Error.'
        seat_id = room_available_map[j - 1].strip('"seat_id":""')

        # check session again
        logging.info('Checking session again')
        checkSession = s.get(session_stat).text
        if 'user_id' in checkSession:
            logging.info('Success')
        else:
            logging.warning('Failed. Re-logging in')
            print('Logged out. Sending login request.')
            del s
            s = sso.login(id=user_id, passwd=password)

        # get addCode
        logging.info('Processing addCode')
        addCode = s.post(get_addCode_url, constructParaForAddCode(seat_id, order_date), headers={'Content-Type': 'application/x-www-form-urlencoded'}).text
        addCode = addCode.split(',')
        addCode = addCode.pop()
        addCode = addCode.lstrip('"addCode":"')
        addCode = addCode.rstrip('"}}\r\n\r\n\r\n\r\n')
        logging.info('addCode is ' + addCode)

        # submit reserve post
        logging.info('Reserving')
        reserve_response = s.post(addSeat_url, constructParaForAddSeat(addCode), headers={'Content-Type': 'application/x-www-form-urlencoded'}).text
        if '预约成功' in reserve_response:
            logging.info('Success')
            print('Success.')
            nice = True
            error = None
            break
        else:
            print('Last Step Error.')
            error = reserve_response
            logging.error('Failed. Error data is')
            logging.error(error)
            logging.info('Detecting if wanted_seats is a list...')
            logging.info('Retrying...')

    # logout
    logging.info('Logging out...')
    s.get(logout_url)
    return seat_label_num, nice, error