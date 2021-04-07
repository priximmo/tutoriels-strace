%title: STRACE
%author: xavki
%blog: [Xavki Blog](https://xavki.blog)


# STRACE : LE TEMPS


<br>

* -t : timestamp h:m:s

<br>

* -tt : microsecondes

<br>

* -ttt : epoch

<br>

* -T : durée par syscall (second)

<br>

* -c : synthèse

<br>

```
sudo strace -p 5387 -f -t 2>&1 | tee trace.log
```
