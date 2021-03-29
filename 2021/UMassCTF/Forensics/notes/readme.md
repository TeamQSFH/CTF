# notes

>The breach seems to have originated from this host. Can you find the user's mistake? Here is a memory image of their workstation from that day.
>
>http://static.ctf.umasscybersec.org/forensics/13096721-bb26-4b79-956f-3f0cddebd49b/image.mem
>
>Created by [breeze]#3600


>## Hint
>There wasn't any suspicious network activity or anything... it's almost as if they just had their passwords up right on the screen.


```bash
$ strings -el image.mem |grep UMASS
UMASS{$3CUR3_$70Rag3}
```
