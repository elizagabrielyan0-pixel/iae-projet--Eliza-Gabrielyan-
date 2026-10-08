> ⚠️ Alerte : deux seuils différents ont été cités dans la transcription Teams pour la signature du virement par le DAF (50 000 par le responsable trésorerie, 100 000 « je crois » par le responsable comptabilité fournisseurs), sans devise. Rien n'a été tranché : [G5] est « À préciser » (questions Q18 et Q19).
> ⚠️ Alerte : 7 informations manquent pour finir le diagramme (questions Q3, Q4, Q8, Q12, Q15, Q18, Q22). Elles apparaissent en « À préciser » dans le fichier BPMN sur [SP1], [SP2] et [G5] ; le trou de Q22 ([T9]) n'est visible que dans ce livrable.
> ⚠️ Alerte : le fichier `.bpmn` a été produit avec 1 anomalie : la minuterie [EV3] « Mardi et jeudi » n'a pas de durée chiffrée et reste sans durée dans le fichier, à compléter dans Camunda (question Q20).

## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Fournisseur | Fournisseur | Participant externe | — | Message « Facture par e-mail » → EV1 ; Message « Facture par courrier » → EV2 ; Message « Avoir » → SP1 | Notes atelier § Explication générale, puces 1 et 4 — Responsable comptabilité fournisseurs | Confirmé |
| EV1 | Gestion facture fournisseur / Comptable fournisseurs | Facture reçue par e-mail | Début message | — | G1 | Notes atelier § Explication générale, puce 1 — Responsable comptabilité fournisseurs (« par e-mail sur la boîte factures@, la grande majorité, en PDF ») | Confirmé |
| EV2 | Gestion facture fournisseur / Accueil | Facture reçue par courrier | Début message | — | T1 | Notes atelier § Explication générale, puces 1 et 2 — Responsable comptabilité fournisseurs (« par courrier, de moins en moins ») | Confirmé |
| T1 | Gestion facture fournisseur / Accueil | Scanner facture papier | Tâche manuelle | — | T2 | Notes atelier § Explication générale, puce 2 — Responsable comptabilité fournisseurs | Confirmé |
| T2 | Gestion facture fournisseur / Accueil | Déposer facture scannée dans boîte factures@ | Tâche utilisateur | — | G1 | Notes atelier § Explication générale, puce 2 — Responsable comptabilité fournisseurs (« puis déposées dans la même boîte mail ») | Confirmé |
| G1 | Gestion facture fournisseur / Comptable fournisseurs | — | Passerelle exclusive | — | T3 | Déduit de Notes atelier § Explication générale, puces 1 et 2 — Responsable comptabilité fournisseurs (les deux canaux aboutissent à la même boîte) | Supposé |
| T3 | Gestion facture fournisseur / Comptable fournisseurs | Rechercher commande d'achat SAP associée | Tâche utilisateur | — | G2 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs (« ouvre chaque facture et cherche s'il y a une commande d'achat SAP associée ») | Confirmé |
| G2 | Gestion facture fournisseur / Comptable fournisseurs | Commande d'achat associée ? | Passerelle exclusive | T4 : OUI ; T7 : NON | T4 ; T7 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs (« Facture avec commande… Facture sans commande… ») | Confirmé |
| T4 | Gestion facture fournisseur / Comptable fournisseurs | Saisir facture dans MIRO avec rapprochement commande et entrée de marchandises | Tâche utilisateur | — | T5 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs | Confirmé |
| T5 | Gestion facture fournisseur / Comptable fournisseurs | Contrôler écarts quantités et prix | Tâche service | — | G3 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs (contrôle fait par SAP « lors du rapprochement ») | Confirmé |
| G3 | Gestion facture fournisseur / Comptable fournisseurs | Écart au-delà de la tolérance ? | Passerelle exclusive | T6 : OUI ; G4 : NON | T6 ; G4 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs ; § Questions posées — Comptable fournisseurs (« 2 % sur le prix, je crois, et aucune sur les quantités. À vérifier dans le paramétrage ») | Non confirmé |
| T6 | Gestion facture fournisseur / Comptable fournisseurs | Bloquer facture au paiement | Tâche service | — | SP1 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs (« SAP bloque la facture au paiement ») | Confirmé |
| SP1 | Gestion facture fournisseur / Comptable fournisseurs | Gestion écart facture | Sous-processus | — | G4 ; Message « Demande de vérification » → P1 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs ; Transcription Teams — Acheteur, Comptable fournisseurs ; § Questions posées (réponse non obtenue) | À préciser |
| T7 | Gestion facture fournisseur / Comptable fournisseurs | Saisir facture dans FB60 | Tâche utilisateur | — | SP2 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs (« frais généraux, abonnements… ») | Confirmé |
| SP2 | Gestion facture fournisseur / Comptable fournisseurs | Validation facture sans commande | Sous-processus | — | G4 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs ; § Questions posées — Responsable comptabilité fournisseurs | À préciser |
| G4 | Gestion facture fournisseur / Comptable fournisseurs | — | Passerelle exclusive | — | EV3 | Déduit de Notes atelier § Explication générale, puce 5 — Responsable comptabilité fournisseurs (« Les factures validées et non bloquées partent dans la proposition de paiement ») | Supposé |
| EV3 | Gestion facture fournisseur / Trésorerie | Mardi et jeudi | Minuterie intermédiaire | — | T8 | Notes atelier § Explication générale, puce 5 — Responsable comptabilité fournisseurs (« deux fois par semaine, mardi et jeudi ») | Confirmé |
| T8 | Gestion facture fournisseur / Trésorerie | Lancer proposition de paiement | Tâche utilisateur | — | T9 | Notes atelier § Explication générale, puce 5 — Responsable comptabilité fournisseurs | Confirmé |
| T9 | Gestion facture fournisseur / Trésorerie | Contrôler proposition de paiement | Tâche utilisateur | — | G5 | Notes atelier § Explication générale, puce 6 — Responsable comptabilité fournisseurs | Confirmé |
| G5 | Gestion facture fournisseur / Trésorerie | Montant au-dessus du seuil DAF ? | Passerelle exclusive | T10 : OUI ; T11 : NON | T10 ; T11 | Transcription Teams — Responsable trésorerie (« au-dessus de 50 000, c'est le DAF qui signe le virement ») ; Transcription Teams — Responsable comptabilité fournisseurs (« je crois que c'est 100 000 maintenant le seuil, non ? Il faudrait vérifier ») | À préciser |
| T10 | Gestion facture fournisseur / DAF | Signer virement | Tâche utilisateur | — | G6 | Transcription Teams — Responsable trésorerie (« c'est le DAF qui signe le virement, pas nous ») | Confirmé |
| T11 | Gestion facture fournisseur / Trésorerie | Lancer paiement par virement | Tâche utilisateur | — | G6 | Notes atelier § Explication générale, puce 6 — Responsable comptabilité fournisseurs ; Transcription Teams — Responsable trésorerie | Confirmé |
| G6 | Gestion facture fournisseur / Trésorerie | — | Passerelle exclusive | — | F1 | Déduit de Notes atelier § Explication générale, puce 6 — Responsable comptabilité fournisseurs ; Transcription Teams — Responsable trésorerie | Supposé |
| F1 | Gestion facture fournisseur / Trésorerie | Virement lancé | Fin | — | — | Déduit de Notes atelier § Explication générale, puce 6 — Responsable comptabilité fournisseurs (« lance le paiement par virement ») | Supposé |

### Détail de SP1

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP1-EV1 | Gestion facture fournisseur / Comptable fournisseurs | — | Début | — | SP1-T1 | Déduit de Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Supposé |
| SP1-T1 | Gestion facture fournisseur / Comptable fournisseurs | Informer acheteur du blocage par mail | Tâche utilisateur | — | SP1-T2 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs ; Transcription Teams — Acheteur (« je reçois juste un mail de la compta, il n'y a pas de workflow dans SAP ») | Confirmé |
| SP1-T2 | Gestion facture fournisseur / Acheteur | Vérifier écart avec fournisseur | Tâche envoi | — | SP1-G1 ; Message « Demande de vérification » → P1 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs (« l'acheteur vérifie avec le fournisseur ») | Confirmé |
| SP1-G1 | Gestion facture fournisseur / Acheteur | Mode de résolution de l'écart ? | Passerelle exclusive | SP1-T3 : Correction commande ; SP1-EV2 : Avoir fournisseur | SP1-T3 ; SP1-EV2 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs (« Soit l'acheteur corrige la commande, soit le fournisseur envoie un avoir ») | Confirmé |
| SP1-T3 | Gestion facture fournisseur / Acheteur | Corriger commande | Tâche utilisateur | — | SP1-G2 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Confirmé |
| SP1-EV2 | Gestion facture fournisseur / Comptable fournisseurs | Avoir | Message reçu | — | SP1-G2 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs ; destinataire de l'avoir non dit | À préciser |
| SP1-G2 | Gestion facture fournisseur / Comptable fournisseurs | — | Passerelle exclusive | — | SP1-T4 | Déduit de Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs (« Une fois l'écart résolu ») | Supposé |
| SP1-T4 | Gestion facture fournisseur / Comptable fournisseurs | Lever blocage facture | Tâche utilisateur | — | SP1-F1 | Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs (« la comptable lève le blocage ») | Confirmé |
| SP1-F1 | Gestion facture fournisseur / Comptable fournisseurs | Écart résolu | Fin | — | — | Déduit de Notes atelier § Explication générale, puce 4 — Responsable comptabilité fournisseurs | Supposé |

### Détail de SP2

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP2-EV1 | Gestion facture fournisseur / Comptable fournisseurs | — | Début | — | SP2-T1 | Déduit de Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs | Supposé |
| SP2-T1 | Gestion facture fournisseur / Comptable fournisseurs | Envoyer facture par mail au responsable budget | Tâche utilisateur | — | SP2-G1 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs (« l'envoie par mail au responsable du budget concerné pour validation ») | Confirmé |
| SP2-G1 | Gestion facture fournisseur / Comptable fournisseurs | Réponse du responsable budget ? | Passerelle exclusive | SP2-T2 : OUI ; SP2-EV2 : NON | SP2-T2 ; SP2-EV2 | Déduit de Notes atelier § Questions posées — Responsable comptabilité fournisseurs (« Et si le responsable budget ne répond pas… on relance au bout d'une semaine ») | Supposé |
| SP2-T2 | Gestion facture fournisseur / Responsable budget | Valider facture | Tâche utilisateur | — | SP2-F1 | Notes atelier § Explication générale, puce 3 — Responsable comptabilité fournisseurs (« pour validation ») | Confirmé |
| SP2-F1 | Gestion facture fournisseur / Responsable budget | Facture validée | Fin | — | — | Déduit de Notes atelier § Explication générale, puce 5 — Responsable comptabilité fournisseurs (« Les factures validées… ») | Supposé |
| SP2-EV2 | Gestion facture fournisseur / Comptable fournisseurs | 1 semaine | Minuterie intermédiaire | — | SP2-T3 | Notes atelier § Questions posées — Responsable comptabilité fournisseurs (« on relance au bout d'une semaine ») | Confirmé |
| SP2-T3 | Gestion facture fournisseur / Comptable fournisseurs | Relancer responsable budget | Tâche utilisateur | — | SP2-F2 | Notes atelier § Questions posées — Responsable comptabilité fournisseurs | Confirmé |
| SP2-F2 | Gestion facture fournisseur / Comptable fournisseurs | À préciser — voir question Q3 | Fin | — | — | Notes atelier § Questions posées — Responsable comptabilité fournisseurs (« Après… honnêtement ça dépend des gens ») | À préciser |

## 2. Questions par interlocuteur

### Responsable comptabilité fournisseurs
- Q1 — [EV1] [EV2] — À confirmer — Les factures arrivent-elles uniquement par la boîte « factures@ » et par courrier, sans autre canal (portail fournisseur, EDI) ?
- Q2 — [T2] — À confirmer — L'accueil dépose-t-il la facture scannée dans la boîte « factures@ » en l'envoyant par mail ?
- Q3 — [SP2] [SP2-F2] — Bloquant pour la modélisation — Que se passe-t-il lorsque le responsable budget ne répond toujours pas après la relance d'une semaine ?
- Q4 — [SP2] [SP2-T2] — Bloquant pour la modélisation — Le responsable budget peut-il refuser une facture sans commande et, si oui, que devient-elle ?
- Q5 — [SP2] [SP2-T2] — À confirmer — Le responsable budget donne-t-il sa validation par retour de mail ?
- Q6 — [SP2] [SP2-EV2] — À confirmer — Le délai d'une semaine avant relance est-il compté à partir de l'envoi du mail au responsable budget ?
- Q7 — [T7] — À confirmer — Une facture saisie dans FB60 reste-t-elle bloquée au paiement tant que le responsable budget ne l'a pas validée ?
- Q8 — [SP1] [SP1-EV2] — Bloquant pour la modélisation — Qui reçoit l'avoir envoyé par le fournisseur, et qui l'enregistre dans SAP ?

### Comptable fournisseurs
- Q9 — [T3] [G2] — À confirmer — Une facture sans numéro de commande est-elle toujours saisie dans FB60, même si une commande existe dans SAP ?
- Q10 — [G3] — À confirmer — Pouvez-vous confirmer dans le paramétrage SAP que la tolérance est de 2 % sur le prix et nulle sur les quantités ?
- Q11 — [T5] [T6] — À confirmer — Le contrôle des écarts et le blocage au paiement sont-ils faits automatiquement par SAP au moment de la saisie dans MIRO ?
- Q12 — [SP1] [SP1-T1] — Bloquant pour la modélisation — Au bout de combien de jours relancez-vous l'acheteur, et que se passe-t-il si l'écart reste sans réponse après plusieurs relances ?
- Q13 — [SP1] [SP1-G2] — À confirmer — Comment apprenez-vous que l'écart est résolu (mail de l'acheteur, réception de l'avoir, autre) ?
- Q14 — [SP1] [SP1-T4] — À confirmer — Levez-vous le blocage vous-même dans SAP, et avec quelle transaction ?

### Acheteur
- Q15 — [SP1] — Bloquant pour la modélisation — Une facture en litige peut-elle être payée sans que l'écart soit résolu et, si oui, qui le décide ?
- Q16 — [SP1] [SP1-G1] — À confirmer — Qui choisit entre la correction de la commande et la demande d'un avoir, et selon quel critère ?
- Q17 — [SP1] [SP1-T2] — À confirmer — Contactez-vous le fournisseur par mail, par téléphone ou par un autre moyen, et comment sa réponse vous parvient-elle ?

### Responsable trésorerie
- Q18 — [G5] — Bloquant pour la modélisation — Le seuil au-dessus duquel le DAF signe le virement est-il de 50 000 ou de 100 000 (les deux montants ont été cités en atelier) ?
- Q19 — [G5] — À confirmer — Ce seuil s'applique-t-il au montant d'une facture ou au montant total d'un virement, et dans quelle devise ?
- Q20 — [EV3] — À confirmer — La proposition de paiement est-elle lancée chaque mardi et chaque jeudi, et reprend-elle toutes les factures validées et non bloquées ou seulement celles arrivées à échéance ?
- Q21 — [T8] — À confirmer — Quelle transaction SAP utilisez-vous pour lancer la proposition de paiement ?
- Q22 — [T9] — Bloquant pour la modélisation — Si le contrôle de la proposition révèle une anomalie, que se passe-t-il (facture retirée, proposition relancée, autre) ?
- Q23 — [T10] [T11] — À confirmer — Lorsque le DAF a signé le virement, la trésorerie a-t-elle encore une étape à faire pour lancer le paiement ?
- Q24 — [F1] — À confirmer — Le processus s'arrête-t-il au lancement du virement, ou le suivi du paiement (relevé bancaire, lettrage) fait-il partie du périmètre ?

## 3. Points signalés

- Aucun nom de personne repéré dans les sources : seules des fonctions apparaissent.
- Aucune consigne adressée à l'IA repérée dans les sources (notes de la consultante et transcription Teams).
- Aucune valeur absurde repérée ; seule une contradiction de seuil ([G5]) et une devise absente ont été relevées.
- La fiche de conventions C4 est présente (brouillon v0.1) ; pour ses sections « À compléter par l'équipe » (représentation de SAP, position des participants externes), le style des modèles C5 / C6 a été suivi : SAP n'a pas de couloir, il apparaît dans les libellés et dans les tâches de service [T5] [T6].
- Aucune procédure écrite ni PDF du client dans les sources : aucun écart pratique / procédure à relever.
- La transcription Teams est générée automatiquement : les montants cités (50 000, 100 000) sont à relire avec prudence.
- [G5] Contradiction : le responsable trésorerie cite 50 000, le responsable comptabilité fournisseurs pense que c'est 100 000 (« il faudrait vérifier ») ; aucune devise n'est donnée ; élément mis « À préciser » (Q18, Q19).
- [G3] Non confirmé : la tolérance (2 % sur le prix, aucune sur les quantités) a été donnée avec « je crois » et « à vérifier dans le paramétrage » (Q10).
- [SP1] Question restée sans réponse en atelier (l'acheteur avait quitté l'atelier) : qui décide si une facture en litige est payée quand même ; la branche manque (Q15).
- [SP1] Sous-processus proposé « Gestion écart facture » (9 éléments au détail), sur le modèle de « Gestion contentieux » (C6) et de l'exemple « Gestion litige » (C4) : à garder ou non.
- [SP1] Placé dans le couloir « Comptable fournisseurs », où commence son détail ; le couloir « Acheteur » n'apparaît donc que dans le détail, pas dans le fichier `.bpmn`.
- [SP1] Statut « À préciser » repris de son détail [SP1-EV2] et de la branche manquante (Q8, Q12, Q15) ; les messages « Demande de vérification » et « Avoir » partent de / arrivent sur [SP1] dans le fichier, et sur [SP1-T2] / [SP1-EV2] dans le détail.
- [SP1-T1] Pratique réelle : l'acheteur est prévenu par mail, sans workflow SAP, et la comptable le relance « deux trois fois » ; ces relances ne sont pas modélisées faute de délai et d'issue connus (Q12).
- [SP1-T2] L'acheteur, rôle interne joint par mail, agit dans son propre couloir ; la réponse du fournisseur à l'acheteur n'a pas été décrite, seul le message vers le fournisseur est modélisé (Q17).
- [SP1-EV2] Placé par défaut dans le couloir « Comptable fournisseurs » ; le destinataire de l'avoir n'a pas été dit (Q8).
- [SP2] Sous-processus proposé « Validation facture sans commande » (8 éléments au détail), car l'envoi, la validation et la relance forment un tout : à garder ou non.
- [SP2] Placé dans le couloir « Comptable fournisseurs », où commence son détail ; le couloir « Responsable budget » n'apparaît donc que dans le détail, pas dans le fichier `.bpmn`.
- [SP2] Statut « À préciser » repris de son détail [SP2-F2] ; une branche « refus » éventuelle n'est pas modélisée (Q4).
- [SP2-T2] La validation du responsable budget, rôle interne joint par mail, est une tâche dans son couloir, pas un message reçu.
- [SP2-G1] Supposé : la décision « réponse ou non » découle de « si le responsable budget ne répond pas… on relance au bout d'une semaine » ; dans Camunda, la minuterie [SP2-EV2] pourra devenir une minuterie attachée à la tâche [SP2-T2].
- [SP2-F2] Ce qui se passe après la relance du responsable budget n'est pas connu (« ça dépend des gens ») : élément « À préciser — voir question Q3 ».
- [G1] [G4] [G6] Supposé : passerelles de convergence déduites des branches décrites, non nommées selon C4.
- [F1] Supposé : la fin « Virement lancé » reprend l'état atteint à la dernière étape décrite, sans avoir été nommée en atelier ; la frontière du processus est à confirmer (Q24).
- [SP1-EV1] [SP2-EV1] Supposé : débuts non nommés des sous-processus, selon C4.
- [SP1-G2] [SP1-F1] [SP2-F1] Supposé : éléments de structure déduits de « une fois l'écart résolu » et « les factures validées ».
- [EV3] La minuterie porte « Mardi et jeudi » : c'est un calendrier, pas une durée chiffrée, donc sans durée dans le fichier (Q20).
- [T1] Type « Tâche manuelle » retenu pour le scan ; [T2] « Tâche utilisateur » pour le dépôt dans la boîte mail (Q2).
- [T10] Le DAF n'a pas participé à l'atelier ; son rôle a été décrit par le responsable trésorerie (Q23).
- [T9] Le contrôle de la proposition n'a pas de suite décrite en cas d'anomalie (Q22).
- Information sans élément : la trésorerie ne voit pas les factures bloquées, seulement la proposition de paiement (Transcription Teams — Responsable trésorerie).
- Le paiement au fournisseur n'est pas modélisé en message, car ni la banque ni l'envoi au fournisseur n'ont été évoqués (Q24).
- Les noms des messages « Facture par e-mail », « Facture par courrier », « Demande de vérification » et « Avoir » ont été formés d'après l'objet transmis (C4), ils n'ont pas été dits tels quels en atelier.
- Fichier `.bpmn` : le programme `generating-bpmn-files` signale 1 anomalie — [EV3] minuterie « Mardi et jeudi » sans durée chiffrée, laissée sans durée dans le fichier ; à compléter dans Camunda (minuterie de type cycle) une fois le calendrier confirmé.
- Fichier `.bpmn` : un réalignement manuel des flux de message de [SP1] reste possible dans Camunda.
