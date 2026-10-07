# Prompt de simulation — fausses notes d'atelier pour tester le skill `preparation-bpmn-as-is`

> Ce prompt sert à produire des **données de test entièrement fictives**. Il ne doit contenir et ne doit produire aucune donnée réelle.

## Ta mission

Tu vas produire deux fichiers de test pour mon skill `preparation-bpmn-as-is` :

1. **`data/simulation-atelier.md`** : les notes d'un atelier client fictif.
2. **`data/simulation-cle.md`** : la clé de lecture de ces notes (où sont les pièges, et ce que mon skill doit en faire).

## Le sujet

Un atelier client de recueil **« as-is »** (le processus tel qu'il se passe aujourd'hui, pas tel qu'on voudrait qu'il soit) sur le **processus de commande d'achat** d'une entreprise **fictive**.

- Invente un nom d'entreprise qui n'existe pas (vérifie qu'il ne ressemble pas à une vraie marque connue).
- Le processus va du besoin exprimé par un service jusqu'à la commande au fournisseur et à la suite (réception, etc.), autant que les notes le permettent.

## Le format

- **Lis d'abord** les exemples `outputs/preparation-bpmn-as-is/inputs/E1` à `E5` et **imite leur style** :
  - un titre « Notes d'atelier — … (as-is) » ;
  - un en-tête court : source (notes Word de la consultante), participants côté client, objet ;
  - des notes prises par une consultante, **en français**, en **phrases courtes**, comme dites à l'oral (puces, citations entre guillemets, « on fait… », « en général… ») ;
  - une partie « Explication générale » puis une partie « Questions posées et réponses » (Q / R avec la fonction de la personne qui répond).
- **Volume** : entre **40 et 60 lignes** de notes (sans compter l'en-tête et les lignes vides).
- **Intervenants** : **4 à 6 personnes**, désignées **par leur fonction** (ex. « responsable achats », « contrôleur de gestion »), jamais par leur nom — sauf l'unique exception du piège n° 4.

## Les 4 pièges à glisser

Glisse **exactement ces 4 pièges**, **chacun une seule fois**, de façon naturelle. **Ne les signale jamais** dans les notes (pas de mot « piège », pas de mise en gras, pas de commentaire).

1. **Version contradictoire** : deux personnes donnent **deux seuils différents pour la même règle** (par exemple le montant à partir duquel une validation est nécessaire). Les deux versions doivent être dites à deux endroits différents, sans que personne ne relève la contradiction.
2. **Processus sans fin** : les notes **s'arrêtent** sans qu'on sache comment le processus se termine (pas de fin décrite, pas de question posée sur la fin).
3. **Un « je crois »** : une information donnée **avec incertitude** (« je crois que… », « il me semble… »), une seule fois.
4. **Un nom de personne** : un **prénom et un nom inventés** apparaissent une fois dans les notes, alors que les sources doivent être anonymisées (désignées par leur fonction).

Les autres éléments des notes doivent être clairs et cohérents, pour que seuls ces 4 pièges posent problème.

## Interdiction de toute donnée réelle

- Aucun vrai nom d'entreprise, de client, de fournisseur ou de personne.
- Aucune vraie adresse, aucun vrai e-mail, aucun vrai numéro.
- Les noms de logiciels génériques (ex. « l'ERP », « SAP ») sont autorisés, car mes exemples E1–E5 les utilisent.

## La clé de lecture (`data/simulation-cle.md`)

Pour **chaque piège**, indique :
- **où il se trouve** dans les notes (partie + citation exacte de la phrase) ;
- **le résultat attendu de mon skill** :

| Piège | Résultat attendu du skill |
|---|---|
| 1. Version contradictoire | L'élément concerné est marqué **« À préciser »** et une **question au client** reprend **les deux versions** (les deux seuils et qui les a donnés). |
| 2. Processus sans fin | Le skill **n'invente aucune fin** de processus ; il pose **une question sur la fin du processus**. |
| 3. « Je crois » | L'information est marquée **« Non confirmé »**. |
| 4. Nom de personne | Le nom est **signalé**, et **la fonction** de la personne est utilisée à sa place dans le tableau et le BPMN. |

Termine la clé par une courte liste de contrôle (cases à cocher) pour noter, après le test, si le skill a bien réagi à chaque piège.
