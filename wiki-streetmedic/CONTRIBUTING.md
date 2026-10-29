# Guide du contributeur
## 1. Ce dont vous avez besoin
Un compte GitHub (un pseudonyme suffit). Dans les paramètres du compte, ne pas rendre l'adresse e-mail publique.

## 2. Corriger une page
1. Ouvrir la page sur le site.
2. Cliquer sur "Modifier cette page" en bas.
3. Modifier le texte avec l'icône crayon.
4. Cliquer sur "Commit changes", puis "Propose changes".
5. Attendre la relecture. Rien n'est publié avant validation.

## 3. Proposer une nouvelle page
Deux possibilités:
- Remplir le formulaire "Proposer un nouvel article" (onglet Issues).
- Ou créer le fichier vous-même: copier un modèle de `outils/modeles/`, puis "Add file", "Create new file", dans `contenu/<section>/<categorie>/<nom>/<nom>.md`.

## 4. Règles
- Dossier et fichier portent le même nom: minuscules, chiffres, tirets, sans accent ni espace (`genl/genl.md`).
- Ne pas répéter le titre de la page en début de texte: il est affiché automatiquement. Le texte commence par `# En bref`.
- Les sections sont en `#`, les sous-sections en `##`, sans sauter de niveau.
- Liens vers une autre page: `[[nom-du-dossier]]`.
- Images: dans le dossier `media/` de la page, nommées `objet-description-01.webp`, sans métadonnées EXIF. Chaque image a une description, une source et une licence (ligne en italique juste dessous).
- Toute information est sourcée. Pour le médical: référentiel officiel de premiers secours.
- Aucune donnée personnelle.
- Valeurs de `type`, `status` et `tags`: celles de `outils/listes-autorisees.yml`.

## 5. Contrôle automatique
Chaque proposition est vérifiée (noms, frontmatter, liens, images). Le message d'erreur indique le fichier et le problème.

## 6. Relecture
Les pages des sections Soigner, Se protéger et Reconnaître sont relues par les personnes désignées dans `.github/CODEOWNERS`.
