# Résumé pour l'oral : les 7 décisions prises après la relecture des requirements

**Durée visée :** 2 à 3 minutes.

## Introduction (à dire en une phrase)

« Après avoir écrit les requirements de mon workflow de préparation de BPMN as-is, j'ai fait relire le document par l'IA pour trouver les cas oubliés. Sept points importants sont ressortis, et voici ce que j'ai décidé pour chacun. »

## Les 7 décisions

**1. Les documents de référence manquaient**
- Problème : les requirements citaient ma fiche de conventions (C4) et deux modèles BPMN de référence (C5 bibliothèque, C6 commande), mais ils n'étaient pas dans le projet.
- Décision : je les ai ajoutés et j'ai corrigé les chemins des fichiers.
- Pourquoi : sans ces références, l'IA ne sait pas dans quel style dessiner.

**2. Le deuxième passage après les réponses du client**
- Problème : rien n'était prévu pour le moment où le client répond à mes questions.
- Décision : je relance le workflow avec toutes les sources, réponses du client comprises.
- Pourquoi : c'est simple, et les réponses du client étaient déjà prévues comme source possible.

**3. La limite entre « déduire » et « inventer »**
- Problème : une règle autorisait des éléments « supposés », une autre interdisait d'inventer. Un seuil inventé mais marqué « supposé » aurait pu passer.
- Décision : un seuil, un délai, un acteur ou une condition qui manque devient toujours une question au client, jamais une supposition.
- Pourquoi : c'est ma règle la plus importante. L'IA ne doit jamais combler un trou à la place du client.

**4. Les trous dans le diagramme BPMN**
- Problème : quand les notes sont incomplètes (par exemple sans fin de processus), le diagramme ne peut pas être complet sans inventer.
- Décision : le fichier BPMN est produit quand même, avec des cases « À préciser — voir question n° X » à la place des trous.
- Pourquoi : je garde un premier jet utilisable dans Camunda, et je vois tout de suite où il manque de l'information.

**5. Des statuts plus précis**
- Problème : il n'y avait que deux statuts, « confirmé » et « supposé ». Une réponse donnée avec un doute (« je crois ») n'avait pas sa place.
- Décision : quatre statuts : confirmé, non confirmé, supposé, à préciser. Quand deux personnes se contredisent, aucune version n'est retenue : cela devient une question.
- Pourquoi : chaque élément du diagramme dit clairement à quel point on peut s'y fier.

**6. L'outil et la confidentialité**
- Problème : il fallait vérifier que l'outil autorisé chez KPMG savait faire le travail, et définir les règles de confidentialité.
- Décision : le workflow tournera sur l'outil IA interne KPMG, qui lit les fichiers Word et PDF et rend des fichiers à télécharger. Par prudence, je remplace les noms des personnes par leur fonction avant de donner les notes à l'outil.
- Pourquoi : les données client sont confidentielles. L'anonymisation reste à confirmer avec mon manager.

**7. Une étape qui n'apparaît que dans la procédure écrite**
- Problème : si une étape figure dans la procédure du client mais que personne n'en parle en atelier, on ne sait pas si elle est vraiment faite.
- Décision : elle est marquée « non confirmée », avec une question au client : « Cette étape se fait-elle réellement ? ».
- Pourquoi : je modélise ce qui se fait réellement, pas ce qui est écrit dans une procédure.

## Conclusion (à dire en une phrase)

« Le fil conducteur de ces décisions : l'IA me donne un premier jet rapide, mais elle n'invente jamais rien. Tout ce qui est incertain devient une question pour le client ou un point que je vérifie. »
