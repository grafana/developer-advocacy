# AI/ML dans Grafana Cloud : économiser du travail, du temps et de l’argent

Grâce à des fonctionnalités telles que Sift, Asserts et Adaptive Metrics, l'AI/ML aide les entreprises à réduire leur charge de travail, ...

Published on 2024-12-13T16:30:15Z

URL: https://www.youtube.com/watch?v=pJfljMEB_ZY

Transcript: alors on mappelle donc on va parler de eaml aujourd'hui je vais me présenter donc cy je crois que je me suis déjà présenté donc je trava dans l'équipe de je je suis engering manager de l'équipe deamn de intelligence artificielle et machine learningol à toi d' je pense oua si vous avez des questions oui on scan on répondra la fin pas trop de questions parce que je pense qu'il y en a qui ont faim allez c'est parti euh du coup les écrans marchent pas les deux sont éteints si on peut mais c'est pas on va quand même commencer euh donc l'automatisation vise à libérer le potentiel humain euh si on regarde un petit peu dans l'histoire ce qui s'est déjà passé grâce aux technologies il y a très longtemps en terme de de newspaper ou ou de papier avant c'était vraiment des des gens qui tapaient à la main et qui travaillait pour créer ces papiers là puis avec l'évolution quelqu'un a inventé l'imprimante c'est une vieille imprimante c'est pas l'imprimante qu'on a aujourd'hui et puis finalement on est arrivé à un point où bah la technologie a complètement remplacé tout ça et puis maintenant on est capable de déployer à travers le monde une news et puis c'est consommable par tout le monde et ça vise un petit peu à libérer le potentiel humain à force de enfin à la place de euh devoir faire des tâches répétitives euh en fait on peut focuser un petit peu plus sur les tâches les plus plus importantes j'imagine que taper à la main une news pour tout le monde la même chose c'est pas le fun en tout cas c'est ce que je pense que ce Mo là n'a pas eu n'a pas eu beaucoup de fun euh lesl c'est déjà pas mal on en parle beaucoup en ce moment on voit que il y a déjà pas mal de d'industries qui l'ont adopté on pense à tout ce qui est santé ou on donne une image d'un scanner par exemple à une a elle est capable de déjà donner un prix diagnostique euh d'autres d'autres cas d'utilisation dans dans beaucoup d'industries qui sont très intéressants où où on ou parfois faire une analyse humaine peut-être un petit peu plus un petit peu compliquée et avoir du préprocessing par une intelligence artificielle est relativement intéressant pas oublier que c'est toujours préprocessing donc il y a toujours quand même côté humain derrière pour valider le le le résultat nous ce qu'on pense à graphanalab c'est que c'est c'est un peu la même chose qu'on pense que ce qui ce qui va se passer avec eaml c'est que ça va permettre en fait à tout le monde de devenir en fait un expert en observabilité sans nécessairement avoir autant d'expérience que un vrai expert ça va vous aider à résoudre plus rapidement et pas spécialement en fait trouver et résoudre les problèmes pour vous mais plutôt vous aider euh et donc je vais passer la parole à Rob qui va montrer un petit peu comment com ça se comment ça se décline dans grafana toutes ces petites fonctionnalités qu'on a ajouté dans grafana qui vous aide à aller plus vite merci donc nous voulons vous fournir des outils pour réduire l'effort et de faciliter vos tâches quotidiennes une grande partie de temps passé dans grin est consacré au dépanage donc ce n'est pas une tâche simple c'est pas facile en général vous recherchez des signaux dans les données de télémétrie bien sûr ce qui peut poser les défis les vrais défis donc je suis ici pour vous présenter quelques fonctionnalités de iaml nouvelle et existant et que que vous aiderant à identifier et à résoudre les problèmes plus rapidement ces fonctionnalités se trouvent dans le nouvel appli explore et dans sift donc explore c'est c'est Open Source sift c'est que dans cloud mais sift c'est dans c'est ça fait partie des des fonctionnalités de ML euh les deux sont entièrement gratuites oui gratuit ENF cloud certain en open source et passons maintenant en revue des différents défis auxquels nous faisons face avec notre cat golden signals des signaux clés si je ah oui désolé le premier défi concerne des logs donc nos logs sont souvent bruillants et verbeux donc scroll des pas de Lig des logs similaires pour trouver un problème spécifique c'est comme chercher une aiguille dans une de fr voici un exemple des logs ici à première vue vous pouvez voir oui ok désolé donc à premère vous vu vous pouvez voir que la plupart des lignes se répètent avec TR ou quatre motifs distincts il serait donc très utile de regrouper ces lignes et de n'afficher chaque motif qu'une seule fois au lieu de voir en boucle cela évite des répétitions c'est bon c'est bien c'est pour cela que nous avons introduit les log patterns de log pour regrouper les logs similaires ainsi il suffit de regarder chaque motif de log une seule fois cela nous permet également de suivre l'évolution des motifs de log au fil du temps pour répérer les log le plus important en cas de problème cette fonctionnalité est actuellement disponible en deux endroitsabord une slide une slide enetard bien enc ok oui bien je CIS ok tout d'abord dans explore logs donc nous utilisons les log patterns pour vous aider à trouver rapidement des logs particuliers que vous rechercher nous présentons tous les motifs de log dans une plage de temps donné afin que vous puissiez filtrer rapidement les logs dont vous avez besoin explog disponible en open source comme j'ai dit deuxèmeir c'est dans sift et imaginons que vous souhaitez enquêter un problème mais que vous ne sachiez pas encore quoi chercher ou même pas où où commencer ça c'est la raison d'être des sift donc si c'est quelque chose com on démarrer en plusieurs endroits d'un d'un dashboard d'une d'une alerte plusieurs endoit une fois que c'est démarré ça fait la recherche un peu pour vous étant donné un contexte restreint comme ça sur laquelle se concentrer site exécute une enquête automatisée et ciblée pour vous faire gagner du temps parmi les autres vérification effectué par sift il examinera également les logs mettant en avant les motifs d'reur potentiellement intéressant nous faisons cela en examinant les motifs log erreur au cours des dernières 24 heures et en vous montrant ce qui présentent une augmentation significative de volume donc tout le monde a des erreurs qui sont toujours là dans les logs l'important c'est qu'est-ce qui a augmenté c'est quoi les signaux qui sont changés ainsi sift expl l sont là pour vous aider à identifier plus facilement les logs problématiques pass passons au défi suivant c'est prendre des time series donc nous avons tous été confrontés à des à des time series où nous nous demandons et maintenant quoi donc pour comprendre les time series nous devons généralement répondre à une des deux questions cette série est-elle anormale par rapport à des serériies similaire ou quel est un bon seuil pour des valeurs anormales dans une série une série une parmi les les autres similaires il peut-être difficile de tirer des conclusions simplement en examinant les time series ell-même et même si vous détectez un motif il n'est pas toujours évident de décider si cela est réellement important c'est ici que les fonctionnalités de Dynamic alerting peuvent être utiles pour vous aider à répérer les anomalies au sein de time series ell comprenent des prévisions la prévision et la détection d'anomalie vous pouvez les trouver dans la série la section machine learning sous l'onglet alert et répondre à la première question ma série Estelle anormale par rapport à des séries similaires outl detection met en évidence les séries qui se comporte différemment au sein de groupe de séries similair par exemple elle vous aidera à identifier quand une instance de votre cluster utilise de manière significative plus de CPU que les autres la deuxième question était quel est une bon seuil le forcasting aide à répondre en anticipant les des plages de valeur plausibles pour chaque série en tenant compte de la saisonalité et des effets pour jours fériers des jours fériers ces plages peuvent alors servir de seuil dynamique pour les alertes bien que cette fonctionnalité existe depuis quelques années mais nous continuons à l'améliorer récemment nous avons créé une nouvelle interface beaucoup plus simple pour configurer les forecast avec un retour instantané lors des modifications des paramètres nous utilisons déjà cette nouvelle interface en interne et euh j'ai démontré là-bas aussi à le à le Ases experts bootth aussi euh et d'ailleurs elle sera bientôt en ligne pour vous vous aussi compter de TR semaines c'est presque là euh passons au 3ème défi la recherche des trace spans les segments de traces les traces vous permettent de suivre une requête à mesure qu'elle parcourt les différents services de votre stack donc chaque segment dans une trace représente une opération et fournit des informations comme la durée les erreurs et les à donné les traces offrent une excellente visibilité sur vos applications les meilleures traces sont celles qui capturent des nombreux segments mais lorsqu'elle devient très profonde il devient difficile de trouver les segments pertinentes comme po logs que nous avons vu précédemment nous voulons vous aider à trouver rapidement les spans clés sans avoir à sans avoir à parcourir tous les traces nous avons activer siift pour regrouper et suivre les segments spans d'intérêt par exemple les spans à for latence les segments d'erreur et ceera ensuite sift met en évidence tout segment particulier dans le comportement change cela se fait en comparant comparant les segments d'intérêt pendant la période de mastigation avec ce des dernières 24 heures c'est comme avectigation des logs les segment long et les segments d'erreur sont encore en dévelement mais seront disponibles prochainement et enfin notre 4è défi comprendre les profils les profil mesur l'tilis des ressources d'une application au fil du temps comme le CPU la mémoire et cetera nous visualisons les profils avec des flame graphs qui montrent des barres empilé hiérarchiquement représentant des appels de fonction et le consommation des ressources les les fl sont très utiles mais c'est beaucoup d'information dans un petit espace sont des visualisation qui nous ne voyons pas aussi souvent et nous sommes pas tous des experts donc nous avons intégré le flame graph explainer dans explore profiles c'est aussi open source pour vous aider à bien démarrer avec les FLS cet outil met en évidence les Goul destranglement et root causes et propose des recommandations des correctifs le flame explainer commence par traiter les profil pour ne conserver que les valeurs textuelles importantes il les transmet ensuite à un LLM que vous pouvez configurer lequel qui analyse les informations et fourn des insights et des recommandations voici les défis que nous avons aborder pour obtenir des insights à partir des données de télémétrie brute et comment nos fonctionnalités de iaml peuvent nous y aider mais nous nous sommes encore plus enthousiastes à l'idée de développer de nouvelles fonctionnalités basées sur les insights que vous venez de voir chaque fois que nous recevons un alerte nous soupçonnons qu'il y a un problème grafana propose de nombreux utils pour vous aider à identifier que ne va pas mais à mesure que la complexité de votre système augmente la quantité de signaux augmente également et bien sûr le bruit aussi donc pouvons-nous faire mieux grâce au ml je vais maintenant vous donner un aperçu de ce sur quoi nous travaillons et testons en interne nous appelons cela service level explanations c'est SLE un peu comme les SLO les SLI dans la même catégorie on cherche toujours les explications donc nous allons voir un scénario ou un alerte se déclenche et comment utiliser les service level explanations pour déboger c'est démarré ou pas oui ok ça roule donc ici en pass de lerte les prédictions de ML rencontrent des problèmes ce qui déclenche une alerte donc notre modèle est immédiatement activé et commence à analyser tous les signaux d'observabilité pour le service de ml et C dépendance sur la page ouiok donc sur la base de service level expation au moment où nous commençons l'investigation notre système a déjà mis en évidence les dépendances présentant des problèmes potentiels ainsi que leur signaux pertinente le graphe des dépendances à service de service s'affiche est une note de 0 à 1 est attribué à chaque service représentant la probabilité de contribution au problème actuel c'est table en bas de page qui on vient de voir oui ok dans ce cas il a signale il a signalé redis et le salary workers qui sont des dépendances internes ainsi que le Off API et gcom qui sont des dépendances externes en amont donc les matriques principales qui indiquent possiblement des problèmes pour chaque service sont mise en avant ici on peut cliquer sur le service pour sauter à explore logs c'est link aussi on peut cliquer sur une matrique pour voir le requête de time series regardez les logs pour le worker salary ici ok donc on observe une augmentation des log d'erreur on peut filtrer pour les log d'erreur les workers ont des problèmes pour se connecter à Ris si on retour les pour ris r on peut voir c'est récment arrêté en vérifiant les mriques principales pour ris nous voyons que la mtrique a complètement cessé d' mettre donc ici en quelques secondes nous avons pu isoler la cause le cause et nos prédictions sans avoir besoin de requête ni de recherche approfondie le modèle a pu indiquer immédiatement où nous devions regarder actuellement nous affichons uniquement le GRF de service et et les signaux de matrique mais nous prévoyons d'éteindre cela pour inclure tous les autres signaux disponibles nous observons des résultats prometteurs en interne avec cette fonctionnalité et nous espérons la rendre disponible sur cloud dans un avenir proche dernier sujet c'est changé oui dernier sujet avant de céder à la parole à cile l'obsabilité de Ia donc peut-être que vous devez surveiller vos services supportés par des LM ou des ml des autres modèles où vous entraîz des modèles ml et dev réagir rapidement en cas d'échec dans l'entraînement notre stratégie évolue ici donc si vous voulez scanner le code QR si vous êtes dans ce endroit scanner le code QR pour rester en connecté avec nous et on va vous dire les choses quand il arrive ok merci Rob alr donc euh dernière partie après on mange euh eaml pour une observabilité moins chère euh donc on en a parlé ce matin un petit peu de adaptive matric je repasse juste une petite slide dessus donc l'adoption est vraiment intéressante on a 2000 clients qui utilisent adaptive matric euh de nos jours euh et on a vraiment réussi à à euh euh al leors euh permettre de sauvegarder plus de d'argent je suis désolé pour le le français j'ai un petit peu du mal avec le français en ce moment euh donc en tout je disais ce matin c'est à peu près 10 millions euh de de dollars que on a refusé et qui leur permet en fait d'investir dans d'autres produits qui peut qui peuvent être plus intéressants alors je sais que c'est pas spécialement quelque chose que notre équipe de sale est spécialement contente avec mais c'est une stratégie qui nous tient à cœur parce que on considère que ça ça a pas pas de valeur de de de sauvegarder des métriques vous vous n'aurez jamais besoin euh la réduction va de 20 à 50 % dépendant un petit peu votre votre déploiement euh ça marche tellement bien que nous à graphanalabs on est commencer à passer en auto en autopilot où les recommandations en fait sont appliquées automatiquement et désppliquées automatiquement alors ce qu'on a aussi c'est qu'on a quand même un service dans lequel on peut dire qu' ne touche pas à ces métriques là si jamais on veut influencer un petit peu les recommandations euh et si c'est quelque chose qui vous intéresse et que vous utilisez adaptive metric vous pouvez avec le QR code ici vous pouvez essayer ça vous-même en fait c'est une gitub action qui vous permet d'appliquer automatiquement les recommandations donc n'hésitez pas encore une fois vous avez toujours des Guard r ça vous permet un petit peu de de choisir quelle métrique sur lesquell métriques ne sont pas influencé par le par les recommandations alors je vais passer un un petit peu plus de temps sur adaptive log qui est plus récent qui est plus intéressant et puis j'ai envie de j'ai un petit peu envie de de vous montrer comment ça marche c'est c'est un petit peu un projet qu'on est on est assez fier de d'avoir lancé récemment euh donc euh juste à l'interne comment ça se passe chez nous on adore utiliser no propres produits euh et on a commencé en fait avec adaptive log un volume on a été un petit peu on voulait euh faire attention de pas perdre trop de log parce qu'en fait c'est tous les logs de de tous nos clard à travers le monde on a commencé avec 10 % ensuite on est monté à peu près à 50 % de de de de log qu'on supprimé puis finalement on est resté vers les à peu près 40 % donc chez nous en fait on a réussi à réduire notre consommation de log de à peu près 40 %. alors comment ça marche euh on va regarder un petit peu contrairement à adaptive matrix c'est un petit peu différent pour les logs parce que comme vous le savez euh les logs on peut pas vraiment les agréger donc on va plutôt les les supprimer ou ne pas les ingérer directement et ça marche avec du machine learning et euh c'est grâce à ce machine learning qu'on peut appliquer des recommandations à grand échelle donc au niveau de l'ingestion des logs ce qu'on fait c'est qu'en fait on intersob tous les logs que l'on reçoit et on va essayer de créer des patterns donc on a un nouveau service auquel on envoie tous les logs qu'on reçoit on va créer des patterns c'est un peu les mêmes patterns que je vous ai montré ce qu'on a vu dans explore logs ou dans sift et ces patterns là on va essayer de compter un petit peu sur une quinzaine de jours à peu près quel est le volume donc on sauvegarde ça dans object storage on adore leob storage c'est le moins cher et ça ressemble à peu près à ça donc là on a quelques quelques exemples de log et puis on voit que la première on peut dire que imaginons que ce soit en Tab tu 100 ab de ce log là à travers 25 clusters dans le monde par exemple ensuite au niveau de vos requête sur le readpff ce qu'on va faire c'est que on va regarder tous les logs qui correspondent à ces patterns et qui vous sont retournés par toutes les requêtes donc toutes les requêes ça inclut aussi tout ce qui est alerting rolling dashboard tout tout ce que vous avez tout ce qui fait des requêtes en fait vers loky va être intercepté regarde un petit peu quels logs sont retournés mais pas filtré si vous avez filtré un log on considère qu'il est pas intéressant pour vous ah et donc ensuite ça ressemble à ça euh donc on voit par exemple que sur la première ligne on le on on requettete plus ce log là que en fait on l'ingère donc il est probablement plus intéressant et grâce à ces deux nombres on va en au final euh faire des recommandations de drop rate donc de de de suppression on en fait on les ingère même pas c'est au moment où on les reçoit on va décider de les les de les mettre à la poubelle donc on voit par exemple que le le le der la dernière ligne est à peu près intéressante la la moitié du temps on fait une requête donc on va proposer en fait de dropper la moitié ok donc ça c'est ce que je viens expliquer ça aussi démo donc là ça on a une petite démo pour montrer à quoi ressemble un peu l'interface de adaptive log pour pour vous montrer à quoi ressemble un petit peu les les recommandation donc on va la lancer je pense qu'il plus ouais c'est parti donc vous allez retrouver donc c'est dans graphana cloud dans cost management et puis il y a log et puis dans optimize donc ça c'est la page d'Adaptive logs qui vous montre en fait quand vous arrivez par défaut tous les patterns qu'on a trouvé donc là ça vous donne ça c'est c'est carrément notre environnement de euh de de développement qu'on a donc on voit les patterns on peut voir le volume sur 15 jours donc là le premier qui est en haut il est à 3.4 TB donc c'est quand même quelque chose de conséquent et puis la colonne juste à côté qui est le ratio de requête contre ingestion donc on voit que celui-là en fait on on le requête pratiquement 5 fois plus que ce qu'on l'inggère donc on va probablement pas vouloir le supprimer on attendre un peu la vidéo va moins vite que moi donc tout ce qui est entre chevron timeestamp et number et tout ça ce sont les les champs variables du pattern hein euh donc là les recommandations on les voit sur le côté hein toutes les recommandations donc les premières on a pas des on a on a des recommandations de zéro parce qu'en fait c'est c'est ce qu'on requette le plus même si on vous donne des recommandations vous pouvez décider quand même d'appliquer des euh des des des du du dropping de de de log en haut si vous avez besoin vous avez un fil donc vous pouvez chercher par patterne donc je pense que c'est ce qu'on va faire là donc il y en a 667 en tout vous avez la possibilité aussi de choisir un dropping global et c'est un maximum donc là on peut choisir de jamais dépasser 20 % à travers tous les toutes les recommandations quand on met ça en place même s'il y a un pattern qui est à 30 % il va redescendre à 20 % donc ça permet de mettre des limites de ce que si on veut quelque chose de global en terme de limite on peut on peut les définir après vous pouvez toujours définir par pattern si vous avez envie mais la limite en haut est celle qui est qui passe auudessus quand vous cliquez sur le bouton preview ça vous donne un petit peu une une estimation de des savings que vous allez faire sur chaque pattern normalement on est aussi capable de voir un petit peu d'où viennent ces patterns on peut avoir plus d'informations donc il faut cliquer sur il y a un petit bouton sur chaque pattern on va attendreou donc quand on clique on peut voir de quel service vienent ce pattern là ça peut être intéressant pour aller parler à cette équipe voir si ils sont corrects avec le fait qu'on décide de suimer un peu ces logs là s'ils sont pas intéressants si cette équipe n'a jamais par exemple en fait requter ces logs là ça peut toujours être intéressant et puis on peut voir aussi les savings par service donc ça c'est c'est pas mal c'est aussi intéressant donc on va aller la suite donc si on a envie de voir carrément les log lin de ces pattern là avant d'aller les supprimer vous pouvez aller voir ça vous envoie donc on a un petit lien là qui vous envoie vers explore puis on peut carrément voir à quoi correspond ces pattern là avant de faire la la suppression puis la vidéo va montrer qu'on peut aussi mettre par service donc là on a choisi un service spécifique et on voit les pattern que de ce service là donc comme je disais tout on peut aussi chercher des patterns en particulier c'est un beau JSON log donc là on est en train de mettre une limite à travers tout ensuite on peut regarder la preview donc ça on l'avait déjà fait donc une fois qu'on applique euh ça prend quelques minutes généralement à se mettre se mettre en place et à commencer à supprimer ces lignes donc on va aller voir un petit peu le résultat dans dans le le dashboard d'Inside qui nous permet de voir un petit peu ce qu'on consomme on va voir que petit à petit en fait ça va commencer à descendre donc ça c'est ce qu'on consomme en ce moment on était sur la montée par exemple et puis on va voir que après une quinzaine de minutes on va commencer à redescendre puisqu'on a appliqué un 20 % sur un des patterns al actuelle C vous payez toujours l'igress en fait puisque vous envoyez toujours à la plateforme forcément sur le long terme ce qu'on veut faire c'est le pousser de votre côté sur votre client pour que le client en fait n'envoie pas la donnée comme ça vous payerez pas les non plus donc là on voit qu'au bout de 15 minutes on est redescendu très bas en terme d'ingestion donc c ce c'était vraiment le but alors juste pour vous montrer quelque chose d'intéressant une dernière chose une fois que vous commencez à à éliminer des des logs vous avez quand même des petites informations qui vous le dit et qui qui informment votre équipe ça c'est très intéressant parce que ça nous est arrivé beaucoup de gens perdent la confiance en fait de bah si on supprime les logs on le sait pas qu'on les a supprimé comment on peut faire confiance au système en fait dans graphana maintenant vous allez avoir une petite information dans explore qui vous dit ce log là en fait on en a que tel pourcentage on a plus les 100 % de ce qui ce qui était censé apparaître ok euh donc si vous voulez essayer adaptive logs euh c'est disponible maintenant dans grafana cloud n'hésitez pas à scanner le QR code donc on s'arrête pas là donc j'ai parlé de adaptive matrix j'ai parlé de adaptive log on est en train de regarder pour adaptive trade c'est adaptive profile qui sont aussi très intéressants euh sur TRACE pourquoi pas juste avoir les trac qui ont des erreurs ou juste les trac qui euh sont lentes pour les profils pourquoi pas être capable de l'activer le désactiver pendant un incident ça éviterait de de de de collecter toutes les toutes les métriques alors que il y a pas spécialement d'anomalie sachant que les profils ça peut très rapidement commenc à coûter cher si vous avez beaucoup d'applications donc ce sont des projets qu'on est en train de regarder le but étant encore une fois d'être sûr que toute la télémétrie que vous payez pour soit intéressante et que le bruit soit supprimé si vous en avez pas besoin
