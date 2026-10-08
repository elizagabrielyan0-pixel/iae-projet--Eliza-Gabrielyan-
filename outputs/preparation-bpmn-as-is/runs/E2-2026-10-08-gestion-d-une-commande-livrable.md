## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Client | Client | Participant externe | — | Message « Commande client » → EV1 ; Message « Confirmation client » → EV3 ; Message « Infirmation client » → EV4 ; Message « Règlement » → EV5 | Notes atelier §Explication générale — Responsable du service commercial ; §Fabrication, livraison, paiement — Chef du service comptable | Confirmé |
| EV1 | Gestion d'une commande / Service commercial | Commande client | Début message | — | T1 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| T1 | Gestion d'une commande / Service commercial | Enregistrer commande | Tâche utilisateur | — | T2 | Notes atelier §Explication générale — Responsable du service commercial (commande « Enregistrée ») | Confirmé |
| T2 | Gestion d'une commande / Service production | Vérifier stock et capacité | Tâche utilisateur | — | G1 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| G1 | Gestion d'une commande / Service production | Stock et capacité ? | Passerelle exclusive | G2 : Stock OK et capacité OK ; EV7 : Capacité insuffisante ; AP1 : Stock insuffisant et capacité OK | G2 ; EV7 ; AP1 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| AP1 | Gestion d'une commande / Service production | À préciser — voir question Q6 | Fin | — | — | Aucune (branche non décrite dans les sources) | À préciser |
| EV7 | Gestion d'une commande / Service production | Vers annulation commande | Lien envoi | — | — | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« on annule la commande (voir plus bas l'annulation) ») | Supposé |
| G2 | Gestion d'une commande / Service production | — | Passerelle parallèle | — | T3 ; T4 | Notes atelier §Explication générale — Responsable du service commercial (« deux choses se font en même temps ») | Confirmé |
| T3 | Gestion d'une commande / Service commercial | Préparer ordre de confirmation | Tâche utilisateur | — | G3 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| T4 | Gestion d'une commande / Service production | Réserver produits semi-finis | Tâche utilisateur | — | G3 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| G3 | Gestion d'une commande / Service commercial | — | Passerelle parallèle | — | EV2 | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« Une fois les deux faits ») | Supposé |
| EV2 | Gestion d'une commande / Service commercial | Ordre de confirmation | Message envoyé | — | Message « Ordre de confirmation » → P1 ; G4 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| G4 | Gestion d'une commande / Service commercial | — | Passerelle basée sur les événements | — | EV3 ; EV4 ; M1 | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« S'il confirme » / « S'il infirme, ou s'il ne répond pas dans les 8 jours ») | Supposé |
| EV3 | Gestion d'une commande / Service commercial | Confirmation client | Message reçu | — | G5 | Notes atelier §Explication générale — Responsable du service commercial (commande « Confirmée ») | Confirmé |
| EV4 | Gestion d'une commande / Service commercial | Infirmation client | Message reçu | — | G8 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| M1 | Gestion d'une commande / Service commercial | 8 jours | Minuterie intermédiaire | — | G8 | Notes atelier §Explication générale et §Questions posées et réponses — Responsable du service commercial | Confirmé |
| G5 | Gestion d'une commande / Service production | — | Passerelle parallèle | — | SP1 ; T5 | Notes atelier §Fabrication, livraison, paiement — Responsable de production / Chef du service comptable (« Quand la fabrication est lancée […] en parallèle ») | Confirmé |
| SP1 | Gestion d'une commande / Service production | Assemblage | Sous-processus | — | G6 | Notes atelier §Fabrication, livraison, paiement — Responsable de production | Confirmé |
| T5 | Gestion d'une commande / Service comptable | Créer facture | Tâche utilisateur | — | G6 | Notes atelier §Fabrication, livraison, paiement ; §Questions posées et réponses — Chef du service comptable (facture « Créée ») | Confirmé |
| G6 | Gestion d'une commande / Service production | — | Passerelle parallèle | — | SP2 | Déduit de Notes atelier §Fabrication, livraison, paiement (« Quand l'assemblage et la facture sont prêts ») | Supposé |
| SP2 | Gestion d'une commande / Service transport | Livraison | Sous-processus | — | Message « Livraison » → P1 ; G7 | Notes atelier §Fabrication, livraison, paiement — Coordinateur transport | Confirmé |
| G7 | Gestion d'une commande / Service comptable | — | Passerelle basée sur les événements | — | EV5 ; M2 | Déduit de Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (« Paiement reçu » / « Pas de paiement au bout de 15 jours ») | Supposé |
| EV5 | Gestion d'une commande / Service comptable | Règlement | Message reçu | — | SP3 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable | Confirmé |
| SP3 | Gestion d'une commande / Service comptable | Traitement comptable | Sous-processus | — | F1 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (« rapprochement de la facture ») | Confirmé |
| F1 | Gestion d'une commande / Service comptable | Commande réglée | Fin | — | — | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (commande « Réglée » et terminée) | Confirmé |
| M2 | Gestion d'une commande / Service comptable | 15 jours | Minuterie intermédiaire | — | SP4 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable ; Procédure PDF PR-COM-04 p. 3 §4.6 | Confirmé |
| SP4 | Gestion d'une commande / Service comptable | Gestion contentieux | Sous-processus | — | F2 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable | Confirmé |
| F2 | Gestion d'une commande / Service comptable | Commande terminée après contentieux | Fin | — | — | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (« la commande est considérée comme terminée ») | Confirmé |
| EV8 | Gestion d'une commande / Service commercial | Vers annulation commande | Lien réception | — | G8 | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« voir plus bas l'annulation ») | Supposé |
| G8 | Gestion d'une commande / Service commercial | — | Passerelle exclusive | — | T6 | Déduit de Notes atelier §Explication générale et §Annulation — Responsable du service commercial (trois causes d'annulation) | Supposé |
| T6 | Gestion d'une commande / Service commercial | Enregistrer annulation | Tâche utilisateur | — | G9 | Notes atelier §Annulation — Responsable du service commercial (commande « Annulée ») | Confirmé |
| G9 | Gestion d'une commande / Service commercial | Produits semi-finis réservés ? | Passerelle inclusive | T7 : OUI ; G10 : NON | T7 ; G10 | Notes atelier §Annulation — Responsable du service commercial (« Si des produits semi-finis avaient été réservés ») | Confirmé |
| T7 | Gestion d'une commande / Service production | Remettre en stock produits semi-finis | Tâche utilisateur | — | G10 | Notes atelier §Annulation — Responsable du service commercial | Confirmé |
| G10 | Gestion d'une commande / Service commercial | — | Passerelle inclusive | — | EV6 | Déduit de Notes atelier §Annulation — Responsable du service commercial | Supposé |
| EV6 | Gestion d'une commande / Service commercial | Notification annulation | Message envoyé | — | Message « Notification annulation » → P1 ; F3 | Notes atelier §Annulation — Responsable du service commercial | Confirmé |
| F3 | Gestion d'une commande / Service commercial | Commande annulée | Fin | — | — | Notes atelier §Annulation — Responsable du service commercial (commande « Annulée ») | Confirmé |

## 2. Questions par interlocuteur

### Responsable du service commercial
- Q1 — [T1] — À confirmer — L'enregistrement de la commande se fait-il dans un logiciel (par exemple SAP) ?
- Q2 — [M1] — À confirmer — Les 8 jours sont-ils comptés en jours calendaires, à partir de l'envoi de l'ordre de confirmation au client ?
- Q3 — [EV2] [T6] [EV6] — À confirmer — Est-ce bien le service commercial qui envoie l'ordre de confirmation, enregistre l'annulation et envoie la notification d'annulation au client ?
- Q4 — [G5] — À confirmer — Après la confirmation du client, le lancement de la fabrication donne-t-il lieu à une action précise (par exemple un ordre de fabrication) et, si oui, par quel service ?
- Q5 — [G9] [EV6] — À confirmer — La notification d'annulation est-elle envoyée au client seulement après la remise en stock des produits semi-finis, ou indépendamment de celle-ci ?

### Responsable de production
- Q6 — [AP1] [G1] — Bloquant pour la modélisation — Lorsque le stock est insuffisant mais que la capacité de production est suffisante, la commande est-elle fabriquée, mise en attente ou annulée ?
- Q7 — [T2] — À confirmer — La vérification du stock et de la capacité se fait-elle dans un logiciel (par exemple SAP) ?
- Q8 — [T7] — À confirmer — La remise en stock des produits semi-finis réservés est-elle faite par le service production, avec une saisie dans un logiciel ?

### Chef du service comptable
- Q9 — [T5] — À confirmer — La facture est-elle toujours créée pendant l'assemblage, ou arrive-t-il qu'elle soit émise après la livraison comme le prévoit la procédure PR-COM-04 (§4.5) ?
- Q10 — [M2] — À confirmer — Les 15 jours sans paiement sont-ils comptés à partir de la livraison, comme l'indique la procédure PR-COM-04 (§4.6) ?
- Q11 — [SP3] — À confirmer — Le traitement comptable se limite-t-il au rapprochement de la facture avec le règlement ?
- Q12 — [SP4] [F2] — À confirmer — La gestion du contentieux comporte-t-elle des échanges avec le client (relance, mise en demeure) qui doivent figurer sur le diagramme ?

### Coordinateur transport
- Q13 — [SP2] — À confirmer — À la fin de la livraison, le service transport transmet-il une confirmation de livraison au service comptable, comme le mentionne la procédure PR-COM-04 (§4.5) ?

## 3. Points signalés

- C4 est un brouillon v0.1 : sur les sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation des systèmes, objets de données, position du participant externe), le style du modèle C6 a été suivi.
- [M1] Écart pratique / procédure : la pratique est de 8 jours « appliqués à tout le monde » (responsable commercial), la procédure PR-COM-04 §4.2 prévoit 10 jours calendaires ; la pratique est retenue (voir Q2).
- [T5] Écart pratique / procédure : la facture est créée pendant l'assemblage (chef comptable), la procédure §4.5 la fait émettre après confirmation de la livraison ; la pratique est retenue (voir Q9).
- [M2] Le délai de 15 jours concorde entre la pratique et la procédure §4.6 ; seul le point de départ (la livraison) vient de la procédure (voir Q10).
- [SP2] La « confirmation de la livraison par le service transport » n'existe que dans la procédure §4.5 : elle n'est pas modélisée (voir Q13).
- Service approvisionnement : couloir non créé, la production indique qu'il n'intervient pas dans ce processus (le modèle C6 avait un couloir « Service appro » vide et un participant « Fournisseurs », non repris).
- Aucun nom de personne repéré dans les sources (seulement des fonctions).
- Aucune consigne adressée à l'IA repérée dans les sources.
- Aucune lecture incertaine : l'extrait du PDF est recopié en texte dans le fichier.
- Aucun élément « Non confirmé » : aucun propos n'a été tenu avec réserve, et les informations propres à la procédure écrite sont soit contredites par la pratique, soit rattachées à une question.
- [AP1] Fin « À préciser » ajoutée pour la branche non décrite « stock insuffisant, capacité OK » de [G1] (voir Q6, bloquante).
- [G1] Les conditions reprennent les mots du responsable commercial (« Stock OK et capacité OK », « Capacité insuffisante ») ; la troisième branche est le cas manquant.
- [G3] [G6] Supposé : passerelles parallèles fermantes déduites de « une fois les deux faits » et « quand l'assemblage et la facture sont prêts ».
- [G4] [G7] Supposé : attentes « réponse ou délai dépassé » modélisées en passerelles basées sur les événements (C4 §4).
- [G8] [G10] Supposé : passerelles de convergence des causes d'annulation et de la remise en stock.
- [EV7] [EV8] Supposé : événements lien « Vers annulation commande » repris du modèle C6 pour éviter un flux long depuis [G1].
- [G5] Le lancement de la fabrication est représenté par l'ouverture parallèle, comme dans C6, sans tâche dédiée (voir Q4).
- [G9] [G10] Passerelle inclusive utilisée pour la remise en stock conditionnelle, selon l'exemple de C4 §5 ; l'ordre remise en stock puis notification suit l'ordre des notes (voir Q5).
- [EV2] [T6] [EV6] Le couloir « Service commercial » est déduit de l'intervenant (responsable commercial, qui dit « on ») ; voir Q3.
- [T1] [T2] [T7] Type « Tâche utilisateur » repris du modèle C6, faute d'information sur l'usage d'un logiciel (voir Q1, Q7, Q8).
- Les statuts de la commande et de la facture (« Enregistrée », « Confirmée », « Créée », « Annulée », « Réglée ») sont cités dans les sources du tableau mais pas dessinés en objets de données comme dans C6 (C4 §8 à compléter).
- [SP1] Sous-processus réduit « Assemblage », repris du modèle C6 ; le client ne l'a pas détaillé ; à garder ou non.
- [SP2] Sous-processus réduit « Livraison », repris du modèle C6 ; le client ne l'a pas détaillé ; à garder ou non.
- [SP3] Sous-processus réduit « Traitement comptable », repris du modèle C6 ; seul le rapprochement de la facture est cité ; à garder ou non.
- [SP4] Sous-processus réduit « Gestion contentieux », repris du modèle C6 ; le client ne l'a pas détaillé ; à garder ou non.
- [SP2] Le flux de message « Livraison » vers le Client est rattaché au sous-processus replié ; le retour du client présent dans C6 n'a pas été cité et n'est pas repris.
- [SP4] Aucun échange avec le client n'est modélisé dans le contentieux, contrairement à C6, faute de source (voir Q12).
- [F1] [F2] Deux fins nommées (« Commande réglée », « Commande terminée après contentieux ») au lieu de la fin unique « Commande terminée » de C6 : règle « une fin nommée par issue ».
- [T3] Libellé « Préparer ordre de confirmation » (terme du client) au lieu de « Créer ordre de confirmation » (C6).
- Section « Fabrication, livraison, paiement » : les notes regroupent trois intervenants (production, comptabilité, transport) ; chaque information est attribuée d'après son service.
- Fichier `.bpmn` : aucune anomalie du tableau (36 lignes : 35 éléments + 1 participant externe ; 38 flux de séquence, 7 flux de message, 8 annotations ; fichier lu sans avertissement par bpmn-moddle) ; un réalignement manuel des flux de message et des éléments de l'annulation dans Camunda reste à prévoir.
