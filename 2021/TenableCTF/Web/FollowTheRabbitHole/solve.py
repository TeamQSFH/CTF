url = 'http://167.71.246.232:8080/rabbit_hole.php?url='
page = 'cE4g5bWZtYCuovEgYSO1'

import requests
import collections

c = {}

first = page
r = requests.get(url+page)
t = r.text

def process(c):
 out = ""
 for _ in range(max(k for k, v in c.items())+1):
  if _ in c:
   out += c[_]
 open('rabbithole.hex','w').write(out)

while t != 'end':
    var = t.split()
    c[int(var[0][1:-1])] = var[1][1:-2]
    page = var[2]
    r = requests.get(url+page)
    t = r.text

process(c)
open('rabbithole.png','wb').write(bytes.fromhex(open('rabbithole.hex','r').read()))
