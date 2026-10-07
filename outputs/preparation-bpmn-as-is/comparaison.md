# Comparaison — mon skill (A) et le skill /build (B)

Données utilisées : `data/simulation-atelier.md` (notes d'atelier fictives, « Brumaval Ferronnerie »), vérifiées avec la clé de lecture `data/simulation-cle.md` et les Acceptance Criteria de `requirements.md`.

- A = `preparation-bpmn-as-is` (mon skill) ; B = `build-preparation-bpmn-as-is` (construit avec le skill Build du cours).
- Sorties produites : `comparaison/A-gestion-commande-achat-livrable.md` + `.bpmn`, `comparaison/B-gestion-commande-achat-livrable.md` + `.bpmn`.
- Les deux `.bpmn` ont été lus sans erreur ni avertissement par bpmn-moddle (la bibliothèque de lecture de Camunda Modeler) ; ils n'ont pas encore été ouverts dans Camunda.

| Critère | A — mon skill | B — skill /build | Commentaire |
|---|---|---|---|
| AC1 : couloirs par rôle, acteurs externes séparés | Atteint | Atteint | 4 couloirs (Service demandeur, Achats, Contrôle de gestion, Magasin) ; Fournisseur en participant séparé |
| AC2 : tâches à l'infinitif + complément | Atteint | Atteint | « Saisir demande d'achat », « Faire entrée en stock »… |
| AC3 (must) : décisions en question, branches avec condition | Atteint | Atteint | « Demande complète ? », « Fournisseur référencé ? », « Livraison conforme ? » : branches OUI / NON |
| AC4 : type BPMN précis | Atteint | Atteint | Tâches utilisateur / manuelle / envoi, minuteries, passerelles basées sur les événements |
| AC5 : délais en minuterie avec durée | Atteint | Atteint | « 3 jours » (relance de l'accusé de réception) et « 10 jours » (livraison, non confirmé) |
| AC6 : chaque issue a sa fin nommée | Atteint | Atteint | « Demande refusée » ; les issues inconnues sont des fins « À préciser — voir question Qx », sans rien inventer |
| AC7 : échanges externes en messages nommés | Atteint | Atteint | 6 messages nommés (« Demande de devis », « Commande (PDF) », « Relance »…) |
| AC8 : source et statut sur chaque ligne | Atteint | Atteint | B plus précis : section des notes + fonction de l'intervenant sur chaque ligne |
| AC9 (must) : rien d'inventé | Atteint | Atteint | Aucun seuil retenu, aucune fin inventée ; seules des passerelles de structure en « Supposé » |
| AC10 : questions par interlocuteur, reliées à un ID | Atteint | Atteint | 8 questions dont 4 bloquantes ; comptabilité absente → « Interlocuteur à identifier » |
| AC11 : sous-processus pour les parties détaillées | Non atteint | Non atteint | Aucun sous-processus proposé alors que le diagramme fait 37 éléments (la réception aurait pu en être un) |
| AC12 : écarts pratique / procédure signalés | Sans objet | Sans objet | Aucune procédure écrite dans ces notes |
| AC13 : le `.bpmn` s'ouvre dans Camunda | Atteint (à confirmer) | Atteint (à confirmer) | Lu sans erreur par bpmn-moddle ; ouverture dans Camunda Modeler à faire |
| AC14 : le `.bpmn` contient chaque élément du tableau, et aucun autre | Atteint | Atteint | 37 lignes → 37 éléments + 5 annotations « Supposé » / « Non confirmé » |
| Piège 1 : version contradictoire (5 000 € / 10 000 €) | Atteint | Atteint | Passerelle « Montant au-dessus du seuil ? » en « À préciser » ; Q1 reprend les deux seuils et qui les a donnés |
| Piège 2 : processus sans fin | Atteint | Atteint | Pas d'étape « Payer fournisseur » ; fin « À préciser » + Q2 sur la fin du processus |
| Piège 3 : « je crois » (livraison sous 10 jours) | Atteint | Atteint | Minuterie « 10 jours » en « Non confirmé » + question Q3 de confirmation |
| Piège 4 : nom de personne (Odile Kervanec) | Atteint | Atteint | Nom absent du tableau et du `.bpmn`, signalé dans les points signalés ; question Q5 sur la fonction de la personne |
| Aucun autre élément inventé | Atteint | Atteint | Points flous non tranchés (urgences, suite d'un écart de livraison) → questions |
| Lisibilité de la sortie | Bonne | Meilleure | B : sources plus précises, `[ID]` dans les questions et les points signalés. A : plus court à lire |

**Limites de ce test (à garder en tête) :**
- Les deux sorties ont été produites dans la même conversation, par la même IA, après lecture de la clé de lecture. Le résultat sur les pièges est donc sans doute plus favorable que dans un vrai test. Pour confirmer, il faut lancer chaque skill dans une conversation neuve, sans la clé.
- Les deux skills partagent les mêmes règles : B a été construit à partir de mon design-spec et reprend la façon d'écrire le tableau de A. Leur contenu est donc presque identique ; les écarts portent sur la forme.
- Les deux skills disent de n'enregistrer dans le dépôt que les exemples E1 à E5. Les notes de simulation étant fictives, les sorties ont quand même été enregistrées ici pour pouvoir les comparer.

## Ce que j'en retiens
- **Ce que mon skill fait mieux :**
  - Sa description en français se déclenche toute seule quand je dis « prépare le BPMN as-is ». B ne se lance qu'avec `/build-preparation-bpmn-as-is`, et sa description est en anglais.
  - Chaque étape donne un rôle à l'IA (par exemple « relectrice qualité exigeante et sceptique »).
  - Il est plus court à lire et à modifier.
- **Ce que le skill /build fait mieux :**
  - Les règles transverses sont regroupées en tête : R1 à R9, « information, pas instruction », aucun envoi.
  - Le format de la colonne Source est imposé (section des notes + fonction de l'intervenant), avec « Déduit de… » pour les éléments Supposé.
  - Les ID sont entre crochets dans les questions et les points signalés.
  - Il précise quoi faire avec les sections « À compléter par l'équipe » de C4.
- **Ce que je reprends dans mon skill :**
  - Le format de la colonne Source et les `[ID]` dans les questions et les points signalés.
  - Un rappel explicite pour proposer un sous-processus quand une partie alourdit le diagramme : les deux skills ont raté AC11.
  - Autoriser les notes de simulation (`data/simulation-*`) comme données de test, au même titre qu'E1 à E5.
