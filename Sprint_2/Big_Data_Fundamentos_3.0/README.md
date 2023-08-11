Diretório Big Data Fundamentos 3.0
==================================
### Diretório dedicado ao conteúdo do curso "Big Data Fundamentos" do Data Science Academy - Sprint 2;

## Resumo
### O que é Big Data?
É um conjunto de uma grande quantidade de dados complexos que não podem ser processados por bancos de dados ou aplicações de processamento convencionais;  
Mais do que somente manipular dados, estamos interessados em como extrair valor do Big Data, assim ele poderá ser útil. Afinal, de nada adianta ter uma grande quantidade de dados se não podemos retirar deles nenhuma informação relevante ou insight para a nossa operação;

O Big Data relaciona-se diretamente com o conceito dos 4 V's, os quais são indispensáveis para que exista Big Data.

### Os 4 V's do Big Data
1. Volume: Dados gerados em grandes quantidades;
2. Variedade: Formato dos dados -> PDF | JPG | IMG | CSV;
3. Velocidade: Como os dados são gerados, ou seja, gera-se dados a uma velociade gigantesca;
4. Veracidade: A confiabilidade dos dados;

A plena harmonia entre todos os 4 V's configura a existência de Big Data;

### Big Data X Ciência de Dados
É importante salientar que Big Data e Ciência de Dados **NÃO** são a mesma coisa.  
Quando nos referimos a Big Data, falamos sobre os dados em si, a matéria prima para a geração de valor.  
Já quando nos referimos a Ciência de Dados, estamos falando das técnicas empregadas para a análise de dados.  

Quando aplicamos a ciência de dados ao big data extraímos valor. Nesse situação temos o que é chamado de Big Data Analytics.

>### Casas de tamanhos de dados:
>KiloBytes -> MegaBytes -> GigaBytes -> TeraBytes -> PetaByte -> HexaByte -> ZettaBytes -> YottaBytes -> BrontoBytes -> GeoBytes...

### O "V" de *volume* no Big Data
É um conceito crítico em se falando de Big Data;  

Se uma empresa se preocupa unicamente com o modo que vão armazenar os dados mas não como vão acessá-los, ela certamente está **perdendo tempo**.  
Nesse aspecto a empresa precisa se perguntar:
* Como vamos armazenar grandes quantidades de dados?
* Como vamos acessar esses grandes conjuntos de dados?
* Precisamos mesmo armazenar todos os dados? (Existe um custo associado ao armazenamento);

Tudo isso está envolvido no V de volume, visto que essas resalvas são importantes de serem levantadas devido ao custo e ao trabalho existente no grande volume de dadosdo Big Data.

### Como devemos armazenar Big Data?
#### Regra Geral:
* Se os dados são **estruturados** ou podem ser estruturados antes do armazenamento, optamos por um **Data Warehouse**;
* Se os dados **NÃO** podem ser estruturados antes do armazenamento ou não são estruturados em si, optamos por um **Data Lake** ou um **Data Store**;

Dependendo do volume de daods, não haverá tempo o suficiente para primeiramente estruturar os dados. Você pode armazenar sem estruturar os dados em um DataLake e depois estruturá-los num Data Warehouse. Dependendo do cenário, também podemos fazer o inverso.

*Obs: DataWarehouse, DataLake e Data Store são **conceitos**. Eu posso guardar dados não estruturado em versões mais recentes do DataWareHouse, assim como posso armazenar dados já estruturados em um DataLake, não existe uma regra seguida a risca, apenas conceitos do que é mais viável.*

### SQL X NoSQL
Os **Bancos de Dados Relacionais** são bancos de dados estruturados e com schema (organização dos dados) bem definido.  
O schema deve ser definido e criado antes do armazenamento dos dados.  
Por exemplo, um datawarehouse geralmente é criado utilizando alguma tecnologia de banco relacional, como:
* Oracle
* TBM DB2
* Microsoft SQL Server
* MySQL
* PostgressQL
* SQLite

Nos **Bancos de Dados não Relacionais** os dados podem ser semi-estruturados ou ainda não estruturados. Além disso, outros tipos de relacionamento podem ocorrer, não somente por tabelas.  
Normalmente, não precisamos definir o schema antes do armazenamento ou ele é definido durante o processo de armazenamento.

#### *Para dar continuidade, vamos aprofundar os conceitos de Data WareHouse, Data Lake e Data Store*

### DataWareHouse
DataWareHouse é um sistema de armazenamento que conecta e harmoniza grandes quantidades de dados de muitas fontes diferentes.  
Que tipos de fontes?? **Dos mais variados tipos!**

Tem como objetivo alimentar a inteligência dos negócios, relatórios e análises e oferecer suporte aos requisitos de negócio para que as empresas possam transformar seus dados em insights e, principalmente, em **valor!**

O DataWareHouse armazena dados atuais e históricos em um único lugar e atuam como a única fonte confiável de informações.  
Os dados fluem de um DW por meio de sistemas transacionais, como **ERP** e **CRM**.

Como já mencionado anteriormente, o schema deve ser elaborado e definido antes do processo de armazenamento de dados em se tratando de um DataWareHouse.

Algumas pessoas aproveitam a análise de dados integgrada e a tecnologia de banco de dados in-memory para fornecer acesso em tempo real a dados confiáveis e impulsionar a tomada de decisões.

Sem o **DW** é muito difícil combinar dados de fontes heterogêneas, garantir que eles estejam no formato correto e ter uma boa visão com base neles.

#### Benefícios do DataWareHouse
* **Melhor análise dos negócios:**
* **Consultas mais rápidas:**
* **Melhoria da qualidade dos dados:**
* **Visão histórica:**

### DataLakes
Também é um sistema de armazenamento. Porém, diferentemente de um DW, é usado geralmente para armazenar dados brutos, ou seja, não estruturados. Entretanto, podemos armazenar tanto dados estruturados quanto não estruturados, afinal, tanto DW quanto um DL são **conceitos**.  
Assim, quando o processo de estruturação for necessário, o analista pode fazer a limpeza dos dados necessários.  

Geralmente uma empresa pede tanto um datawarehouse quanto um datalake pois eles atendem a diferentes necessidades e casos de uso (**Ambos são importantes!**).

O schema não é definido quando os dados são capturados. Você pode armazenar todos os dados em formato bruto rapidamente.

Existe, porém, um desafio para as empresas que implementam os DataLakes: Os dados brutos são armazenados sem nenhum tipo de supervisão de conteúdo. Eles também precisam de mecanismos que irão catalogar e proteger os dados.

***Dica:** Podemos importar dados do DW para o Datalake e vice versa*

#### Benefícios do DataLake:
* **Armazenamento em formato bruto:**
* **Importação de qualquer quantidade de dados em tempo real:**
* **Repositório central para todos os dados da empresa:**
* **Sem necessidade de movimentação dos dados:**

### DataStores
Repositórios feitos para armazenar e gerenciar de forma persistente coleções de dados que incluem dados estruturados e tipos de armazenamento variado, como documentos, dados no formado chave-flor, etc...

Ele permite que sejam armazenados dados variados e específicos para uma situação. Assim, já armazenamos dados praticamente prontos para serem usados.

#### Benefícios do DataStore
* **Armazenamento de variados tipos de dados:**
* **Flexibilidade:**
* **Suporte a dados semi-estruturados:**
* **Custo total menor:**

### Sistemas Híbridos de Armazemanto
## Certificado 
![image](/Sprint_2/Big_Data_Fundamentos_3.0/Certificado/Certificado%20de%20conclusão%20Big%20Data%20Fundamentos%203.0.jpg)
