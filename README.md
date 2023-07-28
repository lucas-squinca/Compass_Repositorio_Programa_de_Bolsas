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
**✨Animes Preferidos:** [Black Clover | Ousama Ranking | Spy X Family];    
**🛠️Experiências:** [None];  
**📁Portfólio:** [[nicitov.github.io]][Portfólio];
## Redes Sociais
[![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white)][Stack Overflow]
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)][Instagram]
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)][LinkedIn]
[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white)][Twitter]

## Aprendendo...
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

## Segurança em aplicações Web

## Métodos ágeis de A a Z

## Sprint #1
- ### *Git & GitHub*
    >### Este resumo tem como objetivo exemplificar o uso de Git e GitHub bem como os comandos mais usados. Para entrar em mais detalhes, acesse o *[arquivo completo](/Sprint_1/Git_&_Hub/README.md)*
- ### *Linux*
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


[Stack Overflow]: https://stackoverflow.com/users/22296808/lucas-dias-squinca
[Twitter]: https://twitter.com/lucas_squinca
[LinkedIn]:https://www.linkedin.com/in/lucas-squinca 
[Instagram]: https://www.instagram.com/lucassquinca/
[Portfólio]: https://nicitov.github.io