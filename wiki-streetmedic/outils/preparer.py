#!/usr/bin/env python3
"""Prépare contenu/ pour Zensical.
- aplatit les dossiers-pages (x/x.md -> x.md, x/media/ -> x/media/)
- convertit les [[liens]] en liens Markdown
- ajoute le titre, décale les niveaux de titre, replie les sections après "En bref"
- ajoute le lien "Modifier cette page"
Usage: python outils/preparer.py [--strict]
"""
import os, re, shutil, sys, pathlib
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "contenu"
OUT = ROOT / "_genere" / "docs"
THEME = ROOT / "theme"
REPO = os.environ.get("WIKI_REPO_URL", "https://github.com/ORGA/wiki-streetmedic").rstrip("/")
BRANCH = os.environ.get("WIKI_BRANCH", "main")
OPEN_SECTIONS = {"en bref", "sources"}
NO_COLLAPSE_TYPES = {"hub", "page"}
SKIP_DIRS = {".obsidian", ".git", ".trash"}
KEEP_DOTFILES = {".nav.yml", ".meta.yml"}
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,5})\s+(.*)$")
WIKILINK = re.compile(r"\[\[([^\]|#\\]+)(#[^\]|\\]+)?(?:\\?\|([^\]]+))?\]\]")


PAGES = []


class Page:
    def __init__(self, path):
        self.path = path
        self.rel = path.relative_to(SRC)
        self.is_folder_page = path.parent != SRC and path.parent.name == path.stem
        self.out_rel = (
            self.rel.parent.parent / (path.stem + ".md") if self.is_folder_page else self.rel
        )
        text = path.read_text(encoding="utf-8")
        self.front_raw, self.body, self.meta = split_front(text)
        self.slug = None if path.stem in ("index", "README") else path.stem
        self.title = str(self.meta.get("title") or path.stem.replace("-", " ").capitalize())


def split_front(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            raw = text[: end + 4]
            body = text[end + 4 :].lstrip("\n")
            try:
                meta = yaml.safe_load(text[4:end]) or {}
            except yaml.YAMLError:
                meta = {}
            return raw, body, meta if isinstance(meta, dict) else {}
    return "", text, {}


def collect():
    pages, errors = [], []
    for p in sorted(SRC.rglob("*.md")):
        if any(part in SKIP_DIRS for part in p.relative_to(SRC).parts) or p.name == "README.md":
            continue
        pages.append(Page(p))
    slugs = {}
    for pg in pages:
        if pg.slug:
            if pg.slug in slugs:
                errors.append(f"Nom de page en double: {pg.slug} ({slugs[pg.slug].rel} et {pg.rel})")
            slugs[pg.slug] = pg
    return pages, slugs, errors


def transform(page, slugs, warnings):
    lines, in_fence, out = page.body.splitlines(), False, []
    stem = page.path.stem
    for line in lines:
        if FENCE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        if page.is_folder_page:
            line = line.replace("](media/", f"]({stem}/media/").replace('src="media/', f'src="{stem}/media/')
        m = HEADING.match(line)
        if m:
            line = "#" + line
        if line.strip() == "<!-- liste-pages -->":
            out.extend(page_list(page))
            continue
        line = rebuild(line, page, slugs, warnings)
        out.append(line)
    body = ["# " + page.title] + out
    collapse = page.meta.get("collapse", page.meta.get("type") not in NO_COLLAPSE_TYPES)
    if collapse:
        body = collapse_sections(body)
    src_rel = (SRC.relative_to(ROOT) / page.rel).as_posix()
    body.append("")
    body.append(f"[Modifier cette page]({REPO}/edit/{BRANCH}/{src_rel}){{ .edit-link }}")
    return "\n".join(body).rstrip() + "\n"


def page_list(hub):
    """Tableau des pages situées dans le même dossier que la page d'accueil de section."""
    rows = [
        pg for pg in PAGES
        if pg.out_rel.parent == hub.out_rel.parent and pg.path.stem != "index"
    ]
    if not rows:
        return ["Aucune page pour le moment."]
    lines = ["| Page | Type | Statut |", "|---|---|---|"]
    for pg in sorted(rows, key=lambda x: x.title.lower()):
        link = os.path.relpath(pg.out_rel, hub.out_rel.parent).replace(os.sep, "/")
        lines.append(f"| [{pg.title}]({link}) | {pg.meta.get('type', '')} | {pg.meta.get('status', '')} |")
    return lines


def rebuild(line, page, slugs, warnings):
    if "[[" not in line:
        return line
    pieces = line.split("`")
    for i in range(0, len(pieces), 2):
        pieces[i] = convert_links_plain(pieces[i], page, slugs, warnings)
    return "`".join(pieces)


def convert_links_plain(text, page, slugs, warnings):
    def repl(m):
        slug = m.group(1).strip()
        anchor = (m.group(2) or "").strip()
        label = (m.group(3) or "").strip()
        target = slugs.get(slug)
        if not target:
            warnings.append(f"{page.rel}: lien introuvable [[{slug}]]")
            return label or slug
        rel = os.path.relpath(target.out_rel, page.out_rel.parent).replace(os.sep, "/")
        return f"[{label or target.title}]({rel}{anchor})"

    return WIKILINK.sub(repl, text)


def collapse_sections(lines):
    first_h2 = next((l for l in lines if l.startswith("## ")), None)
    if not first_h2 or first_h2[3:].strip().lower() != "en bref":
        return lines
    out, i, in_fence = [], 0, False
    sections = []  # (heading, content_lines) ; heading None = préambule
    current = (None, [])
    for l in lines:
        if FENCE.match(l):
            in_fence = not in_fence
        if not in_fence and l.startswith("## "):
            sections.append(current)
            current = (l[3:].strip(), [])
        else:
            current[1].append(l)
    sections.append(current)
    for heading, content in sections:
        if heading is None:
            out.extend(content)
        elif heading.lower() in OPEN_SECTIONS:
            out.append(f"## {heading}")
            out.extend(content)
        else:
            title = heading.replace('"', "'")
            while content and not content[-1].strip():
                content.pop()
            out.append("")
            out.append(f'??? note "{title}"')
            out.append("")
            out.extend(("    " + c) if c.strip() else "" for c in content)
            out.append("")
    return out


def owner_dir(path, folder_pages):
    for parent in path.parents:
        if parent in folder_pages:
            return parent
    return None


def main():
    strict = "--strict" in sys.argv
    pages, slugs, errors = collect()
    PAGES.extend(pages)
    warnings = []
    if OUT.parent.exists():
        shutil.rmtree(OUT.parent)
    OUT.mkdir(parents=True)
    folder_pages = {p.path.parent for p in pages if p.is_folder_page}
    seen_out = {}
    for pg in pages:
        if pg.out_rel in seen_out:
            errors.append(f"Collision de sortie: {pg.out_rel}")
        seen_out[pg.out_rel] = pg
        dest = OUT / pg.out_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        front = pg.front_raw + "\n\n" if pg.front_raw else ""
        dest.write_text(front + transform(pg, slugs, warnings), encoding="utf-8")
    for f in SRC.rglob("*"):
        rel = f.relative_to(SRC)
        if f.is_dir() or f.suffix == ".md" or any(p in SKIP_DIRS for p in rel.parts):
            continue
        if f.name.startswith(".") and f.name not in KEEP_DOTFILES:
            continue
        od = owner_dir(f, folder_pages)
        if od:
            inside = f.relative_to(od)
            dest = OUT / od.relative_to(SRC).parent / od.name / inside
        else:
            dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)
    css = THEME / "extra.css"
    if css.exists():
        (OUT / "stylesheets").mkdir(exist_ok=True)
        shutil.copy2(css, OUT / "stylesheets" / "extra.css")
    for msg in errors:
        print("ERREUR:", msg)
    for msg in warnings:
        print("AVERTISSEMENT:", msg)
    print(f"{len(pages)} pages préparées dans {OUT.relative_to(ROOT)}")
    if errors or (strict and warnings):
        sys.exit(1)


if __name__ == "__main__":
    main()
