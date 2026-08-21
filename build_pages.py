# -*- coding: utf-8 -*-
"""Generate multi-page STM presentation for GitHub Pages."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

NAV = [
    ("index.html", "Старт"),
    ("brand-mika.html", "MIKA"),
    ("brand-torra.html", "TORRA"),
    ("brand-inall.html", "INALL"),
    ("topics.html", "Виды СТМ"),
    ("quiz.html", "Большой тест"),
]


def quiz_html(quiz_id: str, title: str, questions: list[dict]) -> str:
    blocks = []
    for i, q in enumerate(questions, 1):
        opts = []
        for key, text in q["options"].items():
            opts.append(
                f'<label><input type="radio" name="{quiz_id}_q{i}" value="{key}" />'
                f"<span>{text}</span></label>"
            )
        blocks.append(
            f'<div class="q-item" data-answer="{q["answer"]}">'
            f"<h3>{i}. {q['q']}</h3>"
            f'<div class="q-options">{"".join(opts)}</div></div>'
        )
    return f"""
<section class="quiz-block" id="test">
  <h2>Тест для самоконтроля</h2>
  <p class="hint">{title} Отметьте ответы и нажмите «Проверить».</p>
  <form data-mini-quiz>
    {''.join(blocks)}
    <div class="quiz-actions">
      <button class="btn btn-primary" type="submit">Проверить</button>
      <button class="btn btn-ghost" type="button" data-reset>Сбросить</button>
    </div>
    <div class="quiz-result" aria-live="polite"></div>
  </form>
</section>
"""


def page(title: str, body: str, hero: str | None = None) -> str:
    nav = "".join(
        f'<a href="{href}">{label}</a>' for href, label in NAV
    )
    hero_block = hero or ""
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — СТМ презентация</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Unbounded:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="site.css" />
</head>
<body>
  <div class="site">
    <header class="topnav">
      <div class="topnav-inner">
        <a class="brand-lockup" href="index.html">
          <img src="assets/logos/mika.jpg" alt="MIKA" />
          <span>СТМ обучение</span>
        </a>
        <nav class="nav-links">{nav}</nav>
      </div>
    </header>
    <main class="wrap">
      {hero_block}
      {body}
    </main>
    <footer class="foot">По материалам каталога и инструкций СТМ · MIKA / TORRA / INALL</footer>
  </div>
  <script src="site.js"></script>
</body>
</html>
"""


PAGES: dict[str, str] = {}

# ---------- INDEX ----------
PAGES["index.html"] = page(
    "Собственные бренды СТМ",
    """
<section class="section">
  <h2>Три бренда — одна СТМ</h2>
  <p>СТМ (собственная торговая марка) — товары под нашими брендами. Для консультанта важно знать, <strong>какой бренд за что отвечает</strong> и что предложить в конкретной задаче покупателя.</p>
  <div class="logo-row">
    <a class="logo-pill" href="brand-mika.html"><img src="assets/logos/mika.jpg" alt="MIKA" /><span>MIKA</span></a>
    <a class="logo-pill" href="brand-torra.html"><img src="assets/logos/torra.jpg" alt="TORRA" /><span>TORRA</span></a>
    <a class="logo-pill" href="brand-inall.html"><img src="assets/logos/inall.jpg" alt="INALL" /><span>INALL</span></a>
  </div>
</section>

<section class="section">
  <h2>Виды товаров СТМ</h2>
  <p>Ниже — учебные разделы по категориям. В конце каждой страницы — короткий тест.</p>
  <div class="topic-grid">
    <a class="topic-link" href="topic-peny.html"><img src="assets/products/peny_1.jpg" alt="" /><div class="meta"><strong>Пены</strong><span>бытовая, проф, зимняя, огнестойкая, клей-пена</span></div></a>
    <a class="topic-link" href="topic-masla.html"><img src="assets/products/masla_1.jpg" alt="" /><div class="meta"><strong>Масла</strong><span>2T / 4T, ТАД-17, цепь, компрессор</span></div></a>
    <a class="topic-link" href="topic-nasosy.html"><img src="assets/products/nasosy_1.jpg" alt="" /><div class="meta"><strong>Насосы</strong><span>вибрационные, дренаж, скважины, станции</span></div></a>
    <a class="topic-link" href="topic-rastvoriteli.html"><img src="assets/products/rastvoriteli_2.jpg" alt="" /><div class="meta"><strong>Растворители и грунты</strong><span>646, 650, уайт-спирит, огнебио</span></div></a>
    <a class="topic-link" href="topic-stroyka.html"><img src="assets/products/betono_1.jpg" alt="" /><div class="meta"><strong>Стройка</strong><span>тачки, бетоносмесители, мембраны, метизы</span></div></a>
    <a class="topic-link" href="topic-instrument.html"><img src="assets/products/bity_1.jpg" alt="" /><div class="meta"><strong>Инструмент и расходники</strong><span>биты, диски, станки, ножи</span></div></a>
    <a class="topic-link" href="topic-sad.html"><img src="assets/products/masla_3.jpg" alt="" /><div class="meta"><strong>Сад и хозяйство</strong><span>катушки, леска, лопаты, шланги</span></div></a>
    <a class="topic-link" href="topic-avtohimiya.html"><img src="assets/products/myla_1.jpg" alt="" /><div class="meta"><strong>Автохимия и теплоноситель</strong><span>мойка, мыло, антифриз-теплоноситель</span></div></a>
  </div>
</section>

<section class="section split">
  <div class="prose">
    <h2 style="margin-top:0;font-family:var(--display);font-size:1.35rem">Одной фразой</h2>
    <ul>
      <li><strong>MIKA</strong> — основной СТМ почти на всё.</li>
      <li><strong>TORRA</strong> — пена, бетоносмесители, отрезные круги.</li>
      <li><strong>INALL</strong> — аккумуляторный инструмент.</li>
    </ul>
    <div class="chip-row">
      <span class="chip">для продавцов-консультантов</span>
      <span class="chip">по каталогу СТМ</span>
    </div>
  </div>
  <div class="media-frame">
    <img src="assets/products/peny_2.jpg" alt="Ассортимент пен СТМ" />
  </div>
</section>
"""
    + quiz_html(
        "home",
        "Проверьте, что запомнили про бренды.",
        [
            {
                "q": "Какой бренд — основной и самый широкий в СТМ?",
                "options": {"a": "INALL", "b": "MIKA", "c": "AOER", "d": "TORRA"},
                "answer": "b",
            },
            {
                "q": "Аккумуляторный инструмент в нашем СТМ — это бренд:",
                "options": {"a": "MIKA", "b": "TORRA", "c": "INALL", "d": "GARDEN"},
                "answer": "c",
            },
            {
                "q": "TORRA встречается в категориях:",
                "options": {
                    "a": "только масла и насосы",
                    "b": "пена, бетоносмесители, отрезные круги",
                    "c": "только мембраны",
                    "d": "только шуруповёрты",
                },
                "answer": "b",
            },
        ],
    ),
    hero="""
<section class="hero" style="--hero-image:url('assets/products/peny_1.jpg')">
  <p class="eyebrow">Обучение продавцов-консультантов</p>
  <h1>Презентация СТМ</h1>
  <p class="lead">Бренды, виды товаров и шпаргалки для консультации — с тестом на каждой странице.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="topics.html">Смотреть виды СТМ</a>
    <a class="btn btn-ghost" href="quiz.html">Большой тест 30 вопросов</a>
  </div>
</section>
""",
)

# ---------- BRANDS ----------
PAGES["brand-mika.html"] = page(
    "Бренд MIKA",
    """
<header class="page-head">
  <p class="eyebrow">Собственный бренд</p>
  <h1>MIKA</h1>
  <p class="lead">Главное «лицо» СТМ. Если покупатель спрашивает «что у вас своё» — чаще всего речь про MIKA.</p>
</header>
<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/mika.jpg" alt="Логотип MIKA" style="width:180px;background:#fff;padding:0.6rem;border-radius:0.7rem;border:1px solid var(--line)" /></p>
    <h2 style="font-family:var(--display);font-size:1.25rem;margin:1rem 0 0.5rem">Что говорить покупателю</h2>
    <ul>
      <li>Собственная марка — выгодное соотношение цены и качества.</li>
      <li>Широкий ассортимент: от расходников до техники и химии.</li>
      <li>Удобно собирать корзину в одном бренде: пена + пистолет, масло + техника.</li>
    </ul>
    <h2 style="font-family:var(--display);font-size:1.25rem;margin:1rem 0 0.5rem">Где встречается</h2>
    <ul>
      <li>Пены, масла, насосы, растворители, грунтовки, огнебио</li>
      <li>Тачки, метизы, биты, мембраны, станки, рулетки/ножи</li>
      <li>Алмазные диски, теплоноситель, лопаты, электроды, шланги, автохимия</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/masla_1.jpg" alt="" /><figcaption>Масла</figcaption></figure>
    <figure><img src="assets/products/nasosy_1.jpg" alt="" /><figcaption>Насосы</figcaption></figure>
    <figure><img src="assets/products/rastvoriteli_1.jpg" alt="" /><figcaption>Огнебио / химия</figcaption></figure>
  </div>
</section>
<div class="pager">
  <a class="btn btn-ghost" href="index.html" style="color:inherit;border-color:var(--line);background:#fff">← На старт</a>
  <a class="btn btn-ember" href="brand-torra.html">Далее: TORRA →</a>
</div>
"""
    + quiz_html(
        "mika",
        "3 вопроса по бренду MIKA.",
        [
            {
                "q": "MIKA в СТМ — это:",
                "options": {
                    "a": "только аккумуляторный инструмент",
                    "b": "основной и самый широкий бренд",
                    "c": "только отрезные круги",
                    "d": "сторонний бренд-конкурент",
                },
                "answer": "b",
            },
            {
                "q": "К MIKA относится:",
                "options": {
                    "a": "только пена TORRA PRO 65",
                    "b": "масла, насосы, растворители, метизы и др.",
                    "c": "только шуруповёрты INALL",
                    "d": "ничего из каталога",
                },
                "answer": "b",
            },
            {
                "q": "Покупатель: «Что у вас своё подешевле на расходники?» В первую очередь предлагаем:",
                "options": {"a": "INALL", "b": "MIKA", "c": "любой импорт", "d": "только TORRA"},
                "answer": "b",
            },
        ],
    ),
)

PAGES["brand-torra.html"] = page(
    "Бренд TORRA",
    """
<header class="page-head">
  <p class="eyebrow">Собственный бренд</p>
  <h1>TORRA</h1>
  <p class="lead">Дополнительная марка СТМ в ключевых категориях: пена, бетоносмесители, отрезные круги по металлу.</p>
</header>
<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/torra.jpg" alt="Логотип TORRA" style="width:200px;background:#fff;padding:0.6rem;border-radius:0.7rem;border:1px solid var(--line)" /></p>
    <ul>
      <li><strong>Пена</strong> TORRA PRO 65 — проф. всесезонная, рядом с MIKA 65.</li>
      <li><strong>Бетоносмесители</strong> TORRA (в т.ч. серия AOER) — линейка объёмов.</li>
      <li><strong>Отрезные круги</strong> Torra по металлу и нержавейке.</li>
    </ul>
    <p><strong>Важно:</strong> AOER — серия/исполнение внутри TORRA, не отдельный бренд СТМ.</p>
  </div>
  <div class="media-frame"><img src="assets/products/betono_1.jpg" alt="Бетоносмеситель TORRA" /></div>
</section>
<div class="pager">
  <a class="btn btn-ghost" href="brand-mika.html" style="color:inherit;border-color:var(--line);background:#fff">← MIKA</a>
  <a class="btn btn-ember" href="brand-inall.html">Далее: INALL →</a>
</div>
"""
    + quiz_html(
        "torra",
        "Проверьте знания по TORRA.",
        [
            {
                "q": "AOER в названии бетоносмесителя — это:",
                "options": {
                    "a": "отдельный бренд СТМ",
                    "b": "серия/исполнение внутри TORRA",
                    "c": "бренд масел",
                    "d": "название пистолета для пены",
                },
                "answer": "b",
            },
            {
                "q": "Отрезные круги по металлу в СТМ чаще бренда:",
                "options": {"a": "INALL", "b": "TORRA", "c": "только MIKA B1", "d": "GARDEN"},
                "answer": "b",
            },
            {
                "q": "Пена TORRA PRO 65 — это:",
                "options": {
                    "a": "бытовая с трубкой",
                    "b": "профессиональная всесезонная",
                    "c": "клей-пена",
                    "d": "только зимняя",
                },
                "answer": "b",
            },
        ],
    ),
)

PAGES["brand-inall.html"] = page(
    "Бренд INALL",
    """
<header class="page-head">
  <p class="eyebrow">Собственный бренд</p>
  <h1>INALL</h1>
  <p class="lead">Аккумуляторный бесщеточный инструмент СТМ. Не смешивать с расходниками MIKA/TORRA — это отдельная линейка электроинструмента.</p>
</header>
<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/inall.jpg" alt="Логотип INALL" style="width:200px;background:#fff;padding:0.6rem;border-radius:0.7rem;border:1px solid var(--line)" /></p>
    <ul>
      <li>Дрели-шуруповёрты (разный вольтаж и момент)</li>
      <li>УШМ (болгарка) аккумуляторная</li>
      <li>Винтовёрт и гайковёрт ударные</li>
    </ul>
    <p>Уточняйте задачу, Н·м, напряжение и комплектацию (АКБ + ЗУ + кейс). К шуруповёрту апселл — биты MIKA.</p>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/inall_1.jpg" alt="" /><figcaption>INALL</figcaption></figure>
    <figure><img src="assets/products/inall_2.jpg" alt="" /><figcaption>Комплектация</figcaption></figure>
    <figure><img src="assets/products/bity_1.jpg" alt="" /><figcaption>Апселл: биты MIKA</figcaption></figure>
  </div>
</section>
<div class="pager">
  <a class="btn btn-ghost" href="brand-torra.html" style="color:inherit;border-color:var(--line);background:#fff">← TORRA</a>
  <a class="btn btn-ember" href="topics.html">Виды СТМ →</a>
</div>
"""
    + quiz_html(
        "inall",
        "Мини-тест по INALL.",
        [
            {
                "q": "INALL — это:",
                "options": {
                    "a": "бренд монтажных пен",
                    "b": "бренд аккумуляторного инструмента",
                    "c": "серия бетоносмесителей",
                    "d": "теплоноситель",
                },
                "answer": "b",
            },
            {
                "q": "К шуруповёрту INALL логично предложить:",
                "options": {"a": "уайт-спирит", "b": "биты MIKA", "c": "мембрану AM", "d": "ТАД-17"},
                "answer": "b",
            },
            {
                "q": "Что уточнить у покупателя инструмента?",
                "options": {
                    "a": "только цвет кейса",
                    "b": "задачу, момент (Н·м), вольтаж, комплектацию",
                    "c": "только наличие трубки-адаптера",
                    "d": "группу огнезащиты",
                },
                "answer": "b",
            },
        ],
    ),
)

# ---------- TOPICS HUB ----------
PAGES["topics.html"] = page(
    "Виды товаров СТМ",
    """
<header class="page-head">
  <p class="eyebrow">Каталог обучения</p>
  <h1>Виды СТМ</h1>
  <p class="lead">Выберите категорию. На каждой странице — описание, фото и тест самоконтроля.</p>
</header>
<section class="section">
  <div class="topic-grid">
    <a class="topic-link" href="topic-peny.html"><img src="assets/products/peny_1.jpg" alt="" /><div class="meta"><strong>Пены</strong><span>шпаргалка выбора по задаче</span></div></a>
    <a class="topic-link" href="topic-masla.html"><img src="assets/products/masla_2.jpg" alt="" /><div class="meta"><strong>Масла</strong><span>2T, 4T и спецмасла</span></div></a>
    <a class="topic-link" href="topic-nasosy.html"><img src="assets/products/nasosy_2.jpg" alt="" /><div class="meta"><strong>Насосы</strong><span>от колодца до дренажа</span></div></a>
    <a class="topic-link" href="topic-rastvoriteli.html"><img src="assets/products/rastvoriteli_3.jpg" alt="" /><div class="meta"><strong>Растворители</strong><span>химия для ЛКМ и подготовки</span></div></a>
    <a class="topic-link" href="topic-stroyka.html"><img src="assets/products/tachki_1.jpg" alt="" /><div class="meta"><strong>Стройка</strong><span>тачки, миксеры, плёнки</span></div></a>
    <a class="topic-link" href="topic-instrument.html"><img src="assets/products/diski_1.jpg" alt="" /><div class="meta"><strong>Инструмент</strong><span>биты, диски, станки</span></div></a>
    <a class="topic-link" href="topic-sad.html"><img src="assets/products/masla_3.jpg" alt="" /><div class="meta"><strong>Сад</strong><span>леска, катушки, лопаты</span></div></a>
    <a class="topic-link" href="topic-avtohimiya.html"><img src="assets/products/myla_2.jpg" alt="" /><div class="meta"><strong>Автохимия</strong><span>мойка и теплоноситель</span></div></a>
  </div>
</section>
"""
    + quiz_html(
        "topics",
        "Ориентация по разделам.",
        [
            {
                "q": "Шпаргалка «щели → бытовая, двери → проф» относится к разделу:",
                "options": {"a": "Масла", "b": "Пены", "c": "Насосы", "d": "INALL"},
                "answer": "b",
            },
            {
                "q": "Вибрационные ВПН с верхним/нижним забором — это раздел:",
                "options": {"a": "Пены", "b": "Насосы", "c": "Метизы", "d": "Биты"},
                "answer": "b",
            },
            {
                "q": "Бетоносмесители MIKA и TORRA смотрим в разделе:",
                "options": {"a": "Автохимия", "b": "Стройка", "c": "Масла 2T", "d": "Леска"},
                "answer": "b",
            },
        ],
    ),
)

# ---------- TOPIC PAGES ----------
PAGES["topic-peny.html"] = page(
    "Пены СТМ",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA / TORRA</p>
  <h1>Монтажные пены</h1>
  <p class="lead">Подбирайте пену по задаче покупателя — не «какая подешевле», а «для чего».</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>Щели и отверстия</strong> → бытовая MIKA 50 с трубкой.</li>
      <li><strong>Межкомнатные двери / окна / входная дверь</strong> → проф MIKA 65 или TORRA PRO 65.</li>
      <li><strong>Новостройка / усадка</strong> → эластичные: огнестойкая и/или зимняя проф.</li>
      <li><strong>Огнеопасные места</strong> → только огнестойкая MIKA.</li>
      <li><strong>Приклейка материалов</strong> → клей-пена, не обычная монтажная.</li>
    </ul>
    <p>К проф. пене предлагайте пистолет, если его нет у клиента.</p>
  </div>
  <div class="media-frame"><img src="assets/peny-shpargalka.jpg" alt="Шпаргалка выбора пены" style="object-fit:contain;background:#fff;min-height:320px" /></div>
</section>
<section class="section">
  <div class="gallery">
    <figure><img src="assets/products/peny_1.jpg" alt="" /><figcaption>Ассортимент пен</figcaption></figure>
    <figure><img src="assets/products/peny_2.jpg" alt="" /><figcaption>Проф. линейка</figcaption></figure>
    <figure><img src="assets/products/peny_3.jpg" alt="" /><figcaption>Бытовая / спец</figcaption></figure>
  </div>
</section>
"""
    + quiz_html(
        "peny",
        "Шпаргалка по пенам.",
        [
            {
                "q": "Для щелей и отверстий без пистолета лучше:",
                "options": {
                    "a": "клей-пена",
                    "b": "бытовая MIKA 50 с трубкой",
                    "c": "только огнестойкая",
                    "d": "теплоноситель",
                },
                "answer": "b",
            },
            {
                "q": "Для окон и входной двери рекомендуем:",
                "options": {
                    "a": "бытовую с трубкой",
                    "b": "проф. всесезонную MIKA 65 / TORRA PRO 65",
                    "c": "только минеральное масло 2T",
                    "d": "любую пену без пистолета",
                },
                "answer": "b",
            },
            {
                "q": "Огнеопасные места — какую пену?",
                "options": {
                    "a": "любую всесезонную",
                    "b": "только огнестойкую",
                    "c": "клей-пену",
                    "d": "бытовую MIKA 50",
                },
                "answer": "b",
            },
            {
                "q": "Для приклейки блоков/материалов нужна:",
                "options": {"a": "обычная монтажная", "b": "клей-пена", "c": "уайт-спирит", "d": "леска 2.4"},
                "answer": "b",
            },
        ],
    ),
)

PAGES["topic-masla.html"] = page(
    "Масла MIKA",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA</p>
  <h1>Масла</h1>
  <p class="lead">Не путайте 2T и 4T: в двухтактных масло обычно в смесь с бензином, в четырёхтактных — в картер.</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>2T минералка / полусинтетика</strong> — фасовки 1 л, 100 мл, GARDEN, с дозатором.</li>
      <li><strong>4T</strong> — минеральное и полусинтетическое.</li>
      <li><strong>ТАД-17</strong> — трансмиссия, не моторное.</li>
      <li><strong>Для цепей и шин</strong> — не моторное масло.</li>
      <li><strong>Компрессорное</strong> — специальное для поршневых компрессоров.</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/masla_1.jpg" alt="" /><figcaption>2T / 4T</figcaption></figure>
    <figure><img src="assets/products/masla_2.jpg" alt="" /><figcaption>Линейка MIKA</figcaption></figure>
    <figure><img src="assets/products/masla_3.jpg" alt="" /><figcaption>Сад / техника</figcaption></figure>
  </div>
</section>
"""
    + quiz_html(
        "masla",
        "Масла для техники.",
        [
            {
                "q": "Масло для цепей бензопилы — это:",
                "options": {
                    "a": "то же, что 2T моторное",
                    "b": "отдельное масло для смазки цепи и шины",
                    "c": "ТАД-17",
                    "d": "уайт-спирит",
                },
                "answer": "b",
            },
            {
                "q": "2T и 4T взаимозаменяемы?",
                "options": {"a": "да", "b": "нет", "c": "только зимой", "d": "только в компрессоре"},
                "answer": "b",
            },
            {
                "q": "100 мл и 1 л по 2T полусинтетике — это:",
                "options": {
                    "a": "разные типы масел",
                    "b": "разные фасовки одной линейки",
                    "c": "только для автомобилей",
                    "d": "бренд TORRA",
                },
                "answer": "b",
            },
        ],
    ),
)

PAGES["topic-nasosy.html"] = page(
    "Насосы MIKA",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA</p>
  <h1>Насосы</h1>
  <p class="lead">Сначала задача и вода (чистая/грязная), потом тип насоса.</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>Вибрационные ВПН</strong> — колодец/ёмкость; забор В (верхний) или Н (нижний).</li>
      <li><strong>Дренажные</strong> — грязная вода, подтопления.</li>
      <li><strong>Скважинные</strong> винтовые / центробежные — диаметр скважины, напор, песок.</li>
      <li><strong>Поверхностные</strong> — не опускают в воду.</li>
      <li><strong>Насосные станции</strong> — водоснабжение дома с гидробаком.</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/nasosy_1.jpg" alt="" /><figcaption>Погружные</figcaption></figure>
    <figure><img src="assets/products/nasosy_2.jpg" alt="" /><figcaption>Скважинные</figcaption></figure>
    <figure><img src="assets/products/nasosy_3.jpg" alt="" /><figcaption>Станции / дренаж</figcaption></figure>
  </div>
</section>
"""
    + quiz_html(
        "nasosy",
        "Подбор насоса.",
        [
            {
                "q": "Верхний забор (В) у вибрационного насоса лучше, когда:",
                "options": {
                    "a": "нужно выкачать до дна с илом",
                    "b": "важно меньше забирать грязь со дна",
                    "c": "нужна только резка металла",
                    "d": "это клей-пена",
                },
                "answer": "b",
            },
            {
                "q": "Поверхностный насос:",
                "options": {
                    "a": "опускают на дно скважины",
                    "b": "ставят вне воды",
                    "c": "это всегда дренажный",
                    "d": "только для пены",
                },
                "answer": "b",
            },
            {
                "q": "Для грязной воды / луж чаще нужен:",
                "options": {"a": "вибрационный чистой воды", "b": "дренажный", "c": "ТАД-17", "d": "диск турбо"},
                "answer": "b",
            },
        ],
    ),
)

PAGES["topic-rastvoriteli.html"] = page(
    "Растворители, огнебио, грунтовки",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA</p>
  <h1>Растворители и подготовка</h1>
  <p class="lead">Путаница 646 / 650 / уайт-спирит — частая ошибка. Уточняйте тип ЛКМ.</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>Уайт-спирит</strong> — масляные/алкидные; нельзя в водные краски.</li>
      <li><strong>646</strong> — нитроэмали/нитролаки, агрессивнее.</li>
      <li><strong>650</strong> — автоэмали, между 646 и уайт-спиритом.</li>
      <li><strong>Обезжириватель</strong> — пластик/подготовка, не для разбавления масляных.</li>
      <li><strong>Огнебио PROF</strong> — 2-я группа, дерево.</li>
      <li><strong>Грунтовка глубокого проникновения</strong> — пыль, впитываемость, адгезия.</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/rastvoriteli_2.jpg" alt="" /><figcaption>Уайт-спирит</figcaption></figure>
    <figure><img src="assets/products/rastvoriteli_3.jpg" alt="" /><figcaption>Растворители</figcaption></figure>
    <figure><img src="assets/products/rastvoriteli_1.jpg" alt="" /><figcaption>Огнебио / грунт</figcaption></figure>
  </div>
</section>
"""
    + quiz_html(
        "rast",
        "Химия для консультанта.",
        [
            {
                "q": "Уайт-спирит в водоэмульсионку:",
                "options": {"a": "можно", "b": "нельзя — расслоится", "c": "только с 646", "d": "обязательно"},
                "answer": "b",
            },
            {
                "q": "646 в первую очередь для:",
                "options": {"a": "водных красок", "b": "нитроэмалей и нитролаков", "c": "только бетона", "d": "цепей пилы"},
                "answer": "b",
            },
            {
                "q": "Огнебио MIKA ОГНЕБИО PROF — группа:",
                "options": {"a": "1-я", "b": "2-я", "c": "нет группы", "d": "только для металла"},
                "answer": "b",
            },
        ],
    ),
)

PAGES["topic-stroyka.html"] = page(
    "Стройка СТМ",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA / TORRA</p>
  <h1>Стройка</h1>
  <p class="lead">Тачки, бетоносмесители, мембраны/плёнки, метизы — под задачу объекта.</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>Тачки</strong> — садовая легче; строительная усиленная для бетона/щебня; 1 или 2 колеса.</li>
      <li><strong>Бетоносмесители</strong> — MIKA и TORRA, подбирайте по объёму барабана.</li>
      <li><strong>Мембраны</strong> — AM гидро-ветро; A / B / C / D — разные задачи паро/гидроизоляции.</li>
      <li><strong>Метизы</strong> — саморезы, кровельные, крепёж DIN; смотрите фасовку.</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/tachki_1.jpg" alt="" /><figcaption>Тачки</figcaption></figure>
    <figure><img src="assets/products/betono_2.jpg" alt="" /><figcaption>Бетоносмесители</figcaption></figure>
    <figure><img src="assets/products/membrany_1.jpg" alt="" /><figcaption>Мембраны</figcaption></figure>
  </div>
</section>
"""
    + quiz_html(
        "stroy",
        "Строительный ассортимент.",
        [
            {
                "q": "Садовую тачку постоянно под бетон:",
                "options": {
                    "a": "идеально",
                    "b": "нежелательно — корыто сомнётся быстрее",
                    "c": "только зимой",
                    "d": "вместо бетоносмесителя",
                },
                "answer": "b",
            },
            {
                "q": "Мембрана AM — это в первую очередь:",
                "options": {
                    "a": "клей-пена",
                    "b": "гидро-ветрозащита с высокой паропроницаемостью",
                    "c": "масло 4T",
                    "d": "круг по металлу",
                },
                "answer": "b",
            },
            {
                "q": "Бетоносмесители в СТМ бывают брендов:",
                "options": {"a": "только INALL", "b": "MIKA и TORRA", "c": "только GARDEN", "d": "нет таких"},
                "answer": "b",
            },
        ],
    ),
)

PAGES["topic-instrument.html"] = page(
    "Инструмент и оснастка",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA / TORRA</p>
  <h1>Инструмент и расходники</h1>
  <p class="lead">Биты, диски, круги, станки, ножи и рулетки — уточняйте профиль, диаметр и материал.</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>Биты</strong> — торсионные для удара; PH2 самый ходовой; PZ — мебель.</li>
      <li><strong>Алмазные диски MIKA</strong> — бетон/плитка/универсал (сегмент, сплошной, турбо).</li>
      <li><strong>Круги Torra</strong> — металл и нержавейка.</li>
      <li><strong>Станки точильные MIKA</strong> — гараж/мастерская.</li>
      <li><strong>Ножи / лезвия / рулетки</strong> — расходники на каждый день.</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/bity_2.jpg" alt="" /><figcaption>Биты</figcaption></figure>
    <figure><img src="assets/products/diski_1.jpg" alt="" /><figcaption>Диски</figcaption></figure>
    <figure><img src="assets/products/stanki_1.jpg" alt="" /><figcaption>Станки</figcaption></figure>
  </div>
</section>
"""
    + quiz_html(
        "instr",
        "Оснастка.",
        [
            {
                "q": "Для ударного режима шуруповёрта лучше биты:",
                "options": {"a": "самые дешёвые обычные", "b": "торсионные", "c": "только магнитные головки 17", "d": "лезвия 18 мм"},
                "answer": "b",
            },
            {
                "q": "Круги по металлу/нержавейке в СТМ — бренд:",
                "options": {"a": "INALL", "b": "TORRA", "c": "только AM", "d": "EFFECT"},
                "answer": "b",
            },
            {
                "q": "PH2 чаще всего нужен для:",
                "options": {"a": "плитки", "b": "саморезов по дереву/ГКЛ", "c": "сварки", "d": "гидроизоляции"},
                "answer": "b",
            },
        ],
    ),
)

PAGES["topic-sad.html"] = page(
    "Сад и хозяйство",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA</p>
  <h1>Сад и хозяйство</h1>
  <p class="lead">Катушки и леска для триммера, лопаты, шланги, электроды — спрашивайте совместимость.</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>Катушки</strong> — резьба (часто М10×1.25), левая/правая, модель триммера.</li>
      <li><strong>Леска</strong> — диаметр главный; сечение круг/звезда/квадрат.</li>
      <li><strong>Лопата снеговая</strong> — морозоустойчивый полипропилен.</li>
      <li><strong>Шланг</strong> — армированный, морозостойкий.</li>
      <li><strong>Электроды MK-46</strong> — ручная дуговая сварка.</li>
    </ul>
  </div>
  <div class="media-frame"><img src="assets/products/masla_3.jpg" alt="Садовая линейка" /></div>
</section>
"""
    + quiz_html(
        "sad",
        "Сад / расходники.",
        [
            {
                "q": "Главный критерий выбора лески:",
                "options": {"a": "цвет упаковки", "b": "диаметр", "c": "только бренд TORRA", "d": "наличие 646"},
                "answer": "b",
            },
            {
                "q": "Без старой катушки у клиента спросите:",
                "options": {
                    "a": "только цену",
                    "b": "резьбу, сторону накрутки и модель триммера",
                    "c": "группу огнезащиты",
                    "d": "вольтаж INALL",
                },
                "answer": "b",
            },
            {
                "q": "Электроды Mika MK-46 нужны для:",
                "options": {"a": "покраски", "b": "ручной дуговой сварки", "c": "полива", "d": "наклейки обоев"},
                "answer": "b",
            },
        ],
    ),
)

PAGES["topic-avtohimiya.html"] = page(
    "Автохимия и теплоноситель",
    """
<header class="page-head">
  <p class="eyebrow">Вид СТМ · MIKA</p>
  <h1>Автохимия и теплоноситель</h1>
  <p class="lead">Линейки мойки EFFECT / Prof / STANDART и теплоносители на этилен- / пропиленгликоле.</p>
</header>
<section class="section split">
  <div class="prose">
    <ul>
      <li><strong>Бесконтактная мойка</strong> — концентрации 1 кг и 5 кг; сравнивайте задачу и «силу» линейки.</li>
      <li><strong>Мыло жидкое</strong> — есть строительное (добавка) и бытовое перламутровое — не путать.</li>
      <li><strong>Теплоноситель −65 этиленгликоль</strong> — системы отопления; токсичнее.</li>
      <li><strong>ЭКО −30 пропиленгликоль</strong> — более «экологичный» вариант.</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><img src="assets/products/myla_1.jpg" alt="" /><figcaption>Мойка</figcaption></figure>
    <figure><img src="assets/products/myla_2.jpg" alt="" /><figcaption>Линейки</figcaption></figure>
    <figure><img src="assets/products/myla_3.jpg" alt="" /><figcaption>Фасовки</figcaption></figure>
  </div>
</section>
"""
    + quiz_html(
        "auto",
        "Автохимия.",
        [
            {
                "q": "Теплоноситель ЭКО на пропиленгликоле в каталоге — ориентир по морозу:",
                "options": {"a": "−65", "b": "−30", "c": "+35", "d": "нет данных"},
                "answer": "b",
            },
            {
                "q": "EFFECT / Prof / STANDART — это:",
                "options": {
                    "a": "серии бетоносмесителей",
                    "b": "линейки средств бесконтактной мойки",
                    "c": "типы лески",
                    "d": "бренды вместо MIKA",
                },
                "answer": "b",
            },
            {
                "q": "Этиленгликолевый теплоноситель относительно пропиленгликолевого:",
                "options": {
                    "a": "обычно токсичнее, осторожнее в быту",
                    "b": "это то же самое",
                    "c": "только для пены",
                    "d": "только для 2T",
                },
                "answer": "a",
            },
        ],
    ),
)


def write_quiz_page():
    """Keep full quiz as separate page using existing assets."""
    html = """<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Большой тест СТМ — 30 вопросов</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Unbounded:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="stylesheet" href="site.css" />
</head>
<body>
  <div class="bg-grid" aria-hidden="true"></div>
  <header class="topnav">
    <div class="topnav-inner">
      <a class="brand-lockup" href="index.html">
        <img src="assets/logos/mika.jpg" alt="MIKA" />
        <span>СТМ обучение</span>
      </a>
      <nav class="nav-links">
        <a href="index.html">Презентация</a>
        <a href="topics.html">Виды СТМ</a>
        <a class="active" href="quiz.html">Большой тест</a>
      </nav>
    </div>
  </header>

  <main class="shell">
    <section id="screen-start" class="panel">
      <p class="eyebrow">Итоговая проверка</p>
      <h1>СТМ <span>тест</span></h1>
      <p class="lead">30 вопросов по каталогу: растворители, пены, масла, насосы и бренды.</p>
      <ul class="meta">
        <li>Один правильный ответ</li>
        <li>~25–35 минут</li>
        <li>Результат сразу после прохождения</li>
      </ul>
      <label class="name-field">
        <span>Ваше имя (необязательно)</span>
        <input id="user-name" type="text" maxlength="60" placeholder="Например, Анна" autocomplete="name" />
      </label>
      <button type="button" class="btn primary" id="btn-start">Начать тест</button>
    </section>

    <section id="screen-quiz" class="panel hidden" aria-live="polite">
      <div class="topbar">
        <div class="progress-wrap">
          <div class="progress-bar" id="progress-bar"></div>
        </div>
        <div class="topmeta">
          <span id="q-counter">1 / 30</span>
          <span id="q-topic" class="topic"></span>
        </div>
      </div>
      <h2 id="q-text"></h2>
      <div id="options" class="options" role="radiogroup"></div>
      <div class="nav">
        <button type="button" class="btn ghost" id="btn-prev" disabled>Назад</button>
        <button type="button" class="btn primary" id="btn-next" disabled>Далее</button>
      </div>
    </section>

    <section id="screen-result" class="panel hidden">
      <p class="eyebrow">Результат</p>
      <h1 id="score-title">Готово</h1>
      <p class="scoreline"><span id="score-num">0</span><span class="slash">/</span>30</p>
      <p id="score-verdict" class="lead"></p>
      <div id="topic-stats" class="topic-stats"></div>
      <div id="review" class="review"></div>
      <button type="button" class="btn primary" id="btn-restart">Пройти ещё раз</button>
      <p style="margin-top:1rem"><a href="index.html" style="color:var(--brand)">← Вернуться к презентации</a></p>
    </section>
  </main>

  <footer class="foot">По материалам каталога СТМ MIKA / TORRA / INALL</footer>
  <script src="app.js"></script>
</body>
</html>
"""
    (ROOT / "quiz.html").write_text(html, encoding="utf-8")


def main():
    for name, html in PAGES.items():
        (ROOT / name).write_text(html, encoding="utf-8")
        print("wrote", name)
    write_quiz_page()
    print("wrote quiz.html")

    # Redirect old root quiz UX: index is now presentation; keep note in README later
    print("done", len(PAGES) + 1, "pages")


if __name__ == "__main__":
    main()
