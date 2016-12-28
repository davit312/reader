import requests
import os
import time


#get session
def getSession():
	if not os.path.isfile('/tmp/phsess'):
		sess = requests.get('http://www.acapela-group.com/')
		ss = sess.cookies['PHPSESSID']
		row = str(time.time()) + '|' + ss
		f = open("/tmp/phsess", "w")
		f.write(row)
		f.close()
		return ss
	else:
		f = open("/tmp/phsess", "r")
		row = f.read()
		tm = row[0:row.find('|')]
		f.close()
		if float(tm)+2700 > time.time():
			return row[row.find('|')+1:]
		else:
			os.remove("/tmp/phsess") 
			return getSession()


#Send request
def getMp3(text,ss):	
	cookies = dict(PHPSESSID=ss)
	postd = "MyLanguages=sonid25&MySelectedVoice=Alyona&&MyTextForTTS="+text+"&t=1&SendToVaaS="
	headers = {'Content-Type':'application/x-www-form-urlencoded',
			   'User-agent':'my-app/0.0.1'
			   }

	r = requests.post('http://www.acapela-group.com/demo-tts/DemoHTML5Form_V2.php',
		data = postd,
		headers = headers,
		cookies=cookies
	)
	start = r.text.find("var myPhpVar = '")+16
	end = r.text.find("'",start)
	return r.text[start:end]

def splitText(text):
	st = unicode(text,'utf-8')
	length = len(st)
	result = []
	begin = 0
	end = 188
	stop = ['.',',',':',' ',"\r\n"]
	
	while True:
		tmp = st[begin:end]
		if end>length:
			result.append(tmp)
			break

		for i in stop:
			j = tmp.rfind(i)
			if j != -1:
				tmp = tmp[:j+1]
				begin = begin+j+1
				end = begin+188
				result.append(tmp)
				break

	return result