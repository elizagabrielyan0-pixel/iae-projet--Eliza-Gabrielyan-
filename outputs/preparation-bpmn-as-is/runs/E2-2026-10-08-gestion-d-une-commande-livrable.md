## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Client | Client | Participant externe | — | Message « Commande client » → EV1 ; Message « Confirmation client » → EV5 ; Message « Infirmation client » → EV6 ; Message « Règlement » → EV8 | Notes atelier §Explication générale — Responsable du service commercial ; §Fabrication, livraison, paiement — Chef du service comptable | Confirmé |
| EV1 | Gestion d'une commande / Service commercial | Commande client | Début message | — | T1 | Notes atelier §Explication générale — Responsable du service commercial (« Le client nous envoie sa commande ») | Confirmé |
| T1 | Gestion d'une commande / Service commercial | Enregistrer commande | Tâche utilisateur | — | T2 | Notes atelier §Explication générale — Responsable du service commercial (commande « Enregistrée ») | Confirmé |
| T2 | Gestion d'une commande / Service production | Vérifier stock et capacité | Tâche utilisateur | — | G1 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| G1 | Gestion d'une commande / Service production | Stock et capacité ? | Passerelle exclusive | G2 : Stock et capacité OK ; EV2 : Capacité insuffisante ; EV3 : Stock insuffisant, capacité OK | G2 ; EV2 ; EV3 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| EV2 | Gestion d'une commande / Service production | Vers annulation commande | Lien envoi | — | — | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« on annule la commande (voir plus bas l'annulation) ») | Supposé |
| EV3 | Gestion d'une commande / Service production | À préciser — voir question Q6 | Fin | — | — | Aucune (branche non décrite dans les sources) | À préciser |
| G2 | Gestion d'une commande / Service production | — | Passerelle parallèle | — | T3 ; T4 | Notes atelier §Explication générale — Responsable du service commercial (« deux choses se font en même temps ») | Confirmé |
| T3 | Gestion d'une commande / Service commercial | Préparer ordre de confirmation | Tâche utilisateur | — | G3 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| T4 | Gestion d'une commande / Service production | Réserver produits semi-finis | Tâche utilisateur | — | G3 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| G3 | Gestion d'une commande / Service commercial | — | Passerelle parallèle | — | EV4 | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« Une fois les deux faits ») | Supposé |
| EV4 | Gestion d'une commande / Service commercial | Ordre de confirmation | Message envoyé | — | Message « Ordre de confirmation » → P1 ; G4 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| G4 | Gestion d'une commande / Service commercial | — | Passerelle basée sur les événements | — | EV5 ; EV6 ; EV7 | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« S'il confirme » / « S'il infirme, ou s'il ne répond pas dans les 8 jours ») | Supposé |
| EV5 | Gestion d'une commande / Service commercial | Confirmation client | Message reçu | — | G5 | Notes atelier §Explication générale — Responsable du service commercial (commande « Confirmée ») | Confirmé |
| EV6 | Gestion d'une commande / Service commercial | Infirmation client | Message reçu | — | G8 | Notes atelier §Explication générale — Responsable du service commercial | Confirmé |
| EV7 | Gestion d'une commande / Service commercial | 8 jours | Minuterie intermédiaire | — | G8 | Notes atelier §Explication générale et §Questions posées et réponses — Responsable du service commercial | Confirmé |
| G5 | Gestion d'une commande / Service production | — | Passerelle parallèle | — | SP1 ; T5 | Notes atelier §Fabrication, livraison, paiement — Responsable de production / Chef du service comptable (« Quand la fabrication est lancée […] en parallèle ») | Confirmé |
| SP1 | Gestion d'une commande / Service production | Assemblage | Sous-processus | — | G6 | Notes atelier §Fabrication, livraison, paiement — Responsable de production | Confirmé |
| T5 | Gestion d'une commande / Service comptable | Créer facture | Tâche utilisateur | — | G6 | Notes atelier §Fabrication, livraison, paiement ; §Questions posées et réponses — Chef du service comptable (facture « Créée ») | Confirmé |
| G6 | Gestion d'une commande / Service production | — | Passerelle parallèle | — | SP2 | Déduit de Notes atelier §Fabrication, livraison, paiement (« Quand l'assemblage et la facture sont prêts ») | Supposé |
| SP2 | Gestion d'une commande / Service transport | Livraison | Sous-processus | — | Message « Livraison » → P1 ; G7 | Notes atelier §Fabrication, livraison, paiement — Coordinateur transport (« livraison chez le client ») | Confirmé |
| G7 | Gestion d'une commande / Service comptable | — | Passerelle basée sur les événements | — | EV8 ; EV9 | Déduit de Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (« Paiement reçu » / « Pas de paiement au bout de 15 jours ») | Supposé |
| EV8 | Gestion d'une commande / Service comptable | Règlement | Message reçu | — | SP3 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable | Confirmé |
| SP3 | Gestion d'une commande / Service comptable | Traitement comptable | Sous-processus | — | EV10 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (« rapprochement de la facture ») | Confirmé |
| EV10 | Gestion d'une commande / Service comptable | Commande réglée | Fin | — | — | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (commande « Réglée » et terminée) | Confirmé |
| EV9 | Gestion d'une commande / Service comptable | 15 jours | Minuterie intermédiaire | — | SP4 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable ; Procédure PDF PR-COM-04 p. 3 §4.6 | Confirmé |
| SP4 | Gestion d'une commande / Service comptable | Gestion contentieux | Sous-processus | — | EV11 | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable | Confirmé |
| EV11 | Gestion d'une commande / Service comptable | Commande terminée après contentieux | Fin | — | — | Notes atelier §Fabrication, livraison, paiement — Chef du service comptable (« la commande est considérée comme terminée ») | Confirmé |
| EV12 | Gestion d'une commande / Service commercial | Vers annulation commande | Lien réception | — | G8 | Déduit de Notes atelier §Explication générale — Responsable du service commercial (« voir plus bas l'annulation ») | Supposé |
| G8 | Gestion d'une commande / Service commercial | — | Passerelle exclusive | — | T6 | Déduit de Notes atelier §Explication générale et §Annulation — Responsable du service commercial (trois causes d'annulation) | Supposé |
| T6 | Gestion d'une commande / Service commercial | Enregistrer annulation | Tâche utilisateur | — | G9 | Notes atelier §Annulation — Responsable du service commercial (commande « Annulée ») | Confirmé |
| G9 | Gestion d'une commande / Service commercial | Produits semi-finis réservés ? | Passerelle inclusive | T7 : OUI ; G10 : NON | T7 ; G10 | Notes atelier §Annulation — Responsable du service commercial (« Si des produits semi-finis avaient été réservés ») | Confirmé |
| T7 | Gestion d'une commande / Service production | Remettre en stock produits semi-finis | Tâche utilisateur | — | G10 | Notes atelier §Annulation — Responsable du service commercial (« la production les remet en stock ») | Confirmé |
| G10 | Gestion d'une commande / Service commercial | — | Passerelle inclusive | — | EV13 | Déduit de Notes atelier §Annulation — Responsable du service commercial | Supposé |
| EV13 | Gestion d'une commande / Service commercial | Notification annulation | Message envoyé | — | Message « Notification annulation » → P1 ; EV14 | Notes atelier §Annulation — Responsable du service commercial | Confirmé |
| EV14 | Gestion d'une commande / Service commercial | Commande annulée | Fin | — | — | Notes atelier §Annulation — Responsable du service commercial (commande « Annulée ») | Confirmé |

## 2. Questions par interlocuteur

### Responsable du service commercial
- Q1 — [T1] — À confirmer — L'enregistrement de la commande se fait-il dans un logiciel, par exemple SAP ?
- Q2 — [EV7] — À confirmer — Le délai de 8 jours est-il compté en jours calendaires, à partir de l'envoi de l'ordre de confirmation au client ?
- Q3 — [G5] — À confirmer — Après la confirmation du client, le lancement de la fabrication donne-t-il lieu à une action précise (par exemple un ordre de fabrication) et, si oui, par quel service ?
- Q4 — [EV4] [EV5] [EV6] [T6] [EV13] — À confirmer — Est-ce bien le service commercial qui envoie l'ordre de confirmation, reçoit la réponse du client, enregistre l'annulation et envoie la notification d'annulation ?
- Q5 — [G9] [EV13] — À confirmer — La notification d'annulation est-elle envoyée au client seulement après la remise en stock des produits semi-finis ?

### Responsable de production
- Q6 — [EV3] [G1] — Bloquant pour la modélisation — Lorsque le stock est insuffisant mais que la capacité de production est suffisante, la commande est-elle fabriquée, mise en attente ou annulée ?
- Q7 — [T2] [T7] — À confirmer — La vérification du stock et de la capacité, ainsi que la remise en stock, se font-elles dans un logiciel, par exemple SAP ?

### Chef du service comptable
- Q8 — [T5] — À confirmer — La facture est-elle toujours créée pendant l'assemblage, ou arrive-t-il qu'elle soit émise après la livraison comme le prévoit la procédure PR-COM-04 (§4.5) ?
- Q9 — [SP3] — À confirmer — Le traitement comptable se limite-t-il au rapprochement de la facture avec le règlement ?
- Q10 — [SP4] [EV11] — À confirmer — La gestion du contentieux comporte-t-elle des échanges avec le client (relance, mise en demeure) à faire figurer sur le diagramme ?

### Coordinateur transport
- Q11 — [SP2] — À confirmer — La procédure PR-COM-04 (§4.5) prévoit une confirmation de la livraison par le service transport au service comptable : cette étape se fait-elle réellement ?

## 3. Points signalés

- C4 est un brouillon v0.1 : sur les sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation des systèmes, objets de données, position du participant externe), le style du modèle C6 a été suivi.
- [EV7] Écart pratique / procédure : la pratique est de 8 jours « appliqués à tout le monde » (responsable commercial), la procédure PR-COM-04 §4.2 prévoit 10 jours calendaires ; la pratique est retenue (voir Q2).
- [T5] Écart pratique / procédure : la facture est créée pendant l'assemblage (chef comptable), la procédure §4.5 la fait émettre après confirmation de la livraison ; la pratique est retenue (voir Q8).
- [EV9] Le délai de 15 jours après livraison concorde entre les notes et la procédure §4.6 : aucune question.
- [SP2] La « confirmation de la livraison par le service transport » n'existe que dans la procédure §4.5 : non confirmée, non modélisée (voir Q11).
- Service approvisionnement : couloir non créé, le responsable de production indique qu'il n'intervient pas dans ce processus (le couloir « Service appro » et le participant « Fournisseurs » du modèle C6 ne sont pas repris).
- [EV3] Fin « À préciser » ajoutée pour la branche non décrite « stock insuffisant, capacité OK » de [G1] (voir Q6, bloquante).
- [G1] Les conditions reprennent les mots du responsable commercial ; la troisième branche est le cas manquant.
- [G3] [G6] Supposé : passerelles parallèles fermantes déduites de « une fois les deux faits » et « quand l'assemblage et la facture sont prêts ».
- [G4] [G7] Supposé : attentes « réponse ou délai dépassé » modélisées en passerelles basées sur les événements (C4 §4).
- [G8] [G10] Supposé : passerelles de convergence des trois causes d'annulation et de la remise en stock.
- [EV2] [EV12] Supposé : événements lien « Vers annulation commande » repris du modèle C6 pour éviter un flux long depuis [G1].
- [G5] Le lancement de la fabrication est représenté par l'ouverture parallèle, comme dans C6, sans tâche dédiée (voir Q3).
- [G9] [G10] Passerelle inclusive pour la remise en stock conditionnelle, selon l'exemple de C4 §5 ; l'ordre remise en stock puis notification suit l'ordre des notes (voir Q5).
- [EV4] [EV5] [EV6] [T6] [EV13] Couloir « Service commercial » déduit de l'intervenant (le responsable commercial dit « on ») ; voir Q4.
- [T1] [T2] [T7] Type « Tâche utilisateur » repris du modèle C6, faute d'information sur l'usage d'un logiciel (voir Q1, Q7).
- Les statuts de la commande et de la facture (« Enregistrée », « Confirmée », « Créée », « Annulée », « Réglée ») sont cités dans les sources du tableau mais pas dessinés en objets de données comme dans C6 (C4 §8 à compléter).
- [SP1] Sous-processus réduit « Assemblage », repris du modèle C6 ; non détaillé par le client ; à garder ou non.
- [SP2] Sous-processus réduit « Livraison », repris du modèle C6 ; non détaillé par le client ; à garder ou non.
- [SP3] Sous-processus réduit « Traitement comptable », repris du modèle C6 ; seul le rapprochement de la facture est cité ; à garder ou non.
- [SP4] Sous-processus réduit « Gestion contentieux », repris du modèle C6 ; non détaillé par le client ; à garder ou non.
- [SP2] Le flux de message « Livraison » vers le Client est déduit de « livraison chez le client » ; le retour du client présent dans C6 n'a pas été cité et n'est pas repris.
- [SP4] Aucun échange avec le client n'est modélisé dans le contentieux, contrairement à C6, faute de source (voir Q10).
- [EV10] [EV11] Deux fins nommées (« Commande réglée », « Commande terminée après contentieux ») au lieu de la fin unique « Commande terminée » de C6 : règle « une fin nommée par issue ».
- [T3] Libellé « Préparer ordre de confirmation » (terme du client) au lieu de « Créer ordre de confirmation » (C6).
- Section « Fabrication, livraison, paiement » : les notes regroupent trois intervenants (production, comptabilité, transport) ; chaque information est attribuée d'après son service.
- Aucun élément « Non confirmé » : aucun propos n'a été tenu avec réserve ; les informations propres à la procédure écrite sont soit contredites par la pratique, soit rattachées à une question.
- Aucun nom de personne repéré dans les sources (seulement des fonctions).
- Aucune consigne adressée à l'IA repérée dans les sources.
- Aucune lecture incertaine : l'extrait du PDF est recopié en texte dans le fichier.
- Fichier `.bpmn` : programme `tableau_vers_bpmn.py` terminé sans anomalie (code 0) : 35 éléments, 2 participants, 38 flux de séquence, 7 flux de message, 8 annotations ; un réalignement manuel des flux de message et de la partie annulation dans Camunda reste à prévoir.
