# Ving

Ving is a simple MkDocs-based website that catalogs the sunglasses worn by Ving Rhames in various films. It aims for a minimalist, late-1990s “view-source” aesthetic.

## Getting Started

Install dependencies:

```bash
pip install -r requirements.txt
```

Preview the site locally:

```bash
mkdocs serve
```

## Content Structure

- Instead of editing Markdown directly, edit `data/ving.yaml` to add or update your entries.
- Place your images in `docs/images/` (relative to the root).

After editing `data/ving.yaml`, regenerate the index:

```bash
python scripts/generate_index.py
```


## Deployment

This project uses GitHub Actions to build and deploy to GitHub Pages automatically on each push to `main`. See `.github/workflows/mkdocs.yml` for details.

_Note: CI will auto-generate `docs/index.md` from `data/ving.yaml` on each build/deploy._
