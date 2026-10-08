# Journal des tests — préparation BPMN as-is

| Date | Scénario | Résultat | Corrections nécessaires |
|---|---|---|---|
| 2026-10-07 | E1 — atelier bibliothèque (premier passage) | Livrable + `.bpmn` produits : 37 éléments (dont 1 participant externe), 11 questions (1 bloquante), 12 points signalés ; fichier ouvert sans erreur dans bpmn-js | Aucune sur le skill ; réalignement manuel du flux de message de F2 dans Camunda |
| 2026-10-08 | preparation-bpmn-as-is — E1 atelier bibliothèque (premier passage) | Livrable + `.bpmn` produits : 24 éléments au tableau principal (dont 1 participant externe) + 20 en détail de SP1/SP2, 3 sous-processus, 11 questions (1 bloquante), 23 points signalés ; fichier lu sans avertissement par bpmn-moddle | Aucune sur le skill ; réalignement manuel des flux de message de SP1 dans Camunda |
| 2026-10-08 | preparation-bpmn-as-is — E2 atelier commande, écart procédure (premier passage) | Livrable + `.bpmn` produits : 36 lignes au tableau principal (35 éléments + 1 participant externe), 4 sous-processus réduits repris de C6, 13 questions (1 bloquante), 31 points signalés ; 2 écarts pratique / procédure signalés (8 j vs 10 j, facture avant livraison) ; fichier lu sans avertissement par bpmn-moddle | Aucune sur le skill ; réalignement manuel des flux de message et de la partie annulation dans Camunda |
