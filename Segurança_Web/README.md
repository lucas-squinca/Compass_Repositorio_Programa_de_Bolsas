Diretório Segurança em Aplicações Web
=====================================
### Este repositório tem por objetivo armazenar o conteúdo trabalhado no curso de "Segurança em Aplicações Web" da Udemy.

## Resumo

### Princípios da Segurança da Informação
* Autenticidade: A certeza de que um objeto provém das fontes anunciadas. Não sofreu nenhum processo de que não houve nenhuma modoficação;
* Disponibilidade: Os dados/informações precisam sempre estar disponíveis para quando forem necessários;
* Confiabilidade: Numa mensagem entre duas pessoas, apenas e unicamente **as duas** pessoas devem ter acesso à mensagem;
* Integridade: A mensagem que e digitei deve ser exatamente a mesma que você leu;
* Legalidade: Garantir a aderência de um sistema à legislação vigente;

### Análise de Vulnerabilidades e seus Tipos
É uma auditoria completa buscando encontrar possíveis falhas de segurança. Nela, busca-se sempre manter a integridade do sistema auditado.

* BlackBox: Auditoria sem o conhecimento da estrutura. Questões que envolvem o acesso ou arquivos não permitidos, algo mais amplo.
* WhiteBox: Auditoria com o conhecimento prévio da estrutura. Análise de vulerabilidades mais específicas;
* GrayBox: Uma mescla entre WhiteBox e BlackBox;

### Planejamento da Análise de Vulnerabilidades
* Coletar as informações gerais da empresa;
* Produzir um contrato de acordo;
* Produzir relatórios de análise;

#### Fases da Análise de Vulnerabilidades
* Reconhecimento do Ambiente: Coletar informações sobre o ambiente que será auditado;
* Varredura: Escanear toda a infraestrutura em busca de vulnerabilidades;
* Exploração: Tentar achar acesso -> Parte para o ataque;
* Escalação de Privilégios: Ganhar acesso ao sistema em níveis de super-usuário.

#### Metodologias para a análise de Vulnerabilidades
* OSSTMM: Manualmente é realizado o ataque. Feito pelo próprio usuário;
* ISSAF: Framework voltado para sistemas desktop;
* WASC-TC: Classifica as vulnerabilidades presentes;
* OWASP: Projeto que traz as principais vulnerabilidades da Web;

### OWASP
É direcionada para testes em servidores e aplicações Web;  
Eis aqui alguns testes realizados pelo projeto:
- Injeção: SQL, Local File Inclusion, Remote File Inclusion, Code Injection, Command Injection, XSS;
- Quebra do sistema de Autenticação;
- Directory Traversal;
- File Upload;
- Configurações Falhas;
- CSRF;
- Negação de Serviço;

#### OWASP BWA
Broken Web Aplication: Máquina virtual que executa várias aplicações com vulnerabilidades conhecidas, visando apresentar maneiras simples de testar e aprender sobre:
- segurança de aplicações web;
- técnicas de enumeração manual;
- ferramentas automatizadas para enumeração;
- ferramentas de análise de código fonte vulnerável;
- ataques na web;
- WAFs e tecnologias de código similares;

#### OWASP ZAP
É uma das ferramentas de segurança gratuitas mais populares do mundo!!

Trata-se de um proxy que facilita realização de testes de intrusão em aplicações Web, pois possui scanners automatizados em sua toolbox, dentre outras funcionalidades para o mesmo fim, podendo encontrar automaticamente vulnerabilidades de segurança em seus aplicativos da web enquanto estiver desenvolvendo e testando seus aplicativos, bem como pentesters.

### Testes de Vulnerabilidades e Injeções Diversas
#### SQL Injection
É um método para extrair ou modificar dados de dentro de um banco de dados relacionado a uma aplicação web ou sistema;
#### XSS
É uma vulnerabilidade encontrada em sites da web, onde o cibercriminoso pode inserir códigos javascript para obter certas vantagens em relação às vitimas;  
Ele é normalmente aplicado em páginas que sejam comuns a todos os usuários, como por exemplo a página inicial de um site ou até mesmo páginas onde usuários podem deixar seus depoimentos. Para que o ataque possa ocorrer, é necessário que nessas abas haja um espaço para que o criminoso possa digitar, como campos de busca ou inserção de comentários.
#### Command Injection
É possivel, por meio dela, executar comandos diretamente da aplicação, conseguindo acesso não autorizado ao sistema.

Inserimos mais comandos além daqueles desejados dentro de um bloco de comandos para visualizar informações desejadas.
#### LFI & RFI
* LFI: Permite que coloquemos arquivos que já existem dentro do sistema operacional. Esta falha ocorre, por exemplo, quando uma página recebe como entrada, o caminho para o arquivo que será incluído, e esta entrada não é validada de forma correta pela aplicação web.
* RFI: É o processo de inclusão de um arquivo externo ao servidor, dentro do mesmo.

##### Como evitar?
* Evite uploud de arquivos no sistema e, se necessário, use um processo de validação para confirmar se o que está sendo upado é realmente um arquivo seguro;
* Não permita que usuários que não necessitam do powershell tenham permissão para manuseá-lo.

#### Comunicação TCP
Envio de uma mensagem e, ao recebê-la, sempre haverá uma confirmação de recebimento.

Operação da comunicação TCP:
1. Estabelecimento de Conexão:

Antes de iniciar a transferência de dados, o TCP inicia um processo de estabelecimento de conexão. Isso envolve um "aperto de mão" de três vias, conhecido como o handshake de três etapas, entre o remetente (cliente) e o receptor (servidor).
O remetente envia um pacote especial chamado SYN (Synchronize) para o receptor.
O receptor responde com um pacote SYN-ACK (Synchronize-Acknowledgment).
O remetente, por sua vez, responde com um pacote ACK (Acknowledgment), indicando que a conexão foi estabelecida com sucesso.

2. Transferência de Dados:

Após a conexão ser estabelecida, os dados podem ser transmitidos em ambas as direções.
Os dados são segmentados em pacotes menores para transmissão, cada um com um número de sequência.
O receptor recebe os pacotes, reordena-os e verifica se estão livres de erros usando somas de verificação (checksums).
Se um pacote não for recebido ou estiver corrompido, o receptor solicitará sua retransmissão.

3. Controle de Fluxo:

O TCP monitora o congestionamento da rede e ajusta a taxa de transmissão de acordo com a capacidade da rede e a disponibilidade de recursos.
Ele utiliza um mecanismo de controle de fluxo baseado em janelas, onde o receptor informa ao remetente quantos bytes ele pode receber sem sobrecarregar o buffer.

4. Encerramento de Conexão:

Quando a comunicação é concluída, a conexão TCP é encerrada.
Isso envolve outro "aperto de mão" de três etapas, com pacotes FIN (Finish) para indicar que a transferência de dados está concluída.
O receptor confirma o encerramento enviando um pacote ACK.
Cada lado da conexão pode encerrar independentemente sua parte da comunicação.

Se o sistema não possui nenhum nivel de filtragem de arquivo, podemos enviar códigos maliciosos.

#### Denial of Service
Ataque de negação de serviço, onde o objetivo é indisponibilizar o servidor alvo.

Faz uma sobrecarga em um computador ou servidor para que recursos do sistema fiquem indisponíveis para seus utilizadores.

### Transporte Inseguro e Métodos para Recuperação de Senhas Vulneráveis
Quando estamos transportanto dados de maneira não criptografada basicamente estamos mostrando esses dados para todo o mundo!!

#### Brute Force
Aplicado para conseguir acesso a contas em determinado site, serviço, desktop ou servidor por meio de tentativas de login e senha, até que se escalone os provilégios. A força bruta pode ser aplicada tanto manualmente quanto automaticamente por meio da utilização de softwares.
### Métodos de Descoberta Automática de Vulnerabilidades
* **OWASP ZAP**: Possui a capacidade de mostrar automaticamente uma série de vulnerabilidades.
* **Nikto**: Ferramenta poderosa para testes de diversas vulnerabiliades.  
É possível visualizar algumas de suas funcionalidades por meio do comando:

    nikto --help

* **WPScan**;
### Métodos para Proteção
#### Proxy de Aplicação
Proxy de aplicação é uma camada de proteção entre a internet do usuário e o servidor web que ele deseja adentrar. É uma elaborada versão de filtragem de pacotes.

Ele analisa todos os dados de aplicação de um pacote. Todos os pacotes que saem da rede de internet e vão para o servidor web passando pelo proxy reverso são analisados e entende o que o pacote está "falando", assim liberando o acesso para o nosso servidor.

Após isso o servidor interpreta o pacote e o devolve para o proxy de aplicação, o qual também retornada o pacote para a internet.

##### ModSecurity
É um firewall de aplicação WEB que é considerado um kit de ferramentas para o monitoramento, registro e controle de acesso de aplicações web em tempo real.  
É open source e cross platform.  
Ele, por meio de regras, consegue proteger as aplicações WEB de diversas ameaças existentes.

O Modsecurity opera seguindo quatro princípios de orientação. São eles:
* Flexibilidade: Possível pois sua linguagem é baseada em regras determinadas.
* Passividade: O modsecurity não toma decisões por você, pois faz apenas o que é detrminado pelo usuário.
* Previsibilidade: o ModSecurity é previsível e te permite entender a ferramenta por completo, inclusive seis pontos fracos para que o usuário possa contorná-los.
* Qualidade acima de quantidade: Ele possui uma quantidade de recursos limitada, mas que são frequentemente trabalhados e melhorados para que funcionem na melhor maneira possível!

#### HTTPS
É uma implementação do protocolo HTTP sobre uma camada adicional de segurança que utiliza o protocolo SSL/TLS. Essa nova camada permite que os dados sejam transmitidos por meio de uma conexão criptografada e que se verifique a autenticidade do servidor e do cliente por meio de certificados digitais.

#### Certificado SSL
A sigla SSL significa (Secure Sockets Layer), uma tecnologia global de segurança padrão que permite a comunicação criptografada entre um navegador da Internet e um servidor da Web. É usado para reduzir o risco de roubo ou adulteração das informações confidenciais por hackers e ladrões de identidade.

Em sua essência, o SSL permite uma "conversa" privada entre duas partes.

##### Tipos de Certificado SSL
* Único: protege um nome de domínio ou subdomínio totalmente qualificado;
* Curinga: cobre um nome de domínio e um número ilimitado de subdomínios;
* Multidomínio: protege vários nomes de domínio;

##### Tipos de Validação
* Validação de domínio: Cobre a criptografia básica e verificação da propriedade do registro de nome de domínio. Normalmente, é necessário que se espere alguns minutos até alguma horas para receber essa certificação.
* Validação da organização: Além da criptografia básica, alguns detalhes do proprietário são autenticados.
* Validação estendida (VE): Essa certificação oferece um maior nível de segurança devido a sua análise completa que é efetuada antes da emissão. São verificadas, além das instâncias citadas nas outras validações, a exigência jurídica, física e operacional da entidade. Normalmente é necessário esperar de alguns dias até várias semanas para receber esse tipo de certificado.

## Certificado
![certificado](/Segurança_Web/Certificado/Certificado%20de%20Conclusão%20Segurança%20Web.jpg)