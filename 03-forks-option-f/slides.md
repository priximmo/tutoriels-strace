%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : LES FORKS


<br>

Les Forks


pid parent > pid childs

process fils = recopie du contexte du process parent


fork() :

		* retourne le pid du fils sur le parent
		* retourne 0 sur l'enfant

getpid() / getppid()

zombie = le parent n'attend plus l'enfant (wait ou waitpid)

Note : fork utilise le syscall clone()

<br>

ps -e -o pid,ppid,command

sudo -p `pidof nginx | sed -e 's/ /,/g'`


https://unix.stackexchange.com/questions/155017/does-fork-immediately-copy-the-entire-process-heap-in-linux
