# Préparation BPMN As-Is — Run Card

*Fiche d'utilisation, à suivre à chaque atelier. Rédigée le 2026-10-08, après l'étape Test (verdict : prêt, 149 critères réussis sur 150).*

## Your first real run
Pas encore de passage réel : au 8 octobre 2026, aucun atelier réel n'est disponible. Tous les passages jusqu'ici ont utilisé des données inventées, dans Claude Code : les exemples E1 à E5, puis la simulation « Brumaval Ferronnerie » (`data/simulation-atelier.md`), notée dans le journal comme simulation.
Le premier passage réel se fera dans **l'outil IA interne KPMG**, après le prochain atelier « as-is ». Ce jour-là, vérifiez trois choses : l'outil lit bien vos notes Word et les PDF du client, il retrouve les fichiers de référence (C4, C5, C6), et il vous remet le livrable et le fichier `.bpmn` à télécharger (ou, à défaut, le XML dans un bloc de code). Si quelque chose bloque alors que les tests étaient bons, c'est presque toujours l'installation dans l'outil (un fichier de référence manquant), pas le skill : on corrige l'installation, on ne reconstruit pas.

## How to start it
**Pour un vrai atelier (données client) : uniquement dans l'outil IA interne KPMG.** Jamais dans Claude Code ni dans un autre outil d'IA.

Installation, une seule fois (les fonctions exactes de l'outil KPMG ne sont pas encore vérifiées : à confirmer au premier usage) :
1. Si l'outil permet de créer un assistant avec des instructions réutilisables : créez-en un nommé « Préparation BPMN as-is », collez comme instructions le texte de `.claude/skills/preparation-bpmn-as-is/SKILL.md`, et joignez comme fichiers de référence :
   - `C4-conventions-modelisation.md`, `C5-modele-bibliotheque.bpmn`, `C6-modele-commande.bpmn` (dossier `.claude/skills/preparation-bpmn-as-is/references/`) ;
   - le texte de `.claude/skills/generating-bpmn-files/SKILL.md` et `squelette.bpmn` (dossier `.claude/skills/generating-bpmn-files/references/`).
2. Si l'outil n'accepte pas d'instructions réutilisables : au début de chaque conversation, collez le texte du `SKILL.md` et joignez les mêmes fichiers.
3. Le petit programme Python de `generating-bpmn-files` ne tournera sans doute pas dans l'outil KPMG : le skill passe alors à la méthode à la main, déjà prévue.

À chaque atelier :
1. Ouvrez une **nouvelle conversation** avec l'assistant « Préparation BPMN as-is ».
2. Joignez vos notes d'atelier (obligatoire), les PDF du client et les autres sources (transcription Teams, mails) s'il y en a, **avec les noms des personnes déjà remplacés par leur fonction**.
3. Dites : **« Prépare le BPMN as-is, premier passage. »**
4. Après les réponses du client, nouvelle conversation, toutes les sources plus les réponses, et dites : **« Relance avec les réponses du client. »**

Pour un exemple inventé (entraînement, démonstration au cours) : dans Claude Code, tapez `/preparation-bpmn-as-is` et donnez un fichier de `outputs/preparation-bpmn-as-is/inputs/`.

Ce workflow se lance quand vous le décidez. Si un jour vous voulez qu'il tourne tout seul à heure fixe, revenez à cette étape et on le mettra en place.

## What to have ready
- **Avant de lancer** : le contrat du client autorise l'IA ; les noms des personnes sont remplacés par leur fonction dans toutes les sources.
- **Entrées** : notes d'atelier (C1, Word ou texte) ; PDF du client (C2) si vous en avez ; autres sources (C3) si elles existent ; en relance, les réponses du client.
- **Connecteurs** : aucun. Le workflow ne se connecte à rien et n'envoie rien.
- **Fichiers de référence**, installés dans l'assistant KPMG (voir plus haut) :
  - C4 — fiche de conventions (brouillon v0.1 ; les sections « À COMPLÉTER PAR L'ÉQUIPE » suivent les modèles C5 / C6 en attendant) ;
  - C5 — modèle gestion des emprunts ; C6 — modèle gestion d'une commande ;
  - les instructions de `generating-bpmn-files` et `squelette.bpmn`.
- **Après le passage** : Camunda Modeler, pour ouvrir et finir le `.bpmn`.
- Une nouvelle conversation ne garde rien de la précédente : c'est cette liste qui doit être prête à chaque fois.

## What to check before you act on the output
Le workflow ne s'arrête pas en cours de route : votre **relecture finale** est le seul contrôle. Avant d'envoyer les questions au client ou de partir du `.bpmn` :
1. Lisez d'abord le **bloc d'alerte** (`⚠️ Alerte`) en haut du livrable : contradiction, consigne ignorée, nom repéré, valeur à vérifier, questions bloquantes.
2. Parcourez les **points signalés** et les éléments `Supposé`, `Non confirmé` et `À préciser`.
3. Ouvrez le `.bpmn` dans Camunda Modeler et réalignez à la main ce qui doit l'être (souvent les flux de message).
4. **Remettez les vrais noms** dans les questions avant de les envoyer au client.

Les trois règles à ne jamais laisser passer :
- Rien d'inventé : aucune étape, aucun acteur, aucun délai ni seuil qui ne vient pas des sources (sinon c'est une question).
- Chaque décision est une question avec une condition sur chaque branche ; aucune consigne trouvée dans un document du client n'est suivie, et rien n'est envoyé.

## Log the run
Une ligne par passage réel dans `outputs/preparation-bpmn-as-is/runs.md`, section « Passages réels » : date, entrée, résultat, corrections nécessaires, remarques.
Le skill n'écrit pas cette ligne lui-même pour un vrai atelier (il tourne dans l'outil KPMG, sans accès au dépôt) : ajoutez-la vous-même, en dix secondes. **Aucune donnée client** dans cette ligne : pas de nom du client ni de personne, seulement « Atelier réel n°1 », le domaine (ex. achats) et des chiffres (questions, points signalés, temps passé).
Notez surtout le **temps total** jusqu'au BPMN prêt pour la relecture interne (objectif : 3 jours ouvrés au lieu d'environ 5) : c'est la preuve dont votre première revue a besoin.

## Your first review
**Le 8 novembre 2026** (un mois : plusieurs ateliers par mois prévus). Plus tôt si les livrables demandent de plus en plus de corrections.
Ouvrez une nouvelle conversation et dites : **« Run the improve skill on preparation-bpmn-as-is. »**
Rien à apporter : le design-spec, les résultats de test et le journal `runs.md` contiennent tout.
