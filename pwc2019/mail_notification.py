#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText




def send_mail():
    to_list = ['t1@gmail.com', 't2@connect.ust.hk']
    mail_host = "smtp.163.com"

    # your also can change to alicloud to use own email address
    mail_user = "eamil"
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
