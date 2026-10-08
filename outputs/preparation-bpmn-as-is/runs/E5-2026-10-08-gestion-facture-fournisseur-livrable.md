## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | — | Fournisseur | Participant externe | — | Message « Facture papier » → EV1 ; Message « Facture e-mail » → EV2 ; Message « Avoir » → SP1 | Notes atelier § Explication générale, puces 1 et 4 — Responsable comptabilité fournisseurs | Confirmé |
| P2 | — | Responsable budget | Participant externe | — | Message « Validation » → SP2 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs ; § Questions posées, Q2 — Responsable comptabilité fournisseurs | Confirmé |
| EV1 | Gestion facture fournisseur / Accueil | Facture papier | Début message | — | T1 | Notes atelier § Explication générale, puce 1 — Responsable comptabilité fournisseurs | Confirmé |
| T1 | Gestion facture fournisseur / Accueil | Scanner facture papier | Tâche manuelle | — | T2 | Notes atelier § Explication générale, puce 2 — Responsable comptabilité fournisseurs | Confirmé |
| T2 | Gestion facture fournisseur / Accueil | Déposer facture dans boîte factures@ | Tâche utilisateur | — | G1 | Notes atelier § Explication générale, puce 2 — Responsable comptabilité fournisseurs | Confirmé |
| EV2 | Gestion facture fournisseur / Comptable fournisseurs | Facture e-mail | Début message | — | G1 | Notes atelier § Explication générale, puce 1 — Responsable comptabilité fournisseurs | Confirmé |
| G1 | Gestion facture fournisseur / Comptable fournisseurs | — | Passerelle exclusive | — | T3 | Déduit de Notes atelier § Explication générale, puces 1 et 2 — Responsable comptabilité fournisseurs | Supposé |
| T3 | Gestion facture fournisseur / Comptable fournisseurs | Rechercher commande d'achat SAP | Tâche utilisateur | — | G2 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs | Confirmé |
| G2 | Gestion facture fournisseur / Comptable fournisseurs | Commande d'achat associée ? | Passerelle exclusive | T4 : OUI ; T8 : NON | T4 ; T8 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs | Confirmé |
| T4 | Gestion facture fournisseur / Comptable fournisseurs | Saisir facture avec commande (MIRO) | Tâche utilisateur | — | T5 | Notes atelier § Explication générale, puce 3 (facture avec commande) — Responsable comptabilité fournisseurs | Confirmé |
| T5 | Gestion facture fournisseur / Comptable fournisseurs | Contrôler écarts quantités et prix | Tâche service | — | G3 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| G3 | Gestion facture fournisseur / Comptable fournisseurs | Écart au-delà de la tolérance ? | Passerelle exclusive | T6 : OUI ; G4 : NON | T6 ; G4 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs ; § Questions posées, Q1 — Comptable fournisseurs | Confirmé |
| T6 | Gestion facture fournisseur / Comptable fournisseurs | Bloquer facture au paiement | Tâche service | — | SP1 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| SP1 | Gestion facture fournisseur / Comptable fournisseurs | Gestion litige | Sous-processus | — | T7 ; Message « Demande de vérification » → P1 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs ; Transcription Teams — Acheteur, Comptable fournisseurs | Confirmé |
| T7 | Gestion facture fournisseur / Comptable fournisseurs | Lever blocage facture | Tâche utilisateur | — | G4 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| T8 | Gestion facture fournisseur / Comptable fournisseurs | Saisir facture sans commande (FB60) | Tâche utilisateur | — | SP2 | Notes atelier § Explication générale, puce 3 (facture sans commande) — Responsable comptabilité fournisseurs | Confirmé |
| SP2 | Gestion facture fournisseur / Comptable fournisseurs | Validation facture sans commande | Sous-processus | — | G4 ; Message « Facture à valider » → P2 ; Message « Relance » → P2 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs ; § Questions posées, Q2 — Responsable comptabilité fournisseurs | Confirmé |
| G4 | Gestion facture fournisseur / Comptable fournisseurs | — | Passerelle exclusive | — | M1 | Déduit de Notes atelier § Explication générale, puce 5 — Responsable comptabilité fournisseurs | Supposé |
| M1 | Gestion facture fournisseur / Trésorerie | Mardi et jeudi | Minuterie intermédiaire | — | T9 | Notes atelier § Explication générale, puce 5 — Responsable comptabilité fournisseurs | Confirmé |
| T9 | Gestion facture fournisseur / Trésorerie | Lancer proposition de paiement | Tâche utilisateur | — | T10 | Notes atelier § Explication générale, puce 5 — Responsable comptabilité fournisseurs | Confirmé |
| T10 | Gestion facture fournisseur / Trésorerie | Contrôler proposition de paiement | Tâche utilisateur | — | G5 | Notes atelier § Explication générale, puce 6 — Responsable comptabilité fournisseurs | Confirmé |
| G5 | Gestion facture fournisseur / Trésorerie | Montant au-dessus du seuil DAF ? | Passerelle exclusive | T12 : OUI ; T11 : NON | T12 ; T11 | Transcription Teams — Responsable trésorerie (50 000) ; Responsable comptabilité fournisseurs (« je crois » 100 000) | À préciser |
| T11 | Gestion facture fournisseur / Trésorerie | Lancer paiement par virement | Tâche utilisateur | — | G6 | Notes atelier § Explication générale, puce 6 — Responsable comptabilité fournisseurs | Confirmé |
| T12 | Gestion facture fournisseur / DAF | Signer virement | Tâche utilisateur | — | G6 | Transcription Teams — Responsable trésorerie | Confirmé |
| G6 | Gestion facture fournisseur / Trésorerie | — | Passerelle exclusive | — | F1 | Déduit de Transcription Teams — Responsable trésorerie | Supposé |
| F1 | Gestion facture fournisseur / Trésorerie | Facture payée | Fin | — | — | Déduit de Notes atelier, objet de l'atelier et § Explication générale, puce 6 — Responsable comptabilité fournisseurs | Supposé |

### Détail de SP1

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| EV3 | Gestion facture fournisseur / Comptable fournisseurs | — | Début | — | T13 | Déduit de Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Supposé |
| T13 | Gestion facture fournisseur / Comptable fournisseurs | Informer acheteur du blocage | Tâche utilisateur | — | T14 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs ; Transcription Teams — Acheteur (« par mail, pas de workflow dans SAP ») | Confirmé |
| T14 | Gestion facture fournisseur / Acheteur | Vérifier écart avec fournisseur | Tâche envoi | — | G7 ; Message « Demande de vérification » → P1 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| G7 | Gestion facture fournisseur / Acheteur | Correction de la commande ? | Passerelle exclusive | T15 : OUI ; EV4 : NON | T15 ; EV4 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| T15 | Gestion facture fournisseur / Acheteur | Corriger commande | Tâche utilisateur | — | G8 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| EV4 | Gestion facture fournisseur / Comptable fournisseurs | Avoir | Message reçu | — | G8 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| G8 | Gestion facture fournisseur / Comptable fournisseurs | — | Passerelle exclusive | — | F2 | Déduit de Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Supposé |
| F2 | Gestion facture fournisseur / Comptable fournisseurs | Écart résolu | Fin | — | — | Déduit de Notes atelier § Explication générale, puce 4 (« une fois l'écart résolu ») — Responsable comptabilité fournisseurs | Supposé |

### Détail de SP2

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| EV5 | Gestion facture fournisseur / Comptable fournisseurs | — | Début | — | T16 | Déduit de Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs | Supposé |
| T16 | Gestion facture fournisseur / Comptable fournisseurs | Envoyer facture au responsable budget | Tâche envoi | — | G9 ; Message « Facture à valider » → P2 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs | Confirmé |
| G9 | Gestion facture fournisseur / Comptable fournisseurs | — | Passerelle basée sur les événements | — | EV6 ; M2 | Déduit de Notes atelier § Questions posées, Q2 — Responsable comptabilité fournisseurs | Supposé |
| EV6 | Gestion facture fournisseur / Comptable fournisseurs | Validation | Message reçu | — | F3 | Déduit de Notes atelier § Explication générale, puces 3 et 5 — Responsable comptabilité fournisseurs | Supposé |
| F3 | Gestion facture fournisseur / Comptable fournisseurs | Facture validée | Fin | — | — | Déduit de Notes atelier § Explication générale, puce 5 (« factures validées ») — Responsable comptabilité fournisseurs | Supposé |
| M2 | Gestion facture fournisseur / Comptable fournisseurs | 1 semaine | Minuterie intermédiaire | — | T17 | Notes atelier § Questions posées, Q2 — Responsable comptabilité fournisseurs | Confirmé |
| T17 | Gestion facture fournisseur / Comptable fournisseurs | Relancer responsable budget | Tâche envoi | — | AP1 ; Message « Relance » → P2 | Notes atelier § Questions posées, Q2 — Responsable comptabilité fournisseurs | Confirmé |
| AP1 | Gestion facture fournisseur / Comptable fournisseurs | À préciser — voir question Q7 | Fin | — | — | Notes atelier § Questions posées, Q2 (« après… ça dépend des gens ») — Responsable comptabilité fournisseurs | À préciser |

## 2. Questions par interlocuteur

### Comptable fournisseurs
- Q1 — [G3] — À confirmer — La tolérance avant blocage est-elle bien de 2 % sur le prix et nulle sur les quantités dans le paramétrage SAP ?
- Q2 — [T3] [G2] — À confirmer — Si le numéro de commande ne figure pas sur la facture, la traitez-vous comme une facture sans commande ?
- Q3 — [T4] — À confirmer — Que faites-vous si l'entrée de marchandises n'est pas encore enregistrée dans SAP au moment de la saisie MIRO ?
- Q4 — [SP1] [T13] — À confirmer — Au bout de combien de jours relancez-vous l'acheteur quand une facture reste bloquée, et combien de relances faites-vous au maximum ?
- Q5 — [EV4] — À confirmer — L'avoir du fournisseur arrive-t-il dans la boîte factures@ et est-ce vous qui le saisissez dans SAP ?
- Q6 — [T7] — À confirmer — Après correction de la commande ou saisie de l'avoir, SAP refait-il le rapprochement avant que vous leviez le blocage ?

### Responsable comptabilité fournisseurs
- Q7 — [AP1] [SP2] — Bloquant pour la modélisation — Si le responsable budget ne répond toujours pas après la relance d'une semaine, existe-t-il une règle commune (nouvelle relance, escalade vers un autre responsable, autre) ?
- Q8 — [SP2] — À confirmer — Le responsable budget peut-il refuser une facture sans commande, et si oui, que devient-elle ?
- Q9 — [T8] [SP2] — À confirmer — Une facture saisie en FB60 est-elle bloquée au paiement tant que le responsable budget ne l'a pas validée ?
- Q10 — [EV1] [T1] [T2] — À confirmer — Une fois déposées dans la boîte factures@, les factures papier scannées sont-elles traitées exactement comme celles reçues par e-mail ?

### Acheteur
- Q11 — [SP1] — Bloquant pour la modélisation — Une facture bloquée peut-elle être payée sans que l'écart soit résolu, et si oui, qui le décide ?
- Q12 — [T14] — À confirmer — Contactez-vous le fournisseur par e-mail ou par téléphone pour vérifier l'écart ?
- Q13 — [G7] — À confirmer — Le choix entre corriger la commande et obtenir un avoir dépend-il uniquement de la réponse du fournisseur ?

### Responsable trésorerie
- Q14 — [G5] — Bloquant pour la modélisation — Le seuil au-delà duquel le DAF signe le virement est-il aujourd'hui de 50 000 € ou de 100 000 € ?
- Q15 — [G5] — À confirmer — Ce seuil s'applique-t-il au montant d'une facture ou au montant total d'un virement ?
- Q16 — [T11] [T12] — À confirmer — Au-dessus du seuil, la trésorerie prépare-t-elle le virement avant la signature du DAF, puis le lance-t-elle après ?
- Q17 — [T10] — À confirmer — Que se passe-t-il si vous relevez une anomalie lors du contrôle de la proposition de paiement ?
- Q18 — [T12] — À confirmer — Le DAF signe-t-il le virement dans l'outil bancaire, dans SAP ou sur papier ?

### Interlocuteur à identifier
- Q19 — [F1] — À confirmer — Le processus à cartographier s'arrête-t-il au lancement du virement, ou comprend-il des étapes après le paiement (avis de paiement au fournisseur, rapprochement bancaire) ?

## 3. Points signalés

- Sources séparées en deux parties : notes Word de la consultante (C1) et extrait de transcription Teams (C3) ; aucun PDF du client (C2).
- Aucun nom de personne repéré : les intervenants sont désignés par leur fonction (« DAF » est une fonction).
- Aucune consigne adressée à l'IA repérée dans les sources.
- C4 est un brouillon v0.1 : sur les sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation de SAP, position des participants externes), le style des modèles C5 / C6 a été suivi.
- [G5] Contradiction sur le seuil de signature du DAF : 50 000 selon la responsable trésorerie, « 100 000 maintenant, je crois » selon la responsable comptabilité ; élément mis « À préciser » (voir Q14).
- [G5] Montants cités sans devise dans la transcription : « € » ajouté seulement dans la question Q14, à confirmer.
- La transcription Teams est générée automatiquement : les chiffres qu'elle contient (50 000, 100 000) sont à vérifier.
- [G3] Tolérance d'écart (2 % prix, 0 quantité) donnée avec réserve (« je crois, à vérifier dans le paramétrage ») : non reprise dans le libellé, à confirmer (voir Q1).
- [SP1] Écart pratique / outil : le blocage est géré par SAP, mais l'échange avec l'acheteur se fait par mail, sans workflow SAP ; la pratique par mail a été gardée.
- [SP1] [T13] Relances de l'acheteur (« deux trois fois ») bien réelles mais non modélisées en minuterie : le délai n'est pas connu (voir Q4).
- [SP1] Cas « facture en litige payée quand même » évoqué mais sans réponse (acheteur parti) : aucune branche ajoutée (voir Q11).
- [SP1] Sous-processus proposé « Gestion litige », repris du modèle C5 (et « Gestion contentieux » de C6) : à garder ou non ; détail dans « Détail de SP1 ».
- [SP2] Sous-processus proposé « Validation facture sans commande » (suite d'au moins 4 éléments formant un tout, sur le modèle de « Validation d'un emprunt » de C5) : à garder ou non ; détail dans « Détail de SP2 ».
- [SP2] [AP1] Fin « À préciser » ajoutée : la suite après la relance d'une semaine n'est pas définie (« ça dépend des gens ») (voir Q7) ; elle est visible seulement dans le détail de SP2, pas dans le fichier `.bpmn`.
- [P2] Le responsable budget est un rôle interne à l'entreprise, mais il a été modélisé en participant externe pour représenter les échanges par mail (envoi, relance, validation) : à garder ou à remplacer par un couloir.
- [P1] [SP1] Le message « Demande de vérification » vers le fournisseur porte un nom proposé : le canal et l'objet exact ne sont pas connus (voir Q12).
- [EV4] Le destinataire de l'avoir du fournisseur n'est pas dit : placé dans le couloir de la comptable fournisseurs (voir Q5).
- [T7] On ne sait pas si SAP refait le rapprochement après correction ou avoir (voir Q6).
- [G1] [G4] [G6] Supposé : passerelles de convergence déduites de « même boîte mail », « factures validées et non bloquées » et des deux façons de signer le virement.
- [F1] Supposé : nom de fin « Facture payée » déduit de l'objet de l'atelier (« de sa réception à son paiement ») ; frontière de fin à confirmer (voir Q19).
- [EV3] [G8] [F2] [EV5] [G9] [EV6] [F3] Supposé : début, fin et passerelles des sous-processus déduits de ce qui a été décrit.
- [M1] Minuterie « Mardi et jeudi » : c'est un calendrier et non une durée ; libellé gardé tel que dit par le client.
- [T12] Type « Tâche utilisateur » retenu pour la signature du DAF sans savoir l'outil utilisé (voir Q18) ; ordre entre préparation et signature du virement incertain (voir Q16).
- [T10] Aucune branche « anomalie » après le contrôle de la proposition de paiement : non évoquée en atelier (voir Q17).
- [T1] Type « Tâche manuelle » pour le scan (action physique) ; l'accueil n'était pas présent à l'atelier (voir Q10).
- Information hors flux : la trésorerie ne voit pas les factures bloquées, seulement la proposition de paiement ; noté, sans élément ajouté.
- Couloir « Acheteur » présent seulement dans le détail de SP1 : il n'apparaît pas dans le fichier `.bpmn` (sous-processus replié).
- Fichier `.bpmn` : aucune anomalie signalée par la génération ; les flux de message de SP1 et SP2 partent du sous-processus replié ; réalignement manuel attendu dans Camunda.
