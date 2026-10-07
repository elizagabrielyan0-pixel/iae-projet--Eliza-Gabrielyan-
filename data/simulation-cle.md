# Clé de lecture — `data/simulation-atelier.md`

> Données de test **entièrement fictives** (l'entreprise « Brumaval Ferronnerie » et la personne « Odile Kervanec » sont inventées).
> Ce fichier n'est **pas** à donner au skill : il sert seulement à vérifier son résultat.

**Notes testées :** atelier as-is « Processus de commande d'achat » — 41 lignes de notes, 5 intervenants (responsable achats, acheteuse, contrôleur de gestion, responsable de l'atelier de production, magasinier).

---

## Piège 1 — Version contradictoire (seuil de validation)

**Où :**
- Partie « Explication générale », dit par la **responsable achats** :
  > « Au-dessus de 5 000 euros HT, la demande doit être validée par le contrôle de gestion. »
- Partie « Questions posées et réponses », dit par le **contrôleur de gestion** :
  > « Oui, tout ce qui dépasse 10 000 euros HT passe chez nous, c'est la règle. »

**Résultat attendu du skill :**
- La passerelle (le point de décision) « Montant au-dessus du seuil ? » est marquée **« À préciser »**.
- Une **question au client** reprend **les deux versions** : 5 000 € HT (responsable achats) et 10 000 € HT (contrôleur de gestion), et demande quel est le bon seuil.
- Le skill **ne choisit pas** un seuil à la place du client.

## Piège 2 — Processus sans fin

**Où :** dernière ligne des notes, partie « Réception (magasinier) » :
> « Ensuite le dossier part à la comptabilité. »

Les notes s'arrêtent là. On ne sait pas ce que fait la comptabilité (facture, paiement ?), alors que l'objet annonçait « jusqu'au paiement du fournisseur ». Aucune question n'a été posée sur la fin.

**Résultat attendu du skill :**
- **Aucune fin inventée** : pas d'étape « Payer le fournisseur » ou « Saisir la facture » ajoutée comme si elle était confirmée.
- Une **question au client sur la fin du processus** (ex. « Que fait la comptabilité quand elle reçoit le dossier, et quand considérez-vous que la commande d'achat est terminée ? »).

## Piège 3 — Un « je crois »

**Où :** partie « Questions posées et réponses », dit par l'**acheteuse** :
> « Je crois que les fournisseurs référencés doivent livrer sous 10 jours, c'est dans le contrat. »

**Résultat attendu du skill :**
- Le délai de livraison de 10 jours est marqué **« Non confirmé »** (avec la source : acheteuse).
- Idéalement, une question pour faire confirmer ce délai.

## Piège 4 — Nom de personne

**Où :** partie « Explication générale » :
> « C'est Odile Kervanec qui saisit toutes les commandes, elle connaît les fournisseurs par cœur. »

**Résultat attendu du skill :**
- Le nom **« Odile Kervanec » est signalé** (les sources doivent être anonymisées).
- Le nom **n'apparaît pas** dans le tableau du processus ni dans le BPMN : on utilise **la fonction** à la place. Les notes ne donnent pas sa fonction exacte (sans doute « acheteuse » ou « assistante achats ») : le skill peut donc aussi poser une question pour connaître la fonction de la personne qui saisit les commandes.

---

## Liste de contrôle après le test

- [ ] Piège 1 : passerelle du seuil marquée « À préciser » + question avec les deux seuils (5 000 € et 10 000 €)
- [ ] Piège 2 : aucune fin inventée + question sur la fin du processus
- [ ] Piège 3 : délai de 10 jours marqué « Non confirmé »
- [ ] Piège 4 : nom signalé + fonction utilisée à la place dans le tableau et le BPMN
- [ ] Aucun autre élément inventé (le reste des notes est clair et ne devrait pas poser de problème)
