Diretório Sprint #4
===================
### Este diretório está dedicado aos conteúdos trabalhados durante a Sprint 4 do programa de bolsas D&A da Compass UOL
-------------------

## Resumo
### Programação Funcional
É o processo de construir software através da composição de funções puras, evitando compartilhamento de estados, dados mutáveis e efeitos colaterais. É declarativa ao invés de Imperativa. - ***Eric Elliot***

O paradigma funcional foi criado com base num método de solução matemático, com criação de funções que são utilizadas para lidar com abstrações e aplicou no desenvolvimento de sistemas.

### Conceitos Fundamentais
#### Composição de Função
Criação de uma função através da composição de outras funções.
##### Ex:
```js
const numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros.filter((numero) => numero % 2 === 0).map((numero) => numero * 2) 
// [ 4, 8, 12, 16, 20 ]
```
#### Funções Puras
Quando "invocamos" uma função mais de uma vez e produz o mesmo resultado. O retorno da função é sempre o mesmo quando passados os mesmos parâmetros. Ou seja, ela independe de valores mutáveis
##### Ex:
```js
const verfica_se_e_maior_que = (entrada1, entrada2) => entrada1 >= entrada2;
```

#### Imutabilidade
Uma variável recebeu um valor o possuirá para sempre. Um objeto não pode ser modificado (constantes).
##### Ex:
```js
const sobreNome = "Silveira"
sobreNome.replace("Silveira", "Souza") //'Souza'
sobreNome //'Silveira'
```

#### Efeito Colateral
Todo tipo de interação da nossa função com o "mundo externo". Como fazemos interface com o mundo real, é praticamente impossível que não hajam efeitos colaterais em nossas funções. Assim, algumas partes de nossas funções vão ser impuras.  
Deste modo, temos o objetivo de minimizar as impurezas e separá-las do resto de nosso programa.

#### Imperativo Vs Declarativo
Ao invés de programarmos de forma imperativa, ou seja, determinando(exigindo) que seja realizado um código para uma determinada função; programamos códigos na programação funcional de maneira **declarativa**, onde declaramos aquilo que queremos em nosso código sem explicitar como será feito.

#### Estado Compartilhado
Qualquer valor que está acessível por mais de um ponto de uma aplicação.
#### Ex:
```js
const idade = 31
const calculaIdadeDosIrmaos = ( idadeIrmao ) => idade + idadeIrmao 
```
A função calculaIdadeDosIrmaos() utiliaz uma variável externa que não depende dos parâmetros passados.

### Programação Funcional no Python
Em se tratando do Python, temos diversas ferramentas conhecidamente de linguagens funcionais, como:
* **First Class Functions:** A linguagem consegue trabalhar funções como dados, armazenar uma função em uma variável;
* **High Order Functions:** Uma função consegue retornar outra função e consegue receber outra função em seus parâmetros
* **Anonymous Functions:** Lambda; Funções usadas muitas vezes para reuso de memória/espaço. Para determinadas ações específicas, economizam **muito** código;  
    **Map** -> Usado para mapear elementos de, por exemplo, uma lista, e retorná-los em outra lista com algum nível de modificação, não mexendo no valor (lista) original;  
    **Filter:** -> Usado para filtrar uma lista de acordo com um certo parâmetro definido;
* **Closure:** Uma função possui o conhecimento sobre o seu redor, entendimento do lugar onde está escrita;
* **Recursion:** Uma função que chama a ela mesma dentro de si;
* **Immutability:** Um dado criado é imutável em seu conteúdo;
* **Lazy Evaluation:** Deixar o processamento somente para quando ele for realmente necessário;

### Estatística Descritiva em Python
A estatística está subdividida em três partes:
* Descritiva: Coleta, análise e interpretação dos dados de uma maneira geral;
* Probabilística: Já temos informações sobre os dados e precisamos criar modelos para representar os dados;
* Inferencial: As amostras de dados podem ser representativas de um todo envolvido;

#### A importância da Estatística para Data Science
Relacionada ao advento do Big Data: Grandes dados sendo gerados diariamente precisando ser tratados e transformados em informação.  
A estatística entra para a análise e interpretação destes dados.

#### Contexto Geral: Estatística
É uma ciência ramo da matemática aplicada que fornece métodos para coletar, descrever, analisar, apresentar e interpretar dados, para a utilização dos mesmos na tomada de decisões.  
Ela é importante para: Coletar, apresentar e interpretar conjuntos de dados.  
"Estatística" se refere a teoria e método no qual os dados serão analisados, enquanto "estatística**s**" são as próprias estatísticas descritivas obtidas dos dados em estudo.

### Fundamentos da Estatística
Medidas e imprecisões do mundo: Estatística;  
O que significa isso? A matemática é uma ciência **exata**, porém, levando em consideração o nosso mundo mutável e imprevisível, os dados analisados e as ações que encontraremos em nosso trabalho poderão ser incertos, não completamente exatos.

#### **Aleatoriedade**
Se não houvesse aleatoriedade/incertezas na vida, não haveria estatística no mundo, seria algo completamente exato, e sabemos que a vida não é assim.

Os paradigmas de mundo que englobam a nossa sociedade atual foram estudados e estruturados em uma classificação: **Mundo VUCA**, que já foi estudado em Métodos Ágeis de A a Z.

##### Fenômenos Aleatórios:
* Mundo VUCA;
* Incertezas da vida;
* Muitos riscos;
* A intuição humana vai a passos contrários a estatística;
* Na ciência não conseguimos comprovar definitivamente tudo com certeza, em tudo existem incertezas e riscos;

#### População Vs Amostra
* População: São todos os elementos - indivíduos, itens ou objetos - cujas as características estejam sendo estudadas. É o conjunto de todos os elementos de dados.
* Amostra: É uma parte coletada específica a partir da população.
* Censo: É um conjunto de características obtidas de todos os membros da população. Ex: IBGE.

##### Como tornar a minha amostra o mais fiel possível da minha população?
Eu preciso coletar informações sobre a minha população da maneira mais aleatória possível. Não podemos simplesmente pegar dados e informações sobre uma região bem sucedida de uma cidade e ignorar a periferia, os dados não serão minimamente concretos.

#### Medidas Observadas e Variáveis
Os dados são simplesmente valores coletadas por meio da observação e medição. Para que possamos extrair valor deles, precisamos analisá-los e transformá-los em informações.
##### Produção dos Dados:
* Dados Primários: Coletados por quem faz a análise; são mais confiáveis; possuem maior controle;
* Dados Secundários: Coletados por terceiros; não sao muito confiáveis e possuem menor controle;

##### Observação
É uma ocorrência de um item de dados específico que é gravada sobre uma unidade de dados;

##### Variável
É a característica de interesse que é medida em cada elemento da amostra ou população. Seus valores variam de elemento para elemento. As variáveis podem ter valores numéricos ou não numéricos.

### Representações Gráficas
**Por que devemos usar os dados?** Eles representam melhor, de maneira mais dinâmica um grande números de dados e, além disso, já extrair informações e valores a partir somente da análise dos mesmos.

##### Em um gráfico precisamos ter:
* Simplicidade;
* Clareza;
* Veracidade;

#### Gráfico em Barras
Servem para variáveis qualitativas;  
**Objetivos:**
* Comparar  grandezas entre categorias;
* Categorias com designações extensas;

**Em gráficos de colunas, as categorias possuem designações menores**
**Ex:**
![imagem](/Sprint_4/img/Drivers-de-aumento-de-eficiencia-com-grafico-de-barras-horizontais-2.png)

