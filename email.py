# coding: utf-8
import os
from flask_mail import Mail, Message
from flask_script import Manager, Shell
from threading import Thread

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] = 'testforflask@126.com'  
app.config['MAIL_PASSWORD'] = 't123654789'  

mail = Mail(app)
manager = Manager(app)

def send_async_email(mag_dict):
    with app.app_context():
        msg = Message()
        msg.__dict__.update(msg_dict)
        mails.send(msg)

def msg_dict2(to, subject, **kwargs):
    msg = Message(
        subject='木犀团队 ' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = '您好，我是一封邮件'
    msg.html = '<p>您好, 我是一封邮件</p>'
    return msg.__dict__


def send_mail2(to, subject, **kwargs):
    send_async_email.delay(msg_dict2(to, subject, **kwargs))


manager.run()