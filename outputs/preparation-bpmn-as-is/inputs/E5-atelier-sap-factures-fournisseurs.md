# Notes d'atelier — Traitement des factures fournisseurs (as-is)

**Sources :** (1) notes Word de la consultante ; (2) extrait de la transcription Teams de l'atelier
**Contexte projet :** migration SAP S/4HANA — volet Finance / Achats (Procure-to-Pay)
**Participants côté client :** Responsable comptabilité fournisseurs, une comptable fournisseurs, acheteur, responsable trésorerie
**Objet :** comprendre comment une facture fournisseur est traitée aujourd'hui, de sa réception à son paiement

---

## Explication générale (responsable comptabilité fournisseurs)

- Les factures arrivent de deux façons : par e-mail sur la boîte « factures@ » (la grande majorité, en PDF) ou par courrier (de moins en moins).
- Les factures papier sont scannées par l'accueil puis déposées dans la même boîte mail.
- La comptable fournisseurs ouvre chaque facture et cherche s'il y a une commande d'achat SAP associée (numéro de commande sur la facture).
  - Facture avec commande : elle saisit la facture dans SAP (transaction MIRO) en la rapprochant de la commande et de l'entrée de marchandises.
  - Facture sans commande (frais généraux, abonnements…) : elle la saisit directement en comptabilité (FB60) et l'envoie par mail au responsable du budget concerné pour validation.
- Lors du rapprochement, si les quantités ou les prix ne correspondent pas à la commande ou à la réception au-delà de la tolérance, SAP bloque la facture au paiement.
  - Dans ce cas la comptable contacte l'acheteur, qui vérifie avec le fournisseur. Soit l'acheteur corrige la commande, soit le fournisseur envoie un avoir.
  - Une fois l'écart résolu, la comptable lève le blocage.
- Les factures validées et non bloquées partent dans la proposition de paiement, lancée par la trésorerie deux fois par semaine (mardi et jeudi).
- La trésorerie contrôle la proposition, puis lance le paiement par virement.

## Questions posées et réponses

- **Q : Quelle est la tolérance d'écart avant blocage ?**
  R (comptable) : 2 % sur le prix, je crois, et aucune sur les quantités. À vérifier dans le paramétrage.
- **Q : Et si le responsable budget ne répond pas pour une facture sans commande ?**
  R (responsable compta) : on relance au bout d'une semaine. Après… honnêtement ça dépend des gens.
- **Q : Qui décide si une facture en litige est payée quand même ?**
  R : réponse non obtenue, l'acheteur avait quitté l'atelier.

---

## Extrait de la transcription Teams (générée automatiquement)

> **Acheteur :** Alors quand la facture est bloquée moi je reçois juste un mail de la compta, il n'y a pas de workflow dans SAP pour ça, c'est vraiment par mail.
>
> **Comptable fournisseurs :** Oui et parfois je relance deux trois fois parce que ça reste en attente.
>
> **Responsable trésorerie :** Et de notre côté on ne voit pas les factures bloquées, on voit juste ce qui sort dans la proposition. Ah et pour les gros montants, au-dessus de 50 000, c'est le DAF qui signe le virement, pas nous.
>
> **Responsable compta :** Euh, je crois que c'est 100 000 maintenant le seuil, non ? Il faudrait vérifier.
