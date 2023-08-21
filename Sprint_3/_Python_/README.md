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

#### Operadores de atribuição

    = -> Atribuição simples;
    += -> Soma a variável com ela mesma mais outro valor;
    -= -> A variável recebe ela mesma menos um outro valor;
    *= -> A variável recebe ela mesma multiplicada por outro valor;
    /= -> Atribuição da variável por ela mesma dividida por outro valor;
    %= -> Módulo da variável por outro valor;
    **= -> Exponenciação da variável por outro valor;
    //= -> Divisão da vairável por outro valor;

Todas as atribuições citadas servem como uma facilidade, um outro método de escrever atribuições de uma forma resumida:

    a+=5 -> a = a + 5;
    a-=3 -> a = a - 3;

#### Operadores lógicos
- #### **And**
Operador de devolve **True** ou **False**;  
Se qualquer uma das relações que envolvem o operador for falsa, o resultado obrigatóriamente deverá ser falso;

    True and False

Neste caso, o resultado será **False**, pois uma das relações não é verdadeira;

- #### **Or**
Operador que devolve **True** ou **False**;  
Se qualquer uma das relações for verdadeira, o resultado também terá valor verdadeiro/True;  

    True and False

Neste caso o resultado terá valor **True**, pois uma das relações é verdadeira;

- #### **XOR**
Conseguimos o "ou exclusivo" somente com o uso do operador **!=**. Neste caso, deverá ser obrigatoriamente ou um ou outro.  
Em assim sendo, o resultado de "True != True" também será falso, pois é necessário que ele sejam diferentes;

- #### **Not**
Com esse operador, invertemos o valor de uma variável;

    not True 

O valor resultante neste caso será **False**

    not not False

Utilizando o not duas vezes ou quantas vezes forem possíveis, podemos continuar invertendo o valor. Neste caso, como foram usados duas vezes, o valor retorna a ser **False**.

**Cuidado** com os operadores byte a byte **&**, **|** e **^**, elas não são usadas como and, or ou xor e possuem preferências diferentes, tome muito cuidado!!!

**Obs:** Não existe a possibilidade de fazer atribuição e incremento da forma:

    a++
    ++a
    a--
    --a

Igual a outras linguagens, podemos somente fazer com os operadores de atribuição.

#### Operadores Ternários

    esta_chovendo = True
    'Hoje estou com as roupas' + ('secas.', 'molhadas.')[esta_chovendo]

Caso o valor da variável seja verdadeiro, será exibido o pedaço de string mais próximo dos colchetes (molhadas), caso contrário, será exibido a string que está mais afastada dos colchetes (secas).  

Outro modo de escrever:

    esta_chovendo = True
    'Hoje estou com as roupas' + ('molhadas.' if esta_chovendo else 'secas.')

#### Operadores (membro e identidade)
- #### Membro
        lista = [1, 2, 3, 4]
        1° -> 1 in lista
        2° -> 2 not in lista

    No primeiro caso o valor será verdadeiro, pois o valor '1' está na lista.  
    No segundo caso o valor será falso, pois o valor '2' está sim dentro da lista.

- #### Identidade
    
        x = 1
        y = 2
        z = y
        1° -> y is z
        2° -> x is not z
    
    Em ambos os casos teremos condições verdadeiras, pois a variável 'y' possui o mesmo valor da vairável 'z' e a variável 'x' **não** possui o mesmo valor da variável 'z'.

#### BuiltIns
Representa o escopo global do python, todas as coisas que são codadas são "armazenadas" no builtIns. Quando criamos uma nova variável, ela será armazenada no builtIns.  
Além disso, existem muitas funções que já usamos diariamente que são naturais do builtIns, como **help()**, **type()**, **print()**, etc...

As funcionalidades que usamos normalmente nos códigos e não foi necessário trazê-las, estão totalmente no builtIns.

#### Conversão de Tipos

    a = 2
    b = '3'
    print(a + b)

Neste exemplo, sabemos que o valor de 'a' é um inteiro, enquanto o valor de 'b' é uma string. Logo, sabemos que a soma das duas variáveis resultará em um erro.  
Nesse sentido, podemos mudar as tipos de uma variável forçando ela por meio de uma "função", colocando-a dentro de parênteses e passando o valor que desejamos que a mesma se torne.

    a = 2
    b = '3'
    print(a + int(b))

O valor **str** da variável 'b' se torna inteiro e a soma pode ser efetuada.

#### Coerção automática
O python automaticamente identifica o tipo do valor de um resultado.  
* Inteiro / inteiro ou inteiro // inteiro pode gerar um resultado inteiro ou real, dependendo da situação;
* Inteiro / real ou inteiro // real sempre dará resultado real (float).

#### Aprofundando tipos numéricos
- #### Int e Float
    
        <var>.is_integer()

    Função usada para verificar se um valor e/ou variável é do tipo inteiro.

        abs(<num>)
    
    Mostra o número absoluto.

- #### Strings

        nome = 'Pedro'
    
    Podemos acessar as letras da string individualmente, como em um vetor, com índice iniciando no 0;

        nome = 'Pedro'
        nome[0]
    
    Neste caso, o algoritmo retornará a letra 'P'.  
    A string é imutável, não conseguimos atribuir nada dentro de uma string que já possui um conteúdo nos espaços.

    Não conseguimos usar as aspas simples normalmente caso já estivermos a usando para delimitar a string. Podemos usar \' dentro da string para usar as aspas simples ou ainda usar as aspas duplas para dimencionalizar as strings e as aspas simples dentro da string.

        'marca d\'água'
        "marca d'água"

    Podemos ainda ter textos com múltiplas linhas dentro de uma variável usando três aspas duplas como delimitação:

        text = """ Texto com
                múltiplas linhas
                123456
                ABCDEFG """

    Temos a possibilidade de acessar as partes individuais da string também com números negativos, iniciando do '-1' a partir do último caractere:

        nome = 'Pedro'
        nome[4] => 'o'
        nome[-1] => 'o'

    Com strings, podemos delimitar um range até onde queremos pegar o que ela contém, seja do início até uma parte específica ou de uma parte até o fim:

        nome = 'Eduardo'
        nome[:3] => "Edu" -> O último caractere não é contado nesta situação, já que nome[3] corresponde ao 'a'.
        nome[3:] => "eardo" -> Já quando pegamos de uma parte em específico até o fim, contamos o nome[3].
        nome[2:4] => "ua" -> Delimitamos o início e o fim a serem mostrados.
    
    Existem outras delimitações que podemos fazer, veja o exemplo:

        sequencia = '1234567890'
        sequencia[::2] => '13579'
    
    Delimitamos que seriam pegos os números espaçados de dois em dois começando do início. Ou seja, seleciona-se o 1, pula o 2, seleciona-se o 3, pula-se o 4, e assim por diante...

    Com essas informações, podems inverter uma string facilmente em python:

        sequencia = '123456'
        sequencia[::-1] => '654321'

    Caso quisermos mudar todas as letras de uma string para maiúsculas ou minúsculas, devemos usar **.upper()** ou **.lower()** na string.

        frase = 'Olá Mundo'
        frase = frase.lower() -> A frase agora possui todos os seus dígitos como letras minúsculas;

        frase = frase.upper() -> A frase agora possui todos os seus dígitos como letras maiúsculas;

- #### Listas
    Listas são demilitadospor colchetes [];  
    Podemos livremente trabalhar com valores de tipos diferentes dentro de uma lista, seja **int**, **float**, **str**, etc...  
    Porém, não é aconselhável trabalhar com listas heterogêneas;

        lista = []

    Adicionamos valores à nossa lista por meio do **.append**

        lista.append(1)
        lista.append(2)
    
    Nossa lista agora é:

        lista => [1, 2]
    
    Usamos o comando lend() para ver quantos dados temos em nossa lista, como um "count()" de Sql:

        lend(lista) => 2

    Removemos um elemento da lista por meio do **.remove**

        lista.remove(2)
    
    A lista se torna:

        lista => [1]
    
    Podemos inverter os elementos de uma lista por meio do **.reverse**

        nova_lista = [1, 2, 3, 'Ana', 'Letícia']
        nova_lista.reverse => ['Letícia', 'Ana', 3, 2, 1]

    **Obs:** A lista é uma estrutura indexada (possui índice iniciando do 0).

    Conseguimos ainda identificar ual é a posição de um elemento dentro da lista com o comando **.index**

        nova_lista.index('Ana') => 1

    **Obs:** Assim como em uma string, podemos pegar intervalos da nossa lista.

        nova_lista[2:4:1] => [3, 2]

- #### Tuplas
    Diferentemente das listas, as tuplas são imútáveis. Ou seja, não podem ser modificadas;  
    Criamos uma tupla a partir dos parênteses;

        tupla = ()

    Precisamos tomar muito cuidado já que também usamos parênteses para outras funcionalidades.

        tupla = ('um') -> será considerado uma string;
        tupla = ('um',) -> será considerada uma tuple;

- #### Dicionários
    Onde trabalhamos com diversos dados, como se fosse um registro;  
    Usamos as chaves para criar um dicionário;

        pessoa = {'nome': 'Paulo', 'idade': 18, 'cursos': ['inglês', 'português']}

    Outras funcionalidades:

        pessoa.keys() -> Exibe todas as chaves do dicionário;
        pessoa.values() -> Exibe os valores existentes no dicionário;
        pessoa.itens -> Mostra cada item existente, as chaves com os seus respectivos valores;
        pessoa.pop('chave') -> Retorna o valor da chave e o retira do dicionário;
        pessoa.update({'ex_chave': valor, 'outra_chave': 'ex_string'}) -> Atualiza o dicionário com novas chaves e/ou valores para chaves existentes;
        pessoa.clear() -> limpa o dicionário;

    Podemos adicionar outros valores em alguma chave de nosso dicionário:

        pessoa['cursos'].append('python')

- #### Conjuntos
    Diferentemente dos dicionários, não são indexados, não possuem ordenação automática e não aceitam informações iguais/duplicadas;  
    O criamos a partir de chaves.

        a = {1, 2, 3}

    Existem algumas operações que podemos fazer com os conjuntos, iguais aos que aprendemos na escola:

        .union -> Une dois conjuntos em um novo;
        .interssection -> Cria um novo conjunto com os valores que existem em ambos os conjuntos;

    Podemos ainda verificar se um conjunto é subconjunto de outro por meio desta relação:

        conjunto_1 <= conjunto_2
        conjunto_1 >= conjunto_2

    Assim verificamos se o conjunto_2 é subconjunto do conjunto_1

    Com o sinal de subtração, verificamos os valores diferentes entre dois conjuntos:

        {1, 2, 3} - {2}

    Nessa situação, a saída será {1, 3}

    Podemos também atribuir os valores diferente em um conjunto com o operador de atribuição **-=**

        conjunto_1 -= {1}

#### Interpolação
1º Versão (mais antiga):

    nome, idade = 'Ana', 13
    print('Nome: %s Idade: %d' % (nome, idade))

2º Versão (.format):

    print('Nome: {0} Idade: {1}' .format(nome, idade))

3º Versão (f'') - **A MELHOR**:

    print(f'Nome: {nome} Idade: {idade}')

### Estruturas de Controle
#### If, Elif e Else
Estrutura condicional. Nela usamos uma certa condição, caso a mesma seja verdadeira, o bloco de comandos que estão dentro do comando **If** será executado.  
Se também usamos um **Elif**, caso a condição do If seja falsa, passamos para a verificação se a condição do elif é verdadeira. Em caso afirmativo, o bloco de comandos inserido no Elif é executado.  
Agora, se nenhuma condição for verdadeira, podemos inserir um **else**, que abrange todas as situações em que as condições tanto do if quanto do elif são falsas.

> [Exemplo if/elif/else](/Sprint_3/_Python_/Códigos_curso/Estrutura%20de%20dados/ex_if.py)

#### While
É uma estrutura de repetição feita para rodar uma certa parte de código até que a condição inserida no mesmo se torne verdadeira;  
Geralmente usado quando vamos fazer números indeterminados de repetições, até que uma certa condição seja verdadeira;

> [Exemplo While](/Sprint_3/_Python_/Códigos_curso/Estrutura%20de%20dados/while_1.py)

#### For
É um laço de repetição usado quando já sabemos quantas vezes iremos fazer aquela determinada repetição;
> [Exemplo de 'For'](/Sprint_3/_Python_/Códigos_curso/Estrutura%20de%20dados/for_1.py)
#### Break and Continue
São ferramentas geralmente usadas com estruturas de repetição (laços);  
* Continue:  
Quando estruturamos um laço e uma condição em um if e, dentro do if, o **continue** para toda informação verdadeira que entra no if, o código simplismente continuará rodando, seguindo em frente.  
O continue, mesmo dentro de uma estrutura condicional, está mais relacionado com o laço no qual está inserido;

* Break:  
Ao estruturarmos um laço com uma condição dentro do mesmo e, dentro do if, utilizamos um **break**, toda e qualquer afirmação falsa irá passar pelo if e o laço continuará rodando. Quando uma condição verdadeira for passada na estrutura condicional, o break é acionado e ele sai do **laço** imediatamente

> [Exemplo break e continue](/Sprint_3/_Python_/Códigos_curso/Estrutura%20de%20dados/break_continue.py)

#### Switch/Case
Estrutura de múltiplas escolhas, onde caso uma seja verdadeira, será executado o código e passará para a próxima estrutura após o switch.  
Você escolhe uma variável (switch) e determina casos para ela, se um caso for atendido, o código dentro do case será executado.  
Nele ainda temos o default, onde caso nenhuma condição dos cases forem atendidas, será executado o código da estrutura 'default'.

**Na linguagem python, NÃO TEMOS essa estrutura, mas podemos simulá-la com funções e dicionários**

> [Exemplo simulação Switch/Case](/Sprint_3/_Python_/Códigos_curso/Estrutura%20de%20dados/switch_1.py)

**ATUALIZAÇÃO**: A partir da versão 3.10, o python implementou uma estrutura switch, o match/case;  
Extremamente parecido com o switch/case de outras linguagens de programação;  

```python
match valor:
    case <padrao_1>:
        <codigo_caso_padrao_1>
	case <padrao_2>:
        <codigo_caso_padrao_2>
	case <padrao_3>:
        <codigo_caso_padrao_3>
    case _:
        <codigo_caso_nenhum_padrao_definido>
```

### Manipulação de arquivos

### Comprehension
É uma forma de criar listas mias consisas, a partir de somente uma linha (somente em python);  
Python é uma linguagem de altíssimo nível, logo ele permite essas funcionalidades que facilitam a nossa vida;  

Como fazer uma list comprehension?

    <variável> = [ <espressão> for item in <list> if <condicional>]

Ex: Lista com o dobro dos valores de 1 a 10
```python
dobros = [i * 2 for i in range(1, 11)]
print(dobros)
```
Caso não quiséssemos utilizar o list comprehension, poderíamos dar a mesma saída usando uma lista normal e uma sequência de ações:
```python
dobros = []
for i in range(1, 11):
    dobros.append(i * 2)
print(dobros)
```
> Outro exemplo de comprehension [aqui](/Sprint_3/_Python_/Códigos_curso/list_comprehension/comprehension_2.py)

#### Generator
Semelhante ao list comprehension, mas gera os dados e os envia sob demanda, ocupando **MUITO** menos espaço na memória;

    <var> = ( <expressão> for <list> if <condicional>)

Ex:
```python
generator = (i ** 2 for i in range(11) if i % 2 == 0)
print(next(generator)) # Saída 0
print(next(generator)) # Saída 4
print(next(generator)) # Saída 16
print(next(generator)) # Saída 36
print(next(generator)) # Saída 64
print(next(generator)) # Saída 100
```

- #### Generator com FOR
Facilitador para acessar-mos os dados, sem necessidade de tantos print's com next(*variável*);
```python
generator = (i ** 2 for i in range(10) if i % 2 == 0)

for numero in generator:
    print(numero)
```

- #### Dict comprehension
Criação fácil de dicionários com a ajuda do comprehension;

```python
dicionario = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

# Mostrando como tabuada:
for numero, dobro in dicionario.items():
    print(f'{numero} x 2 = {dobro}')
```

### Funções
#### Parâmetros
* Posicional: Serão passados os parâmetros para uma função como argumento de acordo com a posição relativa que foram colocadas
    ```
    função: def função(p1, p2, p3)
    main: função(2, 4, 7)
    ```
* Nomeado: Nele, nomeados quais são os parâmetros que irão receber um determinado argumento
    ```
    função: def função(p1, p2, p3)
    main: função(p2 = 4, p3 = 7, p1 = 2)
    ```

Alguns modelos de parâmetros
```
*<args> -> irá gerar uma tupla;
**<kwargs> -> irá gerar um dicionário
```

### Pacotes
Projetos em python muitas vezes podem não serem feitos apenas em um arquivo/programa;  
Para isso, é necessário a utilização de pacotes, com diferentes arquivos que unificam um mesmo programa;  
Dentro de uma pasta adicionamos o arquivo: '__init__.py' para mostrar que a pasta é um programa;  
Podemos importar um código em outro arquivo fora da pasta onde o __init__.py;  
A partir de um módulo, podemos importar as funcionalidades de outros módulos ou pacotes;

Ao chamarmos módulos, não podemos ter na conciência que eles irão rodar em um outro pacote apenas por chamá-los, precisamos declará-los diretamente:
```python
# Errado
from pacote1 import modulo2

# Correto
from pacote1 import modulo2
modulo2.main() # Declaração direta.
```
- #### Modulos com os mesmos nomes
Em casos de nomes iguais de módulos em pacotes diferentes precisamos apelidar um deles para que não exista nenhum erro!!
```python
# Adicione um apelido a um deles com "as"
from pacote1 import modulo1
from pacote2 import modulo1 as mod1
```
- #### Importação direta de funções
Veja a diferença entre chamadas diretas e indeiretas de funções:
```python
# Direta:
from pacote1.modulo1 import soma
from pacote2.modulo1 import sub

# Indireta
from pacote1 import modulo1
from pacote2 import modulo1
```
Nesse caso, ao chamarmos a nossa função **'soma'** no pacote, não precisaremos chamar junto a seu módulo:
```python
# Direta
print('Soma', soma(3, 2))

# Indireta
print('Soma', modulo1.soma(3, 2))
```

- #### Pacote como façade
Façade, exemplificando, é como uma fachada para o seu programa que mostra suas principais funcionalidades, "os produtos mais importantes", o "pãozinho francês".  
Expor um conjunto de funcionalidades do seu sistema de forma simples;  
Nesse sentido, podemos criar um pacote que expõe funcionalidades de outros pacotes de maneira simples;  
```python
# Importação de funcionalidades no pacote de fachada e implementação no __all__ do arquivo __init__.py:
from pacote1.modulo1 import soma
from pacote2.modulo1 import sub

__all__ = ['soma', 'sub']

# Pacote de fechada agora pode efetuar somente um import com todas as funções desejadas:
from calc import soma, sub

print('Soma', soma(3, 2))
print('Subtração', sub(3, 2))
```

### Programação Orientada a Objetos
É o paradigma que organização de idéias para transformar cenários/problemas do mundo real para dentro de um código de programação;  

Em paradigmas focados em procedimentos, a função é o agente principal e o dado é apenas uma informação a ser usada pela função:
```python
len(lista)
```

Já no contexto orientado a objetos, o dado se torna o principal, e as funções são métodos e comportamentos pertencentes a esse dado:
```python
lista.len()
```

O objeto é algo central dentro do paradigma voltado a objetos, composto por outras partes:
* Atributos: os dados;
* Comportamentos: as funções (métodos);

Agora os objetos são donos de seus comportamentos e não são apenas informações passadas por parâmetros para funções específicas;
#### Classe Vs Objeto
Classe funciona como o molde, enquanto o objeto seriam as instâncias criadas através desse molde;  
Conseguimos criar **n** instâncias a partir de um único molde;  
Quando criamos uma classe com seus devidos comportamentos e a partir dela criamos objetos, os mesmos terão espaços de memória correspondentes aos comportamentos da classe;  
**Classe** -> Estrutura de dados personalizada (para criarmos estruturas próprias);  
#### Pilares da OO
* **Herança**: A capacidade de a partir de um determinado objeto, herdar características de um outro objeto/classe; (Reuso de código)  
Ex: Todos os carros precisam ter características em comum, como a habilidade de frear, acelerar... Sendo assim, é mais fácil termos uma relação única "CARRO" com essas características do que criarmos as mesmas relações para cada tipo diferente de carro;
* **Polimorfismo**: Capacidade de substituir um determinado elemento concreto por um abstrato;  
Ex: Se um determinado objeto consegue realizar as atividades/ações de um classe, ele pode ser referido como essa classe. Um civic tem todas as funções de um carro, logo ele pode ser considerado um carro, por exemplo.
* **Encapsulamento**: Capacidade de usar determinado objeto na vida real sem entendê-lo internamente.  
Ex: Usamos a tv todos os dias, mas não sabemos como ela funciona internamente, temos visão apenas de sua interface manipulada por um controle remoto;
* **Abstração**: Fato de abstrair o mundo real para dentro do seu código (Modelar o que é do mundo real para dentro do sistema - **apenas o necessário**)
Ex: Num hospital e uma mecânica, ambos possuem clientes, mas para cada um as especificidades do cliente são distintas: No hospital deve-se levar em conta o tipo sanguíneo, enquanto numa mecânica precisamos saber o tipo de carro do cliente, a placa do carro, etc... 

#### Construtor
Toda vez que chamamos nossa classe no código com o auxílio de parênteses;  
Faz o "portal" entre a classe e o objeto gerado;  
Chamamos com o mesmo nome de nossa classe;  

    <var> = <nome_classe()>

No python, podemos ter somente um construtor;  
Criamos o construtor a partir de uma função \_\_init\_\;
```python
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
```

#### Classe tarefa
Possui: Descrição, atributo, data...
```python
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluído)' if self.feito else '')
```
Nesse caso, a tarefa é construída com descrição e é feito um sistema que mostra quais estão concluídas.

#### \_\_iter\_\_
Permite que o que foi inserido em sua função seja iterável.  
```python
def __iter__(self):
    return self.tarefas.__iter__()
```
Nesse sentido, não precisamos mais acrescentar o objeto a ser modificado em nosso código:
```python
# Antes:
for tarefa in mercado.tarefas:
    print(f'- {tarefa}')
# Depois:
for tarefa in mercado:
    print(f'- {tarefa}')
```
#### Herança
Atribuição das características e do código de uma classe pai para uma classe filha que terá funcionalidades mais específicas em relação à classe pai;
```python
class Tarefa: # Classe pai
class TarefaRecorrente(Tarefa): # Classe filha
```

#### Métodos Privados
Métodos que iniciam-se com "_" e são exclusivos de uma determinada classe.  
Não podem ser chamados fora dela.
```python
def _add_tarefa(self, tarefa, **kwargs):
    self.tarefas.append(tarefa)

def _add_nova_tarefa(self, descricao, **kwargs):
    self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))
```
Essas funções são usadas para complementar outras funções as quais sim são chamadas na main;
```python
 def adicionar(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
```

### POO Avançada
#### Membros Instância Vs Estáticos
Instância == Objeto;

Ao criarmos uma classe com seus devidos atributos e logo pós criamos instâncias relativas à classe, caso todos os atributos sejam de instância, em cada região de determinada instância estará "ligada" ao respectivo atributo da classe;  

Se um matributo da classe não se relaciona com as suas instâncias, ele é estático e seu valor será atribuído na própria classe. Além disso, ele poderá ser acessado pela própria classe, não sua instância.

Quando temos um método de instância, precisamos primeiramente criar uma instância chamando os atributos para depois chamar a função;  
```python
exemplo = ClasseExemplo(dado1, dado2)
    ...
exemplo.metodo()
    ...
```
Já no método de classe(estático), acessamos os dados diretamente pela classe;
```python
ClasseExemplo.metodo_estatico()
```

#### Tipos de Métodos
* Instância:
```
```
* Classe:
```
```
* Estático:
```
```

#### Propriedades
- #### Método Get/Set
Bom para validações

- #### Método c/ Decorator

#### Classe Abstrata
Contrário de uma classe concreta;  
Usado com, por exemplo, conceitos tão genéricos que se fossemos especificar adentraríamos muito em partes específicas. Assim, usamos este método que não possui implementação;
Este conceito não está disponível nativamente no Python;

#### Herança Múltipla
Herda de mais de uma classe;

### Gerenciamento de Pacotes
Muitas vezes é necessário baixar pacotes de terceiros para avançar em nosso projeto, adicionando novas bibliotecas utilizáveis e novas funcionalidades e facilidades para o código;

#### PIP
Achar comandos importantes:

    pip --help

#### Como iniciar um ambiente virtual
Dentro da pasta escolhida, executar no prompt:
```
python -m venv .<nome_pasta>
.venv\Scripts\activate
python -c "import sys; print('\n'.join(sys.path))"
pip install requests==<versao>
pip freeze > requirements.txt
pip install -r requirements.txt
```


## Certificado