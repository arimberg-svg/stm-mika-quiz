# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

themes = {
    "index.html": "home",
    "brand-mika.html": "mika",
    "brand-torra.html": "torra",
    "brand-inall.html": "inall",
    "brand-stm.html": "stm",
    "analogs.html": "analogs",
    "test.html": "test",
}

NEW_HERO = """
<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">Для продавцов розницы</p>
    <h1>Собственные бренды СТМ</h1>
    <p class="lead">Короткие и понятные карточки: что продаём под своими марками, чем отличаются и что сказать покупателю.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="brand-mika.html">Начать с MIKA</a>
      <a class="btn btn-ghost" href="test.html">Пройти тест</a>
    </div>
  </div>
  <div class="hero-visual">
    <img src="assets/products/peny_1.jpg" alt="Ассортимент СТМ — монтажные пены MIKA" />
  </div>
</section>
""".strip()

for name, theme in themes.items():
    p = ROOT / name
    if not p.exists():
        print("missing", name)
        continue
    html = p.read_text(encoding="utf-8")
    html = re.sub(r"<body[^>]*>", f'<body class="theme-{theme}">', html, count=1)

    if name == "index.html":
        html2, n = re.subn(
            r'<section class="hero"[\s\S]*?</section>',
            NEW_HERO,
            html,
            count=1,
        )
        html = html2
        print("hero replacements", n)
        html = re.sub(
            r'(<a class="topic-link"[^>]*>)<img src="([^"]+)" alt=""\s*/?>',
            r'\1<div class="img-box"><img src="\2" alt="" /></div>',
            html,
        )
        html = html.replace(
            ' style="object-fit:contain;background:#fff"',
            "",
        )

    # wrap gallery images once
    html = re.sub(
        r"<figure>\s*<img src=\"([^\"]+)\" alt=\"([^\"]*)\"[^>]*>\s*<figcaption>",
        r'<figure><div class="img-box"><img src="\1" alt="\2" loading="lazy" /></div><figcaption>',
        html,
    )
    # avoid double wrap
    html = html.replace(
        '<div class="img-box"><div class="img-box">',
        '<div class="img-box">',
    ).replace("</div></div><figcaption>", "</div><figcaption>")

    p.write_text(html, encoding="utf-8")
    print("updated", name, theme)

print("done")
