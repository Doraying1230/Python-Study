#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import urllib.parse
import random
import time
import queue
import csv
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import smtplib
from threading import Thread


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')
#
# # 邮件对象:
# msg = MIMEMultipart()
# msg['From'] = _format_addr('企保招招 <%s>' % from_addr)
# msg['To'] = _format_addr('用户 <%s>' % to_addr)
# msg['Subject'] = Header('来自企保招招的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
#msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#    '<p><img src="cid:0"></p>' +
#    '</body></html>', 'html', 'utf-8'))
#http://of4bjrz5z.bkt.clouddn.com/bg.jpg


config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'charset':'utf8mb4',
    'cursorclass':pymysql.cursors.DictCursor
    }
conn = pymysql.connect(**config)
conn.autocommit(1)
cursor = conn.cursor()
conn.select_db("mail")
n=0
mail_queue=queue.Queue()
mail_queue.put("451875565@qq.com")
mail_queue.put("franky.xu@qibaozz.com")
mail_queue.put("15274326989@163.com")
# csv_reader = csv.reader(open('./guanzhou_email.csv', encoding="GB18030"))
# for row in csv_reader:
#     print(row[0])
#     mail_queue.put(row[0])

print("共发送 %s 封邮件" % mail_queue.qsize())

while mail_queue:
    cursor.execute("select * from user where id = %s",random.randint(1,22))
    result=cursor.fetchone()
    print(result)
    from_addr = result['user_mail']
    password = result['password']
    to_addr = mail_queue.get()
    smtp_server = result['type']
    #邮件内容
    print("邮件内容")
    mail_msg = '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title></title>
            <style>
                *{margin:0;padding: 0;}
                background:url('http://of4bjrz5z.bkt.clouddn.com/bg.jpg')
            </style>
        </head>
        <body>
            <table border="0" cellpadding="0" cellspacing="0" id="tab1" align="center" style="margin: 0px auto; background: url('http://of4bjrz5z.bkt.clouddn.com/bg.jpg') no-repeat;width:750px;height:1400px;font-family: '微软雅黑';">
                <tbody style="text-align: center;">
                    <tr><td style="width:100%;height:93px"></td></tr>
                    <tr><td style="font-size: 35px;color:#e5423d;height:55px;">出口企业信用保障保险</td></tr>
                    <tr><td style="font-size: 35px;color:#e5423d;height:55px;">招招免费送</td></tr>
                    <tr><td style="width:100%;height:61px;"></td></tr>
                    <tr><td style="font-size: 12px;color:#010000;height:68px;padding-left:35px;">企保招招【2017】1号文件</td></tr>
                    <tr><td style="width:100%;height:99px;font-size: 28px;color:#35313f;">企保招招携手PICC中国人保财险隆重推出</td></tr>
                    <tr><td style="width:100%;height:31px;"><div style="width:213px;font-size: 19px;height:29px;line-height:29px;margin:0 auto;color:#fff;background: #e5423d;border:1px solid #eb6d69;">出口企业信用保障保险</div></td></tr>
                    <tr><td style="width:100%;height:240px;"></td></tr>
                    <tr><td style="width:100%;font-size: 18px;height:35px"><span style="color:#524ae7;padding-right: 100px;">货款收不到？</span><span style="color:#e5423d;padding-left: 120px;">企业增信</span></td></tr>
                    <tr><td style="width:100%;font-size: 18px;height:35px"><span style="color:#524ae7;padding-right: 70px;padding-left: 20px;">赔付高达10万美金</span><span style="color:#e5423d;padding-left: 90px;">帮助企业解决融资难</span></td></tr>
                    <tr><td style="width:100%;height:43px;"></td></tr>
                    <tr><td style="width:100%;height:90px;padding: 0 100px 0 120px;line-height:30px;text-align: left;font-size: 14px;color:#727689;">
                        <p>1.在企保招招注册，独享100%补贴，企业不花一分钱，享受企保招招定制SME出口信用险。</p>
                        <p>2.企保招招极光理赔，全程协助。</p>
                    </td></tr>
                    <tr><td style="width:100%;height:22px;"></td></tr>
                    <tr><td style="width:100%;height:32px;font-size: 12px;color:#524ae7;">成功注册企保招招，并领取信用险送京东购物卡500元。</td></tr>
                    <tr><td style="width:100%;height:32px;font-size: 12px;color:#524ae7;">官方400电话：400-009-7855</td></tr>
                    <tr><td style="width:100%;height:22px;">
                        <div style="width:388px;height:40px;line-height: 40px;border:1px solid #a0221e;position:relative;margin:0 auto;border-radius: 20px;">
                            <a href="http://www.qibaozz.com/credit_risk?from=email&email='''
    mail_msg2=to_addr+'''
    " style="width:100%;height:100%;position:absolute;top:-5px;left:-3px;background: #e5423d;color:#fff;font-size:20px ;border-radius: 20px;display:block;text-decoration: none;">我要免费领取</a>
                        </div>
                    </td></tr>
                    <tr><td style="width:100%;height:40px;"></td></tr>
                    <tr><td style="width:100%;height:180px;padding: 0 100px 0 120px;line-height:30px;text-align: left;font-size: 13px;color:#727689;">
                        企保招招（qibaozz.com）是全球领先的一站式的企业保险在线比价服务平台，在这平台上
                        拥有数以万计的企业保险产品、服务及解决方案，以及丰富多彩的保险知识问答平台企保问
                        问。企保招招（qibaozz.com）整合上游国际国内主流知名80+保险公司，为企业提供保险
                        综合订制比价，保单云管理和专业极光理赔的免费Saas平台，利用互联网、 大数据和AI打通
                        数据流的互联网金融服务平台，是企业专属智能风险官，帮助企业做最佳采购决策和风险管
                        理，成就客户！
                    </td></tr>
                    <tr><td style="width:100%;height:65px;"></td></tr>
                    <tr><td style="width:100%;height:16px;padding-right: 85px;font-size: 12px;color:#727689;text-align: right;">企保招招    2016年2月16日印发</td></tr>
                    <tr><td style="width:100%;height:16px;padding-right: 85px;font-size: 12px;color:#727689;text-align: right;">*活动解释权归企保招招</td></tr>
                    <tr><td style="width:100%;"></td></tr>
                </tbody>
            </table>
            <a href="http://www.51.la/?19118225" target="_blank"><img alt="&#x6211;&#x8981;&#x5566;&#x514D;&#x8D39;&#x7EDF;&#x8BA1;" src="http://img.users.51.la/19118225.asp" style="border:none" /></a>
        </body>
    </html>
    '''
    print("邮件对象")
    # 邮件对象:
    msg = MIMEMultipart()
    msg['From'] = _format_addr('企保招招 <%s>' % from_addr)
    msg['To'] = _format_addr('用户 <%s>' % to_addr)
    msg['Subject'] = Header('您有一份出口信用险待领取', 'utf-8').encode()


    msg.attach(MIMEText(mail_msg+mail_msg2, 'html', 'utf-8'))


    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    print("已登录，开始向用户发邮件")
    try:
        print("开始向用户%s发送邮件" % to_addr)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        print("向用户%s发送邮件成功" % to_addr)
        print("还剩%s封邮件需要发送" % mail_queue.qsize())

    except Exception as e:
        print(e)
        print("开始向用户%s发送邮件失败！！！" % to_addr)
        csv_file = open('./email_fail.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(csv_file)
        writer.writerow(to_addr)
        continue
    finally:
        server.quit()
        time.sleep(20)

# for i in range(3):
#     t = Thread(target=send_mail)
#     t.start()

# msg='''
# <table style="width:100%; font-family:'Microsoft Yahei';">
# 	<tbody>
# 		<tr>
# 			<td>
#
# 			<table style="width:100%; max-width:700px; margin:20px auto 0; padding:20px; background:#f6bb43;">
# 				<tbody>
# 					<tr style="overflow:hidden;">
# 						<td><span style="float:left; padding:2px 4px; color:#fff; font-size:18px; border:solid 1px #fff; font-weight:100;">本日天气 </span></td>
# 					</tr>
# 					<tr>
# 						<td style="font-size:30px; font-weight:700; text-align:center;"><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICI1ZWNkZDgzMTIxN2NlOWU5ZTMyY2YwNGNiNGE5MTZmNyIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzU3IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="display:block; margin:20px 0; color:#fff; line-height:1.6em; text-decoration:none;" target="_blank">代码还没写好，等写好了告诉你</a></td>
# 					</tr>
# 					<tr>
# 						<td style="font-size:15px;"><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICI1ZWNkZDgzMTIxN2NlOWU5ZTMyY2YwNGNiNGE5MTZmNyIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzU3IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="color:#fff; text-decoration:none;" target="_blank">代码还没写好，等写好了告诉你</a></td>
# 					</tr>
#
# 				</tbody>
# 			</table>
#
# 			<table style="width:100%; max-width:700px; margin:0 auto; padding:20px; background:#fff; border:solid 1px #eee;">
# 				<tbody>
# 					<tr style="overflow:hidden;">
# 						<td><span style="float:left; padding:2px 4px; color:#5e5e5e; font-size:18px; border:solid 1px #5e5e5e; font-weight:100;">开心一下 </span></td>
# 					</tr>
# 					<tr>
# 						<td style="padding:40px 0 10px; font-size:18px; color:#fff; font-weight:700;"><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICIwZDllNzBhYmM0ZjhmY2ZkYTlmZjFmYjhkNzU1YjVlMyIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNjYzIiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="color:#f6bb43; text-decoration:none;" target="_blank">Python猜解Web登录</a></td>
# 					</tr>
# 					<tr>
# 					</tr>
# 					<tr>
# 						<td><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICIwZDllNzBhYmM0ZjhmY2ZkYTlmZjFmYjhkNzU1YjVlMyIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNjYzIiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="color:#333; text-decoration:none; font-size:16px;" target="_blank">没有一种万能的方法达到破解密码的目的，挖洞利用门槛高，有时也没这个必要，所以猜解就成为唯一的选择。本实验使用Python实现暴力猜解wordpress管理员登录表单的功能，并使用多线程、破解队列来优化破解过程。</a></td>
# 					</tr>
# 					<tr>
# 						<td style="padding:10px 0 20px; overflow:hidden; font-size:14px; color:#999; border-bottom:solid 1px #ccc;"><span style="display:inline-block; margin-right:10px;">1个实验</span> <span>4558人学过</span> <a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICIwZDllNzBhYmM0ZjhmY2ZkYTlmZjFmYjhkNzU1YjVlMyIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNjYzIiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="float:right; color:#999; text-decoration:none; font-size:14px;" target="_blank">查看详情</a></td>
# 					</tr>
# 					<tr>
# 						<td style="padding:20px 0 10px; font-size:18px; color:#fff; font-weight:700;"><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICIwN2FlZjAxZjk4MjQ5OGQ2OGY5NjVmNmM1MDVmYzU3OCIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzQ5IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="color:#f6bb43; text-decoration:none;" target="_blank">3个C语言实例带你掌握递归方法论</a></td>
# 					</tr>
# 					<tr>
# 					</tr>
# 					<tr>
# 						<td><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICIwN2FlZjAxZjk4MjQ5OGQ2OGY5NjVmNmM1MDVmYzU3OCIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzQ5IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="color:#333; text-decoration:none; font-size:16px;" target="_blank">递归（英语：Recursion），又译为递回，在数学与计算机科学中，是指在函数的定义中使用函数自身的方法。递归一词还较常用于描述以自相似方法重复事物的过程。本课程通过3个C语言编程实例，让你在利用递归解决实际问题的过程中学习递归并掌握其核心思想。举一反三，懂得如何使用递归解决其他实际问题。</a></td>
# 					</tr>
# 					<tr>
# 						<td style="padding:10px 0 20px; overflow:hidden; font-size:14px; color:#999; border-bottom:solid 1px #ccc;"><span style="display:inline-block; margin-right:10px;">1个实验</span> <span>58人学过</span> <a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICIwN2FlZjAxZjk4MjQ5OGQ2OGY5NjVmNmM1MDVmYzU3OCIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzQ5IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="float:right; color:#999; text-decoration:none; font-size:14px;" target="_blank">查看详情</a></td>
# 					</tr>
# 					<tr>
# 						<td style="padding:20px 0 10px; font-size:18px; color:#fff; font-weight:700;"><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICI4N2M0Yjg0ZDBmNGUyNjgwYTk2YzNjYjNiZWM4MWY4MCIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzQ1IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="color:#f6bb43; text-decoration:none;" target="_blank">C++实现智能指针</a></td>
# 					</tr>
# 					<tr>
# 					</tr>
# 					<tr>
# 						<td><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICI4N2M0Yjg0ZDBmNGUyNjgwYTk2YzNjYjNiZWM4MWY4MCIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzQ1IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="color:#333; text-decoration:none; font-size:16px;" target="_blank">本系列课程通过使用C++语言实现智能指针的过程，来了解C++基本程序设计的方法，包括类的定义与使用，运算符的重载，模板类的使用方法，以及引用计数技术。</a></td>
# 					</tr>
# 					<tr>
# 						<td style="padding:10px 0 20px; overflow:hidden; font-size:14px; color:#999; border-bottom:solid 1px #ccc;"><span style="display:inline-block; margin-right:10px;">4个实验</span> <span>136人学过</span> <a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICI4N2M0Yjg0ZDBmNGUyNjgwYTk2YzNjYjNiZWM4MWY4MCIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvNzQ1IiwgImNhdGVnb3J5X2lkIjogNjc5MTZ9.html" style="float:right; color:#999; text-decoration:none; font-size:14px;" target="_blank">查看详情</a></td>
# 					</tr>
# 					<tr>
# 						<td style="padding:30px; text-align:center;"><a href="http://sendcloud_track.daily.shiyanlou.com/track/click/eyJ1c2VyX2lkIjogMjgzNjgsICJ0YXNrX2lkIjogIiIsICJlbWFpbF9pZCI6ICIxNDg3OTg0NDQ1MTIzXzI4MzY4XzI5NzE2Xzg2Njguc2MtMTBfOV81MV8xMjAtaW5ib3VuZDUzJDQ1MTg3NTU2NUBxcS5jb20iLCAic2lnbiI6ICIyZjRmN2QxMmIwZjJiNWYwMDEzMTU4YjU5MzI5ZWQzMSIsICJ1c2VyX2hlYWRlcnMiOiB7fSwgImxhYmVsIjogMCwgImxpbmsiOiAiaHR0cHMlM0EvL3d3dy5zaGl5YW5sb3UuY29tL2NvdXJzZXMvJTNGY291cnNlX3R5cGUlM0RhbGwlMjZ0YWclM0RhbGwlMjZvcmRlciUzRGxhdGVzdCIsICJjYXRlZ29yeV9pZCI6IDY3OTE2fQ==.html" style="display:inline-block; padding:8px 24px; color:#fff; background:#f6bb43; font-size:16px; border-radius:4px; text-decoration:none;" target="_blank">更多课程</a></td>
# 					</tr>
# 				</tbody>
# 			</table>
#
#
# '''