#!/usr/bin/env python3
"""Generate docs/index.md from data/ving.yaml"""

import yaml
from pathlib import Path


def main():
    data_file = Path('data/ving.yaml')
    docs_file = Path('docs/index.md')
    data = yaml.safe_load(data_file.read_text(encoding='utf-8'))
    entries = data.get('entries', [])

    header = [
        '# Ving Rhames Sunglasses',
        '',
    ]

    lines = []
    lines.extend(header)

    for entry in entries:
        title = entry.get('title', 'Untitled')
        image = entry.get('image', '')
        make_model = entry.get('make_model', '')
        purchase = entry.get('purchase_link', '')
        notes = entry.get('notes', '')

        lines.append(f'## {title}')
        lines.append('')

        if image:
            # standardize image display size for readability
            lines.append(f'<img src="{image}" alt="{title}" style="max-width:300px; height:auto;"/>')
            lines.append('')

        if make_model:
            lines.append(f'- **Make & Model:** {make_model}')

        if purchase:
            lines.append(f'- **Purchase Link:** [{purchase}]({purchase})')

        if notes:
            lines.append(f'- **Notes:** {notes}')

        lines.append('')

    docs_file.write_text('\n'.join(lines), encoding='utf-8')
    print('docs/index.md generated from data/ving.yaml')


if __name__ == '__main__':
    main()