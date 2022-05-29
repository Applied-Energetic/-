"""
@author: 尚善蒲
@contact: applied_energetic@163.com
@Created on: 2022/5/29 
@Remark: 发送邮件功能
"""
from django.core.mail import send_mail
from application import settings
from django.shortcuts import HttpResponse
from django.core.mail import send_mail

def send_email_demo(request):
    from_who = settings.EMAIL_FROM  
    #发件人  已写在 配置中 可直接使用（163邮箱）
    to_who = '631526820@qq.com' 
    #收件人 是一个列表 不限邮箱
    subject = '检测到未出勤情况，请尽快回复'  
    # 发送的标题
    message = '检测到未出勤情况，请尽快回复'  
    # 发送的消息
    send_mail(subject, message, from_who, [to_who])
    return HttpResponse("ok")


#python manage.py shell

#进入Django Shell 使用电子邮件
from django.core.mail import send_mail
from application import settings
send_mail(
    subject='检测到未出勤情况，请尽快回复',
    message='检测到未出勤情况，请尽快回复',
    from_email=settings.EMAIL_HOST_USER,
    recipient_list=['631526820@qq.com'])

"""
源码: send_mail 的源码 里面参数很多
    def send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None):

"""