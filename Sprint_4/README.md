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

#### Gráfico em Setores
Dividir um circulo em setores proporcionais às frequências observadas nas categorias.  
Recomendável para observar algo em relação ao total.  
Usado com números de categorias pequenas.

#### Gráfico de Linhas
Para representar séries cronológicas de dados.  
Recomendado para representar séries temporais.

#### Histogramas
Colunas justapostas para representar distribuição de frequência em dados;  
No eixo horizontal temos os limites das classes de agrupamento.

### Medidas de Tendência Central
São aqueas conhecidas por indicarem um ponto em torno do qual se concentram os dados;  
A MTC podem ser calculadas a partir de dados populacionais (PARÂMETROS) ou a partir de dados amostrais (ESTIMADORES);

#### Média Aritmética
Soma de todos os valores observados da variável dividida pelo número total de observações.  
É o centro de gravidade que representa o ponto de quilíbrio de um conjunto de dados.

A soma dos desvios é sempre **ZERO** -> A soma da diferença de cada valor observado em relação à média é zero.

#### Moda
Maior frequência da variável entre os valores observados;
#### Mediana
Valor que ocupa a posição central dos dados ordenados;

#### Medidas Separatrizes
Medidas que dividem o conjunto de dados em partes iguais.  
Elas podem ser:
* Quartil: divide o conjunto de dados em 4 partes iguais;
* Decil: divide o conjunto de dados em 10 partes iguais;
* Percentil: divide o conjunto de dados em 100 partes iguais;

### Medidas de Dispersão
Permitem identificar até que ponto os resultados se concentram ou não ao redor da tendência central de um conjunto de dados observados.  
**Os dados apresentam semelhanças e variabilidades.**

As medidas de dispersão nos ajudam nas MTC para descrever melhor os dados.  
Indicam o quanto os dados estão ou não próximos uns dos outros.  
Precisamos tanto de uma MTC e MD para descrever de maneira adequada os dados.

#### Amplitude Total
Diferença entre o maior e o menor valor observado;  
Não leva em consideração dos dados intermediários;  
Não temos informações de como os dados estão distribuídos;  

#### Amplitude Interquartílica
Diferença entre o primeiro e o terceiro quantil;  
É uma média mais estável do que a amplitude total;  
Abrange 50% dos dados;  
É interessante para detectar valores discrepantes;

#### Desvio Médio
Diferença entre cada valor observado e a média;

A soma dos desvios é sempre igual a **zero**. Neste caso, precisamos tirar o módulo dos valores para que possamos ter um valor inteiro para realizar o cálculo do desvio médio (média das diferenças).

#### Variância e Desvio Padrão
* Variância: Soma dos quadrados dos desvios. (desvio médio ao quadrado, assim não precisamos tirar o módulo);
* Desvio Padrão: Retorna a dimensão original dos dados (Raiz quadrada da variância).

#### Coeficiente de Variação
Indica a variabilidade da medida em relação à média;

Permite comparar a dispersão de diferentes distribuições com diferentes médias e desvios padrões;

### Medidas de Assimetria
Importantes na construção de um histograma;  
Estamos interessados em saber a forma da distribuição dos dados;  
* **Coeficiente de assimetria:**  

##### Classificação das distribuições de frequências:
* Simétrica: (As = 0);
* Assimétrica negativa: (As < 0);
* Assimétrica positiva: (As > 0);

#### Medidas de Curtose
Quantifica a concentração ou dispersão os valores de um conjunto de dados em relação às medidas de tendência central;  
Mede o grau de achatamento de uma distribuição;  
Complementar às informações de disersão -> Kurtosis;

##### Classificação do grau de achatamento:
* Leptocúrtica: dados muito concentrados em torno do centro (k < 0.263>);
* Mesocúrtica: dados levemente cocnentrados no centro (k = 0.263);
* Platicúrtica: dados pouco concentrados em torno do centro (k > 0.263);
```  
K = 0,263
```

#### BoxPlot
Condensa várias informações sobre estatística descritiva;  
É um gráfico que utiliza cinco medidas estatísticas estudadas anteriormente:
* Valor mínimo;
* Valor máximo;
* Mediana;
* Primeiro Quartil;
* Terceiro Quartil;

![exemplo boxplot](/Sprint_4/img/bloxpot.png)

### Docker
#### O que é Docker?
É um software que reduz a complexidade de setup de aplicações;  
É onde configuramos containers, que são como um servidor para rodar asa nossas aplicações;  
Podemos criar ambientes independentes para rodar a aplicação e que funcionam em diversos SO's de maneira extremamente mais fácil;  
Ainda, deixa os projeto performáticos;  

#### Por que usar Docker?
* Ele proporciona mais velocidade na configuração do ambiente de um dev; 
* Gasta-se menos tempo em manutenção, containers são executados como configurados;
* É mais performático na execução de uma aplicação a uma Virtual Machine;
* Nos livra da **Matrix from hell**;

#### Conhecendo Matrix from hell
Dentro de um projeto maior, utilizamos diversos programas, linguagens de programação e softwares diferentes, *TODOS* rodando na máquina.  
Nesse caso, as tecnlogias devem ser instaladas em cada ambiente diferente da empresa, diversos computadores, máquinas diferentes. **Muito complexo**;  
Com o Docker, eu crio somente um ambiente e rodo eles em minhas máquinas. **Muito mais prático**.

#### O que é um Container?
É um pacote de código que pode executar uma ação, por exemplo: rodar uma aplicação em Python, PHP...  
Ou seja, os nossos projetos são criados dentro de containers que criamos/utilizamos;  
Containers usam imagens para serem executados.  
Múltiplos containers podem rodar juntos, como um para PHP e um para MySQL...

#### Container Vs Imagem
Ambos são conceitos fundamentais do Docker. Porém, imagem é o "projeto" que será executado pelo container, todas as instruções estarão declaradas nela. Já cointainer é o Docker rodando em alguma imagem, consequentemente executando algum código proposto por ela;  
Geralmente programamos uma imagem para executarmos por meio de um container;

#### Container Vs Virtual Machine
Container é uma aplicação que serve para um determinado fim, não possui sistema operacional e seu tamanha é de apenas alguns mbs.  
Enquanto isso, uma VM possui sistema operacional próprio, tamanho em gbs e pode executar diversas funções ao mesmo tempo.  

Containers gastam menos recursos ao passo que exercem algumas funções limitadas e específicas para um uso.  
Já uma VM gasta mais recursos do sistema na medida que é capaz de exercer diversas outras funções ao mesmo tempo.
#### Encontrando Imagens
Podemos encontrar as imagens referentes a alguma tecnologia(Node.js, Python, Js) no site [hub.docker.com](https://hub.docker.com);  

Executamos uma imagem por meio do comando:
```
docker run <imagem>
```

Ao iniciarmos um container podemos ver mais opções da mesmo a iterando:
```
docker run -it <imagem>
```

#### Verificar Containers Executados
Podemos verificar se um container está sendo rodada por meio do comando:
```
docker ps
```
```
docker container ls
```

Utilizando a flag "-a" observamos todos os caontainers que já foram executados:
```
docker ps -a
```
Isso é utíl para entender o que está sendo executado o o que está acontecendo em nosso ambiente;

#### Executando container com iteração
Ao iniciarmos um container com a flag -it podemos deixá-lo executando no terminal:
```
docker run -it <imagem>
```

#### Executando container em background
Quando icniciamos um container que persiste, ele fica ocupand o terminal;  
Podemos, assim, executar um container em background para não precisar ficar com diversas abas de terminal aberto. Para isso usamos a flag **-d**(detached);  
Também verificamos contaienrs em background por meio do "docker ps".

#### Expondo Portas
Os containers de docker não possuem conexão com anda de fora deles;  
Em razão disso, precisamos expor portas por meio da flag **-p**;  
Podemos uá-la da seguinte maneira:
```
-p 80:80
```
Deste modo, o container ficará disponível na porta 80.

#### Parando Containers
Podemos parar um container por meio do comando:
```
docker stop <id ou nome>
```
Desta maneira liberamos recursos que estão sendo gastos pelo mesmo.

#### Reiniciando Containers
Para voltar a rodar um container que foi parado com o "docker strop" usamos o comando:
```
docker start <id>
```

#### Definindo um nome para um Container
Definimos um nome do container com a flag **--name**;  
Caso não coloquemos nomes, receberemos um nome aleatório, o que é um problema para uma aplicação profissional.  
Esta flag é inserida juntamente com o comando **run**:
```
docker run -d -p 80:80 --name <nome> <imagem>
```

#### Acessando o Log de um Container
Podemos verificar o que aconteceu em um container co o seguinte comando:
```
docker logs <id>
```

#### Removendo um Container
Para remover um container da máquina que estamos executando o Docker usamos o seguinte comando:
```
docker -rm <id>
```
```
docker -rm -f <id>
```
No segundo caso, usamos a flag **-f** para forçar a remoção.

#### O que é uma Imagem?
São originadas de arquivos que programamos para que o Docker crie uma estrutura que execute determinadas ações em containers;  
Elas contém informações como: imagem base, diretório base, comandos a serem executados, porta de aplicação, etc.  
Ao rodar um container baseado em uma imagem, as instruções serão executadas em camadas.

#### Criando uma Imagem
Para criarmos uma imagem vamos precisar de um arquivo Dockerfile me uma pasta na qual ficará o projeto;  
Este arquivo vai precisar de algumas instruções para poder ser executado:
* FROM: imagem base;
* WORKDIR: diretório da aplicação;
* EXPOSE: porta da aplicação;
* COPY: quais arquivos precisasm ser copiados;

#### Executando uma Imagem
Precisamos, para executar uma imagem, primeiramente fazer o build por meio do comando:
```
docker build <dir da imagem>
```
Depois utilizamos o comando **run** para executá-la:
```
docker run <imagem>
```

#### Alterando uma Imagem
Sempre que alterarmos a imagem precisaremos fazer a build dela novamente;  
Para o Docker é como se ela fosse uma imagem completamente nova;  
Após o build por um outro id único criado juntamente ao comando **run**.

#### Camadas das imagens
As imagens do Docker são divididas em camadas;  
Cada instrução do DockerFile representa uma layer;  
Quando algo é atualizado apenas as layers depois da linha atualizada são refeitas;  
O resto permanece em cache, tornando o build mais rápido;

#### Download de imagens
Podemos fazer o download de alguma imagem do hub e deixá-la disponível em nosso ambiente;  
Vamos utilizar o comando:
```
docker pull <imagem>
```
Assim, caso se use em outro container, a imagem já estará pronta para ser utilizada;

**Com a flag *--help* teremos um leque de todas as opções disponíveis nos comandos**

#### Múltiplas aplicações
Podemos iniciar vários containers com uma mesma imagem para todos.  
Neste caso, as aplicações estarão funcionando em paralelo.  
Para testar isso, podemos determinar uma porta diferente para cada uma e rodar no moto detached.  

#### Nomeando imagens
Podemos nomear as imagens que criamos:
```
docker tag <id> <nome>
```
Também podemos modificar a tag, que seria como uma versão da imagem, uam outra versão.  

Para inserir uma tag utilizamos:
```
docker tag <id>:<nome>
```

#### Iniciando imagem com um nome
Podemos nomear nossa imagem já na criação da mesma por meio do uso da flag **-t**.  
Neste caso, podemos também adicionar nome **e** tag na sintaxe: **nome:tag**

Torna o processo de nomear imagens mais **simples**

#### Comando start Interativo
Podemos rodar nossa imagem com o comando "start" ao adicionarmos a flag **-it**. Assim, não é necessário usar o comando "run", que criaria outro container.
```
docker start -it <container>
```
#### Removendo Imagens
Podemos remover imagens por meio do comando:
```
docker rmi <imagem>
```
Imagens que no momento de remoção estão sendo usadas pelo container apresentarão uma mensagem de erro;

Ainda podemos utilizar a flag **-f** para forçar a ação de remoção da imagem.

#### Removendo Imagens e Containers
```
docker system prune
```
Com este comando, podemos remover imagens, containers e networks que não são utilizados.

Para essa ação, o sistema pedirá confirmação de usuário para realizar a remoção.

#### Removendo container após a utilização
```
docker run --rm <container>
```
Neste comando, iniciamos um container com o comando "run" e, após utilizá-lo, ele será automaticamente deletado.

#### Copiar Arquivos entre Containers
```
docker cp
```
Pode ser usado para copiar um arquivo de um diretório para um container, de um container para um diretório determinado ou entre containers divergentes.

#### Verificar Informações de Processamento
Verificar dados de execuçãoi de um container:
```
docker top <container>
```

#### Inspecionando Container
Podemos usar um comando para verificar informações diversas de um container, como: id, data de criação, imagem, etc...
```
docker inspect <container>
```
Com ele, entendemos como o container está configurado.

#### Verificando Processamento (Geral)
Para verificar os processos que estão sendo executados em um container, devemos utilizar o comando:
```
docker stats
```
Desta forma temos acesso ao andamento do processamento e a memória gasta pelo mesmo.

#### Autenticação no Docker Hub
Devemos nos autenticar com a conta do Docker Hub pelo terminal para podermos enviar imagens.  
Nos autenticamos pelo comando:
```
docker login
```

#### Logout do Docker Hub
```
docker logout
```

#### Enviando imagens para o Docker Hub
Para enviar imagens para o Hub usamos o comando:
```
docker push <imagem>
```
Antes de enviarmos a imagem, precisamos criar o repositório para a mesma no site do Hub.

#### Atualizando Imagens no Docker Hub
Precisamos:
* Fazer o build da imagem;
* Trocar a tag da imagem para a aversão atualizada;
* Fazer um push para o repositório;
  
Assim, todas as versões estarão disponíveis para serem utilizadas;

#### Utilizando a Imagem
Para baixar a imagem usamos:
```
docker pull <imagem>
```

Logo após, criamos um novo container com o comando:
```
dockar run <imagem>
```
E pronto! Estamos usamos a nossa própria imagem dentro de um container.