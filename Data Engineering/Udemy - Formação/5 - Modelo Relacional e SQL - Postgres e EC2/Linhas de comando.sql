
---SQL P2
-- DML - INSERT, UPDATE, DELETE
INSERT INTO relacional.clientes (idcliente, cliente, estado, sexo, status)
VALUES
(251, 'Fernando Amaral', 'RS', 'M', 'Silver')

UPDATE relacional.clientes
SET estado='MS', status='Platinum'
WHERE idcliente=251;

DELETE FROM relacional.clientes
WHERE idcliente = 251;

-- DDL - CREATE TABLE, INDEX, VIEW, ALTER TABLE
CREATE TABLE relacional.clientes
(
    idcliente integer NOT NULL DEFAULT nextval ('relacional.idcliente'::regclass),
    cliente character varying (50),
    estado character verying (2),
    sexo character (1),
    status character varying(50),
    CONSTRAINT clientes_pkey PRIMARY KEY (idcliente)
)

-- DTL - BEGIN TRANSCATION, COMMIT, ROLLBACK
BEGIN;
INSERT INTO relacional.clientes(
    idcliente, cliente, estado, sexo, status)
    VALUES (251, 'Fernando Amaral', 'RS', 'M', 'Silver')
    SELECT * FROM relacional.clientes WHERE idcliente = 251
    ==COMMIT
    ROLLBACK
    SELECT * FROM relacional.clientes WHERE idcliente = 251

--- SQL P3
select count (*) from relacional.vendas as vendas;
inner join relacional.vendedores as vendedores on (vendas.idvendedor = vendedores.idvendedor);
select count (*) from relacional.vendas as vendas;
right join relacional.vendedores as vendedores on(vendas.idvendedor=vendedores.idvendedor)