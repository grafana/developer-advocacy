# L’observabilité unifiée des applications et de l’infrastructure dans Grafana Cloud

Lors de l'ObservabilityCON 2023, nous avons annoncé l'acquisition d'Asserts, qui offre une couche d'intelligence aux données ...

Published on 2024-12-13T16:32:08Z

URL: https://www.youtube.com/watch?v=VPpmIrl5hTc

Transcript: et donc je vais rester avec vous j'ai le plaisir de rester avec vous pour pour la prochaine session euh donc je me suis pas encore présenté je suis Abdelkarim Hadid directeur technique chez grafanaalps pour l'Europe du Sud euh je suis chez grafana depuis 4 ans donc j'ai vu un peu l'évolution de la plateforme et euh et de nos solutions où euh il y a quelques années on était principalement une solution de dashboarding puis ensuite de monitoring avec la gestion des métriques promeétius et des log loky et aujourd'hui on a une plateforme d'observabilité complète avec plusieurs solutions sur étagère et en ayant toutes ces solutions on commencé à avoir d'autres challenges ou d'autres difficultés sur lesquelles on a travaillé avec l'acquisition de ACERT et notamment comment avoir une vue unifiée et et homogène sur l'ensemble de la stack et comment vous aider à résoudre les problèmes plus rapidement donc pour trouver la route cause analysis si vous pouvez juste lancer le le timer comme ça je peux suivre s'il vous plaît merci donc je vous remets le QR code si vous avez des questions et puis on prendra dans la salle si on a un peu de temps et on sera toujours à l'extérieur pour pouvoir répondre à à vos questions donc avant de de parler de troublhoooting de ACERT et vous avez déjà pu voir une petite démo de de cil ce matin on reviendra un peu plus en détail on prendra le temps d'expliquer différents concepts donc je vous propose de revenir en arrière et voir comment un SRE ou un développeur utilise gra cloud autre outil aujourd'hui pour diagnostiquer lorsqu'ils sont en estreinte et un problème donc je suis un sux je suis assez junior je viens de démarrer un nouveau job don donc j'ai rejoint une boîte qui a un site internet pour vendre des télescopes pour pour revenir sur la la démo open télémétrie et donc on est un business international donc on a un service d'astrin 247 et cette semaine je suis à d'astrin 2h du matin je reçois cette alerte euh donc voilà on a un système ào on est plutôt bien organisé donc on se rend compte que il y a des clients qui sont sur le site mais le le site à peen a recherché des produits sur sur le catalogue qu'on a donc il y a une latence qui augmente on a des asso on a un error budget qu'on est en train de consommer très rapidement et heureusement pour moi donc il y a un lien vers un dashboard qui va m'aider pour comprendre ce qui se passe je rappelle he je suis nouveau mais lors de l'enboarding on m'a expliqué que il faut d'abord commencer par la Digital user experience pour comprendre l'impact des pannes sur mes clients est-ce qu'ils arrivent à acheter de produits ou pas donc je vais aller ouvrir real user monitoring je vois effectivement il y a beaucoup d'erreurs euh il y a de la latence qui augmente on peut le voir en bas et puis ça touche plusieurs pages ça touche l'ensemble du site mais notamment euh la le catalogue produits donc c'est en cohérence avec l'alerte que j'ai eu mais aussi checkout donc ça veut dire queil y a des clients qui essayent d'acheter des choses et qui n'y arrivent pas à cause de ce problème donc il y a de l'argent en jeu il faut que je trouve une solution rapidement sinon le CTO c'est lui qui va m'appeler à 3h du matin et j'ai intérêt à trouver la solution donc ce qui est intéressant dans rom c'est que je peux rentrer dans les détails pour comprendre c'est quoi la panne donc là je me rends compte que même si on voit les problèmes au niveau du front le c'est juste un symptôme le vrai problème c'est au niveau des IPI et notamment les IPI product voilà donc il faut que je comprenne ce qui se passe je vois il y a des erreurs 500 je regarde plusieurs erreur c'est plus ou moins la même chose donc c'est cohérent maintenant il faut que je prenne un peu de recul pour essayer de trouver quelle est la cause du problème donc je rappelle he je suis assez nouveau donc je connais pas vraiment l'architecture je sais qu'on fait du microservice on a une trentaine de services trois bases de données des caches des CDN je comprends toujours pourquoi on a toute cette complexité alors que c'est un simple site web mais bon c'est comme ça qu'on qu'on fait du dev aujourd'hui euh donc on a un product catalogue qui appelle un service de recommandation donc on a des featur flag qu'on peut activer ou pas et effectivement le frontend fait à le product catalogue donc ça ça explique ça reste toujours cohérent mais je sais toujours pas par par où commencer donc j'espère qu'on a des bons dashboard on a quelques centaines de dashboard sur notre instance grafana donc je vais trouver quelque chose qui va m'aider euh on a mieux même on a application observability donc c'est la même manière avec laquelle on va voir toutes les données Open téléméri rate error duration donc je peux me débrouiller donc je regarde pour le product catalog blog ça a l'air cohérent donc il y a des erreurs je regarde un peu les services qui viennent en dessous notamment le service de recommandation il y a rien de de particulier donc ça a l'air de bien fonctionner et enfin je regarde aussi le le dernier dashboard qui est le le checkout future flag donc qui semble aussi être liié à cette à cette panne toujours rien rien rien d'intéressant alors avant de rejoindre la boîte j'étais j'ai fait un nom de de SRE dans une autre boîte en tant qu'altern donc je connais un peu les pannes et je sais que dans la plupart des cas ça commence par la base de données donc je vais me dire je vais aller voir notre base de données j'ai vu sur le schéma qu'on a un post gré d'accord euh par contre je vois je vois rien d'intéressant donc il y a tout a à l'air normal et surtout on a trois instances je sais même pas c'est quelle instance qui qui euh que je dois regarder plus il a 3h et15 je je suis encore pas bien réveillé donc voilà c'est un peu la situation dans laquelle pas mal d'entre vous se retrouvent peuvent se retrouver euh lorsque on est en instrain parce que on a toutes les données qu'il faut on a collecté les maétriques on a collecté les logs les traces c'est très bien on a une plateforme scalable on a plusieurs dashbards qui nous permettent de avoir une vision claire sur les différentes composants les applications ainsi de suite mais en fait lorsqu'il y a un problème c'est très difficile de savoir par où commencer et comment partir des symptômes vers les causes un autre problème aussi c'est que souvent un problème il vient pas seul donc on a tout cet effet boule de neige ça ça neige donc c'est c'est c'est assez cohérent euh donc on a un problème dans l'Infra qui se retrouve sur la le service et puis on peut on peut le voir au niveau du front-end et donc on se retrouve avec plein d'alertes plein de problèmes et c'est difficile de comprendre par par où commencer et donc pour cette raison en particulier qu'on a décidé réfléchi euh d'acquérir l'entreprise àert donc c'est un produit qu'on a intégré à grafana cloud donc depuis 1 an on a fait tout l'exercice de le mettre dans grafana cloud de l'intégrer dans les différentes solutions pour que ça soit pas encore un autre outil qu'on va utiliser mais que ça apporte une une vue uniforme et et homogène pour vous permettre de de faire une analyse avec du contexte automatisé aussi donc il y a pas mal de check d'algorithmes qui permettent de faire des analyses pour nous et qui nous ressort un peu des signaux intéressants depuis la masse de données qu'on a collecté pour on espère accélérer la résolution à travers la détection de de la rou de cause du problème maintenant je vais vous expliquer un peu comment ça fonctionne et puis je passerai vers une démo euh sur un cas concret donc ce qu'il faut savoir c'est que ACERT se base sur les données d'observabilité Open Source donc prométhus et Open télémétri principalement lorsque vous envoyez des métriques prometthus ver graph an cloud ce qu'on va faire c'est qu'on va analyser d'abord tous les labels qui va qui vont nous permettre de d'identifier pas mal de choses donc par exemple on peut regarder euh CUB node info CUB pod info pour savoir que vous avez C nud cuberntis C pod qui tourn on va regarder toutes les métriques qui nous viennent du du node exporteur pour analyser CPU RAM mais aussi de comprendre quels sont les VM quels sont les serveurs qui sont déployés dans votre de votre infra euh on va également regarder tout ce qui est service mesh et trace pour trouver les liens entre toutes ces ces ces individus ces entités et pourquoi pas euh si vous avez des applications aussi qui sont instrumentées par prometus ou bien par open télémetry on peut également détecter les services et les relations entre eux donc tout ça pourquoi on le fait pour créer ce qu'on appelle un enti graphe donc c'est un graphe dynamique temps réel et versionné de l'ensemble des objets qui qui interagissent dans votre infrastructure et application et donc là ce qu'on voit c'est principalement des services mais il y a aussi des bases de données qu'on peut voir en périphérie et donc vous vous rappelez de la page confluente qu'on a déf même si on arrive à la maintenir une fois par mois une fois tous les de mois il se peut que les développeurs ont changé quelque chose et ils n'ont pas encore partager l'information avec nous donc moi qui suis à strin j'ai peut-être une information qui n'est pas à jour donc avec ce graphe j'ai la vision temps réel de mon système et s'il y a des changements je peux aussi le voir c'est y a un service qui a été déployé hier soir bah il sera directement ici donc c'est déjà très bien ça me donne une vue mise à jour mais qu'est-ce que je peux faire avec ça pour accélérer la la la recherche de de route ca donc ce qu'on va faire c'est à partir de l'ensemble des informations on va extraire des Golden signals par rapport à la latence le nombre d'erreurs la saturation ainsi de suite selon à ce que c'est un composant infra ou applicatif et à partir de ça on va appliquer le modèle safe donc c'est un ensemble de règles d'algorithme qui tourne en permanence qui analyse vos données et qui vont identifier des signaux faibles ou fort qui vous permettent de dire ok sur l'ensemble des données je vais commencer peut-être par à regarder ici donc on va voir la saturation est-ce qu'il y a des services qui reçoivent plus de requêtes que d'habitude ça peut être une base de données et donc peut-être que mon code n'est pas bien conçu ou peut-être qu'on a plein d'utilisateurs qui arrivent sur le site qui déclench quelque chose on va voir tout ce qui est anomalie donc on calcul des baselines donc on regarde pour chaque service pour chaque métrique quelle est la norme par jour par semaine par mois en en prenant en considération la saisonnalité et puis on va vous mettre en évidence tout le comportement qui sort de l'ordinaire par rapport à l' l'apprentissage qu'on a fait on va regarder les amend les amend c'est tout ce qui est changement de configuration déploiement d'une nouvelle version parce que c'est souvent là où on essaie de déployer quelque chose de nouveau on n pas bien testé tout et donc ça déclenche le problème et puis ça arrive sur des erreurs euh qui peuvent être temporaires ou bien des composants qui s'arrête de fonctionner complètement et donc on a envie de de voir donc voilà euh pour revenir un peu sur le schéma qu'on a vu au début donc j'ai mon front end j'ai mon product catalog qui parle avec le service de recommandation et j'ai envie de débuger donc là on va passer en mode démo donc s'il vous plaît si vous pouvez changer changer l'écran Mo j'étais juste en veille c'était sur le bon adaptateur c'ester parfait donc là on a la vue d'acert qui fait partie de grafana Cloud donc par défaut on peut voir l'ensemble des services et de leur connexion qui représente en fait tout mon parc infrastructure et applicatif donc là on montre principalement des services mais on peut montrer n'importe quoi donc par exemple on peut voir les différents euh nœud estce que je suis connecté ouais ouais recharger hop donc là je peux voir les les déploiements les Dimet les datas sources si vous avez par exemple des brokers Kafka vous pouvez voir tout les topies et les relations qui consomment depuis cas donc ce qu'il faut garder en tête c'est que c'est un modèle par défaut euh qui est très orienté service cuberntis mais qui est extensible en configuration on n pas besoin de redéployer ou de recoder quelque chose de notre côté ou de votre côté pour rajouter des composants des entités par exemple vous voulez représenter un data center ben on a la possibilité de le faire et de l'afficher sur le graphe euh donc là ce qui m'intéresse moi c'est le product catalog c'est ce qui a causer le problème donc on va se brancher sur ce service et tous les services qui sont connectés donc ça me permet de me focaliser sur l'objet d'intérêt en cachant l'ensemble du reste et donc là ce graphhe il est versionné par le temps donc là je regarde sur la dernière heure mais je peux venir sur la 24h parce que oui depuis on a on a réglé le problème autrement je seraai pas là en train de présenter et donc si je reviens sur 24 he on peut voir apparaître des codes couleur qui vont montrer tous les problèmes qu'on a identifié donc ça peut être des anomalies ça peut être des changements de configur furtion par exemple ici on voit que le feuture flag a changé d'état et ainsi de suite donc là si les services me permett de d'avoir une vision complète c'est suffisant sinon je peux aussi aller chercher des détails plus pour comprendre de quel de quel service il s'agit de quelle base de données quelle version ainsi de suite et donc supposons que je veux voir sur quel pod le product log service est déployé ou le check en fait on a la possibilité de le faire en cliquant et en rajoutant le pod qui est lié à ça j'ai envie de voir sur quel nœud il est déployé pour voir ce qu'il y a un problème d'infra je peux également étendre mon mon cluster et donc on peut comme ça rentrer rajouter toutes les composantes qui me permettent de comprendre ce qui se passe euh je peux le faire là élément par élément mais je peux également venir et enrichir tout le graphe en disant pour ma vue métier ce que j'ai envie d'avoir comme information pour démarrer la résolution c'est que chaque service je veux voir le pod qui est associé et pour chaque pod je veux voir le nœud qui associe donc là on commence à avoir beaucoup d'informations peut-être c'est pas c'est pas ce qu'il faut faire euh mais sinon on peut également venir et dire mais je veux me focaliser sûrement sur les services qui sont liés à un problème et donc là je reviens sur une vue un peu plus centré résolution avec l'ensemble des composantes qui me permettent de savoir qu'est-ce qui se passe passe comment ça se cascade et comment les différents systèmes fonctionnent donc ça c'est plutôt une analyse un peu un peu manuelle qui me permet de comprendre ce qui se passe maintenant ce que je veux ce que je veux savoir c'est j'ai ce product catalogue il a l'air d'être la source du problème donc ce que je vais faire je vais passer en mode troubl shooting avec le Workbench donc là ce que je fais je vais avoir une vue temporelle sur l'ensemble des problèmes qu'on a identifié et ce que je vais faire c'est je vais cliquer ici pour ramener tous les services qui sont liés à ce prodect catalogue pour lesquels on a vu un problème lors des 24 dernières heures et donc là j'ai l'ensemble de ce que assert a identifié automatiquement encore une fois grâce au modèle safe qui qui en train d'être lancé et donc je vois que j'ai une concentration de problèmes vers minuit hier donc ce que je vais faire je vais sélectionner ici pour focaliser sur cette euh zone tempoil donc là par défaut les données sont triées par score donc ici le product catalogue c'est le service où on voit le plus de problèmes donc si je regarde ici il y a des erreurs il y a des failur il y a il y a des anomalies qui ont été détectées mais ce qu'on peut voir aussi c'est peut-être organiser les événements partant pour voir quelle est la première erreur qu'on a commencé à voir et comment elle s'est répercuté sur les autres services et donc pour avoir une vue un peu plus détaillée je vais je vais revenir sur ça Paris je vais commencer à voir des informations intéressantes donc d'abord je vois qu'on a activé un feature flag d'accord par la suite on a commencé à avoir des problèmes sur notre base postgé avec beaucoup de connexion et de la latence ensuite le product catalogue service a commencé à avoir des problèmes avec des pods qui crachent en continue avec de la latence sur des API comme list product et get product et enfin ces erreurs commencent à émerger vers le front et donc impacter mes clients et c'est ce que j'aimerais continuer à analyser pour pour voir ce qui se passe donc si je regarde le feature flag ce qui est intéressant c'est que on a un feature flag qui s'appelle re from po Grey qui passe de 0 à 1 donc il s'agit de quelque chose qu'on a activé dans la plateforme et juste après on a commencé à avir ces problèmes là je vois que la première la première entité qui a commencé à à subir c'est la base de données donc je regarde ici on a effectivement une baseline qu'on a qu'on a défini mais on voit qu'on sort de cette baseline là et notamment par rapport au aux connexions donc je vois qu'il y a un pic de connexion à chaque fois et on dépasse les seuils si je veux voir les KPI de la base de données elle-même je ne suis pas obligé de me connecter sur un autre dashboard ou une autre solution j'ai toutes j'ai tous les dashboards et toutes les données qui sont dans votre écosystème gfana qui sont intégrés directement dans assert et donc là j'ai mon dashboard pour gré je vois effectivement qu'il y a des pics de connexion mais rien de de surprenant j'ai le nombre de connexion Activ pareil je vois pas de problème et comme la base de données elle est déployée sur kuberntis bah je peux aller aussi sur la vue kuberntis pour voir à ce que il y a un problème d'infra donc là j'ai le workload CPU mémoire je vois que ça ça oscile c'est normal on a beaucoup plus de charg mais j'ai pas défini de seuil donc j'ai pas de out of memory qui explique le redémarrage de certains services donc voilà je je trouve rien d'intéressant je vais descendre un peu d'un niveau pour euh pour voir le le service pod qui qui redémarre et donc effectivement on a quelques quelques problèmes encore une fois on peut ramener les autres données les autres dashboards qu'on a par rapport à ce service- là et notamment application observability donc on peut voir la vue un peu APM donc c'est cohérent je vois pas mal d'erreurs qui sont déclenchées euh et une latence qui augmente sur les 10 dernières minutes et donc j'ai également toutes les traces les logs qui sont récupérés donc si je regarde les logs effectivement il y a quelque chose d'intéressant donc on voit que il y a sql.go qui euh qui a été utilisé et donc on a un une segmentation violation donc peut-être un un nul pointeur et à partir de ça on va avoir un problème qui se déclenche au niveau du service ce qui explique en fait tous les redémarrages euh est-ce qu'on a eu un problème avec la mémoire pas vraiment je vois que mon service utilise très peu donc c'est bien efficace côté consommation de mémoire j'ai pas atteint la limite que j'ai défini pour ce service donc c'est vraiment un problème de code dans l'utilisation de post Gray qu'on vient d'activer à travers le feature flag donc je vais attendre le retour du développeur ce qu'on fait c'est que on va rollback notre feature flag ici donc on revient on le désactive et puis ça nous permet de revenir dans un état nominal sans problème voilà à peu près un exemple concret sur comment vous pouvez utiliser ACERT qui vous permet de ramener l'ensemble des données les dashboards dans un unul environnement et puis vous faire des analyses automatiques sur quelles sont peut-être les causes de ce problème et puis les analyser soit sur le temps soit sur la gravité en espérant qu'on va trouver la roue de cause en tout cas on vous facilite l'accès à la route cause donc si on peut revenir sur les slides donc voici le schéma qu'on a eu tout à l'heure donc àert comme je vous le dis nous a permis de découvrir automatiquement l'ensemble des objets comment elles sont liées et puis faire ces analyses là automatiquement pour nous et puis remonter les les informations qui sont intéressantes et les signaux qui peuvent nous aider dans notre notre approche voilà maintenant cert en soit c'est un produit donc c'était toute une plateforme une entreprise autour de ce service qui permettait d'offrir ce type de fonctionnalité sur n'importe quel backend qui peut stocker du proméus de open télémétrie ainsi de suite ce qu'on a fait depuis un an c'est qu'on l'a intégré à l'intérieur de la STAC donc ça devient un produit donc si on voit dans le menu graphana cloud c'est un produit en tant que tel mais ce qui est intéressant aussi c'est de pouvoir ramener les Insight que ACERT va produire ou déclencher et les mettre à disposition un peu partout dans la plateforme donc si vous êtes dans la vue APM vous avez envie peut-être de savoir que sur les services que vous êes en train de voir on a détecté ces anomalies ces latensces et cette nouvelle version qui a été déployée donc on commence à récupérer un peu l'intelligence qui sort de cet outil la mettre un peu partout sur l'application observability sur kuberntis sur du Front End et un peu partout plus tard dans la plateforme donc ce que je vous ai montré tout à l'heure c'était comment on peut intégrer application et cuberntis monitoring à l'intérieur de ACERT pour pas bouger et sortir et perdre le contexte mais on est en train aussi de faire l'inverse c'est-à-dire extraire les informations et puis les afficher sur ces solutions et donc là on a application kuberntis eto et le prochain sur la ligne ça sera du frontend souvent lorsque je présente àert on pose des questions sur la scalabilité et sur est-ce que ça va vraiment fonctionner sur mes données euh en dehors d'un environnement de démo et donc comme on l'a vu ce matin avant de rendre ce service ga on a fait l'exercice de déployant production chez des vrais clients avec des déploiements assez larges euh donc on a eu à New York récemment donc Black Rock qui nous ont fait un retour sur sur leur usage donc ce qui est intéressant c'est que euh c'est le même constat un peu partout on a toutes les données pour faire de l'analyse mais àert va nous permettre d'aller plus vite pour savoir quelle est la donnée intéressante à analyser à un moment donné et comprendre la route C donc là c'était leur un peu workflow d'analyse donc il reçoi des trades donc c'est une c'est un service financier ils ont un certain nombre d'étapes à faire et à réaliser et donc avec ACERT ils ont pu supprimer de trois étapes de leur process et accélérer les étapes qui étaient déjà présentes donc euh pour résumé à CER permet d'abord d'accélérer la résolution pour en trouvant la la route cause plus rapidement et donc si vous avez un service qui est exposé à vos clients réduire l'impact financier ou sur l'image de marque ou sur la stabilité du service améliorer la productivité des développeurs qui peuvent se concentrer sur le développement et lorsqu'il y a des problèmes on peut rapidement trouver et résoudre C ces derniers et enfin euh comme on a vu il y a pas mal de travail qui est fait pour les gens directement au lieu de construire les dashboards de les intégrer de les mettre à jour c'est déjà fait pour vous c'est automatique donc ça vous permet de réduire euh voilà toute la partie automatisation et et le travail que vous faites autour de ça maintenant si vous posez la question j'espère c'est intéressant pour vous et vous dites comment je peux démarrer donc il y a un certain nombre de contraintes en tout cas sur le court terme qu'il faut garder en tête même si à cert elle peut fonctionner sur n'importe quel de déploiement que ça soit des VM des serveurs assez traditionnels pour la première version on a besoin que l'infrastructure utilisée soit kuberntis pourquoi parce que c'est le plus simple on connaît le modèle on a pas mal d'informations cohérentes qui nous remontent par rapport au label par rapport au aux API de kuberntis donc on on arrive à construire out of the box tout le modèle et on est en train de travailler sur le support aussi de tout ce qui est AWS Amazon Azure d'un point de vue application on s'attend à ce que les données arrivent en Open télémétrie donc application observability sera nécessaire pour la partie APM et puis on intégrera d'autres d'autres framework d'instrumentation plus tard et euh dernier point c'est disponible pour les clients en advanced donc si vous avez un compte grafana cloud pro en selfsve vous mettez votre carte bleue et vous commencez à utiliser ce n'est pas encore disponible ça le sera en début d'année prochaine si vous avez des questions par rapport à ça n'hésitez pas à venir nous voir un peu plus tard
