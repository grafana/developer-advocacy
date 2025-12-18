# Dos Dashboards às decisões: Como a IA com Agentes Inteligentes está Transformando a Observabilidade

Published on 2025-12-11T01:05:01Z

## Description

A inteligência artificial está transformando a observabilidade de um processo manual e centrado em especialistas para uma ...

URL: https://www.youtube.com/watch?v=CeXQLDXWgP4

## Summary

O vídeo apresenta uma palestra de Beto Muniz, engenheiro de software na Grafana, que discute inovações recentes em inteligência artificial e machine learning na plataforma Grafana. Muniz compartilha sua experiência de três anos na empresa e os produtos que ajudou a lançar, incluindo o Grafana Assistant, uma ferramenta que visa melhorar a eficiência da análise de dados e a rapidez na entrega de soluções. Ele aborda como a inteligência artificial transforma o desenvolvimento, facilitando protótipos e a análise de problemas, mas também introduz novos desafios para monitoramento e responsabilidade. A apresentação inclui uma demonstração do Grafana Assistant, mostrando suas funcionalidades, como personalização e integração com serviços como GitHub. Muniz conclui destacando a importância do feedback dos usuários para aprimorar a ferramenta e a visão de um assistente proativo que não só responde, mas também antecipa problemas. A ferramenta está disponível no Grafana Cloud, com um modelo de preços definido.

## Chapters

00:00:00 Introduções e boas-vindas 
00:02:30 Apresentação de Beto Muniz e sua experiência na Grafana 
00:05:00 Discussão sobre o impacto da inteligência artificial no desenvolvimento 
00:08:15 Lançamento do Grafana Assistant e sua funcionalidade 
00:11:00 Como o Grafana Assistant pode ajudar usuários novos e experientes 
00:15:00 Demonstração de uso do Grafana Assistant em uma análise de infraestrutura 
00:20:00 Explicação sobre a personalização do assistente através de regras 
00:25:30 Integração do Grafana Assistant com GitHub para geração de código 
00:30:00 Feedback dos usuários sobre o Grafana Assistant e sua adoção 
00:35:00 Futuros desenvolvimentos e funcionalidades do Grafana Assistant 

# Palestra sobre Grafana e Inteligência Artificial

**Está me ouvindo? Beleza?** Eu costumo falar um pouco baixo, então qualquer coisa, pode falar "fala mais alto". Tudo certinho? Inicialmente, boa tarde, bom dia, algo assim. Meu nome é Beto Muniz e atualmente sou Software Engineer na Grafana. Estou aqui há aproximadamente três anos e já passei por diversos times e lançamentos. Meu primeiro lançamento na Grafana foi o **Prometheus Care Builder**, seguido pelo **Grafana SLO**. Atualmente, estou no time de inteligência artificial e machine learning, e recentemente lançamos alguns produtos nessa direção.

Hoje, trago uma reflexão sobre como estamos projetando e construindo estudos em inteligência artificial. Antes de continuar, gostaria de saber: quem aqui utiliza inteligência artificial para programação? É legal, não é? Essa reflexão é pertinente, pois a inteligência artificial tem sido muito utilizada para resolver problemas diversos, tanto pessoais quanto profissionais.

Essa transformação de paradigma no desenvolvimento e análise gera um cenário onde entregamos tudo mais rapidamente. A ponte entre a ideia e a implementação foi reduzida, permitindo que possamos prototipar e experimentar muito mais. Contudo, isso também traz novos desafios, como sistemas para monitorar e mais sinais para entender, resultando em maior responsabilidade para as equipes.

Nesse contexto, a Grafana trouxe o **Grafana Assistant** para auxiliar nesse fluxo de trabalho com inteligência artificial. A ideia é que, independente do seu nível de experiência, o assistente ajude na busca por soluções. Muitos de vocês já estão familiarizados com ferramentas que utilizam linguagem natural para resolver problemas, e a proposta do assistente é ser uma ferramenta útil para todos.

O assistente funciona em várias partes da sua stack de observabilidade, apoiando no **filing**, **tracing** e **SQL**, seguindo a nossa filosofia de "big tent". Isso significa que quanto mais integrado, melhor. Ele abrange diversas fontes de dados, incluindo aquelas que são tradicionalmente mais complexas de consultar.

A personalização é um aspecto fundamental do assistente. Utilizamos um conceito de regras, que permite definir comportamentos e boas práticas para que o assistente chegue ao objetivo que você deseja. Por exemplo, se ele estiver sendo prolixo ou utilizando uma língua que você não deseja, você pode ajustar essas regras.

Além disso, o assistente também fornece conhecimento e integrações com ferramentas como Jira e GitHub. A nossa visão é que o Grafana Assistant não seja apenas uma ferramenta passiva, mas algo proativo que ajude a colaborar com a sua equipe. Ele pode atuar em investigações, permitindo que múltiplos agentes ajam em incidentes e antecipem problemas antes que eles aconteçam.

Agora, gostaria de fazer uma demonstração para vocês. Para isso, já preparei alguns prompts para otimizar nosso tempo. O primeiro prompt pedirá ao assistente que crie um diagrama da minha estrutura com base nas métricas mais recentes e faça uma análise do **Framegraf**.

O assistente começa a planejar as próximas ações e gera uma pré-análise da infraestrutura, acelerando o processo de resposta. A integração com o **Infrastructure Memories** permite que ele mapeie serviços e defina representações dentro da estrutura.

Após gerar o diagrama, ele me apresentará um follow-up. O assistente também permite que você adicione contexto, como métricas específicas de uma fonte de dados, o que enriquece as respostas.

Agora, ele está analisando um problema crítico na infraestrutura e me dará recomendações. Uma das funcionalidades interessantes é que ele não age sem autorização; ele pergunta se deseja que ele crie uma branch no repositório e gere um código de correção para os problemas identificados.

A interação com o GitHub já está configurada, e o assistente criará a branch e o arquivo com as correções necessárias. Ele também retorna um link para a branch criada, permitindo que você acesse as otimizações feitas.

Para concluir, o **Grafana Assistant** agora está disponível para todos no Grafana Cloud. O custo é de **20 USD por usuário ativo mensalmente**, mas é gratuito até janeiro para qualquer tier. Além disso, a funcionalidade de investigações está em **public preview**. Nossa visão é criar uma plataforma de observabilidade que não apenas monitore, mas também previna e atue de forma autônoma.

Estamos muito animados para continuar desenvolvendo essa visão e recebendo feedbacks de vocês. O Grafana Assistant tem ajudado muitos usuários a reduzir a carga cognitiva e a encontrar causas raízes mais rapidamente. Agradeço a todos pela atenção e estou à disposição para perguntas!

## Raw YouTube Transcript

Está me ouvindo? Beleza? Eu costumo falar um pouco baixo,
então qualquer coisa pode falar. Fala mais alto, fala mais alto. É, deixa eu ver aqui. Tudo certinho? Beleza, pessoal, é bom. Primeiramente não é boa tarde, bom dia. Alguma coisa assim no
meio está quase bom. Boa tarde já não é? Sou a? Palestra antes do almoço antes
da próxima que vem do almoço. Está tudo certo. Hoje a gente não almoça meio-dia. É beleza. Meu nome é Beto Muniz. Eu atualmente sou frente. É sendo software engeneer na grafana? É. Estou aqui há mais ou menos 3 anos e já passei por diversos times, né? Já diversos lançamentos. É o meu primeiro lançamento
dentro da Grafana foi o, Prometeu's Care Builder, depois foi o Grafana SLO. Agora eu estou no time de inteligência
artificial e machine learning. E a gente, né? Recentemente fez o lançamento de
alguns produtos nesta nessa direção. É que eu vou falar mais sobre eles aqui. E a gente trouxe essa reflexão, não é que aí é está acelerando
como projetamos, construindo estudos. Não é quem aqui só fazendo uma pergunta, quem é que utiliza
inteligência artificial para código? É legal? Ei, basicamente,
eu acho que essa reflexão faz muito sentido, né? A gente vem utilizando muito mesmo e para resolver nossos problemas, seja qual for,
seja para coisas pessoais. Alguém até me fez uma
pergunta hoje sobre isso, seja para coisas de trabalho, não é? E basicamente? Essa transformação de
de paradigma eu diria até de desenvolvimento de análise, seja qual for o motivo que você
estiver utilizando ali. A sua, a sua inteligência
artificial, né? Ou a de alguém não é, é cria. Um cenário onde a gente entrega
tudo muito mais rápido, né? A ponte entre a ideia e a implementação Ela foi reduzida, né? A gente consegue prototipar,
experimentar muito mais. Porém com isso, né,
a gente também enfrenta novas, novas realidades, novos problemas, né? Com o mais sistemas para monitorar, né? Mais sinais para ter que entender e, no fim do dia,
mais responsabilidade para as equipes. E nessa, nesse, nessa direção,
grafana traz o grafana assistent, não é para também dar mais problemas aí para vocês,
no sentido de mais sinais, para mais coisas, para fazer com esse tipo de solução
e inteligência artificial? De solução para a inteligência
artificial no workflow de vocês? Deixa eu só. A ideia, né? É bem comum. Acho que, como muitos levantaram a mão, até quem não levantou a
mão e não está utilizando no dia a dia, acho que
já está bem adaptado a como funciona esse tipo de ferramenta, né? Você vai utilizar ali linguagem natural é para basicamente
alcançar pelo menos essa expectativa, né? Alcançar soluções que vocês. é A solução dos problemas que vocês
estiverem enfrentando ali no momento? A ideia, né? É justo, opa. Sumiu a opa, vou. Apareceu no slide aqui. Só. Deixa eu dar continuidade. De qualquer forma,
a ideia é justamente auxiliar, independente do tipo de usuário que você for, é. Ao utilizar a Grafana, né? No caso é seja você um usuário novo. E uma analogia que eu gosto
de fazer com relação a isso é que como usuário novo, a gente sempre a Grafana,
lança algo novo ou até igual. Eu escutei aqui falando sobre
se dá suporte ao diário ou alguma coisa do tipo. Sempre que alguém aparece com uma nova,
um novo problema, a gente é usuário novo naquele problema. É um é uma novidade para a gente. A gente não gostaria de ter
problemas no final do dia, né? Então, nesse sentido,
o assistente te ajuda muito, seja você um usuário novo do Grafana em específico, mas também eu acho que ele ajuda
ainda mais se você é experiente, não é? Você vai ser capaz de dar mais contexto, dar mais insights ali para ele,
a conduzir ele a te ajudar a chegar em
uma solução mais rápido. É prova, né? Dessa ideia maluca que eu estou, que eu estava falando de velocidade, né? Que a gente está tendo, eu não sei. Alguém que já experimentou
o Grafana Assistent? No cloud. É bacana. Vocês provavelmente
que já experimentaram, provavelmente repararam. Não sei se estão experimentando
tipo de forma constante, mas ele muda bastante. A gente está seguindo mesmo essa
tendência de mercado de entregar rápido. É o. A nossa visão basicamente
sobre este tipo de ferramenta e um gráfico que a gente colocou aqui é que foi uma até ali, mais ou menos meados de setembro,
mês de setembro, enfim, mas mais ou menos
meados da opção mesmo. A gente estava está entregando ali
uma nova versão a cada 4 dias. Obviamente, utilizando-se inteligência
artificial para nos auxiliar a chegar nos nos objetivos que a gente quer
chegar com essa ferramenta. É, mas o que que tem de novo
ali desde o que foi apresentado na obscom até aqui? Gente, não tem tudo, não vou falar
tudo porque realmente é muita coisa, mas eu vou tentar passar aqui por cima de
das coisas mais importantes que a gente acredita que seja interessante para vocês. É o assistente no momento ele
ele funciona em mais é partes. Não é da sua state de
observabilidade, não é? A gente coloca ali para
o filing stressing. SQL é seguindo,
não é a nossa filosofia de big tent, então essa vai ser sempre a tendência. Quanto mais integrado, melhor, não é? É acesso a diversas Fontes de
diversas Fontes de dados data sources não é no final do dia, incluindo aqueles não é,
que são tradicionalmente mais complexos. Não é de consultar, né? E extrair valores úteis
mesmo para o dia a dia. É como tracing,
profiling é a ideia principal é que o seu Grafana consegue acessar algo. O Grafana assistente,
a gente também vai conseguir acessar é, e além disso não é. Tem também a parte de personalização, que é uma parte
fundamental para esse tipo de ferramenta. E a gente faz isso por meios de roose, que é um conceito de
regras que você pode definir tanto comportamento como também boas
práticas ali para o assistente, basicamente chegar ao objetivo que você quer. Às vezes, vamos supor, ele é muito. É prolixo, não é? Ele desenvolve demais ali. A análise que ele estiver fazendo traz coisas
que você não queria que ele trouxesse. É às vezes responde muito em inglês, você queria que ele
tivesse te respondendo o tempo todo em português? É qualquer. Qualquer regra que você
queria passar para ele, ele vai respeitar, não ele às vezes. É esse tipo de regra que
você tiver passando? É. Além disso, ele também é uma maneira de. É uma das uma maneira de. Fornecer conhecimento para
para o assistente, não é? Outra maneira de personalização
é os mcp servers, né? É essa seria uma maneira que eu sugeriria
para quem, por exemplo, quer fazer uma integração com Jia ou com algum outro
tipo de gerenciador de tarefas, né? Que a gente tem. A gente tem pré-configurado
já do GitHub, essas 3 aqui e do linner aqui também. Mas isso aqui tem
bastante flexibilidade, porque existe a maneira de adicionar. MCV service customizados. Dependendo da sua demanda. Capsula aquilo dentro de um MCP server ou consome de um serviço
externo que você já já tenham aí? No seu steck que basicamente
vai o Grafana system, opa, vou fui para a frente o Grafana assistente, ele vai ter o conhecimento
daquele tipo de ferramenta que você também utiliza. É. Além do que já foi dito,
não é aqui no keynote, não é integração [ininteligível]. E. Muito mais é. É BAC para controle de acesso,
é compartilhamento, não é de. Conversas, né? Conversação é que mais
geração de código. Por exemplo, se tiver um
problema específico na sua estec que durante a análise do assistente, ele basicamente viu que. É, era algum trecho, algum link que estava
acontecendo em algum trecho do código específico. Se ele tiver, por exemplo,
a integração com kit hub, que consegue já enxergar o seu código, ele vai conseguir não só gerar, mas também fazer interação, né? Direta, já com o get hub,
criando o boo request, algo que eu vou tentar fazer por aqui em uma demo. Vamos torcer, vou dar tudo certo. Deixa eu ver tutorial, né? Basicamente para poder fazer
a introdução de vocês. E basicamente pessoal. Esse a adoção tem sido a resposta? A essa ferramenta tem sido bastante
interessante dos usuários aqui. Foi quando? A gente anunciou o Grafana assistente na
grafanacom mais ou menos 6 meses atrás, e essa tem sido a adoção. Dele nessa esse gráfico
que ele tem mostrado como tem sido a aceitação e adoção de usuários recorrentes,
não é utilizando a assistência, quer dizer, tem impactado de fato. O dia a dia não é de
quem está utilizando e para quem quiser utilizar, por favor, não é, nos mande feedback. A gente precisa desses feedbacks. A gente não espera que a
ferramenta esteja 100%, até porque esse mercado ainda está em, né? Todo mundo sabe aí em constante. Desenvolvimento, né, eu diria? E então é um é uma, é um, é um. É uma coisa que a gente
precisa de feedback para entregar para
vocês a melhor solução possível. É. E a jornada não necessariamente
acaba por aqui, não é? É? Vocês já ouviram alguém aqui? Já ouviu? Acho que no keynote foi falado isso, mas dos Grafana da
funcionalidade de investigações. Do Grafana assistente. Vocês ouviram, não é? Então nosso nossa visão é que a gente. Possa possa, né? Oferecer para vocês. A. A ideia de que essas não
só sejam copiloto uma, ferramenta passiva, mas algo que seja proativo, preventivo, que basicamente possa atuar como
um colaborador da sua equipe, né? Não substituindo necessariamente,
vou colocar em palavras mais claras, mas obviamente fazendo uma tarefa que o seu
colaborador não queria focar agora, ele queria focar em outra. E a ideia é do investigations, é justamente. Nessa direção? É ir além do chat para a gente,
é você se questionar, não é? E se múltiplos agentes pudessem agir? Em todos os Data
services é sempre um incidente acontecido. Qual que seria as possibilidades
sobre isso, não é? É, é o assistente já
economiza há bastante tempo, mas e se você nem se
você necessariamente não? Nem soubesse algo que estivesse
acontecendo já e o agente, de forma proativa, chegasse e. Fizesse isso pra vocês. Eu já é algo que não
atua só no problema, né? Mas na prevenção dele também. E né? A nossa resposta para isso,
como eu já disse, foi a funcionalidade investigations dentro do Grafana assistent que
já falamos aí dentro do keynote. É, estou olhando aqui e agora, ué? Estou desatualizado. Mas beleza. Há beleza? A gente, opa, ainda está aqui? Pode mudar? Bom, agora eu vou fazer uma
demonstraçãozinha para vocês. Tinha uma agenda ali, um slide. Estou falando que estava desatualizado,
mas tem uma agendazinha. A ideia é fazer uma introdução do Assis, a gente também fazer
uma introdução aí do investigations. Acho que vocês já viram aqui no demo. A Marília acabou de passar,
mas eu vou tentar fazer. Tem muito pouco tempo, mas eu já meio que preparei
também algum um plano bezinho aqui caso. É, não dê tempo do meu assistente,
demore um pouquinho para responder. Está bom? É. Deixa eu ver como é que está tudo? Ok, vou aumentar aqui. É. Bom. Já obviamente escrevia os meus prompts, não é para não demorar
escrevendo, mas aí o primeiro prompt aqui vai ser é basicamente ele fazer um
diagrama da minha estrutura, né? É baseado nas métricas mais
recentes e retornar um follow-up é para me fazer fazer uma análise do framegraf, não é? Vou dar um entre aqui. Vamos. Esperar tomara que a internet
esteja boa aqui, se não. Olha, primeiramente ele
começa a planejar, não é o? O que que ele quer fazer
as próximas ações? Fazer um plano de ação. É. Que ele já retornou? Ah, inclusive isso aqui é uma
funcionalidade bem interessante, que é também relacionada à customização. Que é o infrastructure memories
eu posso mostrar para vocês enquanto ele roda, é? A gente vai no
infrastructure memories, eu previamente fiz um. Uma. Um escaneamento da minha infraestrutura e ele mapeou serviços que eu tenho nessa minha infraestrutura e. Definiu basicamente o que que é a
representação desse dessa entidade dentro da minha estrutura? E com base nisso, nossa demo já está já está dando certo aqui, não é? E com base nisso, ele. Prover para para o assistente, né? É uma pré-análise,
basicamente do que eu tenho na minha infraestrutura. Isso eu acelero bastante o processo. De resposta, beleza, acabou aqui o. E é só uma forma de customizar, quer ou não,
o comportamento do assistente. Sem isso você teria outro comportamento,
comportamento mais lento, não é? Ele teria que fazer todo
esse processo e tudo mais. Agora eu vou usar essa. Eu pedi a ele um follow-up, para poder fazer uma
análise do framegraf, né? E eu vou basicamente
tentar fazer por aqui, caso contrário, mando o comando. Ele na verdade,
ele gerou um prompt para mim e eu vou usar aquele prompt que ele gerou que ele já está esperando
para poder dar continuidade aqui no na demonstração. É, deixa eu ver outra coisa? Esse aqui seria o Ulisses. Não é que eu tenho 2 roles definidas,
que seria o code generation, é a linguagem que eu quero que ele use
quando gerar um código que às vezes se você manda pergunta em em português, ele vai
colocar os comentários, os nomes de funções, tudo em português. Eu quero que ele aqui eu estou definido
para ele responder essa geração de código em inglês. E o repositório desse projeto aqui? Aqui ele também está mostrando
uma integração com Pyroscope, não é para criar o Fleming Graph. É. Meu tempozinho. É criou? É. Tempo é assim mesmo. Era mais um. 20 segundinhos se não eu já pulo para o. Ele está buscando basicamente
um problema crítico dentro do da infraestrutura, não é basicamente? Deixa eu ver esse outro, ó. Uma outra coisa interessante é que vocês podem,
durante a interação com o assistente. Que é isso? Não, não é rede necessariamente, né? Ele realmente está
processando obrigado, viu? É. Que que eu estava falando? Ah, está, é, você tem com a
possibilidade de adicionar contexto, não é de acordo com você. Se você tem se você quer
analisar métricas específicas de um data source, você pode. É utilizar. Vou colocar aqui mais clicável. Por exemplo, você tem
uma forma de utilizar? Seria. Assim, você tem esse aqui em cima que você selecione Datas
source que você quiser colocar dentro do seu prompt, né? Inicial tem como adicionar métricas, né? Acho que ali também é
um jeito interessante de mostrar de um data source específico, por exemplo, e isso enriquece, né? Principalmente quanto mais
especialistas você for, isso vai enriquecer mais ainda a saída que ele tiver ali. Aqui ele já terminou, beleza? Está terminando. Se é uma coisa que pode reduzir
também essa prolixidade, não é deixar de falar demais, vai ser mais sucinto. Bacana é, deixa eu ver aqui se ele
fez o que que ele encontrou. Espera aí um pouquinho? Problema crítico,
recomendação prioritário foi serviço desabilitar profiling, que seria desabilitar o profile em produção que ele está considerando
no ambiente de produção. É, enfim. Vou, eu vou tentar aqui fazer um,
cantar um pouquinho. Um. Que ele faça uma interação com um repositório
de projeto que eu tenho configurado lá no rules. Que basicamente faça com que ele crie uma
branch para mim no repositório e coloque o um código de correção, né? Relacionado a esses problemas que
ele identificou na estec aqui. E compartilhe o link dessa branch. Beleza. Oh My God. É um branch repositório. Aí ele vai fazer. Aqui é interessante porque
eu utilizei anteriormente, mas ele te pergunta se você quer criar essa branch,
ele vai te pedir autorização, ele não vai criando ou fazendo ou alterando o código nem nada não, que ele criou a branch
já agora ele vai criar O arquivo que traz a otimização que foi detectada no profile. E aí eles perguntam,
a autorização não é algo que é. É sem autorização não é? Porque eu permitia aceitar tudo aí. Para tentar acelerar,
não é o de um aqui. Agora ele está criando. Aí, ó, está vendo? A gente faz esse tipo de
perguntas para vocês. Eu vou também atualizar tudo. Aqui está? Ao menos sobre essa função, não é esse essa ferramenta,
na verdade, do MCP server e do GitHub? É demonstração, não é já? Vocês sabem, não é? É? Deixa eu ver aqui. Se tem alguma coisa mais interessante
é uma forma de acessar o assistente. Eu acho que é bem interessante
falar sobre isso, né? É, seria por esse ícone aqui. Mas se vocês também podem
acessar via paleta de comandos, não é assistente, você tem como abrir o assistente,
seja a sidebar, via sidebar, então ir para home do assistente na home,
acho que é legal falar também. A gente tem algumas informações aqui, ó. Bem legais, não é? Ou seja, para quem está
começando, por exemplo, aprender mais sobre o que que é o assistente, além do que a
gente está falando aqui hoje? É. E também tem para as áreas
mais recorrentes, não é? É. É essa sessão de atividades recentes
que você teve, no caso, investigações. E também é conversas, não é? Ele está, ele criou, não é? Tá dando tudo certo,
então acho que esse demo vai dar certo, entendeu? É o próximo novo,
acho que não vou ter tempo de mostrar, mas eu vou estar lá no Esc da Experts, aí eu posso mostrar esse
outro demo que é bem legal. É, mas acho que não vai dar tempo. Deixa ele só terminar aí. Perfeito. Outra coisa também que é interessante que
ó ele colocou ali perfeito agora é esse tipo de comportamento. Não é muito afirmativo, não é? É algo legal para colocar
em roles ali para ele. Não ficar concordando o
tempo todo com você, né? Que seja algo mais bem natural,
máximo possível você pedir ele para ser. É questionador,
não é um assistente mais questionador do seu. Nossa, eu não pedi? Mas ele está criando. Deixa eu, deixa eu ver se conseguem ver. Esse essa aqui foi a
branch que ele criou. Ele vai retornar ali. Eu posso mostrar para vocês,
mas essa foi a branch que ele criou. Com um, opa, a correção,
basicamente gente. Espera aí que? Tamo indo, com os commits
que ele fez agora ali, e basicamente as correções que ele fez, né? Não, isso aqui não tem nada a ver,
que é o histórico. Há uma que eu. Perdendo aqui, aqui ó. Esse foi o commit, na verdade. Aqui ó, com a correção. Basicamente, eu pedi ali na demonstração
que ele criasse um arquivo novo, não agisse em cima do arquivo em específico. Que ele encontrou o problema? Mas para mostrar para vocês, beleza? Deixa eu ver se ele retornou aqui,
ó, aqui ele retorna e retornou o link que eu tinha pedido, readme e todo processo de
otimização de acordo com o que eu pedi. É, pode voltar para os slides que
eu só vou encerrar agora, está bom? Tem mais demos, então,
por favor, vão lá. Acredito que em termos de demo,
é bem complicado também abordar tudo, porque vai de casa a casa, que é um
caso bem controlado, não é? Então, bem legal vocês trazerem as
demonstrações para a gente também, que a gente pode testar ali, ao vivo, próximo. Com isso, né? Para fins de informação,
né o Grafana assistant Agora ele é disponível para todos,
então no Grafana Cloud é. O custo dele será basicamente de 20 USD
por usuário ativo mensalmente, porém ele é gratuito para qualquer
tier até janeiro, então a ideia é usar bastante agora, né? O Grafano assistant
investigations a funcionalidade Ela Foi colocada em public preview. Então, ela já é possível
utilizar a pelo Grafana Cloud. E da em breve será disponível
para todos também, como o Grafana Assistant. E como eu disse, né? A nossa visão não parar por aí, né? A ideia é criar uma plataforma
de observabilidade. Agente que é, né,
que realmente ajuda vocês não só a monitorar o ou entender, né? Ali usando o co-pilot, né? Mas prever, né? E agir de forma autônoma é,
é e preventiva. E algumas funcionalidades
que a gente já. Está em desenvolvimento,
está em estudo, em consideração. São essas todas. Aqui é, por exemplo,
a integração com Easy Deck. Não sei se está colocado aqui,
mas com IRM que mais? Com Teams com. Mobile? Enfim, né encontrar. Por exemplo, uma das interessantes aqui é a detecção de pontos
cegos da sua configuração de observabilidade, algo que,
principalmente para quem está começando, é bem comum. Não é deixar algum ponto que. Deveria ter cuidado, segurança e tal. Então acaba que você tem aqui bastante vai ter nesse tipo de ação preventiva. Se a Grafana lança uma nova versão, você vai ter ali a sugestão
de como atualizar, de como andar com o seu Stack,
basicamente. É, realmente está desatualizado. Meus slides aqui é, porém eu ia mostrar para
vocês uma demonstração. Eu posso mostrar também
lá no Esc da Experts, uma demonstração da
integração do Garfield Assistant com o Slack, mas para quem quiser participar
do private preview dele, pode fazer o scan desse QR Code aqui, que tem um formulário que você
pode pedir para participar. E para fechar, não é, é? Eu quero ressaltar que a visão
não é como eu falei ali, já está sendo. Para quem está adotando
de forma recorrente, já está sendo interessante já. E já vê isso nos números,
nos nossos números, basicamente. Mas já ressoa, né? Positivamente aí para
clientes mesmo em produção, como é o caso do. Neil Wilson, que é Diretor de Engenharia
de Software da LexisNexis Risk Solutions, é, ele resumiu bem,
não é fazendo um apanhado que ele está falando aqui,
um dos maiores benefícios que ele viu foi
reduzir a carga cognitiva sobre os engenheiros deles, que a gente falou, né? Isso e o Grafana Assistant me tem ajudado
a chegar à causa raiz mais rápido, sem precisar de conhecimento profundo de
cada parte do sistema que. Para eles, se consideram bem complexo. É para finalizar,
a gente está muito animado, não é em continuar a executar essa visão.

