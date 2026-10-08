> ⚠️ Alerte : 1 information manque pour finir le diagramme (question Q1 : suite du processus quand le dossier d'un nouvel adhérent est « en attente »). Elle apparaît en « À préciser » dans le fichier BPMN.

## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Adhérent | Adhérent | Participant externe | — | Message « Demande d'emprunt » → EV1 ; Message « Informations adhérent » → SP1 ; Message « Cotisation » → SP1 ; Message « Ouvrage » → EV4 ; Message « Ouvrage » → EV6 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| EV1 | Gestion emprunt / Bibliothécaire | Demande d'emprunt | Début message | — | T1 | Notes atelier §Explication générale — Bibliothécaire (« un adhérent vient au guichet et demande à emprunter un ouvrage ») | Confirmé |
| T1 | Gestion emprunt / Bibliothécaire | Rechercher adhérent | Tâche utilisateur | — | G1 | Notes atelier §Explication générale — Bibliothécaire (« cherche d'abord l'adhérent dans le logiciel ») | Confirmé |
| G1 | Gestion emprunt / Bibliothécaire | Adhérent inscrit ? | Passerelle exclusive | G2 : OUI ; SP1 : NON | G2 ; SP1 | Notes atelier §Explication générale — Bibliothécaire (« S'il n'est pas encore inscrit… ») | Confirmé |
| SP1 | Gestion emprunt / Bibliothécaire | Création d'un adhérent | Sous-processus | — | Message « Demande d'informations » → P1 ; Message « Demande de cotisation » → P1 ; G2 | Notes atelier §Explication générale — Bibliothécaire | À préciser |
| G2 | Gestion emprunt / Bibliothécaire | — | Passerelle exclusive | — | SP2 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« que l'adhérent soit ancien ou nouveau ») | Supposé |
| SP2 | Gestion emprunt / Bibliothécaire | Validation d'un emprunt | Sous-processus | — | G3 | Notes atelier §Explication générale — Bibliothécaire ; §Questions posées et réponses (intervenant non indiqué) | Confirmé |
| G3 | Gestion emprunt / Bibliothécaire | Emprunt possible ? | Passerelle exclusive | T2 : OUI ; EV2 : NON | T2 ; EV2 | Notes atelier §Explication générale — Bibliothécaire (« Si un seul de ces contrôles ne passe pas, l'emprunt est refusé ») | Confirmé |
| EV2 | Gestion emprunt / Bibliothécaire | Emprunt impossible | Fin message | — | Message « Notification de refus » → P1 | Notes atelier §Explication générale — Bibliothécaire (« on le dit à l'adhérent (notification de refus) ») | Confirmé |
| T2 | Gestion emprunt / Bibliothécaire | Enregistrer emprunt | Tâche utilisateur | — | EV3 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| EV3 | Gestion emprunt / Bibliothécaire | Ouvrage | Message envoyé | — | Message « Ouvrage » → P1 ; G4 | Notes atelier §Explication générale — Bibliothécaire (« remet l'ouvrage à l'adhérent ») | Confirmé |
| G4 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | EV4 ; EV5 | Déduit de Notes atelier §Questions posées et réponses — Bibliothécaire (« on attend un mois ») | Supposé |
| EV4 | Gestion emprunt / Bibliothécaire | Retour ouvrage | Message reçu | — | G6 | Notes atelier §Retour de l'ouvrage — Bibliothécaire (« Quand l'adhérent rapporte l'ouvrage ») | Confirmé |
| EV5 | Gestion emprunt / Bibliothécaire | 1 mois | Minuterie intermédiaire | — | T3 | Notes atelier §Questions posées et réponses — Bibliothécaire (« Au bout d'un mois sans retour ») | Confirmé |
| T3 | Gestion emprunt / Bibliothécaire | Relancer adhérent | Tâche envoi | — | Message « Relance » → P1 ; G5 | Notes atelier §Questions posées et réponses — Bibliothécaire (« on envoie une relance à l'adhérent ») | Confirmé |
| G5 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | EV6 ; EV7 | Déduit de Notes atelier §Questions posées et réponses — Bibliothécaire (« 15 jours après la relance » / « après la relance mais avant les 15 jours ») | Supposé |
| EV6 | Gestion emprunt / Bibliothécaire | Retour ouvrage | Message reçu | — | G6 | Notes atelier §Questions posées et réponses — Bibliothécaire (« rapporte l'ouvrage après la relance mais avant les 15 jours ») | Confirmé |
| EV7 | Gestion emprunt / Bibliothécaire | 15 jours | Minuterie intermédiaire | — | T4 | Notes atelier §Questions posées et réponses — Bibliothécaire | Confirmé |
| T4 | Gestion emprunt / Bibliothécaire | Transmettre dossier au service litige | Tâche utilisateur | — | SP3 | Notes atelier §Questions posées et réponses — Bibliothécaire (« on transmet le dossier au service litige ») | Non confirmé |
| SP3 | Gestion emprunt / Service litige | Gestion litige | Sous-processus | — | EV9 | Notes atelier §Questions posées et réponses — Agent du service litige (« On ne détaillera pas notre procédure aujourd'hui ») | Confirmé |
| EV9 | Gestion emprunt / Service litige | Emprunt clos en litige | Fin | — | — | Notes atelier §Questions posées et réponses — Agent du service litige (« l'emprunt est clos “en litige” ») | Confirmé |
| G6 | Gestion emprunt / Bibliothécaire | — | Passerelle exclusive | — | T5 | Déduit de Notes atelier §Questions posées et réponses — Bibliothécaire (« on enregistre le retour normalement ») | Supposé |
| T5 | Gestion emprunt / Bibliothécaire | Enregistrer retour | Tâche utilisateur | — | T6 | Notes atelier §Retour de l'ouvrage — Bibliothécaire (« enregistre le retour dans le logiciel ») | Confirmé |
| T6 | Gestion emprunt / Documentaliste | Ranger ouvrage | Tâche manuelle | — | EV8 | Notes atelier §Retour de l'ouvrage — Bibliothécaire (« la documentaliste range l'ouvrage en rayon ») | Confirmé |
| EV8 | Gestion emprunt / Documentaliste | Emprunt terminé | Fin | — | — | Notes atelier §Retour de l'ouvrage — Bibliothécaire (« Là, l'emprunt est terminé ») | Confirmé |

### Détail de SP1 — Création d'un adhérent

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP1-EV1 | Gestion emprunt / Bibliothécaire | — | Début | — | SP1-T1 | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP1-T1 | Gestion emprunt / Bibliothécaire | Demander informations | Tâche envoi | — | Message « Demande d'informations » → P1 ; SP1-EV2 | Notes atelier §Explication générale — Bibliothécaire (« on lui demande ses informations (nom, adresse, pièce d'identité) ») | Confirmé |
| SP1-EV2 | Gestion emprunt / Bibliothécaire | Informations adhérent | Message reçu | — | SP1-T2 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« on les enregistre ») | Supposé |
| SP1-T2 | Gestion emprunt / Bibliothécaire | Enregistrer adhérent | Tâche utilisateur | — | SP1-T3 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T3 | Gestion emprunt / Bibliothécaire | Demander cotisation | Tâche envoi | — | Message « Demande de cotisation » → P1 ; SP1-G1 | Notes atelier §Explication générale — Bibliothécaire (« on lui demande de régler la cotisation ») | Confirmé |
| SP1-G1 | Gestion emprunt / Bibliothécaire | — | Passerelle basée sur les événements | — | SP1-EV3 ; SP1-EV4 | Déduit de Notes atelier §Explication générale — Bibliothécaire (« S'il paie tout de suite » / « S'il ne paie pas dans les 5 minutes ») | Supposé |
| SP1-EV3 | Gestion emprunt / Bibliothécaire | Cotisation | Message reçu | — | SP1-T4 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T4 | Gestion emprunt / Bibliothécaire | Valider inscription | Tâche utilisateur | — | SP1-EV5 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-EV5 | Gestion emprunt / Bibliothécaire | Inscription validée | Fin | — | — | Déduit de Notes atelier §Explication générale — Bibliothécaire (« la bibliothécaire valide l'inscription ») | Supposé |
| SP1-EV4 | Gestion emprunt / Bibliothécaire | 5 minutes | Minuterie intermédiaire | — | SP1-T5 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP1-T5 | Gestion emprunt / Bibliothécaire | Mettre dossier en attente | Tâche utilisateur | — | SP1-EV6 | Notes atelier §Explication générale — Bibliothécaire (« on met son dossier “en attente” ») | Confirmé |
| SP1-EV6 | Gestion emprunt / Bibliothécaire | À préciser — voir question Q1 | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire ; suite non décrite | À préciser |

### Détail de SP2 — Validation d'un emprunt

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP2-EV1 | Gestion emprunt / Bibliothécaire | — | Début | — | SP2-T1 | Déduit de Notes atelier §Explication générale — Bibliothécaire | Supposé |
| SP2-T1 | Gestion emprunt / Bibliothécaire | Contrôler cotisation | Tâche service | — | SP2-G1 | Notes atelier §Explication générale — Bibliothécaire (contrôle 1, « c'est le logiciel qui fait les contrôles automatiquement ») | Confirmé |
| SP2-G1 | Gestion emprunt / Bibliothécaire | Cotisation à jour ? | Passerelle exclusive | SP2-T2 : OUI ; SP2-EV2 : NON | SP2-T2 ; SP2-EV2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-T2 | Gestion emprunt / Bibliothécaire | Contrôler emprunt en retard | Tâche service | — | SP2-G2 | Notes atelier §Explication générale — Bibliothécaire (contrôle 2) | Confirmé |
| SP2-G2 | Gestion emprunt / Bibliothécaire | Emprunt en retard ? | Passerelle exclusive | SP2-T3 : NON ; SP2-EV2 : OUI | SP2-T3 ; SP2-EV2 | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-T3 | Gestion emprunt / Bibliothécaire | Contrôler nombre emprunts en cours | Tâche service | — | SP2-G3 | Notes atelier §Explication générale — Bibliothécaire (contrôle 3) | Confirmé |
| SP2-G3 | Gestion emprunt / Bibliothécaire | Nombre emprunts en cours ? | Passerelle exclusive | SP2-EV3 : < 5 ; SP2-EV2 : >= 5 | SP2-EV3 ; SP2-EV2 | Notes atelier §Explication générale — Bibliothécaire (« moins de 5 emprunts en cours ») | Confirmé |
| SP2-EV2 | Gestion emprunt / Bibliothécaire | Emprunt impossible | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire | Confirmé |
| SP2-EV3 | Gestion emprunt / Bibliothécaire | Emprunt possible | Fin | — | — | Notes atelier §Explication générale — Bibliothécaire | Confirmé |

## 2. Questions par interlocuteur

### Bibliothécaire (responsable de la bibliothèque)
- Q1 — [SP1] [SP1-EV6] — Bloquant pour la modélisation — Quand le dossier d'un nouvel adhérent est mis « en attente » faute de paiement, la demande d'emprunt s'arrête-t-elle là, ou passe-t-elle quand même aux contrôles du droit d'emprunt ?
- Q2 — [SP1-EV4] — À confirmer — Les 5 minutes sont-elles comptées à partir du moment où vous demandez la cotisation ?
- Q3 — [SP1-EV2] — À confirmer — Les informations du nouvel adhérent sont-elles données oralement au guichet et saisies directement par vous dans le logiciel ?
- Q4 — [SP2] — À confirmer — Le logiciel fait-il les trois contrôles dans l'ordre cité (cotisation, emprunt en retard, nombre d'emprunts en cours) et s'arrête-t-il au premier contrôle non passé ?
- Q5 — [EV2] — À confirmer — La notification de refus est-elle donnée oralement au guichet ou remise par écrit à l'adhérent ?
- Q6 — [EV5] — À confirmer — Le délai d'un mois court-il à partir de la date d'enregistrement de l'emprunt ?
- Q7 — [T3] — À confirmer — Par quel moyen la relance est-elle envoyée à l'adhérent (courrier, e-mail ou téléphone) ?
- Q8 — [EV7] — À confirmer — Le délai de 15 jours court-il à partir de la date d'envoi de la relance ?
- Q9 — [T4] — À confirmer — Le dossier est-il transmis au service litige par la bibliothécaire, et par quel moyen (logiciel, e-mail ou papier) ?
- Q10 — [EV1] — À confirmer — Les demandes d'emprunt se font-elles uniquement au guichet ?

### Agent du service litige
- Q11 — [SP3] — À confirmer — Si l'adhérent rapporte l'ouvrage une fois le dossier transmis au service litige, le retour est-il quand même enregistré par la bibliothèque ?
- Q12 — [EV9] — À confirmer — Pour la bibliothèque, l'emprunt reste-t-il clos « en litige » quelle que soit l'issue du dossier ?

### Documentaliste
- Q13 — [T6] — À confirmer — Comment savez-vous qu'un ouvrage retourné est à ranger (chariot de retour, liste dans le logiciel ou autre) ?

## 3. Points signalés

- C4 est un brouillon v0.1 : sur ses sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation du logiciel, position des participants externes), le style du modèle C5 a été suivi.
- Une seule source (notes d'atelier C1) : aucune procédure écrite (C2) fournie, donc aucun écart pratique / procédure relevé.
- Aucun nom de personne repéré : les intervenants sont désignés par leur fonction.
- Aucune consigne adressée à l'IA repérée dans les sources.
- Aucune valeur absurde ou incohérente, ni contradiction entre intervenants (délais 5 minutes, 1 mois, 15 jours et seuil de 5 emprunts cohérents).
- [SP1] [SP1-EV6] À préciser : la suite du processus quand le dossier est « en attente » n'a pas été décrite (Q1, bloquante).
- [T4] Non confirmé : l'action « transmettre le dossier » est dite au « on », sans préciser qui la fait ni comment (Q9) ; C5 passe directement au sous-processus « Gestion litige ».
- [G2] Supposé : passerelle de convergence déduite de « que l'adhérent soit ancien ou nouveau ».
- [G4] [G5] Supposé : attentes « retour ou délai dépassé » modélisées en passerelles basées sur les événements (C4 §4).
- [G6] Supposé : convergence des deux retours possibles avant « Enregistrer retour ».
- [SP1-EV1] [SP1-EV2] [SP1-G1] [SP1-EV5] [SP2-EV1] Supposé : éléments de structure des sous-processus.
- [SP1] Sous-processus repris du modèle C5 (« Création d'un adhérent ») ; à garder ou non.
- [SP2] Sous-processus repris du modèle C5 (« Validation d'un emprunt ») ; à garder ou non.
- [SP3] Sous-processus réduit, sans contenu : le service litige n'a pas détaillé sa procédure (C4 §3).
- [SP1-EV5] [SP1-EV6] Deux fins dans SP1 (C5 n'a qu'une fin « Fin ») : règle « une fin nommée par issue ».
- [SP1] Les échanges avec l'adhérent (informations, cotisation) sont rattachés au sous-processus replié dans le fichier `.bpmn`.
- [G1] Libellé « Adhérent inscrit ? » (terme du client) au lieu de « Adhérent existant ? » (C5).
- [EV4] [EV6] Libellé « Retour ouvrage » (terme des notes) au lieu de « Retour emprunt » (C5).
- [EV8] [EV9] Fins nommées avec les termes du client (« Emprunt terminé », « Emprunt clos en litige ») au lieu de « Fin emprunt » / « Fin emprunt litige » (C5).
- [EV3] La remise physique de l'ouvrage est modélisée en message envoyé « Ouvrage », comme dans C5.
- [SP2] Les contrôles automatiques du logiciel sont des tâches service dans le couloir Bibliothécaire, sans couloir « système » (C4 §8 à compléter).
- [SP2] La réponse « c'est le logiciel » n'a pas d'intervenant indiqué dans les notes ; elle concorde avec l'explication de la bibliothécaire.
- [SP2] L'ordre des contrôles reprend la numérotation des notes (1, 2, 3) ; voir Q4.
- [SP3] Le retour d'un ouvrage après transmission au service litige n'a pas été abordé : seule la partie couverte est modélisée (Q11).
- Fichier `.bpmn` : aucune anomalie du tableau signalée par le programme (24 éléments, 2 participants, 25 flux de séquence, 10 flux de message, 6 annotations) ; un réalignement manuel des flux de message de [SP1] dans Camunda reste à prévoir.
