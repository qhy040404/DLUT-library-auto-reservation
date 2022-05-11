import requests

from . import des


def initial(initUrl, id):
    s = requests.Session()
    response = s.get(initUrl)
    al = 'LT{}cas'.format(response.text.split('LT')[1].split('cas')[0])
    s.cookies.set('dlut_cas_un', id)
    s.cookies.set('cas_hash', "")
    return s, al


def constructPara(id, passwd, lt):
    al = {
        'none': 'on',
        'rsa': des.strEnc(id + passwd + lt, '1', '2', '3'),
        'ul': str(len(id)),
        'pl': str(len(passwd)),
        'sl': str(0),
        'lt': lt,
        'execution': 'e1s1',
        '_eventId': 'submit',
    }
    return '&'.join([i + '=' + j for i, j in al.items()])


def login(id, passwd):
    targetUrl = 'https://sso.dlut.edu.cn/cas/login?service=http://seat.lib.dlut.edu.cn/yanxiujian/client/login.php?redirect=index.php'
    s, lt = initial(targetUrl, id)
    s.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
    }
    s.post(targetUrl, constructPara(id, passwd, lt), headers={'Content-Type': 'application/x-www-form-urlencoded'})
    return s


if __name__ == '__main__':
    pass
