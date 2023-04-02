#Inclusão no inicio da lista, sintaxe:
LPUSH 4545 SQLSERVER ORACLE POSTGRES MYSQL
(integer) 4

#Inclusão no fim da lista
RPUSH 4545 DB2
(integer) 5

#Antes ou depois do Valor
LINSERT 4545 AFTER ORACLE FIREBIRD
(integer) 6
LRANGE 4545 0 5

LINSERT 4545 BEFORE FIREBIRD SQLLITE
(integer 7)