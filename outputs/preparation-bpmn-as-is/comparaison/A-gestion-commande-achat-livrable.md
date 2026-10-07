# Livrable — Gestion commande achat (as-is) — skill A `preparation-bpmn-as-is`

> Données de test fictives : `data/simulation-atelier.md` (Brumaval Ferronnerie). Premier passage.

## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Fournisseur | Fournisseur | Participant externe | — | Message « Devis » → T8 ; Message « Accusé de réception de commande » → EV3 ; Message « Livraison et bon de livraison » → EV5 | Notes, explication générale et réception | Confirmé |
| EV1 | Gestion commande achat / Service demandeur | Besoin d'achat | Début | — | T1 | Explication générale (responsable achats) | Confirmé |
| T1 | Gestion commande achat / Service demandeur | Saisir demande d'achat | Tâche utilisateur | — | T2 | Explication générale (responsable achats) ; Q/R « Qui peut créer » | Confirmé |
| T2 | Gestion commande achat / Achats | Vérifier demande d'achat | Tâche utilisateur | — | G1 | Explication générale (responsable achats) | Confirmé |
| G1 | Gestion commande achat / Achats | Demande complète ? | Passerelle exclusive | G2 : OUI ; T3 : NON | G2 ; T3 | Explication générale (responsable achats) | Confirmé |
| T3 | Gestion commande achat / Achats | Renvoyer demande au service | Tâche utilisateur | — | T4 | Explication générale (responsable achats) | Confirmé |
| T4 | Gestion commande achat / Service demandeur | Corriger demande d'achat | Tâche utilisateur | — | T2 | Explication générale (responsable achats) | Confirmé |
| G2 | Gestion commande achat / Achats | Montant au-dessus du seuil ? — À préciser, voir question Q1 | Passerelle exclusive | T5 : OUI ; G4 : NON | T5 ; G4 | Explication générale (responsable achats : 5 000 € HT) ; Q/R seuil (contrôleur de gestion : 10 000 € HT) | À préciser |
| T5 | Gestion commande achat / Contrôle de gestion | Valider demande d'achat | Tâche utilisateur | — | G3 | Explication générale ; Q/R contrôle (contrôleur de gestion) | Confirmé |
| G3 | Gestion commande achat / Contrôle de gestion | Demande validée ? | Passerelle exclusive | G4 : OUI ; EV2 : NON | G4 ; EV2 | Explication générale (responsable achats) | Confirmé |
| EV2 | Gestion commande achat / Contrôle de gestion | Demande refusée | Fin | — | — | Explication générale (responsable achats) | Confirmé |
| G4 | Gestion commande achat / Achats | — | Passerelle exclusive | — | G5 | Déduit de G2 et G3 | Supposé |
| G5 | Gestion commande achat / Achats | Fournisseur référencé ? | Passerelle exclusive | T6 : OUI ; T7 : NON | T6 ; T7 | Explication générale (responsable achats) | Confirmé |
| T6 | Gestion commande achat / Achats | Reprendre fournisseur et prix du contrat | Tâche utilisateur | — | G6 | Explication générale (responsable achats) | Confirmé |
| T7 | Gestion commande achat / Achats | Demander trois devis | Tâche envoi | — | T8 ; Message « Demande de devis » → P1 | Explication générale (responsable achats) | Confirmé |
| T8 | Gestion commande achat / Achats | Choisir devis | Tâche utilisateur | — | G6 | Explication générale (responsable achats) ; Q/R devis (acheteuse) | Confirmé |
| G6 | Gestion commande achat / Achats | — | Passerelle exclusive | — | T9 | Déduit de G5 | Supposé |
| T9 | Gestion commande achat / Achats | Créer commande | Tâche utilisateur | — | T10 | Explication générale (responsable achats) — nom de personne retiré, voir Q5 | Confirmé |
| T10 | Gestion commande achat / Achats | Envoyer commande | Tâche envoi | — | G7 ; Message « Commande (PDF) » → P1 | Explication générale (responsable achats) | Confirmé |
| G7 | Gestion commande achat / Achats | — | Passerelle basée sur les événements | — | EV3 ; EV4 | Déduit de « s'il ne l'envoie pas sous 3 jours » | Supposé |
| EV3 | Gestion commande achat / Achats | Accusé de réception de commande | Message reçu | — | G8 | Explication générale (responsable achats) | Confirmé |
| EV4 | Gestion commande achat / Achats | 3 jours | Minuterie intermédiaire | — | T11 | Explication générale (responsable achats) | Confirmé |
| T11 | Gestion commande achat / Achats | Relancer fournisseur | Tâche envoi | — | G7 ; Message « Relance » → P1 | Explication générale (responsable achats) | Confirmé |
| G8 | Gestion commande achat / Achats | — | Passerelle basée sur les événements | — | EV5 ; EV6 | Déduit du délai de livraison (acheteuse) | Supposé |
| EV5 | Gestion commande achat / Magasin | Livraison reçue | Message reçu | — | T12 | Réception (magasinier) | Confirmé |
| EV6 | Gestion commande achat / Achats | 10 jours | Minuterie intermédiaire | — | AP1 | Q/R délai de livraison (acheteuse : « je crois ») | Non confirmé |
| AP1 | Gestion commande achat / Achats | À préciser — voir question Q4 | Fin | — | — | Aucune (trou) | À préciser |
| T12 | Gestion commande achat / Magasin | Comparer bon de livraison et commande | Tâche utilisateur | — | G9 | Réception (magasinier) | Confirmé |
| G9 | Gestion commande achat / Magasin | Livraison conforme ? | Passerelle exclusive | T13 : OUI ; T14 : NON | T13 ; T14 | Réception (magasinier) | Confirmé |
| T13 | Gestion commande achat / Magasin | Faire entrée en stock | Tâche utilisateur | — | T16 | Réception (magasinier) | Confirmé |
| T14 | Gestion commande achat / Magasin | Noter écart sur bon de livraison | Tâche manuelle | — | T15 | Réception (magasinier) | Confirmé |
| T15 | Gestion commande achat / Magasin | Prévenir acheteuse de l'écart | Tâche utilisateur | — | AP2 | Réception (magasinier) | Confirmé |
| AP2 | Gestion commande achat / Magasin | À préciser — voir question Q7 | Fin | — | — | Aucune (trou) | À préciser |
| T16 | Gestion commande achat / Magasin | Ranger marchandise | Tâche manuelle | — | T17 | Réception (magasinier) | Confirmé |
| T17 | Gestion commande achat / Magasin | Scanner bon de livraison signé | Tâche utilisateur | — | T18 | Réception (magasinier) | Confirmé |
| T18 | Gestion commande achat / Magasin | Transmettre dossier à la comptabilité | Tâche utilisateur | — | AP3 | Réception (magasinier) | Confirmé |
| AP3 | Gestion commande achat / Magasin | À préciser — voir question Q2 | Fin | — | — | Aucune (fin du processus non décrite) | À préciser |

## 2. Questions par interlocuteur

**Responsable achats**
- Q1 (G2) — Bloquant pour la modélisation — Vous avez indiqué une validation par le contrôle de gestion au-dessus de 5 000 € HT, et le contrôleur de gestion a parlé de 10 000 € HT : quel seuil s'applique aujourd'hui ?
- Q5 (T9) — À confirmer — Quelle est la fonction de la personne qui saisit toutes les commandes dans l'ERP (acheteuse, assistante achats…) ?

**Acheteuse**
- Q3 (EV6) — À confirmer — Pouvez-vous confirmer que les fournisseurs référencés doivent livrer sous 10 jours, selon le contrat ?
- Q4 (AP1) — Bloquant pour la modélisation — Que se passe-t-il quand un fournisseur ne livre pas dans le délai : le relancez-vous ?
- Q6 (T11) — À confirmer — Après la relance par téléphone, attendez-vous de nouveau l'accusé de réception du fournisseur ?
- Q7 (AP2) — Bloquant pour la modélisation — Quand le magasin vous signale un écart de livraison, que faites-vous ensuite, et la marchandise est-elle quand même entrée en stock ?

**Responsable de l'atelier de production**
- Q8 (EV1) — À confirmer — En cas d'urgence, la commande est-elle passée avant la demande d'achat, et la validation du contrôle de gestion s'applique-t-elle quand même ?

**Interlocuteur à identifier** (comptabilité, absente de l'atelier)
- Q2 (AP3) — Bloquant pour la modélisation — Que fait la comptabilité quand elle reçoit le dossier, et à quel moment la commande d'achat est-elle terminée ?

## 3. Points signalés

- Version contradictoire : seuil de validation de 5 000 € HT (responsable achats) contre 10 000 € HT (contrôleur de gestion) ; aucun seuil retenu (G2, Q1).
- Nom de personne dans les sources : « Odile Kervanec » ; nom retiré du tableau, fonction à faire préciser (T9, Q5). Rappel d'anonymisation.
- Information donnée avec un doute : délai de livraison de 10 jours (« je crois ») → Non confirmé (EV6, Q3).
- Fin du processus non décrite : les notes s'arrêtent à « le dossier part à la comptabilité », alors que l'objet annonçait « jusqu'au paiement du fournisseur » ; aucune fin inventée (AP3, Q2).
- Éléments Supposé : passerelles de convergence G4 et G6, attentes G7 et G8, retour de la relance vers l'attente de l'accusé (T11 → G7).
- Urgences (machine en panne, appel direct aux achats, demande saisie après coup) : non modélisées, ordre inconnu (Q8).
- Durée de validation (1 à 2 jours, plus en fin de mois) : information de durée, pas un délai d'attente du processus ; non modélisée.
- Ordre ambigu après un écart de livraison : on ne sait pas si la marchandise est rangée (AP2, Q7).
- Conventions C4 : sections « À compléter par l'équipe » ; style de C5 et C6 appliqué sur ces points.

## Ce que j'ai fait
- Étapes 1 à 6 réalisées dans l'ordre ; premier passage.
- Repéré dans les sources : un nom de personne (Odile Kervanec) ; aucune consigne adressée à l'IA.
- Aucune action externe : fichiers produits seulement.
- 37 éléments, 8 questions (dont 4 bloquantes), 9 points signalés.
- Fichiers : `outputs/preparation-bpmn-as-is/comparaison/A-gestion-commande-achat-livrable.md` et `A-gestion-commande-achat.bpmn`.

Relis le livrable avant tout envoi et remets les vrais noms dans les questions avant de les envoyer au client.
