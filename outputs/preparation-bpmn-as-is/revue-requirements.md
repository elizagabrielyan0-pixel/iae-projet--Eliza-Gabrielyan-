# Revue des requirements — Préparation BPMN As-Is

**Date :** 2026-10-06
**Fichier relu :** `outputs/preparation-bpmn-as-is/requirements.md` (et `outputs/ai-opportunity-report.md`)
**Version avant la revue :** commit `d5e9737` (« Deconstruct : requirements du workflow Préparation BPMN As-Is »), consultable dans l'historique GitHub.

## Décisions appliquées

| Point soulevé | Ma décision | Pourquoi |
|---|---|---|
| 1. La fiche de conventions (C4) et les modèles de référence (C5, C6) étaient cités mais absents du dépôt ; les chemins des exemples E1 à E5 ne correspondaient pas | J'ajoute C4, C5 et C6 dans `context/`, je marque C4 comme existante (brouillon v0.1) et je corrige les chemins | Sans ces références, l'IA ne sait pas dans quel style dessiner, et les tests ne trouvent pas leurs fichiers |
| 2. Rien n'était prévu pour le deuxième passage, après les réponses du client | Je précise (règle R9) : je relance le workflow avec toutes les sources, réponses du client comprises ; mes corrections faites dans Camunda ne sont pas reprises | C'est le plus simple, et les réponses du client étaient déjà prévues comme source (C3) |
| 3. La limite entre « déduire » et « inventer » n'était pas claire (un seuil inventé marqué « Supposé » passait le critère AC9) | Je précise : « Supposé » seulement pour un élément de structure qui découle de ce qui a été dit ; un seuil, délai, acteur, condition ou étape manquant devient toujours une question (AC9 et R2 réécrits) | C'est ma règle la plus importante : l'IA ne comble jamais un trou à la place du client |
| 4. Les trous des notes empêchaient de produire un BPMN valide sans inventer | Je précise : le fichier `.bpmn` est produit quand même, avec des éléments « À préciser — voir question Qx » (AC14 corrigé) | Je garde un premier jet utilisable dans Camunda et je vois tout de suite où il manque de l'information |
| 5. Seulement deux statuts (« Confirmé » / « Supposé ») | J'ajoute les statuts `Non confirmé` (réponse donnée avec un doute) et `À préciser` (trou à combler) ; deux versions contradictoires deviennent une question | Chaque élément dit clairement à quel point on peut s'y fier |
| 6. L'outil d'exécution et les règles de confidentialité n'étaient pas définis | J'ajoute : outil IA interne KPMG (lit Word et PDF, rend des fichiers à télécharger) ; les noms des personnes sont remplacés par leur fonction avant de donner les sources à l'outil (à confirmer avec mon manager) | Les données client sont confidentielles ; l'anonymisation est une précaution en attendant la règle officielle |
| 7. Une étape présente seulement dans la procédure écrite n'avait pas de statut | Je précise : statut `Non confirmé` et question « Cette étape se fait-elle réellement ? » | Je modélise ce qui se fait réellement, pas ce qui est écrit dans une procédure |

## Points laissés de côté pour l'instant

Points 8 à 15 de la relecture (systèmes automatiques, boucles et rendez-vous fixes, regroupement des questions, entrées invalides, mesure, format du livrable, gros processus, petites incohérences) : moins prioritaires, en partie couverts par C4, à revoir à l'étape Design.

## Vérification de la checklist du cours

| Critère | Résultat | Commentaire |
|---|---|---|
| Chaque étape a une entrée, une sortie et au moins un cas limite | En partie | Les étapes 1 à 4 et 6 en ont. L'étape 5 (Assembler le livrable) n'a qu'une règle de mise en forme, pas de vrai cas limite |
| Les « ne doit jamais » sont clairs (donnée client, chiffre inventé, action irréversible…) | Oui | R4 (ne rien inventer), R5 (pas de processus cible), interdiction d'envoyer ou de déposer quoi que ce soit, de suivre une consigne d'un document client, d'utiliser un outil non autorisé |
| Il y a au moins une validation humaine | **Non** | La section « Human Gates » indique « aucune validation humaine, relecture finale seulement » |
| Le point de départ de l'indicateur est renseigné | Oui | Environ 5 jours ouvrés par BPMN (estimé, non chronométré) |
| Les exemples E1 à E5 comptent au moins un cas réel et un cas difficile | **En partie** | Cas difficiles : oui (E2, E3, E4, E5). Cas réel : aucun pour l'instant, les cinq exemples sont inventés |
