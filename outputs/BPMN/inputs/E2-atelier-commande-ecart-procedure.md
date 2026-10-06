# Notes d'atelier — Gestion d'une commande client (as-is)

**Sources :** (1) notes Word de la consultante ; (2) extrait de la procédure écrite fournie par le client en PDF, recopié en fin de document
**Participants côté client :** Responsable du service commercial, responsable de production, chef du service comptable, coordinateur transport
**Objet :** processus réel de traitement d'une commande, de la réception à l'encaissement ou à l'annulation

---

## Explication générale (responsable commercial)

- Le client nous envoie sa commande. Le service commercial l'enregistre (la commande passe au statut « Enregistrée »).
- Le service production vérifie le stock et la capacité de production.
  - Si la capacité n'est pas suffisante, on annule la commande (voir plus bas l'annulation).
  - Si le stock et la capacité sont OK, deux choses se font en même temps : le service commercial prépare l'ordre de confirmation, et la production réserve les produits semi-finis.
- Une fois les deux faits, on envoie l'ordre de confirmation au client.
- Le client a 8 jours pour confirmer.
  - S'il confirme (la commande passe « Confirmée »), on lance la fabrication.
  - S'il infirme, ou s'il ne répond pas dans les 8 jours, on annule.

## Fabrication, livraison, paiement (production, comptabilité, transport)

- Quand la fabrication est lancée, la production fait l'assemblage et, en parallèle, la comptabilité crée la facture (facture « Créée »).
- Quand l'assemblage et la facture sont prêts, le service transport s'occupe de la livraison chez le client.
- Après la livraison, la comptabilité attend le règlement du client.
  - Paiement reçu : traitement comptable (rapprochement de la facture), la commande est « Réglée » et terminée.
  - Pas de paiement au bout de 15 jours : le dossier part en gestion du contentieux (comptabilité). Après le contentieux, la commande est considérée comme terminée.

## Annulation (responsable commercial)

- On enregistre l'annulation (commande « Annulée »).
- Si des produits semi-finis avaient été réservés, la production les remet en stock.
- On envoie une notification d'annulation au client.

## Questions posées et réponses

- **Q : Le service approvisionnement intervient-il ?**
  R (production) : pas dans ce processus, il intervient sur les achats fournisseurs, c'est un autre sujet.
- **Q : La facture est-elle vraiment créée avant la livraison ?**
  R (chef comptable) : oui, en pratique on la crée pendant l'assemblage pour gagner du temps, même si la procédure dit autre chose.
- **Q : Le délai de confirmation est-il toujours de 8 jours ?**
  R (commercial) : oui, c'est ce qu'on applique à tout le monde.

---

## Extrait de la procédure écrite du client (PDF « PR-COM-04 Traitement des commandes », p. 3)

> 4.2 — À réception de l'ordre de confirmation, le client dispose de 10 jours calendaires pour confirmer sa commande. Passé ce délai, la commande est annulée.
>
> 4.5 — La facture est émise par le service comptable après confirmation de la livraison par le service transport.
>
> 4.6 — En l'absence de règlement sous 15 jours après livraison, le dossier est transmis au contentieux.
