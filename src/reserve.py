# coding=utf-8

# import
import sso
import datetime

# pre-define
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
    al = {
        'seat_id': seat_id,
        'order_date': order_date,
    }
    return '&'.join([i+'='+j for i, j in al.items()])

def constructParaForAddSeat(addCode):
    al = {
        'addCode': addCode,
        'method': 'addSeat',
    }
    return '&'.join([i+'='+j for i, j in al.items()])

def Reserve(user_id, password, wanted_seats, room_id):
    # 执行状态定义
    nice = False

    # 登录并检查登录状态
    online = False
    while online is not True:
        s = sso.login(id=user_id, passwd=password)
        ifLogin = s.get(session_stat).text
        if '用户在线' in ifLogin:
            online = True
        else:
            print('Login error.')
            del s

    # 获取座位状态
    room_available_map = s.get(room_available_map_url[0] + order_date + room_available_map_url[1] + room_id).text
    room_available_map = room_available_map.strip('\ufeff\r\n\r\n[[{}]]\r\n\r\n\r\n\r\n')
    room_available_map = room_available_map.split('},{')
    room_available_map = (',').join(room_available_map)
    room_available_map = room_available_map.split(',')

    # 查看座位是否可用，获取seat_id
    isASeat = False
    if type(wanted_seats) == str:
        seat_label_num = wanted_seats
        seat_label = '"seat_label":"' + wanted_seats + '"'
        while seat_label in room_available_map:
            j = room_available_map.index(seat_label)
            seat_type = int(room_available_map[j + 4].strip('"seat_type":"'))
            if seat_type == 1:
                isASeat = True
                print('Seat setted.')
                break
            elif seat_type == 2 or seat_type == 3:
                print(seat_label_num + 'Seat unavailable.(Type)')
                break
            else:
                print('Not a seat. Switching...')
                room_available_map.remove(seat_label)
    else:
        for i, seat_label_num in enumerate(wanted_seats):
            seat_label = '"seat_label":"' + seat_label_num + '"'
            while seat_label in room_available_map:
                j = room_available_map.index(seat_label)
                seat_type = int(room_available_map[j + 4].strip('"seat_type":"'))
                if seat_type == 1:
                    isASeat = True
                    print('Seat setted.')
                    break
                elif seat_type == 2 or seat_type == 3:
                    print(seat_label_num + 'Seat unavailable.(Type)')
                    break
                else:
                    print('Not a seat. Switching...')
                    room_available_map.remove(seat_label)

    if isASeat is not True:
        print('Failed. Seat unavailable.')
        return None, nice, 'Type Error.'

    status = int(room_available_map[j + 5].lstrip('"seat_order_status":'))
    if status == 1:
        pass
    else:
        print('Seat Unavailable.(status)')
        return None, nice, 'Status Error.'
    seat_id = room_available_map[j - 1].strip('"seat_id":""')

    # 检查是否仍然在线
    checkSession = s.get(session_stat).text
    if '用户在线' in checkSession:
        pass
    else:
        print('Logged out. Sending login request.')
        del s
        s = sso.login(id=user_id, passwd=password)

    # 提取addCode
    addCode = s.post(get_addCode_url, constructParaForAddCode(seat_id, order_date), headers={'Content-Type': 'application/x-www-form-urlencoded'}).text
    addCode = addCode.split(',')
    addCode = addCode.pop()
    addCode = addCode.lstrip('"addCode":"')
    addCode = addCode.rstrip('"}}\r\n\r\n\r\n\r\n')

    # 提交预约post
    reserve_response = s.post(addSeat_url, constructParaForAddSeat(addCode), headers={'Content-Type': 'application/x-www-form-urlencoded'}).text
    if '预约成功' in reserve_response:
        print('Success.')
        nice = True
        error = None
    else:
        print('Last Step Error.')
        error = reserve_response

    # 登出
    s.get(logout_url)
    return seat_label_num, nice, error