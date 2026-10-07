# Build notes — Préparation BPMN As-Is

## Où sont les skills
| Skill | Emplacement | Commande |
|---|---|---|
| S1 — preparation-bpmn-as-is (orchestrateur, étapes 1 à 6) | `.claude/skills/preparation-bpmn-as-is/SKILL.md` + `references/` (copies de C4, C5, C6) | `/preparation-bpmn-as-is` |
| S2 — generating-bpmn-files (étape 6 : tableau → fichier `.bpmn`) | `.claude/skills/generating-bpmn-files/SKILL.md` + `references/squelette.bpmn` | `/generating-bpmn-files` |

## Ce qui a été construit (par rapport au design-spec)
- S1 : vérification au lancement (rappel anonymisation et contrat, premier passage ou relance, notes C1 obligatoires) ; étapes 2 à 4 avec rôle, tâche, règles et format ; étape 6 qui appelle S2, avec plan de secours (XML dans un bloc de code) ; noms des fichiers, journal `runs.md` pour les tests, résumé « Ce que j'ai fait ».
- S2 : correspondance type BPMN → élément XML, annotations « Supposé » / « Non confirmé », règles de mise en page, contrôle final, anomalies listées sans correction silencieuse. Le squelette `.bpmn` est lu sans erreur par bpmn-moddle (bibliothèque de lecture de Camunda Modeler).

## Reste à faire
- Étape Test : lancer S1 sur E1 à E5 et ouvrir chaque `.bpmn` produit dans Camunda Modeler (AC13).
- Outil IA KPMG : vérifier ses capacités (instructions réutilisables, fichiers de référence, création de fichier) puis y recopier S1, S2 et leurs fichiers de référence.
- Compléter les sections « À COMPLÉTER PAR L'ÉQUIPE » de C4 quand elles sont connues (puis recopier C4 dans `references/`).

## Corrections après relecture (2026-10-07)
Comparaison du skill avec le design-spec et les requirements ; corrections faites dans S1 (et S2 pour rester d'accord) :
- Notes d'atelier acceptées en Word, `.md` ou texte collé ; un fichier qui regroupe plusieurs sources (cas des exemples E1 à E5) est découpé en C1 / C2 / C3. Avant, « Word obligatoire » pouvait bloquer les tests.
- Façon d'écrire le tableau fixée (ID, liste des types BPMN, participants externes, messages, conditions des passerelles), la même dans S1 et S2, pour que le fichier `.bpmn` se génère sans anomalie.
- Chaque élément « Non confirmé » ou « À préciser » a sa question Qx (le `.bpmn` y renvoie).
- Relance : ce que devient une question à laquelle le client a répondu.
- Noms des fichiers et test / usage réel : seuls E1 à E5 sont enregistrés dans le dépôt ; toute autre source n'y est jamais écrite.
