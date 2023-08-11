Diretório SQL para Análise de Dados
===================================
### Diretório dedicado aos conteúdos abordados no curso "SQL para Ançaíse de Dados: Do básico ao avançado" - Sprint 2;

## Resumo
### Comandos básicos

- ### SELECT
Comando usado para selecionar as colunas de tabelas

	select coluna_1, coluna_2, coluna3 from schema_1.tabela_1
Devemos separar colunas por vírgulas quando selecionarmos mais de uma;  
Podemos usar o "*" para selecionar todo o conteúdo da tabela;  

- ### DISTINCT
Usado para remover linhas duplicadas e mostrar somente linhas distintas;  

	select distinct coluna_1, coluna_2, coluna_3
	from schema_1.tabela_1
Se mais de uma colina for selecionada, o comando "SELECT DISTINT" irá retornar todas as combinações distintas;  

- ### WHERE
Usado para filtrar linhas de acordo com uma condição

	select coluna_1, coluna_2, coluna_3
	from schema_1.tabela_1
	where condição_x=true
No PostgreSQL são utilizadas aspas simples para delimitar strings: 'Texto'
Pode-se combinar mais de uma condição utilizando os operadores lógicos...
No PostgreSQL as datas são escritas no formato 'YYYY-MM-DD' ou 'YYYYMMDD'

- ### ORDER BY
Comando usado para ordenar a seleção de acordo com uma regra defenida pelo usuário;

	select coluna_1, coluna_2, coluna_3
	from schema_1.tabela_1
	where condição_x=true
	order by coluna_1
Por padrão, esse comando ordena em ordem crescente, para usar o decrescente use o comando: DESC  
Em strings, a ordenação padrão é em ordem alfabética  

- ### LIMIT
Comando usado para limitar o n° de linhas da consulta -> Explorar dados;

	select coluna_1, coluna_2, coluna_3
	from schema_1.tabela_1
	limit N
Usado principalmente com o ORDER BY para situações como: TOP "n" pamentos mais recentes, produtos mais caros...

### Operadores aritmédicos
Realizam operações matemáticas. 

    1. Adição: +
    2. Subtração: -
    3. Multiplicação: * 
    4. Divisão: /
    5. Módulo: %
    6. Exponencial: ^
    7. OU: || -> Para strings (não é operador aritmédico)

Podemos "nomear" colunas novas usando "as"  
Ex:

	(current_date - birth_date) / 365 **as** age -> Este comando pega a data atual, subtrai da data de aniversãrio salva no banco de dados, divide por 365 (calculando a idade da pessoa). Logo, demos o nome da coluna de "age".
Usamos aspas duplas para nomes de colunas para mostrar que tudo, mesmo com espaços, é o nome da coluna.  
O operador "||" em strings irá concatener as strings: 'eduardo' || 'carlos' = eduardocarlos.

### Operadores de comparação
Comparam dois valores e retornam TRUE ou FALSE;  
Usado em conjunto com o WHERE para filtrar linhas de uma seleção;  

    1. = IGUAL
    2. > MAIOR
    3. < MENOR
    4. <= MENOR OU IGUAL
    5. >= MAIOR OU IGUAL
    6. <> DIFERENTE

Usados também para criarem colunas "flag" que retornam TRUE ou FALSE;

### Operadores lógicos
Unir expressões simples em compostas;  

	1. AND: Verificação se ambas são verdadeiras, se uma for falsa, o resultado será FALSE;
	2. OR: Vaerificação se pelo menos uma é verdadeira, assim o resultado será TRUE;
	3. NOT: Inverte o valor, se é TRUE, vira FALSE;
	4. BETWEEN: Verifica quais valores estão dentro do range definido;
	5. IN: Funciona como múltiplos OR'S, se algo está dentro de...;
	6. LIKE: Compara textos e é sempre utilizado em conjunto com o "%", que funciona indicando que qualquer texto pode aparecr no lugar do campo definido;
	7. ILIKE: Igual o Like, mas ignora se o campo tem letras maiúsculas ou minúsculas na comparação;
	8. IS NULL: Verifica se o campo é nulo;

### Funções agregadas
Funcionam para executar operações aritméticas nos registros da coluna;

	1. COUNT()
	2. SUM()
	3. MIN()
	4. MAX()
	5. AVG()

> Funções agregadas não consideram o valor "null" como 0;  
> Na função COUNT() podemos usar o "*" para contar os registros;  
> COUNT(DISTINCT) mostrará somente valores exlusivos;  
> Podemos usar uma linha de código em outro código (subqueries -> serão vistas mais adiante);  

- ### GROUP BY
Agrupa os registros semelhantes de uma coluna;  
O GROUP BY usado sozinho, sem funções de agregação, funciona como um DISTINCT, que elimina as linhas duplicadas;  
Também se pode referenciar a coluna no "group by" de maneira ordinal, ou seja, por números, de acordo com a posição que estão no respectivo select;  

- ### HAVING
Filtra as linhas da seleção por uma coluna agrupada;  
Tem a mesma função do WHERE. mas pode ser utilizado para filtrar os resultados das funções agregadas;  
O HAVING também pode filtrar colunas não agregadas;  

### JOIN's
Combinam colunas de uma ou mais tabelas; 

	select t1.coluna_1, t1.coluna_1, t2.coluna_1, t2.coluna_2
	from schema.tabela_1 as t1
	ALGUM join schema.tabela_2 as t2
    	on condição_de_join

Tipos de Join's:  
  * LEFT JOIN: Toma como referência a tabela à esquerda, pegando todos os dados. Equanto pegamos apenas os elementos da tabela direita que batem com as da esquerda;  
  * INNER JOIN: Pega apenas os dados que existem tanto na tabela da esquerda quanto da direita;  
  * RIGHT JOIN: Toma como referência os dados da tabela da direita e pega somente os dados da tabela esquerda que correspondam aos da direita;  
  * FULL JOIN: Pega todos os dados, tanto da tabela da direita quanto da esquerda e os unem;


O uso do comando "join" sozinho funciona como "inner join" -> Pega as informações que existem em todas as colunas.

### Unions
Usado para "colar" uma tabela sobre a outra, desde que as tabelas tenham a mesma quantidade de colunas e essas colunas possuam o mesmo tipo de unidade;  
*Se* você possui duas colunas com 10 linhas e **todas** são numéricas, você pode usar o comando "union", por exemplo;  

#### UNION ALL
Realiza sua função citada anteriormente, mas não elimina linhas duplicadas;

#### UNION
Remove linhas iguais/duplicadas;
## Certificado
![Image](Certificado/Certificado%20de%20conclusão%20SQL%20para%20análise%20de%20dados.jpg)