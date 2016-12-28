#!/usr/bin/python
# -*- coding: utf-8 -*-
import os,time,threading
import Acapela

sigkill = False

def Alyona():
	global sigkill
	global allowmp3
	sigkill = False
	allowmp3 = False
	
	tx = open('/tmp/ttsdata')
	txt = tx.read()

	res = Acapela.splitText(txt)
	session = Acapela.getSession()
	count = len(res)
	
	wr = threading.Thread(target=ru_writer,args=[res,session])
	wr.start()
	ct = 200
	while ct>0:
		if ct == 0:
			return
		if allowmp3:
			for i in range(0,count):
				os.system('mpg123 -q /tmp/ttsres'+str(i))
			return	
		else:
			ct = ct-1
			time.sleep(0.25)	


def ru_writer(res,session):
	global sigkill
	global allowmp3
	count = len(res)
	for i in range(0,count):
		if sigkill == True:
			return -1
		FILENAME = '/tmp/ttsres'+str(i)
		++count
		url = Acapela.getMp3(res[i].encode('utf-8'),session)
		r = Acapela.requests.get(url)	
		mp = open(FILENAME,'w')
		mp.write(bytearray(r.content))
		mp.close()
		if i == 0:
			allowmp3 = True

def sigKill():
	global sigkill
	sigkill = True


Alyona()