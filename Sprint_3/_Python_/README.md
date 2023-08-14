Diretório Python
================
### Diretório dedicado ao conteúdo do curso "Python 3 - Curso completo do básico ao avançado" da Cod3r - Sprint 3;

>#### Acesse a Apostila Python clicando [aqui](/Sprint_3/Apostila_python.pdf)

## Resumo
#### Algoritmos
Conjunto de passos que podem ser resolvidos sequencialmente ou com repetição para a resolução de um problema ou alcançar um objetivo primário;

#### Estrutura de Dados
É algo que traz regras e ordem de como os dados são organizados;  
Existe uma sequência de regras que tornam um dado do tipo **INT**...

A *estrutura* da ordem para os *dados* os quais compõem um *algoritmo*
### O que é Python?
Python é uma linguaguem de programação de alto nível e de tipagem dinâmica e forte. De fácil aprendizado e sintaxe simples, é muito utilizada em escolas estadunidenses para introduzir a lógica de programação aos seus alunos.  

Python é muito utilizado para:
* Desenvolvimento Web;
* Programação com I.A;
* Big Data;
* Data Science;

### Filosofia do Python: Zen of Python
A linguagem python possui uma filosofia com algumas frases que trazem conceitos de como é e como deve ser a linguagem, a escrita e os códigos desenvolvidos nesta linguagem, são eles:
* Bonito é melhor que feio;
* Explícito é melhor que implícito;
* Simples é melhor que complexo;
* Complexo é melhor que complicado;
* Linear é melhor que aninhado;
* Esparso é melhor que denso;
* Legibilidade conta;
* Casos especiais não são especiais o bastante para quebrar as regras;
* Ainda que praticidade vença a pureza;
* Erros nunca podem passar silenciosamente -> a menos que sejam explicitamente silenciados;
* Diante da ambiguidade, recuse a tentação de adivinhar;
* Deveria haver um - **e preferencialmente só um** - modo de fazer algo -> Embora esse modo pode não ser óbvio a princípio, a menos que você seja holandês;
* **Agora** é melhor do que **nunca**, embora **nunca** frequentemente seja melhor que **imediatamente**;
* Se a implementação é Difícel de explicar, é uma má idéia. Se for fácil de explicar, é uma boa idéia;

### PEP 8
É o guia de estilo de código oficial do python: Como deve ser um determinado espaçamento? Eu preciso colocar ponto e vírgula ao final? etc.. etc.. etc...

> Clique [aqui](https://peps.python.org/pep-0008/) para acessar a PEP 8 oficial em inglês;

> Ou ainda clique [aqui](https://www.alura.com.br/conteudo/pep8-linters-python) para uma introdução ao PEP 8 feita pela Alura;

### Fundamentos Python
**Importante:** Linguagem python se preocupa muito com a identação do programa, tome cuidado!!!

#### Tipos básicos
* Valores lógicos(boolean): **True** and **False**
* Valores inteiros(int): {1, 2, 3, 4, 5, 6, 7, ...}
* Valores reais(float): {1.2 , 3.4, 2.0, 2.00, ...}
* Valores cadeia(string) - Sempre irão aparecer com aspas simples ou duplas: 'hello word', "hoje o dia está nublado", '256', ...   
Podemos concatenar números com strings caso não haja ambiguidade, como em:
    
    print('Você é ' + 3 * 'muito ' + 'legal!')

Neste caso, o número três "multiplicando" a palavra "muito" irá repetí-la três vezes.

#### Variáveis
Quando criamos uma variável, estamos gerando um espaço de memória que é nomeado para que possamos trabalhar com ela.

    a = 10

Criamos uma variável que possui o valor inteiro 10;

**Obs:** Por ser uma linguagem dinâmica, uma mesma variável pode mudar os tipos de dados de seu conteúdo (ao contrário de, por exemplo, linguagem C, na qual devemos declarar o tipo de nossa variável antes de usá-la, não podendo ser mudada posteriormente).

#### Comentários de código
Podemos "comentar" partes de nosso código quando queremos que esta definida região seja ignorada quando dermos "run" no código. Com ele, podemos criar anotações e comentários sobre o que o nosso código faz nas prórpias linhas de comando.

Comentando apenas uma linha, usamos o "#"

    # Esta linha está comentada

Também podemos comentar diversas linhas adicionando o "#" no início de cada uma

    # Esta linha está comentada
    # Esta também
    # print('Essa aqui também')

Podemos ainda realmente comentar diversas linhas abrindo e fechando aspas duplas ou simples

    """
    Todas estas linhas
    estarão comentadas
    em seu código
    !!
    """

**Obs:** Use comentários com calmaria e pensando realmente se o comentário é necessário para o seu código.
#### Operadores aritmédicos

    - -> Subtração;
    + -> Soma;
    * - > Multiplicação;
    / - > Divisão;
    // -> Divisão com resultado em número inteiro;
    ** -> Potência;
    % -> Módulo: Devolve o resto da divisão;

#### Operadores relacionais
Cuja resposta sempre será um valor bool (**True** or **False**)

    > -> Maior;
    < -> Menor;
    >= -> Maior ou igual;
    <= -> Menor ou igual;
    != -> Diferente de;
    == -> Igual a;
    
## Certificado