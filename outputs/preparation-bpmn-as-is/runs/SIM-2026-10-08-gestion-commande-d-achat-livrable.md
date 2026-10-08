> ⚠️ Alerte : 1 nom de personne a été trouvé dans les notes d'atelier (§ Explication générale, création de la commande). Il a été remplacé par « Fonction à préciser » ; anonymisez le fichier source.
> ⚠️ Alerte : deux seuils différents ont été cités pour la validation par le contrôle de gestion (5 000 € HT par la responsable achats, 10 000 € HT par le contrôleur de gestion). Rien n'a été tranché (question Q1).
> ⚠️ Alerte : 7 informations manquent pour finir le diagramme (questions Q1, Q2, Q4, Q6, Q7, Q13, Q16). Elles apparaissent en « À préciser » dans le fichier BPMN.

## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| P1 | Fournisseur | Fournisseur | Participant externe | — | Message « Devis » → T9 ; Message « Accusé de réception de commande » → EV2 ; Message « Livraison avec bon de livraison » → EV4 | Notes atelier § Explication générale — Responsable achats ; § Réception — Magasinier | Confirmé |
| EV1 | Gestion commande d'achat / Service demandeur | Besoin d'achat | Début | — | T1 | Notes atelier § Explication générale, puce 1 — Responsable achats (« Tout part d'un besoin dans un service ») | Confirmé |
| T1 | Gestion commande d'achat / Service demandeur | Saisir demande d'achat dans l'ERP | Tâche utilisateur | — | T2 | Notes atelier § Explication générale, puces 2-3 — Responsable achats ; § Questions posées — Responsable achats (« tous les chefs de service ») | Confirmé |
| T2 | Gestion commande d'achat / Acheteuse | Vérifier demande d'achat | Tâche utilisateur | — | G1 | Notes atelier § Explication générale, puces 4-5 — Responsable achats | Confirmé |
| G1 | Gestion commande d'achat / Acheteuse | Demande complète ? | Passerelle exclusive | G2 : OUI ; T3 : NON | G2 ; T3 | Notes atelier § Explication générale, puce 5 — Responsable achats (« Si c'est incomplet… ») | Confirmé |
| T3 | Gestion commande d'achat / Acheteuse | Renvoyer demande au service avec commentaire | Tâche utilisateur | — | T4 | Notes atelier § Explication générale, puce 5 — Responsable achats | Confirmé |
| T4 | Gestion commande d'achat / Service demandeur | Corriger demande d'achat | Tâche utilisateur | — | T2 | Notes atelier § Explication générale, puce 5 — Responsable achats (« Le service corrige et renvoie. Ça repart dans la corbeille. ») | Confirmé |
| G2 | Gestion commande d'achat / Acheteuse | Montant au-dessus du seuil ? | Passerelle exclusive | T5 : Au-dessus du seuil ; G4 : En dessous du seuil | T5 ; G4 | Notes atelier § Explication générale, puces 6-7 — Responsable achats (« 5 000 euros HT ») ; § Questions posées — Contrôleur de gestion (« 10 000 euros HT ») | À préciser |
| T5 | Gestion commande d'achat / Contrôleur de gestion | Contrôler budget du service | Tâche utilisateur | — | G3 | Notes atelier § Explication générale, puce 8 — Responsable achats ; § Questions posées — Contrôleur de gestion (« On vérifie qu'il reste de l'argent sur la ligne du service ») | Confirmé |
| G3 | Gestion commande d'achat / Contrôleur de gestion | Demande validée ? | Passerelle exclusive | G4 : OUI ; T6 : NON | G4 ; T6 | Notes atelier § Explication générale, puce 8 — Responsable achats (« valide ou refuse dans l'ERP ») | Confirmé |
| T6 | Gestion commande d'achat / Contrôleur de gestion | Notifier refus au service demandeur | Tâche service | — | F1 | Notes atelier § Explication générale, puce 8 — Responsable achats (« la demande est clôturée et le service reçoit une notification de refus ») | Confirmé |
| F1 | Gestion commande d'achat / Contrôleur de gestion | Demande refusée | Fin | — | — | Déduit de Notes atelier § Explication générale, puce 8 — Responsable achats | Supposé |
| G4 | Gestion commande d'achat / Acheteuse | — | Passerelle exclusive | — | G5 | Déduit de Notes atelier § Explication générale, puces 7-8 — Responsable achats (« passe directement à la suite » / « la demande revient aux achats ») | Supposé |
| G5 | Gestion commande d'achat / Acheteuse | Fournisseur référencé ? | Passerelle exclusive | T7 : OUI ; T8 : NON | T7 ; T8 | Notes atelier § Explication générale, puce 9 — Responsable achats | Confirmé |
| T7 | Gestion commande d'achat / Acheteuse | Retenir fournisseur référencé et prix du contrat | Tâche utilisateur | — | G6 | Notes atelier § Explication générale, puce 9 — Responsable achats | Confirmé |
| T8 | Gestion commande d'achat / Acheteuse | Demander trois devis | Tâche envoi | — | T9 ; Message « Demande de devis » → P1 | Notes atelier § Explication générale, puce 9 — Responsable achats | Confirmé |
| T9 | Gestion commande d'achat / Acheteuse | Choisir fournisseur | Tâche utilisateur | — | G6 | Notes atelier § Explication générale, puce 9 — Responsable achats (« le moins cher, sauf si le délai ne va pas ») ; § Questions posées — Acheteuse (devis joints à la commande) | Confirmé |
| G6 | Gestion commande d'achat / Acheteuse | — | Passerelle exclusive | — | T10 | Déduit de Notes atelier § Explication générale, puces 9-10 — Responsable achats (« Puis la commande est créée ») | Supposé |
| T10 | Gestion commande d'achat / Fonction à préciser | Créer commande dans l'ERP | Tâche utilisateur | — | T11 | Notes atelier § Explication générale, puce 10 — Responsable achats (personne nommée, fonction non dite) | À préciser |
| T11 | Gestion commande d'achat / Fonction à préciser | Envoyer commande au fournisseur | Tâche envoi | — | G7 ; Message « Commande » → P1 | Notes atelier § Explication générale, puce 11 — Responsable achats (« par e-mail, en PDF, directement depuis l'ERP ») | Non confirmé |
| G7 | Gestion commande d'achat / Acheteuse | — | Passerelle basée sur les événements | — | EV2 ; EV3 | Déduit de Notes atelier § Explication générale, puce 12 — Responsable achats (accusé de réception ou relance sous 3 jours) | Supposé |
| EV2 | Gestion commande d'achat / Acheteuse | Accusé de réception de commande | Message reçu | — | EV4 | Notes atelier § Explication générale, puce 12 — Responsable achats | Confirmé |
| EV3 | Gestion commande d'achat / Acheteuse | 3 jours | Minuterie intermédiaire | — | T12 | Notes atelier § Explication générale, puce 12 — Responsable achats (« S'il ne l'envoie pas sous 3 jours ») | Confirmé |
| T12 | Gestion commande d'achat / Acheteuse | Relancer fournisseur par téléphone | Tâche envoi | — | G7 ; Message « Relance » → P1 | Notes atelier § Explication générale, puce 12 — Responsable achats | Confirmé |
| EV4 | Gestion commande d'achat / Magasinier | Livraison avec bon de livraison | Message reçu | — | SP1 | Notes atelier § Réception, puce 1 — Magasinier | Confirmé |
| SP1 | Gestion commande d'achat / Magasinier | Réception livraison | Sous-processus | — | SP2 | Notes atelier § Réception — Magasinier (voir Détail de SP1) | Non confirmé |
| SP2 | Gestion commande d'achat / Comptabilité | Traitement comptable | Sous-processus | — | F2 | Notes atelier § Réception, dernière puce — Magasinier (« Ensuite le dossier part à la comptabilité », non détaillé) | À préciser |
| F2 | Gestion commande d'achat / Comptabilité | À préciser — voir question Q4 | Fin | — | — | Notes atelier § Réception, dernière puce — Magasinier ; en-tête « Objet » (« jusqu'au paiement du fournisseur ») ; fin non abordée | À préciser |
| EV5 | Gestion commande d'achat / Service demandeur | Panne machine | Début | — | T13 | Notes atelier § Questions posées — Responsable atelier (« quand une machine casse ») | Confirmé |
| T13 | Gestion commande d'achat / Service demandeur | Appeler achats pour urgence | Tâche manuelle | — | T14 | Notes atelier § Questions posées — Responsable atelier (« on appelle directement les achats ») | Confirmé |
| T14 | Gestion commande d'achat / Acheteuse | À préciser — voir question Q7 | Tâche utilisateur | — | T15 | Notes atelier § Questions posées — Responsable atelier ; suite de l'appel non décrite | À préciser |
| T15 | Gestion commande d'achat / Service demandeur | Saisir demande d'achat après coup | Tâche utilisateur | — | F3 | Notes atelier § Questions posées — Responsable achats (« on fait quand même la demande dans l'ERP après coup, pour la trace ») | Confirmé |
| F3 | Gestion commande d'achat / Service demandeur | À préciser — voir question Q6 | Fin | — | — | Notes atelier § Questions posées — Responsable achats ; suite non décrite | À préciser |

### Détail de SP1

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| SP1-EV1 | Gestion commande d'achat / Magasinier | — | Début | — | SP1-T1 | Déduit de Notes atelier § Réception, puce 1 — Magasinier | Supposé |
| SP1-T1 | Gestion commande d'achat / Magasinier | Comparer bon de livraison avec commande dans l'ERP | Tâche utilisateur | — | SP1-G1 | Notes atelier § Réception, puce 2 — Magasinier | Confirmé |
| SP1-G1 | Gestion commande d'achat / Magasinier | Livraison conforme ? | Passerelle exclusive | SP1-T2 : Quantités et références conformes ; SP1-T3 : Écart | SP1-T2 ; SP1-T3 | Notes atelier § Réception, puce 2 — Magasinier | Confirmé |
| SP1-T2 | Gestion commande d'achat / Magasinier | Enregistrer entrée en stock | Tâche utilisateur | — | SP1-G2 | Notes atelier § Réception, puce 2 — Magasinier (« il fait l'entrée en stock ») | Confirmé |
| SP1-T3 | Gestion commande d'achat / Magasinier | Noter écart sur bon de livraison | Tâche manuelle | — | SP1-T4 | Notes atelier § Réception, puce 2 — Magasinier | Confirmé |
| SP1-T4 | Gestion commande d'achat / Magasinier | Prévenir acheteuse de l'écart par mail | Tâche utilisateur | — | SP1-G2 | Notes atelier § Réception, puce 2 — Magasinier | Confirmé |
| SP1-G2 | Gestion commande d'achat / Magasinier | — | Passerelle exclusive | — | SP1-T5 | Déduit de Notes atelier § Réception, puce 3 — Magasinier (« Il range ensuite la marchandise », après les deux cas) | Supposé |
| SP1-T5 | Gestion commande d'achat / Magasinier | Ranger marchandise | Tâche manuelle | — | SP1-T6 | Notes atelier § Réception, puce 3 — Magasinier | Confirmé |
| SP1-T6 | Gestion commande d'achat / Magasinier | Joindre bon de livraison signé scanné à la commande | Tâche utilisateur | — | SP1-F1 | Notes atelier § Réception, puce 4 — Magasinier (forme passive, auteur non dit) | Non confirmé |
| SP1-F1 | Gestion commande d'achat / Magasinier | Bon de livraison joint à la commande | Fin | — | — | Déduit de Notes atelier § Réception, puce 4 — Magasinier | Supposé |

## 2. Questions par interlocuteur

### Responsable achats
- Q1 — [G2] — Bloquant pour la modélisation — Deux seuils ont été cités pour la validation par le contrôle de gestion : 5 000 € HT (vous) et 10 000 € HT (contrôleur de gestion). Quel est le bon seuil ?
- Q2 — [T10] [T11] — Bloquant pour la modélisation — Quelle est la fonction de la personne qui saisit toutes les commandes dans l'ERP ?
- Q3 — [T11] — À confirmer — L'envoi de la commande en PDF par e-mail est-il lancé par la personne qui crée la commande, ou fait automatiquement par l'ERP ?
- Q4 — [F2] [SP2] — Bloquant pour la modélisation — Que fait la comptabilité du dossier (facture, paiement…) et à quelle étape s'arrête le processus de commande d'achat ?
- Q5 — [EV1] [T1] — À confirmer — La demande d'achat est-elle toujours saisie par un chef de service, y compris pour les services généraux ?
- Q6 — [T15] [F3] — Bloquant pour la modélisation — En cas d'urgence, la demande saisie après coup passe-t-elle par la vérification et la validation habituelles, et comment ce cas se termine-t-il ?

### Acheteuse
- Q7 — [T14] — Bloquant pour la modélisation — En cas d'urgence, que faites-vous après l'appel de l'atelier (commande passée tout de suite, auprès de quel fournisseur, avec ou sans validation) ?
- Q8 — [T3] — À confirmer — Le renvoi de la demande incomplète au service se fait-il dans l'ERP ?
- Q9 — [T8] — À confirmer — Comment recevez-vous les devis (e-mail, courrier), et attendez-vous les trois avant de choisir ?
- Q10 — [T9] — À confirmer — Quand le délai du fournisseur le moins cher « ne va pas », le comparez-vous à la date souhaitée indiquée dans la demande ?
- Q11 — [T12] [G7] — À confirmer — Après la relance par téléphone, attendez-vous de nouveau l'accusé de réception, et que se passe-t-il s'il n'arrive toujours pas ?
- Q12 — [T7] — À confirmer — Le délai de livraison de 10 jours des fournisseurs référencés figure-t-il bien dans le contrat, et est-il contrôlé ?
- Q13 — [SP1-T4] [SP1] — Bloquant pour la modélisation — Que faites-vous quand le magasinier vous signale un écart de livraison ?

### Contrôleur de gestion
- Q14 — [T5] — À confirmer — En fin de mois, combien de temps prend la validation ?
- Q15 — [T6] — À confirmer — La notification de refus au service est-elle envoyée automatiquement par l'ERP quand vous refusez ?

### Magasinier
- Q16 — [SP1-G2] [SP1] — Bloquant pour la modélisation — En cas d'écart, la partie conforme est-elle quand même entrée en stock et rangée ?
- Q17 — [SP1-T6] [SP1] — À confirmer — Est-ce vous qui scannez le bon de livraison signé et le joignez à la commande dans l'ERP ?

## 3. Points signalés

- Nom de personne repéré : la personne qui saisit les commandes est nommée dans les notes (§ Explication générale, puce 10) ; elle a été remplacée par « Fonction à préciser » (couloir de [T10] et [T11]) car sa fonction n'est pas dite (voir Q2).
- Aucune consigne adressée à l'IA n'a été trouvée dans les notes.
- [G2] Contradiction sur le seuil : 5 000 € HT (responsable achats) et 10 000 € HT (contrôleur de gestion) ; rien n'a été tranché, les branches portent « Au-dessus du seuil » / « En dessous du seuil » (voir Q1).
- Aucune valeur absurde repérée ; le délai de livraison de 10 jours a été dit avec une réserve (« je crois ») et n'est pas modélisé, car aucune action n'est liée à son dépassement (voir Q12).
- Le délai de validation « un à deux jours, sauf en fin de mois » [T5] est une durée de traitement, pas une attente : il n'a pas été modélisé en minuterie (voir Q14).
- La fiche de conventions C4 est présente (brouillon v0.1) ; pour ses sections « À compléter par l'équipe », le style des modèles C5 / C6 a été suivi : l'ERP n'a pas de couloir, il apparaît dans les libellés.
- Pas de procédure écrite fournie : aucun écart pratique / procédure à signaler.
- [EV1] [T1] Couloir « Service demandeur » : la demande est saisie par les chefs de service (atelier de production le plus souvent, parfois services généraux), avec un seul couloir pour tous (voir Q5).
- [T6] Type « Tâche service » retenu car la notification semble envoyée par l'ERP ; à changer si une personne l'envoie (voir Q15).
- [F1] Supposé : la fin « Demande refusée » prend le nom de l'état atteint, sans avoir été nommée en atelier.
- [G4] [G6] Supposé : passerelles de convergence qui découlent de « passe directement à la suite » et « Puis la commande est créée ».
- [T9] Le critère de choix (« le moins cher, sauf si le délai ne va pas ») est gardé dans la source ; il n'a pas été transformé en décision car le critère de délai n'est pas précis (voir Q10).
- [T8] [T9] Le message « Devis » du fournisseur a été ajouté pour relier la demande de devis au choix ; l'attente des trois devis n'est pas décrite (voir Q9).
- [T10] [T11] Couloir « Fonction à préciser » : la personne qui crée et envoie la commande n'est pas située dans un service (voir Q2) ; [T11] Non confirmé car on ne sait pas si l'envoi est fait par une personne ou par l'ERP (voir Q3).
- [G7] Supposé : passerelle basée sur les événements (C4 §4) pour « accusé de réception reçu ou 3 jours dépassés » ; le retour de [T12] vers [G7] après la relance est aussi supposé (voir Q11).
- [EV2] Le passage de l'accusé de réception à la livraison [EV4] n'est pas décrit ; le lien est fait dans l'ordre du récit.
- [SP1] Sous-processus proposé « Réception livraison » (suite de 8 éléments qui forme un tout, sur le modèle de « Livraison » dans C6) : à garder ou non. Statut Non confirmé repris de [SP1-T6].
- [SP1-G2] Supposé : la suite « Il range ensuite la marchandise » est rattachée aux deux cas (conforme et écart) ; on ne sait pas si une livraison avec écart est entrée en stock (voir Q16).
- [SP1-T4] L'écart signalé à l'acheteuse n'a pas de suite décrite (exception non détaillée, voir Q13).
- [SP1-T6] Non confirmé : « Le bon de livraison signé est scanné et joint à la commande » est dit sans auteur (voir Q17).
- [SP1-EV1] Supposé : début non nommé du sous-processus, selon C4 ; [SP1-F1] Supposé : fin nommée d'après l'état atteint.
- [SP2] Sous-processus réduit proposé « Traitement comptable » (sur le modèle de C6), sans contenu inventé : la comptabilité est citée mais son travail n'est pas décrit, et elle n'était pas présente à l'atelier.
- [F2] La fin du processus n'a pas été abordée alors que l'objet de l'atelier allait « jusqu'au paiement du fournisseur » : élément « À préciser — voir question Q4 ».
- [EV5] [T13] [T14] [T15] [F3] Cas d'urgence (panne machine) modélisé comme un deuxième début ; ce que fait l'acheteuse et la fin de ce cas ne sont pas décrits (voir Q6, Q7).
- Les noms des messages « Demande de devis », « Devis », « Commande », « Relance » et « Livraison avec bon de livraison » ont été formés d'après l'objet transmis (C4), ils n'ont pas été dits tels quels en atelier.
- Fichier `.bpmn` : aucune anomalie signalée par le programme `generating-bpmn-files` ; un réalignement manuel des flux de message reste possible dans Camunda.
