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
