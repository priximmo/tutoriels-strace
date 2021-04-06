%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : LES FORKS


<br>

## FORKS

<br>

pid parent > pid childs

ppid > pid

processus fils = recopie du contexte du process parent
		* copie de la mémoire avec copy on write
		* économique : copie si écriture nécessaire

<br>

fork() :

		* retourne le pid du fils sur le parent
		* retourne 0 sur l'enfant

getpid() / getppid()

Note : fork utilise le syscall clone()

------------------------------------------------------------------------------

## ZOMBIES

<br>

zombie = le parent n'attend plus l'enfant (wait() ou waitpid)
	* plus de lien entre parent et enfant
	* processus ayant terminé son exécution (exit())
	* reste en table processus (pas de wait() pour le supprimer)
	* les ressources sont libérés mais pas les PID (saturation)

<br>

* arrêt d'un zombie = signal SIGCHLD au parent

```
kill -s SIGCHLD <pid_parent>
```

----------------------------------------------------------------------------

## OPTIONS -f

<br>

* strace du parent et des enfants = -f

```
ps -e -o pid,ppid,command
strace -p <pid> -f
```

<br>

* si difficulté à s'attacher aux enfants ?

```
strace -p $(pidof nginx | sed -e 's/ /,/g')
```


