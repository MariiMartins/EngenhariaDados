<!--
# Namespaces

Namespaces foram adicionados no kernel Linux na versão 2.6.24 e são eles que permitem o isolamento de processos quando estamos utilizando o Docker. São os responsáveis por fazer com que cada container possua seu próprio environment, ou seja, cada container terá a sua árvore de processos, pontos de montagens, etc., fazendo com que um container não interfira na execução de outro. Vamos saber um pouco mais sobre alguns namespaces utilizados pelo Docker.

## PID namespace
O PID namespace permite que cada container tenha seus próprios identificadores de processos. Isso faz com que o container possua um PID para um processo em execução -- e quando você procurar por esse processo na máquina host o encontrará; porém, com outra identificação, ou seja, com outro PID.

A seguir temos o processo "testando.sh" sendo executado no container.

Perceba o PID desse processo na árvore de processos dele:
```
root@c774fa1d6083:/# bash testando.sh &
[1] 7

root@c774fa1d6083:/# ps -ef
UID  PID PPID C STIME TTY TIME     CMD
root 1   0    0 18:06 ?   00:00:00 /bin/bash
root 7   1    0 18:07 ?   00:00:00 bash testando.sh
root 8   7    0 18:07 ?   00:00:00 sleep 60
root 9   1    0 18:07 ?   00:00:00 ps -ef

root@c774fa1d6083:/#
```
Agora, perceba o PID do mesmo processo exibido através do host:
```
root@linuxtips:~# ps -ef | grep testando.sh

root 2958 2593 0 18:12 pts/2 00:00:00 bash testando.sh
root 2969 2533 0 18:12 pts/0 00:00:00 grep --color=auto testando.sh

root@linuxtips:~#
```
Diferentes, né? Porém, são o mesmo processo. :)

## Net namespace
O Net Namespace permite que cada container possua sua interface de rede e portas. Para que seja possível a comunicação entre os containers, é necessário criar dois Net Namespaces diferentes, um responsável pela interface do container (normalmente utilizamos o mesmo nome das interfaces convencionais do Linux, por exemplo, a eth0) e outro responsável por uma interface do host, normalmente chamada de veth* (veth + um identificador aleatório). Essas duas interfaces estão linkadas através da bridge Docker0 no host, que permite a comunicação entre os containers através de roteamento de pacotes.

Conforme falamos, veja as interfaces. Interfaces do *host*:

```
root@linuxtips:~# ip addr

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
       inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
2: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
        link/ether 00:1c:42:c7:bd:d8 brd ff:ff:ff:ff:ff:ff
        inet 10.211.55.35/24 brd 10.211.55.255 scope global eth1
            valid_lft forever preferred_lft forever
        inet6 fdb2:2c26:f4e4:0:21c:42ff:fec7:bdd8/64 scope global dynamic
            valid_lft 2591419sec preferred_lft 604219sec
        inet6 fe80::21c:42ff:fec7:bdd8/64 scope link
            valid_lft forever preferred_lft forever
3: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
        link/ether 02:42:c7:c1:37:14 brd ff:ff:ff:ff:ff:ff
        inet 172.17.0.1/16 scope global docker0
            valid_lft forever preferred_lft forever
        inet6 fe80::42:c7ff:fec1:3714/64 scope link
            valid_lft forever preferred_lft forever
5: vetha2e1681: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master docker0 state UP group default
        link/ether 52:99:bc:ab:62:5e brd ff:ff:ff:ff:ff:ff
        inet6 fe80::5099:bcff:feab:625e/64 scope link
             valid_lft forever preferred_lft forever
root@linuxtips:~#
```

## Interfaces do container:

```
root@6ec75484a5df:/# ip addr

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
            valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
            valid_lft forever preferred_lft forever
6: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
        link/ether 02:42:ac:11:00:03 brd ff:ff:ff:ff:ff:ff
        inet 172.17.0.3/16 scope global eth0
            valid_lft forever preferred_lft forever
        inet6 fe80::42:acff:fe11:3/64 scope link
            valid_lft forever preferred_lft forever
root@6ec75484a5df:/#
```

Conseguiu visualizar as interfaces Docker0 e veth* do host? E a eth0 do container? Sim? Otémooo! :D

## Mnt namespace
É evolução do chroot. Com o Mnt Namespace cada container pode ser dono de seu ponto de montagem, bem como de seu sistema de arquivos raiz. Ele garante que um processo rodando em um sistema de arquivos não consiga acessar outro sistema de arquivos montado por outro Mnt Namespace.

## IPC namespace
Ele provê um SystemV IPC isolado, além de uma fila de mensagens POSIX própria.

## UTS namespace
Responsável por prover o isolamento de hostname, nome de domínio, versão do SO, etc.

## User namespace
O mais recente namespace adicionado no kernel Linux, disponível desde a versão 3.8. É o responsável por manter o mapa de identificação de usuários em cada container.