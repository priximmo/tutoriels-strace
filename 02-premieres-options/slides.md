%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : PREMIERES OPTIONS


<br>

CE TUTO :

	* découvrir les options -s / -p / -o


<br>

Rappel

```
strace ls
```

<br>

Mais si le programme tourne déjà ???

* -p / --attach : permet de passer un PID

```
ps aux | grep hello
pidof xxx
strace -p PID
```

<br>

-t : temps 

<br>

* strace de strace
