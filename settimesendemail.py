#!/uer/bin/env python
#-*-coding:utf-8-*-

from flask import render_template, jsonify        #这两段在本程序中没有用，这两个包可以不导入'''
from flask_mail import Message, Mail                #提供对邮件的支持'''
#from celery.utils.log import get_task_logger            #记录器,似乎没有用，或者说我还没理解到位'''
import time                                            #时间模块，本程序是定时发送，所以没有用到，如果是定时间，即每天的几点发送，会用'''
from celery import Celery                               #celery 没什么好说的'''
from celery.schedules import crontab                    #用来实现定时发送，但是似乎不倒入也没有关系啊，什么鬼？'''
from flask import Flask                                     #flask.......'''


app = Flask(__name__)                               
app.config['MAIL_SERVER'] = 'smtp.126.com'                  #邮件配置，flask里学过，不过最好不要把
app.config['MAIL_PORT'] = 25                                #MAIL_USERNAME  MAIL_PASSWORD直接写到程序里
app.config['MAIL_USE_TLS'] = True                           #可以保存在环境变量里，本处邮箱仅供测试使用
app.config['MAIL_DEBUG'] = True
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME'] = 'testforflask@126.com'   
app.config['MAIL_PASSWORD'] = 't123654789'                                      

#CELERY_BROKER_URL = 'redis://redis1:6385/0'
#CELERY_BACKEND_URL = 'redis://redis1:6385/1'
CELERY_BROKER_URL = 'redis://localhost: 6379/0'             #配置redis， 具体的端口由自己决定，根据自己配置的时候修改
CELERY_BACKEND_URL = 'redis://localhost:6379/1'


celery = Celery('settimesendemail', broker=CELERY_BROKER_URL, backend=CELERY_BACKEND_URL)   ##建celery实例
mails = Mail(app)           #邮件....


@celery.task                   
def send_async_email(msg_dict):     #celery.task 创建一个celery任务， 由之后的celery beat调用
    with app.app_context():
        msg = Message()                 #异步发送邮件
        msg.__dict__.update(msg_dict)
        mails.send(msg)


def msg_dict2(to, subject, **kwargs):
    msg = Message(                              #构造邮件
        subject='哈哈哈' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = '您好，我是一封垃圾邮件'
    msg.html = '<p>您好, 我是一封垃圾邮件</p>'
    return msg.__dict__


def send_mail2(to, subject, **kwargs):
    send_async_email.delay(msg_dict2(to, subject, **kwargs))

@celery.on_after_configure.connect              
def setup_periodic_tasks(sender, **kwargs):         #由 celery beat实现周期性调用
	sender.add_periodic_task(5.0,send_async_email.s(msg_dict2('1113713599@qq.com',' 一封邮件')))


if __name__ == '__main__' :
    app.run()


'''具体运行：
            1.redis-server       ------启用redis服务器
            2.celery worker -A   <filename>.celery        -----启用该worker
            3.celery -A <filename>.celery beat         -----启用celery beat在规定时间内调用task

            至于为什么是 -A  我查的是 因为我们是用的flask写的 APP'''