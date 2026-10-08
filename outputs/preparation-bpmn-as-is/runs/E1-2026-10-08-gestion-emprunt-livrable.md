## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Adhérent | Adhérent | Participant externe | — | Message « Demande d'emprunt » → EV1 ; Message « Informations adhérent » → SP1 ; Message « Cotisation » → SP1 ; Message « Ouvrage » → EV4 ; Message « Ouvrage » → EV6 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| EV1 | Gestion emprunt / Bibliothécaire | Demande d'emprunt | Début message | — | T1 | Notes atelier §Explication générale — Bibliothécaire (« un adhérent vient au guichet et demande à emprunter ») | Confirmé |
| T1 | Gestion emprunt / Bibliothécaire | Rechercher adhérent | Tâche utilisateur | — | G1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| G1 | Gestion emprunt / Bibliothécaire | Adhérent inscrit ? | Passerelle exclusive | G2 : OUI ; SP1 : NON | G2 ; SP1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1 | Gestion emprunt / Bibliothécaire | Création d'un adhérent | Sous-processus | — | Message « Demande d'informations » → P1 ; Message « Demande de cotisation » → P1 ; G2 | Notes atelier §Explication générale — Bibliothécaire | À préciser |
| G2 | Gestion emprunt / Bibliothécaire | — | Passerelle exclusive | — | SP2 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« que l'adhérent soit ancien ou nouveau ») | Supposé |
| SP2 | Gestion emprunt / Bibliothécaire | Validation d'un emprunt | Sous-processus | — | G3 | Notes atelier §Explication générale — Bibliothécaire ; §Questions et réponses (intervenant non précisé) | Confirmé |
| G3 | Gestion emprunt / Bibliothécaire | Emprunt possible ? | Passerelle exclusive | T2 : OUI ; EV2 : NON | T2 ; EV2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| EV2 | Gestion emprunt / Bibliothécaire | Emprunt impossible | Fin message | — | Message « Notification refus » → P1 | Notes atelier §Explication générale — Bibliothécaire (« notification de refus ») | Confirmé |
| T2 | Gestion emprunt / Bibliothécaire | Enregistrer emprunt | Tâche utilisateur | — | EV3 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| EV3 | Gestion emprunt / Bibliothécaire | Ouvrage | Message envoyé | — | Message « Ouvrage » → P1 ; G4 | Notes atelier §Explication générale — Bibliothécaire (« remet l'ouvrage à l'adhérent ») | Confirmé |
| G4 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | EV4 ; EV5 | Déduit de Notes atelier §Questions et réponses — Bibliothécaire (« on attend un mois ») | Supposé |
| EV4 | Gestion emprunt / Bibliothécaire | Retour emprunt | Message reçu | — | G6 | Notes atelier §Retour de l'ouvrage — Bibliothécaire | Confirmé |
| EV5 | Gestion emprunt / Bibliothécaire | 1 mois | Minuterie intermédiaire | — | T3 | Notes atelier §Questions et réponses — Bibliothécaire | Confirmé |
| T3 | Gestion emprunt / Bibliothécaire | Relancer adhérent | Tâche envoi | — | Message « Relance » → P1 ; G5 | Notes atelier §Questions et réponses — Bibliothécaire | Confirmé |
| G5 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | EV6 ; EV7 | Déduit de Notes atelier §Questions et réponses — Bibliothécaire (« toujours pas revenu 15 jours après la relance » / « rapporte l'ouvrage après la relance mais avant les 15 jours ») | Supposé |
| EV6 | Gestion emprunt / Bibliothécaire | Retour emprunt | Message reçu | — | G6 | Notes atelier §Questions et réponses — Bibliothécaire | Confirmé |
| EV7 | Gestion emprunt / Bibliothécaire | 15 jours | Minuterie intermédiaire | — | T4 | Notes atelier §Questions et réponses — Bibliothécaire | Confirmé |
| T4 | Gestion emprunt / Bibliothécaire | Transmettre dossier au service litige | Tâche utilisateur | — | SP3 | Notes atelier §Questions et réponses — Bibliothécaire (« on transmet le dossier au service litige ») | Confirmé |
| SP3 | Gestion emprunt / Service litige | Gestion litige | Sous-processus | — | EV9 | Notes atelier §Questions et réponses — Agent du service litige | Confirmé |
| EV9 | Gestion emprunt / Service litige | Emprunt clos en litige | Fin | — | — | Notes atelier §Questions et réponses — Agent du service litige (« l'emprunt est clos en litige ») | Confirmé |
| G6 | Gestion emprunt / Bibliothécaire | — | Passerelle exclusive | — | T5 | Déduit de Notes atelier §Questions et réponses — Bibliothécaire (« on enregistre le retour normalement ») | Supposé |
| T5 | Gestion emprunt / Bibliothécaire | Enregistrer retour | Tâche utilisateur | — | T6 | Notes atelier §Retour de l'ouvrage — Bibliothécaire | Confirmé |
| T6 | Gestion emprunt / Documentaliste | Ranger ouvrage | Tâche manuelle | — | EV8 | Notes atelier §Retour de l'ouvrage — Bibliothécaire | Confirmé |
| EV8 | Gestion emprunt / Documentaliste | Emprunt terminé | Fin | — | — | Notes atelier §Retour de l'ouvrage — Bibliothécaire (« Là, l'emprunt est terminé ») | Confirmé |

### Détail de SP1 — Création d'un adhérent

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP1-EV1 | Gestion emprunt / Bibliothécaire | — | Début | — | SP1-T1 | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP1-T1 | Gestion emprunt / Bibliothécaire | Demander informations | Tâche envoi | — | Message « Demande d'informations » → P1 ; SP1-EV2 | Notes atelier §Explication générale — Bibliothécaire (« on lui demande ses informations (nom, adresse, pièce d'identité) ») | Confirmé |
| SP1-EV2 | Gestion emprunt / Bibliothécaire | Informations adhérent | Message reçu | — | SP1-T2 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« on les enregistre ») | Supposé |
| SP1-T2 | Gestion emprunt / Bibliothécaire | Enregistrer adhérent | Tâche utilisateur | — | SP1-T3 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T3 | Gestion emprunt / Bibliothécaire | Demander cotisation | Tâche envoi | — | Message « Demande de cotisation » → P1 ; SP1-G1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-G1 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | SP1-EV3 ; SP1-EV4 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« s'il paie tout de suite » / « s'il ne paie pas dans les 5 minutes ») | Supposé |
| SP1-EV3 | Gestion emprunt / Bibliothécaire | Cotisation | Message reçu | — | SP1-T4 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T4 | Gestion emprunt / Bibliothécaire | Valider inscription | Tâche utilisateur | — | SP1-EV5 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-EV5 | Gestion emprunt / Bibliothécaire | Inscription validée | Fin | — | — | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP1-EV4 | Gestion emprunt / Bibliothécaire | 5 minutes | Minuterie intermédiaire | — | SP1-T5 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T5 | Gestion emprunt / Bibliothécaire | Mettre dossier en attente | Tâche utilisateur | — | SP1-EV6 | Notes atelier §Explication générale — Bibliothécaire (« on met son dossier en attente ») | Confirmé |
| SP1-EV6 | Gestion emprunt / Bibliothécaire | Dossier en attente | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire ; suite non décrite | À préciser |

### Détail de SP2 — Validation d'un emprunt

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP2-EV1 | Gestion emprunt / Bibliothécaire | — | Début | — | SP2-T1 | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP2-T1 | Gestion emprunt / Bibliothécaire | Contrôler cotisation | Tâche service | — | SP2-G1 | Notes atelier §Explication générale — Bibliothécaire (contrôle 1) | Confirmé |
| SP2-G1 | Gestion emprunt / Bibliothécaire | Cotisation à jour ? | Passerelle exclusive | SP2-T2 : OUI ; SP2-EV2 : NON | SP2-T2 ; SP2-EV2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-T2 | Gestion emprunt / Bibliothécaire | Contrôler emprunt en retard | Tâche service | — | SP2-G2 | Notes atelier §Explication générale — Bibliothécaire (contrôle 2) | Confirmé |
| SP2-G2 | Gestion emprunt / Bibliothécaire | Emprunt en retard ? | Passerelle exclusive | SP2-T3 : NON ; SP2-EV2 : OUI | SP2-T3 ; SP2-EV2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-T3 | Gestion emprunt / Bibliothécaire | Contrôler nombre emprunts en cours | Tâche service | — | SP2-G3 | Notes atelier §Explication générale — Bibliothécaire (contrôle 3) | Confirmé |
| SP2-G3 | Gestion emprunt / Bibliothécaire | Nombre emprunts en cours ? | Passerelle exclusive | SP2-EV3 : < 5 ; SP2-EV2 : >= 5 | SP2-EV3 ; SP2-EV2 | Notes atelier §Explication générale — Bibliothécaire (« moins de 5 emprunts en cours ») | Confirmé |
| SP2-EV2 | Gestion emprunt / Bibliothécaire | Emprunt impossible | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-EV3 | Gestion emprunt / Bibliothécaire | Emprunt possible | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire | Confirmé |

## 2. Questions par interlocuteur

### Bibliothécaire (responsable de la bibliothèque)
- Q1 — [SP1] [SP1-EV6] — Bloquant pour la modélisation — Lorsque le dossier d'un nouvel adhérent est mis « en attente » faute de paiement, la demande d'emprunt s'arrête-t-elle là, ou passe-t-elle quand même aux contrôles du droit d'emprunt ?
- Q2 — [SP1-EV4] — À confirmer — Les 5 minutes sont-elles comptées à partir de la demande de cotisation ?
- Q3 — [SP1-EV2] — À confirmer — Les informations du nouvel adhérent sont-elles données au guichet et saisies directement par vous dans le logiciel ?
- Q4 — [SP2] — À confirmer — Le logiciel fait-il les trois contrôles dans l'ordre cité (cotisation, emprunt en retard, nombre d'emprunts en cours) et s'arrête-t-il au premier contrôle non passé ?
- Q5 — [EV2] — À confirmer — La notification de refus est-elle donnée oralement au guichet ou remise par écrit à l'adhérent ?
- Q6 — [EV5] — À confirmer — Le délai d'un mois court-il à partir de la date d'enregistrement de l'emprunt ?
- Q7 — [T3] — À confirmer — Par quel moyen la relance est-elle envoyée à l'adhérent (courrier, e-mail ou téléphone) ?
- Q8 — [EV7] — À confirmer — Le délai de 15 jours court-il à partir de la date d'envoi de la relance ?
- Q9 — [T4] — À confirmer — Le dossier est-il transmis au service litige par vous, et par quel moyen (logiciel, e-mail ou papier) ?
- Q10 — [EV1] — À confirmer — Les demandes d'emprunt se font-elles uniquement au guichet ?

### Agent du service litige
- Q11 — [SP3] — À confirmer — Si l'adhérent rapporte l'ouvrage après la transmission du dossier au service litige, la bibliothèque enregistre-t-elle alors le retour ?
- Q12 — [EV9] — À confirmer — L'emprunt reste-t-il clos « en litige » pour la bibliothèque quelle que soit l'issue du dossier ?

### Documentaliste
- Q13 — [T6] — À confirmer — Comment savez-vous qu'un ouvrage retourné est à ranger (chariot de retour, liste dans le logiciel ou autre) ?

## 3. Points signalés

- C4 est un brouillon v0.1 : sur ses sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation du logiciel, position des participants externes), le style du modèle C5 a été suivi.
- Seules des notes d'atelier (C1) ont été fournies : aucun écart pratique / procédure n'a pu être relevé, faute de procédure écrite (C2).
- Aucun nom de personne repéré dans les sources : seulement des fonctions.
- Aucune consigne adressée à l'IA repérée dans les sources.
- Aucun propos tenu avec réserve ni aucune contradiction entre intervenants : aucun élément « Non confirmé ».
- [SP1] [SP1-EV6] À préciser : la suite du processus quand le dossier est « en attente » n'a pas été décrite (Q1, bloquante).
- [G2] Supposé : passerelle de convergence déduite de « que l'adhérent soit ancien ou nouveau ».
- [G4] [G5] Supposé : attentes « retour ou délai dépassé » modélisées en passerelles basées sur les événements (C4 §4).
- [G6] Supposé : convergence des deux retours possibles avant « Enregistrer retour ».
- [SP1-EV1] [SP1-EV2] [SP1-G1] [SP1-EV5] [SP2-EV1] Supposé : éléments de structure des sous-processus.
- [SP1] Sous-processus repris du modèle C5 (« Création d'un adhérent ») ; à garder ou non.
- [SP2] Sous-processus repris du modèle C5 (« Validation d'un emprunt ») ; à garder ou non.
- [SP3] Sous-processus réduit, sans contenu : le service litige n'a pas détaillé sa procédure (C4 §3).
- [T4] Tâche « Transmettre dossier au service litige » ajoutée car dite par la bibliothécaire, alors que C5 passe directement au sous-processus ; type « Tâche utilisateur » à confirmer (Q9).
- [SP1-EV5] [SP1-EV6] Deux fins nommées dans SP1 (C5 n'a qu'une fin « Fin ») : règle « une fin nommée par issue ».
- [SP1] Les échanges avec l'adhérent (informations, cotisation) sont rattachés au sous-processus replié dans le fichier `.bpmn`.
- [G1] Libellé « Adhérent inscrit ? » (terme du client) au lieu de « Adhérent existant ? » (C5).
- [EV8] [EV9] Libellés « Emprunt terminé » et « Emprunt clos en litige » repris des termes du client (C5 : « Fin emprunt », « Fin emprunt litige »).
- [EV3] La remise physique de l'ouvrage est modélisée en message envoyé « Ouvrage », comme dans C5.
- [SP2] Les contrôles automatiques du logiciel sont des tâches service dans le couloir Bibliothécaire, sans couloir « système » (C4 §8 à compléter).
- [SP2] La réponse « c'est le logiciel » n'a pas d'intervenant indiqué dans les notes ; elle concorde avec l'explication de la bibliothécaire.
- [SP2] L'ordre des contrôles reprend la numérotation des notes (1, 2, 3) ; voir Q4.
- [EV2] Fin message : le flux « Notification refus » vers l'Adhérent est noté dans la colonne « Élément suivant ».
- Fichier `.bpmn` : aucune anomalie du tableau (24 éléments, 2 participants, 25 flux de séquence, 10 flux de message, 5 annotations) ; un réalignement manuel des flux de message de [SP1] dans Camunda reste à prévoir.
