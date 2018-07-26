#!/bin/bash
#i can send mail to your email
export PATH=/usr/sbin:/usr/bin:$PATH
obj=`date +"%m%d"`"mycar"
cat /root/pycar/newurl |mailx -s $obj 你的邮箱地址
