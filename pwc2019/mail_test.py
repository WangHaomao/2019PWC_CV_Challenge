#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText




def send_mail():
    to_list = ['wanghaomao.cn@gmail.com', 'hwangdo@connect.ust.hk']
    mail_host = "smtp.163.com"
    mail_user = "whmabcok"
    mail_pass = "2019pwc"
    mail_postfix = "163.com"

    sub = "subtitle"

    content = """
        write down your content here
    """

    me="hello"+"<"+mail_user+"@"+mail_postfix+">"


    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()

        return True
    except:
        return False

if __name__ == '__main__':

    print(send_mail())
