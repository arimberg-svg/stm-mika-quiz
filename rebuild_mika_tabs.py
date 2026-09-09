# -*- coding: utf-8 -*-
"""Rebuild brand-mika.html as tabbed product catalog."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSORT = json.loads((ROOT / "assets/_assortment.json").read_text(encoding="utf-8"))

NAV = (
    '<a href="index.html">Главная</a>'
    '<a href="brand-mika.html">MIKA</a>'
    '<a href="brand-torra.html">TORRA</a>'
    '<a href="brand-inall.html">INALL</a>'
    '<a href="analogs.html">Аналоги</a>'
    '<a href="test.html">Тест</a>'
)
FAV = """  <link rel="icon" href="assets/favicon.png" type="image/png" />
  <link rel="shortcut icon" href="favicon.ico" />"""
FOOT = """    <footer class="foot">
      Материалы для продавцов розницы сети «У Михалыча» · собственные бренды MIKA / TORRA / INALL
      <a href="https://gvozditut.ru/brands/mika/" target="_blank" rel="noopener">gvozditut.ru</a>
    </footer>"""


def items(key: str):
    return [
        x
        for x in ASSORT.get(key, [])
        if "TORRA" not in x["name"].upper() or "MIKA" in x["name"].upper()
    ]


def cards(rows, show_art=True):
    parts = ['<div class="prod-grid">']
    for it in rows:
        art = (it.get("art") or "").strip()
        name = it["name"]
        # skip bad art like руб/кг
        if art.lower().startswith("руб") or art == "None":
            art = ""
        art_html = f'<span class="art">{art}</span>' if show_art and art else ""
        parts.append(
            f'<article class="prod-card"><strong>{name}</strong>{art_html}</article>'
        )
    parts.append("</div>")
    return "\n".join(parts)


def metizy_mika():
    rows = []
    for it in ASSORT.get("МЕТИЗЫ", []):
        if "MIKA" not in it["name"].upper():
            continue
        name = it["name"]
        art = it.get("art") or ""
        if art.lower().startswith("руб"):
            art = ""
        rows.append({"art": art, "name": name})
    return rows


def solvent_groups():
    rows = items("РАСТВОРИТЕЛИ, огнебио, грунтовк")
    groups = {
        "Растворители": [],
        "Обезжириватель": [],
        "Огнебиозащита": [],
        "Грунтовка": [],
    }
    for it in rows:
        n = it["name"].lower()
        if "огнебио" in n:
            groups["Огнебиозащита"].append(it)
        elif "грунтов" in n:
            groups["Грунтовка"].append(it)
        elif "обезжир" in n:
            groups["Обезжириватель"].append(it)
        else:
            groups["Растворители"].append(it)
    return groups


PUMPS_HTML = """
<div class="prod-grid">
<article class="prod-card"><strong>Вибрационный ВПН-10В (верхний забор)</strong><span class="art">335110В</span><span class="hint">280 Вт · 18 л/мин · кабель 10 м</span></article>
<article class="prod-card"><strong>Вибрационный ВПН-10Н (нижний забор)</strong><span class="art">335110Н</span><span class="hint">280 Вт · 18 л/мин · кабель 10 м</span></article>
<article class="prod-card"><strong>Вибрационный ВПН-15В (верхний забор)</strong><span class="art">335115В</span><span class="hint">кабель 15 м</span></article>
<article class="prod-card"><strong>Вибрационный ВПН-15Н (нижний забор)</strong><span class="art">335115Н</span><span class="hint">кабель 15 м</span></article>
<article class="prod-card"><strong>Вибрационный ВПН-25В (верхний забор)</strong><span class="art">335125В</span><span class="hint">кабель 25 м</span></article>
<article class="prod-card"><strong>Вибрационный ВПН-25Н (нижний забор)</strong><span class="art">335125Н</span><span class="hint">кабель 25 м</span></article>
<article class="prod-card"><strong>Вибрационный ВПН-40В (верхний забор)</strong><span class="art">335140В</span><span class="hint">кабель 40 м · выход ¾″</span></article>
<article class="prod-card"><strong>Дренажный ДН-750 (грязная вода)</strong><span class="art">33528D</span><span class="hint">750 Вт · 10 м³/ч</span></article>
<article class="prod-card"><strong>Дренажный НД-750</strong><span class="art">335275D</span><span class="hint">13 000 л/ч · частицы до 30 мм</span></article>
<article class="prod-card"><strong>Насосная станция НС-750 · 24 л</strong><span class="art">335324L</span><span class="hint">напор 50 м · 3600 л/ч</span></article>
<article class="prod-card"><strong>Скважинный винтовой СН-В 370 Вт</strong><span class="art">3354370В</span><span class="hint">25 л/мин · напор 45 м</span></article>
<article class="prod-card"><strong>Скважинный винтовой СН-В 550 Вт</strong><span class="art">3354550В</span><span class="hint">30 л/мин · напор 90 м</span></article>
<article class="prod-card"><strong>Скважинный центробежный СН-Ц 370 Вт</strong><span class="art">335430Ц</span><span class="hint">47 л/мин · напор 50 м</span></article>
<article class="prod-card"><strong>Скважинный центробежный СН-Ц 550 Вт</strong><span class="art">335450Ц</span><span class="hint">47 л/мин · напор 70 м</span></article>
<article class="prod-card"><strong>Поверхностный ПН-800</strong><span class="art">335543П</span><span class="hint">800 Вт · 5000 л/ч</span></article>
</div>
"""

solv = solvent_groups()
solv_html = []
for title, rows in solv.items():
    if not rows:
        continue
    tip = {
        "Растворители": "Под задачу ЛКМ / очистки: уайт-спирит, 646, 650, ацетон, сольвент, керосин. Сверьте фасовку.",
        "Обезжириватель": "Перед покраской / склейкой металла и пластика.",
        "Огнебиозащита": "Для древесины: защита от огня и биопоражения. Напомните про группу защиты и расход.",
        "Грунтовка": "Глубокого проникновения — перед финишной отделкой. Сверьте объём 5 / 10 л.",
    }.get(title, "")
    solv_html.append(
        f'<h3 class="subhead">{title}</h3><p class="sell">{tip}</p>{cards(rows)}'
    )

bits_guide = """
<div class="prose bits-guide">
  <h3 style="margin-top:0;font-family:var(--display);font-size:1.05rem">Как подбирать биты MIKA</h3>
  <ol>
    <li><strong>Шлиц</strong> — PH (крестовой Philips), PZ (Pozidriv). PH2 / PZ2 — самые ходовые для саморезов.</li>
    <li><strong>Длина</strong> — 50 мм для обычной работы; 70–90 мм, если нужен вылет или работа в углублении.</li>
    <li><strong>Одна сторона или две</strong> — двухсторонние удобны «в кармане»; односторонние — в держатель/набор.</li>
    <li><strong>Под инструмент</strong> — к шуруповёрту / INALL; для ударного режима лучше торсионные.</li>
  </ol>
  <h3 style="font-family:var(--display);font-size:1.05rem">Цвет / покрытие — для чего</h3>
  <ul>
    <li><strong>Красные торсионные</strong> — усиленные, пружинят при ударе/перекосе. Для ударных шуруповёртов и плотных саморезов (каркас, металл к дереву).</li>
    <li><strong>Коричневые двухсторонние</strong> — повседневная работа, два рабочих конца PH2/PH2. Для мебели, гипсокартона, общего монтажа без сильного удара.</li>
    <li><strong>Чёрные двухсторонние торсионные</strong> — та же двухсторонность + торсион. Когда нужен запас прочности, но удобство «перевернул — работаешь».</li>
    <li><strong>С магнитным ограничителем</strong> — фиксирует глубину усадки самореза (гипсокартон, чистовая отделка), меньше срыва шлица и «утопления» шляпки.</li>
    <li><strong>Обычные PH / PZ</strong> — базовый расходник под частую замену; берите по шлицу и длине.</li>
    <li><strong>Магнитные головки 8 / 10 / 13 / 17</strong> — под болты/гайки и саморезы с шестигранной головкой; магнит держит метиз.</li>
    <li><strong>Наборы 41 / 49 предметов</strong> — если покупатель собирает первый комплект «под дом/бригаду».</li>
  </ul>
  <p><strong>В зале:</strong> спросите шлиц на саморезе (PH или PZ), есть ли ударный режим, нужна ли длинная бита. Не путайте PH и PZ — от этого срывает шлицы.</p>
</div>
"""

tabs = [
    (
        "about",
        "О бренде",
        f"""
<div class="split">
  <div class="prose">
    <p><img src="assets/logos/mika.jpg" alt="Логотип MIKA" style="width:170px;background:#fff;padding:.55rem;border:1px solid var(--line);border-radius:.7rem" /></p>
    <p>Главный собственный бренд сети. Баланс <strong>качество + цена + широкий ассортимент</strong>.</p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что сказать покупателю</h3>
    <ul>
      <li>«Это наша собственная марка — без переплаты за громкое имя».</li>
      <li>«Можно собрать всё нужное в одной линейке».</li>
      <li>«Подходит и для дома/дачи, и для рабочих задач».</li>
    </ul>
  </div>
  <div class="gallery gallery-2">
    <figure><div class="img-box"><img src="assets/web/mika/foam_mika65.jpg" alt="MIKA PRO 65" loading="lazy" /></div><figcaption>Пена MIKA PRO 65</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/nasosy_1.jpg" alt="Насосы" loading="lazy" /></div><figcaption>Насосы MIKA</figcaption></figure>
  </div>
</div>
""",
    ),
    (
        "foams",
        "Пены",
        f"""
<p class="sell">Щели → бытовая; двери/окна → проф под пистолет; мороз → зимняя; огонь → B1; плиты/блоки → клей-пена. Шпаргалка — на <a href="index.html">главной</a>.</p>
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/foam_mika65.jpg" alt="MIKA PRO 65" loading="lazy" /></div><figcaption>Проф. MIKA PRO 65</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_site_glue.jpg" alt="Клей-пена" loading="lazy" /></div><figcaption>Клей-пена</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_winter.jpg" alt="Зимняя" loading="lazy" /></div><figcaption>Зимняя</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_fire.jpg" alt="Огнестойкая" loading="lazy" /></div><figcaption>Огнестойкая B1</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_50.jpg" alt="MIKA 50" loading="lazy" /></div><figcaption>Бытовая MIKA 50</figcaption></figure>
  <figure><div class="img-box"><img src="assets/products/peny_2.jpg" alt="Выход пены" loading="lazy" /></div><figcaption>Выход пены PRO 65</figcaption></figure>
</div>
{cards([x for x in items('Пены') if 'TORRA' not in x['name'].upper()])}
""",
    ),
    (
        "pumps",
        "Насосы",
        f"""
<p class="sell">Верхний забор — чище вода сверху; нижний — почти до дна. Скважина: винтовой терпит примеси, центробежный — больше л/мин на чистой воде.</p>
<div class="gallery">
  <figure><div class="img-box"><img src="assets/products/nasosy_1.jpg" alt="" loading="lazy" /></div><figcaption>Вибрационные</figcaption></figure>
  <figure><div class="img-box"><img src="assets/products/nasosy_2.jpg" alt="" loading="lazy" /></div><figcaption>Скважинные / станции</figcaption></figure>
  <figure><div class="img-box"><img src="assets/products/nasosy_3.jpg" alt="" loading="lazy" /></div><figcaption>Поверхностные / дренаж</figcaption></figure>
</div>
{PUMPS_HTML}
""",
    ),
    (
        "briq",
        "Брикеты",
        """
<p class="sell">Арт. 331113. Плотные брикеты — не торопить разжиг 15–20 минут, не лить жидкость и не раздувать сразу.</p>
<div class="gallery gallery-1">
  <figure><div class="img-box"><img src="assets/web/mika/briquettes.jpg" alt="Брикеты" loading="lazy" /></div><figcaption>Угольные брикеты MIKA, 3 кг</figcaption></figure>
</div>
<div class="prose">
  <h3 style="margin-top:0;font-family:var(--display);font-size:1.05rem">Стартером (быстро)</h3>
  <p>Засыпаете брикеты сверху, снизу один-два спиртовых тюбика. Поджигаете. За счёт тяги в цилиндре схватываются равномерно за 15–20 минут.</p>
  <h3 style="font-family:var(--display);font-size:1.05rem">«Домиком» без стартера</h3>
  <p>Колодец/шалашик из брикетов, внутрь — щепа или лучина. Или спиртовые тюбики на дно мангала и домик над ними. Главное — воздух снизу и 15–20 минут без спешки.</p>
</div>
""",
    ),
    (
        "mixers",
        "Бетоносмесители",
        f"""
<p class="sell">Спросите объём работ → подберите объём барабана. Рядом можно показать TORRA как альтернативу по цене/наличию.</p>
<div class="media-frame"><img src="assets/web/mika/mixer.jpg" alt="Бетоносмеситель MIKA" loading="lazy" /></div>
{cards(items('БЕТОНОСМЕСИТЕЛИ'))}
""",
    ),
    (
        "oils",
        "Масла",
        f"""
<p class="sell">2T и 4T не взаимозаменяемы. Цепь / компрессор / ТАД-17 — только по назначению. Сверьте фасовку.</p>
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/oil_1.jpg" alt="Масло MIKA" loading="lazy" /></div><figcaption>Масла MIKA</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/oil_2.jpg" alt="Масло MIKA" loading="lazy" /></div><figcaption>2T / 4T</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/oil_3.jpg" alt="Масло MIKA" loading="lazy" /></div><figcaption>Цепь / спецмасла</figcaption></figure>
</div>
{cards(items('МАСЛА'))}
""",
    ),
    (
        "solvents",
        "Растворители и подготовка",
        f"""
<p class="sell">Сначала задача: разбавить / обезжирить / защитить дерево / загрунтовать. Напомните про вентиляцию и перчатки.</p>
<div class="media-frame"><img src="assets/web/mika/solvents.jpg" alt="Растворители MIKA" loading="lazy" /></div>
{''.join(solv_html)}
""",
    ),
    (
        "wheel",
        "Тачки",
        f"""
<p class="sell">Объём кузова, тип колеса, сад или стройка.</p>
<div class="media-frame"><img src="assets/web/mika/wheelbarrow.jpg" alt="Тачка MIKA" loading="lazy" /></div>
{cards(items('ТАЧКИ'))}
""",
    ),
    (
        "reels",
        "Катушки",
        f"""
<p class="sell">Под триммер: резьба/посадка и тип головки. Сразу предложите леску нужного диаметра.</p>
<div class="media-frame"><img src="assets/web/mika/reels.jpg" alt="Катушка MIKA" loading="lazy" /></div>
{cards(items('КАТУШКИ'))}
""",
    ),
    (
        "line",
        "Леска",
        f"""
<p class="sell">Диаметр и профиль (круг / квадрат / звезда / семиугольник). Сверьте с катушкой и мощностью триммера.</p>
<div class="media-frame"><img src="assets/web/mika/line.jpg" alt="Леска MIKA" loading="lazy" /></div>
{cards(items('ЛЕСКА'))}
""",
    ),
    (
        "metizy",
        "Метизы MIKA",
        f"""
<p class="sell">Только маркировка MIKA. Сверьте тип, диаметр, длину и фасовку (кг / уп.).</p>
{cards(metizy_mika())}
""",
    ),
    (
        "bits",
        "Биты",
        f"""
{bits_guide}
<div class="media-frame"><img src="assets/web/mika/bits.jpg" alt="Биты MIKA" loading="lazy" /></div>
{cards(items('БИТЫ'))}
""",
    ),
    (
        "membrane",
        "Мембраны и плёнки",
        f"""
<p class="sell">Паро/гидро/ветрозащита — по узлу. Не путайте стороны укладки.</p>
<div class="media-frame"><img src="assets/web/mika/membrane.jpg" alt="Мембрана MIKA" loading="lazy" /></div>
{cards(items('МЕМБРАНЫ И ПЛЕНКИ'))}
""",
    ),
    (
        "discs",
        "Алмазные диски",
        f"""
<p class="sell">Материал решает тип: сегмент — бетон/кирпич; сплошной/турбо — плитка/керамогранит; Alligator/Grizzly — армированный бетон/гранит. Металл — круги TORRA.</p>
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/disc_diamond.jpg" alt="Диск MIKA" loading="lazy" /></div><figcaption>Алмазные диски MIKA</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/disc_mika_0.jpg" alt="Segment" loading="lazy" /></div><figcaption>Segment / бетон</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/disc_mika_2.jpg" alt="Turbo" loading="lazy" /></div><figcaption>Turbo / универсальный</figcaption></figure>
</div>
{cards(items('ДИСКИ АЛМАЗНЫЕ И КРУГИ ОТРЕЗНЫЕ'))}
""",
    ),
    (
        "bench",
        "Станки",
        f"""
<p class="sell">Точильные: диаметр круга и нужна ли лампа. Дисково-ленточный — если и круг, и лента.</p>
<div class="media-frame"><img src="assets/web/mika/bench.jpg" alt="Станок MIKA" loading="lazy" /></div>
{cards(items('СТАНКИ'))}
""",
    ),
    (
        "tape",
        "Рулетки и ножи",
        f"""
<p class="sell">Длина рулетки; к ножу — запасные лезвия того же размера (18 / 25 мм).</p>
<div class="media-frame"><img src="assets/web/mika/tape_knife.jpg" alt="Рулетка MIKA" loading="lazy" /></div>
{cards(items('РУЛЕТКИ НОЖИ ЛЕЗВИЯ'))}
""",
    ),
    (
        "auto",
        "Автохимия",
        f"""
<p class="sell">EFFECT / Prof / STANDART — под интенсивность мойки. Сверьте объём 1 / 5 кг.</p>
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/auto_1.jpg" alt="Автошампунь" loading="lazy" /></div><figcaption>Автошампунь MIKA</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/auto_2.jpg" alt="Автохимия" loading="lazy" /></div><figcaption>Линейки мойки</figcaption></figure>
</div>
{cards(items('МЫЛО И АВТОШАМПУНИ'))}
""",
    ),
    (
        "shovel",
        "Лопаты",
        f"""
<p class="sell">Снеговая морозоустойчивая — для зимы; уточните наличие черенка/рукояти в комплекте.</p>
<div class="media-frame"><img src="assets/web/mika/shovel.jpg" alt="Лопата MIKA" loading="lazy" /></div>
{cards(items('ЛОПАТЫ'))}
""",
    ),
    (
        "electrodes",
        "Электроды",
        f"""
<p class="sell">MIKA-46 для ручной дуговой сварки. Сверьте диаметр и фасовку 1 / 5,5 кг под аппарат.</p>
<div class="media-frame"><img src="assets/web/mika/electrodes.jpg" alt="Электроды MIKA" loading="lazy" /></div>
{cards(items('ЭЛЕКТРОДЫ'))}
""",
    ),
    (
        "hose",
        "Шланги",
        f"""
<p class="sell">Поливочный армированный 3/4″×25 м, 5 слоёв, морозостойкий. Сверьте фитинги/пистолет полива.</p>
<div class="media-frame"><img src="assets/web/mika/hose.jpg" alt="Шланг MIKA" loading="lazy" /></div>
{cards(items('ШЛАНГИ'))}
""",
    ),
]

tab_btns = []
tab_panels = []
for i, (tid, label, body) in enumerate(tabs):
    active = " is-active" if i == 0 else ""
    hidden = "" if i == 0 else " hidden"
    tab_btns.append(
        f'<button type="button" class="tab-btn{active}" role="tab" aria-selected="{"true" if i==0 else "false"}" data-tab="{tid}">{label}</button>'
    )
    tab_panels.append(
        f'<section class="tab-panel{active}" id="tab-{tid}" role="tabpanel"{hidden}>\n{body}\n</section>'
    )

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Бренд MIKA — Обучение «У Михалыча»</title>
{FAV}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Unbounded:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="site.css" />
</head>
<body class="theme-mika">
  <div class="site">
    <header class="topnav">
      <div class="topnav-inner">
        <a class="brand-lockup" href="index.html">
          <img src="assets/logos/mika.jpg" alt="MIKA" />
          <span>Обучение · свои марки</span>
        </a>
        <nav class="nav-links">{NAV}</nav>
      </div>
    </header>
    <main class="wrap">

<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>MIKA</h1>
  <p class="lead">Ассортимент по вкладкам: откройте нужный тип товара — фото, состав линейки и как предлагать в зале.</p>
</header>

<div class="tabs" data-tabs>
  <div class="tab-list" role="tablist" aria-label="Типы товаров MIKA">
    {''.join(tab_btns)}
  </div>
  <div class="tab-panels">
    {''.join(tab_panels)}
  </div>
</div>

<div class="pager">
  <a class="btn btn-ghost" href="index.html" style="color:inherit;border-color:var(--line);background:#fff">← Главная</a>
  <a class="btn btn-ember" href="brand-torra.html">Далее: TORRA →</a>
</div>

    </main>
{FOOT}
  </div>
  <script src="site.js"></script>
</body>
</html>
"""

(ROOT / "brand-mika.html").write_text(html, encoding="utf-8")
print("brand-mika.html", len(html), "tabs", len(tabs), "metizy", len(metizy_mika()))
