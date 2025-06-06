Diretório para confirmação das atividades Sprint #6
===================================================

## Laboratório s3
#### Site estático funcionando com URL do Bucket:
![image](/Sprint_6/Laboratórios/lab-s3/Home%20Page%20do%20meu%20WebSite%20-%20Opera%2004_10_2023%2015_49_28.png)

#### Bucket configurado com os arquivos e funcionando:
![image](/Sprint_6/Laboratórios/lab-s3/Home%20Page%20do%20meu%20WebSite%20-%20Opera%2004_10_2023%2015_49_43.png)

#### Acesso ao público desabilitado:
![image](/Sprint_6/Laboratórios/lab-s3/Home%20Page%20do%20meu%20WebSite%20-%20Opera%2004_10_2023%2015_49_57.png)

#### Hospedagem de site estático configurado / Documento de índice e de erro adicionados:
![image](/Sprint_6/Laboratórios/lab-s3/Home%20Page%20do%20meu%20WebSite%20-%20Opera%2004_10_2023%2015_50_14.png)

## Laboratório Athena

#### Criando pasta **queries** Amazon S3:
![image](/Sprint_6/Laboratórios/lab-athena/Home%20Page%20do%20meu%20WebSite%20-%20Opera%2004_10_2023%2015_58_21.png)

#### Configurando Amazon Athena:
![image](/Sprint_6/Laboratórios/lab-athena/Home%20Page%20do%20meu%20WebSite%20-%20Opera%2004_10_2023%2016_03_17.png)

#### Criando o banco de dados:
![image](/Sprint_6/Laboratórios/lab-athena/Home%20Page%20do%20meu%20WebSite%20-%20Opera%2004_10_2023%2016_04_27.png)

#### Criando Tabela:
![image](/Sprint_6/Laboratórios/lab-athena/Query%20editor%20_%20Athena%20_%20us-east-1%20-%20Opera%2004_10_2023%2016_38_47.png)

#### Teste de dados do banco com consulta inicial:
![image](/Sprint_6/Laboratórios/lab-athena/Query%20editor%20_%20Athena%20_%20us-east-1%20-%20Opera%2004_10_2023%2016_39_27.png)

#### Resultado da consulta inicial solicitada:
![image](/Sprint_6/Laboratórios/lab-athena/Query%20editor%20_%20Athena%20_%20us-east-1%20-%20Opera%2004_10_2023%2016_40_02.png)

#### Query da consulta "Crie uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje."
![image](/Sprint_6/Laboratórios/lab-athena/_Query%20editor%20_%20Athena%20_%20us-east-1%20-%20Opera%2006_10_2023%2015_47_26.png)

#### Resultado da Query(também disponível como documento .csv na pasta)
![image](/Sprint_6/Laboratórios/lab-athena/_Query%20editor%20_%20Athena%20_%20us-east-1%20-%20Opera%2006_10_2023%2015_47_54.png)

#### Query SQL Final:

```sql
WITH TotalPorDecada AS (
  SELECT
    FLOOR(ano / 10) * 10 AS decada,
    nome,
    SUM(total) AS total_decada
  FROM minhatabela
  GROUP BY FLOOR(ano / 10) * 10, nome
),

NomesOrdenadosPorDecada AS (
  SELECT
    decada,
    nome,
    total_decada,
    ROW_NUMBER() OVER (PARTITION BY decada ORDER BY total_decada DESC) AS posicao
  FROM TotalPorDecada
)

SELECT
  nome,
  decada,
  total_decada,
  posicao
FROM NomesOrdenadosPorDecada
WHERE posicao <= 3 and decada >= 1950
ORDER BY decada asc, posicao;
```


## Laboratório Lambda

#### Imagem criada:
![image](/Sprint_6/Laboratórios/lab-lambda/Dockerfile%20-%20Repositório%20-%20D&A%20-%20Visual%20Studio%20Code%2005_10_2023%2014_58_24.png)

#### Container criado:
![image](/Sprint_6/Laboratórios/lab-lambda/Dockerfile%20-%20Repositório%20-%20D&A%20-%20Visual%20Studio%20Code%2005_10_2023%2015_05_36.png)

#### Execução de função sem a biblioteca pandas:
![image](/Sprint_6/Laboratórios/lab-lambda/funcao-lambda%20-%20Lambda%20-%20Opera%2005_10_2023%2014_13_57.png)

#### Camada criada:
![image](/Sprint_6/Laboratórios/lab-lambda/Lambda%20_%20us-east-1%20-%20Opera%2005_10_2023%2015_11_36.png)

#### Execução final da função bem-sucedida:
![image](/Sprint_6/Laboratórios/lab-lambda/Lambda%20_%20us-east-1%20-%20Opera%2005_10_2023%2015_15_56.png)

#### Layer configurada e aplicada na função:
![image](/Sprint_6/Laboratórios/lab-lambda/Lambda%20_%20us-east-1%20-%20Opera%2005_10_2023%2015_12_46.png)

## Excluindo Recursos

#### S3 removido
![image](/Sprint_6/Laboratórios/lab-s3/S3%20Management%20Console%20-%20Opera%2009_10_2023%2011_36_06.png)

#### Função Lambda removida
![image](/Sprint_6/Laboratórios/lab-lambda/AwsDataCatalog%20_%20Data%20sources%20_%20Athena%20_%20us-east-1%20-%20Opera%2009_10_2023%2011_32_46.png)

#### Database removida
![image](/Sprint_6/Laboratórios/lab-athena/AwsDataCatalog%20_%20Data%20sources%20_%20Athena%20_%20us-east-1%20-%20Opera%2009_10_2023%2011_29_40.png)