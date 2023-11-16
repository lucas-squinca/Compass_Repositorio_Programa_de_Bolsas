CREATE TABLE Clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE Carros (
    idCarro INT,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT,
    idCombustivel INT,
    FOREIGN KEY (idCombustivel) REFERENCES Combustiveis(idCombustivel)
);

CREATE TABLE Combustiveis (
    idCombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

CREATE TABLE Vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(15),
    sexoVendedor INT,
    estadoVendedor VARCHAR(40)
);

CREATE TABLE Locacoes (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    kmCarro INT,
    dataLocacao DATETIME,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL(18, 2),
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carros(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedores(idVendedor)
);

INSERT INTO Clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT 
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
FROM tb_locacao
ORDER BY idCliente;

INSERT INTO Carros (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
SELECT DISTINCT 
	idCarro,
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro,
	idCombustivel
FROM tb_locacao
ORDER BY idCarro;

INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT 
	idVendedor, 
	nomeVendedor, 
	sexoVendedor, 
	estadoVendedor
FROM tb_locacao;

INSERT INTO Locacoes (idLocacao, idCliente, idCarro, kmCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT DISTINCT 
	idLocacao, 
	idCliente, 
	idCarro, 
	kmCarro,
	dataLocacao, 
	horaLocacao, 
	qtdDiaria, 
	vlrDiaria, 
	dataEntrega, 
	horaEntrega, 
	idVendedor
FROM tb_locacao;

INSERT INTO Combustiveis (idCombustivel, tipoCombustivel)
SELECT DISTINCT 
	idcombustivel, 
	tipoCombustivel
FROM tb_locacao;

-------------------------------------------------------------
SELECT * FROM Clientes 

SELECT * FROM Vendedores 

SELECT * FROM Carros 

SELECT * FROM Combustiveis 

SELECT * FROM Locacoes 