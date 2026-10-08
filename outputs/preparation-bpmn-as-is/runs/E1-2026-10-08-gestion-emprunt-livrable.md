## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Adhérent | Adhérent | Participant externe | — | Message « Demande d'emprunt » → EV1 ; Message « Informations adhérent » → SP1 ; Message « Cotisation » → SP1 ; Message « Ouvrage » → EV3 ; Message « Ouvrage » → EV4 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| EV1 | Gestion emprunt / Bibliothécaire | Demande d'emprunt | Début message | — | T1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| T1 | Gestion emprunt / Bibliothécaire | Rechercher adhérent | Tâche utilisateur | — | G1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| G1 | Gestion emprunt / Bibliothécaire | Adhérent inscrit ? | Passerelle exclusive | G2 : OUI ; SP1 : NON | G2 ; SP1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1 | Gestion emprunt / Bibliothécaire | Création d'un adhérent | Sous-processus | — | Message « Demande d'informations » → P1 ; Message « Demande de cotisation » → P1 ; G2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| G2 | Gestion emprunt / Bibliothécaire | — | Passerelle exclusive | — | SP2 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« que l'adhérent soit ancien ou nouveau ») | Supposé |
| SP2 | Gestion emprunt / Bibliothécaire | Validation d'un emprunt | Sous-processus | — | G3 | Notes atelier §Explication générale — Bibliothécaire ; §Questions-réponses (intervenant non précisé) | Confirmé |
| G3 | Gestion emprunt / Bibliothécaire | Emprunt possible ? | Passerelle exclusive | T2 : OUI ; F1 : NON | T2 ; F1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| F1 | Gestion emprunt / Bibliothécaire | Emprunt impossible | Fin message | — | Message « Notification refus » → P1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| T2 | Gestion emprunt / Bibliothécaire | Enregistrer emprunt | Tâche utilisateur | — | EV2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| EV2 | Gestion emprunt / Bibliothécaire | Ouvrage | Message envoyé | — | Message « Ouvrage » → P1 ; G4 | Notes atelier §Explication générale — Bibliothécaire (« remet l'ouvrage à l'adhérent ») | Confirmé |
| G4 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | EV3 ; M1 | Déduit de Notes atelier §Questions-réponses — Bibliothécaire (« on attend un mois ») | Supposé |
| EV3 | Gestion emprunt / Bibliothécaire | Retour emprunt | Message reçu | — | G6 | Notes atelier §Retour de l'ouvrage — Bibliothécaire | Confirmé |
| M1 | Gestion emprunt / Bibliothécaire | 1 mois | Minuterie intermédiaire | — | T3 | Notes atelier §Questions-réponses — Bibliothécaire | Confirmé |
| T3 | Gestion emprunt / Bibliothécaire | Relancer adhérent | Tâche envoi | — | Message « Relance » → P1 ; G5 | Notes atelier §Questions-réponses — Bibliothécaire | Confirmé |
| G5 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | EV4 ; M2 | Déduit de Notes atelier §Questions-réponses — Bibliothécaire (« 15 jours après la relance ») | Supposé |
| EV4 | Gestion emprunt / Bibliothécaire | Retour emprunt | Message reçu | — | G6 | Notes atelier §Questions-réponses — Bibliothécaire | Confirmé |
| M2 | Gestion emprunt / Bibliothécaire | 15 jours | Minuterie intermédiaire | — | SP3 | Notes atelier §Questions-réponses — Bibliothécaire | Confirmé |
| SP3 | Gestion emprunt / Service litige | Gestion litige | Sous-processus | — | F3 | Notes atelier §Questions-réponses — Bibliothécaire ; Agent du service litige | Confirmé |
| F3 | Gestion emprunt / Service litige | Emprunt clos en litige | Fin | — | — | Notes atelier §Questions-réponses — Agent du service litige | Confirmé |
| G6 | Gestion emprunt / Bibliothécaire | — | Passerelle exclusive | — | T4 | Déduit de Notes atelier §Questions-réponses — Bibliothécaire (« on enregistre le retour normalement ») | Supposé |
| T4 | Gestion emprunt / Bibliothécaire | Enregistrer retour | Tâche utilisateur | — | T5 | Notes atelier §Retour de l'ouvrage — Bibliothécaire | Confirmé |
| T5 | Gestion emprunt / Documentaliste | Ranger ouvrage | Tâche manuelle | — | F2 | Notes atelier §Retour de l'ouvrage — Bibliothécaire | Confirmé |
| F2 | Gestion emprunt / Documentaliste | Emprunt terminé | Fin | — | — | Notes atelier §Retour de l'ouvrage — Bibliothécaire | Confirmé |

### Détail de SP1 — Création d'un adhérent

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP1-EV1 | Gestion emprunt / Bibliothécaire | — | Début | — | SP1-T1 | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP1-T1 | Gestion emprunt / Bibliothécaire | Demander informations | Tâche envoi | — | Message « Demande d'informations » → P1 ; SP1-EV2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-EV2 | Gestion emprunt / Bibliothécaire | Informations adhérent | Message reçu | — | SP1-T2 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« on lui demande ses informations […], on les enregistre ») | Supposé |
| SP1-T2 | Gestion emprunt / Bibliothécaire | Enregistrer adhérent | Tâche utilisateur | — | SP1-T3 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T3 | Gestion emprunt / Bibliothécaire | Demander cotisation | Tâche envoi | — | Message « Demande de cotisation » → P1 ; SP1-G1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-G1 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | SP1-EV3 ; SP1-M1 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« s'il paie tout de suite » / « s'il ne paie pas dans les 5 minutes ») | Supposé |
| SP1-EV3 | Gestion emprunt / Bibliothécaire | Cotisation | Message reçu | — | SP1-T4 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T4 | Gestion emprunt / Bibliothécaire | Valider inscription | Tâche utilisateur | — | SP1-F1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-F1 | Gestion emprunt / Bibliothécaire | Inscription validée | Fin | — | — | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP1-M1 | Gestion emprunt / Bibliothécaire | 5 minutes | Minuterie intermédiaire | — | SP1-T5 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T5 | Gestion emprunt / Bibliothécaire | Mettre dossier en attente | Tâche utilisateur | — | SP1-F2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-F2 | Gestion emprunt / Bibliothécaire | Dossier en attente | Fin | — | — | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |

### Détail de SP2 — Validation d'un emprunt

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP2-EV1 | Gestion emprunt / Bibliothécaire | — | Début | — | SP2-T1 | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP2-T1 | Gestion emprunt / Bibliothécaire | Contrôler cotisation | Tâche service | — | SP2-G1 | Notes atelier §Explication générale — Bibliothécaire (contrôle 1) | Confirmé |
| SP2-G1 | Gestion emprunt / Bibliothécaire | Cotisation à jour ? | Passerelle exclusive | SP2-T2 : OUI ; SP2-F1 : NON | SP2-T2 ; SP2-F1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-T2 | Gestion emprunt / Bibliothécaire | Contrôler emprunt en retard | Tâche service | — | SP2-G2 | Notes atelier §Explication générale — Bibliothécaire (contrôle 2) | Confirmé |
| SP2-G2 | Gestion emprunt / Bibliothécaire | Emprunt en retard ? | Passerelle exclusive | SP2-T3 : NON ; SP2-F1 : OUI | SP2-T3 ; SP2-F1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-T3 | Gestion emprunt / Bibliothécaire | Contrôler nombre emprunts en cours | Tâche service | — | SP2-G3 | Notes atelier §Explication générale — Bibliothécaire (contrôle 3) | Confirmé |
| SP2-G3 | Gestion emprunt / Bibliothécaire | Nombre emprunts en cours ? | Passerelle exclusive | SP2-F2 : < 5 ; SP2-F1 : >= 5 | SP2-F2 ; SP2-F1 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-F1 | Gestion emprunt / Bibliothécaire | Emprunt impossible | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-F2 | Gestion emprunt / Bibliothécaire | Emprunt possible | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire | Confirmé |

## 2. Questions par interlocuteur

### Bibliothécaire (responsable de la bibliothèque)
- Q1 — [SP1] — Bloquant pour la modélisation — Quand le dossier d'un nouvel adhérent est mis « en attente » faute de paiement, la demande d'emprunt passe-t-elle quand même aux contrôles du droit d'emprunt, ou s'arrête-t-elle là ?
- Q2 — [SP1-M1] — À confirmer — Le dossier est-il mis « en attente » après 5 minutes sans paiement, ou dès que l'adhérent indique qu'il ne peut pas payer ?
- Q3 — [SP2] — À confirmer — Le logiciel fait-il les trois contrôles dans l'ordre cité (cotisation, emprunt en retard, nombre d'emprunts en cours) et s'arrête-t-il au premier contrôle non passé ?
- Q4 — [F1] — À confirmer — La notification de refus est-elle donnée oralement au guichet ou remise par écrit à l'adhérent ?
- Q5 — [M1] — À confirmer — Le délai d'un mois court-il bien à partir de la date d'enregistrement de l'emprunt ?
- Q6 — [T3] — À confirmer — Par quel moyen la relance est-elle envoyée à l'adhérent (courrier, e-mail, téléphone) ?
- Q7 — [SP3] — À confirmer — Comment le dossier est-il transmis au service litige (formulaire, e-mail, logiciel), et est-ce la bibliothécaire qui s'en charge ?
- Q8 — [EV1] — À confirmer — Les demandes d'emprunt arrivent-elles uniquement au guichet, ou aussi par d'autres canaux (réservation en ligne, téléphone) ?

### Agent du service litige
- Q9 — [SP3] — À confirmer — Si l'adhérent rapporte l'ouvrage après la transmission du dossier au service litige, l'emprunt est-il alors enregistré comme retourné par la bibliothèque ?
- Q10 — [F3] — À confirmer — Le service litige informe-t-il la bibliothèque de l'issue du dossier, ou l'emprunt reste-t-il clos « en litige » quelle que soit cette issue ?

### Documentaliste
- Q11 — [T5] — À confirmer — Comment savez-vous qu'un ouvrage retourné est à ranger (dépôt sur un chariot, liste dans le logiciel, autre) ?

## 3. Points signalés

- C4 est un brouillon v0.1 : sur les sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation du logiciel, position des participants externes), le style du modèle C5 a été suivi.
- Seules des notes d'atelier (C1) ont été fournies : aucun écart pratique / procédure n'a pu être relevé, faute de procédure écrite (C2).
- Aucun nom de personne repéré dans les sources (seulement des fonctions).
- Aucune consigne adressée à l'IA repérée dans les sources.
- Aucun élément « Non confirmé » ni « À préciser » : aucun propos n'a été tenu avec réserve.
- [G2] Supposé : passerelle de convergence déduite de « que l'adhérent soit ancien ou nouveau ».
- [G4] [G5] Supposé : attentes « retour ou délai dépassé » modélisées en passerelles basées sur les événements (C4 §4).
- [G6] Supposé : convergence des deux retours possibles avant « Enregistrer retour ».
- [SP1-EV1] [SP1-EV2] [SP1-G1] [SP1-F1] [SP1-F2] [SP2-EV1] Supposé : éléments de structure des sous-processus.
- [SP1] Sous-processus repris du modèle C5 (création d'adhérent) ; à garder ou non.
- [SP2] Sous-processus repris du modèle C5 (validation d'emprunt) ; à garder ou non.
- [SP3] Sous-processus réduit, sans contenu : le service litige n'a pas détaillé sa procédure (C4 §3).
- [SP1-F1] [SP1-F2] Deux fins nommées dans SP1, alors que C5 n'en a qu'une (« Fin ») : règle « une fin nommée par issue ».
- [SP1] Les échanges avec l'adhérent (demande d'informations, cotisation) sont rattachés au sous-processus replié.
- [G1] Libellé « Adhérent inscrit ? » (terme du client) au lieu de « Adhérent existant ? » (C5).
- [F2] [F3] Libellés « Emprunt terminé » et « Emprunt clos en litige » repris des termes du client (C5 : « Fin emprunt », « Fin emprunt litige »).
- [SP3] La transmission du dossier au service litige est représentée par le passage de couloir M2 → SP3, sans tâche dédiée, comme dans C5 (voir Q7).
- [EV2] La remise de l'ouvrage, physique, est modélisée en message envoyé « Ouvrage », comme dans C5.
- [SP2] Les contrôles automatiques du logiciel sont des tâches service dans le couloir Bibliothécaire, sans couloir « système » (C4 §8 à compléter).
- [SP2] L'ordre des contrôles reprend la numérotation des notes (1, 2, 3) ; voir Q3.
- [SP2] La réponse « c'est le logiciel » n'a pas d'intervenant indiqué dans les notes ; elle concorde avec l'explication de la bibliothécaire.
- [F1] Fin message : le flux « Notification refus » vers l'Adhérent est noté dans la colonne « Élément suivant ».
- Fichier `.bpmn` : aucune anomalie du tableau (24 éléments, 24 flux de séquence, 10 flux de message, 4 annotations) ; un réalignement manuel des flux de message de [SP1] dans Camunda reste à prévoir.
