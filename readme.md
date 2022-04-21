# Test technique Data Engineering
Ce test permet d'évaluer votre niveau de connaissance en base et traitement de données ainsi de développement.

## Prérequis
- Connaissance en base de données relationnelles (création, insertion et requête).
- Connaissance d'un langage de programmation afin lire des fichiers, traiter des données et accéder à un base de données.
- Connaissance de Git.

 ## Contenu
Le répertoire `data` contient 2 fichiers utilisés pour ce test:
- `lieux.csv`: où chaque ligne contient une commune, son département et sa région.
- `personnes.csv`: où chaque ligne contient un nom, un prénom, une date et une commune de naissance.
- `exemple_resultat.json`: exemple de fichier de sortie.

## Instructions
Voici les différentes étapes à accomplir durant ce test:
1. Définir un schéma de base correspondants aux fichiers fournis.
2. Créer un processus d'ingestion de données pour insérer les données fournies dans la base qui vient d'être créée. Le language de votre choix peut-être utilisé.
3. Créer 2 fichiers de résultats (similaire à `exemple_resultat.json`) listant le nombre de personnes nées:
    - par département
    - par région

## Attendus
Le test doit être hébergé sur un dépôt Git de votre choix.

3 types de rendus sont attendus:
- Le script de création du schéma de base de données
- Le code du processus d'ingestion de données
- Le code de génération des résultats

# Notes
- Il n'y a pas de bonne façon de faire ce test du moment que vos choix sont justifiés.
- La qualité du code est importante.
