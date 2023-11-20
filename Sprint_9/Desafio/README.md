Diretório Desafio Compass Uol
==============================

## Tarefa 3: Processamento da Trusted

Nesta tarefa foram transformados os dados do csv "movies.csv" e dos dados pegos pela API do TMDB em arquivos parquet:

#### Job do CSV
Neste job o arquivo csv foi transformado em parquet e direcionado a uma pasta do S3 "desafio-aws-compass-lucas"
![image](Tarefa%203%20-%20Processamento%20Trusted/img/job_csv.png)

#### Dados salvos do CSV no S3
![image](Tarefa%203%20-%20Processamento%20Trusted/img/csv.png)

#### Job Genero
Neste job a coluna "genero" do csv foi "explodida" em uma outra tabela. Isso foi feito pois esta coluna era um array de gêneros, eu gostaria que cada gênero estivesse em uma linha da tabela para que futuramente se tornasse mais fácil a manipulação destes dados. Além disso, este código modificou os dados presentes do CSV no S3, filtrando os dados pelos filmes que possuem o gênero "Fantasy".

![image](Tarefa%203%20-%20Processamento%20Trusted/img/job_genero.png)

#### Dados salvos da tabela "genero" no S3
![image](Tarefa%203%20-%20Processamento%20Trusted/img/genero.png)

#### Dados do CSV modificados no S3
![image](Tarefa%203%20-%20Processamento%20Trusted/img/CSV_modificado_fantasy.png)

#### Job JSON
Neste Job os dados da API do TMDB salvos em Json foram transformados em arquivos parquet. Além disso, no mesmo job foi separado a coluna "produtores" em uma outra tabela pelos mesmos motivos da coluna "genero" do CSV, ela era um array de strings com os nomes dos produtores, então o explodi para que cada produtor estivesse em uma linha distinta da coluna. Assim, foi criado a tabela "producers" e a tabela com os dados do TMDB sem a coluna dos produtores.

É importante destacar que os dados do Json foram mapeados em um schema e transformados no código em seus devidos tipos, deste modo os dados não serão todos do tipo "string".

![image](Tarefa%203%20-%20Processamento%20Trusted/img/job_json.png)

#### Dados do TMDB salvos no S3
![image](Tarefa%203%20-%20Processamento%20Trusted/img/json_filmes.png)

#### Dados salvos da tabela "producers" no S3
![image](Tarefa%203%20-%20Processamento%20Trusted/img/json_produtores.png)

#### Crawlers
Foi utilizado os crawlers para que as tabelas fossem salvas no AWS Glue Data Catalog. Por ser uma ferramenta que já havia sido trabalhada durante a Sprint 7 achei que seria melhor salvas os databases e/ou tabelas criadas da Trusted por meio dele.

![image](Tarefa%203%20-%20Processamento%20Trusted/img/crawlers%20usados.png)

#### Dados salvos no Glue Data Catalog (tabelas)

![image](Tarefa%203%20-%20Processamento%20Trusted/img/dados_salvos_catalog.png)

## Tarefa 4: Modelagem da Refined

Nesta tarefa foi feito a modelagem dimensional dos dados que serão usados para a criação de insights, as tabelas realizadas na tarefa 5 foram criadas com base no seguinte modelo:

![image](tarefa%204%20-%20Modelagem%20Refined/img/diagramaDimensional2.png)

#### Criando as views de interesse para facilitar a análise

![image](tarefa%204%20-%20Modelagem%20Refined/img/views.png)

## Tarefa 5: Processamento da Refined

Nesta tarefa foram criadas as tabelas com base na modelagem dimensional feita para a refined.

#### Jobs feitos

Segue a imagem dos Jobs feitos, um para cada dimensão/fato do database "refined"

![image](Tarefa%205%20-%20Processamento%20Refined/img/Jobs_feitos_AWSGlue.png)

#### Job dimProdutores
Neste Job os dados que já foram separados dos produtores durante o processamento da trusted não sofrem alterações, somente as colunas são renomeadas.

![image](Tarefa%205%20-%20Processamento%20Refined/img/dimProdutores.png)

#### Job dimMovies
Neste Job os dados da tabela do CSV se juntam aos dados do TMDB para que os filmes pegos sejam somente os de interesse para a análise futura (somente os filmes cujo id está nos dados do TMDB). Assim, cria-se a tabela com os dados básicos dos filmes.

![image](Tarefa%205%20-%20Processamento%20Refined/img/dimMovies.png)

#### Job dimGenero
Neste Job a tabela "genero" feita na trusted passa por algumas mudanças, como renome de algumas colunas e refinamento dos dados para que os gêneros sejam somente dos filmes de interesse a serem analizados, semelhantemente ao que foi feito no dimMovies.

![image](Tarefa%205%20-%20Processamento%20Refined/img/dimGenero.png)

#### Job FatoFilmes
Neste job foram pegos os dados mutáveis para a composição da "fato", como o orçamento dos filmes, renda e popularidade. Além disso, foram coletados os id's de todas as dimensões por meio dos JOIN's realizados.

![image](Tarefa%205%20-%20Processamento%20Refined/img/fatofilmes.png)

#### Crawlers
Durante o processamento da refined foi optado o uso dos crawlers para que as tabelas fossem salves no Glue Data Catalog. Tentou-se salvar os dados em tabelas pelo próprio script do Job, mas vários erros ocorreram durante as tentativas. A solução foi realmente trabalhar com o que já era conhecido, os crawlers, que salvou os dados no Data Catalog.

![image](Tarefa%205%20-%20Processamento%20Refined/img/crawlers.png)

#### Dados salvos como tabelas no Glue Data Catalog

![image](Tarefa%205%20-%20Processamento%20Refined/img/tabelas_salvas_dataCatalog.png)

#### Dados da tabela salvos no S3
![image](Tarefa%205%20-%20Processamento%20Refined/img/dados_salvos_s3.png)