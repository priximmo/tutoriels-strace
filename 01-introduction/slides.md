%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : INTRODUCTION


<br>

## ORIGINES

<br>

* Outil de debug, diagnostic, analyse et performance

<br>

* Site : https://strace.io/

<br>

* Dépôt : https://github.com/strace/strace

<br>

* Date 1991 sur SunOS (Paul Kranenburg)

* Arrivé sur linux en 1992 (Branko Lankester)

<br>

* Installé de base sur Linux

* Evolutions : https://github.com/strace/strace/blob/master/NEWS

---------------------------------------------------------------------------


# STRACE : INTRODUCTION

<br>

## PRINCIPE

* Observation des syscalls (appels système) : user mode > kernel mode
		* principe de TRAP permet d'entrer dans le kernel mode
		* utilisé par à travers la libC

* Syscalls : Abstraction entre les programmes des utilisteurs et le kernel
		* sorte de fonction avec des paramètres

<br>

* man 2 syscall

```
       The system call is the fundamental interface between an
       application and the Linux kernel.
```

Rq : env 300 syscalls pour Linux

-----------------------------------------------------------------------------

# STRACE : INTRODUCTION

<br>

## INCEPTION

* strace utilise lui-même un syscall > ptrace

```
       #include <sys/ptrace.h>
       long ptrace(enum __ptrace_request request, pid_t pid,
                   void *addr, void *data);
```

<br>

* attention : réduit la performance des programmes

<br>

* utilisation simple

```
strace ls
```

Cf : fichiers joints

-----------------------------------------------------------------------------

# STRACE : INTRODUCTION

<br>

## QUI PEUT TRACER ?


<br>

* définit dans un paramètre kernel

```
/proc/sys/kernel/yama/ptrace_scope
```

0 : même UID

1 : ascendance (sinon élévation de privilèges)

2 : admin seulement

3 : interdit

Doc : https://www.kernel.org/doc/Documentation/security/Yama.txt

-----------------------------------------------------------------------------

# STRACE : INTRODUCTION

<br>

## QUI PEUT TRACER ?
<br>

* temporairement

```
sudo sysctl -w kernel.yama.ptrace_scope=0
```

* permanente

```
sudo echo 0 > /proc/sys/kernel/yama/ptrace_scope
```

ou

```
sudo vim /etc/sysctl.conf
sudo vim /etc/sysctl.d/10-ptrace.conf
```
