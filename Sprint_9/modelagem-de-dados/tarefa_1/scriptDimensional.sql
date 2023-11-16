

CREATE TABLE dimCliente (
	id INT PRIMARY KEY,
	nome VARCHAR(100),
	cidade VARCHAR(40),
	estado VARCHAR(40),
	pais VARCHAR(40)
)

INSERT INTO dimCliente (id, nome, cidade, estado, pais)
SELECT DISTINCT 
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tb_locacao;
-------------------------------------
SELECT * FROM dimCliente;
-------------------------------------
CREATE TABLE dimCarros (
	id INT PRIMARY KEY,
	classiCarro VARCHAR(50),
	marca VARCHAR(80),
	modelo VARCHAR(80),
	ano INT,
	tipoCombustivel VARCHAR(20)
)

INSERT INTO dimCarros (id, classiCarro, marca, modelo, ano, tipoCombustivel)
SELECT DISTINCT 
	idCarro,
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro,
	tipoCombustivel
FROM tb_locacao;
------------------------------
SELECT * FROM dimCarros ;
------------------------------
CREATE TABLE dimVendedores (
	id INT PRIMARY KEY,
	nome VARCHAR(15),
	sexo INT,
	estado VARCHAR(40)
)

INSERT INTO dimVendedores (id, nome, sexo, estado)
SELECT DISTINCT 
	idVendedor, 
	nomeVendedor, 
	sexoVendedor, 
	estadoVendedor
FROM tb_locacao;
-----------------------------------------------------
SELECT * FROM dimVendedores ;
-----------------------------------------------------

CREATE TABLE fatoLocacao (
	id INT PRIMARY KEY,
	kmCarro INT,
	qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    DataLocacao DATETIME,
    horaLocacao TIME,
	DataEntrega DATE,
	horaEntrega TIME,
	idCliente INT,
	idCarro INT,
	idVendedor INT,
	FOREIGN KEY (idCliente) REFERENCES dimCliente(id),
    FOREIGN KEY (idCarro) REFERENCES dimCarros(id),
    FOREIGN KEY (idVendedor) REFERENCES dimVendedores(id)
)

INSERT INTO fatoLocacao (id, kmCarro, qtdDiaria, vlrDiaria, DataLocacao, horaLocacao, DataEntrega, horaEntrega, idCliente, idCarro, idVendedor)
SELECT DISTINCT 
	idLocacao, 
	kmCarro, 
	qtdDiaria, 
	vlrDiaria, 
	dataLocacao, 
	horaLocacao,
	dataEntrega, 
	horaEntrega,
	idCliente,
	idCarro,
	idVendedor
FROM tb_locacao
---------------------------------
SELECT * from fatoLocacao 
---------------------------------
