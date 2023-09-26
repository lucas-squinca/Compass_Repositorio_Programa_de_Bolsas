Diretório Sprint #6
===================
Este diretório possui por finalidade armazenar os conteúdos trabalhados durante a Sprint 6 do programa de bolsas D&A - CompassUol.

## Análise de Dados
Análise é a avaliação sistemática de dados. Análise de dados é o processo analítico específico sendo aplicado.

A análise de dados é vital para empresas de pequeno e grande porte. Os processos analíticos de dados são combinados para criar soluções de avaliação de dados, que ajudam as empresas a decidir onde e quando lançar novos produtos, quando oferecer descontos e quando comercializar em novas áreas. Sem os dados fornecidos por análise de dados, muitos responsáveis por tomar decisões se baseariam em intuição e pura sorte. 

À medida que as empresas começam a implementar soluções de avaliação de dados, surgem desafios. Esses desafios são baseados nas características dos dados e das análises necessárias para o caso de uso dessas empresas. No passado, esses desafios foram definidos como desafios de “big data”. Entretanto, no ambiente atual baseado na nuvem, esses desafios podem se aplicar a conjuntos de dados pequenos ou lentos quase tão frequentemente quanto a conjuntos de dados muito grandes e rápidos.

### Benefícios da Análise de Dados para as Empresas
* Personalização do Cliente;
* Detecção de Fraudes;
* Detecção de Ameaças à Segurança;
* Comportamento do Usuário;
* Modelagens e Previsões Financeiras;
* Alertas em Tempo Real;

### Componentes de uma Solução de Avaliação de Dados
![image](/Sprint_6/img/JUNRpZlWkHO_VIT3_pROjjmyRC5Wj3iiz.png)

## Origem dos Dados
A maioria dos dados ingeridos por soluções de avaliação de dados provem bancos de dados e armazenamentos de arquivos existentes on-premises. O estado desses dados costuma exigir processamento mínimo na solução.

Os dados de streaming são uma fonte de dados de negócios cada vez mais popular. Essa fonte é menos estruturada. Pode ser necessário usar programas especializados para coletar os dados e aplicativos de processamento específicos para agregá-los e analisá-los corretamente quase em tempo real.

Conjuntos de dados públicos são outra fonte de dados para as empresas. Essa fonte conta com dados de censo, dados de saúde, dados populacionais e muitos outros conjuntos de dados que ajudam as empresas a compreender os dados sendo coletados sobre seus clientes. Pode ser necessário transformar esses dados para que contenham apenas aquilo de que a empresa precisa.

## Volume
### Crescimento exponencial de dados de negócios

As empresas armazenam dados há décadas, isso não é novidade. O que mudou nos últimos anos foi a capacidade de analisar determinados tipos de dados.

Há três classificações amplas de tipos de origem dos dados:

* Dados estruturados são organizados e armazenados na forma de valores que são agrupados em linhas e colunas de uma tabela.
* Dados semiestruturados muitas vezes são armazenados em conjuntos de pares de chave-valor que são agrupados em elementos em um arquivo.
* Dados não estruturados não são estruturados de forma consistente. Alguns dados podem ter uma estrutura semelhante a dados semiestruturados, mas outros podem conter apenas metadados.

O conjunto de dados coletados estão cada vez maiores! Plataformas modernas de gerenciamento de dados devem capturar dados de diversas fontes em velocidade e escala. Os dados precisam ser reunidos em repositórios gerenciáveis e centrais, dividindo os silos tradicionais. Os benefícios da coleta e avaliação de todos os dados de negócios devem superar os custos.

## Como Armazenar Dados
### Amazon Simple Storage Service (S3)
Serviço de armazenamento de objeto/dados, ou seja, armazena qualquer tipo de arquivo.  
É durável e flexível quanto a quantidade de arquivos que podem ser armazenados.

**Bucket** são como pastas de arquivos, mas maiores.

O Amazon S3 é o armazenamento para a internet. Esse serviço foi projetado para facilitar a computação em escala web para os desenvolvedores. O Amazon S3 fornece uma interface simples de serviços da web que pode ser usada para armazenar e recuperar qualquer quantidade de dados, a qualquer momento e a partir de qualquer lugar. O serviço concede acesso a todos os desenvolvedores à mesma infraestrutura altamente escalável, confiável, segura, rápida e econômica que a Amazon utiliza para executar sua própria rede global de sites. O serviço tem como objetivo maximizar os benefícios de escala e repassar esses benefícios para os desenvolvedores.

Os benefícios do Amazon S3 são:

- Armazenamento de qualquer coisa;
- Armazenamento seguro de objetos;
- Acesso HTTP nativamente on-line;
- Escalabilidade ilimitada; 
- Durabilidade de 99,999999999%

#### Conceitos S3
* Objeto:  é composto por um arquivo e quaisquer metadados que descrevam esse arquivo. Para armazenar um objeto no Amazon S3, você faz o upload do arquivo que deseja armazenar no bucket. Ao fazer o upload de um arquivo, você pode definir permissões no objeto e adicionar metadados.
* Buckets: são contêineres lógicos para objetos. Você pode ter um ou mais buckets em sua conta e controlar o acesso a cada um individualmente. Você controla quem pode criar, excluir e listar objetos no bucket. Você também pode visualizar logs de acesso do bucket e seus objetos e escolher a região geográfica onde o Amazon S3 armazenará o bucket e o respectivo conteúdo.
* Chave de objeto: é um identificador exclusivo de um objeto em um bucket. Como a combinação de um bucket, chave e ID de versão identifica exclusivamente cada objeto, você pode considerar o Amazon S3 como um mapa de dados básico entre “bucket + chave + versão” e o próprio objeto. Cada objeto no Amazon S3 pode ser endereçado exclusivamente pela combinação de endpoint de serviço web, nome de bucket, da chave e, opcionalmente, a versão.

#### Solução de avaliação de dados no Amazon S3
* Arquitetura de dados centralizada;
* Integração com serviços AWS sem cluster e sem servidor;
* Interfaces de programação de aplicativo (API's) padronizadas;
* Desacoplamento entre o armazenamento e o processamento de dados;

### DataLakes (revisão Sprint #2)
Os data lakes prometem armazenar todos os dados de uma empresa em um único repositório. Você pode aproveitar os data lakes para armazenar grandes volumes de dados em vez de manter esses dados em data warehouses. Os data lakes, como os criados no Amazon S3, geralmente têm custo inferior às soluções especializadas de armazenamento de big data. Dessa forma, você paga apenas pelas soluções especializadas ao usá-las para processamento e análise, e não para armazenamento de longo prazo. Sua extração, transformação e carregamento (ETL) e o processo analítico ainda podem acessar esses dados para análise.

#### Benefícios DataLakes
* Fonte única de confiança;
* Armazene qualquer tipo de dados, independentemente da estrutura;
* Pode ser analizado por meio da I.A e machine learning;

#### Benefícios de um datalake na AWS
* São uma solução de armazenamento de dados econômica. Você pode armazenar de forma durável uma quantidade quase ilimitada de dados usando o Amazon S3.
Implemente a segurança e a conformidade líderes do setor. A AWS usa rigorosos mecanismos de segurança, conformidade, privacidade e proteção de dados.
* Permite que você aproveite muitas ferramentas diferentes de coleta e ingestão de dados para ingerir dados em seu data lake. Esses serviços incluem o Amazon Kinesis para dados de streaming e dispositivos AWS Snowball para grandes volumes de dados locais.
* Ajudam você a categorizar e gerenciar seus dados de forma simples e eficiente. Use o AWS Glue para entender os dados dentro do seu data lake, prepará-los e carregá-los de forma confiável em datastores. Depois que o AWS Glue cataloga seus dados, eles são imediatamente pesquisáveis, podem ser consultados e estão disponíveis para processamento de ETL.
* Ajuda você a transformar dados em informações significativas. Utilize o poder dos serviços analíticos criados para finalidades específicas em vários casos de uso, como avaliação interativa, processamento de dados usando o Apache Spark e o Apache Hadoop, data warehousing, análise em tempo real, análise operacional, painéis e visualizações.

#### Amazon EMR e data lakes

As empresas começaram a perceber o poder dos data lakes. Elas podem colocar dados em um data lake e usar os frameworks de processamento distribuído de código aberto que preferirem, como os compatíveis com o Amazon EMR. O Apache Hadoop e o Spark são compatíveis com o Amazon EMR, que tem a capacidade de ajudar as empresas a implementar soluções de processamento de dados baseadas em data lakes do Amazon S3 de modo fácil, rápido e econômico.

#### AWS Lake Formation

O AWS Lake Formation facilita a ingestão, limpeza, catalogação, transformação e proteção dos seus dados, além de disponibilizá-los para avaliação e machine learning. O Lake Formation oferece um console central no qual você pode descobrir origens dos dados, configurar trabalhos de transformação para mover dados para um data lake do Amazon S3, remover duplicações e combinar registros, catalogar dados para acesso por ferramentas analíticas, configurar políticas de segurança e acesso a dados e auditar e controlar o acesso dos serviços analíticos e de machine learning da AWS.

O Lake Formation configura automaticamente os serviços AWS básicos para garantir a conformidade com suas políticas definidas. Se você configurou trabalhos de transformação que abrangem os serviços AWS, o Lake Formation configura os fluxos, centraliza a orquestração e permite que você monitore a execução dos trabalhos.

### Data WareHouse
Um data warehouse é um repositório central de dados estruturados de muitas origens de dados. Esses dados são transformados, agregados e preparados para relatórios e avaliaçãos de negócios.

Os dados são armazenados no data warehouse usando um esquema. Um esquema define como os dados são armazenados em tabelas, colunas e linhas. O esquema impõe restrições nos dados para garantir a integridade deles. O processo de transformação muitas vezes envolve as etapas necessárias para fazer com que os dados da fonte estejam em conformidade com o esquema. Após a primeira ingestão bem-sucedida de dados no data warehouse, o processo de ingestão e transformação dos dados pode continuar em um ritmo regular.

#### Data Warehouse Tradicional
**Vantagens:**
* Rápida configuração de dados;
* Conjunto de dados com curadoria;
* Armazenamento centralizado;
* Melhor Business Intelligence

**Desvantagens:**
* Custo elevado para inplementar;
* Manutenção pode ser desafiadora;
* Preocupações com segurança;
* Dificuldade de escalar para atender à demanda;

#### Amazon Redshift
É aqui que o Amazon Redshift entra. O Amazon Redshift supera todos esses pontos negativos oferecendo um ambiente baseado na nuvem, escalável e seguro para seu data warehouse. É fácil configurar, implantar e gerenciar o Amazon Redshift, sendo que ele oferece desempenho até 10 vezes mais rápido do que outras soluções de data warehousing.

**Benefícios:**
* Desempenho mais rápido: 10 vezes mais rápido do que outros data warehouses
* Fácil de configurar, implantar e gerenciar
* Seguro
* Escala rapidamente para atender às suas necessidades
### Data Mart
Um subconjunto de dados de um data warehouse é chamado de data mart. Os data marts se concentram em apenas um assunto ou uma área funcional. Um data warehouse pode conter todas as fontes relevantes para uma empresa, mas um data mart pode armazenar apenas as fontes de um único departamento. Como os data marts geralmente são uma cópia dos dados já contidos em um data warehouse, eles geralmente são rápidos e simples de implementar.

### Apache Hadoop

O Hadoop usa uma arquitetura de processamento distribuído, no qual uma tarefa é mapeada para um cluster de servidores convencionais para processamento. Cada bloco de trabalho distribuído aos servidores do cluster pode ser executado ou re-executado em qualquer um dos servidores. Os servidores do cluster usam frequentemente o Hadoop Distributed File System (HDFS) para armazenar dados localmente para processamento. Os resultados da computação realizada pelos servidores são reduzidos a um único conjunto de saída. Um nó, designado como nó principal, controla a distribuição de tarefas e pode lidar automaticamente com falhas dos servidores.

#### Benefícios do Hadoop
* Lida melhor com a incerteza;
* Gerencia uma variedade de dados;
* Tem amlpla seção de soluções;
* Visa ao volume e à velocidade;

### Implementação do Hadoop com o Amazon EMR

O Amazon EMR é o serviço AWS que implementa frameworks Hadoop. O serviço fará a ingestão dos dados de praticamente qualquer tipo de origem a praticamente qualquer velocidade! O Amazon EMR consegue implementar dois sistemas de arquivos diferentes: HDFS ou Elastic MapReduce File System (EMRFS). Um sistema de arquivos é um conjunto de regras organizacionais que controlam como os arquivos são armazenados. 

### HDFS

Para lidar rapidamente com volumes enormes de dados, o sistema de processamento exigia uma maneira de distribuir a carga de leitura e gravação de arquivos em dezenas ou até centenas de servidores de alta capacidade. O HDFS éum armazenamento distribuído que permite que os arquivos sejam lidos e gravados em clusters de servidores em paralelo. Isso reduz drasticamente a duração total de cada operação.

É útil compreender o funcionamento interno de um cluster do HDFS. Um cluster do HDFS consiste primariamente em um NameNode, que gerencia os metadados do sistema de arquivos, e DataNodes, que armazenam os dados reais.

### Amazon EMR

O Amazon EMR é o serviço AWS que implementa frameworks Hadoop. Um processo do Amazon EMR começa ingerindo dados de uma ou mais origens de dados e armazenando esses dados em um sistema de arquivos. Se estiver usando o HDFS, o sistema de arquivos será armazenado como um volume do Elastic Block Store. Esse volume de armazenamento no EMR é efêmero, o que significa que o armazenamento é de natureza temporária. Assim que os dados forem copiados para o volume do HDFS, a transformação e a avaliação dos dados serão executadas. Em seguida, os resultados são enviados para um datastore analítico, como um data lake do Amazon S3 ou um data warehouse do Amazon Redshift.

### Amazon EMRFS

O Amazon EMR oferece uma alternativa ao HDFS: o EMR File System (EMRFS). O EMRFS pode ajudar a garantir que haja uma “fonte confiável” persistente para dados do HDFS armazenados no Amazon S3. Ao implementar o EMRFS, não é necessário copiar dados para o cluster antes de transformar e analisar os dados como no HDFS. O EMRFS pode catalogar dados em um data lake no Amazon S3. O tempo economizado eliminando a etapa de cópia pode melhorar drasticamente o desempenho do cluster.

## Velocidade

### Processamento em Batch
Grandes intermitências de dados;

O processamento em batch geralmente é considerado um processo lento. Esse não é o caso. O processamento em batch deve consumir, de maneira rápida e eficiente, uma enorme quantidade de dados de uma só vez. Isso gera desafios que não existem com o processamento em stream.

O processamento de dados em batch oferece às empresas a capacidade de se aprofundarem nos dados coletados para produzir análise complexa que não pode ser obtida apenas usando a análise de streaming.

O processamento em batch é a execução de uma série de programas ou trabalhos em um ou mais computadores sem intervenção manual. Os dados são coletados em batches de maneira assíncrona. O batch é enviado a um sistema de processamento quando condições específicas são atendidas, como um horário específico do dia. Os resultados do trabalho de processamento são enviados a um local de armazenamento que pode ser consultado posteriormente, conforme necessário.

#### **Processamento de dados em batch com o Amazon EMR e o Apache Hadoop**

As organizações que precisam de soluções de big data estão trabalhando com dados em volume e velocidade tão altos que os ambientes tradicionais não conseguem atender às suas necessidades.

O Amazon EMR é um serviço gerenciado para a implantação de cargas de trabalho do Apache Hadoop. Além de executar o framework Apache Hadoop, você também pode executar outros frameworks distribuídos conhecidos, como Apache Spark, HBase, Presto e Flink no EMR. Você tem a vantagem adicional de poder interagir com dados em outros datastores da AWS, como o Amazon S3 e o Amazon DynamoDB. 

Os Amazon EMR notebooks oferecem um ambiente de desenvolvimento e colaboração sem servidor para consultas únicas e avaliaçãos exploratórias. Você pode manipular os dados e gerar gráficos de dados usando ferramentas gráficas avançadas. Os Amazon EMR notebooks monitoram seus trabalhos e até ajudam você a depurar o código dos notebooks.

#### Casos de uso programação em Batch
* Análise de logs;
* Visualização unificada de dados entre múltiplos datastores;
* Análise preditiva;
* Consultas em um datalake do Amazon S3;
### Processamento em Stream
Pequenas intermitências de dados;

O processamento de dados em stream oferece às empresas a capacidade de obter informações de seus dados em segundos após a coleta dos dados.

As empresas não podem mais se dar ao luxo de ignorar ou evitar grandes quantidades de dados que estão sendo enviados por meio de aplicativos web, compras de comércio eletrônico, atividades de jogadores em jogos virtuais e informações de redes sociais.

#### Processamento de big data em stream

Há vários motivos para usar soluções de dados de streaming. Em um sistema de processamento em batch, o processamento é sempre assíncrono e o sistema de coleta e de processamento costumam ser agrupados. Com soluções de streaming, o sistema de coleta (produtor) e o sistema de processamento (consumidor) são sempre separados. Os dados de streaming usam o que chamamos de produtores de dados. Cada um desses produtores pode gravar seus dados no mesmo endpoint, permitindo que vários streams de dados sejam combinados em um único stream para processamento. Outra grande vantagem é a capacidade de preservar a ordem dos dados do cliente e a capacidade de executar o consumo paralelo de dados. Isso permite que múltiplos usuários trabalhem simultaneamente nos mesmos dados.

#### Processamento de dados em stream com o Amazon Kinesis

No processamento em stream, você usa vários serviços: um serviço para ingerir o stream constante de dados, outro para processar e analisar o stream, e outro para carregar os dados em um datastore analítico, se necessário. O Amazon Kinesis atende a cada uma dessas necessidades e você pode usar cada serviço do Kinesis independentemente para criar uma solução de streaming ideal.

#### Casos de uso de procesamento stream
* Construir aplicativos de análise de vídeo;
* Evoluir o processamento em batch para a análise em tempo real;
* Analisar dados de dispositivos IoT;
### Aceleração de dados
A taxa na qual grandes coleções de dados podem ser ingeridas, processadas e analisadas. A aceleração de dados não é constante, ela vem em picos. Considere o Twitter como exemplo. Hashtags podem se tornar imensamente populares e aparecer centenas de vezes em apenas segundos, ou diminuir a velocidade para uma tag por hora. Isso é a aceleração de dados em ação. Seu sistema deve conseguir lidar de forma eficiente com o pico de centenas de tags por segundo e com a baixa demanda de uma tag por hora. 

## Variedade

### Banco de Dados Relacionais

O armazenamento de arquivos de texto puro pode não atender às suas necessidades de armazenamento de dados estruturados. A próxima etapa lógica é migrar para uma solução mais robusta: um banco de dados relacional.

Um processo conhecido como normalização ajuda uma empresa a transformar dados de arquivos de texto puro em um banco de dados relacional. A normalização é um conjunto de regras que funcionam juntas para reduzir a redundância, aumentar a confiabilidade e melhorar a consistência do armazenamento de dados.

Um banco de dados relacional é criado para armazenar dados estruturados para que possam ser coletados, atualizados e consultados facilmente. Bancos de dados relacionais dependem de uma série de estruturas, chamadas de tabelas, para armazenar os dados coletados. Essas tabelas são navegadas usando a linguagem de consulta estruturada ou SQL.

Logicamente, tabelas de banco de dados relacional agrupam dados com base em uma pessoa, um local, uma coisa ou um evento relacionado a esses dados. Esses agrupamentos são chamados de entidades. Cada entidade é armazenada como uma tabela. 

Uma coluna, conhecida como campo, é usada para descrever um atributo da entidade. Uma linha, conhecida como registro, na tabela representa uma única instância de uma entidade.

Pense em uma planilha, em que cada linha tem uma célula para cada coluna. Cada célula pode conter um valor. As regras dentro do esquema definem se o atributo é obrigatório ou opcional.

As relações são criadas primeiramente garantindo que cada linha em uma tabela seja exclusiva. Isso é feito criando uma chave primária. Esse valor de chave primária pode ser usado para criar relações entre tabelas. Uma chave externa é um campo que usa os valores de uma chave primária em outra tabela para definir um registro na tabela atual. Essa ação é o que cria a relação. Alguns mecanismos de banco de dados podem impor essa relação para garantir que apenas os valores da chave primária possam ser usados na chave externa.

#### Bancos de dados OLTP
Bancos de dados de processamento de transações on-line (OLTP), geralmente chamados de bancos de dados operacionais, organizam logicamente os dados em tabelas, com foco principal na velocidade da entrada de dados. Esses bancos de dados são caracterizados por um grande número de operações de inserção, atualização e exclusão.

Todas as decisões sobre a organização de dados e o armazenamento de atributos se baseiam em garantir entrada e atualizações rápidas de dados. A eficácia de um sistema OLTP geralmente é medida pelo número de transações por segundo.
#### Bancos de dados OLAP
Bancos de dados de processamento analítico on-line (OLAP), geralmente chamados de data warehouses, organizam logicamente os dados em tabelas, com foco principal na velocidade da recuperação de dados por meio de consultas. Esses bancos de dados são caracterizados por um número relativamente baixo de operações de gravação e a falta de operações de atualização e exclusão.

Todas as decisões sobre a organização de dados e o armazenamento de atributos são baseadas nos tipos de consultas e em outras análises que serão feitas usando os dados. A eficácia de um sistema OLAP geralmente é medida pelo tempo de resposta dos resultados da consulta.

### Banco de Dados Não Relacionais
Bancos de dados não relacionais são criados para armazenar dados semiestruturados e não estruturados de uma forma que ofereça rápida coleta e recuperação. Existem várias categorias amplas de bancos de dados não relacionais e os dados são armazenados em cada um para atender a requisitos específicos.

#### Armazenamento de Documentos
Os armazenamentos de documentos são um tipo de banco de dados não relacional que armazena dados semiestruturados e não estruturados na forma de arquivos. Esses arquivos variam em forma, mas incluem JSON, BSON e XML. Os arquivos podem ser navegados usando várias linguagens, incluindo Python e Node.js.

Logicamente, os arquivos contêm dados armazenados como uma série de elementos. Cada elemento é uma instância de uma pessoa, local, coisa ou evento. Por exemplo, o armazenamento de documentos pode conter diversos arquivos de log de um conjunto de servidores. Esses arquivos de log podem conter os detalhes desse sistema sem se preocupar com o que os arquivos de log em outros sistemas contêm.

Vantagens:

* Flexibilidade;
* Não necessidade de planejar um tipo específico de dados ao criar um;
* Fáceis de dimensionar.

Desvantagens:

* Sacrifica a conformidade com ACID para ter flexibilidade;
* Não é possível consultar entre arquivos.

#### Armazenamento de Chave-Valor
Bancos de dados de chave-valor são um tipo de banco de dados não relacional que armazena dados não estruturados na forma de pares de chave-valor.

Logicamente, os dados são armazenados em uma única tabela. Na tabela, os valores são associados a uma chave específica. Os valores são armazenados na forma de objetos binários grandes (BLOB) e não exigem um esquema predefinido. Os valores podem ser de praticamente qualquer tipo.

Vantagens: 

* Muito flexíveis;
* São capazes de lidar com uma grande variedade de tipos de dados;
* As chaves são vinculadas diretamente aos seus valores, sem precisar de indexação ou operações de agrupamento complexas;
* O conteúdo de uma chave pode ser facilmente copiado para outros sistemas sem reprogramar os dados.

Desvantagens: 

* É impossível consultar valores porque são armazenados como um BLOB único;
* É muito difícil atualizar ou editar o conteúdo de um valor;
* Nem todos os objetos são modelados facilmente como pares de chave-valor.

### Vantagens e desvantagens do banco de dados não relacional

Os bancos de dados não relacionais têm o principal benefício de ir além das limitações dos bancos de dados relacionais, especialmente por meio de esquemas dinâmicos, que oferecem aos DBAs a capacidade de atualizar esquemas em tempo real. Isso leva a ciclos de desenvolvimento mais rápidos e menos tempo de inatividade. Além disso, como os bancos de dados não relacionais podem ser implantados em servidores de commodities distribuídos em massa, esses bancos de dados têm uma vantagem em scaling e podem lidar com conjuntos de dados muito maiores.

A distribuição massiva tem uma desvantagem, na forma de “consistência eventual”, o que significa que os dados não são atualizados instantaneamente a cada alteração e, em vez disso, alcançam a atualização como uma tarefa em segundo plano. Embora seja aceitável em muitas circunstâncias, isso dificulta atingir a conformidade com ACID. Observe que o DynamoDB oferece suporte à conformidade com ACID.

Outra desvantagem é que os bancos de dados não relacionais não têm desempenho tão bom quanto os bancos de dados relacionais em aplicativos que exigem latência transacional extremamente baixa. Por fim, embora as plataformas não relacionais estejam evoluindo e crescendo constantemente, praticamente não há a mesma maturidade que as tecnologias relacionais ou o mesmo nível de especialização em campo.

## Veracidade
### Práticas para ajudar a identificar problemas de integridade dos dados

#### Saiba qual deve ser a limpeza
Antes de fazer qualquer outra coisa, você deve ter consenso sobre o resultado limpo. Algumas empresas consideram dados limpos os dados em seu formato bruto com regras empresariais aplicadas. Algumas empresas consideram dados limpos os dados que foram normalizados, agregados e tiveram substituições de valor aplicadas para regular todas as entradas. Esses são dois entendimentos muito diferentes de limpeza. Verifique qual é a sua meta.

#### Saiba de onde os erros vêm
À medida que você encontrar erros nos dados, rastreie a origem provável. Isso ajudará a prever cargas de trabalho que terão problemas de integridade. Isso também ajudará você a justificar alterações no sistema que melhorariam a eficiência das operações de ETL.

#### Saiba quais são as alterações aceitáveis
Sob uma perspectiva unicamente centrada em dados, inserir um zero em uma coluna vazia pode parecer uma decisão de limpeza de dados fácil, mas é preciso saber quais os efeitos dessa alteração. Da mesma maneira, combinar os números de inventário “Em pedido” e “Em estoque” nos relatórios mensais pode parecer inconsequente. No entanto, esses dados podem acabar nas mãos de um gerente de inventário que agora acredita que há um problema de perda de inventário. Esses são os pequenos detalhes que podem causar um impacto negativo enorme.

#### Saiba se os dados originais possuem valor
Em alguns sistemas, os dados originais não têm mais valor depois de terem sido transformados. No entanto, em dados altamente regulamentados ou dados altamente voláteis, é importante que tanto os dados originais quanto os dados transformados sejam mantidos no sistema de destino.

Por exemplo, em um sistema de jogos on-line, pode não haver valor em registrar cada mudança de direção que um jogador faz à medida que se move no mapa. O único valor importante é quando o participante entra ou sai das principais áreas do mapa. No entanto, em um aplicativo de serviços bancários, todos os detalhes de cada transação são vitais para a auditoria, embora o cliente possa apenas se preocupar em verificar se a transação teve sucesso ou não.

### Esquema de Banco de Dados
Bancos de dados relacionais dependem de esquemas de banco de dados para organizar o conteúdo dentro do banco de dados e impor a integridade referencial e de domínio. Os programadores também usam esses esquemas ao escrever o software para interagir com o banco de dados.

#### Esquemas de Dados
Um esquema de dados é o conjunto de metadados usado pelo banco de dados para organizar objetos de dados e impor restrições de integridade. O esquema define os atributos do banco de dados, fornecendo as descrições de cada objeto e como ele interage com outros objetos no banco de dados. Um ou mais esquemas podem residir no mesmo banco de dados.

Há dois tipos de esquemas: lógico e físico.

##### Esquema Lógico:
Os esquemas lógicos se concentram nas restrições a serem aplicadas aos dados no banco de dados. Isso inclui a organização de tabelas, visualizações e verificações de integridade.

Tabelas e exibições podem ser relacionadas entre si. O esquema define as informações de cada relação e como ela deve ser imposta. O esquema também pode fornecer integridade de domínio definindo restrições sobre os valores permitidos em campos específicos dentro da tabela que fornece integridade de domínio.

As verificações de integridade vêm em diferentes formas, mas o objetivo é garantir que quaisquer alterações feitas no banco de dados não resultem em perda de consistência de dados.

##### Esquema Físico:
Os esquemas físicos se concentram no armazenamento real de dados em disco ou em um repositório de nuvem. Esses esquemas têm detalhes sobre os arquivos, índices, tabelas particionadas, clusters e muito mais.

Em geral, os analistas podem usar esquemas físicos para calcular estimativas sobre o espaço de armazenamento necessário e o crescimento potencial do sistema. Esses esquemas também são importantes para a recuperação de desastres e o planejamento da infraestrutura.

#### Esquema de Informações
Você já imaginou como um DBMS gerencia todos os bancos de dados, tabelas e relações? A resposta está no esquema de informações. Um esquema de informações é um banco de dados de metadados que armazena informações sobre os objetos de dados em um banco de dados.

O Microsoft SQL Server chama seu esquema de informações de banco de dados mestre. A Oracle usa tabelas de dicionário de dados e um registro de metadados. O Apache Hadoop usa um metastore. Cada DBMS pode ter nomes diferentes para a estrutura de dados que armazena os metadados, mas a finalidade é a mesma: definir quais são todos os objetos no banco de dados e registrar informações vitais sobre eles. Esses bancos de dados armazenam informações como o nome e o tamanho de uma tabela, os índices na tabela e as restrições de dados na tabela. As configurações de segurança para usuários, ativos de dados externos e configurações de gerenciamento também podem ser incluídas.

Dadas as permissões apropriadas no banco de dados, você pode consultar o esquema de informações para saber mais sobre os objetos no banco de dados. Quando as consultas são executadas, essas informações são usadas para garantir a melhor otimização para a consulta. O esquema de informações também pode ser usado na manutenção do próprio banco de dados.

### ACID
ACID é um acrônimo para Atomicidade, Consistência, Isolamento e Durabilidade. É um método para manter a consistência e a integridade em um banco de dados estruturado.

### Conformidade com o ACID

ACID é o bastião de longa duração da integridade dos dados relacionais. Em um banco de dados como o Amazon RDS, uma sequência de instruções executadas em conjunto é chamada de transação. Milhões de transações podem ser executadas consecutivamente. Os dados e as restrições nesses dados são muito ativos em bancos de dados relacionais.

O objetivo de um banco de dados compatível com ACID é retornar a versão mais recente de todos os dados e garantir que os dados inseridos no sistema atendam a todas as regras e restrições atribuídas em todos os momentos.

#### Atomicidade
Ao executar uma transação em um banco de dados, a atomicidade garante que suas transações sejam bem-sucedidas por completo ou falhem por completo. Nenhuma declaração pode ser bem-sucedida sem as outras. Como muitas solicitações para um banco de dados são multifacetadas, essa interação é muito importante para evitar falhas no seu conjunto de dados.

Quando a atomicidade falha, os resultados podem ser problemáticos. Imagine uma operação definida para copiar todos os pedidos de uma tabela temporária para uma tabela permanente a cada 10 minutos. Se um único registro dentro dessa transação falhar, tudo o que o seguir também falhará. Isso deixa parte da operação bem-sucedida e parte com falha. Pode ser quase impossível identificar as partes que tiveram êxito e as partes que falharam.
#### Consistência
A consistência garante que todas as transações forneçam dados válidos para o banco de dados. Esses dados devem aderir a todas as regras e restrições definidas. Para que uma transação seja concluída com êxito, todas as declarações dentro dela devem ser válidas em relação a todas as restrições relevantes definidas no banco de dados. Se qualquer declaração única violar essas verificações, toda a transação será revertida e o banco de dados retornará ao estado anterior. A consistência também garante que as atualizações de dados estejam disponíveis somente quando todas as replicações também forem atualizadas.
#### Isolamento
O isolamento garante que uma transação não possa interferir em outra transação simultânea. Os bancos de dados são locais ocupados. O isolamento garante que, quando várias transações solicitam os mesmos dados, existam regras em vigor garantindo que as operações não causem corrupção de dados e que todos os dados sejam disponibilizados de maneira ordenada.
#### Durabilidade
A durabilidade dos dados tem a ver com garantir que suas alterações realmente se mantenham. Após a conclusão bem-sucedida de uma transação, a durabilidade garante que o resultado da transação seja permanente mesmo em caso de falha do sistema. Isso significa que todas as transações concluídas que resultam em um novo registro ou atualização em um registro existente serão gravadas em disco e não deixadas na memória.

### BASE
BASE é um acrônimo para BAsicamente disponível, eStado flexível, Eventualmente consistente. É um método para manter a consistência e a integridade em um banco de dados estruturado ou semiestruturado.

### Conformidade com BASE

O BASE promove a integridade de dados em bancos de dados não relacionais, às vezes são chamados de bancos de dados NoSQL. Bancos de dados não relacionais, como o Amazon DynamoDB, ainda usam transações para processar solicitações. Esses bancos de dados são hiperativos e a principal preocupação é a disponibilidade dos dados em relação à consistência dos dados. Para garantir que os dados estejam altamente disponíveis, as alterações nos dados são disponibilizadas imediatamente na instância em que a alteração foi feita. No entanto, pode levar algum tempo para que essa alteração seja replicada em toda a frota de instâncias. O objetivo é que a alteração acabe sendo totalmente consistente em toda a frota. 

#### Basicamente Disponível
O BA permite que uma instância receba uma solicitação de alteração e disponibilize essa alteração imediatamente. O sistema sempre garantirá uma resposta para cada solicitação. No entanto, é possível que a resposta possa ser uma falha ou dados obsoletos se a alteração não tiver sido replicada em todos os nós. Em um sistema ACID, a alteração não seria disponibilizada até que todas as instâncias fossem consistentes. A consistência em um modelo BASE é trocada pela disponibilidade.

#### Estado Flexível
Em um sistema BASE, há tolerâncias para consistência parcial entre instâncias distribuídas. Por esse motivo, considera-se que os sistemas BASE estão em um estado flexível, também conhecido como estado alterável.

Em um sistema ACID, considera-se que o banco de dados está em um estado rígido porque os usuários não podem acessar dados que não são totalmente consistentes.

#### Consistência Eventual
Isso reforça as outras letras no acrônimo. Os dados estarão eventualmente consistentes. Em outras palavras, uma alteração será feita em cada cópia em algum momento. No entanto, os dados estarão disponíveis em qualquer estado durante a propagação da alteração.

### Operações ETL
Extração, transformação e carregamento (ETL) é o processo de coletar dados de origens brutas e transformá-los em um tipo comum. Esses novos dados são carregados em um local final para serem disponibilizados para avaliação e inspeção analíticas. Em ambientes modernos baseados na nuvem, geralmente nos referimos a esse processo como ELT (extração, transformação e carregamento). As etapas são simplesmente executadas em uma ordem diferente, mas o resultado é o mesmo.

### Ferramentas AWS para Processamento de dados em ETL
Quando se trata de executar o componente de transformação de dados do ETL, há duas opções na AWS: o Amazon EMR e o AWS Glue. Esses dois serviços fornecem resultados semelhantes, mas exigem diferentes quantidades de conhecimento e investimento de tempo.

O Amazon EMR é uma abordagem mais prática para criar seu pipeline de dados. Esse serviço fornece uma plataforma robusta de coleta e processamento de dados. Para usar esse serviço, sua equipe deve ter sólido conhecimento técnico e know‑how. A vantagem dele é que você pode criar um pipeline personalizado para atender às suas necessidades de negócios. Além disso, os custos de infraestrutura podem ser menores do que executar a mesma carga de trabalho no AWS Glue.

O AWS Glue é uma ferramenta de ETL gerenciada sem servidor que oferece uma experiência muito mais simplificada do que o Amazon EMR. Isso torna o serviço ideal para tarefas simples de ETL, mas você não terá tanta flexibilidade quanto teria com o Amazon EMR. Você também pode usar o AWS Glue como um metastore para seus dados transformados finais usando o AWS Glue Data Catalog. Esse catálogo é uma substituição de uma metastore do Hive.

Ao decidir com qual dessas ferramentas vai trabalhar, considere o final. Você prefere um pipeline de dados contínuo que exija pouca sobrecarga? Você precisa de processamento paralelo massivo de dados? Qual o nível de personalização de que sua solução de dados precisará?

## Valor

### O que é análise de dados?

Dados sem significado são irrelevantes. Palavras em um idioma que você não compreende são igualmente insignificantes. É somente quando o significado é atribuído que os dados ou as palavras podem ser compreendidos.

A análise de dados tem duas classificações: análise de informações e análise operacional. Análise de informações é o processo de análise de informações para encontrar o valor contido nelas. É uma ampla classificação de análise de dados que pode abranger tópicos que vão desde contabilidade financeira de uma empresa até a análise do número de entradas e saídas em um edifício protegido. A segunda forma de análise é a operacional. Ela é muito semelhante à análise de informações, no entanto, ela se concentra nas operações digitais de uma organização.

### Análise de informações

Análise de informações é o processo de análise de informações para encontrar o valor contido nelas. Esse termo geralmente é sinônimo de análise de dados.

### Análise operacional

As empresas têm milhares de sistemas, aplicativos e clientes que geram dados constantemente. Essa é uma das áreas de coleta de dados que mais cresce. A análise operacional é uma forma de análise usada especificamente para recuperar, analisar e relatar dados para operações de TI. Esses dados incluem logs de sistema, logs de segurança, eventos e processos complexos de infraestrutura de TI, transações de usuários e até mesmo ameaças à segurança.

Na AWS, o Amazon Elasticsearch Service é comumente usado para implementar análises operacionais.

### Tipos de Análise
![image](/Sprint_6/img/YnMthvfAz9UUYqPJ_44lqgg8rG8MQp953.png)

#### Análise preditiva

A AWS tem o Amazon ML e um conjunto de serviços (incluindo inteligência artificial [IA]) que facilitam para os desenvolvedores a aplicação de análise preditiva aos seus dados e a adição de novos recursos inteligentes de processamento de dados aos seus aplicativos. A Amazon tem uma longa e rica tradição em torno de machine learning (ML) e muito dessa tecnologia acumulada foi organizada em um pacote para o uso do cliente com esse serviço.

A pilha de machine learning tem três camadas principais:

1. Serviços de aplicativos permitem que os desenvolvedores conectem a funcionalidade de IA pré-criada nos aplicativos sem se preocuparem com os modelos de ML que alimentam esses serviços.
2. Serviços de plataforma facilitam para qualquer desenvolvedor começar e se aprofundar em ML.
3. Frameworks e interfaces para especialistas em ML.

Na arquitetura a seguir, você vê um exemplo do uso do Amazon ML para produzir previsões em tempo real para usuários de um aplicativo. Nessa arquitetura, há vários serviços trabalhando em conjunto para produzir as previsões.

#### Análise cognitiva

Análise cognitiva é a forma mais recente de análise de dados. Ele oferece uma oportunidade incrível de fornecer recomendações altamente especializadas para empresas sem qualquer envolvimento humano, além da configuração inicial e do treinamento dos modelos de ML.

Alguns exemplos reais de análise cognitiva são:

1. Software financeiro que fornece recomendações de investimento precisas, em tempo real e baseadas em fatos;
2. Software para a área de saúde que oferece aos clientes acesso a recomendações confiáveis sobre tratamentos e opções atualizadas de saúde;
3. Software veterinário que ajuda os veterinários a diagnosticar com rapidez e precisão seus pacientes;
4. Software que auxilia ligas de futebol americano e entusiastas a gerenciarem suas equipes.

### Serviços analíticos e velocidade

Na primeira vez em que você envia dados por um sistema de análise de dados, os dados fluem da ingestão para um local de armazenamento intermediário. Em seguida, os dados são processados a partir do local intermediário e podem resultar na colocação dos dados em um datastore analítico. O processamento dos dados do local intermediário pode ser repetido muitas vezes para produzir muitos resultados analíticos diferentes.

#### Análise em Batch
A análise em batch geralmente envolve consulta a grandes quantidades de dados “frios”. A análise em batch é implementada em grandes conjuntos de dados para produzir um grande número de resultados analíticos de forma regular. Os sistemas baseados em MapReduce, como o Amazon EMR, são exemplos de plataformas compatíveis com análise em batch.

Os frameworks de alto nível executados no Apache Hadoop podem simplificar e acelerar significativamente a análise em batch. O framework que deve usar depende muito do tipo de carga de trabalho que você tem. Alguns dos frameworks mais populares usados com o Hadoop são Hive, Flink, Tez, HBase, Presto, Pig e Spark. Cada um desses frameworks pode ser instalado em clusters do Amazon EMR.

#### Análise em Stream
Análise em stream exige a ingestão de uma sequência de dados e a atualização incremental de métricas, relatórios e estatísticas de resumo em resposta a cada registro de dados recebido. Esse método é mais adequado para funções de monitoramento e resposta em tempo real.

O processamento de dados de streaming requer duas camadas: uma camada de armazenamento e uma camada de processamento. A camada de armazenamento precisa ser compatível com a solicitação de registros e ter forte consistência para permitir leituras e gravações rápidas, de baixo custo e reproduzíveis de grandes fluxos de dados. A camada de processamento é responsável pelo consumo de dados da camada de armazenamento, realizando cálculos sobre esses dados e, em seguida, enviando notificações para a camada de armazenamento excluir os dados que não são mais necessários. Surgiram várias plataformas que oferecem a infraestrutura necessária para criar aplicativos de dados de streaming, incluindo o Amazon Kinesis, o Apache Kafka, o Apache Flume, o Apache Spark Streaming e o Apache Storm.

O Amazon Kinesis é uma plataforma para dados de streaming na AWS, oferecendo serviços avançados para facilitar o carregamento e a análise de dados de streaming e permite que você crie aplicativos de dados de streaming personalizados para necessidades específicas. O Kinesis oferece dois serviços: o Amazon Kinesis Data Firehose e o Amazon Kinesis Data Streams.

Se os dados no fluxo precisarem de conversão de formato, transformação, enriquecimento ou filtragem, você poderá pré-processar os dados usando uma função do AWS Lambda. Você pode fazer isso antes que o código SQL do aplicativo seja executado ou antes que o aplicativo crie um esquema do seu stream de dados.

Você pode instalar plataformas de dados de streaming de sua escolha no Amazon Elastic Compute Cloud (Amazon EC2) e no Amazon EMR e criar suas próprias camadas de armazenamento e processamento em stream. Ao criar sua solução de dados em streaming no Amazon EC2 e no Amazon EMR, você pode evitar o atrito causado pelo provisionamento da infraestrutura e obter acesso a diversos frameworks de armazenamento e processamento em stream. As opções da camada de armazenamento de dados em streaming são o Apache Kafka e o Apache Flume. As opções para a camada de processamento em stream são o Apache Spark Streaming e o Apache Storm.

#### Análise Interativa
Análise interativa normalmente envolve a execução de consultas intrincadas em conjuntos de dados complexos em altas velocidades. Esse tipo de análise é interativo, pois permite que o usuário consulte e veja os resultados imediatamente. A avaliação em batch geralmente é executada em segundo plano, fornecendo avaliação em formato de relatórios entregues de forma programada.

Para avaliaçãos interativas, o Amazon Athena facilita a avaliação de dados diretamente no Amazon S3 e no Amazon S3 Glacier usando consultas SQL padrão. O Athena é um serviço sem servidor, por isso, não é necessário configurar ou gerenciar a infraestrutura. Você pode começar a consultar dados imediatamente, obter resultados em segundos e pagar apenas pelas consultas executadas. Basta apontar para os dados no Amazon S3, definir o esquema e iniciar as consultas usando SQL padrão. A maioria dos resultados é entregue em segundos.

O Amazon ES permite pesquisar, explorar, filtrar, agregar e visualizar seus dados quase em tempo real. O serviço tem APIs fáceis de usar e recursos de análise em tempo real, juntamente com a disponibilidade, a escalabilidade e a segurança exigidas pelas cargas de trabalho de produção.

O Amazon Redshift oferece a capacidade de executar consultas complexas e análises em petabytes de dados estruturados e inclui o Redshift Spectrum, que executa consultas SQL diretamente em exabytes de dados estruturados ou não estruturados no Amazon S3 sem precisar mover dados de forma desnecessária.

### Soluções de avaliação de dados e serviços AWS

#### Ingerir/Coletar
* Amazon EMR;
* AWS Glue;
* Amazon Kinesis;
#### Armazenar
* Amazon S3;
* Data lakes do Amazon S3;
* Amazon RDS;
* Amazon DynamoDB;
* Amazon Redshift;
#### Processar/Analisar
* Amazon ML;
* Amazon EMR;
* AWS Glue;
* Amazon Kinesis Data Analytics;
* Amazon Athena;
#### Consumir/Visualizar
* Amazon Redshift;
* Amazon QuickSight;
* Amazon Athena;

### Visualização dos Dados
#### Preparação de dados

Lembre-se de que há um processo pelo qual os dados devem passar para serem realmente valiosos. Esse processo inclui:

* Exploração de dados - essa primeira fase geralmente faz parte do planejamento envolvido na criação de uma operação de ETL.
* Limpeza de dados - esse é o processo de normalização dos dados dentro da operação de ETL para garantir que os campos contenham os valores corretos e lidar com o problema de valores ausentes.
* Transformação de dados - essa fase envolve a aplicação de funções para manipular dados em novos formatos para fins analíticos.
* Visualização de dados - esse é o processo de criação de relatórios e painéis para apresentar o valor contido nos dados.
  
Já discutimos os três primeiros processos de análise de informações. Esta lição ajudará você a entender o processo final, que é a visualização dos dados.

#### O que há em um relatório?

Os relatórios analíticos são apresentados em vários formatos e tamanhos diferentes. A origem dos dados raramente afeta os relatórios resultantes. Os relatórios são organizados para atender às necessidades dos consumidores dos relatórios.

Há três tipos amplos de relatórios: estáticos, interativos e painéis.

* Os relatórios estáticos não desapareceram nesta era digital. Na verdade, ainda são muito utilizados para apresentações e reuniões. São encontrados em formato PDF e slides do PowerPoint e, muitas vezes, podem ser acessados por meio de portais da web e interfaces de software.
* Os relatórios interativos estão se tornando cada vez mais comuns. Esses tipos de relatórios geralmente se enquadram como business intelligence de autoatendimento. Esses relatórios costumam ter um estilo de relatório para impressão, mas têm a vantagem de que os consumidores podem aplicar filtros a tabelas e gráficos, alterar as escalas e até mesmo agrupar e classificar os valores nos relatórios. Isso permite que um consumidor conte sua própria história usando a base estabelecida pelo criador do relatório.
* Painéis são outra ferramenta de relatórios muito conhecida. A interatividade dos painéis depende do software empregado. Os consumidores encontram o maior benefício em painéis quando se concentram em roll-ups de alto nível dos principais fatores de negócios.

Relatórios e painéis são compostos por vários gráficos e tabelas para responder perguntas. Se as perguntas forem claras, o relatório ou o painel fornecerão as respostas. Relatórios e painéis também podem ser divididos em páginas ou exibições. Essas páginas devem ter um único tema para todos os elementos do relatório nelas. É muito comum dar aos consumidores de relatórios e painéis interativos filtros que podem ser aplicados a toda a página ou a elementos individuais na página.

#### Práticas recomendadas para escrever relatórios

Elaborar um relatório sólido que fornecerá aos consumidores o que eles precisam para tomar decisões críticas é uma forma de arte. Há algumas etapas para ter sucesso:

* Coletar dados, fatos, itens de ação e conclusões.
* Identificar o público, as expectativas dele e o método apropriado de entrega.
* Identificar os estilos de visualização e o estilo de relatório que melhor atendem às necessidades do público.
* Criar os relatórios e painéis.