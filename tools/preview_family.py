#!/usr/bin/env python3
"""Build a portable, offline comparison of the RivetFox marketplace artwork."""

import argparse
import ast
import base64
from html import escape
from pathlib import Path
from shutil import copyfile


def data_url(path):
    mime = {".png": "image/png", ".gif": "image/gif", ".svg": "image/svg+xml", ".woff2": "font/woff2"}[path.suffix]
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def card(checkout, module, title, output):
    manifest = ast.literal_eval((checkout / module / "__manifest__.py").read_text())
    assets = checkout / module / "static/description"
    poster = data_url(assets / "theme-preview.png")
    animation = data_url(assets / "theme_screenshot.gif")
    version = escape(manifest["version"])
    package = checkout / "dist" / f'{module}-{manifest["version"]}.zip'
    download = ""
    if package.is_file():
        for file in [package, package.with_suffix(".zip.sha256")]:
            copyfile(file, output / file.name)
        download = f'<a href="{escape(package.name)}" download>Download release ZIP</a>'
    return f'''<article>
<img class="artwork" src="{animation}" data-animation="{animation}" data-poster="{poster}"
  width="1000" height="1210" alt="{escape(title)} marketplace thumbnail for Odoo {version.split('.')[0]}">
<div class="caption"><strong>{escape(title)}</strong><span>Odoo {version.split('.')[0]} Community · {version}</span>{download}</div>
</article>'''


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--neo-theme", type=Path, action="append", help="Neo Brutal checkout; repeat for version branches")
    parser.add_argument("--output", type=Path, default=root / "dist/brand-preview/index.html")
    args = parser.parse_args()
    neo = args.neo_theme or [root.parent / "odoo-neobrutalism-theme"]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cards = [card(root, "minimalism_theme", "Minimalism", args.output.parent)]
    cards += [card(checkout, "neobrutalism_theme", "Neo Brutal", args.output.parent) for checkout in neo]
    brand = data_url(root / "tools/branding/rivetfox-mark.svg")
    font = data_url(root / "tools/branding/space-grotesk-latin.woff2")
    html = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>RivetFox · Theme artwork</title><style>
@font-face{font-family:RivetFox;src:url(FONT) format("woff2");font-weight:300 700}*{box-sizing:border-box}body{margin:0;background:#f2f1ed;color:#252520;font:15px/1.5 system-ui,sans-serif}
main{max-width:1020px;margin:auto;padding:40px 28px 56px}.brand{font-family:RivetFox,system-ui,sans-serif;display:flex;align-items:center;gap:10px;font-size:25px;font-weight:750;letter-spacing:-1px}
.brand img{width:38px;height:38px}.brand b{color:#da542a}h1{font-size:38px;letter-spacing:-1.5px;line-height:1.15;margin:24px 0 12px}
.intro{color:#62625d;max-width:620px;margin:0 0 22px}button{border:1px solid #cfcfc7;background:#fffaf3;border-radius:8px;padding:10px 14px;font:inherit;cursor:pointer}
.cards{display:flex;justify-content:center;flex-wrap:wrap;gap:26px;margin-top:30px}.cards article{width:298px;max-width:100%;background:white;border:1px solid #ddddd6;border-radius:10px;overflow:hidden;box-shadow:0 8px 28px #25252008}
.artwork{display:block;width:100%;height:auto}.caption{padding:14px 16px;border-top:1px solid #e8e8e1}.caption strong,.caption span{display:block}.caption span{font-size:12px;color:#686861;margin-top:4px}.caption a{display:inline-block;font-size:12px;margin-top:10px;color:#a33c1a;text-underline-offset:3px}
h2{font-size:20px;letter-spacing:-.4px;margin-top:36px}footer{font-size:12px;color:#73736b;margin-top:32px;text-align:center}
@media(max-width:600px){main{padding:24px 16px}h1{font-size:30px}.cards{gap:20px}}
</style><main><div class="brand"><img src="BRAND" alt="RivetFox fox"><span>rivetfox<b>.</b></span></div>
<h1>Two themes. One maker.</h1><p class="intro">A shared RivetFox signature. Two distinct Odoo workspaces. Preview the actual animated marketplace assets at catalog-card size.</p>
<button id="motion" aria-pressed="false">Pause animations</button><div class="cards" id="current">CURRENT</div>
LEGACY
<footer>Local artwork preview · Real version-specific Odoo captures · Not a live Odoo Apps listing</footer></main>
<script>
const button=document.getElementById('motion');
function setPaused(paused){document.querySelectorAll('.artwork').forEach(img=>img.src=paused?img.dataset.poster:img.dataset.animation);button.setAttribute('aria-pressed',String(paused));button.textContent=paused?'Play animations':'Pause animations'}
button.addEventListener('click',()=>setPaused(button.getAttribute('aria-pressed')!=='true'));
if(matchMedia('(prefers-reduced-motion: reduce)').matches)setPaused(true);
</script></html>'''
    legacy = '<h2>Neo Brutal · Odoo 16–18</h2><div class="cards">' + "".join(cards[2:]) + "</div>" if len(cards) > 2 else ""
    html = html.replace("FONT", font).replace("BRAND", brand).replace("CURRENT", "".join(cards[:2])).replace("LEGACY", legacy)
    license_text = escape((root / "tools/branding/OFL-Space-Grotesk.txt").read_text())
    html = html.replace("</html>", f'<template id="font-license">{license_text}</template></html>')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(html)
    print(args.output)


if __name__ == "__main__":
    main()
