

--- Criando view de clientes
CREATE VIEW dimClientes AS
SELECT DISTINCT 
	idCliente as id,
	nomeCliente as nome,
	cidadeCliente as cidade,
	estadoCliente as estado,
	paisCliente as pais
FROM Clientes c ;


--- Criando view de tempo
CREATE VIEW dimTempo AS
SELECT DISTINCT 
	dataLocacao,
	horaLocacao,
	dataEntrega,
	horaEntrega
FROM Locacoes l;


--- Criando view de carros
CREATE VIEW dimCarro AS
SELECT DISTINCT 
	c.idCarro,
    c.classiCarro,
    c.marcaCarro as marca,
    c.modeloCarro as modelo,
    c.anoCarro as ano,
    c.idCombustivel,
    c2.tipoCombustivel
FROM Carros c 
JOIN Combustiveis c2 ON c.idCombustivel = c2.idCombustivel;


--- Tentativa de criar dimCarro com mais dados -> Descartado
--- CREATE VIEW dimCarro AS
--- SELECT DISTINCT
---    c.idCarro,
---    c.classiCarro,
---    c.marcaCarro as marca,
---    c.modeloCarro as modelo,
---    c.anoCarro as ano,
---    l.kmCarro,
---    c.idCombustivel,
---    c2.tipoCombustivel
--- FROM Carros c
--- JOIN Combustiveis c2 ON c.idCombustivel = c2.idCombustivel
--- JOIN Locacoes l ON c.idCarro = l.idCarro;

--- Criando view dos vendedores
CREATE VIEW dimVendedor AS
SELECT DISTINCT 
	v.idVendedor as id,
	v.nomeVendedor as nome,
	v.sexoVendedor as sexo,
	v.estadoVendedor as estado
FROM Vendedores v ;

SELECT * FROM dimVendedor ;

--- Criando view da tabela fato

CREATE VIEW fatoLocacoes AS
SELECT DISTINCT 
	idLocacao as id,
	idCliente,
	idCarro,
	idVendedor,
	kmCarro,
	qtdDiaria as qtdDiariaLocacao,
	vlrDiaria as valorDiariaLocacao
FROM Locacoes l ;

--- Consultas ao DW

SELECT * FROM dimClientes;

SELECT * FROM dimTempo;

SELECT * FROM dimCarro ;

SELECT * FROM dimVendedor ;

SELECT * FROM fatoLocacoes ;