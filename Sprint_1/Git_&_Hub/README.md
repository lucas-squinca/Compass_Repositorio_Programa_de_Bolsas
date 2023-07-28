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

### Clonar repositórios
Quando começamos a trabalhar em um projeto já existente, devemos receber o código. Para isso, faz-se o uso do "git clone" para facilitar a cópia de códigos para diferentes máquinas;

    git clone
### Como remover arquivos do projeto?
    git rm <nome_arquivo>
Com este comando, removemos um arquivo da supervisão do git.

## ```EM CONSTRUÇÃO...```

## **Certificado**
<img src="Certificado/certificado de conclusão Git e GitHub - foto.jpg" width="600px"/>