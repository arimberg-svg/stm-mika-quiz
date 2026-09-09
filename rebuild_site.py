# -*- coding: utf-8 -*-
"""Rebuild STM training site for retail sellers: brands, analogs, self-test."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

NAV = [
    ("index.html", "Главная"),
    ("brand-mika.html", "MIKA"),
    ("brand-torra.html", "TORRA"),
    ("brand-inall.html", "INALL"),
    ("brand-stm.html", "СТМ сантехника"),
    ("analogs.html", "Аналоги"),
    ("test.html", "Тест"),
]


def page(title: str, body: str, extra_js: str = "") -> str:
    nav = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Обучение СТМ «У Михалыча»</title>
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
          <span>СТМ · обучение</span>
        </a>
        <nav class="nav-links">{nav}</nav>
      </div>
    </header>
    <main class="wrap">
{body}
    </main>
    <footer class="foot">
      Материалы для продавцов розницы сети «У Михалыча» · по каталогу СТМ и сайту
      <a href="https://gvozditut.ru/brands/mika/" target="_blank" rel="noopener">gvozditut.ru</a>
    </footer>
  </div>
  <script src="site.js"></script>
  {extra_js}
</body>
</html>
"""


def gallery(paths: list[tuple[str, str]]) -> str:
    figs = []
    for src, cap in paths:
        figs.append(f'<figure><img src="{src}" alt="{cap}" loading="lazy" /><figcaption>{cap}</figcaption></figure>')
    return f'<div class="gallery">{"".join(figs)}</div>'


PAGES: dict[str, str] = {}

# ---- INDEX ----
PAGES["index.html"] = page(
    "Собственные бренды",
    f"""
<section class="hero" style="--hero-image:url('assets/products/peny_1.jpg')">
  <p class="eyebrow">Для продавцов розницы</p>
  <h1>Собственные бренды СТМ</h1>
  <p class="lead">Короткие и понятные карточки: что продаём под своими марками, чем отличаются и что сказать покупателю.</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="brand-mika.html">Начать с MIKA</a>
    <a class="btn btn-ghost" href="test.html">Пройти тест</a>
  </div>
</section>

<section class="section">
  <h2>Зачем продавцу знать СТМ</h2>
  <div class="prose">
    <p>СТМ — <strong>собственные торговые марки</strong> сети. Это товары, которые мы рекомендуем в первую очередь: своя марка, понятная цена, качество без переплаты за «громкое имя».</p>
    <ul>
      <li>Легче закрыть потребность покупателя «здесь и сейчас».</li>
      <li>Можно собрать корзину в одном бренде (пена + пистолет, масло + леска, шуруповёрт + биты).</li>
      <li>На сайте помечены как «Своя марка» — это ваш аргумент в зале.</li>
    </ul>
  </div>
</section>

<section class="section">
  <h2>Наши бренды</h2>
  <div class="logo-row">
    <a class="logo-pill" href="brand-mika.html"><img src="assets/logos/mika.jpg" alt="MIKA" /><span>MIKA</span></a>
    <a class="logo-pill" href="brand-torra.html"><img src="assets/logos/torra.jpg" alt="TORRA" /><span>TORRA</span></a>
    <a class="logo-pill" href="brand-inall.html"><img src="assets/logos/inall.jpg" alt="INALL" /><span>INALL</span></a>
    <a class="logo-pill" href="brand-stm.html"><span style="font-family:var(--display);font-size:1.4rem;padding:0.6rem 0">СТМ</span><span>сантехника</span></a>
  </div>
</section>

<section class="section">
  <h2>Как пользоваться обучением</h2>
  <div class="topic-grid">
    <a class="topic-link" href="brand-mika.html"><img src="assets/products/nasosy_1.jpg" alt="" /><div class="meta"><strong>1. Страницы брендов</strong><span>что это, ассортимент, фразы для зала</span></div></a>
    <a class="topic-link" href="analogs.html"><img src="assets/products/bity_1.jpg" alt="" /><div class="meta"><strong>2. Аналоги</strong><span>с чем сравнивают покупатели и что отвечать</span></div></a>
    <a class="topic-link" href="test.html"><img src="assets/products/peny_2.jpg" alt="" /><div class="meta"><strong>3. Тест</strong><span>контрольные вопросы — результат сразу на странице</span></div></a>
  </div>
</section>

<section class="section split">
  <div class="prose">
    <h2 style="margin-top:0;font-family:var(--display);font-size:1.3rem">Одной фразой</h2>
    <ul>
      <li><strong>MIKA</strong> — основной широкий СТМ (химия, насосы, пены, тачки, расходники…).</li>
      <li><strong>TORRA</strong> — бетоносмесители, пена PRO, отрезные круги.</li>
      <li><strong>INALL</strong> — аккумуляторный инструмент (эксклюзив сети).</li>
      <li><strong>СТМ</strong> — сантехника: краны, МП труба, фитинги, комплекты на радиатор.</li>
    </ul>
  </div>
  <div class="media-frame"><img src="assets/peny-shpargalka.jpg" alt="Шпаргалка по пенам" style="object-fit:contain;background:#fff" /></div>
</section>
""",
)

# ---- MIKA ----
PAGES["brand-mika.html"] = page(
    "Бренд MIKA",
    f"""
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>MIKA</h1>
  <p class="lead">Главный бренд СТМ. Если покупатель спрашивает «что у вас своё / посоветуйте нормальное недорого» — чаще начинайте с MIKA.</p>
</header>

<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/mika.jpg" alt="Логотип MIKA" style="width:170px;background:#fff;padding:.55rem;border:1px solid var(--line);border-radius:.7rem" /></p>
    <p>По материалам сайта «У Михалыча»: марка относительно новая, но уже с хорошими отзывами. Баланс <strong>качество + доступная цена + широкий ассортимент</strong>. Производство — на известных заводах России и Китая, контроль качества, низкий процент брака, сервис.</p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что сказать покупателю</h3>
    <ul>
      <li>«Это наша собственная марка — без переплаты за громкое имя».</li>
      <li>«Можно собрать всё нужное в одной линейке».</li>
      <li>«Подходит и для дома/дачи, и для рабочих задач».</li>
    </ul>
  </div>
  {gallery([
    ("assets/products/peny_1.jpg", "Пены"),
    ("assets/products/nasosy_1.jpg", "Насосы"),
    ("assets/web/mika/01.png", "С сайта gvozditut.ru"),
  ])}
</section>

<section class="section">
  <h2>Ассортимент (что лежит в зале)</h2>
  <div class="prose">
    <ul>
      <li><strong>Насосы</strong> — вибрационные (верхний/нижний забор), скважинные, дренажные, станции, поверхностные.</li>
      <li><strong>Бетоносмесители MIKA</strong> — рядом смотрите также TORRA.</li>
      <li><strong>Пены и клей-пена</strong> — бытовая и профессиональная; шпаргалка выбора — ниже по смыслу: щели → бытовая, двери/окна → проф, огонь → огнестойкая.</li>
      <li><strong>Масла</strong> — 2T/4T, цепь, компрессор, ТАД-17 (не путать типы!).</li>
      <li><strong>Растворители и подготовка</strong> — уайт-спирит, 646, 650, ацетон, обезжириватель, грунтовка, огнебио.</li>
      <li><strong>Тачки, мембраны/плёнки, метизы, биты, диски, станки, рулетки/ножи, теплоноситель, лопаты, шланги, электроды, автохимия</strong>.</li>
      <li><strong>Сад</strong> — катушки и леска для триммера.</li>
    </ul>
    <p>Каталог на сайте: <a href="https://gvozditut.ru/brands/mika/" target="_blank" rel="noopener">gvozditut.ru/brands/mika</a></p>
  </div>
</section>

<section class="section">
  <h2>Частые вопросы в зале</h2>
  <div class="prose">
    <ul>
      <li><em>«Чем лучше именитого бренда?»</em> — не «лучше имени», а «то же рабочее качество без переплаты».</li>
      <li><em>«Есть гарантия/сервис?»</em> — да, по правилам сети; при необходимости направляем в сервис.</li>
      <li><em>«2T или 4T масло?»</em> — смотрим технику: двухтакт / четырёхтакт, не взаимозаменяемы.</li>
    </ul>
  </div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="index.html" style="color:inherit;border-color:var(--line);background:#fff">← Главная</a>
  <a class="btn btn-ember" href="brand-torra.html">Далее: TORRA →</a>
</div>
""",
)

# ---- TORRA ----
PAGES["brand-torra.html"] = page(
    "Бренд TORRA",
    f"""
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>TORRA</h1>
  <p class="lead">Узкий, но сильный СТМ: бетоносмесители, профессиональная пена и отрезные круги по металлу.</p>
</header>

<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/torra.jpg" alt="Логотип TORRA" style="width:190px;background:#fff;padding:.55rem;border:1px solid var(--line);border-radius:.7rem" /></p>
    <p>На сайте в карточке бренда — линейка бетоносмесителей разных объёмов, пена <strong>TORRA PRO 65</strong> и супертонкие отрезные круги по металлу/нержавейке.</p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что сказать покупателю</h3>
    <ul>
      <li>«TORRA — наша марка для стройки: миксеры, пена, круги».</li>
      <li>По пене: PRO 65 — профессиональная, под пистолет (рядом с MIKA 65).</li>
      <li>По кругам: тонкий рез металла и нержавейки.</li>
    </ul>
    <p><strong>Важно:</strong> в названиях бетоносмесителей встречается серия AOER — это исполнение внутри TORRA, не отдельный бренд.</p>
  </div>
  {gallery([
    ("assets/web/torra/01.png", "С сайта"),
    ("assets/products/betono_1.jpg", "Бетоносмесители"),
    ("assets/products/diski_3.jpg", "Круги"),
  ])}
</section>

<section class="section">
  <h2>Как продавать рядом с MIKA</h2>
  <div class="prose">
    <ul>
      <li>Бетоносмеситель — уточните объём барабана, сравните MIKA и TORRA.</li>
      <li>Двери/окна — предложите выбор: MIKA 65 проф или TORRA PRO 65.</li>
      <li>Резка металла — круги Torra; камень/бетон/плитка — чаще алмазные диски MIKA.</li>
    </ul>
    <p>Каталог: <a href="https://gvozditut.ru/brands/torra/" target="_blank" rel="noopener">gvozditut.ru/brands/torra</a></p>
  </div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="brand-mika.html" style="color:inherit;border-color:var(--line);background:#fff">← MIKA</a>
  <a class="btn btn-ember" href="brand-inall.html">Далее: INALL →</a>
</div>
""",
)

# ---- INALL ----
PAGES["brand-inall.html"] = page(
    "Бренд INALL",
    f"""
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>INALL</h1>
  <p class="lead">Аккумуляторный бесщеточный инструмент. «У Михалыча» — единственный официальный дистрибьютор Inall в России.</p>
</header>

<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/inall.jpg" alt="Логотип INALL" style="width:190px;background:#fff;padding:.55rem;border:1px solid var(--line);border-radius:.7rem" /></p>
    <p>По сайту: у компании INALL Tools большой опыт в электроинструменте. Инструмент ориентирован на надёжную работу; перед продажей проходит проверку. По заявлениям бренда — уровень, сопоставимый с известными марками (в т.ч. сравнивают с Makita/Bosch), за счёт тех же поставщиков комплектующих и контроля качества.</p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что в линейке</h3>
    <ul>
      <li>Дрели-шуруповёрты (разный вольтаж и момент)</li>
      <li>УШМ (болгарка) аккумуляторная</li>
      <li>Винтовёрт и гайковёрт ударные</li>
      <li>Аккумуляторы (в т.ч. аналоги популярных типоразмеров)</li>
    </ul>
  </div>
  {gallery([
    ("assets/web/inall/01.png", "С сайта"),
    ("assets/products/inall_1.jpg", "Шуруповёрты"),
    ("assets/products/bity_1.jpg", "Апселл: биты MIKA"),
  ])}
</section>

<section class="section">
  <h2>Скрипт продавца</h2>
  <div class="prose">
    <ul>
      <li>Спросите задачу: мебель / стройка / авто / резка.</li>
      <li>Уточните момент (Н·м), напряжение, комплектацию (2 АКБ + ЗУ + кейс).</li>
      <li>Апселл: биты и расходники MIKA.</li>
      <li>«Это эксклюзив нашей сети, с официальной гарантией».</li>
    </ul>
    <p>Каталог: <a href="https://gvozditut.ru/brands/inall/" target="_blank" rel="noopener">gvozditut.ru/brands/inall</a></p>
  </div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="brand-torra.html" style="color:inherit;border-color:var(--line);background:#fff">← TORRA</a>
  <a class="btn btn-ember" href="brand-stm.html">Далее: СТМ сантехника →</a>
</div>
""",
)

# ---- STM plumbing ----
PAGES["brand-stm.html"] = page(
    "Бренд СТМ (сантехника)",
    f"""
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>СТМ — сантехника</h1>
  <p class="lead">Отдельная линейка на сайте под названием «СТМ» / CTM: краны, металлопластик, обжимные фитинги, комплекты на радиатор, группа безопасности котла.</p>
</header>

<section class="section split">
  <div class="prose">
    <p>Не путайте в разговоре с покупателем:</p>
    <ul>
      <li><strong>«СТМ»</strong> как общее слово = все наши собственные марки (MIKA, TORRA, INALL…).</li>
      <li><strong>Бренд «СТМ» / CTM на ценнике</strong> = конкретно сантехническая группа (краны, МП, фитинги).</li>
    </ul>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что предлагать</h3>
    <ul>
      <li>Шаровые краны разных диаметров (рычаг / бабочка, ВР-ВР, ВР-НР).</li>
      <li>Металлопластиковая труба (например 16×2).</li>
      <li>Муфты обжимные промежуточные и с резьбой.</li>
      <li>Комплекты для радиаторов 1/2" и 3/4".</li>
      <li>Группа безопасности котла, аксессуары.</li>
    </ul>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что уточнить у покупателя</h3>
    <ul>
      <li>Диаметр (1/2, 3/4, 1", 16/20/26 мм для МП).</li>
      <li>Тип присоединения: ВР / НР, нужен ли обжим.</li>
      <li>Задача: перекрытие, радиатор, обвязка котла.</li>
    </ul>
    <p>Каталог: <a href="https://gvozditut.ru/brands/stm/" target="_blank" rel="noopener">gvozditut.ru/brands/stm</a></p>
  </div>
  {gallery([
    ("assets/web/stm/01.jpg", "Краны СТМ"),
    ("assets/web/stm/12.jpg", "МП / фитинги"),
    ("assets/web/stm/13.jpg", "С сайта"),
  ])}
</section>

<div class="pager">
  <a class="btn btn-ghost" href="brand-inall.html" style="color:inherit;border-color:var(--line);background:#fff">← INALL</a>
  <a class="btn btn-ember" href="analogs.html">Аналоги брендов →</a>
</div>
""",
)

# ---- ANALOGS ----
PAGES["analogs.html"] = page(
    "Бренды-аналоги",
    """
<header class="page-head">
  <p class="eyebrow">Для работы в зале</p>
  <h1>Разные бренды и аналоги</h1>
  <p class="lead">Покупатель часто сравнивает «с тем, что знает». Ниже — как отвечать коротко и честно, без спора «чей бренд круче».</p>
</header>

<section class="section">
  <h2>Таблица для консультанта</h2>
  <div class="prose" style="overflow:auto">
    <table class="cmp">
      <thead>
        <tr><th>Наша СТМ</th><th>С чем сравнивают</th><th>Как говорить</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>INALL</strong> инструмент</td>
          <td>Makita, Bosch и др.</td>
          <td>«Рабочий бесщеточный инструмент, эксклюзив сети, с гарантией. По комплектующим бренд ориентируется на тот же класс. Давайте подберём по задаче и моменту (Н·м)».</td>
        </tr>
        <tr>
          <td><strong>INALL</strong> АКБ</td>
          <td>Makita BL1840B и аналоги</td>
          <td>В ассортименте есть аккумуляторы-аналоги популярных типоразмеров — сверяем вольтаж и посадку.</td>
        </tr>
        <tr>
          <td><strong>MIKA</strong> пена</td>
          <td>Peter Paul и др. проф. пены</td>
          <td>«Своя марка, под задачу: бытовая / проф / зимняя / огнестойкая / клей-пена». Не продаём «просто баллон» — продаём решение.</td>
        </tr>
        <tr>
          <td><strong>TORRA PRO 65</strong></td>
          <td>Другие проф. пены 65 л</td>
          <td>Альтернатива рядом с MIKA 65 — дайте выбор по наличию и цене.</td>
        </tr>
        <tr>
          <td><strong>MIKA</strong> автохимия</td>
          <td>Romax, Karcher и др.</td>
          <td>«Свои линейки EFFECT / Prof / STANDART — подберём под тип мойки и объём».</td>
        </tr>
        <tr>
          <td><strong>MIKA</strong> расходники</td>
          <td>Любые «известные» биты/диски/масла</td>
          <td>«То же назначение, своя марка, выгоднее по цене. Подберём размер/тип правильно».</td>
        </tr>
        <tr>
          <td><strong>СТМ</strong> сантехника</td>
          <td>Другие обжимные системы / краны</td>
          <td>Сверяем диаметр и тип (ВР/НР, обжим). Не смешиваем несовместимые системы без уточнения.</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section split">
  <div class="prose">
    <h2 style="margin-top:0;font-family:var(--display);font-size:1.25rem">Правила разговора</h2>
    <ul>
      <li>Не ругайте бренд покупателя — переводите на задачу.</li>
      <li>Сначала потребность, потом марка.</li>
      <li>Предлагайте СТМ как основной вариант + 1 альтернативу при необходимости.</li>
      <li>Фиксируйте артикул и наличие перед обещанием.</li>
    </ul>
  </div>
  <div class="prose">
    <h2 style="margin-top:0;font-family:var(--display);font-size:1.25rem">Когда НЕ давить СТМ</h2>
    <ul>
      <li>Покупателю нужен именно совместимый расходник к уже купленному инструменту другой марки.</li>
      <li>Нет нужной фасовки/размера в СТМ — честно предложите аналог из общего ассортимента.</li>
      <li>Гарантийный/сервисный кейс по другой марке — не подменяйте товар.</li>
    </ul>
  </div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="brand-stm.html" style="color:inherit;border-color:var(--line);background:#fff">← СТМ сантехника</a>
  <a class="btn btn-ember" href="test.html">К тесту →</a>
</div>
""",
)

# Write pages first without test; test built separately with embedded questions JS
for name, html in list(PAGES.items()):
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)


TEST_QUESTIONS = [
    {
        "q": "Что такое СТМ в общем смысле для продавца сети?",
        "options": {
            "a": "Только сантехнические краны",
            "b": "Собственные торговые марки сети",
            "c": "Только импортный инструмент",
            "d": "Название акции на выходные",
        },
        "answer": "b",
    },
    {
        "q": "Какой бренд — основной и самый широкий СТМ?",
        "options": {"a": "INALL", "b": "TORRA", "c": "MIKA", "d": "AOER"},
        "answer": "c",
    },
    {
        "q": "INALL — это:",
        "options": {
            "a": "монтажные пены",
            "b": "аккумуляторный инструмент (эксклюзив сети)",
            "c": "только теплоноситель",
            "d": "металлопластиковая труба",
        },
        "answer": "b",
    },
    {
        "q": "TORRA в зале чаще всего:",
        "options": {
            "a": "масла 2T и леска",
            "b": "бетоносмесители, пена PRO, отрезные круги",
            "c": "только шуруповёрты",
            "d": "только мембраны",
        },
        "answer": "b",
    },
    {
        "q": "AOER в названии бетоносмесителя — это:",
        "options": {
            "a": "отдельный бренд СТМ",
            "b": "серия/исполнение внутри TORRA",
            "c": "бренд масел",
            "d": "название пистолета",
        },
        "answer": "b",
    },
    {
        "q": "Для щелей без пистолета лучше предложить:",
        "options": {
            "a": "клей-пену",
            "b": "бытовую пену MIKA 50 с трубкой",
            "c": "только огнестойкую",
            "d": "уайт-спирит",
        },
        "answer": "b",
    },
    {
        "q": "Огнеопасные места — какая пена?",
        "options": {
            "a": "любая всесезонная",
            "b": "только огнестойкая",
            "c": "бытовая MIKA 50",
            "d": "TORRA круг по металлу",
        },
        "answer": "b",
    },
    {
        "q": "Уайт-спирит в водоэмульсионную краску:",
        "options": {
            "a": "можно всегда",
            "b": "нельзя — состав расслоится",
            "c": "только зимой",
            "d": "только с 646",
        },
        "answer": "b",
    },
    {
        "q": "Растворитель 646 в первую очередь для:",
        "options": {
            "a": "водных красок",
            "b": "нитроэмалей и нитролаков",
            "c": "полива огорода",
            "d": "смазки цепи",
        },
        "answer": "b",
    },
    {
        "q": "Масла 2T и 4T взаимозаменяемы?",
        "options": {"a": "да", "b": "нет", "c": "только летом", "d": "только в тачке"},
        "answer": "b",
    },
    {
        "q": "Верхний забор (В) у вибрационного насоса полезен, когда:",
        "options": {
            "a": "нужно забрать ил со дна",
            "b": "важно меньше тянуть грязь со дна",
            "c": "режем металл",
            "d": "клеим блоки",
        },
        "answer": "b",
    },
    {
        "q": "Бренд «СТМ» на ценнике сантехники — это:",
        "options": {
            "a": "то же, что INALL",
            "b": "линейка кранов, МП трубы и фитингов",
            "c": "только бетоносмесители",
            "d": "название акции на пену",
        },
        "answer": "b",
    },
    {
        "q": "К шуруповёрту INALL логичный апселл:",
        "options": {"a": "уайт-спирит", "b": "биты MIKA", "c": "МП муфта 16", "d": "ТАД-17"},
        "answer": "b",
    },
    {
        "q": "Покупатель сравнивает INALL с Makita. Лучший ответ:",
        "options": {
            "a": "Makita всегда хуже",
            "b": "Давайте подберём по задаче и моменту; INALL — эксклюзив сети с гарантией",
            "c": "Откажитесь продавать",
            "d": "Предложите только пену",
        },
        "answer": "b",
    },
    {
        "q": "Круги по металлу/нержавейке в СТМ чаще бренда:",
        "options": {"a": "INALL", "b": "TORRA", "c": "только EFFECT", "d": "GARDEN"},
        "answer": "b",
    },
]

import json

q_json = json.dumps(TEST_QUESTIONS, ensure_ascii=False)

test_body = f"""
<header class="page-head">
  <p class="eyebrow">Самоконтроль</p>
  <h1>Контрольные вопросы</h1>
  <p class="lead">Ответьте на вопросы по теме СТМ. Нажмите «Проверить» — результат появится сразу на этой странице.</p>
</header>

<section class="quiz-block" id="test">
  <h2>Тест для продавца</h2>
  <p class="hint">Один правильный ответ в каждом вопросе. Можно сбросить и пройти ещё раз.</p>
  <form id="self-test" data-mini-quiz>
    <div id="questions-root"></div>
    <div class="quiz-actions">
      <button class="btn btn-primary" type="submit">Проверить</button>
      <button class="btn btn-ghost" type="button" data-reset>Сбросить</button>
    </div>
    <div class="quiz-result" id="final-result" aria-live="polite"></div>
  </form>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="analogs.html" style="color:inherit;border-color:var(--line);background:#fff">← Аналоги</a>
  <a class="btn btn-ember" href="index.html">На главную</a>
</div>
"""

extra = f"""
<script>
const QUESTIONS = {q_json};
const root = document.getElementById('questions-root');
QUESTIONS.forEach((q, i) => {{
  const n = i + 1;
  const wrap = document.createElement('div');
  wrap.className = 'q-item';
  wrap.dataset.answer = q.answer;
  let opts = '';
  Object.entries(q.options).forEach(([key, text]) => {{
    opts += `<label><input type="radio" name="tq${{n}}" value="${{key}}" /><span>${{text}}</span></label>`;
  }});
  wrap.innerHTML = `<h3>${{n}}. ${{q.q}}</h3><div class="q-options">${{opts}}</div>`;
  root.appendChild(wrap);
}});
</script>
"""

(ROOT / "test.html").write_text(page("Тест самоконтроля", test_body, extra), encoding="utf-8")
print("wrote test.html")

# CSS addition for comparison table
css_path = ROOT / "site.css"
css = css_path.read_text(encoding="utf-8")
if ".cmp" not in css:
    css += """

table.cmp {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.92rem;
}
table.cmp th, table.cmp td {
  border: 1px solid var(--line);
  padding: 0.65rem 0.7rem;
  vertical-align: top;
  text-align: left;
}
table.cmp th {
  background: #e7eddc;
  font-family: var(--display);
  font-size: 0.85rem;
}
table.cmp tr:nth-child(even) td { background: #f7f9f2; }
"""
    css_path.write_text(css, encoding="utf-8")
    print("updated site.css")

# README
(ROOT / "README.md").write_text(
    """# Обучение СТМ для продавцов розницы

Презентация собственных брендов сети «У Михалыча» (MIKA / TORRA / INALL / СТМ сантехника).

## Онлайн

https://arimberg-svg.github.io/stm-mika-quiz/

## Страницы

- `index.html` — что такое СТМ
- `brand-mika.html`, `brand-torra.html`, `brand-inall.html`, `brand-stm.html` — по брендам
- `analogs.html` — аналоги и как отвечать в зале
- `test.html` — контрольные вопросы, результат сразу на странице

Материалы: обучающие папки СТМ + тексты/ассортимент с [gvozditut.ru](https://gvozditut.ru/brands/mika/).

## Сборка

```bash
python rebuild_site.py
```
""",
    encoding="utf-8",
)

# Remove obsolete topic pages from being linked; leave files or delete
obsolete = [
    "topics.html",
    "topic-peny.html",
    "topic-masla.html",
    "topic-nasosy.html",
    "topic-rastvoriteli.html",
    "topic-stroyka.html",
    "topic-instrument.html",
    "topic-sad.html",
    "topic-avtohimiya.html",
    "quiz.html",
]
for name in obsolete:
    p = ROOT / name
    if p.exists():
        p.unlink()
        print("removed", name)

print("DONE")
