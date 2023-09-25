Diretório Sprint #5
===================
### Este diretório é dedicado para os conteúdos trabalhados durante a Sprint 5 do programa de bolsas D&A da CompassUol

### Conceitos de Nuvem e Serviços da AWS

A computação em nuvem é a entrega de recursos de TI sob demanda pela Internet com pagamento conforme o uso.

### Modelos de implantação de computação em nuvem
* **Software como serviço (SaaS)**:
* **Plataforma como serviço (PaaS)**:
* **Infraestrutura como serviço (IaaS)**:

### Padrões entre clientes da AWS
* Desenvolvedor e Tester: Desenvolvimento de novas aplicações/aplicativos ou migração de cargas de baixo risco para a nuvem.
* Produção: Migração de cargas de trabalho para a nuvem.
* Essencial para a operação: Movimentação das cargas de sua organização para a nuvem. Neste caso, percebe-se a dedicação intensa ao uso da nuvem.
* Integral: Ultima fase do desenvolvimento em nuvem, onde o cliente integra essa funcionalidade em todas as suas operações. É o estágio final.

### Por que os clientes escolhem a AWS
A AWS oferece uma série de benefícios em escala global, para todos os clientes por meio de serviços, metodologias de redução de custo e foco no crescimento e inovação do cliente.

* Troque os investimentos antecipados pelo modelo de consumo de pagamento conforme o uso;
* Aumento da velocidade e agilidade;
* Simplificação e aprimoramento das decisões de infraestrutura.
* Aumento das margens;
* Dimensionamento global;
* Melhoria na segurança;
* Aumento da inovação;
* Redução do tempo de chegada ao valor comercial;

#### Diferenciais AWS
* Experiência e liderança empresarial;
* Cultura da Amazon;
* Variedade de Serviços;
* Ritmo e Inovação;
* Presença Global;
* Segurança e Privacidade;
* Maior comunidade de parceiros;
* Recursos de Nuvem Híbrida;

##### Infraestrutura Global altamente disponível
As regiões AWS são compostas por várias zonas de disponibilidade para aumentar o dimensionamento e a tolerância a falhas.  
A infraestrutura da AWS oferece verdadeira alta disponibilidade para proporcionar a redundância e a durabilidade que os clientes exigem;  
Geralmente as instalações se localizam a dezenas de quilômetros de distância umas das outras, o que isola os desastres mais comuns como enchentes, incêncios e tempestades severas.

### Serviços da AWS
A Amazon Web Services possuem uma gigantesca variedade de serviços disponíveis globalmente, dentre eles:
![image](/Sprint_5/img/variedade_aws.png)

#### Categorias de Serviço
* Computação;
* Armazenamento;
* Banco de Dados;
* Segurança;
* Gerenciamento;
* Redes;

### Recursos AWS Marketplace
O AWS Marketplace é um catálogo digital que ajuda os clientes a descobrir softwares de terceiros. Eles também podem conhecer e comprar serviços profissionais para configurar, implantar e gerenciar softwares de terceiros.

### Modernização de aplicativos em geral
Mudança da criação de aplicativos monolíticos para microsserviços menores e idenpendentes que são implantados separadamente, mas podem interagir juntos para alcançar um caso de uso mais amplo.

### O que é valor comercial?
Pode aparecer como custos reduzidos, recursos liberados, tempo de inatividade reduzido e tomada de decisão aprimorada. O AWS Cloud Value Framework fornece orientação sobre como fazer isso e mostra as diferentes áreas de valor comercial que os clientes perceberam ao migrar para a AWS.  

O valor comercial é entender o que impulsiona a adoção da nuvem, por que isso é importante para os clientes e os resultados tangíveis que as empresas podem alcançar.

### Cloud Value Framework
Estrutura conceitual destinada a criar um caso de negócio abrangente para a adoção da nuvem e ajuda a articular o valor da adoção da nuvem. Ele faz isso medindo e rastreando o progresso dos clientes que migraram para a AWS em relação a quatro pilares principais de valor: 
* Economia de custo;
* Produtividade da equipe;
* Resiliência da equipe;
* Resiliência operacional;
* Agilidade Operacional;

### Como lidar com objeções à Nuvem

Quando trabalhamos com clientes, precisamos entender quaisquer objeções existentes para proporcionar o melhor produto ou serviço possível.

Dentre algumas objeções temos:
* Custo;
* Segurança, conformidade e privacidade;
* Perda de controle ou visibilidade;
* Infraestrutura existente;
* Déficit de habilidades;
* Atrelamento a fornecedor;
* Sustentabilidade;
* Recursos do módulo;

### O que é Venda Conjunta?
É uma dinâmica de vendas em que a AWS e AWS Partners trabalham em conjunto em uma oportunidade do cliente. As equipes de vendas AWS querem trabalhar com AWS Partners para agilizar o tempo de entrega de valor aos clientes por meio de soluções especializadas, conhecimento no setor e modelos flexíveis de engajamento.

#### Por que os parceiros vendem em conjunto com a AWS?
* Aumentar a receita;
* Melhorar os relacionamentos com clientes;
* Ganhar incentivos financeiros;

## AWS Partner: Accreditation (Technical)

### Serviços de Armazenamento
#### Amazon Elastic

#### Amazon S3
Armazenamento de objetos durável e dimensionável.

#### Amazon S3 Glacier
Arquivamento e backup de dados.

#### AWS Storage Gateway
Integre armazenamento na nuvem com cargas de trabalho no local.
#### Amazon Elastic File System
Armazenamento de arquivos para instâncias do Amazon EC2.

#### Amazon FSx
Armazenamento de arquivos para sistemas de arquivo amplamente usados.

#### Amazin Elastic Block Store
Armazenamento em bloco anexo à rede para uso com as instâncias Amazon EC2
* Persistente independentemente de sua instância;
* Usado como um disco rígido;
* Replicação automática;
* Anexado a qualquer instância na mesma AZ;
* Um volume do EBS para uma instância EC2;
* Uma instância para vários volumes EBS;
* Os volumes EBS podem reter dados após o encerramento da instância do EC2;
* Permite Snapshots pontuais para incrementos de GiB do S3.

### Serviços de Banco de Dados
Desenvolvido para casos de uso de aplicativos específicos.

* Amazon RDS: Capacidade econômica e redimensionável;
* Amazon DynamoDB: Desempenho rápido e previsível
* Amazon ElastiCache: Recuperação rápida e gerenciada de informações;

Os bancos de dados da AWS são fáceis de configurar, gerenciar e manter; reduz o trabalho pesado genérico; alta disponibilidade ao clique de um botão.

### Serviços de Redes
#### Amazon VPC
Crie uma rede virtual na nuvem;

#### Grupos de segurança
Controle o acesso às instâncias

#### Amazon route 53
Direcione usuários finais para aplciativos na internet

### Segurança na Nuvem AWS 
A segurança na nuvem é a maior prioridade da AWS.
* Benefícios da herança do data center e da arquitetura de rede da AWS;
* Semelhante aos data centers locais, sem manutenção de instalações e hardware;
* Pode ser facilmente automatizado;
* Herda todas as práticas recomendadas da AWS.

### Como lidar com Objeções
* Abordar as objeções antes de avançar para um próximo passo;
* As objeções nem sempre são factuais;

Primeiramente devemos nos conectar com o cliente, identificar o problema com o ponto de vista do cliente.

Logo após, identificamos a principal preocupação e tomamos medidas para a resolução da mesma.

### Processo de Migração
#### Avaliação
Identificar a prévia preparação do cliente e identificar possíveis resultados comerciais.
#### Preparação e Planejamento
Analisar o ambiente, determinar estratégias de migração e criar uma landing zone bem arquitetada.
#### Migração e Modernização
Projetar, migrar e validar cada aplicativo, migrar dados e modernizar a configuração.

### Colocando em Produção
#### Práticas Recomendadas:
* Envolva a equipe de contas da AWS;
* Requisitos regulatórios específicos do cliente;
* Nível do AWS Support;

### Análise de redução de custos
Comparar com o cliente o custo necessário para o seu serviço usando a infraestrutura tradicional da T.I em relação ao custo de adotar alguma resolução da AWS.

### Aspectos Econômicos na Nuvem
Os aspectos econômicos na nuvem focalizam duas áreas diferentes uma da outra, mas que também têm muito em comum: valor comercial e gerenciamento financeiro na nuvem.

A primeira área, valor comercial, inclui todos os componentes que promovem os negócios dos clientes. O valor comercial é o que você discute com os clientes antes de uma venda para ajudá-los a compreender o valor da AWS, e como a AWS melhorará todos os aspectos do desempenho do negócio e da experiência do cliente.

Embora o valor comercial inclua o conceito já conhecido de custo total de propriedade, ou TCO, há muito mais, com muitos outros componentes que afetam diretamente os negócios.


O gerenciamento financeiro na nuvem é a outra parte dos aspectos econômicos na nuvem. Essa área se concentra em ajudar os clientes da AWS a terem sucesso no gerenciamento financeiro na infraestrutura da nuvem.

O gerenciamento financeiro na nuvem ajuda os clientes a desenvolverem as habilidades e as ferramentas necessárias para concretizar todo o benefício econômico da nuvem através da jornada da AWS. Isso inclui o planejamento da migração ou a criação de um aplicativo para execução de seus negócios na nuvem em escala completa. O gerenciamento financeiro na nuvem é uma parte importante das conversas com clientes durante a fase de pré-venda, durante todo o processo de migração e após a migração. Há análises de redução de custos que podem ser feitas como parte da avaliação do portfólio de migração antecipadamente no processo, além de outras partes do gerenciamento financeiro na nuvem a considerar após a migração. Isso é discutido em mais detalhes na lição Gerenciamento financeiro na nuvem.

Como as conversas sobre os aspectos econômicos com os clientes aceleram a tomada de decisões e ajudam os clientes a migrarem para a AWS? Os aspectos econômicos na nuvem ajudam a criar um caso de negócio para a AWS analisando ambientes on-premises e quantificando o valor percebido pela migração. Isso ajuda os clientes a obterem confiança em sua decisão de compra.

Quando os aspectos econômicos na nuvem criam um caso de negócio em oportunidades de migração, percebemos que temos mais probabilidade de ganhar negócios, o uso do cliente aumenta mais rapidamente e o ciclo de vendas é reduzido. Isso conclui este vídeo. Continue no curso.

### Valor Comercial
A conversa e a análise do valor comercial ajudam você a abordar os componentes financeiros que normalmente são as principais preocupações dos clientes em potencial.

Ao desenvolver um caso de negócio, lembre-se de que o objetivo não é criar um forecast financeiro com 100% de precisão. Em vez disso, você quer que o cliente tenha todos os dados necessários para tomar uma decisão de compra com confiança. Os clientes percebem isso nos vários estágios durante a análise e, quando atingem esse ponto, você conclui seu trabalho. No geral, seu trabalho em uma interação de valor comercial é remover os problemas financeiros principais. Quando isso é feito, uma análise de valor comercial não é mais necessária.

No entanto, nem a conversa nem a análise fornecem o valor completo para o cliente. O valor é entregue por meio de atividades, como provas de conceito, revisões de arquitetura, migração de cargas de trabalho e assim por diante. A análise do valor comercial facilita o avanço para essas atividades posteriores. Portanto, as interações sobre o valor comercial devem ser as mais rápidas e eficientes possíveis, para que seja possível conversar sobre outras áreas importantes.

Faça a transição do cliente para uma prova de conceito, para que ele possa começar a perceber o valor real. Os solutions architects da AWS trabalham com centenas de casos de negócios de clientes e testemunham áreas em que os clientes percebem e quantificam valores. A AWS desenvolveu o Cloud Value Framework como uma maneira de considerar o valor da nuvem.

O framework é composto de cinco pilares: redução de custo, produtividade da equipe, resiliência operacional, agilidade empresarial e sustentabilidade.

Normalmente, a redução de custos é o fator principal que motiva os clientes a migrarem para a nuvem. Embora o custo seja importante, os outros quatro pilares do framework promovem um valor comercial ainda maior e devem ser enfatizados nas conversas sobre valor comercial com o cliente.

Para ter conversas bem-sucedidas, é necessário ter uma boa base de todos os cinco pilares. 

* A redução de custos é realizada evitando as infraestruturas on-premises com grandes gastos fixos e reduzindo a variável de gastos contínuos usando as economias de escala das ofertas da AWS.
* A produtividade da equipe é medida em resultados maiores pela equipe do mesmo tamanho porque muito do trabalho tático anterior não é mais necessário.
* A resiliência operacional é conquistada com maior disponibilidade e segurança e menor tempo de inatividade.
* A agilidade empresarial consiste nos novos produtos, nas novas expansões de geolocalização ou de mais recursos dos produtos existentes que os clientes podem fornecer.
* A sustentabilidade é a redução do impacto ambiental das operações de TI.

### Redução de Custos
A redução de custos se refere a quanto os clientes pagam pela TI tradicional em comparação com o que pagariam usando a AWS, em números reais. Como AWS Partner, você precisa compreender a redução de custos e como discuti-la de forma eficaz para que os clientes vejam como a AWS pode ajudar a reduzir custos.

Uma ferramenta principal para informar sobre a redução de custos aos clientes é uma análise de redução de custos. Uma análise de redução de custos calcula o custo total de propriedade, que são os custos de aquisição e operacionais, para comparar a execução de um ambiente de TI tradicional completo on-premises com a implantação da AWS. Use uma análise de redução de custos para ajudar o cliente a comparar custos e criar um caso de negócio para fazer a transição para a AWS. Muitas vezes, o maior desafio dos clientes é compreender o verdadeiro escopo de seus custos atuais.

Agora, vamos explorar como os clientes podem reduzir custos com a AWS.

Imagine um cenário em que o cliente deseja iniciar um novo aplicativo. Com a infraestrutura tradicional, o cliente começa planejando e definindo o escopo da arquitetura e identifica os servidores necessários para executar o aplicativo. O cliente cria uma ordem de compra e a envia para a pessoa ou o departamento apropriado na empresa.

Neste ponto, o cliente entra no jogo da espera. Como a maioria sabe, o ciclo normal de aquisição pode levar de algumas semanas a alguns meses. Enquanto aguarda pela aprovação da ordem de compra, o cliente prepara o data center garantindo que haja espaço, energia e resfriamento suficientes e outra infraestrutura de suporte de back-end.

O que acontece normalmente durante esse período de espera? Os requisitos do hardware pedido já não parecem ser a melhor opção ou o cliente pode perceber que o pedido está acima ou abaixo das necessidades atualizadas.

A AWS ajuda os clientes a reduzirem os custos de três maneiras principais: o modelo baseado em consumo, os modelos de preços e as frequentes reduções de preços da AWS.

Primeiro, vamos explorar um modelo baseado em consumo. Com um modelo baseado em consumo, os clientes da AWS pagam apenas pelo que usam em vez de pagar adiantado pelo que acham que precisarão no futuro. Por exemplo, ao superprovisionar, o cliente implanta mais servidores do que precisa e acaba com recursos não utilizados. Ao subprovisionar, o cliente implanta poucos servidores e experimenta problemas no desempenho dos aplicativos, além do custo da oportunidade de não atender à demanda. Nos dois casos, os trade-offs são ineficiência e perda financeira.

Com a AWS, os clientes podem evitar ineficiências e perdas financeiras iniciando a infraestrutura de que precisam quando precisam. Com esse modelo, a superprovisão e a subprovisão não são mais problemas. Os clientes alinham a infraestrutura, serviços e custos aos padrões de uso.

Com a AWS, os clientes podem otimizar suas despesas correspondendo o modelo de uso com os requisitos das cargas de trabalho por vencimento e comportamento. Há três modelos de preços gerais para a compra de recursos de computação do Amazon Elastic Compute Cloud (Amazon EC2).

Os preços de instâncias sob demanda permitem que os clientes paguem pela capacidade computacional que realmente usam por hora, sem compromissos de longo prazo. É possível usar esse modelo de preços para cargas de trabalho com vários graus de disponibilidade, como um ambiente de sandbox ou de um projeto com um cronograma limitado. Se os requisitos de disponibilidade média de instâncias do Amazon EC2 forem maiores que aproximadamente 70 horas por semana, poderá ser mais vantajoso colocar esses ambientes em um modelo de preços diferente.

O Savings Plans e as instâncias reservadas são modelos flexíveis que oferecem preços mais baixos em comparação com os preços sob demanda, em troca de compromissos de uso específico em um período de um a três anos.

As Spot Instances do Amazon EC2 oferecem capacidade computacional de reserva na nuvem AWS, com grandes descontos em comparação com as instâncias sob demanda. As Spot Instances permitem economizar até 90% em comparação com as instâncias sob demanda e são melhores para cargas de trabalho tolerantes a falhas, como processamento em batch, renderização e cargas de trabalho em contêiner. 

Por fim, a AWS diminui os custos com a redução contínua dos preços. A AWS opera em grande escala, o que possibilita aumentar a eficiência e reduzir os custos. Repassamos a economia para nossos clientes por meio das reduções de preços. Sempre que reduzimos os preços, todos os clientes da AWS percebem a economia imediatamente. Quando ocorrem reduções de preços, os clientes recebem os preços mais baixos automaticamente. Não precisam nos ligar, entrar em contato com um gerente de conta, renegociar um contrato ou solicitar uma redução de preço.

Por exemplo, quando a AWS reduziu o preço do Amazon Simple Storage Service Glacier (Amazon S3 Glacier) em 30%, todos os clientes do S3 Glacier começaram a pagar 30% a menos imediatamente naquele mês. Os clientes puderam usar a economia para buscar novos projetos. 

Da mesma forma, quando a AWS reduziu o preço dos snapshots do Amazon Elastic Block Store em 47%, os clientes viram um impacto imediato semelhante.

#### Análise de Redução de Custo
Para começar uma discussão sobre a análise de redução de custos, considere o cenário tradicional de TI que é baseado em despesas de capital fixas, longos ciclos de planejamento e de vários componentes que o cliente precisa comprar, criar, gerenciar e atualizar ao longo do tempo. Alguns desses elementos são difíceis de quantificar, e outros são facilmente negligenciados. Para otimizar suas discussões com os clientes, você precisa entender como eles geralmente visualizam os custos relacionados à TI.

Este diagrama ilustra como os clientes normalmente visualizam os custos. Ele inclui os importantes buckets de custos: computação, armazenamento, redes e mão de obra. Na vida real, o custo total é mais complexo e se parece mais com isso, que inclui itens adicionais. Por exemplo, custos de instalações, como energia, espaço e resfriamento. Mesmo que um cliente não veja isso diretamente como um item de linha na declaração de lucros e perdas, ele estará certamente pagando por esses custos, e o grupo de CFO estará ciente disso.

Esse diagrama também mostra extras, que podem incluir custos organizacionais compartilhados adicionais que talvez não sejam visíveis para todas as partes na organização. Dependendo da organização, especialmente em organizações maiores, o rastreamento de cada item de linha, que deveria estar incluído em uma análise integral de redução de custos, pode ser desafiador. Portanto, antes de fazer uma análise de redução de custos, é necessário entender como o cliente vê seus custos e com quais suposições razoáveis ele concorda. Isso ajuda a saber o que incluir na redução de custos e o que deve ser visualizado como suposição. Evite desperdiçar ciclos com itens que podem não ter um impacto material sobre a análise.

Ao realizar uma análise da redução de custo, você precisa considerar as muitas facetas do processo. Uma das facetas mais importantes é garantir que todos os stakeholders estejam incluídos na primeira conversa e sejam mantidos no loop continuamente. Isso significa que TI, finanças e outros membros da organização envolvidos na adoção da nuvem devem ser incluídos na reunião inicial.

O segundo fator importante é que o cliente deve ser o proprietário da análise. Portanto, a análise deve ser realizada de forma colaborativa, e o cliente deve poder falar sobre cada item da linha com confiança. Em uma interação típica, o cliente apresentará os resultados da análise à liderança da empresa, portanto, é essencial que esteja capacitado a compreender e defender os resultados da análise. Obter o apoio da liderança é essencial para que as migrações para a nuvem sejam bem-sucedidas.

Outra prática recomendada é usar percentuais realistas dos picos de uso de CPU e de RAM ao dimensionar corretamente de on-premises para a AWS. Geralmente, os servidores não operam em pico de throughput 100% do tempo. Se o cliente não tiver esses dados, verifique se ele concorda em usar as médias do setor ou use uma ferramenta de varredura que possa coletar essas informações.

O uso de percentuais realistas ajuda a dimensionar um ambiente da AWS baseado no que o cliente realmente precisa, em vez de simplesmente replicar todos os servidores on-premises na nuvem. Essa abordagem de dimensionamento correto é essencial para entregar uma redução de custos significativa na análise e, portanto, não deve ser ignorada.

Por fim, inclua sempre os benefícios do valor comercial em seu caso de negócio. Os fatores de valor comercial incluem produtividade da equipe, resiliência operacional, agilidade empresarial e sustentabilidade (os outros quatro pilares do Cloud Value Framework.)

O que não funciona? Primeiro, evite focalizar apenas o preço. Uma discussão sobre preços não é uma discussão sobre redução de custos. Os clientes geralmente começam dizendo que uma infraestrutura on-premises é mais econômica que a AWS. Muitas vezes, o que o cliente quer que você faça é ajustar os preços da AWS para reduzir o custo. A melhor maneira de abordar isso é analisar a redução de custos dos clientes e examinar mais profundamente os custos on-premises. Normalmente, essa abordagem mostra que os custos on-premises são realmente muito mais altos que o estimado inicialmente porque o cliente não inclui elementos de custos, como cabeamento, energia, resfriamento e instalações.

Ao dimensionar corretamente o ambiente da AWS e usar o modelo de preços correto para a carga de trabalho, é possível criar uma comparação justa que, provavelmente, mostrará que a AWS é a opção mais econômica.

Naturalmente, isso não significa que os preços da AWS não devem ser abordados. Os preços são um tópico importante. No entanto, é função do gerente de conta na AWS desenvolver um programa especial de preços ou de descontos que possa reduzir os custos do cliente. Assim que o gerente de conta na AWS do cliente confirmar os preços, eles devem ser integrados à análise.

O próximo item que não funciona é a abordagem de lift and shift pura. Se um processo for ineficiente em um ambiente, por que movê-lo como está para outro ambiente? Por exemplo, em uma infraestrutura on-premises, as cargas de trabalho pequenas às vezes são executadas em grandes máquinas, mas essa abordagem é desnecessária na AWS.

O terceiro item que não funciona é ter uma única pessoa executando toda a análise. Conforme discutido anteriormente, esse é um grande risco. Um ambiente de TI é muito complexo para uma só pessoa captar. O suporte da equipe é necessário para executar um caso de negócio abrangente e confiável.

Por fim, dependendo da empresa, a análise da redução de custos pode levar semanas ou até mesmo meses. Portanto, quanto mais cedo a reunião inicial acontecer, melhor. Você e os clientes precisam saber quais são as principais datas e os processos de aprovação necessários. Se o cliente indicar que gostaria que essa análise fosse realizada, inicie o processo o mais rápido possível.
### Produtividade da Equipe
No Cloud Value Framework, a produtividade da equipe se refere à eficiência adquirida com a redução ou a eliminação das tarefas não mais necessárias com os serviços de nuvem. Por exemplo, ao migrar para a AWS, a equipe do cliente gastará menos tempo na infraestrutura e terá mais tempo para se concentrar em novos projetos com impacto estratégico no negócio.

À medida que as empresas migram para a AWS, surgem alguns padrões comuns no nível da equipe de TI. O trabalho tático e indiferenciado necessário anteriormente nos data centers tradicionais, como aquisição, configuração e manutenção de hardware, não é mais necessário. Isso economiza tempo da equipe e reduz o tempo de inovação.

Com a AWS, os recursos dos clientes podem migrar para um trabalho mais estratégico. À medida que a maturidade da AWS aumenta, os clientes aprendem a aprimorar ainda mais seus negócios com a AWS. Eles adotam novos serviços e tecnologias, o que pode resultar em redução de custos adicionais e tempo de entrada no mercado acelerado. Os membros da equipe de TI que costumavam trabalhar em projetos, como implantações de ambientes de armazenamento e atualizações de servidores, podem fazer a transição para se tornarem especialistas em DevOps. Ao serem integrados à equipe de desenvolvimento, eles podem oferecer suporte ao desenvolvimento de novos produtos e serviços. Na AWS, usamos benchmarking para quantificar o valor que os clientes percebem na área de produtividade da equipe. A equipe de aspectos econômicos na nuvem inclui esses benefícios sempre que cria um caso de negócio de migração para um cliente. Também é possível quantificar os benefícios da produtividade da equipe avaliando as funções individuais de TI do cliente em um nível detalhado e aplicando alguma lógica de como cada função será afetada por uma migração para a nuvem.

A AWS analisa seis categorias principais de funções relacionadas à TI: servidor, rede, armazenamento, aplicativo, instalações e segurança. Embora cada organização seja diferente, descobrimos que essas são as funções típicas. As três primeiras funções de TI, servidor, rede e armazenamento, são centradas no gerenciamento da infraestrutura de hardware. As funções comuns incluem administradores, implementadores e engenheiros. A produtividade da equipe também inclui funções de aplicativos cobertas por funções como database administrators, AppDev, QA e funções de suporte. As funções de instalações abrangem principalmente o gerenciamento das instalações e incluem funções para clientes que têm um data center on-premises. Por fim, as funções de segurança ajudam as empresas a garantir que sua infraestrutura atenda aos padrões de conformidade, normativos e corporativos.

Cada função tem uma ou mais funções para apoiá-la. Cada função tem aproximadamente 10 a 15 atividades principais. Em nosso modelo de cálculo dos benefícios, que você verá no vídeo a seguir, estimamos o tempo gasto em cada uma dessas atividades antes da migração para a AWS e calculamos a redução no tempo gasto após essa migração, quando aplicável.

Para ajudar os clientes a compreenderem e se sentirem seguros com os benefícios ao migrarem para a AWS, é possível usar algumas práticas recomendadas. Durante a criação de um caso de negócio de migração, é possível coletar informações sobre as funções e responsabilidades da TI e da equipe de desenvolvimento do cliente. É possível aplicar os benchmarks que são mostrados depois deste vídeo para criar uma estimativa dos benefícios da migração para a produtividade potencial da equipe. Isso ajuda o cliente a começar a pensar além da redução de custos e a considerar o valor comercial muito mais estratégico de adotar a AWS.
### Resiliência Operacional
A resiliência operacional é o benefício conquistado com a melhoria na disponibilidade e na segurança. Isso representa mais tempo ativo, menos tempo de inatividade e risco reduzido. Ao pensar em resiliência operacional, duas coisas vêm à mente: tempo ativo e segurança. Manter uma infraestrutura operacionalmente resiliente e disponível envolve vários componentes, da camada de rede, servidores e armazenamento, à camada de banco de dados. Cada componente de um aplicativo precisa estar disponível.



O tempo de inatividade resulta em efeitos macro para as empresas, muitas vezes com consequências significativas. Por exemplo:

Uma interrupção no data center de uma empresa aérea cancelou 2.000 voos e custou mais de 150 milhões de dólares. 
Um banco experimentou um longo tempo de inatividade por causa de um ataque de negação de serviço distribuído (DDoS), o que afetou a confiança dos clientes. 
Um aplicativo de forecast de vendas impossibilitou o envio de orientações ao The Street, provocando uma interrupção nas vendas e nas finanças e, por fim, causando a inabilidade de reportar orientações para Wall Street. 
Um importante varejista sofreu uma violação de dados, que custou 252 milhões de dólares.
Em geral, é evidente que grande parte das perdas envolveu uma redução na resiliência operacional. Os impactos do tempo de inatividade não são baratos. 

Esses eventos de tempo de inatividade custam às empresas da Fortune 1000 entre 1,25 e 2,5 bilhões de dólares anualmente, com prejuízos por falhas em aplicativos essenciais que chegam a 1 milhão de dólares por hora.
Em 2020, o tempo de inatividade médio de uma única interrupção foi de 79 minutos, a um custo médio de USD 84.650 por hora. 
A recuperação de ataques cibernéticos custa em média USD 4,6 milhões para as organizações, sem incluir qualquer pagamento de ransomware ao invasor. 
Esses custos de tempo de inatividade incluem:

* Taxas de terceiros
* Substituição de equipamentos
* Custos incidentais após o ocorrido
* Atividades e custos de recuperação
* Custos de detecção associados à descoberta inicial e investigações subsequentes
* Equipe de TI improdutiva e custos de usuários finais
Perda de receita
* Custos de interrupção dos negócios
Muitas vezes, as causas do tempo de inatividade não são os ataques externos. O tempo de inatividade costuma ocorrer porque a demanda de serviços excede a capacidade da infraestrutura para atendê-la. É por isso que o tempo de inatividade geralmente ocorre durante os horários de pico, enquanto o banco de dados está com um número excessivo de consultas.

Ao quantificar o impacto, usamos uma pesquisa líder de terceiros para ajudar a orientar os negócios. Aqui, uma informação interessante é que o custo da interrupção dos negócios é maior que o custo da perda de receita. Isso significa que o prejuízo para a marca da empresa, a rotatividade dos clientes e a perda de oportunidades são maiores que a perda da receita. Mesmo para aplicativos internos, os impactos na produtividade dos negócios geram custos de downstream muito elevados para uma empresa. Além disso, a interrupção dos negócios é equivalente às perdas econômicas, incluindo danos à reputação, rotatividade dos clientes e perda de oportunidades.

#### Segurança
Agora, vamos explorar algumas das causas de violações de segurança. Elas incluem:

* Malware, como worms e vírus
* Ataques de rede, como portas abertas e pacotes fragmentados
* Aplicativos ou sistemas operacionais sem aplicação de patches
* Problemas de segurança, como divulgações de senhas e credencias não armazenadas com segurança
* E autenticação precária ou limitada
Lembra-se do Mike? Logo depois que ele terminou de limpar a sujeira do café, alguém pediu para ele alocar um espaço para armazenar dados sigilosos que exigem conformidade com regulamentações de integridade.

O Mike não tinha um armazenamento em conformidade disponível e decidiu armazenar os dados temporariamente descriptografados. Afinal, a nova matriz de armazenamento que foi solicitada para essa carga de trabalho deveria chegar em poucos dias. O que são alguns dias? Nada demais, certo? Bem, nesse mesmo dia, um hacker detectou uma vulnerabilidade no data center de Mike e baixou os dados sigilosos.

Por que isso não aconteceria com a AWS? Por que Mike não precisaria tomar uma decisão subjetiva. Em vez disso, todos os recursos são acessíveis rapidamente. Mike poderia ter provisionado armazenamento criptografado, em conformidade com as regulamentações de integridade em poucos minutos.

A AWS tem um modelo de segurança que compartilha as responsabilidades de segurança com os clientes. Nesse modelo, a AWS é responsável pela segurança de tudo, do nível do hipervisor ao sistema operacional.

Isso ajuda a reduzir os riscos de segurança de várias maneiras, como:

* Usar a automação e as ferramentas da AWS para ajudar os clientes a minimizar os riscos de segurança mais graves, incluindo DDoS
* Fornecer o serviço AWS Identity Access Management (IAM) para gerenciar centralmente usuários e credenciais
* Usar uma lista de mais de 30 certificações e credenciamentos de conformidade para ajudar nossos clientes a criarem ambientes seguros e em conformidade
#### Operações
Vamos analisar algumas causas principais de falhas operacionais. Elas incluem: 

* Erros humanos, como a falta de procedimentos claramente definidos ou privilégios de usuário
* Erros de configuração nas definições do hardware ou do sistema operacional e scripts de inicialização
* Erros de procedimentos, como restaurar o backup incorreto ou esquecer-se de reiniciar um dispositivo
* E acidentes comuns no data center, como tropeçar nos cabos, derrubar o equipamento ou desconectar dispositivos

Por exemplo, suponha que um funcionário, Mike, entre em um data center e coloque seu café sobre um servidor.

Todos sabem que a probabilidade do café de Mike cair sobre o servidor é proporcional à importância do servidor. Aqui, em primeiro lugar, o fator humano é que nem Mike nem qualquer outra pessoa deve entrar em um data center com uma caneca de café. Mas Mike é humano, e humanos cometem erros, principalmente quando se sentem muito confiantes.

Por que isso não acontece na AWS? Temos todos os ingredientes necessários: café, servidores e humanos. Mas a maioria dos clientes executa um data center por necessidade, e não porque esse seja o seu negócio. Seu negócio pode ser qualquer coisa, da execução de um site de encontros à produção de empilhadeiras, mas provavelmente não é gerenciar data centers. A execução de data centers é o nosso negócio. E, por esse motivo, somos muito cuidadosos com as nossas regras e as seguimos rigorosamente.

O foco da AWS é a alta segurança e a contratação dos melhores recursos para que possamos identificar ameaças antecipadamente e evitar desastres. Mesmo que tenhamos um contratempo, nosso nível de resiliência, disponibilidade e redundância nos permitirá recuperar de modo que a maioria dos nossos clientes não vai nem perceber.

Como a AWS ajuda a mitigar as interrupções operacionais e os desastres? A AWS usa a automação; gerencia serviços de ponta a ponta; proporciona a visibilidade de todo o sistema para uso, desempenho e métricas operacionais; usa a configuração de segurança e de governança dos recursos da AWS e monitora o acesso à API.
#### Software
Vamos analisar algumas causas comuns de falhas na resiliência do software. Elas incluem:

* Esgotamento de recursos, como processos descontrolados, vazamentos de memória e aumento de arquivos
* Erros de computação ou de lógica, como referências incorretas, indicadores corrompidos e erros de sincronização
* Monitoramento inadequado, como inabilidade de identificar problemas
* Atualizações com falha, como intercompatibilidade e integrações
* A AWS oferece serviços para que os clientes possam aumentar ou reduzir os recursos necessários e fazer com que a AWS gerencie as alterações. 

Para fornecer resiliência de software, a AWS:

* Oferece implantações azuis/verdes que permitem reversões rápidas
* Automatiza a integração e o fluxo de trabalho de entrega contínuos
* Executa implantações de código menores para reduzir bugs de unidade, de integração e do sistema
* Fornece recursos atuais e seguros com aplicação de patches do sistema operacional
* Cria e gerencia um conjunto de recursos relacionados da AWS
#### Infraestrutura
Agora vamos analisar algumas causas de falhas na infraestrutura. Elas incluem:

* Falha de hardware de servidores, armazenamento ou redes
* Desastres naturais, como furacões, inundações e terremotos
* Interrupções de energia, como falha no fornecimento de energia e nas baterias
* Ataques volumétricos, como DDoS e amplificação do Sistema de nomes de domínio (DNS)

A AWS ajuda a reduzir falhas na infraestrutura de várias maneiras.

* A AWS continua a expandir nossa infraestrutura e lidera o setor em melhorias de data centers em grande escala.
* Nossos clientes podem executar aplicativos e fazer failover em várias zonas de disponibilidade e regiões.
* Os sistemas da AWS são criados para serem altamente disponíveis e duráveis.
* Como padrão, cada zona de disponibilidade em cada região é conectada de modo redundante a vários provedores de trânsito de camada 1.
* Cada instância de computação é atendida por duas fontes de energia independentes, cada uma com serviço público, fonte de alimentação ininterrupta e gerador de energia de backup.
### Agilidade Empresarial
A agilidade empresarial significa entregar mais, por exemplo, responder mais rapidamente, fazer mais experiências e entregar resultados no mesmo tempo ou antes. Trata-se da habilidade de agregar mais valor aos clientes. Por exemplo, a agilidade empresarial pode promover o desenvolvimento de produtos, a expansão de novos mercados e a capacidade de resposta do stakeholder interno ou externo.

A agilidade empresarial é uma ampla área de valor que basicamente abre mais oportunidades para os clientes experimentarem e responderem com mais rapidez às mudanças das condições do negócio. Aqui, você pode ver uma lista independente do setor baseada nos principais indicadores de desempenho, ou KPIs, nos quais nossos clientes percebem valor.

Essa lista parcial de métricas abrange várias áreas da agilidade empresarial e pode ser um bom ponto de partida para os clientes.

Depois deste vídeo, você aprenderá como a AWS pode ajudar revisando os estudos com estas três métricas principais:

* Tempo de entrada no mercado de novos recursos de aplicativos
* Tempo médio para liberações em produção (dias úteis)
* Tempo necessário para transformar dados brutos em informações acionáveis

#### Inovação ao reduzir riscos e custos
Algumas das atividades mais importantes que uma empresa íntegra deve manter para continuar a crescer e inovar são o escopo, a priorização e a adoção de novas iniciativas. É possível imaginar o processo de iniciativa como um funil de projetos.

A TI oferece suporte a muitas iniciativas. A maioria das organizações com uma infraestrutura on-premises deve analisar com cuidado como e quando usar recursos limitados na busca de cada iniciativa. A AWS oferece às organizações mais flexibilidade.

Por exemplo, imagine uma organização que começa com 20 boas iniciativas. Em vez de escolher uma, ela configura um ambiente de teste e desenvolvimento em minutos e experimenta cada iniciativa. Após a primeira rodada de testes, ela decide implantar 10 das iniciativas usando os produtos e serviços flexíveis da AWS. Com o tempo, ela constata que apenas duas iniciativas são bem-sucedidas a longo prazo. Durante todo esse processo, a organização encerra cada iniciativa com falha sem o trabalho e os recursos desperdiçados associados a um ambiente on-premises não flexível. Isso é o que significa falhar rapidamente e reduzir os custos da falha.

Embora esse exemplo seja muito simplificado, os clientes podem conquistar o poder e a flexibilidade para colocar mais projetos potenciais no funil para consideração. Essa capacidade acelera a concretização de projetos, o que costuma aumentar os sucessos e reduzir as consequências derivadas de falhas.
### Sustentabilidade
A sustentabilidade se tornou uma meta para a maioria das organizações. Resumindo, a sustentabilidade significa evitar o esgotamento dos recursos naturais para manutenção do balanço ecológico.

A sustentabilidade toca muitas áreas da economia, de como descarbonizamos nossas operações empresariais à conservação da água, ao emprego responsável. Ela sustenta a economia circular com zero aterro sanitário e reciclagem.

A Amazon está compromissada a criar um negócio sustentável para nossos clientes e para o planeta. Em 2019, a Amazon se tornou a cofundadora do The Climate Pledge, um compromisso de ser carbono zero líquido em nossos negócios até 2040, 10 anos antes do Acordo de Paris. O The Climate Pledge já tem mais de 375 signatários. A Amazon está no caminho de atingir 100% de energia renovável até 2025, cinco anos antes do compromisso original de 2030. Em junho de 2020, a Amazon anunciou o The Climate Pledge Fund, que inclui um financiamento inicial de USD 2 bilhões para investir em empresas visionárias cujos produtos e soluções facilitarão a transição para uma economia de baixo carbono.

Vamos ver como a AWS pode ajudar. A AWS pode ajudar os clientes a conquistarem suas metas de sustentabilidade e a reduzir suas pegadas de carbono em várias áreas:

* Infraestrutura energeticamente eficiente da AWS
* Servidores mais eficientes e maior utilização de servidores
* Consumo reduzido de eletricidade e uso de energia renovável

Por que a AWS é mais eficiente? Nossa escala permite alcançar uma utilização de recursos e eficiência energética muito maiores do que um data center on-premises típico. Desde a infraestrutura altamente disponível que alimenta nossos servidores, até as técnicas que usamos para resfriar nossos data centers e os designs de servidor inovadores que fornecemos aos clientes, a eficiência energética é uma meta principal de todas as partes da nossa infraestrutura global.

A infraestrutura global da AWS é baseada em hardware personalizado da Amazon, desenvolvido e otimizado com finalidade específica para as cargas de trabalho executadas pelos clientes da AWS. A AWS sempre teve e continua com um foco preciso na melhoria da eficiência em todos os aspectos da nossa infraestrutura. A história não acaba após a migração. Após a migração para a AWS, os clientes podem otimizar o consumo de recursos da AWS para obter reduções continuadas da pegada de carbono da carga de trabalho.

A maioria dos clientes começa com coisas relativamente fáceis, por exemplo:

* Usar o Programador de instâncias da AWS para desligar a computação quando não estiver em uso.
* Escolher a tecnologia sem servidor quando possível.
* Usar instâncias baseadas no AWS Graviton.
* O AWS Graviton3 é nosso processador mais eficiente em termos de energia, que usa até 60% menos energia para obter o mesmo desempenho que as instâncias comparáveis do Amazon EC2.
* Usar o AWS Cost Explorer para recomendações de dimensionamento correto das cargas de trabalho.

A AWS iniciou a ferramenta de visualizações de dados da pegada de carbono para fornecer aos clientes as seguintes informações:

* Calcular as emissões de carbono geradas pelas cargas de trabalho da AWS.
* Visualizar o histórico da pegada de carbono e analisar as alterações das emissões ao longo do tempo.
* Fazer o forecast das emissões que mostram como a pegada de carbono de um cliente será alterada enquanto a Amazon permanece no caminho de capacitar suas operações com 100% de energia renovável até 2025 e atingir a marca de carbono zero líquido até 2040 como parte do compromisso com o Climate Pledge.
* A ferramenta de pegada do carbono está disponível no AWS Billing Console e ajuda a apoiar os clientes em sua jornada para a sustentabilidade.