# Rapport d'opportunités IA

| | |
|---|---|
| **Rôle** | Consultante SAP en alternance, KPMG (Conseil / Technology Consulting) |
| **Date** | 2026-10-05 |
| **Angle** | Individuel |
| **Opportunités identifiées** | 5 |
| **Recommandation principale** | Premier jet de BPMN « as-is » : c'est la tâche la plus chronophage (environ une semaine par processus), et l'IA peut faire la structuration à votre place. |

> **Outils autorisés :** outil IA interne KPMG et Microsoft Copilot (Teams, Excel, PowerPoint). Toutes les pistes ci-dessous se limitent à ces deux outils. Avant d'y mettre des données d'un client, vérifiez que le contrat ou les règles du projet n'interdisent pas l'usage de l'IA (certains clients l'excluent). En cas de doute, anonymisez les données.

## Tableau de synthèse

| # | Opportunité | Autonomie | Implication | Impact |
|---|------------|----------|-------------|--------|
| 1 | Premier jet de BPMN « as-is » | Guided | Augmented | High |
| 2 | Présentation de comité depuis le suivi Excel | Guided | Augmented | High |
| 3 | Qualification des demandes client | Guided | Augmented | Medium |
| 4 | Compte rendu de réunion structuré | Guided | Augmented | Medium |
| 5 | Mise à jour des fichiers de suivi Excel | Deterministic | Augmented | Medium |

## Recommandations prioritaires

1. **Premier jet de BPMN « as-is ».** C'est votre plus gros gisement de temps. Les données d'entrée (explications et réponses de l'atelier) sont exactement ce que l'IA sait mettre en ordre.
2. **Présentation de comité depuis le suivi Excel.** Elle se répète à chaque comité avec la même structure, donc chaque amélioration se rentabilise plusieurs fois.
3. **Compte rendu de réunion structuré.** C'est un gain rapide et facile à mettre en place dans Teams. Les comptes rendus alimentent ensuite le suivi Excel et les comités.

## Fiches détaillées

### Deterministic

---

**5. Mise à jour des fichiers de suivi Excel**

**Autonomie :** Deterministic
**Implication :** Augmented

**Pourquoi c'est un bon candidat :**
La structure des fichiers est fixe (colonnes, statuts, responsables, dates). La mise à jour applique des règles simples à des informations qui existent déjà ailleurs : comptes rendus, demandes client, e-mails.

**Point de douleur actuel :**
Il faut ressaisir à la main des informations déjà écrites ailleurs. On oublie des lignes, les statuts ne sont pas cohérents d'un fichier à l'autre, et ces fichiers alimentent ensuite les comités.

**Comment l'IA aide :**
À partir d'un compte rendu ou d'une liste de demandes, l'IA produit les lignes à ajouter ou à modifier, dans le format exact de votre fichier (mêmes colonnes, mêmes valeurs de statut). Vous vérifiez, puis vous collez ou validez.

**Pour démarrer cette semaine :**
Dans Copilot, donnez l'en-tête de votre fichier de suivi (noms des colonnes et valeurs autorisées) avec un compte rendu récent. Demandez un tableau « lignes à créer / lignes à mettre à jour » au même format. Notez ce qu'il faut corriger : cela deviendra vos règles.

---

### Guided

---

**1. Premier jet de BPMN « as-is »**

**Autonomie :** Guided
**Implication :** Augmented

**Pourquoi c'est un bon candidat :**
La matière de départ est du langage (explications du client, réponses à vos questions). Le livrable suit une norme très structurée (BPMN 2.0 : couloirs, tâches, passerelles, événements). Camunda travaille dans ce format XML standard, ce qui permet d'importer un brouillon généré.

**Point de douleur actuel :**
Il faut environ une semaine par processus. La plus grande partie du temps sert à reconstruire l'ordre des étapes, les acteurs et les exceptions à partir des notes d'atelier, à repérer ce qui manque, puis à tout dessiner.

**Comment l'IA aide :**
L'IA prend vos notes d'atelier et en tire :
1. une description structurée du processus : acteurs, étapes dans l'ordre, décisions et leurs conditions, exceptions ;
2. la liste des **points flous ou manquants** à faire confirmer par le client ;
3. un brouillon de fichier `.bpmn` (XML BPMN 2.0) à ouvrir dans Camunda Modeler pour le retoucher.

Vous gardez la main sur la validation métier et la mise en forme finale.

**Pour démarrer cette semaine :**
Reprenez les notes d'un atelier déjà traité. Demandez à l'outil interne KPMG un tableau « couloir / étape / passerelle / condition / étape suivante », plus la liste des questions ouvertes. Comparez avec le BPMN que vous avez réellement produit. Quand ce tableau est fiable, passez à l'étape suivante : demandez le XML BPMN 2.0 complet, section de diagramme incluse, et testez l'import dans Camunda. Prévoyez de réajuster la mise en page.

---

**2. Présentation de comité depuis le suivi Excel**

**Autonomie :** Guided
**Implication :** Augmented

**Pourquoi c'est un bon candidat :**
La présentation est récurrente, avec une structure qui se répète d'un comité à l'autre. Les données sources existent déjà (fichiers de suivi) et la charte est imposée. Ce sont des conditions idéales pour une génération à partir d'un modèle.

**Point de douleur actuel :**
À chaque comité, il faut reprendre les chiffres des fichiers Excel, rédiger les messages clés, appliquer la charte KPMG, refaire une présentation très proche de la précédente, puis intégrer les corrections du manager.

**Comment l'IA aide :**
L'IA lit les fichiers de suivi à jour, calcule les indicateurs (avancement, anomalies ouvertes ou fermées, risques, actions en retard) et rédige pour chaque slide des messages clés qui comparent la situation au comité précédent. Elle produit un brouillon dans le modèle KPMG. Vous affinez les messages et votre manager valide.

**Pour démarrer cette semaine :**
Rédigez une fois le « plan type » de vos comités : liste des slides et données nécessaires à chacune. Avant le prochain comité, donnez ce plan et le fichier Excel à Copilot dans PowerPoint ou à l'outil interne. Demandez les messages clés slide par slide. Gardez les corrections de votre manager : elles affineront vos consignes.

---

**3. Qualification des demandes client**

**Autonomie :** Guided
**Implication :** Augmented

**Pourquoi c'est un bon candidat :**
Les demandes arrivent sous forme de texte libre (e-mail, ticket, remarque en réunion). Le traitement suit toujours le même schéma : reformuler, classer, évaluer l'impact, estimer, enregistrer.

**Point de douleur actuel :**
Chaque demande doit être comprise, reformulée et classée (évolution, anomalie, question). Il faut aussi évaluer son impact sur SAP, estimer une charge et l'inscrire dans le suivi. Les canaux sont dispersés et la qualification varie d'une demande à l'autre.

**Comment l'IA aide :**
À partir du texte de la demande, l'IA produit une fiche standard : reformulation claire, catégorie proposée, modules ou processus SAP probablement concernés, questions à poser au client, premier ordre de grandeur de charge marqué « à valider », et ligne prête pour le fichier de suivi. Vous validez l'analyse d'impact et l'estimation.

**Pour démarrer cette semaine :**
Définissez un modèle de fiche de qualification de 6 à 8 champs. Testez-le avec Copilot sur 3 demandes récentes déjà traitées et comparez avec ce que vous aviez fait vous-même.

---

**4. Compte rendu de réunion structuré**

**Autonomie :** Guided
**Implication :** Augmented

**Pourquoi c'est un bon candidat :**
Le format est stable : contexte, points abordés, décisions, actions avec responsable et échéance. La tâche revient souvent, et Copilot dans Teams est conçu pour ça.

**Point de douleur actuel :**
La rédaction se fait après coup à partir de notes. Le temps passé est répété à chaque réunion, et les actions ne sont pas toujours reportées dans les fichiers de suivi.

**Comment l'IA aide :**
L'IA rédige le compte rendu dans votre modèle à partir de la transcription Teams (si l'enregistrement est autorisé par le client) ou de vos notes. Elle extrait la liste des actions avec responsable et échéance. Cette liste alimente directement l'opportunité n°5.

**Pour démarrer cette semaine :**
Écrivez votre modèle de compte rendu (sections et ton). À la prochaine réunion interne, utilisez Copilot dans Teams, ou collez vos notes dans l'outil interne, avec ce modèle. Mesurez le temps gagné et ce que vous avez dû corriger.

---

## Annexe : définitions des classifications

**Autonomie : quelle part de décision revient à l'IA ?**

- **Deterministic** : l'IA suit des règles fixes, sans jugement. La même entrée donne toujours la même sortie.
- **Guided** : l'IA prend des décisions encadrées. Vous fixez la direction, elle choisit comment y arriver.
- **Autonomous** : l'IA planifie, décide et s'adapte seule, et utilise des outils.

**Implication humaine : y a-t-il quelqu'un dans la boucle pendant l'exécution ?**

- **Augmented** : vous participez pendant le déroulement (relecture, orientation, décisions clés).
- **Automated** : l'IA va de bout en bout seule. Vous ne relisez que le résultat final.

## Synthèse des workflows candidats

### Candidat 1 : Premier jet de BPMN « as-is » à partir des notes d'atelier

| Champ | Valeur |
|---|---|
| **Nom du workflow** | Premier jet de BPMN « as-is » à partir des notes d'atelier |
| **Description** | Transforme les notes d'un atelier client en description structurée du processus existant, liste des points à clarifier et brouillon de diagramme BPMN 2.0 pour Camunda. |
| **Déclencheur** | Manuel : après un atelier client de recueil du processus existant, quand les notes sont disponibles. |
| **Livrable** | Un tableau du processus (couloirs, étapes, passerelles, conditions), une liste de questions ouvertes pour le client et, dans un second temps, un fichier `.bpmn` importable dans Camunda Modeler. |
| **Autonomie** | Guided |
| **Implication** | Augmented |
| **Point de douleur** | Environ une semaine par BPMN, passée surtout à reconstruire l'ordre, les acteurs et les exceptions à partir des notes, à repérer les manques, puis à dessiner. |
| **Opportunité IA** | L'IA structure les notes en processus BPMN (acteurs, étapes, décisions, exceptions), signale les incohérences et les informations manquantes, puis génère le XML BPMN 2.0. La consultante valide le contenu métier et finalise le diagramme dans Camunda. |
| **Fréquence** | Ad-hoc (à chaque atelier de recueil « as-is ») |
| **Priorité** | High |
| **Justification** | Plus fort gain de temps identifié (environ une semaine par livrable). Les données d'entrée sont textuelles, le livrable suit une norme stricte, et les outils autorisés (outil IA interne KPMG, Copilot) suffisent. |
| **Angle** | Individuel |

**Recommandation : par quoi commencer.** C'est votre premier workflow avec la méthode, et le BPMN est votre candidat le plus ambitieux. Construisez d'abord une **version de départ réduite** : notes d'atelier → tableau structuré du processus + liste des questions ouvertes, déclenchée à la main, sans connexion à un outil. La génération du fichier `.bpmn` importable dans Camunda viendra ensuite, comme évolution du même workflow, une fois le tableau fiable.

**Registre :** aucun registre IA dans cet espace. Le candidat est consigné dans ce rapport uniquement. Vous pourrez en créer un avec le skill `scaffolding-registry`.
