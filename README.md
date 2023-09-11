Repositório D&A - Compass UOL
=============================
Repositório destinado para a trilha de atividades da Compass - UOL;  
Armazenamento de: Anotações e códigos dos assuntos estudados durante o programa de bolsas;

## Apresentação  
**🧔Nome:** [Lucas Dias Squinca];  
**👴Idade:** [18];  
**🏡Cidade:** [Mirandópolis/SP];  
**👨‍💻Curso:** [Sistemas de Informação];  
**🏫Instituição de ensino:** [Universidade Federal de Mato Grosso do Sul - UFMS CPTL (Três Lagoas)];  
**⌚Semestre:** [2º];  
**🏃Hobbies:** [Cozinhar | Academia | Livros];  
**📖Livros Preferidos:** [Bíblia | Dom Casmurro | Viagens à minha terra | Bons Dias!];  
**✨Animes Preferidos:** [Black Clover | Ousama Ranking | Spy X Family | Anohana | Tonari to Totoro | Sen to Chihiro no Kamikakushi];    
**🛠️Experiências:** [None];  
**📁Portfólio:** [[nicitov.github.io]][Portfólio];
------
>### **João 3:16 "Porque Deus amou o mundo de tal maneira que entregou o seu Filho unigênito para que todo aquele que nEle crê nao pereça, mas tenha a vida eterna".**
------
## Redes Sociais
[![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white)][Stack Overflow]
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)][Instagram]
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)][LinkedIn]
[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)][Twitter]

## Aprendendo...
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
---------------
## Segurança em aplicações Web

## Métodos ágeis de A a Z

## Sprint #1
- ### *Git & GitHub*
    ### Para acessar o certificado [clique aqui](/Sprint_1/Git_&_Hub/Certificado/)
    >### Este resumo tem como objetivo exemplificar o uso de Git e GitHub bem como os comandos mais usados. Para entrar em mais detalhes, acesse o *[arquivo completo](/Sprint_1/Git_&_Hub/README.md)*
    Antes de abordar plenamente sobre Git e GitHub, é importante detalhar o que é **controle de versão**:

    Controle de versão é um modo de trabalhar com o código fonte em uma aplicação. Possibilita o trabalho conjunto.  
    Existem algumas ferramentas que permitem o trabalho com o código fonte, dentre elas temos o **Git**.

    **Git** é um programa de controle de versão que se baseia no controle de repositórios. Nele, qualquer pessoa pode compartilhar e modificar projetos.
    ### Repositórios no Git
    É onde o código é armazenado. Geralmente são ligados a um servidor de gerenciamento de repositórios (GitHub).
    ### GitHub
    É um serviço de gerenciamento de repositórios amplamente usado;
    É nele que disponibilizamos os nossos códigos com outros dev's;
    ### Abas do GitHub
    - **Code:** Nela temos acesso aos arquivos, ao readme, a licença do projeto, criação de branches, etc;
    - **Issue:** Nele organiza-se problemas e tarefas e serem feitos, designando os responsáveis pelas tarefas;
    - **Pull Request:** Onde os códigos são enviados para uma avaliação. Quando aprovado, será enviado ao repo remoto principal;
    - **Actions:** Aba para criação de automatizações. Por exemplo, automizar um "git push" todo dia 12 às 14 horas;
    - **Projects:** Aba para criação de um quadro de tarefas a serem feitas. As notas criadas podem virar issues. Semelhante a sites de gerenciamento de tarefas, como Trello e Monday.com;
    - **Wiki:** Aba para criação de praticamente uma "Wikipédia" do seu projeto. Criação de uma documentação mais extensa do projeto;
    - **Insights:** Aba que mostra a linha de desenvolvimento do projeto do iníco ao fim;
    - **Settings:** Aba de configurações (mudar nome do projeto, ver contribuidores, etc.);
    - **Gist:** Onde podemos adicionar pequenos blocos de códigos e salvá-los;
    ### Ligando um repositório ao GitHub
    #### Siga os seguintes passos:
        echo "# <nome_repo_github>" >> README.md
        git init
        git add README.md
        git commit -m "first commit"
        git branch -M main
        git remote add origin https://github.com/<usuario_github>/<nome_repo_github>.git
        git push -u origin main
    ### Comandos fundamentais do Git
        git status -> Verifica alterações no projeto;
        git add . -> Adiciona arquivos "untracked";
        git commit -a -m <mensagem> -> Salva todas as alterações;
        git push -> Envia as alterações para o repositório remoto;
        git pull -> Recebe alterações do repositório remoto | alterações de branch;
        git clone <Url> -> Clona um repositório existente;
        git rm <arquivo> -> Remove um arquivo específico; do projeto;
        git log -> Histórico com todos os commits dados
        git mv -> Renomeia arquivos | Move arquivos dentro do repo;
        git checkout -> Desfaz alterações de um arquivo, ou seja, volta ao estado original;
        git reset --hard -> Desfaz todas as alterações já commitadas e as pendentes;
    #### **Podemos ignorar arquivos adicionando um arquivo .gitignore na pasta do repositório.**

    ### Branches
    Modo de separar diferentes versões de um projeto. Primeiramente, desenvolve-se uma parte e um projeto em uma branch e depois une-se a "main";
    #### Principais Comandos
        git branch <nome_branch> -> Cria branches
        git branch -> Visualiza Branches
        git branch -d <nome_branch> -> Deleta um branch específico;
        git checkout <nome_branch> -> Muda de branch;
        git checkout -b <nome_novo_branch> -> Cria um branch novo e automaticamente muda para ele;
        git merge <nome_branch> -> Une branches
        git stash -> "Salva" a ultima versão do seu código, permitindo alternativas diferentes de desenvolvimento. Quando executado, volta a última versão salva;
        git stash list -> Visualizar stashs existentes;
        git stash <nome_stash> -> Recuperar stash e trabalhar a partir do que está salvo nela;
        git stash clear -> Remove todas as stashs;
        git stash drop <nome_stash> -> Remove uma stash em específico;
        git tag -a <nome_tag> -m <mensagem> -> Cria uma tag;
        git show <nome> -> Verifica uma tag;
        git checkout <nome_tag> -> Muda de uma tag para outra;
        git push origin <nome_tag> -> Enviar tags para o repositório remoto;
        git push origin --tags -> Enviar todas as tags de uma vez;

    ### Compartilhamento e atualização
    #### Principais Comandos
        git fetch -> Atualiza e encontra branches não mapeados pelo Git;
        git remote -> Remove ou trackeia um repositório remoto;
        git remote add origin <link> -> Liga um repositório remoto existente ao seu repo Git da máquina (quando o repositório local ainda não está linkado a um repo remoto);
        git submodule -> Verifica submódulos;
        git submodule add <repositório> -> Adiciona submódulos;
        git push --recurse-submodules=on-demand -> Atualiza um submódulo (apenas ele);

    ### Análises e inspeção
    #### Principais Comandos
        git show -> Exibe uma gama de informações sobre o repositório;
        git show <tag_nome> -> Exibe informações sobre uma tag em específico;
        git diff -> Exibe as diferenças entre branches;
        git diff <arquivo1> <arquivo2> -> Exibe as diferenças entre diferentes arquivos;
        git shortlog -> Exibe informações resumidas sobre o repositório, as quais se agrupam por autor;
        git describe --tags -> Verifica todas as tags existentes em nosso projeto;

    ### Administrando o Repositório
    #### Principais Comandos
        git clean -> Remove todos os arquivos "untracked"
        git gc -> Otimiza o repositório em questão de performance;
        git fsck -> Checa a integridade de arquivos;
        git reflog -> Exibe todas as atividades feitas do projeto. Uma "linha do tempo";
        git reset --hard <hash> -> Avança ou retrocede entre hashs do reflog. Recupera arquivos com reflog;
        git archive --format zip --output main_files.zip main -> Cria um arquivo .zip do nosso repositório;

    ### Markdown
    #### Principais Comandos
    - Cabeçalhos: Iguais ao do HTML5;
        
            # = <h1>
            ## = <h2>
            ### = <h3>
            #### = <h4>
            ##### = <h5>
            ###### = <h6>
    - Ênfase: Negrito e Itálico;
            
            **<Seu texto em negrito aqui>**
            __<Seu texto em negrito aqui>__
        ```
            *<Seu texto em itálico aqui>*
            _<Seu texto em itálico aqui>_
        ```
            _**<Seu texto em negrito e itálico aqui>**_
    - Listas: Ordenada e Não Ordenada
        
            Ordenada:
                1. Primeiro ponto;
                2. Segundo ponto;
                3. Terceiro ponto;
            Não ordenada:
                * Primeiro ponto;
                * Segundo ponto;
                * Terceiro ponto;
    - Imagens:
            
            ![Texto_imagem](link_imagem)
    - Links:
            
            [Texto_link](Url_link)
    - Códigos: Colocar o código entre seis acentos graves

            ```
            <Seu código aqui>
            ```
        Podemos ainda estilizar com as cores da linguagem escrita:
            
            ```<Linguagem de programação>
            <Seu código aqui>
            ```
    - TaskList:

            [x] Task concluída
            [ ] Task não concluída
    ### Boas práticas no Commit
    É importante padronizar nossas mensagens nos commits para deixar o processo de criação claro, assim como para o desenvolvimento pleno de nosso projeto.  
    Podemos, para melhorar nossos commits:
    1. Fazer separação do entre o corpo e o assunto do commit;
    2. Desenvolver o assunto com no máximo 50 caracteres;
    3. Desenvolver o corpo do commit com no máximo 72 caracteres;
    4. Explicar, no commit, o "porque" e "como" **do commit**, não do que está escrito e sendo inserido no código;

>##### Para mais informações e explicações sobre Git e GitHub, não se esqueça de acessar o [README.md de Git e GitHub](/Sprint_1/Git_&_Hub/README.md) 😉
    
- ### *Linux*
    ### Para visualizar o certificado [clique aqui](/Sprint_1/Linux/Certificado/)
    >### Este resumo é dedicado a abordar teoricamente os principais fundamentos e códigos do Linux, para ter acesso o arquivo da teoria completa *[clique aqui](/Sprint_1/Linux/README.md)*
    O **linux** é um sistema operacional **open source** com diversas distribuições, que são versões diferentes do Linux, como: Debian, Ubuntu, Mint, Kali Linux, dentre outros;  
    Mas afinal, por quê existem tantas distribuições? Diferentemente de outros sistemas operacionais como Windows e MacOS, o Linux não trabalha com atualizações fixas que inviabilizam a utilização das anteriores. Pelo contrário, cada usuário é capaz de, por meio de alguma versão base, desenvolver uma nova versão do Linux com melhorias ou peculiaridades de seu interesse;  
    Agora, falando um pouco sobre o sistema, temos o Kernel, que é o coração de todo o sistema. Ele faz a ligação com os hardwares do computador, os quais entregam as respostas desejadas pelo usuário. Ou seja, é o Kernel que faz a comunicação entre usuário e hardware;
    
    ### *Quais são as principais vantagens do Linux?*
    1. É gratuito;
    2. É o principal sistema operacional para servidores Web;
    3. Grandes empresas utilizam com mais recorrência (AWS, Heroku...);
    4. Geralmente é requisito essencial para muitas vagas de emprego;
    5. A comunidade é extremamente ativa;
    6. Segurança elevada;
    7. Possui suporte nativo para muitas linguagens de programação;

    **Sintaxe geral dos comandos:** COMANDO -OPÇÕES ARQUIVOS/DIRETÓRIOS;  
    **Diretório:** É uma pasta com arquivos e/ou outras pastas inseridas nele;
    ### Principais comandos no Linux:
        + -> (ALGUNS COMANDOS PRECISAM DE AUTORIZAÇÃO DE DESENVOLVEDOR, PARA ISSO, USE: <sudo> <comando>)
        (NÃO SABE O QUE ALGUM COMANDO FAZ? USE: <comando> <--help> PARA INFORMAÇÕES DETALHADAS SOBRE ELE) 
            cd -> Usado para mudar de diretório;
            ls -> Mostra os arquivos e pastas do diretório atual;
            clear -> Limpa o terminal;
            cat -> Cria um arquivo ou possibilita a visualização de um arquivo;
            touch -> Usado para criar novos arquivos e modificar a data de alteração de um arquivo;
            man -> Manual completo do sistema;
            mkdir -> Cria diretórios;
            rm -> Remove diretórios;
            cp -> Copia diretórios e/ou arquivos;
            mv -> Move diretórios e/ou arquivos para outro destino;
            +apt-get upgrade: Atualiza aplicativos existentes no computador;
            +apt-get update: Atualiza os repositórios do computador
            +apt-get install: Instala pacotes/aplicativos;
            +apt-get purge: Remove pacotes/aplicativos;
            +apt-cache search: "Aba de busca" por aplicativos para instalar;
            grep -> Usado para procurar conteúdos específicos dentro de arquivos;
            find -> Encontar diretórios e/ou arquivos;
            +adduer -> Adicionar um usuário;
            +userdel -> Deletar um usuário no Linux;
            tar -czvf -> Compactar um arquivo ou diversos arquivos em um só (arquivo .tar);
            tar -xzvf -> Descompactar um arquivo (arquivo .tar);
            zip -r -> Compactar um arquivo em .zip;
            unzip -> Descompactar um arquivo .zip;
            groupadd -g <ID do grupo> <nome do grupo> -> Cria Grupos;
            usermod -a -G <nome do grupo> <nome do usuário> -> Move usuários para outros grupos;
            gpasswd -d <nome do usuário> <nome do grupo> -> Removendo um usuário de um grupo;
            ping -> Verificar se estamos conectados a um domínio;
            ifconfig -> Ver as configurações de rede do nosso sistema;
            hostname -I -> Ver o IP da nossa máquina;


    ### **Editores de texto mais famosos do Linux:**
     - Nano;      
    - VIM;  
    
    ### __Grupos no Linux:__  
    #### O que é? 
    Conjunto de usuários com a funcionalidade de facilitar o gerenciamento de permissões;  
    ### **Permissões no Linux:**  
    #### O que são permissões?  
    *É a possibilidade de alterarmos três estados dos arquivos/repositórios: Leitura; Escrita; Execução*  
    **Leitura:** Se os usuários poderão ler o arquivo (R -read)  
	**Escrita:** Se os usuários poderão escrever no arquivo (W - write)  
	__Execução:__ Se os usuários poderão executar o arquivo (X - execute) 

    #### Sintaxe das permissões: **1 222 333 444 -> drwxr-xr-x;** onde:  
        1 => Arquivo ou diretório;  
        2 => Permissões do owner;  
        3 => Permissões do grupo;  
        4 => Permissões dos usuários;  
        d => directory = diretório  
        r => read = ler  
        w => write = escrever/editar  
        x => executar  
        "-" => não há permissão  
    - #### Permissão numérica:
        Permissão designada a usuários, grupos e/ou owners por meio numérico.

            Comando: chmod xxx <file/dir>

        Significado dos números:

            0 = Sem permissão --  
            1 = Executar --x  
            2 = Escrever -w-  
            3 = Executar e Escrever -wx  
            4 = Ler r--  
            5 = Ler e Executar r-x  
            6 = Ler e escrever rw-  
            7 = Ler, escrever e executar rwx
    - #### Permissão simbólica:
        Permissão designada a owner, grupos e usuários por meio de símbolos.

            Comando: chmod <argumentos> <file/dir>

        Argumentos:

            + : Adiciona permissão a um arquivo ou diretório;  
	        - : Remove permissão a um arquivo ou diretório;  
	        = : Determina as permissões, substituindo as anteriores;  
	        u : Dono do arquivo;  
	        g : Grupos;  
	        o : Outros;  
	        a: Todos;
    ### Gerenciamento de Redes
    #### Como a Web funciona?
    Genericamente, enunciamos que a web funciona da seguinte maneira: Uma requisição "sai" da sua máquina e procura o servidor que receberá esta requisição, o qual enviará a resposta desejada até o seu computador;
    Nesse contexto, é importante destacar alguns componentes da rede essenciais para o funcionamento Web:

    1. DNS: É o "tradutor", aquele de traduz o IP de um servidor para um respectivo domínio;
    2. Portas: São "domínios diferentes" que resultam numa mesma resposta, mas com diferenças técnicas. Podemos citar:
        >HTTP;  
        >HTTPS;  
        >SSH;  
        >FTP;
    3. TCP: Protocolo de transmissão de dados da rede, o qual se preocupa com a confiabilidade dos dados;
    4. UDP: Protocolo para transmissão de dados, mas se preocupa com a velocidade de transmissão;

>##### Para informações mais completas sobre Linux e suas funcionalidades, acesso o [README.md](/Sprint_1/Linux/README.md) específico de Linux 😊

## Sprint #2

- ### SQL p/ análise de dados
    ### Para acessar o certificado, [clique aqui](/Sprint_2/SQL_análise_de_dados/Certificado/Certificado%20de%20conclusão%20SQL%20para%20análise%20de%20dados.jpg)

    >### Este é um resumo dos conceitos trabalhados no curso de SQl para análise de dados. Para ver o conteúdo completo [clique aqui](/Sprint_2/SQL_análise_de_dados/README.md)
    #### *O que é SQL?*
    É uma linguagem de programação usada para processar informações num banco de dados relacional. As informações armazenadas no banco de dados podem ser vista em formato tabular, com suas delimitações feitas por linhas e colunas;  
    #### Quais são os comandos básicos de SQL?

        SELECT -> Usado para selecionar colunas;
        DISTINCT -> Mostra somente linhas distintas, sem duplicação;
        WHERE -> Usado com uma <condição>, a qual determinará os dados que serão apresentados;
        ORDER BY -> Ordenar uma seleção de acordo com uma determinada <condição>;
        LIMIT -> Limita o nº de linhas em uma consulta;
        FROM -> Seleciona de onde os dados serão retirados / quais tabelas serão utilizadas;
    
    #### Operadores
    ##### De comparação:
        = -> IGUAL;
        > -> MAIOR QUE;
        < -> MENOR QUE;
        >= -> MAIOR OU IGUAL A QUE;
        <= -> MENOR OU IGUAL A QUE;
        <> -> DIFERENTE;
        
    ##### Lógicos:
        AND -> Se uma proposição for falsa, o resultado também será falso;
        OR -> Se uma das proposições for verdadeira, o resultado também será verdadeiro;
        NOT -> Inverte o valor da proposição;
        BETWEEN -> Verifica dentro de um espaço delimitado pelo comando;
        IN -> Tudo que esteja "dentro" de algo. Funciona como múltiplos Or's;
        LIKE -> Compara textos;
        ILIKE -> Compara textos ignorando divergências entre maiúsculas e minúsculas;
        IS NULL -> Verifica se o campo é nulo;
    #### Funções agregadas:

    ##### **GROUP BY**
    Agrupa os registros semelhantes existentes em uma coluna;
        
        Select <coluna1>, <coluna2>, <coluna3>
        from <schema.tabela>
        group by <coluna1>
    ##### **HAVING**
    Filtra as linhas de seleção por uma coluna agrupada, podendo ser usado para filtrar resultados de função agregadas, algo que é inviável usando o WHERE;

    #### Join
    Combina as colunas de tabelas distintas.
    * Inner Join: Pega os dados que possuem semelhança em ambas tabelas;
    * Left Join: Seleciona tudo da tabela à esquerda e correlaciona os dados da tabela à direita que possuem semelhança;
    * Right Join: Seleciona tudo da tabela à direita e correlaciona os dados da tabela à esquerda que possuem semelhança;
    * Full Join: Seleciona todos os dados de ambas as colunas;

    #### Union
    "Cola" as colunas de uma mesma tabela, desde que elas possuam a mesma quantidade de colunas e com o mesmo tipo de dado inserido nelas;

    #### Subqueries
    É a posibilidade de consultarmos dados de outras consultas (como uma função);

    **Exemplos feitos no curso:**
    ##### WHERE:
        select *
        from sales.products
        where price = (select min(price) from sales.products)

        select min(price) from sales.products

    ##### WITH
        with alguma_tabela as (
            select
	            professional_status,
	            (current_date - birth_date)/365 as idade
            from sales.customers
        )
        select 
	        professional_status,
	        avg(idade) as idade_media
        from alguma_tabela
        group by professional_status
    
    ##### FROM
        select 
	        professional_status,
	        avg(idade) as idade_media
        from (
		        select
			        professional_status,
			        (current_date - birth_date)/365 as idade
		        from sales.customers
	        ) as alguma_tabela
        group by professional_status

    ##### SELECT
        select
	        fun.visit_id,
	        fun.visit_page_date,
	        sto.store_name,
	        (
		        select count(*)
		        from sales.funnel as fun2
		        where fun2.visit_page_date <= fun.visit_page_date
			        and fun2.store_id = fun.store_id
	        ) as visitas_acumuladas
        from sales.funnel as fun
        left join sales.stores as sto
	        on fun.store_id = sto.store_id
        order by sto.store_name, fun.visit_page_date

    >###### Acesse o [resumo completo](/Sprint_2/SQL_análise_de_dados/README.md) de SQL para mais informações.

- ### Big Data Fundamentos 3.0

    #### Acesse o certificado de Big Data clicando [aqui](/Sprint_2/Big_Data_Fundamentos_3.0/Certificado/Certificado%20de%20conclusão%20Big%20Data%20Fundamentos%203.0.jpg)

    >#### Importante: Para acessar o resumo completo [clique aqui!](/Sprint_2/Big_Data_Fundamentos_3.0/README.md)
    
    ### O que é Big Data?
    Grande conjunto de dados complexos que possuem: Volume(a quantidade de dados que é gerado diariamente), Variedade(formato dos dados), Velocidade(os dados são gerados com uma velocidade gigantesca) e Veracidade(a confiabilidade dos dados). Estes, inclusive, são os 4 V's que unidos compõem o Big Data.

    **IMPORTANTE:** O "V" de Volume é crítico no big data, visto que é um fator de grande consideração na hora de implementar o Big Data. Você é capaz de comportar tantos dados assim? Precisamos das ferramentas certas para desenvolver e integrar Big Data Analytics em nosso projeto.

    ### Big Data Vs Ciência de Dados
    Como vimos, Big data é um grande conjunto de dados. Porém, dele não se extrai informações valiosas e insights ao acaso.  
    Deste modo, a ciência de dados é o conjunto de métodos usados para extrair valor do Big Data.  

    Quando usamos ciência de dados para extrair valor do Big Data, temos o que é chamado de: **Big Data Analytics**

    ### Armazenando Dados:
    Quando os dados são estruturados usamos: Data WareHouse;  
    Quando os dados **não** são estruturados usamos: DataLake;

    Dependendo do cenário, podemos armazenar primeriamente os dados brutos num Datalake e depois estruturá-los em um Data WareHouse.

    ### SQL Vs NoSQL
    * Bancos de dados relacionais: São bancos de dados estruturados e com schema bem definido;

    * Bancos de dados não relacionais: São bancos de dados com dados não estruturados e sem necessidade de definir o schema previamente;

    ### Data WareHouse
    Sistema de armazenamento de dados que conecta e harmoniza diferentes fontes de dados.  
    Possui o schema bem definido previamente ao armazenamento dos dados.  
    
    #### Benefícios do DW
    * Melhor análise dos negócios;
    * Consultas mais rápidas;
    * melhoria da qualidade dos dados;
    * Visão histórica;

    ### DataLake
    Sistema de armazenamento usado para armazenar dados em seus formatos originais, brutos.  
    Não é necessário definir o schema antes de armazenar os dados.  

    É importante ficar atento quanto aos dados que são armazenados, pois se não forem minimamente tratados, o DataLake certamente se tornará numa bagunca; o chamado **Data Swamp**.

    #### Benefícios do DataLake
    * Armazenamento em formato bruto;
    * Importação de qualquer quantidade de dados em tempo real;
    * Repositório central para todos os dados da empresa;
    * Sem necessidade de movimentação dos dados;

    ### DataStores
    Repositório usado para armazenar coleções de dados com formatos variados.  
    Os dados já estão praticamente preparados para serem usados.

    #### Benefícios do DataStore
    * Armazenamento de variados tipos de dados;
    * Flexibilidade;
    * Suporte a dados semi-estruturados;
    * Custo total menor.

    ### Armazenamento e Processamento paralelos
    #### Cluster de computadores
    São um conjunto de servidores unidos para um mesmo fim;

    **Escalabilidade Horizontal:** Para aumentar a capacidade, instalam-se novas máquinas.  
    **Escalabilidade Vertical:** Para aumentar a capacidade, melhoram-se as máquinas já instaladas.

    #### Armazenamento Paralelo
    Distribuição dos dados armazenados em diversos servidores, aumentando assim a sua capacidade com hardware de baixo custo.

    Exemplo de Software usado: Apache Hadoop -> Nele, os arquivos são salvos em mais de um computador. Caso um falhe, os arquivos/dados não serão perdidos;

    #### Arquitetura de armazenamento e Processamento Paralelo
    - **MapReduce Layer:** Usado para processar dados em um ambiente distribuído;
    - **HDFS Layer:** Armazenamento dos dados dentro das máquinas do cluster;

    #### Soluções de arquitetura e processamento paralelo
    * Apache Hadoop;
    * CloudEra;
    * Azure;
    * DataBricks;

    ### Cloud Computing
    Devido ao grande volume de dados gerado diariamente, servidores locais não podem mais comportar individualmente. O desenvolvimento em nuvem entra para liberar e facilitar o Big Data Analytics.

    É uma ferramenta que oferece acesso a um servidor com ferramentas e recursos fornecidos por um provedor;  

    #### Principais provedores em nuvem
    * Amazon Web Services;
    * Microsoft Azure;
    * Google Cloud Plataform;
    * IBM Cloud;
    * Oracle Cloud.

    ### MLOPs e DataOPs
    **Machine Learning:** Usa algoritmos e dados para imitar o processo de aprendizagem humana em uma máquina; 

    **PipeLine de Dados:** É o fluxo da máquina, o processo desde o início até a máquina já aperfeiçoada;

    **DevOPs:** Abordagem para o desenvolvimento de software utilizando automação.

    #### MLOPs
    Unifica o desenvolvimento de sistemas para padronizar e agilizar entregas constantes com alta qualidade;

    #### DataOPs
    Linha de produção orientada a processos para o desenvolvimento de análises;

    ### Big Data Vs Small Data
    **Big Data**, como já citado anteriormente, refere-se a um grande conjunto de dados com velocidade, variedade, volume e veracidade.  
    Já **Small Data** refere-se a um conceito da quantidade unicamente necessária e mínima para desenvolver um problema.

    ### DaaS (Data as a Service)
    Alavanca os dados com um ativo de negócios para garantir maior agilidade na análise;

    #### Arquitetura DaaS
    * Simplifica o acesso aos dados;  
    * Oferece um fluxo de dados já tratados;  

    #### Principais benefícios das DaaS
    * Monetização dos dados;
    * Redução dos custos;
    * Caminho mais rápido para invovação;
    * Agilidade no processo de decisão baseado em dados;

    ### As Arquiteturas modernas de Big Data
    #### Data LakeHouse
    Possibilita o uso de BI e Machine Learning em todos os dados armazenados, combinando a flexibilidade dos datalakes com o gerenciamento de dados e transações ACID dos Data WareHouse.
    #### Data Mesh
    Arquitetura de plataforma que consegue abrangir todos os dados da empresa. Permite um design orientado ao domínio e ao autoatendimento.  
    *Obs:* Arquitetura completamente descentralizada;  

    Os datamesh's resolvem três problemas, são eles: falta de propriedade; falta de qualidade; escalonamento organizacional.

    Evita a duplicação de esforços por meio de um tratamento de dados como produto e sua infraestrutura como plataforma.

    ### ETL
    É o processo de extração e consecutiva limpeza dos dados para que os mesmos possam ser utilizados.

    #### ETL Vs ELT
    O ELT não faz esse processo de limpeza primordial para depois armazenar os dados. Nela, os dados são armazenados brutos em um DataLake e posteriormente, conforme a necessidade, pega-se os dados, promove-se a limpeza para depois utilizá-los. Nele também conseguimos:
    * Deixamos o DW pronto para o usuário;
    * Conseguimos armazenar todos os dados;

    #### Soluções ETL e ELT presentes no mercado:
    * Oracle Data Integrator;
    * Pentaho;
    * Apache Spark;
    * Apache nifi;
    * Azure Data Factory;

    ### Os quatro passos essenciais para iniciar um projeto Big Data
    #### Definição do Business Care
    * Definição dos objetivos a serem alcançados;
    * Delimitar os problemas a serem resolvidos;
    * Definir como será desenvolvido o projeto, do início ao fim;

    #### Planejamento do Projeto
    * Determinar e quantificar os requisitos necessários;
    * Identificar as questões comerciais e o resultado alvo esperado;
    * Definir como seria uma implementação de Big Data bem definida;
    * Definir uma linha de tempo;

    #### Definição dos requisitos técnicos
    * Definir quais são os atributos de banco de dados que serão usados;
    * Definir quais serão as fontes de dados usadas;
    * Definir quais serão as ferramentas de análise;;
    * Elencar quais serão as habilidades necessárias para trabalhar neste projeto: Capacitação de funcionários;
    * Definir qual será o tipo de arquitetura usada no projeto;
    * Definir as ferramentas que serão usadas para visualização de gráficos;

    #### Criação de um Total Business Value Assessment
    No TBVA, precisamos validar se o nosso esforço no projeto realmente trará valor. Nesse aspecto, alguns aspectos são levantados:
    * Time to business: Quanto tempo para que o projeto esteja pronto?
    * Escalabilidade: Precisamos ter cuidado para que a dimensão
    * Padrões técnicos: A empresa precisa criar seus próprios padrões técnicos;
    * Maturidade para dados: A empresa realmente tem a estrutura para armazenamtento dos dados?
    * Facilidade de uso: O quão fácil é a utilização do projeto para o cliente?


    >##### Acesse o [resumo completo](/Sprint_2/Big_Data_Fundamentos_3.0/README.md) para informações mais aprofundadas!

## Sprint #3
- ### Python
    >#### Acesse o Resumo completo de Python clicando [aqui](/Sprint_3/_Python_/README.md)
  
    >#### Acesse o Desafio Python AWS clicando [aqui](/Sprint_3/_Python_/Desafio%20AWS_python/)

    >#### Acesse as atividades AWS 3/10 clicando [aqui](/Sprint_3/_Python_/Exercícios_AWS_3-10/)

## Sprint #4
>### Acesse o Conteúdo completo dos cursos trabalhados [clicando aqui](/Sprint_4/README.md)

- ### Programação Funcional
    >#### Acesse o Certificado [clicando aqui](/Sprint_4/programacao_funcional/)

    >#### Acesse o Desafio [Python Funcional](/Sprint_4/Ex_python_AWS_4-10/) 

- ### Estatística Descritiva em Python
    >#### Acesse o certificado [clicando aqui](/Sprint_4/Estatística_python/Certificado/Certificado%20de%20conclusão%20Estatística%20com%20Python.jpg)

- ### Docker para Desenvolvedores
    >#### Acesse o certificado [clicando aqui](/Sprint_4/Docker/Certificado/Certificado%20de%20Conclusão%20Docker.jpg)

    >#### Acesse o Desafio [Docker](/Sprint_4/Docker/Desafio_AWS_4-10/)

## Certificados AWS
### Sprint #1
![image](Certificados%20AWS/Certificado%20AWS%201-10.jpg)
---------------
### Sprint #2
![image](Certificados%20AWS/Certificado%20AWS%202-10.jpg)
---------------
### Sprint #3
![image](/Certificados%20AWS/Certificado%20AWS%203-10.jpg)

### Sprint #4
![image](/Certificados%20AWS/Certificado%20AWS%204-10.jpg)


[Stack Overflow]: https://stackoverflow.com/users/22296808/lucas-dias-squinca
[Twitter]: https://twitter.com/lucas_squinca
[LinkedIn]:https://www.linkedin.com/in/lucas-squinca 
[Instagram]: https://www.instagram.com/lucassquinca/
[Portfólio]: https://nicitov.github.io