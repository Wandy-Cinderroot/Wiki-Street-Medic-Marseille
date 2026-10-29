# Wiki Street Medic Marseille
Savoirs de terrain: reconnaître, se protéger, soigner, s'organiser.
Site: https://ORGA.github.io/wiki-streetmedic/ (à adapter)

Ce wiki complète une formation. Il ne remplace ni des soins professionnels ni les secours.
En cas d'urgence vitale: 15 (SAMU), 18 (pompiers), 112.

## Contribuer
- Corriger une page: bouton "Modifier cette page" en bas de la page du site.
- Proposer ou signaler: onglet Issues, formulaires "Proposer un nouvel article" et "Corriger ou compléter un article".
- Guide complet: [CONTRIBUTING.md](CONTRIBUTING.md).

## Organisation du dépôt
- `contenu/`: tout ce qui s'écrit (pages et images). Ouvrir ce dossier comme coffre Obsidian.
- `outils/`: scripts de contrôle et de préparation, modèles de pages, listes autorisées.
- `theme/`: styles du site.
- `.github/`: formulaires, relecture obligatoire, publication automatique.
- `zensical.toml`: configuration du site.

## Tester en local
```
pip install -r requirements.txt
python outils/verifier.py
python outils/preparer.py
zensical serve
```
Puis ouvrir http://localhost:8000. Relancer `python outils/preparer.py` après chaque modification de contenu.

## Ce qui n'a pas sa place ici
Noms, visages reconnaissables, lieux sensibles, contacts, procédures internes. Ces éléments restent dans un espace privé.
