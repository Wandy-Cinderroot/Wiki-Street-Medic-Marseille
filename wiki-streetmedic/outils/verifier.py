#!/usr/bin/env python3
"""Contrôles avant publication: noms, frontmatter, liens, images.
Usage: python outils/verifier.py   (code de sortie 1 si une erreur)"""
import re, sys, pathlib
import yaml
from PIL import Image

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import preparer as P

NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
OK_FILES = {"index.md", "README.md", ".nav.yml", ".meta.yml"}
ALLOWED = yaml.safe_load((P.ROOT / "outils" / "listes-autorisees.yml").read_text(encoding="utf-8"))


def main():
    errors, warnings = [], []
    pages, slugs, dup = P.collect()
    errors += dup

    for f in sorted(P.SRC.rglob("*")):
        rel = f.relative_to(P.SRC)
        if any(part in P.SKIP_DIRS for part in rel.parts):
            continue
        if f.is_dir():
            if not NAME.match(f.name):
                errors.append(f"{rel}: nom de dossier invalide (minuscules, chiffres, tirets)")
            continue
        if f.name in OK_FILES:
            continue
        if not NAME.match(f.stem):
            errors.append(f"{rel}: nom de fichier invalide (minuscules, chiffres, tirets, sans accent ni espace)")
        if f.suffix.lower() in IMG_EXT:
            try:
                with Image.open(f) as im:
                    if len(im.getexif()) > 0 or "exif" in im.info:
                        errors.append(f"{rel}: métadonnées EXIF présentes, à supprimer")
            except Exception as e:  # image illisible
                errors.append(f"{rel}: image illisible ({e})")
            if f.stat().st_size > 500_000:
                warnings.append(f"{rel}: image de plus de 500 Ko")

    for pg in pages:
        where = pg.rel
        if pg.path.stem not in ("index",) and pg.path.parent != P.SRC and not pg.is_folder_page:
            if pg.meta.get("type") not in ("page", "hub"):
                errors.append(f"{where}: une fiche doit être dans un dossier du même nom (ex. genl/genl.md)")
        m = pg.meta
        if not m:
            errors.append(f"{where}: frontmatter absent")
            continue
        for key in ("title", "type", "status"):
            if not m.get(key):
                errors.append(f"{where}: clé obligatoire vide ou absente: {key}")
        for key in ("type", "status", "body_area"):
            if m.get(key) and m[key] not in ALLOWED[key]:
                errors.append(f"{where}: valeur non autorisée pour {key}: {m[key]}")
        for tag in m.get("tags") or []:
            if tag not in ALLOWED["tags"]:
                errors.append(f"{where}: étiquette non autorisée: {tag}")
        for key in ("injuries", "ppe", "launchers", "equipment", "protects_against", "sources"):
            for slug in m.get(key) or []:
                if slug not in slugs:
                    errors.append(f"{where}: {key} renvoie vers une page inexistante: {slug}")
        body = pg.body
        if re.search(r"^# ", body, re.M) is None and m.get("type") != "page":
            warnings.append(f"{where}: aucune section de niveau 1")
        if re.match(r"\s*# " + re.escape(str(m.get("title", ""))) + r"\s*$", body.splitlines()[0] if body.splitlines() else ""):
            errors.append(f"{where}: ne pas répéter le titre en H1 dans le corps")
        if m.get("type") in ("weapon-contact", "munition", "launcher", "tactical", "vehicle", "unit", "ppe"):
            first = next((l for l in body.splitlines() if l.startswith("# ")), "")
            if first.strip().lower() != "# en bref":
                errors.append(f"{where}: la première section doit s'appeler 'En bref'")
            if not re.search(r"^# Sources\s*$", body, re.M):
                errors.append(f"{where}: section 'Sources' absente")
        for n, line in enumerate(body.splitlines(), 1):
            for mm in P.WIKILINK.finditer(line):
                if mm.group(1).strip() not in slugs:
                    errors.append(f"{where}:{n}: lien introuvable [[{mm.group(1).strip()}]]")
        if m.get("type") in ("situation", "care") and m.get("status") == "validated":
            warnings.append(f"{where}: page médicale validée, vérifier la relecture")

    for w in warnings:
        print("AVERTISSEMENT:", w)
    for e in errors:
        print("ERREUR:", e)
    print(f"{len(pages)} pages contrôlées: {len(errors)} erreur(s), {len(warnings)} avertissement(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
