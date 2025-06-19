# Specifications for Ving Rhames Sunglasses

## Project Title
Ving

## Purpose & Vision

I want to make a dead simple html website, called "ving", using github pages. The website is a single-page, Web 1.0-style microsite that catalogues the sunglasses worn by actor Ving Rhames in various films, including a picture, then the make and model of the glasses, and perhaps some links to buy them on ebay, or elsewhere. 

The site should evoke the late-1990s “view-source” aesthetic—fast, lightweight, and free of modern bloat.

## Tools

Codex will write ALL the code for the project, according to my specifications. Coxed will always ask for clarification from me, when needed. 

Use mkdocs

Use github pages and its built in workflow. 

create a workflow similar to this at ving/.github/workflows/

```
name: mkdocs build and deployment
permissions:
  contents: write

on:
  pull_request:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: mkdocs build --strict          # fails fast on broken links etc.

  deploy:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: mkdocs gh-deploy --force --clean --verbose
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

all my code pushes to main branch. 

Keep it simple. 