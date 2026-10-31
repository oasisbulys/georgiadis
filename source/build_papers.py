"""Rebuild all eight PDFs with Tectonic; the website itself needs no build."""
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
compiler = shutil.which('tectonic')
if not compiler:
    raise SystemExit('Install Tectonic before rebuilding the manuscript PDFs.')
for source in sorted((root/'source/papers').rglob('*.tex')):
    subprocess.run([compiler, '-X', 'compile', str(source), '--outdir', str(root/'papers')], cwd=source.parent, check=True)
