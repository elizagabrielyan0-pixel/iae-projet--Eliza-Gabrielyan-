> ⚠️ Alerte : 2 noms de personnes ont été trouvés dans les notes d'atelier « E3-notes-lacunaires-achats.md » (en-tête, puces 3 et 5), alors qu'ils étaient annoncés comme remplacés. Ils ont été remplacés par leur fonction (Responsable achats, Contrôle de gestion) ; anonymisez le fichier source.
> ⚠️ Alerte : 9 informations manquent pour finir le diagramme (questions Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q12, Q13). Elles apparaissent en « À préciser » ou « Non confirmé » dans le fichier BPMN.

## 1. Tableau du processus

| ID | Participant / Couloir | Libellé | Type BPMN | Condition | Élément suivant | Source | Statut |
|---|---|---|---|---|---|---|---|
| EV1 | Gestion demande d'achat / Service demandeur | Besoin d'achat | Début | — | T1 | Notes atelier puce 1 — intervenant non noté (« Un service a besoin de quelque chose ») | Confirmé |
| T1 | Gestion demande d'achat / Service demandeur | Faire demande d'achat | Tâche utilisateur | — | T2 | Notes atelier puce 1 — intervenant non noté (« il fait une demande d'achat (formulaire ? mail ? pas clair) ») | Confirmé |
| T2 | Gestion demande d'achat / Service achats | Vérifier cohérence demande | Tâche utilisateur | — | G1 | Notes atelier puce 2 — intervenant non noté (« On vérifie que c'est cohérent ») | Confirmé |
| G1 | Gestion demande d'achat / Service achats | Montant supérieur au seuil ? | Passerelle exclusive | T3 : OUI ; G2 : NON | T3 ; G2 | Notes atelier puce 3 — intervenant non noté (« Au-dessus d'un certain montant ») ; seuil non donné (Questions restées sans réponse) | À préciser |
| T3 | Gestion demande d'achat / Contrôle de gestion | Valider demande d'achat | Tâche utilisateur | — | G2 | Notes atelier puce 3 — Contrôle de gestion (« en général c'est nous, mais pas toujours ») | Non confirmé |
| G2 | Gestion demande d'achat / Service achats | — | Passerelle exclusive | — | G3 | Déduit de Notes atelier puce 3 — validation seulement au-dessus d'un certain montant | Supposé |
| G3 | Gestion demande d'achat / Service achats | Demande acceptée ? | Passerelle exclusive | G4 : OUI ; F1 : NON | G4 ; F1 | Notes atelier puce 6 — intervenant non noté (« Parfois la demande est refusée ») ; étape du refus non dite | À préciser |
| F1 | Gestion demande d'achat / Service achats | À préciser — voir question Q5 | Fin | — | — | Notes atelier puce 6 — intervenant non noté (« Ce qui se passe ensuite n'a pas été abordé ») | À préciser |
| G4 | Gestion demande d'achat / Service achats | Fournisseur référencé ? | Passerelle exclusive | T4 : OUI ; SP1 : NON | T4 ; SP1 | Notes atelier puces 4 et 5 — Responsable achats (puce 5) | Confirmé |
| T4 | Gestion demande d'achat / À préciser — voir question Q6 | Créer commande dans SAP | Tâche utilisateur | — | G5 | Notes atelier puce 4 — intervenant non noté (« Qui la crée ? → réponse non notée ») | À préciser |
| SP1 | Gestion demande d'achat / Service achats | Traitement fournisseur non référencé | Sous-processus | — | G5 | Notes atelier puce 5 — Responsable achats (« là on fait autrement », non détaillé) | À préciser |
| G5 | Gestion demande d'achat / Service achats | — | Passerelle exclusive | — | T5 | Aucune : la suite du cas « fournisseur non référencé » n'a pas été décrite | À préciser |
| T5 | Gestion demande d'achat / Magasin | Réceptionner marchandise | Tâche manuelle | — | F2 | Notes atelier puce 7 — intervenant non noté (« le magasin s'en occupe ») | Confirmé |
| F2 | Gestion demande d'achat / Magasin | À préciser — voir question Q9 | Fin | — | — | Notes atelier puce 8 — intervenant non noté (« Fin du processus ? Paiement fournisseur ? Pas abordé ») | À préciser |

## 2. Questions par interlocuteur

### Responsable achats
- Q1 — [T1] — À confirmer — Le service demandeur transmet-il sa demande d'achat par un formulaire (dans SAP ou dans un autre outil) ou par mail ?
- Q2 — [T2] — À confirmer — La vérification de la cohérence de la demande par le service achats se fait-elle dans SAP ?
- Q3 — [G1] — Bloquant pour la modélisation — À partir de quel montant (et dans quelle devise) une demande d'achat doit-elle être envoyée en validation ?
- Q4 — [G3] [F1] — Bloquant pour la modélisation — Une demande peut-elle être refusée lors de la vérification par les achats, lors de la validation au-dessus du seuil, ou aux deux étapes ?
- Q5 — [F1] — Bloquant pour la modélisation — Quand une demande est refusée, le service demandeur en est-il informé, et la demande est-elle close ou peut-elle être corrigée puis renvoyée ?
- Q6 — [T4] — Bloquant pour la modélisation — Quand le fournisseur est référencé, la commande dans SAP est-elle créée par le service achats, par le service demandeur ou par un autre service ?
- Q7 — [SP1] — Bloquant pour la modélisation — Pourriez-vous décrire les étapes suivies quand le fournisseur n'est pas référencé ?
- Q8 — [G5] [SP1] — Bloquant pour la modélisation — Après le traitement d'un fournisseur non référencé, la marchandise est-elle elle aussi réceptionnée par le magasin ?
- Q9 — [F2] — Bloquant pour la modélisation — Pour cette cartographie, le processus s'arrête-t-il à la réception de la marchandise par le magasin, ou va-t-il jusqu'au paiement du fournisseur ?
- Q10 — [G4] — À confirmer — Le contrôle du référencement du fournisseur a-t-il bien lieu après la validation de la demande, et non avant ?
- Q11 — [T4] — À confirmer — Une fois créée dans SAP, la commande est-elle envoyée au fournisseur et, si oui, par qui et par quel moyen ?
- Q12 — [T2] — Bloquant pour la modélisation — Existe-t-il un délai de traitement d'une demande d'achat et, si oui, quelle est sa durée et entre quelles étapes est-il compté ?

### Contrôle de gestion
- Q13 — [T3] — Bloquant pour la modélisation — Au-dessus du seuil, quand ce n'est pas le contrôle de gestion qui valide la demande, qui la valide et dans quels cas ?
- Q14 — [T3] — À confirmer — La validation de la demande d'achat se fait-elle dans SAP ou par un autre moyen (mail, signature) ?

### Interlocuteur à identifier (magasin)
- Q15 — [T5] — À confirmer — La réception de la marchandise par le magasin donne-t-elle lieu à une saisie dans SAP ?

## 3. Points signalés

- Noms de personnes repérés dans les notes (en-tête, puces 3 et 5) alors qu'ils étaient annoncés comme remplacés : « Mme Durand » remplacée par « Responsable achats » et « M. Petit » par « Contrôle de gestion » ; anonymisation du fichier source à reprendre.
- Aucune consigne adressée à l'IA repérée dans les sources.
- Aucune valeur absurde ou incohérente repérée : les notes ne donnent aucun chiffre (ni seuil, ni délai).
- Aucune contradiction entre intervenants repérée.
- Une seule source (notes d'atelier C1, sans PDF ni transcription) : aucun écart pratique / procédure et aucune lecture incertaine.
- C4 est un brouillon v0.1 : pour les sections « À COMPLÉTER PAR L'ÉQUIPE » (représentation de SAP, position des participants), le style des modèles C5 / C6 a été suivi.
- Atelier écourté et notes rapides : la plupart des puces ne disent pas qui parle, la source porte alors « intervenant non noté ».
- Le contrôle de gestion n'était présent que la première demi-heure : ses informations se limitent à la puce 3.
- [EV1] Début simple (non message) : la demande vient d'un service interne, pas d'un acteur externe.
- [T1] Type « Tâche utilisateur » retenu par défaut, le support de la demande (formulaire ou mail) n'étant pas clair (voir Q1).
- [G1] Seuil de validation non donné : la décision est gardée avec des branches « OUI » / « NON » sans montant (voir Q3).
- [T3] Non confirmé : le contrôle de gestion valide « en général, mais pas toujours » ; l'autre validateur est inconnu (voir Q13).
- [G2] Supposé : passerelle qui referme la branche de validation, déduite de « au-dessus d'un certain montant ».
- [G3] Décision de refus placée après la validation, faute de mieux ; l'étape où le refus a lieu n'a pas été dite (voir Q4).
- [F1] Fin du cas « refus » non abordée en atelier : libellé « À préciser — voir question Q5 », sans état final inventé.
- [G4] Ordre supposé d'après l'ordre des notes (référencement après validation) ; décision placée dans le couloir « Service achats », car c'est la responsable achats qui décrit les deux cas (voir Q10 et Q6).
- [T4] Acteur inconnu : la tâche est mise dans un couloir « À préciser — voir question Q6 » plutôt que d'inventer un service.
- [SP1] Sous-processus réduit proposé (C4 §3, partie mentionnée sans être décrite), sans contenu inventé : à garder ou non (voir Q7).
- [G5] Passerelle de convergence « À préciser » : rien ne dit que le cas « fournisseur non référencé » mène aussi à la réception (voir Q8).
- [T5] Type « Tâche manuelle » retenu (action physique du magasin) ; une saisie dans SAP la ferait passer en tâche utilisateur (voir Q15).
- [F2] Frontière du processus non définie (« Fin du processus ? Pas abordé ») : libellé « À préciser — voir question Q9 » ; seule la partie vue en atelier (jusqu'à la réception) est modélisée.
- Aucun participant externe créé : le fournisseur est cité, mais aucun échange avec lui n'a été décrit (voir Q11).
- Aucune minuterie modélisée : le délai de traitement est resté sans réponse et son point de départ est inconnu (voir Q12).
- Aucun sous-processus repris de C5 / C6 : aucune partie du processus ne correspond à un sous-processus des modèles.
- Fichier `.bpmn` : aucune anomalie signalée par la génération (programme terminé avec le code 0 ; 14 éléments, 15 flux, 7 annotations) ; réalignement manuel possible dans Camunda.
