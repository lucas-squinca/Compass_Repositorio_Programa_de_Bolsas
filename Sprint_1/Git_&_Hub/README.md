Diretório Git & GitHub
======================
### Diretório dedicado a arquivos e conteúdos do curso de Git e GitHub do Hora de Codar - Sprint 1;

## Resumo
### Controle de Versão
É uma técnica usada para trabalhar no gerenciamento de código fonte de uma determinada aplicação, registrando todas as suas modificações de códigos e, deste modo, criando diferentes versões de projetos e softwares.  
Uma grande qualidade é a sua praticidade em alternar entre versões distintas do projeto e sua facilidade de trabalho conjunto, pois cada pessoa pode ter a sua própia versão em sua máquina;

Assim, existem algumas ferramentas que fornecem a capacidade de trabalhar o controle de versão. Dentre elas, temos o _**GIT**_.
### Git
#### O que é?
É o sistema de controle de versão mais utilizado no **Mundo**.  
Basea-se no controle por repositórios, os quais contém todas as versões disponíveis do código bem como cada cópia dos desenvolvedores envolvidos.  
Git é um projeto de código aberto, ou seja, é descentralizado e permite que qualquer pessoa possa compartilhar e modificar tecnologias. É **gratuito** e **acessível ao público!**
- ### Repositórios
  É o local onde o código é armazenado(pasta). Geralmente, os repositórios são ligados a servidores gerenciadores de repo's (repositórios), como o **GitHub**.  
  Dentro de um projeto hospedado, cada participante pode copiá-lo e fazer a sua própria versão, que fica armazenada em ua máquina.
  ### Criando REPO'S
  É por meio deste código que criamos os repositórios (um por projeto):

        git init

    Ao executá-lo, uma pasta oculta .git será criada no diretório escolhido. A partir deste momento, o git responderá aos demais comandos.
    
### GitHub
#### O que é?
É um serviço de gerenciamento de repositórios amplamente usado e gratuito.  
É por meio dele que conseguidos disponibilizar nossos projetos e permitir que outros desenvolvedores possam trabalhar nele ou criarem suas próprias versões pessoais, respeitando o tipo da _licença_ de cada projeto.
#### Criando repositórios
Podemos criar um repositório no site da GitHub para depois linká-lo à nossa máquina;  
Algumas informações necessárias para iniciar um projeto são: Nome do repositório, descrição, licença, etc;  
É uma interface mais interativa, com alguns cliques o seu repositório remoto está criado;

### Abas do GitHub
#### **Code**
Nela temos acesso a diversas informações, como o código fonte, os detalhes da licença agregada ao projeto, o arquivo README.md, etc;  
É nela também que criamos branches, adicionamos arquivos, e diversas outras coisas!

#### **Issue**
Por meio dela organiza-se tarefas a serem feitas ou bugs existentes para serem corrigidos. Geralmente é designado para alguém solucionar a issue;  
Nela podemos atualizar o estado de resolução do problema ou tarefa até que seja efetivamente concluída;

#### **Pull Request**
É onde os códigos são enviados, os quais passam por uma análise para identificação de issues e novas possíveis funcionalidades;  
Primeiramente o código passa pelo "pull request" para depois ser enviado para o repositório "main" do projeto;  

#### **Actions**
Aba para criação de automatizações de deploy com outros serviços, como "Continuous Integration" e "Continuous Development";  
Por meio do "Actions" podemos criar rotinas de atualização dos códigos automaticamente, por exemplo;

#### **Projects**
Muito semelhante a aplicações Web de organização de equipe, como: Trello e Monday.com;  
É um quadro de tarefas já inserido no próprio GitHub, cuja vantajem está atrelada a ter várias aplicações em um só lugar!  
Estrutura: BackLog | Retorno de Qualidade | Desenvolvimento | Teste | Finalizadas;  
Método ágil Kanban, onde se criam notas que podem virar pedidos de issues para organização do projeto;

#### **Wiki**
Aba feita para criar um ambiente para documentação mais extensa, como a própria [Wikipédia](https://pt.wikipedia.org/wiki/Wikipédia:Página_principal);  
Nela podemos descrever as funcionalidades do projeto;  

#### **Insights**
Aba de informações sobre o projeto, como: Todos os commits, os contribuidores do projeto, forks, dentre outras;  
Linha de desenvolvimento do projeto, do início ao fim;  

#### **Settings**
Aba de configurações, como o próprio nome já diz;  
Podemos modificar diversas partes do projeto: Nome, contribuidores, acesso, features, até mesmo remover o projeto do repositório remoto;

#### **Gist**
É uma funcionalidade do GitHub;  
Nele podemos adicionar pequenos blocos de código que podem ser hospedados do github;  
Podemos salvar uma solução que achamos interessante, ou também uma pequena funcionalidade importante que não queremos perder, por exemplo:  
```c
include <stdio.h>

int main(void)
{
    /* Lendo um vetor numérico de até 100 valores */

    int vet[100], tamanho, i;

    printf("Informe o tamanho do vetor");
    scanf("%d", &tamanho);

    printf("Informe a sequência de números");
    for(i = 0; i <= tamanho - 1; i = i + 1)
    {
        scanf("%d", &vet[i]);
    }
}
```

### Como enviar repositórios ao GitHub?
Ao iniciar-mos o nosso repositório, devemos relacioná-lo com o github por meio da seguinte sequência de códigos:

    echo "# <nome_repo_github>" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/<usuario_github>/<nome_repo_github>.git
    git push -u origin main
    
**Esta sequência só será feita uma vez por projeto.**

### Como verificar mudanças no projeto?
    git status
Um dos comandos mais simples e utilizados do git, onde são mapeados diversas alterações, como:
1. Arquivos modificados;
2. Arquivos adiconados;
3. Arquivos não monitorados;
   
### Como adicionar novos arquivos?
    git add <nome_arquivo>
Podemos também adicionar diversos arquivos novos de uma vez:

    git add .
Com este comando, os arquivos "untracked", ou seja, os arquivos não mapeados pelo git serão adicioados ao projeto.
### Como salvar alterações?
**Obs:** É comum enviar uma mensagem junto ao comando usando a flag "-m". O conteúdo da mensagem deve ser uma pequena frase especificando as alterações salvas;

    git commit <arquivo_novo> -m "mensagem"
Podemos salvar todas as alterações existentes usando a flag "-a":

    git commit -a -m "mensagem"

### Enviando para o GitHub
    git push 
Após o comando, o repositório do GitHub será atualizado com o conteúdo do repo que está nem nossa máquina;

### Recebendo alterações
    git pull
Inversamente ao "git push", usamos o código para receber alterações existentes no repo do GitHub;  
_Branches (abordado mais a frente) também são atualizadas com o comando "git pull";_

### Clonar repositórios
Quando começamos a trabalhar em um projeto já existente, devemos receber o código. Para isso, faz-se o uso do "git clone" para facilitar a cópia de códigos para diferentes máquinas;

    git clone <Url_repositório>
### Como remover arquivos do projeto?
    git rm <nome_arquivo>
Com este comando, removemos um arquivo da supervisão do git.

### Histórico (log)
Podemos usar o respectivo comando para ter acesso a um histórico com todos os commits dados no projeto.

    git log

### Renomear arquivos
    git mv
Comando usado para renomear e mover arquivos para outras pastas/diretórios;

### Desfazer alterações (arquivo)
    git checkout
Este comando retoma o estado original do arquivo modificado;

### Como ignorar arquivos no projeto?
Ao incluirmos um arquivo chamado ".gitignore" na raiz de nosso projeto, podemos "ignorar" arquivos, basta que adicionemos os nomes dos arquivos dentro do .gitignore;

### Desfazendo alterações (reset total)
    git reset
    git reset --hard (Forçar o reset)
**CUIDADO!** Com este comando, todas as alterações comitadas e pendentes serão excluídas

### Branches
Cada nova versão/feature reside em uma "branch", que é a maneira que o git separa diferentes versões do mesmo projeto;  
Cada branch diferente pode ser, por exemplo, pessoas que trabalham em um projeto, cada uma desempenhando uma função e efetuando uma determinada tarefa.  
Assim, cada pessoa primeiramente desenvolve sua parte em seu respectivo branch que pode ser visto no servidor da GitHub.

- ### Criando Branches
        git branch <nome_branch>
- ### Visualizando Branches
        git branch
- ### Deletando Branches
        git branch -d <nome_branch>
        git branch --delete <nome_branch>
- ### Como mudar de branch
        git checkout <nome_branch>
    
    Ainda podemos nos mover para um branch que ainda não existe! Ou seja, criar e se mover para o branch ao mesmo tempo:
        
        git checkout -b <nome_novo_branch>
- ### Unir Branches
        git merge <nome_branch>
    Assim, o branch atual e o branch selecionado serão unidos;

### Como usar o Stash
Podemos salvar as nossas modificações do projeto e seguir de um modo diferente de solução e mesmo assim não perder o antigo código salvo, por meio do Stash;
        
        git stash

Após a execução do comando, o branch será resetado de acordo com o seu repositório salvo;
- ### Recuperar e Visualizar Stashs
    Podemos visualizar stashs existentes com o seguinte comando:

        git stash list
    Além disso, podemos recuperar uma stash, ou seja, podemos continuar de onde paramos com os arquivos que estão salvos na stash:

        git stash <nome_stash>
- ### Remover Stashs
    Podemos tanto remover todas as stashs de uma vez:

        git stash clear
    Quanto remover uma Stash em específico:

        git stash drop <nome_stash>
### Tags
As tags são como "checkpoints" no nosso branch/projeto.  
É geralmente usada para demarcar estágios de desenvolvimento em nosso projeto.
#### Ex:
>"Calculadora.py" -> Finalizada
>> "v3.5"
>>> "v3.0"
>>>> "v2.1"
>>>>> "v1.0"
- ### Criando tags
        git tag -a <nome_tag> -m <mensagem>
- ### Verificando tags
        git show <nome>
- ### Alterando entre tags
        git checkout <nome_tag>
    Com esse comando, conseguimos avançar ou retroceder entre os checkpoints da branch;
- ### Enviando tags
    Ainda podemos enviar nossas tags para o repositório e assim compartilhá-lo com os nossos colegas desenvolvedores:

        git push origin <nome_tag>
    Podemos enviar todas as nossas tags de uma só vez:

        git push origin --tags

### Compartilhamento e Atualização
- ### Comando para "encontrar" branches
        git fetch
    Atualiza os branches e insere oq que não estavam sendo mapeados pelo seu Git;
#### **Obs: Comandos como "git push" e "git pull" também são usados em branches, podendo receber ou enviar alterações para o repositório remoto ou compartilhar códigos com outros participantes**

- ### Comando "remote"
        git remote
    Usado para trackear ou remover um repositório;

        git remote add origin <link>
    Comando usado quando criamos um repositório remoto, como no GitHub, e queremos adicioná-lo à nossa máquina;
### Submódulos
#### O que é?
É a maneira pela qual podemos ter mais de um projeto em somente um repositório.  
 "Linkamos" um projeto ao outro, mantendo suas estruturas separadas;
- ### Verificando submódulos
        git submodule
- ### Como adicionar submódulos?
        git submodule add <repositório>
- ### Atualizando submódulos
    Podemos atualizar um submódulo primeiramente commitando as mudanças e após isso executar o comando:
        
        git push --recurse-submodules=on-demand
    Deste modo, atualizamos somente o submódulo, não o projeto o qual está inserido;
### Análises e inspeção
- ### Como exibir informações?
        git show
    Este comando oferece uma gama de informações, como os commits de nosso branch atual, as modificações feitas nos arquivos entre cada commit feito, dentre outras;
        
        git show <tag_nome>
    Usado para exibir informações sobre uma tag em específico;
- ### Exibindo diferanças
        git diff
    Por meio deste comando, exibe-se as diferenças entre o branch atual e o remoto;

        git diff <arquivo1> <arquivo2>
    Podemos também exibir as diferenças entre diferentes arquivos;
- ### Log resumido
        git shortlog
    Nos dá informações resumidas, agrupando os commits por autores. Assim, podemos ver quais commits foram enviados ao projeto e por quem;  
    **Obs: Por meio disso, é visível a importância de enviar boas mensagens nos commits para mostrar aos outros participantes o que foi feito e enviado de maneira prática!**
- ### Describe
        git describe --tags
    Podemos verificar, por meio do comando, todas as tags existentes em nosso projeto;
### Administrando o repositório
- ### Limpando arquivos "Untracked"
        git clean
    Este comando possui por função limpar/excluir todos os arquivos que não foram adicionados ao repositório por meio do comando "git add ."
- ### Otimização de REPO's
        git gc
    O repositório é otimizado em questões de performance, pois o comando avalia e elimina os arquivos que julga não mais necessários;
- ### Checando integridade de arquivos
        git fsck
    **COMANDO DE ROTINA**  
    File System Check: checa a integralidade de arquivos bem como sua conectividade, procurando por corrupção nos mesmos.
- ### Reflog
        git reflog
    Este comando exibe todos os seus passos dentro do projeto, desde um novo commit até uma mudança entre branches.  
    **Atenção:** Reflogs ficam salvos até expirarem (cerca de 30 dias);
    ### Recuperando arquivos com reflog
        git reset --hard <hash>
    Podemos tanto avançar quando retroceder entre as hashs de um reflog. Porém, é importante lembrar de que reflogs expiram;
- ### Como transformar repo em arquivo
        git archive --format zip --output main_files.zip main
    Compactamos um repositório em arquivo .zip, por exemplo;

### Markdown
É uma forma de estilização de textos para a Web, possuindo diversas funcionalidades, como:
1. Exibir trechos de código estilizados;
2. Inserir links;
3. Inserir imagens;
4. Atrelar links a imagens;

Suas funcionalidades permitem uma melhor experiência do cliente nas documentações;

- ### Cabeçalhos
    Usados com o símbolo "#";  
    Semelhantes ao sistema de cabeçalhos do html, que vão por ordem hierárquica (h1 até h6);  
    #### Ex:

    ```html
    <h1>Título Principal</h1>
    <p>Assunto do título sendo abordado e detalhado</p>
    <h2>Outro título, menor</h2>
    ...
    ```
    Quanto maior a prioridade (h1), menos hashtags são usadas, ou seja, para usarmos o "h1" em markdown, usamos o "#" uma vez;  
    #### Ex:

    ```
    # Título Principal
    Assunto do título sendo abordado e detalhado
    ## Outro título, menor
    ...
    ```
- ### Ênfase
    Usamos símbolos para dar ênfase nos nossos textos, são eles "**" ou "__" para **negrito** (abrindo e fechando) e "*" ou "_" para _itálico_;
    #### Ex:
        **Este texto estará em negrito em um arquivo Markdown** | __Este texto também__
    ```
        *Este texto estará em itálico em um arquivo Markdown* | _Este texto também_
    ```
        _**Este texto estará em negrito e em itálico em um arquivo Markdown**_

- ### Listas
    Temos listas ordenadas e não ordenadas em arquivos .md, assim como n html;  
    Listas ordenadas iniciam com: "número".(Item);  
    Listas não ordenadas iniciam com: *Item;
    #### Ex de não ordenada:
    * Primeiro ponto;
    * Segundo ponto;
    * Terceiro ponto;  

    #### No código markdown:
        * Primeiro ponto;
        * Segundo ponto;
        * Terceiro ponto;

    #### Ex de ordenada:
    1. Primeiro item;
    2. Segundo item;
    3. Terceiro item;

    #### No código markdown:
        1. Primeiro item;
        2. Segundo item;
        3. Terceiro item;

    Note que, tanto na exibição quanto no código, as listas ordenadas são apresentadas da mesma maneira;

- ### Imagens
    O Markdown permite que inserimos imagens no nosso documento, por meio do código:

        ![Texto_imagem](link_imagem)
    
    #### Ex:
    **No código:**

        ![logo markdown](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)
    
    **No documento:**  
    ![logo markdown](https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg)

    **Obs: A imagem pode se encontrar dentro do repositório ou ter sua url externa, funciona dos dois modos.**

- ### Links
    Podemos também inserir links facilmente em nosso documento por meio do código:

        [Texto_link](Url_link)

    #### Ex:
    **No código:**
        
        [Youtube](https://www.youtube.com/watch?v=GHMXAvTSRAY)
    
    **No documento:**

    [Youtube](https://www.youtube.com/watch?v=GHMXAvTSRAY)

- ### Códigos no GitHub
    Para inserir códigos no arquivo markdown usamos abre e fecha de acentos graves:

        ```
        Seu código aqui
        ```
    Ainda podemos deixar o nosso código estilizado, informando em qual linguagem estamos escrevendo após os primeiros três primeiros acentos:

        ```python
        Seu código aqui
        ```
    Deste modo, nosso código fica estilizado, colorido para as funções que são reconhecidas pelo documento.
    #### Ex:
    **No código:**
    ```
        ```python
        num = int(input('Informe um número inteiro'))
        num2 = int(input('Informe outro número'))
        soma = num + num2
        print(f'A soma dos dois números é {soma})
        ```
    ```
    **No documento:**
    ```python
        num = int(input('Informe um número inteiro'))
        num2 = int(input('Informe outro número'))
        soma = num + num2
        print(f'A soma dos dois números é {soma})
        ```
- ### TaskList
    Ainda podemos adicionar uma lista de tarefas no Markdown, tanto concluídas quanto não concluídas.  
    **Obs:** Essa sintaxe do markdown é especial e exclusiva do GitHub;

    #### Ex:
    **No código:**
    
        [x] Estudar GitHub
        [ ] Estudar SQL
    **No documento:**
        [x] Estudar GitHub
        [ ] Estudar SQL

### Escrevendo Commits corretamente
Commits mal escritos atrapalham o entendimento e continuação do projeto.  
A padronização das mensagens dos commits são de extrema importância para o versionamento do projeto, assim como para o bom entendimento durante seu desenvolvimento;

Escrever bons commits ajuda em:
1. Reviews de Pull Request;
2. Melhoria dos Logs (git log), bem como de suas variantes, como "shortlog" e "relog";
3. Entender em que ponto o projeto se encontra por meio dos commits;
4. Manutenção do projeto;

#### Possíveis soluções para commits:
- #### Private Branches
    Consiste na criação de branches que não serão compartilhados com o repositório. Deste modo, podemos escrever qualquer tipo de commit;  
    Ao solucionarmos o problema ou projeto, podemos dar um "rebase" com o comando:
     
        git rebase <atual> <funcionalidade> -i
    Com esse comando, podemos editar ou até mesmo excluir commits dados. Assim, commits também podem ser reutilizados, apenas trocamos o que está escrito;  
    Excluímos com "squash" e renomeamos com "reword".
- #### Boas Práticas de commits
    Podemos:
    1. Separar o assunto do corpo da mensagem (como se fosse um "título", assunto principal);
    2. Máximo de 50 caracteres para o assunto;
    3. Máximo de 72 caracteres para o corpo;
    4. Explicar o "porque" e o "como" do commit, não o código escrito em si;

## **Certificado**
<img src="Certificado/certificado de conclusão Git e GitHub - foto.jpg" width="600px"/>