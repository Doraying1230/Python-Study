#!/usr/bin/python
#coding:utf8

import os
def dirList(path):
	filelist = os.listdir(path)
	for filename in filelist:
		filepath = os.path.join(path,filename)
		if os.path.isdir(filepath):
			dirList(filepath)
		print filepath

allfile = dirList('/root/my/test')
print allfile




for path,d,filelist  in os.walk('/root/my/test'):
	for filename in filelist:
		os.path.join(path,filename)
