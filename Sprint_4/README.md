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

#### O que são Volumes?
São uma forma prática de persistir dados em aplicações e não depender de containers para isso;  
Todo dad ocriado por um container é salvo nele, quando o container é removido perdemos os dados;  
Precisaremos dos volumes para gerenciar os dados e também conseguir fazer backups de forma mais simples;

#### Tipos de Volumes
* Anônimos: Criados pela flag **-v**, porém com um nome aleatório;
* Nomeados: Volumes com nomes, referimo-nos a ele com facilidade;
* Bind mounts: Uma forma de salvar dados na nossa máquina, sem o gerenciamento do Docker, informamos um diretório para este fim;

#### O problema da Persistência de Dados
Se criamos um container com alguma imagem, todos os arquivos que geramos dentro dele serão do container;  
Quando o container foi removido, também removemos os nossos arquivos -> Por isso precisamos dos **Volumes**

#### Volumes Anônimos
```
docker run -v /data
```
Neste caso, o /data será o diretório que contém o volume anônimo;  
Este container estará atrelado ao volume anônimo;  
Com o comando "docker volume ls" poderemos ver todos os volumes existentes em nosso ambiente;  
```
docker volume ls
```

#### Volumes nomeados
Podemos criar um volume nomeado com o uso do seguinte comando:
```
docker run -v nomedovolume:/data
```
Agora o volume possui um nome e pode ser facilmente referenciado;  
Usado, assim como o anônimo, para armazenar dados;

#### Bind Mounts
Também é um volume, porém ele fica em um diretório que nós especificamos;  
Não criamos um volume em si, mas sim apontamos um diretório;  

O comando para criar um bind mount é:
```
docker run /dir/data:/data
```
Deste modo, o diretório /dir/data no nosso computador será o volume deste container;

#### Extra: BindMount
O Bind mount não serve somente para a criação de volumes;  
Podemos usar essa técnica para atualizar o nosso projeto em tempo real, sem precisar refazer o build a cada atualização do mesmo;  


#### Criando um Volume Manualmente

```
docker colume create <nome>
```
Desta forma temos um named volume criado, podemos atrelar a algum container na execução;

#### Listando todos os volumes 
```
docker volume ls
```

#### Inspecionando um Volume
```
docker volume inspect <nome>
```
Neste comando, temos acesso total ao local em que o volume guarda dados, nome, escopo, etc;  
O docker salva os dados dos volumes em algum diretório do nosso computador. Com esse comando podemos saber qual é;

#### Removendo um Volume
```
docker volume rm <nome>
```
Observe atentamente que quando removemos um volume também removeremos todos os dados a ele pertencentes

**OBS:** Podemos remover todos os volumes que não estão sendo utilizados com apenas um comando, evitando assim remover os volumes um a um;  
```
docker volume prune
```

#### Volume somente para leitura
Criação de um volume que possui somente permissão de leitura.  
Para efetuar esta configuração utilizamos o comando:
```
docker run -v volume:/data:ro
```
> ro = read only

#### O que são Networks?
São uma forma de gerenciar a conexão do Docker com outras plataformas ou até mesmo entre containers;  
As redes são criadas separadas dos containers, como os volumes;  
Além disso, existem alguns drivers de rede;  
Uma rede deixa simples a comunicação entre containers;

#### Tipos de Conexão
* Externa: Conexão com uma API de um servidor remoto;
* Com o Host: Comunicação com a máquina que está executando o Docker;  
* Entre Containers: Comunicação que utiliza o driver "bridge" e permite a comunicação entre dois ou mais containers;

#### Tipos de Drivers
* Bridge: O mais comum do Docker, utilizado quando containers precisam se conectar;  
* Host: Permite a conexão entre um container a máquina que está hosteando o Docker;
* macvlan: permite a conexão a um container por um MAC address;
* none: remove todas as conexões de rede de um container;
* plugins: permite extensões de terceiros para criar outras redes;

#### Listando Redes
Podemos verificar todas as redes do nosso ambiente com o comando:
```
docker network ls
```

#### Criando Redes
```
docker network create <nome>
```
Esta rede, quando não determinamos o tipo, será do tipo **bridge**

Usamos a flag **-d** para determinar o tipo de rede que iremos criar.
```
docker network create -d <tipo> <nome>
```
#### Removendo Redes
```
docker network rm <nome>
```

Para remover redes que não estamos utilizando de uma vez usamos o comando:
```
docker network prune
```

#### Conexões Externas
Os containers podem se conectar livremente ao mundo externo, como por exemplo a uma API de código aberto;

#### Conexão com o Host
Podemos também conectar um container com o host do Docker;  
Host é uma máquina que está executando o Docker;  
Como ip de host utilizamos: host.docker.internal;

#### Conexão entre Containers
Podemos estabelecer uma conexão entre containers: Usado, por exemplo, quando duas imagens distintas rodando em containers separados precisam se conectar para inserir um dado no banco;  
Neste caso, precisaremos de um rede **bridge** para efetuar a conexão;

#### Conectando um Container a uma Rede
Podemos conectar um container a uma rede por meio do comando:
```
docker network connect <rede> <container>
```

#### Desconectando um Container
Podemos também desconectar um container:
```
docker network disconnect <rede> <container>
```

#### Inspecionando Redes
```
docker network inspect <nome>
```
#### O que é YAML?
É uma linguagem de serialização, seu nome é YAML ain't Markup Language;  
É usada geralmente para arquivos de configuração, incluindo o Docker na hora de configurar  o Docker Compose;  
* De fácil leitura para o ser humano;
* Extensão: .yml ou .yaml;

#### Criando o arquivo YAML
O arquivo .yaml possui chaves e valores, os qusi são de onde iremos retirar as configurações do nosso sistema;  
Para definir uma chave apenas devemos inserir o nome dela, em seguida colocamos dois pontos e depois o valor;

#### Espaçamento e Indentação
O fim de uma linha significa o final da instrução. Neste caso, não usamos ponto e vírgula;  
A indentação se dá com um ou mais espaços. Não usamos **TAB**;  
Cada uma define um bloco;  
O espaço é obrigatório após a declaração das chaves;

#### Comentários do YAML
Usamos o **#** para usar comentários;

#### Dados numéricos YAML
* Inteiros: 18
* Floats: 15.7

#### Strings YAML
Podemos usar strings tanto com aspas duplas quanto sem aspas nenhuma.

#### Dados nulos YAML
Podemos colocar um valor nulo (None) dentro do YAML tanto com o valor "null" quanto com o símbolo "~"

#### Booleanos
* True ou On;
* False ou Off;

#### Arrays
Temos duas sintaxes para o uso das listas no YAML:
```
items: [1, 2, 3, 4, 5]
```
```
items:
  - 1
  - 2
  - 3
  - 4
```

#### Dicionários no YAML
Sintaxes:
```
obj: {a: 1, b: 2, c: 3}
```
```
objeto:
  chave: 1
  chave: 2
```

#### O que é Docker Compose?
É uma ferramenta para rodar múltiplos containers;  
Temos apenas um arquivo de configuração, que orquestra totalmente esta situação;  
É essencial para projetos maiores;

#### Criando arquivo compose
Primeiro: Criar arquivo docker-compose.yml na raiz do projeto -> Responsável por coordenar containers e imagens;  
* version: versão do compose; 
* services: Containers/serviços que vão rodar nessa aplicação;
* volumes: Possível adição de volumes;

#### Rodando o Compose
```
docker compose up
```
Assim, as instruções do arquivo serão executadas.

#### Compose em Background
O compose pode ser executado em modo detached. Para isso, utilizamos a flag **-d** no comando.  
Deste modo, os containers estarão rodando em background;

#### Parando Compose
```
docker compose down
```

#### Variáveis de Ambiente no Compose
Como definir uma variável de ambiente: Definindo um arquivo base em env_file;  
As variáveis podem ser chamadas pela sintaxe: ${VAR}  
Útil quando o dado a ser inserido é sensível;
#### Redes no Compose
O compose cria um rede básica Bridge entre os containers pertencentes à aplicação;  
Além disso, podemos isolar as redes com a chave networks. Assim poderemos conectar apenas os containers que optarmos.

#### O que é Orquestração de Containers?
É o ato de conseguir gerenciar e escalar os containers da nossa aplicação;  
Temos um serviço que rege sobre outros serviços, verificando se os mesmo estão funcionando como deveriam;  
Desta forma conseguimos garantir uma aplicação saudável e também que estaja sempre disponível;
#### O que é Docker Swarm?
Uma ferramenta do Docker que serve para orquestrar containers. Nela, podemos escalar horizontalmente nossos projetos de maneira simples.  

A facilidade do Swarm para outros orquestradores é que todos os comandos são muito semelhantes ao do Docker;
#### Conceitos Fundamentais do Swarm
* Nodes: É uma instância que participa do Swarm;
* Manager Node: Node que gerencia os demais Nodes;
* Worker Node: Nodes que trabalham em função do Manager;
* Service: Um conjunto de tasks que  o Manager Node manda o Work Node executar; 
* Task: Comandos que são executados nos Nodes;
#### Formas de Executar o Swarm
Para executar o Swarm precisaremos de mais máquinas. Para isso, temos algumas soluções:
* AWS;
* Docker Labs;

#### Iniciando o Swarm
```
docker swarm init
```
Em alguns casos em que formos iniciar o Swarm precisaremos especifinar o IP com a flag **--advertise-addr**

#### Listando Nodes Ativos
```
docker node ls
```
Deste modo, poderemos monitorar o que o Swarm está orquestrando;

#### Adicionando Máquinas ao Swarm
```
docker swarm join --token <TOKEN> <IP>:<PORTA>
```
Com o uso deste comando, duas máquinas estarão conectadas. Deste modo, a nova máquina entrará na hierarquia como Worker.

#### Subindo um novo Serviço
Iniciamos um novo serviço por meio deste comando:
```
docker service create --name <nome> <imagem>
```

Por meio disso adicionaremos um novo container ao nosso Manager;

#### Verificar Serviços rodando no Swarm
```
docker service ls
```
Assim os serviços serão exibidos bem como algumas informações importantes sobre os mesmos: nome, replicas, imagem, porta;

#### Removendo Serviços
```
docker service rm <nome>
```
Para de rodar o serviço selecionado;

#### Replicando Serviços
Podemos iniciar um determinado serviço já contendo um número maior de réplicas por meio do comando:
```
docker service create --name <NOME> --replicas <NUMERO> <IMAGEM>
```

#### Checando o Token do Swarm
```
docker swarm join-token manager
```

Checamos o token pelo próprio terminal.

#### Removendo instância Swarm
Podemos parar de executar uma instância Swarm por meio do comando:
```
docker swarm leave
```

#### Removendo um Node
```
docker node rm <ID>
```
Com este comando, a instância não será considerada mais um Node, saindo do Swarm.

#### Inspecionando Serviços
```
docker service inspect <ID>
```

#### Verificando quais Containers estão rodando
```
docker service ps <ID>
```
Receberemos uma lista dos containers que estão rodando e daqueles que já receberam baixa;

#### Compose no Swarm
Usaremos nesta situação os comandos de Stack:
```
docker stack deploy -c <ARQUIVO.YAML> <NOME>
```
Assim teremos um arquivo compose sendo executado.

#### Replicando no Stack
```
docker service scale <NOME>=<REPLICAS>
```

#### Como parar de receber Tasks
Podemos fazer com que um serviço pare de receber as ordens do Manager por meio do referido comando;
```
docker node update --availability drain <ID>
```

#### Atualizando uma imagem no Swarm
```
docker service update --image <IMAGEM> <SERVIÇO>
```

#### Criando Redes para serviços no Swarm
A conexão entre instâncias usa um driver diferente chamado "overlay"  
Podemos criar uma rede com:
```
docker network create
```
e depois ao criar um service adicionar a tag: 
```
--network <REDE>
```
para inserir as instâncias na nossa nova rede.

#### Conectando um serviço a uma rede existente
```
docker service update --network <REDE> <NOME>
```

#### O que é Kubernetes?
É uma ferramenta de orquestração de containers. Permite a criação de múltiplos containers em diferentes máquinas (nodes);  
Ela gerencia serviços, garantindo que as aplicações sejam executads sempre da mesma forma.

#### Conceitos Fundamentais - Kubernetes
* Control Plane: Onde é gerenciado o controle dos processos dos Nodes;
* Nodes: Máquinas que são gerenciadas pelo Control Plane;
* Deployment: A execução de uma imagem/projeto em um Pod;
* Pod: Um ou mais containers que estão em um Node;
* Services: Serviços que expõe os Pods ao mundo externo;
* Kubectl: Cliente de linha de comando para o Kubernetes;

#### Inicializando Minikube
```
minikube start --driver=<DRIVER>
```
Onde o driver vai depender de como foi sua instalação das dependências, seja por virtualbox, hyper-v ou docker.

Podemos testar o minikube com:
```
minikube status
```
#### Encerrando Minikube
```
minikube stop
```
#### Acessando a DashBoard
O minikube nos disponibiliaza uma dashboard e nela podemos ver todo o detalhamento de nosso projeto: Serviços, Pods, etc.  
A acessamos por meio do comando:
```
minikube dashboard
```
Ou ainda usamos este comando com a flag **--url** para apenas obter a URL.
#### Deployment
É uma parte fundamenta ldo Kubernetes. Com ele, criamos nosso serviço que vai rodar nos Pods;  
Definimos uma imagem e um nome para posteriormente ser replicado entre os servidores.  
A partir da criação do deployment teremos containers rodando.

#### Criando o Deployment
```
kubectl create deployment <Nome> --image=<Imagem>
```
#### Verificando Deployment
Para verificar o Deployment usamos o comando:
```
kubectl get deployments
```
E para receber mais detalhes dos mesmos utilizamos:
```
kubectl describe deployments
```
Com estes comandos saberemos se o projeto está de fato rodando e o que está rodando nele.
#### Checando Pods
Os pods são componentes nos quais os containers realmente são executados.  
Para verificar um Pod usamos:
```
kubectl get pods
```
E para receber mais detalhes:
```
kubectl describe pods
```
#### Configurações do Kubernetes
```
kubectl config view
```

#### Services
Possibilita expor os Pods para o mundo externo.  
Os Services são uma entidade separada dos Pods, que os expõe eles a uma rede.
#### Criando um Service
```
kubectl expose deployment <NOME> --type=<TIPO> --port=<PORT>
```

#### Gerando um IP para o Service
```
minikube service <NOME>
```
#### Detalhes do Service
Podemos usar o seguinte comando para obter detalhes os services já criados:
```
kubectl get services
```
#### Escalando Aplicação
```
kubectl scale deployment/<NOME> --replicas=<NUMERO>
```

#### Verificando o número de Réplicas
```
kubectl get rs
```

#### Diminuir número de Réplicas
```
kubectl scale deployment/<Nome> --replicas=<NUMERO_MENOR>
Colocando um número menor do que o número de réplicas existentes, o mesmo será reduzido.
```

#### Atualização de Imagem
```
kubectl set image deployment/<NOME> <NOME_CONTAINER>=<NOVA_IMAGEM>
```

#### Desfazendo Alterações
Verificando alterações:
```
kbectl rollout status deployment/<NOME>
```

Voltar a alteração(desfazer):
```
kubectl rollout undo deployment/<NOME>
```

#### Deletando Services
```
kubectl delete service <NOME>
```
#### Deletando Deployments
```
kubectl delete deployment <NOME>
```
#### Modo Declarativo
Até o momento passado estávamos trabalhando com o modo imperativom onde iniciamos a aplicação com comandos.

O modo declarativo é guiado por um arquivo semelhantemente ao Docker Compose. Desta forma tornamos as nossas configurações mais simples e centralizamos tudo em um comando, apenas.

#### Chaves mais usadas no modo declarativo:
* apiVersion: Versão utilizada da ferramenta;
* Kind: tipo do arquivo (Deployment, Service);
* metadata: Descrever algum objeto, inserindo chaves como name;
* replicas: número de réplicas de Nodes/Pods;
* containers: Definir as especificações de containers como: nome e imagem;

#### Executando Arquivo Deployment
```
kubectl apply -f <ARQUIVO>
```

#### Parando o Deployment
```
kubectl delete -f <ARQUIVO>
```

#### Executando o serviço (service)
```
kubectl apply -f <ARQUIVO>
```

#### Parando o Serviço
```
kubectl delete -f <ARQUIVO>
```

#### Atualizando o Projeto
1. Criar uma nova versão da imagem;
2. Fazer o push para o Hub;
3. Alterar a tag no arquivo de Deployment;
4. Reaplicar o comando de Apply;
#### Unindo Arquivos
Em um mesmo arquivo podemos ter o nosso Deployment e Service, ocorrendo a separação por meio de "---".


## Certificados:
![estatistica](/Sprint_4/Estatística_python/Certificado/Certificado%20de%20conclusão%20Estatística%20com%20Python.jpg)

![docker](/Sprint_4/Docker/Certificado/Certificado%20de%20Conclusão%20Docker.jpg)