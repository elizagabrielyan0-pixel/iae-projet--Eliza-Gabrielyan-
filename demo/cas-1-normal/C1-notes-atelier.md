# C1 — Notes d'atelier — Gestion des réclamations clients (as-is)

**Source :** C1 — notes Word de la consultante
**Client :** Maison Lumen (vente en ligne de luminaires) — données inventées pour la démonstration
**Atelier :** traitement des réclamations clients, de la réception au règlement
**Participants côté client :** responsable du service client, conseillère service client, responsable qualité, comptable

---

## Explication générale (responsable du service client)

- Tout commence quand un client envoie une réclamation par e-mail (produit cassé, produit non conforme, colis incomplet).
- La conseillère service client enregistre la réclamation dans le CRM.
- Elle vérifie ensuite la commande du client dans le CRM (date d'achat, produit, photos envoyées).
- Elle décide si la réclamation est recevable : la commande a moins de 30 jours et le problème est prouvé par une photo.
  - Si la réclamation n'est pas recevable, elle envoie au client un e-mail de refus motivé. La réclamation est close « refusée ».
  - Si elle est recevable, elle demande au client s'il préfère un remboursement ou un échange.

## Cas du remboursement

- Si le montant à rembourser est inférieur ou égal à 200 €, la conseillère prépare directement la demande de remboursement.
- Au-dessus de 200 €, le responsable qualité doit valider le remboursement avant.
  - S'il refuse, la conseillère envoie un e-mail de refus au client et la réclamation est close « refusée ».
  - S'il valide, la conseillère prépare la demande de remboursement.
- Le comptable effectue le remboursement par virement.
- La conseillère envoie au client un e-mail de confirmation du remboursement. La réclamation est close « remboursée ».

## Cas de l'échange

- La conseillère crée une commande d'échange dans le CRM et envoie au client une étiquette de retour.
- Le client renvoie le produit défectueux.
- Quand le produit revient, la conseillère expédie le produit de remplacement. La réclamation est close « échangée ».

## Questions posées et réponses

- **Q : Que se passe-t-il si le client ne renvoie pas le produit ?**
  R (conseillère) : au bout de 14 jours sans retour, on envoie une relance au client.
- **Q : Et si, après la relance, il ne renvoie toujours rien ?**
  R (conseillère) : 7 jours après la relance, on annule l'échange. La réclamation est close « échange annulé ».
- **Q : Qui fixe le seuil de 200 € ?**
  R (responsable du service client) : c'est la règle interne depuis deux ans, elle est appliquée tout le temps.
- **Q : Le comptable informe-t-il le client ?**
  R (comptable) : non, je fais seulement le virement ; c'est la conseillère qui prévient le client.
