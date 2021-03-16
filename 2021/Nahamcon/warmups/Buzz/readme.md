# Buzz

Tags: _compress'd data_
## Challenge
>Author: @JohnHammond#6971
>
>You know, that sound that bumblebees make?
>
>Download the file below.
>Attachments:  buzz
>

## Solving
https://www.systutorials.com/docs/linux/man/1-compress/


```
$ file buzz
buzz: compress'd date 16 bits
```

`cp buzz buzz.z`

`uncompress buzz.z`

```
$ cat buzz
flag{b3a33db7ba04c4c9052ea06d9ff17869}
```

`flag{b3a33db7ba04c4c9052ea06d9ff17869}`
