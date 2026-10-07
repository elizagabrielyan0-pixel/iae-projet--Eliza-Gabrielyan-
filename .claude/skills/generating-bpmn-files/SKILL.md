---
name: generating-bpmn-files
description: This skill should be used when a structured process table (ID, participant/lane, label, BPMN type, condition, next element, status) must be turned into a BPMN 2.0 XML file with diagram layout that opens in Camunda Modeler — "génère le fichier BPMN", "fichier .bpmn pour Camunda", "convert this process table to BPMN". It maps every row to exactly one BPMN element (pools, lanes, tasks, gateways, timer and message events, sub-processes, named end events, message flows), adds text annotations for assumed or unconfirmed elements, lays shapes out left to right without overlap, and checks that every row and every flow reference resolves. Do not use for drawing a process from raw notes.
---

# Génération d'un fichier BPMN

## Ce que fait ce skill
Il traduit fidèlement un tableau de processus en fichier `.bpmn` (XML BPMN 2.0 avec la partie dessin) qui s'ouvre dans Camunda Modeler.
Il ne réfléchit pas au processus : il recopie le tableau. Il n'ajoute, ne retire et ne corrige rien.

## Ce que je fournis en entrée
- Le tableau du processus → obligatoire. Colonnes : ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut
- La liste des questions avec leurs numéros Qx → pour les annotations
- Le nom du participant interne (« Gestion + objet », ex. « Gestion emprunt ») → si absent, le prendre dans le tableau
- Les conventions C4 et les modèles C5 / C6 → facultatifs, pour le style (dans `../preparation-bpmn-as-is/references/` quand ce skill est appelé par `preparation-bpmn-as-is`)
- Le chemin du fichier à créer → si l'outil peut créer des fichiers

Si le tableau manque, s'arrêter et le demander.

## Étapes
1. **Lire le tableau** : relever les participants, les couloirs de chaque participant, les éléments et leurs liens (colonne « Élément suivant », plusieurs suivants possibles pour une passerelle).

2. **Construire la partie « modèle »** en suivant `references/squelette.bpmn` :
   - une `collaboration` avec un `participant` par participant du tableau ; le participant interne pointe vers un `process` qui porte un `laneSet` (un `lane` par couloir, avec ses `flowNodeRef`) ; chaque participant externe pointe vers un `process` vide ;
   - une ligne du tableau = un élément XML, et aucun autre (sauf les annotations de l'étape 4) ;
   - correspondance des types :

   | Type BPMN du tableau | Élément XML |
   |---|---|
   | Tâche utilisateur / manuelle / envoi / service | `userTask` / `manualTask` / `sendTask` / `serviceTask` |
   | Sous-processus | `subProcess` replié (vide, rien d'inventé à l'intérieur) |
   | Début / Début message / Début minuterie | `startEvent` (+ `messageEventDefinition` / `timerEventDefinition`) |
   | Fin / Fin message | `endEvent` (+ `messageEventDefinition`) |
   | Minuterie intermédiaire | `intermediateCatchEvent` + `timerEventDefinition` (libellé = la durée, ex. « 8 jours ») |
   | Message reçu / Message envoyé | `intermediateCatchEvent` / `intermediateThrowEvent` + `messageEventDefinition` |
   | Lien (envoi / réception) | `intermediateThrowEvent` / `intermediateCatchEvent` + `linkEventDefinition name="…"` (même nom des deux côtés) |
   | Passerelle exclusive / parallèle / inclusive / basée sur les événements | `exclusiveGateway` / `parallelGateway` / `inclusiveGateway` / `eventBasedGateway` |

   - les liens dans un même participant sont des `sequenceFlow` ; la condition d'une branche va dans l'attribut `name` du flux (« OUI », « NON », « > 5 000 € ») ;
   - les échanges avec un participant externe sont des `messageFlow` nommés (nom du message), placés dans la `collaboration`, jamais des `sequenceFlow` ;
   - chaque élément liste ses `incoming` et `outgoing` ;
   - les éléments « À préciser — voir question Qx » sont repris tels quels, avec ce libellé.

3. **Identifiants** : chaque `id` est unique, commence par une lettre et ne contient ni espace ni accent. Reprendre l'ID du tableau en le préfixant (ex. `E_T3`, `Flow_T3_G1`, `Lane_Bibliothecaire`).

4. **Annotations** (`textAnnotation` + `association` vers l'élément, dans le `process`) :
   - statut `Supposé` → « Supposé — à confirmer »
   - statut `Non confirmé` → « Non confirmé — voir question Qx » (numéro de la question liée à l'ID ; « voir points signalés » s'il n'y en a pas)
   - aucune autre annotation.

5. **Dessiner (partie `bpmndi`)** : une forme `BPMNShape` par participant, couloir, élément et annotation ; une `BPMNEdge` par flux et par association. Règles de mise en page :
   - lecture de gauche à droite ; chaque élément est placé dans une colonne selon son rang depuis le début (début = colonne 0, suivant = colonne 1…) ; colonnes espacées de 150 ;
   - un couloir = une rangée horizontale de 150 de haut (plus haute si plusieurs éléments partagent la même colonne dans le couloir : les empiler verticalement) ;
   - participant interne : bande d'en-tête de 30 à gauche ; ses couloirs sont empilés sans espace ;
   - participants externes : bande de 100 de haut, au-dessus du participant interne (espace de 50) ;
   - tailles : tâche et sous-processus 100 × 80 ; événement 36 × 36 ; passerelle 50 × 50 ; annotation 120 × 50, au-dessus de son élément ;
   - chaque élément est centré verticalement dans son couloir ; aucune forme ne se superpose ;
   - flux : points de passage (`di:waypoint`) du bord droit de la source au bord gauche de la cible, avec un coude à angle droit si les hauteurs diffèrent ; flux de message vertical entre l'élément et le bord du participant externe ;
   - sur les passerelles exclusives : `isMarkerVisible="true"` ; sur les participants et couloirs : `isHorizontal="true"`.

6. **Contrôle final avant de rendre le fichier** :
   - chaque ID du tableau est présent une seule fois dans le fichier, et aucun élément en plus (hors annotations) ;
   - chaque `sourceRef`, `targetRef`, `flowNodeRef`, `processRef` et `bpmnElement` pointe vers un `id` qui existe ;
   - tous les `id` sont uniques ; chaque élément du modèle a sa forme ou son trait dans le dessin ;
   - le XML est bien formé (balises fermées, caractères `&`, `<`, `"` échappés dans les libellés).

## Quand le tableau a un problème
- Type BPMN inconnu, élément suivant qui n'existe pas, lien vers un autre participant noté comme flux de séquence → **ne pas corriger en silence** : produire tout le reste et lister l'anomalie après le fichier (« Anomalies du tableau non corrigées »).
- Diagramme très grand → garder la mise en page simple et rappeler qu'un réalignement manuel dans Camunda est attendu.

## Règles
- Toujours : un élément par ligne du tableau, ni plus ni moins (sauf annotations)
- Toujours : garder les libellés exacts du tableau (termes du client et termes SAP compris)
- Toujours : produire le fichier même s'il reste des questions bloquantes
- Jamais : inventer, renommer, fusionner ou supprimer un élément
- Jamais : envoyer, partager ou déposer le fichier ailleurs que là où on me le demande

## Format de la sortie
- **Si l'outil peut créer des fichiers** : écrire le fichier `.bpmn` au chemin demandé (sinon `processus-as-is.bpmn`) et donner son emplacement.
- **Plan de secours, si l'outil ne peut pas créer de fichier** : afficher le XML complet dans un seul bloc de code, du `<?xml` jusqu'à `</bpmn:definitions>`, sans rien couper, puis écrire : « Copiez tout ce bloc dans un fichier texte, enregistrez-le avec l'extension `.bpmn`, puis ouvrez-le dans Camunda Modeler. »
- Dans les deux cas, ajouter ensuite : nombre d'éléments, de flux et d'annotations ; la liste des anomalies non corrigées (ou « Aucune »).
