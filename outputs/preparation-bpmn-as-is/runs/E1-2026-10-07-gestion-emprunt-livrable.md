# Gestion emprunt — préparation BPMN as-is (premier passage, 2026-10-07)

Source unique : C1 = notes d'atelier de la consultante (`E1-atelier-bibliotheque.md`). Aucune source C2 (PDF) ni C3.
Abréviations des sources : « C1 §Général » = Explication générale du fonctionnement (bibliothécaire) ; « C1 §Retour » = Retour de l'ouvrage ; « C1 §Q&R » = Questions posées et réponses.

## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Adhérent | Adhérent | Participant externe | — | Message « Demande d'emprunt » → EV1 ; Message « Informations » → EV2 ; Message « Cotisation » → EV3 ; Message « Ouvrage » → EV6 ; Message « Ouvrage » → EV8 | C1 §Général, §Retour, §Q&R (bibliothécaire) | Confirmé |
| EV1 | Gestion emprunt / Bibliothécaire | Demande d'emprunt | Début message | — | T1 | C1 §Général (bibliothécaire) : « un adhérent vient au guichet et demande à emprunter » | Confirmé |
| T1 | Gestion emprunt / Bibliothécaire | Rechercher adhérent | Tâche utilisateur | — | G1 | C1 §Général (bibliothécaire) : « cherche l'adhérent dans le logiciel » | Confirmé |
| G1 | Gestion emprunt / Bibliothécaire | Adhérent existant ? | Passerelle exclusive | G3 : OUI ; T2 : NON | G3 ; T2 | C1 §Général (bibliothécaire) : « s'il n'est pas encore inscrit » | Confirmé |
| T2 | Gestion emprunt / Bibliothécaire | Demander informations | Tâche envoi | — | EV2 ; Message « Demande informations » → P1 | C1 §Général (bibliothécaire) : « on lui demande ses informations (nom, adresse, pièce d'identité) » | Confirmé |
| EV2 | Gestion emprunt / Bibliothécaire | Réception informations | Message reçu | — | T3 | Découle de T2 et T3 (C1 §Général) | Supposé |
| T3 | Gestion emprunt / Bibliothécaire | Enregistrer adhérent | Tâche utilisateur | — | T4 | C1 §Général (bibliothécaire) : « on les enregistre » | Confirmé |
| T4 | Gestion emprunt / Bibliothécaire | Demander cotisation | Tâche envoi | — | G2 ; Message « Demande cotisation » → P1 | C1 §Général (bibliothécaire) : « on lui demande de régler la cotisation » | Confirmé |
| G2 | Gestion emprunt / Bibliothécaire | (sans nom) | Passerelle basée sur les événements | — | EV3 ; EV4 | C1 §Général (bibliothécaire) : paie tout de suite / ne paie pas dans les 5 minutes | Confirmé |
| EV3 | Gestion emprunt / Bibliothécaire | Cotisation | Message reçu | — | T5 | C1 §Général (bibliothécaire) : « s'il paie tout de suite » | Confirmé |
| EV4 | Gestion emprunt / Bibliothécaire | 5 minutes | Minuterie intermédiaire | — | T6 | C1 §Général (bibliothécaire) : « s'il ne paie pas dans les 5 minutes » | Confirmé |
| T5 | Gestion emprunt / Bibliothécaire | Valider inscription | Tâche utilisateur | — | G3 | C1 §Général (bibliothécaire) : « la bibliothécaire valide l'inscription » | Confirmé |
| T6 | Gestion emprunt / Bibliothécaire | Mettre adhérent en attente | Tâche utilisateur | — | F1 | C1 §Général (bibliothécaire) : « on met son dossier en attente » | Confirmé |
| F1 | Gestion emprunt / Bibliothécaire | Dossier en attente (À préciser — voir question Q1) | Fin | — | — | C1 §Général : suite non décrite après la mise en attente | À préciser |
| G3 | Gestion emprunt / Bibliothécaire | (convergence, sans nom) | Passerelle exclusive | — | T7 | C1 §Général (bibliothécaire) : « que l'adhérent soit ancien ou nouveau, on contrôle » | Supposé |
| T7 | Gestion emprunt / Bibliothécaire | Contrôler cotisation | Tâche service | — | G4 | C1 §Général (bibliothécaire) contrôle 1 ; §Q&R : fait automatiquement par le logiciel | Confirmé |
| G4 | Gestion emprunt / Bibliothécaire | Cotisation à jour ? | Passerelle exclusive | T8 : OUI ; F2 : NON | T8 ; F2 | C1 §Général (bibliothécaire) : « si un seul de ces contrôles ne passe pas, l'emprunt est refusé » | Confirmé |
| T8 | Gestion emprunt / Bibliothécaire | Contrôler emprunt en retard | Tâche service | — | G5 | C1 §Général (bibliothécaire) contrôle 2 ; §Q&R | Confirmé |
| G5 | Gestion emprunt / Bibliothécaire | Emprunt en retard ? | Passerelle exclusive | T9 : NON ; F2 : OUI | T9 ; F2 | C1 §Général (bibliothécaire) | Confirmé |
| T9 | Gestion emprunt / Bibliothécaire | Contrôler nb emprunt en cours | Tâche service | — | G6 | C1 §Général (bibliothécaire) contrôle 3 ; §Q&R | Confirmé |
| G6 | Gestion emprunt / Bibliothécaire | Nb emprunt en cours ? | Passerelle exclusive | T10 : < 5 ; F2 : >= 5 | T10 ; F2 | C1 §Général (bibliothécaire) : « moins de 5 emprunts en cours » | Confirmé |
| F2 | Gestion emprunt / Bibliothécaire | Emprunt impossible | Fin message | — | Message « Notification refus » → P1 | C1 §Général (bibliothécaire) : « l'emprunt est refusé et on le dit à l'adhérent (notification de refus) » | Confirmé |
| T10 | Gestion emprunt / Bibliothécaire | Enregistrer emprunt | Tâche utilisateur | — | EV5 | C1 §Général (bibliothécaire) : « enregistre l'emprunt » | Confirmé |
| EV5 | Gestion emprunt / Bibliothécaire | Ouvrage | Message envoyé | — | G7 ; Message « Ouvrage » → P1 | C1 §Général (bibliothécaire) : « remet l'ouvrage à l'adhérent » | Confirmé |
| G7 | Gestion emprunt / Bibliothécaire | (sans nom) | Passerelle basée sur les événements | — | EV6 ; EV7 | C1 §Retour et §Q&R (bibliothécaire) : retour ou un mois sans retour | Confirmé |
| EV6 | Gestion emprunt / Bibliothécaire | Retour emprunt | Message reçu | — | G9 | C1 §Retour (bibliothécaire) : « l'adhérent rapporte l'ouvrage » | Confirmé |
| EV7 | Gestion emprunt / Bibliothécaire | 1 mois | Minuterie intermédiaire | — | T11 | C1 §Q&R (bibliothécaire) : « on attend un mois » | Confirmé |
| T11 | Gestion emprunt / Bibliothécaire | Relancer adhérent | Tâche envoi | — | G8 ; Message « Relance » → P1 | C1 §Q&R (bibliothécaire) : « on envoie une relance à l'adhérent » | Confirmé |
| G8 | Gestion emprunt / Bibliothécaire | (sans nom) | Passerelle basée sur les événements | — | EV8 ; EV9 | C1 §Q&R (bibliothécaire) : retour avant les 15 jours ou pas | Confirmé |
| EV8 | Gestion emprunt / Bibliothécaire | Retour emprunt | Message reçu | — | G9 | C1 §Q&R (bibliothécaire) : « rapporte l'ouvrage après la relance mais avant les 15 jours » | Confirmé |
| EV9 | Gestion emprunt / Bibliothécaire | 15 jours | Minuterie intermédiaire | — | SP1 | C1 §Q&R (bibliothécaire) : « toujours pas revenu 15 jours après la relance » | Confirmé |
| G9 | Gestion emprunt / Bibliothécaire | (convergence, sans nom) | Passerelle exclusive | — | T12 | C1 §Q&R (bibliothécaire) : « on enregistre le retour normalement » | Supposé |
| T12 | Gestion emprunt / Bibliothécaire | Enregistrer retour | Tâche utilisateur | — | T13 | C1 §Retour (bibliothécaire) : « enregistre le retour dans le logiciel » | Confirmé |
| T13 | Gestion emprunt / Documentaliste | Ranger ouvrage | Tâche manuelle | — | F3 | C1 §Retour (bibliothécaire) : « la documentaliste range l'ouvrage en rayon » | Confirmé |
| F3 | Gestion emprunt / Documentaliste | Fin emprunt | Fin | — | — | C1 §Retour (bibliothécaire) : « Là, l'emprunt est terminé » | Confirmé |
| SP1 | Gestion emprunt / Service litige | Gestion litige | Sous-processus | — | F4 | C1 §Q&R (bibliothécaire) : « on transmet le dossier au service litige » ; (agent litige) : procédure non détaillée | Confirmé |
| F4 | Gestion emprunt / Service litige | Fin emprunt litige | Fin | — | — | C1 §Q&R (agent litige) : « l'emprunt est clos en litige » | Confirmé |

## 2. Questions pour le client

### Responsable de la bibliothèque (bibliothécaire principale)
- **Q1** (F1, T6) — Bloquant pour la modélisation : quand le dossier est mis en attente faute de paiement dans les 5 minutes, la demande d'emprunt s'arrête-t-elle là ?
- **Q2** (T6) — À confirmer : quand un adhérent en attente revient payer plus tard, reprend-on à la validation de l'inscription ?
- **Q3** (T2, EV2, T3, T4, T6) — À confirmer : est-ce bien la bibliothécaire, au guichet, qui recueille les informations, enregistre l'adhérent, demande la cotisation et met le dossier en attente ?
- **Q4** (T7, T8, T9) — À confirmer : le logiciel fait-il les trois contrôles dans l'ordre cotisation, retard, nombre d'emprunts, et s'arrête-t-il au premier refus ?
- **Q5** (F2) — À confirmer : qui annonce le refus à l'adhérent, et sous quelle forme (oral au guichet, message, courrier) ?
- **Q6** (EV7) — À confirmer : le délai d'un mois court-il à partir de la date de l'emprunt ?
- **Q7** (T11) — À confirmer : qui envoie la relance, et par quel moyen (courrier, mail, logiciel) ?
- **Q8** (EV9, SP1) — À confirmer : qui transmet le dossier au service litige, et de quelle façon ?

### Agent du service litige
- **Q9** (SP1) — À confirmer : pourriez-vous nous décrire, lors d'un prochain échange, les étapes de la gestion d'un litige ?
- **Q10** (SP1, F4) — À confirmer : si l'adhérent rapporte l'ouvrage une fois le dossier transmis, qui enregistre le retour ?

### Documentaliste
- **Q11** (T13) — À confirmer : rangez-vous en rayon chaque ouvrage dont le retour a été enregistré ?

## 3. Points signalés

- Anonymisation : aucun nom de personne repéré dans les sources, seulement des fonctions.
- Consignes : aucune consigne adressée à l'IA repérée dans les sources.
- Sources : seules les notes C1 ; aucun PDF ni procédure écrite, donc aucun écart pratique / procédure à signaler.
- Interlocuteurs : la documentaliste n'a pas pris la parole d'après les notes ; T13 repose sur ce qu'a dit la bibliothécaire (Q11).
- C4 présente mais en brouillon v0.1 ; la façon de représenter le logiciel (§8) n'est pas fixée : les contrôles automatiques T7, T8, T9 sont placés dans le couloir Bibliothécaire, comme dans le modèle C5.
- Le modèle C5 regroupe l'inscription et les contrôles dans les sous-processus « Création d'un adhérent » et « Validation d'un emprunt » ; ici ils sont laissés à plat car l'atelier les a décrits. À replier dans Camunda si tu préfères le niveau de détail de C5.
- Supposé (structure seulement) : EV2 « Réception informations », convergences G3 et G9.
- À préciser : F1, fin ajoutée après la mise en attente pour que le diagramme tienne (Q1).
- La transmission au service litige n'est pas une tâche à part : elle est représentée par le passage du flux vers le couloir Service litige, comme dans C5 (Q8).
- SP1 « Gestion litige » est un sous-processus réduit et vide : le service litige n'a pas détaillé sa procédure (Q9).
- Coquilles du modèle C5 non reproduites (« Emprunt  impossible » avec double espace).
- Mise en page générée automatiquement (fichier ouvert sans erreur dans bpmn-js, le moteur de Camunda) : le flux de message de F2 passe derrière T10, un réalignement manuel dans Camunda est attendu.
