# Observabilidade Mais Inteligente com Grafana Cloud | ObservabilityCON on the Road São Paulo 2025

Published on 2025-12-11T01:05:13Z

## Description

Nesta sessão, você vai aprender como a Grafana Cloud garante que você esteja coletando exatamente os dados de que precisa, ...

URL: https://www.youtube.com/watch?v=FA9_yBrIH6c

## Summary

No vídeo, Dylan, um engenheiro da Grafana com quatro anos de experiência, apresenta uma palestra sobre "Observabilidade Inteligente", focando em como capturar dados de forma eficaz para otimizar custos. Ele introduz três novos produtos: Adaptive Traces, Adaptive Profiles e uma ferramenta de gerenciamento de custos, todos lançados recentemente. Dylan discute a importância de utilizar telemetria adaptativa para coletar apenas os dados realmente necessários, evitando desperdícios. Ele detalha como o Adaptive Traces melhora a eficiência da coleta de dados, permitindo uma amostragem mais inteligente e o uso de inteligência artificial para decisões de amostragem. Além disso, ele apresenta o Adaptive Profiles, que analisa o desempenho do código e sugere otimizações, e conclui com uma nova ferramenta de gerenciamento de custos que ajuda a monitorar e atribuir despesas dentro da empresa. A apresentação inclui demonstrações práticas das ferramentas e destaca a integração com outras soluções da Grafana.

## Chapters

Here are 10 key moments from the livestream transcript along with their timestamps:

00:00:00 Introductions by Dylan, Backend Engineer at Grafana  
00:02:20 Overview of today's presentation topic: Intelligent Observability  
00:04:15 Introduction to Adaptive Telemetry and its benefits  
00:08:00 Explanation of Adaptive Traces and its importance  
00:12:45 Discussion on the challenges of traditional tracing and sampling methods  
00:15:30 Introduction to the new Adaptive Traces tool and its features  
00:20:10 Demonstration of how to use Adaptive Traces  
00:27:00 Introduction to Adaptive Profiles and its early preview  
00:30:15 Explanation of the benefits of profiling in telemetery  
00:35:00 Overview and demo of the Cost Management tool in Grafana  

These timestamps will help viewers navigate to specific sections of the livestream for more targeted information.

# Apresentação sobre Observabilidade Inteligente

Oi, gente! Boa tarde! 

Meu nome é Dylan, sou engenheiro da Grafana há 4 anos e atuo como back-end engineer no time do Loki. Estarei aqui o resto do dia para responder a quaisquer dúvidas que vocês tenham sobre Loki, logs e os outros bancos de dados que temos. Estarei na mesa ali de experts, então, se vocês tiverem alguma dúvida, é só me procurar.

Hoje, minha apresentação não tem nada a ver com o que eu apresentei ano passado, mas, para quem estava aqui, talvez tenha visto a outra apresentação sobre os "Adaptive Logs". O título de hoje é **"Observabilidade Inteligente: Capture os Dados que Você Precisa, Quando Você Precisa e Saiba o que Vai Custar."** O tema principal será como utilizar produtos que lançamos recentemente, há cerca de três semanas, para gastar menos e, ao mesmo tempo, ser tão efetivo quanto na resolução de problemas que a sua empresa enfrenta.

A ideia é que, mesmo que você receba um alerta à meia-noite, consiga resolver o problema, mas gastando muito menos. Vou falar sobre como você consegue isso, principalmente através de três novos produtos: **Adaptive Traces**, **Adaptive Profiles** e a ferramenta de **Gerenciamento de Custos**.

A Grafana está enfatizando a utilização da telemetria adaptativa para que você capture apenas os dados que realmente precisa, assim, você pode gastar menos, mas, como mencionei, continua sendo tão efetivo quanto antes. Também vou mostrar uma nova ferramenta que gostei bastante e que acredito que vocês também vão achar interessante. Ela ajuda a visualizar os seus custos e entender qual time está gastando mais.

## Telemetria Adaptativa

Aqui está uma linha do tempo de todas as ferramentas que já lançamos. Podemos ver que estamos em 2025. O **Adaptive Profiles** está depois dessa linha, e isso é porque vou mostrar o Adaptive Profiles para vocês. Ele está em preview ainda, e quem quiser pode participar desse preview fechado, mas ainda não está disponível para todos, como as outras ferramentas.

A primeira ferramenta que segue essa linha adaptativa que lançamos foi o **Adaptive Matrix**. Para lançar essa funcionalidade, levamos aproximadamente um ano e meio. A segunda, que foi o **Adaptive Logs**, levou quase um ano e foi a que apresentei ano passado. Agora, um ano depois, conseguimos lançar o **Adaptive Traces**, e o **Profiles** já está em private preview.

Com os aprendizados dos produtos anteriores, estamos conseguindo ser ainda mais efetivos. Vou falar primeiro sobre o **Adaptive Trace**.

### Adaptive Trace

O tracing é um tipo de telemetria muito poderosa, pois informa exatamente o que está acontecendo de ponta a ponta. Se você tem uma aplicação distribuída complexa com muitos microsserviços, o tracing vai te mostrar todo o fluxo que uma requisição teve. Por exemplo, quando um cliente nos diz que suas queries estão lentas, normalmente utilizo o tracing para descobrir exatamente qual parte da consulta está lenta.

Contudo, o tracing tem um problema de natureza: se você captura todos os dados de ponta a ponta, precisa de muita informação, e isso pode ser caro. Não podemos simplesmente descartar informações, pois pode ser que a informação descartada seja a que precisamos. Assim, a chave para não gastar muito é descartar os traces que não têm valor.

As ferramentas tradicionais de tracing utilizavam uma técnica chamada **sampling head sampling**, onde você precisa decidir imediatamente se vai manter aquele trace ou não. Isso pode ser problemático, pois impede que você veja o contexto geral para decidir se aquele trace é útil.

A segunda técnica é a amostragem de calda, que permite que você gere o trace e, ao final, decida se ele deve ser mantido ou não. O **Adaptive Traces** foi desenvolvido para garantir que você mantenha apenas os traces que são valiosos para você.

Se você usa Loki ou outra ferramenta, não há alteração na forma como você envia seus traces. No **Adaptive Traces**, você define recomendações e regras, e somente essas recomendações e regras que você configurar serão salvas, assim você só paga por isso.

### Demonstração do Adaptive Traces

Vou mostrar um demo do **Adaptive Traces**. Aqui está a tela do meu laptop com uma aplicação demo do OpenTelemetry. Você pode começar utilizando o **Adaptive Traces** pela barra da esquerda ou pela barra de pesquisa. Ao aplicar as recomendações, o sistema já começa a gerar novas regras automaticamente.

É possível criar novas políticas de amostragem para ajustar a coleta de dados conforme a necessidade da sua aplicação. E você pode optar por ampliar a amostragem em caso de incidentes ou anomalias.

## Adaptive Profiles

Agora, passando para o **Adaptive Profiles**, que ainda não está oficialmente lançado, mas já está em uso por alguns clientes de forma privada. O profiling é o tipo de telemetria que aponta na linha de código o que está acontecendo e descreve o problema que você está vendo no seu sistema. É uma ferramenta poderosa que permite ver detalhes sobre CPU, memória e outras métricas.

A ideia do **Adaptive Profiles** é a mesma do **Adaptive Traces**: você envia profiles para o nosso backend, que analisa se devem ser mantidos ou não. No meu demo, por exemplo, foram gerados 21 TB de dados, mas apenas 3 TB foram armazenados, resultando em uma redução de 83%.

### Demonstração do Adaptive Profiles

Vou mostrar um demo do **Adaptive Profiles**. Aqui, já ingeri dados e a ferramenta começou a analisar os frame graphs do meu profile. Ela utiliza uma LLM para gerar insights sobre o que pode ser otimizado no código.

Se você precisar de detalhes, pode expandir as informações e entender melhor onde estão os pontos de otimização. A ferramenta é integrada ao **Drew Down**, facilitando a investigação.

## Gerenciamento de Custos

Por fim, quero falar sobre a ferramenta de **Gerenciamento de Custos**. A Grafana começou a dar mais ênfase à visibilidade de custos, pois é importante entender como estão sendo gastos os recursos, especialmente em um contexto de nuvem.

Essa ferramenta atua em três frentes: prevenção (alertas sobre limites de gastos), atribuição (saber qual departamento é responsável pelos custos) e unificação (padronização da linguagem entre diferentes serviços de nuvem).

### Demonstração do Gerenciamento de Custos

Vou mostrar um demo da ferramenta de gerenciamento. Aqui, você pode configurar alertas para quando os gastos ultrapassarem determinados limites. Além disso, é possível visualizar os gastos por serviço, facilitando a atribuição.

A ferramenta também segue uma especificação comum, chamada **Focus**, que é utilizada por várias nuvens grandes, como AWS, Azure e Google.

## Encerramento

Para concluir, falei sobre a prevenção em relação aos custos, a atribuição e a unificação da linguagem. Essas ferramentas visam facilitar a gestão dos custos e melhorar a visibilidade, evitando surpresas desagradáveis.

Se alguém tiver interesse em participar do preview fechado do **Adaptive Profiles**, é só me procurar depois. Fico à disposição para perguntas!

## Raw YouTube Transcript

Oi gente, boa tarde é me apresentando. Meu nome é Dylan, é,
eu sou engenheiro da Grafana, tem 4 anos e eu sou back end engineer do time do Loki é depois
da apresentação aqui eu vou estar o resto do dia pra tirar qualquer dúvida que vocês tenham. Sobre Loki, logs, Ah, e os outros
bancos de dados que a gente tem? É, eu vou estar na
mesa ali de expert. Então se vocês tiverem alguma
dúvida aí que vocês queiram tirar, é só procurar. É hoje a minha apresentação,
não tem nada a ver com isso, mas quem estava aqui ano passado, né? Talvez tenha visto uma outra apresentação
que eu tinha apresentado ano passado, que era sobre o adaptative logs,
a de hoje o título é. Observabilidade inteligente é
capture os dados que você precisa. Quando você precisa e
saiba o que vai custar, é o tema principal aqui
dessa apresentação. Vai ser como você pode utilizar
produtos recentes que a gente lançou? Recentes, eu digo que a gente
lançou 3 semanas atrás. Sei lá como você pode utilizar esses
serviços para você gastar menos, mas ao mesmo tempo. Ser tão efetivo quanto
é resolvendo problemas que você que a empresa que você está tenha é a ideia é ainda que sei lá, você recebe um alerta à
meia-noite e você consiga resolver o problema,
só que gastando muito menos. É, eu vou falar,
como você consegue isso? Principalmente através
de 3 produtos novos, o Adaptive traces, Adaptive profiles e a ferramenta de gerenciamento de custos. É uma Confront uma visão recente da Grafana,
mas que está sendo bem, é enfatizada, é a questão de você usar a telemetria
adaptativa para você só é capturar os dados
que você realmente vai precisar e assim gastar menos. Mas igual eu falei,
continuando o teu efetivo quanto e também a parte de gerenciamento de cursos, vou mostrar uma ferramenta
nova que eu gostei bastante. Acho que vocês vão gostar também. É te ajuda a ver os seus custos. Saber o quanto vai gostar. A visualização é muito bem feita. Você consegue é entender qual
time está gastando mais. Eu eu acho que todo mundo
vai querer usar isso. Falando primeiro sobre a
telemetria adaptativa, é, aqui está um timeline de todas as ferramentas que a gente já lançou e aqui vocês conseguem ver que. A gente está aqui em 2025, né? Esse ano é 2025, é o Adaptive profiles, ele está depois dessa linha aqui, isso é porque eu vou mostrar o
adaptative profiles para vocês. Ele está em preview ainda, quem quiser pode participar
desse preview fechado, mas ele ainda não está,
é disponível ainda para todo mundo. Igual as outras ferramentas é,
mas são os dados interessantes. Aqui é a primeira ferramenta
que segue essa linha Adaptive que a gente lançou, foi o adaptative Matrix. E para lançar essa, essa essa funcionalidade durou
mais ou menos ali um ano e meio ou 2 anos. Para lançar a segunda,
que foi o adaptative logs, foi menos de 1 ano, quase um ano, que foi a que eu apresentei ano passado e agora é esse ano. Um ano depois, a gente conseguiu
fazer o adaptative traces e o profiles já está em private preview, então? É com os aprendizados dos dos produtos anteriores, a gente está conseguindo ser
ainda mais efetivo e tudo mais. E também tem ar, não é? Ajuda muito. Vou falar um pouco sobre o
Adaptive Trace primeiro. Que é o que eu falei,
que já está lançado e todo mundo pode usar. Falando especificamente de tracing, tracing é um tipo de
telemetria muito poderosa, porque é o tipo de é de
telemetria que você tem ali entre os 4 tipos, né? Métricas, logs, traces e profiles. Ele é o tipo que te diz exatamente o
que está acontecendo de ponta a ponta. Então, se você tem uma
aplicação distribuída, que é tipo muito complexa,
microsserviços, 30 microsserviços,
tudo está explodindo e tal. É o trace, ele vai te falar exatamente. É para uma certa requisição. Todo o flow que aquela
requisição teve é, eu uso bastante. Por exemplo, eu trabalho no flow que e às vezes a gente tem
um cliente falando pô, é mesmo? Minhas queries aqui estão
muito lentas por algum motivo, e a gente precisa investigar quando a gente está de oncall. E aí normalmente o que eu acabo fazendo é usando o tracing para isso. O tracing vai me falar exatamente qual
ponto da daquela consulta que está lento. Pô, que talento é o Cash? É puxar os dados da Cloud. É, está muito tempo em fila. E aí traceing,
me dá exatamente essa informação. Só que trace tem um problema que é meio que da natureza
desse tipo de telemetria, que é o seguinte. Se você está tendo todos
os dados de ponta à ponta, você precisa de ter muita informação, mas se você tem muita informação,
é muito caro. E você também não pode simplesmente
sair jogando informação fora. Se não, depois você não vai
conseguir resolver seu problema. Às vezes, a informação
que você jogou fora era a informação que você IA precisar. Então você precisa
manter o Trace completo. Ele precisa ser íntegro. Só que a chave para
você não gastar tanto é você jogar os traces que você não vai ver valor fora completamente. É então a pergunta que fica é, como é que eu mantenho
só os traces bons? É as ferramentas mais tradicionais
e mais antigas de tracing. Elas usavam a técnica chamada
sampling head sampling, ou amostragem de cabeça, que é o seguinte,
quando você começa a gerar esse trace, você já precisa imediatamente tomar uma decisão. Se você vai, vou voltar no outro site, porque eu acho que o
outro fica melhor depois. Você precisa tomar uma decisão se você quer manter
aquele tracing ou não. Já, já ajuda muito, não é? Por exemplo, você quer manter só 5%
dos teus traces totais, pô, assim que você vai começar a gerar o Trace,
você já toma uma decisão se se aquilo ali está nos 5% que você quer fazer, amostragem ou não. O problema disso é se você
tem que tomar essa decisão, se você vai manter o tradicional logo de cara, quer dizer que você não vai
conseguir olhar para o contexto geral para decidir se aquele trailers
IA ser útil ou não. E aí vem um segundo método,
de fazer sempre, né? De fazer amostragem mais interessante,
assim, mais efetivo, que é o que eu vou mostrar aqui, que o tempo usa,
que é o amostragem de calda, que é o seguinte, você gera o Trace, você faz tudo com
ele e vem a requisição, vai de um lado para o outro, o teu sistema distribuído,
o complexo e tudo mais chegou. No final, ele analisa tudo e decide se ele vai manter aquele Trace ou não. E aí, o que você vai pagar? É se no finalmente você vai
armazenar aquele Trace ou não. Então você não precisa só
aleatoriamente salvar 5%, você consegue ter regras muito mais complexas. E aí eu vou estar detalhando
isso com a nova ferramenta, que é o Adaptive traces. É, qual que é a ideia? É a premissa do adaptative traces? É, a gente quer que vocês só mantenham
os traces que são valiosos para vocês. O que que vai mudar no seu dia a dia? É do ponto de vista do
agent que você usa. Se você usa loy ou outra coisa,
não muda nada. Você continua mandando
todos os os seus traces. Só que nessa ferramenta que eu vou
mostrar um demo daqui a pouco, inclusive deixa eu desbloquear meu computador. É no Adaptive traces, você vai? Definir recomendações e regras e somente as recomendações
e regras que você está configurando é o que vai. É o que vai ser salvo no final,
então você só vai pagar por isso. E, por fim, no Grafana Tempo
o que você viu de valioso e que você seguiu as recomendações aqui, fez parte da amostragem, você consegue consultar
esses traces e aí vai estar tudo certo. Acho que a questão que fica é, você realmente precisa de
todo o dado que você gera? Quase sem precisar, não? Aqui tem alguns exemplos. É, você pode manter uma
amostra pequena ali de todos os tuas aqui que deram certo e que são rápidas. Você não precisa manter todas,
mas talvez o que você queira manter tudo. São os 3 que tem uma latência muito alta ou que tem muito erro aqui está falando quatrobutos específicos. Então assim é, imagina que
você trabalha num banco e aí você tem um sistema lá que faz auditoria, pô, talvez esse sistema ele seja muito mais
importante que outros. Então para isso é que é
um sample maior assim, e aí com Adaptive traces e com o tempo você consegue definir essas coisas. O Adaptive traces,
ele vai ficar te gerando recomendações você se você já sabe quais regras você quer,
você não precisa seguir as recomendações. Mas quando você está começando a usar, é legal ter recomendações, né? Ainda mais se você está
aprendendo o sistema e tudo mais. Aqui tem 13 exemplos de recomendações que ele gera no demo,
eu vou mostrar para vocês ele gerando para mim. E assim, apesar de serem bem gerais,
elas são muito úteis. A primeira aqui é 5% dos traces,
é bem comum essa. É a segunda traces com os erros
e a terceira traces lentos. Assim, normalmente é os 3 aí que você
vai querer começar dando uma olhada. Não sei quantas pessoas
aqui já usam open telemetry mais a boa notícia é se você já usou open telemetry. É as regras que você define
para as tuas recomendações. Se você já sabe,
o pintelímetro é o pareamento, é um para um ali,
então tudo o que você consegue escrever com um,
você já consegue escrever com outro, porque ele já segue. É a especificação, né? Então ajuda bastante. É os que eu mostrei
nos slides anteriores. Eles estão todos aqui. Tem coisas que tem aqui que não tem lá. Mas eu imagino que,
com o tempo assim vá adicionando ainda mais regras e tudo mais. Aqui a gente tem um exemplo
de um tenant interno nosso, é só para mostrar aqui, mais ou menos, qual efetivo dá para ser. É aqui no Adaptive
tracing em gestão 2.5 GB, isso aqui é por segundo, então a gente estava gerando 2.5 GB por segundo, mas no final, o que a
gente realmente armazenou foi 399 MB, ou seja, a gente. Né? Salvou ali 84%. A gente conseguiu jogar fora,
não precisou salvar e economizou, só que a alternativa nossa. Mas. Para vocês vai ser a mesma coisa, não é? Acho que acho. Acho que assim dá para
ver que é muito fácil você salvar assim pelo menos metade do de tudo que tu gera. Eu acho interessante. E agora, na minha opinião, a parte mais
interessante aí do Adaptive traces, que talvez seja diferencial em relação às
outras ferramentas de traces, né? É o time do Adaptive traces. É, eu conheço alguns deles
e eles estavam dando foco, um foco recente no na amostra. na amostragem de call que eu comentei. De na parte de analisar o contexto, consegui usar a IA IML
pra decidir se você vai. É ampliar aquele que ele trai ou não. Mudemos aqui eu vou mostrar pra
vocês mais ou menos como funciona, mas a ideia é o seguinte. É o teu serviço, ele tá saudável. Quase todos os dias,
o ano todo, tudo certo. Quando chega, a gente está em novembro,
vai ter a Black Friday. Quando for lá, a Black Friday
vai ter uma explosão de uso. É o é. Tem uma higiene de recomendação
dentro do Adaptive traces, que ele está o tempo todo. É comparando o teu tracic
com o que é normal, com o que é baseline,
com o que é anomalia. Quando ele percebe que
a anomalia aconteceu, ele entende que. Está acontecendo alguma coisa muito importante
que você vai querer entender melhor depois. Então ele aumenta as amostragens para se ampliar mais traces
durante aquele período que você está tendo anomalia. E assim, você mesmo que você não preveje
todos os casos onde é importante você ter uma amostragem maior,
ele automaticamente ele vai fazer isso para você. No demo, eu também vou mostrar
um pouquinho de como funciona. Há aqui. Não sei se vai dar para ver,
porque na imagem eu vou, então vou explicar aqui o que é que está acontecendo. Vocês estão vendo que
tem uma faixa azul aqui? Essa faixa azul seria tudo
que a gente considera normal, um comportamento normal. É aqui Ah, ele que está
escrito span latency, não é? Então é a latência do desse span quando o spam ele sai dessa faixa. É a ingini do do
adaptative trace entende que, caramba, uma coisa muito ruim está acontecendo, então ele começa a se ampliar mais traces, que é o que dá para você ver aqui. Aqui, por exemplo,
acontece um outro período grande onde fica fora dessa faixa, eles são players mais e assim por diante. Então, o que que é interessante? Você tá salvando ali 50%
dos teus cursos, você? É, você vai ter menos
coisa para pesquisar, só que não é por causa disso que Você vai ter é menos dados importantes
para você descrever um comportamento ruim que está acontecendo no teu sistema. É, ele é tão efetivo quanto é,
só que você realmente está gastando menos. Outra coisa interessante é ano passado,
quando apresentei, eu acho que eu apresentei o Explorer log. Se eu não tiver enganando,
nem lembro mais. É o as ferramentas explore
da Grafana Explorer metrics, Explorer logs e tudo mais. Elas foram renomeadas pra Drew down, mas a finalidade em si é a mesma, né? Uma coisa interessante
é o adaptive traces. Ele está 100% integrado com o drew down. Então se você já usa um,
é legal porque você está investigando. Ali você está John, qual e tudo mais. Você facilmente consegue pular
do adaptative Trace para o drew down e continuar a tua investigação, porque as ferramentas são
todas bem integradas. E agora vou mostrar um demo pra
vocês do adaptative traces. Bom, aqui é a tela do meu laptop
e eu tenho uma aplicação demo, é o open telemetry demo, inclusive talvez
alguém aqui já tenha usado e ele está gerando dados e tudo mais. É, eu vou. Como é que você começa
utilizando o adaptative traces? Você tem 2 opções,
você pode vim aqui nessa barra da esquerda e aqui tem todas as ferramentas adaptive ou você pode vim aqui, esse aqui normalmente
é o que eu uso, tá? Eu venho aqui na barra de
pesquisar e eu escrevo Adaptive. pois To com Internet. Tudo bem? É. Então eu ainda não não fiz nada aqui. Vou começar a usar agora, é? Ele já começou já me gerando
uma primeira apólice que é probabilística. Eu vou dar um apply aqui. É, esses aqui são todos os dados que eu
tô que eu tô ingerindo agora nas últimas 6 horas, né? Dá pra ver que é bastante é,
eu apliquei. Tópico é a primeira recomendação é, Hum, eu acho que aqui o ambiente aqui eu dei uma zoada nele. Ah não tá. É aquela apólice que é a
primeira que ele gerou, que é a probabilística. Eu apliquei ela. Ela aparece bem aqui
na lista de apólices. Eu posso vim nela, obviamente. E se eu achar que 5% é muito, 5%,
quer dizer, dropa 95% de tudo. Eu posso editar ela, né, obviamente? É a que eu posso editar o nome,
eu posso mudar o tipo e eu posso mudar a porcentagem. Se eu mudar aqui a porcentagem
que eu falei que é 5% pra 15. E dá um update, ele automaticamente ele
já faz o ele já atualiza no tempo, é? E se eu ficar aqui dando
F5 igual maluco aqui, vocês vão ver que o gráfico já vai mudar já e tudo mais. Mas mais interessante,
agora que eu ativei o Adaptive traces e que eu apliquei a primeira recomendação,
a engine já recomendou mais 2. Essa primeira aqui é de erros e
a segunda é a de slow traces, que eu falei para vocês que são as mais comuns. Eu vou aplicar elas também só por. Pra gente ver o que acontece,
apliquei mais elas e agora eu posso vir aqui em apoiar. Elas estão aqui, né? Se você precisar de de um histórico. E aqui estão as 3, né? A primeira aqui que ele
gerou e as outras 2. Isso aí foi gerado automaticamente. Quando vocês forem usar,
vai acontecer a mesma coisa com vocês. E aí vocês costumizam do
jeito que vocês querem? Mais mais interessante é o seguinte. Eu posso criar minha apólice? Alice. Aqui nos chips é aqueles
tipos que eu falei que seguem o open telemetry. Então se você já usa esse aqui, vai ser fácil para você
migrar para esse aqui. É as mais comuns que eu acho
que você vai querer saber, né? É o wand que é para
você combinar várias. Então, por exemplo, você tem uma
regra que é muito complexa, tipo, pô, tem que acontecer isso, isso, isso. E aí eu quero sampliar,
você vem aqui e usa o end? E tem o inverso do end, que é o drop. E tá em algum lugar aqui? Se todas as situações
que você colocar aqui, se todas elas acontecerem, você quer que 100% das vezes drop,
aí você coloca aqui e acabou. Bom, isso era um dos
ambientes que eu tinha. Esse ambiente ali tava novo, vocês viram que eu é habilitei
o Adaptive traces agora, apliquei as recomendações
agora e tudo mais. Esse aqui é um outro ambiente
que eu já deixei preparado. E aí, tipo, antes da apresentação aqui,
eu fiquei tipo, fazendo um monte de besteira nele para ele trigar aqui umas coisas é, vocês estão vendo
aqui que ele gerou essas recomendações aqui de anomaly detected. É porque eu fiz umas coisas lá para forçar o sistema a
ficar lento e tudo mais. E aí ele gerou essas
recomendações do ano e a Essa aqui é a tela que
vocês vão ver, tá? Aqui tem uma explicação
do que que aconteceu. Mas você pode clicar aqui. Pra você dar um zoom nessa recomendação? Aqui é a mesma coisa que
eu mostrei naquele slide, vocês podem ver aqui que tem uma faixa azul. Quando acontece uma coisa
estranha e sai da faixa azul? Ele começa a ampliar mais traces. E aqui tá o botão dos redon,
você pode vim aqui. Se eu tiver com Internet,
eu tô com Internet. E aí você pode se você acostumado já a usar
o drew down do traces daqui você já parte a tua é investigação,
você pode vir aqui em traces é aqui. Eu não, eu não recebi ainda os traces, mas se eu tivesse,
eu clicaria aqui e aí eu poderia dar um zoom nesse trace e entender exatamente o que aconteceu. É esse é o primeiro demo que eu
tinha para mostrar para vocês sobre o adaptative traces. Eu vou continuar agora. Com o adoptive profiles. Uh, ok. Então, voltando para os slides, é, acabei de mostrar para
vocês o adaptative traces, e agora a segunda ferramenta que
eu queria mostrar para vocês hoje é o adaptative profiles, é o Adaptive profiles. Ele ainda não está lançado oficialmente, mas já tem,
já é clientes usando de maneira mais privada. Vocês também podem. Eu vou mostrar para vocês um QR Code depois
que se vocês preencheram um server, vocês podem já estar participando
dessa prévia fechada. Mas eu acredito que não vá demorar
muito pra lançar pra todo mundo. É, eu queria começar falando que o profile dos 4 tipos
de telemetria com certeza é o menos utilizado. Aqui, sei lá, eu diria que. Talvez menos de 10% use assim. Eu mesmo eu venha usar
muito recentemente, mas ele é muito poderoso porque ele é o único tipo de telemetria
que é feito para te apontar na linha de código o que que está acontecendo, o que que descreve o
problema que você está vendo no teu sistema? Tem como você fazer isso com logs? Tem. Eu posso ir ir no meu log e botar
lá um, um atributo Collor e falar, pô, é essa linha aqui de esse log,
ele foi gerado por essa linha de código aqui. Só que se vocês usam log,
você sabem que isso pode ter cardinalidade finita,
você não pode indexar, se não pode indexar, pode ficar lento. Você pode resolver com logins,
mas logs não é feito para isso, profiling é profiling. Vai descrever não só
a parte da do código que eu estou comentando, mas. CPU, memória e tudo mais. Então é bem interessante. Se você usa go, a integração de profile
com go é muito boa. Para ver, gotina para ver,
scheduler para ver. garbage collector e tudo mais, então ela é bem mais
interessante que as outras. Pra ver a nível de código. É, e agora eu vou estar
falando para vocês sobre o adaptative profiles. A ideia é exatamente a mesma do
que eu falei do adaptative traces e que também era a mesma do adaptative logs. Então, se você já está
habituado com eles, essa migração é tipo muito simples. É a idade do adaptative profiles. Continua na mesma o teu. E a gente vai estar enviando profiles. É pro nosso backend. Esse backend vai ter uma engine
de recomendações e tudo mais. É, ele vai analisar se aquele
profile deve ser mantido ou não. Se for mantido,
aí é quando você precisa pagar pelo pelo dado que
você está armazenando. Se ele for descartado,
você não paga por isso. É aqui já é já o adaptative
profiles em em prática. Eu vou tentar falar mais
ou menos o desse aqui porque eu acho que está difícil para ler, mas é o seguinte. É, eu deixei rodando
o adaptative profiles para alguns dados que eu gerei. Ele. Ele começa a analisar
os frame graphs do meu, do profile que eu tenho. Ele usa uma LLM,
que eu Acredito que seja do OpenAI, para gerar um insight aqui do que que está acontecendo. É, então você consegue ao
mesmo tempo que você tem aqui o frame graph, sei lá. Aqui no caso é uso de CPU, não é? Ao mesmo tempo que você
tem aqui o frame graph explicando o quanto o de CPU está sendo gasto em cada função. Você também tem é um texto explicando. O que que seria uma
otimização esperada ali? É aqui é o Adaptive
profiles em em prática, né? Vocês conseguem ver que aqui, apesar de ter sido gerado
21 TB de dados, realmente só foram gerados armazenados 3 TB,
então uma redução de 83%. Muito bom. Também segue na mesma linha do
adaptative tracing que eu mostrei. É, e aqui? Esse insight aqui que vocês estão vendo é a mesma idade de
insights que eu mostrei para o Adaptive traces. Então ele está o tempo
todo olhando o contexto, vendo se vale a pena ou não. É você mexer a tua estratégia
de armazenamento de profiles. Vou mostrar agora um
segundo demo pra vocês. Que é sobre dessa vez,
adaptative profiles. Bom, eu vou pra esse outro
ambiente que eu tenho preparado e aqui eu já to rodando o adaptative profiles. É nesse meu tenante aqui eu
já ingeri um ponto 83 GB. Salvei só 249 MB. Redução muito boa também. É de novo. Antes da apresentação. Eu já fiz umas coisas aqui e tal
para ele me gerar uns insights, mas a visão que você vai ter é isso aqui, ó. É cada um desses aqui. Foi um insight que ele gerou
usando machine learning. Usando OpenAI e tudo mais
é e você pode detalhar e ver quais que são interessantes. Acho assim. É, é útil tanto no dia a dia, mas se acontecer uma coisa
muito problemática com teu sistema, você vai ver que o comportamento
vai ser ainda mais acentuado pro problema atual que você está tendo. Pra esse primeiro aqui. Ele está me falando o seguinte,
que é, eu estou. Eu deveria otimizar o jeito
que eu estou alocando memória e ele e ele conseguiu concluir isso principalmente pelo meu uso do é
pelas chamadas do run time malok GC. Né? Que é chamado a alocação de memória. Quem usa go provavelmente
já viu coisa parecida. Você pode deta...
você pode é expandir aqui, né? O frame graph. A resolução toda é ruim,
então não vai dar para ver, mas. Esse branco time maloke,
ele vai estar aqui em algum lugar. Se você precisa dar uma expandida maior e ver com mais detalhes
o que que está aqui, você pode vir em details. E aqui é a mesma coisa. Você tem uma explicação aqui, né? Utilizando é a LLM que eu falei. Explicando o que que você poderia
fazer de diferente nesse código? Se você quiser detalhar mais ainda,
você pode ir no go to drew down. Igual falei, eh tudo,
tudo está bastante integrado. Esse gap aqui que vocês
estão vendo é porque eu parei de gerar dados aqui porque
eu eu estava aqui apresentando, então não tem mais esses dados,
mas se eu tivesse esse gráfico, aquilo ia ser contínuo. Essa Barrinha azul,
azul aqui que vocês estão vendo é porque eu tô sampleando só a 10% dos dados totais. E aqui está o frame graph que
vocês estavam vendo aqui. Eu poderia, por exemplo,
pesquisar por maloke. Esse e aqui uh, a funcionar,
que ele tinha chamado. É, não sei por que que não
está aqui no frame graph. Acho que é porque eu estou
vendo só 30 minutos. Talvez seja isso. É, mas o fluxo seria por aí. Deixa eu só voltar aqui ver se tem mais
alguma coisa interessante pra mostrar pra vocês, Ah. É, imagina que você tenha, sei lá. Você tem 30 microsserviços, e aí todos esses microsserviços
tu sampleia ali mais ou menos 10% do total de profiles. Mas imagina que é teve um
incidente lá na sua empresa e esse incidente ele só. Afetou um microsserviço. Se você tá investigando
esse microsserviço, o que que aconteceu? Faz sentido você dar ênfase só pra ele? Se as recomendações
do adaptative profiles aqui não atender exatamente o que você precisa, você pode buscar esse serviço. Buscar significa você falar
para o adaptive profiles, cara, eu quero que vocês samplem tudo desse serviço específico
aqui nesse meu demo eu tenho cada um deles aqui é um serviço diferente, eu posso vim um deles e dá um create a sampling, falar qual a duração que eu quero é estender o meu
sampling para esse serviço. Então 1 hora e aqui eu
posso falar o motivo. O motivo, por exemplo, é, pô,
estou John, call, call é. Incidente, sei lá, deu um incidente. Vamos ver se eu consigo escrever. Então. Depois que eu aplico aqui
por 1 hora esse produto aqui que é o nem sei se dá para ler. A product count talog service, ele vai estar ampliando mais profiles. Vai ser 100% por um tempo. É, eu acho bem interessante porque te dá uma
flexibilidade muito boa, é. Se não, você vai ter que rezar
para sempre o sistema aqui. Adivinhar exatamente qual o cenário
perfeito que você quer e tudo mais. Ele, ele é muito é. Ele, ele acerta muito mais. É sempre bom você ter
um fall back ali, né? Se você né, vai que você está
na urgência e tudo mais. A última coisa que você quer
ficar esperando ele acertar. Bom pro adaptive profiles, é isso é,
eu vou passar agora pro slide novo, mas. A ideia é muito é parecida
com a dos outros produtos? É o que eu acho interessante é que é um conhecimento que
se você consegue, se você tem um, você consegue
reutilizar em todos os outros. Assim eu comentei antes, né? Ele está em prévia fechada. Se vocês é quem aqui tiver interesse, tudo mais em participar
da prévia fechada. Não quer esperar? Vocês podem ler esse QR Code. Não sei se vai dar tempo de
vocês lerem aí e tudo mais, mas vai ter um formulário lá. Vocês preenchem o formulário e aí vocês recebem um convite
para participar do da prévia fechada do do adaptive profiles. Eu vou passar o slide, mas se alguém quiser depois,
no final, é só me procurar que eu eu mostro de novo. E agora eu vou falar sobre a
terceira ferramenta e a última. Que é a ferramenta para fazer
gerenciamento de custos e cobrança. É, recentemente a Grafana
começou a dar uma ênfase grande também em melhorar toda a questão de visibilidade de custos. Porque custos não só na Grafana assim, eu acho que nuvem em geral,
se você for analisar, é. De mais recentemente, melhorou, mas sei lá, pega 5 anos
atrás era era meio difícil você prever o que que ia acontecer, né? Do teu uso e tudo mais, e entender o porquê que
cada coisa teve tal preço. É por conta disso, a gente teve um foco maior nessa
questão de entender entendimento dos cursos. Por a por transparência
e vários fatores. E esse trabalho em cima
de causa nos custos foi feito principalmente em 3 frontes. A primeira é a prevenção, para você ter um controle de
que teus custos não vão passar um certo limite. O segundo é a atribuição
para você poder saber. Qual departamento da sua
empresa tá tá sendo responsável por qual parte desses cursos? Porque isso é bem importante, né? Tipo, às vezes você tem uma empresa aqui,
um setor muito pequeno, está tipo sendo responsável por 95% dos custos porque estão usando muito
errado é você saber disso, é importante. E o terceiro é unificar,
no sentido de unificar a linguagem, porque é, né, sei lá, você usa Grafana, mas você
também usa alguma nuvem, você usa WS, por exemplo, é, as linguagens às vezes
são muito diferentes, os termos são diferentes,
o jeito de cobrança é diferente, então se conseguisse unificar
todas essas linguagens. E eu facilitar muito
a vida dos usuários. Então essa ferramenta que
eu vou mostrar agora, ela tenta atuar em todas essas 3 frentes. Primeiro, vou começar mostrando um
demo sobre a parte de prevenção. Será que foi? Está agora foi, dei play. Beleza, essa é a essa é
a visão da ferramenta, é o nome da ferramenta ecos management em bullying... em billing. E ali a gente vai começar
acertando alguns alertas. Esses alertas você pode definir se você quer em valor absoluto,
tipo, pô, passei de 1000 dólares, eu quero que você me avise, ou ou você pode falar
em termos de volume de telemetria, então é, vamos supor, passei de 100 GB ingeridos
para logs, eu quero que você me avise. E aí você consegue. Você está esse tipo de de threshold, e quando ele bate esse threshold,
você configura o que que você quer que ele faça? Você quer a mensagem no Slack? Você quer que dê um page e non call. E você também pode configurar ali os thresholds,
por exemplo, as vezes você quer que você não quer acordar
alguém meia-noite porque você chegou em 10% do thresholds ou 50%. Sei que é só uma mensagem,
mais às vezes, quando você está ali nos 90%,
quase um 100%, aí você quer uma
coisa mais agressiva? É aqui no demo, a gente
configurou 4 thresholds diferentes e eles ficam aqui nessa nessa tela de alerts. É, eu acabei de mostrar para
vocês sobre a prevenção. E assim que você atingir a prevenção, é você definindo uns thresholds. Se eles forem atingidos,
você vai ficar sabendo. Aqui é a mesma tela, mas acho que aqui a
visibilidade está bem melhor. É, você tem ali um gráfico,
ele mostra o que que você tinha falado, que era o limite ali, que você queria ser alertado. E aqui seria o gráfico subindo,
você foi ingerindo mais dados e tal. Você vai chegando mais perto do threshold. Você vai ter um maior controle
dos seus gastos assim. É a segunda coisa que eu
falei é sobre a atribuição, como é que é feita? A atribuição? Depende de qual telemtria
você está utilizando e que a gente está falando sobre se é log, symmetrical, trace e tudo mais. É, elas funcionam parecidas, mas você tem que configurar
o agente corretamente, né? Mas a ideia é, você vai
configurar as labels? Eu acredito que a label
padrão seja service name se você configurar o service name das coisas certinho. Aqui ele já vai mostrar. Os gastos por cada um
desses serviços names, então a atribuição fica mais fácil. Aquele cenário que eu falei
de tu ter um departamento que ta gastando muito, você vai ver isso aqui,
isolado de todos os outros. O terceiro que eu falei era
a unificação dos gastos. Comentei da WS e comentei
que é importante se ter uma linguagem unificada. E essa ferramenta e a Grafana no geral. Quando ela está gerando
o teu billing ali é a gente teve um esforço de seguir uma especificação que é comum utilizada,
que é a chamada focus. Eu nunca tinha ouvido falar
até algumas semanas atrás, mas aí conforme eu fui estudando aqui para apresentação,
eu vi que é existe essa unificação, todas as nuvens grandes. Estão utilizando então AWS, Azure é a Google,
Alibaba é, todas elas estão utilizando esse Focus e a Grafana
também está utilizando. Eu acho que acho que no
total só tem 8 empresa utilizando contando essas 3 e a Grafana. Então é uma coisa que eu sei
que a gente está sendo pioneiro e isso mostra também o esforço da Grafana em utilizar. Utilizar coisas abertas,
padrões abertos durante a apresentação também comentei bastante sobre o open telemetry. É uma coisa que assim a gente
colocou um foco grande e aqui é a mesma coisa. Estamos só recapitulando aqui, a apresentação está acabando,
é falei sobre a prevenção em relação aos custos. Você consegue isso na
na nova ferramenta, né? De de cross management. Lá você tem a sessão de alertas, então se algum momento lá na
sua empresa vocês tomaram um susto com a conta,
chegou muito alto e tudo mais. Agora não é mais precisa acontecer porque você pode configurar os alertas,
a questão da atribuição, se na na empresa que você
trabalha você já teve um problema de po um departamento aqui. Utilizou muitos dados,
ninguém, e a gente não sabia. A gente demorou um tempo até entender qual departamento estava
carregando esses cursos. Agora isso também já
está é incluído, né? É de maneira bem natural até,
e a partir da unificação, eu acho que é bem útil. Se você também interage
muito com nuvens diferentes, é hoje tudo bem, a linguagem já está mais unificada,
mas até um tempo atrás era um pouco mais difícil, é, você tinha que. Juntar dados de spreads diferentes? Você tinha que ter um setor da
empresa de finance ali o tempo todo, analisando e tudo mais. Essa questão meio que já
está bem mais bem resolvida.

