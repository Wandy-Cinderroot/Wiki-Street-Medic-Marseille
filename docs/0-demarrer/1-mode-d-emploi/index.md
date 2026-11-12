---
title: Mode d'emploi
description:
not_in_nav: "true"
---
Lire les pages  
Imprimer les fiches résumés et les afficher chez soi  
Chercher des éléments quand vous avez des doutes 
```
Get-ChildItem -Path . -Filter "0-index.md" -Recurse -File |
    Rename-Item -NewName "index.md"
```

This renames every `index.md` to `0-index.md` in all subdirectories.

Note: Check that no directory already contains a `0-index.md` file, to avoid naming conflicts.