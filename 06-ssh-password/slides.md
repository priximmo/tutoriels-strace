%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : FILTRER LES SYSCALLS



<br>

## EXEMPLE SSH 

```
echo $$
strace -e read -p <pid> -f
```

<br>

## OUVERTURE DE FICHIERS CONF : PROFILE

```
strace -o trace.log -e openat -f bash --login -i
grep "/etc\|$HOME" trace.log
```
