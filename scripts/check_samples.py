#!/usr/bin/env python3
"""Read-only sample manifest validation; never generates images."""
from pathlib import Path
import hashlib, json

def check(root):
    manifest = json.loads((root/'references/samples.json').read_text())
    assert manifest['panel'] == root.name, 'Wrong panel'
    digest = hashlib.sha256((root/'references/original-prompt/zh-CN.md').read_bytes()).hexdigest()
    assert manifest['source_sha256'] == digest, 'Canonical source changed'
    entries = manifest['samples']
    assert manifest['status'] in ('not-generated', 'ready'), 'Invalid status'
    assert bool(entries) == (manifest['status'] == 'ready'), 'Status/count mismatch'
    seen = set()
    for item in entries:
        rel = Path(item['file'])
        assert not rel.is_absolute() and '..' not in rel.parts, 'Unsafe path'
        assert rel.parts[:2] == ('assets', 'examples'), 'Wrong sample directory'
        path = (root/rel).resolve()
        assert path.is_relative_to(root.resolve()) and path.is_file(), 'Missing or escaped sample'
        assert str(rel) not in seen, 'Duplicate sample'
        seen.add(str(rel))
        assert item['source_sha256'] == digest, 'Wrong sample source brief'
        assert item['visual_review'] == 'passed', 'Visual acceptance missing'
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], 'Sample changed'
        assert item['mode'] in ('top-bottom','left-right','design-only','wallpaper-pack'), 'Wrong mode'
        from PIL import Image
        with Image.open(path) as image:
            image.load()
            assert image.format == 'PNG', 'Final sample must be PNG'
            assert list(image.size) == [item['width'],item['height']], 'Wrong size'
            if item['mode'] == 'top-bottom': assert image.height % 2 == 0, 'Unequal halves'
            if item['mode'] == 'left-right': assert image.width % 2 == 0, 'Unequal halves'
    folder = root/'assets/examples'
    actual = {str(p.relative_to(root)) for p in folder.rglob('*') if p.is_file() and not p.name.startswith('.')} if folder.exists() else set()
    assert actual == seen, 'Unregistered or missing sample files'
    return len(entries)

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    try:
        count = check(root)
    except (AssertionError, KeyError, ValueError, OSError) as exc:
        raise SystemExit(f'Sample check FAILED: {exc}')
    print(f'{root.name}: sample manifest OK ({count} generated samples); visual quality requires human review')
