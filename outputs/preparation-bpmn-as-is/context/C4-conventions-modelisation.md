# C4 — Conventions de modélisation BPMN « as-is »

**Statut :** brouillon v0.1, à valider par l'équipe projet.
**Bâti à partir de :** norme BPMN 2.0 (C7) et des deux modèles de référence KPMG (C5 gestion des emprunts, C6 gestion d'une commande, réalisés sous Camunda Modeler 5.27).
**Règle de priorité :** ce document prime sur le style déduit des modèles. Les sections marquées **[À COMPLÉTER PAR L'ÉQUIPE]** couvrent les règles propres au projet et au client qui ne figurent dans aucun modèle.

---

## 1. Structure du diagramme

- Un **participant (pool) interne** porte le nom du processus, sous la forme « Gestion + objet » : « Gestion emprunt », « Gestion d'une commande ».
- Chaque **acteur externe** au processus (client, adhérent, fournisseur) est un participant séparé : « Adhérent », « CLIENT », « Fournisseurs ».
- Le participant interne est découpé en **couloirs (lanes)**, un par service ou par rôle, jamais par personne nommée : « Service commercial », « Service production », « Bibliothécaire », « Documentaliste ».
- Un couloir ou un participant qui n'intervient dans aucune étape du processus n'est pas créé.
- Les échanges avec un acteur externe sont des **flux de messages** entre participants, jamais des flux de séquence.

## 2. Nommage

| Élément | Règle | Exemples tirés des modèles |
|---|---|---|
| Tâche | Verbe à l'infinitif + complément, sans article | « Enregistrer commande », « Rechercher adhérent », « Créer facture » |
| Sous-processus | Nom d'action, éventuellement avec article | « Gestion litige », « Validation d'un emprunt », « Livraison » |
| Événement de début déclenché par l'extérieur | Nom du message reçu | « Commande client », « Demande d'emprunt » |
| Événement de début d'un sous-processus | Non nommé | — |
| Message | Nom de l'objet transmis | « Ordre confirmation », « Relance », « Notification annulation » |
| Minuterie | Durée seule | « 8 jours », « 15 jours », « 1 mois » |
| Passerelle de décision | Question courte terminée par « ? » | « Adhérent existant ? », « Stock et capacité ? », « Cotisation à jour ? » |
| Branches d'une décision | Réponse ou condition courte | « OUI » / « NON », « < 5 » / « >= 5 » |
| Passerelle de convergence | Non nommée | — |
| Événement de fin | État final de l'objet traité, un par issue | « Commande terminée », « Commande annulée », « Fin emprunt litige » |
| Événement lien | « Vers » + destination | « Vers fabrication », « Vers annulation commande » |

- Les libellés sont relus pour éviter fautes de frappe et doubles espaces (exemples à ne pas reproduire : « Vérfier », « Emprunt  impossible »).
- Les termes du client et les termes SAP (noms de transactions, de documents, de statuts) sont conservés tels quels.

## 3. Types de tâches

| Type | Quand l'utiliser | Exemples |
|---|---|---|
| Tâche utilisateur (userTask) | Une personne agit dans un système ou un logiciel | « Enregistrer emprunt », « Créer ordre de confirmation » |
| Tâche manuelle (manualTask) | Une action physique, sans système | « Ranger ouvrage » |
| Tâche d'envoi (sendTask) | Une personne envoie une demande ou une information à un acteur externe | « Relancer adhérent », « Demander cotisation » |
| Tâche de service (serviceTask) | Un contrôle ou un traitement automatique fait par le système | « Contrôler cotisation », « Contrôler emprunt en retard » |
| Sous-processus | Un ensemble d'étapes qui alourdirait le diagramme, ou une partie que le client n'a pas détaillée | « Gestion litige », « Assemblage », « Traitement comptable » |

- Une tâche correspond à une seule action réalisée par un seul acteur.
- Les contrôles automatiques successifs sont des tâches de service distinctes, chacune suivie de sa décision.
- Une partie que le client mentionne sans la décrire (« on ne détaillera pas notre procédure ») est un sous-processus réduit, sans contenu inventé.

## 4. Événements

- Un processus déclenché par une demande externe commence par un **événement de début de type message**.
- Chaque délai ou relance est un **événement minuterie** portant sa durée.
- Une attente du type « réponse reçue ou délai dépassé » se modélise par une **passerelle basée sur les événements**, suivie d'un événement message et d'un événement minuterie.
- Un envoi à l'extérieur en cours de processus est un événement intermédiaire de type message (émission) ou une tâche d'envoi.
- Une fin qui notifie l'acteur externe est un **événement de fin de type message** (« Emprunt impossible »).
- Les **événements lien** remplacent les flux longs qui traverseraient le diagramme.

## 5. Passerelles

| Type | Usage |
|---|---|
| Exclusive | Une seule branche selon une condition (décision) |
| Parallèle | Activités menées en même temps, avec ouverture et fermeture explicites |
| Inclusive | Une ou plusieurs branches selon les conditions (ex. remettre en stock seulement si des produits étaient réservés) |
| Basée sur les événements | Attente du premier événement survenu (réponse ou délai) |

- Chaque passerelle ouvrante a sa passerelle fermante du même type, sauf quand les branches mènent à des fins différentes.
- Chaque branche sortante d'une passerelle exclusive ou inclusive porte une condition.

## 6. Niveau de détail

- Le diagramme décrit l'existant tel qu'il est pratiqué, sans amélioration.
- Le niveau de détail retenu est celui des modèles de référence : une ligne de diagramme lisible par participant interne, le détail renvoyé en sous-processus.
- **[À COMPLÉTER PAR L'ÉQUIPE]** Niveau de détail attendu sur ce projet (macro-processus, processus, procédure) et nombre maximal de tâches par diagramme avant découpage.

## 7. Mise en page

- Lecture de gauche à droite, couloirs horizontaux.
- Aucune forme superposée, flux sans croisement quand c'est possible.
- **[À COMPLÉTER PAR L'ÉQUIPE]** Position des participants externes (au-dessus ou au-dessous du participant interne), alignement, tailles.

## 8. Règles propres au projet et au client [À COMPLÉTER PAR L'ÉQUIPE]

- Langue des libellés exigée par le client (par défaut : français).
- Convention d'identifiants ou de numérotation des processus (ex. référence du processus dans la cartographie du projet).
- Façon de représenter les systèmes (SAP, outils annexes) : couloir dédié, annotation ou absence.
- Façon de représenter les exceptions et les cas rares.
- Usage des annotations et des objets de données.
- Éléments attendus par le client sur le livrable final (cartouche, version, date, format d'export).
- Circuit de validation interne avant envoi.
