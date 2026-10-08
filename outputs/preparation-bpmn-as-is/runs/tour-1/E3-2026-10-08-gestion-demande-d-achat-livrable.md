## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| EV1 | Gestion demande d'achat / Service demandeur | Besoin d'achat | Début | — | T1 | Notes atelier puce 1 — intervenant non noté | Confirmé |
| T1 | Gestion demande d'achat / Service demandeur | Faire demande d'achat | Tâche utilisateur | — | T2 | Notes atelier puce 1 — intervenant non noté (« formulaire ? mail ? pas clair ») | Confirmé |
| T2 | Gestion demande d'achat / Service achats | Vérifier cohérence demande | Tâche utilisateur | — | G1 | Notes atelier puce 2 — intervenant non noté (« On vérifie que c'est cohérent ») | Confirmé |
| G1 | Gestion demande d'achat / Service achats | Demande acceptée ? | Passerelle exclusive | G2 : OUI ; AP1 : NON | G2 ; AP1 | Notes atelier puce 6 — intervenant non noté (« Parfois la demande est refusée ») ; place dans le processus non précisée | À préciser |
| AP1 | Gestion demande d'achat / Service achats | À préciser — voir question Q4 | Fin | — | — | Notes atelier puce 6 (« Ce qui se passe ensuite n'a pas été abordé ») | À préciser |
| G2 | Gestion demande d'achat / Service achats | Montant supérieur au seuil ? | Passerelle exclusive | T3 : OUI ; G3 : NON | T3 ; G3 | Notes atelier puce 3 — intervenant non noté (« Au-dessus d'un certain montant ») | Confirmé |
| T3 | Gestion demande d'achat / Contrôle de gestion | Valider demande d'achat | Tâche utilisateur | — | G3 | Notes atelier puce 3 — Représentant du contrôle de gestion (« en général c'est nous, mais pas toujours ») | Non confirmé |
| G3 | Gestion demande d'achat / Service achats | — | Passerelle exclusive | — | G4 | Déduit de Notes atelier puce 3 (validation seulement au-dessus du montant) | Supposé |
| G4 | Gestion demande d'achat / Service achats | Fournisseur référencé ? | Passerelle exclusive | T4 : OUI ; SP1 : NON | T4 ; SP1 | Notes atelier puces 4 et 5 — Responsable achats pour la puce 5 | Confirmé |
| T4 | Gestion demande d'achat / À préciser — voir question Q5 | Créer commande dans SAP | Tâche utilisateur | — | G5 | Notes atelier puce 4 — intervenant non noté (« Qui la crée ? → réponse non notée ») | À préciser |
| SP1 | Gestion demande d'achat / Service achats | Traitement fournisseur non référencé | Sous-processus | — | G5 | Notes atelier puce 5 — Responsable achats (« là on fait autrement », non détaillé) | À préciser |
| G5 | Gestion demande d'achat / Service achats | — | Passerelle exclusive | — | T5 | Aucune (suite du cas « fournisseur non référencé » non décrite) | À préciser |
| T5 | Gestion demande d'achat / Magasin | Réceptionner marchandise | Tâche manuelle | — | AP2 | Notes atelier puce 7 — intervenant non noté (« le magasin s'en occupe ») | Confirmé |
| AP2 | Gestion demande d'achat / Magasin | À préciser — voir question Q9 | Fin | — | — | Notes atelier puce 8 (« Fin du processus ? Paiement fournisseur ? Pas abordé ») | À préciser |

## 2. Questions par interlocuteur

### Responsable achats
- Q1 — [T1] — À confirmer — Le service demandeur fait-il sa demande d'achat par un formulaire (dans SAP ou un autre outil) ou par mail ?
- Q2 — [T2] — À confirmer — Pourriez-vous préciser ce que vous contrôlez quand vous vérifiez la cohérence d'une demande, et si ce contrôle se fait dans SAP ?
- Q3 — [G1] — Bloquant pour la modélisation — Une demande peut-elle être refusée lors de la vérification par les achats, lors de la validation au-dessus du seuil, ou aux deux étapes ?
- Q4 — [AP1] [G1] — Bloquant pour la modélisation — Quand une demande est refusée, le service demandeur en est-il informé, et la demande est-elle close ou peut-elle être corrigée puis renvoyée ?
- Q5 — [T4] — Bloquant pour la modélisation — Quand le fournisseur est référencé, la commande dans SAP est-elle créée par le service achats ou par un autre service ?
- Q6 — [SP1] — Bloquant pour la modélisation — Pourriez-vous décrire les étapes suivies quand le fournisseur n'est pas référencé ?
- Q7 — [G5] [SP1] — À confirmer — Après le traitement d'un fournisseur non référencé, la demande aboutit-elle elle aussi à une réception de la marchandise par le magasin ?
- Q8 — [T4] — À confirmer — La commande créée dans SAP est-elle transmise au fournisseur et, si oui, par qui et sous quelle forme ?
- Q9 — [AP2] — Bloquant pour la modélisation — Pour cette cartographie, le processus s'arrête-t-il à la réception de la marchandise par le magasin, ou va-t-il jusqu'au paiement du fournisseur ?
- Q10 — [T2] — À confirmer — Existe-t-il un délai de traitement d'une demande d'achat et, si oui, quelle est sa durée et à partir de quelle étape est-il compté ?

### Représentant du contrôle de gestion
- Q11 — [G2] — À confirmer — À partir de quel montant une demande d'achat doit-elle être validée ?
- Q12 — [T3] — Bloquant pour la modélisation — Au-dessus de ce montant, qui valide la demande quand ce n'est pas le contrôle de gestion, et dans quels cas ?
- Q13 — [T3] — À confirmer — La validation de la demande se fait-elle dans SAP ou par un autre moyen (mail, signature) ?

### Interlocuteur à identifier (magasin)
- Q14 — [T5] — À confirmer — La réception de la marchandise par le magasin donne-t-elle lieu à une saisie dans SAP ?

## 3. Points signalés

- Noms de personnes repérés dans les notes (en-tête et puces 3 et 5) alors qu'ils étaient annoncés comme remplacés : « Mme Durand » remplacée par « Responsable achats », « M. Petit » par « Représentant du contrôle de gestion » ; rappel d'anonymisation à vérifier dans le fichier source.
- Aucune consigne adressée à l'IA repérée dans les sources.
- Une seule source (notes d'atelier C1) : pas de PDF ni de transcription, donc aucun écart pratique / procédure et aucune lecture incertaine.
- C4 est un brouillon v0.1 : sur les sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation de SAP, position des participants), le style des modèles C5 / C6 a été suivi.
- Atelier écourté et notes prises rapidement : la plupart des puces ne disent pas qui parle, la source porte alors « intervenant non noté ».
- Le représentant du contrôle de gestion n'était présent que la première demi-heure : les informations des puces suivantes ne peuvent venir que de la responsable achats ou d'un intervenant non noté.
- [G1] La décision de refus est placée après la vérification par les achats faute de mieux ; sa vraie place n'a pas été dite (voir Q3).
- [AP1] Fin « À préciser » ajoutée pour la suite d'un refus, non abordée en atelier (voir Q4).
- [G2] Seuil non chiffré : les branches sont notées « OUI » / « NON » sans montant (voir Q11).
- [T3] Non confirmé : le contrôle de gestion valide « en général, mais pas toujours » ; l'autre validateur est inconnu (voir Q12).
- [G3] Supposé : passerelle qui referme la branche de validation, déduite de « au-dessus d'un certain montant ».
- [T4] Acteur inconnu : la tâche est placée dans un couloir « À préciser — voir question Q5 » plutôt que d'inventer un service.
- [SP1] Sous-processus réduit proposé (C4 §3, partie mentionnée sans être décrite) : à garder ou non, son contenu est à recueillir (voir Q6).
- [G5] Passerelle de convergence « À préciser » ajoutée : rien ne dit que le cas « fournisseur non référencé » mène aussi à la réception (voir Q7).
- [T1] Type « Tâche utilisateur » retenu par défaut, le support de la demande (formulaire ou mail) n'étant pas clair (voir Q1).
- [T5] Type « Tâche manuelle » retenu (action physique du magasin) ; une saisie dans SAP la ferait passer en tâche utilisateur (voir Q14).
- Aucun participant externe créé : le fournisseur est cité mais aucun échange avec lui n'a été décrit (voir Q8).
- Aucun délai modélisé : le délai de traitement est resté sans réponse (voir Q10).
- [AP2] Frontière du processus non définie : seule la partie vue en atelier (jusqu'à la réception) est modélisée (voir Q9).
- [G4] Couloir « Service achats » retenu pour la décision, car c'est la responsable achats qui décrit les deux cas.
- Fichier `.bpmn` : aucune anomalie signalée par la génération ; réalignement manuel possible dans Camunda.
