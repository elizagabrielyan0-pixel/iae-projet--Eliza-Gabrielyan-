# Justification des choix du Design — Préparation BPMN As-Is

Une phrase par choix, pour l'oral. Le plan complet est dans `design-spec.md`.

## Les trois grandes décisions

| Choix | Justification |
|---|---|
| **Plateforme : outil IA interne KPMG** | La politique KPMG n'autorise les données client que dans les outils internes, donc le workflow tourne là où les vraies données ont le droit d'aller. |
| **Construction et tests dans Claude Code** | Je construis et je teste avec cinq ateliers inventés, sans aucune donnée client, puis je transfère les instructions dans l'outil KPMG. |
| **Forme : un skill plutôt qu'un agent** | C'est moi qui lance le travail après chaque atelier et les étapes sont toujours les mêmes, donc il n'y a pas besoin d'une IA qui choisit son propre chemin. |
| **Validation du plan** | J'ai relu le plan complet avant de le valider, pour que rien ne soit fabriqué sans mon accord. |

## Architecture

| Choix | Justification |
|---|---|
| **Autonomie « Guidé »** | L'ordre des étapes est fixe et l'IA fait des choix (statut, questions), mais dans un cadre strict, et je relis tout à la fin. |
| **Mode « Augmented » (je suis présente)** | Le workflow est lancé à la main et je relis le résultat, il ne tourne jamais seul ni à heure fixe. |
| **Emballage « Standalone Skill »** | Un ensemble d'instructions autonome se charge une fois et se réutilise facilement, sans infrastructure particulière. |
| **Aucune connexion à d'autres logiciels** | Je dépose les fichiers et je télécharge les résultats moi-même, ce qui est plus simple et plus sûr. |
| **Modèle d'IA « raisonnement »** | Reconstituer un processus à partir de notes incomplètes et contradictoires demande du jugement, et le fichier BPMN exige une grande précision. |
| **Lecture d'images pour l'étape 2** | Certains PDF du client sont scannés ou faits de schémas, l'IA doit donc pouvoir lire des images. |
| **Pas de mémoire entre deux exécutions** | À chaque relance je redonne toutes les sources, ce qui évite que l'IA réutilise une ancienne version périmée du processus. |

## Découpage en skills

| Choix | Justification |
|---|---|
| **Deux skills au lieu d'un** | Transformer un tableau en fichier BPMN est un savoir-faire technique différent, réutilisable sur d'autres projets et testable à part. |
| **S1 `preparation-bpmn-as-is`, skill principal** | Il enchaîne les étapes 1 à 5 dans l'ordre et appelle S2 à la fin, pour que je lance tout en une seule commande. |
| **S2 `generating-bpmn-files`, nommé d'après sa capacité** | Un nom qui décrit ce qu'il fait permet de le réutiliser en dehors de ce workflow. |
| **Aucun agent** | Rien dans le workflow ne demande à l'IA de décider seule de la suite, un agent ajouterait du risque sans bénéfice. |
| **Construire S2 en premier** | L'ouverture du fichier dans Camunda est le risque principal, donc je le vérifie avant tout le reste. |
| **Rappel au lancement (anonymisation, contrat client)** | Ces deux vérifications sont obligatoires avant d'utiliser l'IA, et un rappel systématique évite de les oublier. |
| **Arrêt si les notes d'atelier manquent** | Sans les paroles des intervenants, l'IA ne peut rien confirmer et produirait un résultat inutilisable. |
| **Solution de repli : XML à copier** | Si l'outil KPMG ne sait pas créer de fichier, je peux quand même obtenir le BPMN en copiant le texte, ce qui marche partout. |

## Sécurité

| Choix | Justification |
|---|---|
| **Lecture seule, aucun envoi** | Le workflow ne fait que produire des fichiers, c'est moi seule qui décide ce qui part chez le client. |
| **Documents du client = information, jamais consigne** | Un document pourrait contenir une instruction cachée adressée à l'IA, elle doit l'ignorer et me la signaler (testé avec l'exemple E4). |
| **Ma relecture finale comme point de contrôle** | Le pire risque est un élément inventé envoyé au client, ma relecture avant tout envoi l'empêche. |
| **Statut et source sur chaque élément** | Je vois immédiatement à quel point je peux me fier à chaque élément et d'où il vient. |
| **Anonymisation des noms, confirmée par mon manager** | Les données client sont confidentielles, donc les noms sont remplacés par les fonctions avant de passer par l'outil. |

## Tests et suite

| Choix | Justification |
|---|---|
| **Réutiliser les 14 critères et 5 exemples de mes requirements** | Ils définissent déjà ce qu'est un bon résultat, inutile de les réécrire. |
| **Ajouter un atelier réel avant les tests** | Les cinq exemples sont inventés, un cas réel anonymisé montrera si le workflow tient face à la réalité. |
| **Mesurer le temps jusqu'au BPMN prêt à envoyer** | C'est l'indicateur qui prouvera le gain : passer d'environ 5 jours à 3 jours par BPMN. |
