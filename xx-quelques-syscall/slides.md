%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : QUELQUES SYSCALLS A AVOIR SOUS LE COUDE...



<br>

* execve : permettre d'exécuter un programme comme un nouveau process

```
       int execve(const char *pathname, char *const argv[],
                  char *const envp[]);
```

```
pathname must be either a binary executable, or a script starting with a line of the form:
     #!interpreter [optional-arg]
```

Retour : 
0 = OK
-1 = erreur + code

Codes erreurs :
man 2 intro
man 3 errno


Variables :
strace ls /root/  2>&1 | head -n 1
strace -v -s 1024 ls /root/  2>&1 | head -n 1
strace -v -s 1024 ls /root/  2>&1 | head -n 1 | awk -F "[" '{print $3}' | tr "," "\n" | wc -l

Variables héritées du process

* open : 

* openat :

* read :

* write : 

* getxattr : 

* lgetxattr : 

* close :

* clone :

* stat :

* mmap :

* getdents :

* connect :

* accept :

* socket :

* ioctl :

* brk

* rt_sigaction

man 2 syscalls
