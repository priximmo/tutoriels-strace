%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : Un premier pas vers le diagnostic


<br>

## EXEMPLE LS VS ALIAS

```
alias ls='ls -larth'
alias
\ls
echo $$
```

<br>

* trace de ls

```
sudo strace -p <pid> -f
```

* syscall execve 

```
man 2 intro
man 2 execve
```

-----------------------------------------------------------------------------

## EXECVE : LES SYSCALLS

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

----------------------------------------------------------------------------------

## UN AUTRE EXEMPLE AVEC LES QUOTES

<br>

* autre exemple les quotes :

```
$xavki="A B    C"
echo $xavki
echo "$xavki"
```

