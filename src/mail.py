import smtplib

import reserve


class Mail:
    def __init__(self, host, user, passwd, message):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.message = message

    def send(self, count):
        print(f'Sending email#${count}...')
        reserve.logging.info(f'Sending email#${count}...')
        try:
            smtp_obj = smtplib.SMTP_SSL(self.host, 465)
            smtp_obj.login(self.user, self.passwd)
            smtp_obj.sendmail(self.user, self.user, self.message)
            smtp_obj.quit()
            print(f'Email #${count} succeed')
            reserve.logging.info(f'Email #${count} succeed')
        except smtplib.SMTPException as e:
            print(f'Email #${count} error', e)
            reserve.logging.error(f'Email #${count} error. ' + str(e))


mails: list[Mail] = []


def send_all():
    if len(mails) == 0:
        return
    count = 1
    for mail in mails:
        mail.send(count)
        count += 1
