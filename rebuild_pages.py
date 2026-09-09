# -*- coding: utf-8 -*-
"""Rebuild training site pages: remove STM plumbing, update MIKA/TORRA/home."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NAV = (
    '<a href="index.html">Главная</a>'
    '<a href="brand-mika.html">MIKA</a>'
    '<a href="brand-torra.html">TORRA</a>'
    '<a href="brand-inall.html">INALL</a>'
    '<a href="analogs.html">Аналоги</a>'
    '<a href="test.html">Тест</a>'
)

FOOT = """    <footer class="foot">
      Материалы для продавцов розницы сети «У Михалыча» · собственные бренды MIKA / TORRA / INALL
      <a href="https://gvozditut.ru/brands/mika/" target="_blank" rel="noopener">gvozditut.ru</a>
    </footer>"""


def shell(title: str, theme: str, body: str, logo: str = "assets/logos/umih.jpg", lockup_alt: str = "У Михалыча") -> str:
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Обучение «У Михалыча»</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;800&family=Unbounded:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="site.css" />
</head>
<body class="theme-{theme}">
  <div class="site">
    <header class="topnav">
      <div class="topnav-inner">
        <a class="brand-lockup" href="index.html">
          <img src="{logo}" alt="{lockup_alt}" />
          <span>Обучение · свои марки</span>
        </a>
        <nav class="nav-links">{NAV}</nav>
      </div>
    </header>
    <main class="wrap">
{body}
    </main>
{FOOT}
  </div>
  <script src="site.js"></script>
</body>
</html>
"""


INDEX = shell(
    "Собственные бренды",
    "home",
    """
<section class="hero">
  <div class="hero-copy">
    <p class="eyebrow">Для продавцов розницы</p>
    <h1>Собственные бренды</h1>
    <p class="lead">Короткие карточки MIKA, TORRA и INALL: что продаём, чем отличаются и что сказать покупателю.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="brand-mika.html">Начать с MIKA</a>
      <a class="btn btn-ghost" href="test.html">Пройти тест</a>
    </div>
  </div>
  <div class="hero-visual hero-logo">
    <img src="assets/logos/umih.jpg" alt="Логотип сети У Михалыча" />
  </div>
</section>

<section class="section">
  <h2>Зачем продавцу знать свои марки</h2>
  <div class="prose">
    <p>Это <strong>собственные торговые марки</strong> сети. Их рекомендуем в первую очередь: своя марка, понятная цена, качество без переплаты за «громкое имя».</p>
    <ul>
      <li>Легче закрыть потребность покупателя «здесь и сейчас».</li>
      <li>Можно собрать корзину в одной линейке (пена + пистолет, масло + леска, шуруповёрт + биты).</li>
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
  </div>
</section>

<section class="section">
  <h2>Как пользоваться обучением</h2>
  <div class="topic-grid">
    <a class="topic-link topic-icon" href="brand-mika.html">
      <div class="icon-box" aria-hidden="true">
        <svg viewBox="0 0 64 64" fill="none"><rect x="10" y="8" width="34" height="48" rx="4" stroke="currentColor" stroke-width="3"/><path d="M18 20h18M18 30h18M18 40h12" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="46" cy="46" r="10" fill="currentColor"/><path d="M46 41v10M41 46h10" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/></svg>
      </div>
      <div class="meta"><strong>1. Страницы брендов</strong><span>что это, ассортимент, фразы для зала</span></div>
    </a>
    <a class="topic-link topic-icon" href="analogs.html">
      <div class="icon-box" aria-hidden="true">
        <svg viewBox="0 0 64 64" fill="none"><path d="M14 40V24l18-12 18 12v16l-18 12-18-12z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M32 28v24M14 24l18 12 18-12" stroke="currentColor" stroke-width="3"/></svg>
      </div>
      <div class="meta"><strong>2. Аналоги</strong><span>с чем сравнивают покупатели и что отвечать</span></div>
    </a>
    <a class="topic-link topic-icon" href="test.html">
      <div class="icon-box" aria-hidden="true">
        <svg viewBox="0 0 64 64" fill="none"><circle cx="32" cy="32" r="22" stroke="currentColor" stroke-width="3"/><path d="M20 33l8 8 16-18" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </div>
      <div class="meta"><strong>3. Тест</strong><span>контрольные вопросы — результат сразу на странице</span></div>
    </a>
  </div>
</section>

<section class="section split split-cheat">
  <div class="prose">
    <h2 style="margin-top:0;font-family:var(--display);font-size:1.3rem">Одной фразой</h2>
    <ul>
      <li><strong>MIKA</strong> — основной широкий бренд (химия, насосы, пены, тачки, расходники…).</li>
      <li><strong>TORRA</strong> — бетоносмесители, пена PRO, отрезные круги.</li>
      <li><strong>INALL</strong> — аккумуляторный инструмент (эксклюзив сети).</li>
    </ul>
  </div>
  <div class="media-frame media-frame-lg"><img src="assets/peny-shpargalka.jpg" alt="Шпаргалка по пенам MIKA" /></div>
</section>
""",
)

MIKA = shell(
    "Бренд MIKA",
    "mika",
    """
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>MIKA</h1>
  <p class="lead">Главный собственный бренд. Если покупатель спрашивает «что у вас своё / посоветуйте нормальное недорого» — чаще начинайте с MIKA.</p>
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
  <div class="gallery gallery-2">
    <figure><div class="img-box"><img src="assets/web/mika/foam_pro65_can.jpg" alt="Пена MIKA 65" loading="lazy" /></div><figcaption>Пена проф. MIKA 65</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/nasosy_1.jpg" alt="Насосы MIKA" loading="lazy" /></div><figcaption>Насосы MIKA</figcaption></figure>
  </div>
</section>

<section class="section">
  <h2>Монтажные пены</h2>
  <div class="gallery">
    <figure><div class="img-box"><img src="assets/web/mika/foam_site_pro65_0.jpg" alt="MIKA 65 с сайта" loading="lazy" /></div><figcaption>Проф. всесезонная MIKA 65 (сайт)</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_pro65_can.jpg" alt="MIKA 65" loading="lazy" /></div><figcaption>MIKA 65 — баллон</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_site_glue.jpg" alt="Клей-пена" loading="lazy" /></div><figcaption>Клей-пена проф. MIKA (сайт)</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_winter.jpg" alt="Зимняя пена" loading="lazy" /></div><figcaption>Зимняя пена</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_fire.jpg" alt="Огнестойкая" loading="lazy" /></div><figcaption>Огнестойкая пена</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_50.jpg" alt="MIKA 50" loading="lazy" /></div><figcaption>Бытовая / MIKA 50</figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <p>Подбор: щели → бытовая; двери/окна → проф под пистолет; мороз → зимняя; огонь → огнестойкая; плиты/блоки → клей-пена. Шпаргалка — на <a href="index.html">главной</a>.</p>
  </div>
</section>

<section class="section">
  <h2>Все насосы MIKA</h2>
  <p>Полный список из каталога. Уточняйте наличие и артикул на складе.</p>
  <div class="prose" style="overflow:auto">
    <table class="cmp">
      <thead>
        <tr><th>Артикул</th><th>Наименование</th><th>Ключевое</th></tr>
      </thead>
      <tbody>
        <tr><td>335110В</td><td>Вибрационный ВПН-10В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 10 м · напор 60–70 м</td></tr>
        <tr><td>335110Н</td><td>Вибрационный ВПН-10Н (нижний забор)</td><td>280 Вт · 18 л/мин · кабель 10 м · напор 60–70 м</td></tr>
        <tr><td>335115В</td><td>Вибрационный ВПН-15В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 15 м</td></tr>
        <tr><td>335115Н</td><td>Вибрационный ВПН-15Н (нижний забор)</td><td>280 Вт · 18 л/мин · кабель 15 м</td></tr>
        <tr><td>335125В</td><td>Вибрационный ВПН-25В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 25 м</td></tr>
        <tr><td>335125Н</td><td>Вибрационный ВПН-25Н (нижний забор)</td><td>280 Вт · 18 л/мин · кабель 25 м</td></tr>
        <tr><td>335140В</td><td>Вибрационный ВПН-40В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 40 м · выход ¾″</td></tr>
        <tr><td>33528D</td><td>Дренажный ДН-750 Вт (грязная вода)</td><td>750 Вт · 10 м³/ч · напор 10 м · частицы / универсальный фитинг</td></tr>
        <tr><td>335275D</td><td>Дренажный НД-750</td><td>750 Вт · 13 000 л/ч · напор 7,5 м · частицы до 30 мм</td></tr>
        <tr><td>335324L</td><td>Насосная станция НС-750 · 24 л</td><td>750 Вт · напор 50 м · 3600 л/ч · бак 24 л · чугун</td></tr>
        <tr><td>3354370В</td><td>Скважинный винтовой СН-В 370 Вт</td><td>25 л/мин · напор 45 м · Ø 3,5″ · кабель 20 м</td></tr>
        <tr><td>3354550В</td><td>Скважинный винтовой СН-В 550 Вт</td><td>30 л/мин · напор 90 м · кабель 20 м</td></tr>
        <tr><td>335430Ц</td><td>Скважинный центробежный СН-Ц 370 Вт</td><td>47 л/мин · напор 50 м · кабель 30 м · Ø 3″</td></tr>
        <tr><td>335450Ц</td><td>Скважинный центробежный СН-Ц 550 Вт</td><td>47 л/мин · напор 70 м · кабель 50 м · Ø 3″</td></tr>
        <tr><td>335543П</td><td>Поверхностный ПН-800</td><td>800 Вт · напор 43 м · 5000 л/ч · всас 8 м</td></tr>
      </tbody>
    </table>
  </div>
  <div class="gallery" style="margin-top:1rem">
    <figure><div class="img-box"><img src="assets/products/nasosy_1.jpg" alt="Насос MIKA" loading="lazy" /></div><figcaption>Вибрационные / погружные</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/nasosy_2.jpg" alt="Насос MIKA" loading="lazy" /></div><figcaption>Скважинные / станции</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/nasosy_3.jpg" alt="Насос MIKA" loading="lazy" /></div><figcaption>Поверхностные / дренаж</figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <p><strong>В зале:</strong> верхний забор — чистая вода сверху; нижний — когда нужно забрать почти до дна. Скважинный винтовой терпит больше примесей, центробежный — чище вода и выше производительность.</p>
  </div>
</section>

<section class="section">
  <h2>Угольные брикеты MIKA, 3 кг</h2>
  <p>Арт. 331113. Плотные брикеты — разжигать иначе, чем обычный уголь из пыли.</p>
  <div class="gallery gallery-2">
    <figure><div class="img-box"><img src="assets/web/mika/briquettes.jpg" alt="Угольные брикеты MIKA" loading="lazy" /></div><figcaption>Угольные брикеты MIKA, 3 кг</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/briquettes_2.jpg" alt="Брикеты в упаковке" loading="lazy" /></div><figcaption>Упаковка / вид брикетов</figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <h3 style="font-family:var(--display);font-size:1.05rem;margin-top:0">Сценарий №1 — самый быстрый (стартером)</h3>
    <p>Самый быстрый способ разжечь именно эти плотные брикеты — стартером. Засыпаете их сверху, снизу ставите один-два спиртовых тюбика. Поджигаете. За счёт плотной тяги внутри цилиндра тяжёлые брикеты схватываются равномерно. Буквально 15–20 минут — и всё готово.</p>

    <h3 style="font-family:var(--display);font-size:1.05rem">Сценарий №2 — экономичный «Домиком» (без стартера)</h3>
    <p>Поскольку брикеты тяжелее и плотнее обычной древесной пыли, им нужен правильный подвод воздуха снизу.</p>
    <p><strong>Шаг 1 (классический).</strong> Строим из самих брикетов колодец или шалашик. Пустота внутри даст отличную тягу. А внутрь «домика» подкладываем лёгкие дровишки — щепу, тонкие ветки или лучину. Они быстро займутся и плавно разогреют массивные брикеты по краям. Через те же 15–20 минут всё прогорит ровно.</p>
    <p><strong>Шаг 2 (гибридный, если нет мелких дров).</strong> Если тонких дров под рукой нет, можно использовать спиртовые тюбики. Кладёте их прямо на дно мангала, строите над ними тот же домик из брикетов, а сверху можете накинуть немного крупных дров для аромата, если нужно. Тюбики дадут мощный импульс снизу, чтобы пробить плотность брикета.</p>

    <h3 style="font-family:var(--display);font-size:1.05rem">Важно сказать покупателю</h3>
    <p>С этими брикетами главное правило — <strong>не торопиться</strong>. Не лейте жидкость и не пытайтесь раздуть их мехами сразу. Дайте этим 15–20 минут. И где-то в начале придётся придерживать огонь, аккуратно подкидывая мелкие веточки, пока конструкция не окрепнет.</p>
  </div>
</section>

<section class="section">
  <h2>Остальной ассортимент</h2>
  <div class="prose">
    <ul>
      <li><strong>Бетоносмесители MIKA</strong> — рядом смотрите также TORRA.</li>
      <li><strong>Масла</strong> — 2T/4T, цепь, компрессор, ТАД-17 (не путать типы!).</li>
      <li><strong>Растворители и подготовка</strong> — уайт-спирит, 646, 650, ацетон, обезжириватель, грунтовка, огнебио.</li>
      <li><strong>Тачки, мембраны/плёнки, метизы, биты, диски, станки, рулетки/ножи, теплоноситель, лопаты, шланги, электроды, автохимия</strong>.</li>
      <li><strong>Сад</strong> — катушки и леска для триммера.</li>
    </ul>
    <p>Каталог: <a href="https://gvozditut.ru/brands/mika/" target="_blank" rel="noopener">gvozditut.ru/brands/mika</a></p>
  </div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="index.html" style="color:inherit;border-color:var(--line);background:#fff">← Главная</a>
  <a class="btn btn-ember" href="brand-torra.html">Далее: TORRA →</a>
</div>
""",
    logo="assets/logos/mika.jpg",
    lockup_alt="MIKA",
)

TORRA = shell(
    "Бренд TORRA",
    "torra",
    """
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>TORRA</h1>
  <p class="lead">Бетоносмесители разных объёмов, профессиональная пена TORRA PRO 65 и супертонкие отрезные круги по металлу и нержавейке.</p>
</header>

<section class="section">
  <div class="prose">
    <p><img src="assets/logos/torra.jpg" alt="Логотип TORRA" style="width:190px;background:#fff;padding:.55rem;border:1px solid var(--line);border-radius:.7rem" /></p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что сказать покупателю</h3>
    <ul>
      <li>«TORRA — наша марка для стройки: миксеры, пена, круги».</li>
      <li>По пене: PRO 65 — профессиональная, под пистолет (рядом с MIKA 65).</li>
      <li>По кругам: тонкий рез металла и нержавейки.</li>
    </ul>
    <p><strong>Важно:</strong> в названиях бетоносмесителей встречается серия AOER — это исполнение внутри TORRA, не отдельный бренд.</p>
  </div>
</section>

<section class="section">
  <h2>Бетоносмесители TORRA</h2>
  <div class="gallery gallery-products">
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_140.jpg" alt="Бетоносмеситель TORRA 140L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 140L<br /><span class="art">арт. 84040CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_160.jpg" alt="Бетоносмеситель TORRA 160L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 160L<br /><span class="art">арт. 84050CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_180.jpg" alt="Бетоносмеситель TORRA 180L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 180L<br /><span class="art">арт. 84060CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_200.jpg" alt="Бетоносмеситель TORRA 200L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 200L<br /><span class="art">арт. 84070CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_220.jpg" alt="Бетоносмеситель TORRA 220L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 220L<br /><span class="art">арт. 84072CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_65.jpg" alt="Бетоносмеситель TORRA 65L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 65L<br /><span class="art">арт. 84009</span></figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <p>Также в линейке исполнения <strong>TORRA …L (AOER)</strong>: 140 / 160 / 180 / 200 / 220 / 240 л — уточняйте наличие в зале.</p>
  </div>
</section>

<section class="section">
  <h2>Пена TORRA PRO 65</h2>
  <div class="gallery gallery-2">
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/foam_pro65.jpg" alt="TORRA PRO 65" loading="lazy" /></div><figcaption>Пена монтажная проф. TORRA PRO 65</figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/products/peny_2.jpg" alt="Пена в зале" loading="lazy" /></div><figcaption>Рядом с MIKA 65 — дайте выбор</figcaption></figure>
  </div>
</section>

<section class="section">
  <h2>Отрезные круги Torra</h2>
  <div class="gallery">
    <figure><div class="img-box img-box-lg"><img src="assets/products/diski_1.jpg" alt="Круг Torra 125" loading="lazy" /></div><figcaption>Круг 125×1,0×22,2 мм · металл / нерж.<br /><span class="art">арт. 338142125-10</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/products/diski_2.jpg" alt="Круг Torra 125" loading="lazy" /></div><figcaption>Круг 125×1,2×22,2 мм · металл / нерж.<br /><span class="art">арт. 338142125-12</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/products/diski_3.jpg" alt="Круг Torra 230" loading="lazy" /></div><figcaption>Круг 230×1,6 / 2,0×22,2 мм · металл / нерж.<br /><span class="art">арт. 338142230-16 / -20</span></figcaption></figure>
  </div>
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
    logo="assets/logos/torra.jpg",
    lockup_alt="TORRA",
)

INALL = shell(
    "Бренд INALL",
    "inall",
    """
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>INALL</h1>
  <p class="lead">Аккумуляторный бесщеточный инструмент. «У Михалыча» — единственный официальный дистрибьютор Inall в России.</p>
</header>

<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/inall.jpg" alt="Логотип INALL" style="width:190px;background:#fff;padding:.55rem;border:1px solid var(--line);border-radius:.7rem" /></p>
    <p>По сайту: у компании INALL Tools большой опыт в электроинструменте. Инструмент ориентирован на надёжную работу; перед продажей проходит проверку. По заявлениям бренда — уровень, сопоставимый с известными марками, за счёт тех же поставщиков комплектующих и контроля качества.</p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что в линейке</h3>
    <ul>
      <li>Дрели-шуруповёрты (разный вольтаж и момент)</li>
      <li>УШМ (болгарка) аккумуляторная</li>
      <li>Винтовёрт и гайковёрт ударные</li>
      <li>Аккумуляторы (в т.ч. аналоги популярных типоразмеров)</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><div class="img-box"><img src="assets/web/inall/01.png" alt="INALL" loading="lazy" /></div><figcaption>Шуруповёрт INALL</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/inall_1.jpg" alt="Линейка INALL" loading="lazy" /></div><figcaption>Линейка в зале</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/bity_1.jpg" alt="Биты MIKA" loading="lazy" /></div><figcaption>Апселл: биты MIKA</figcaption></figure>
  </div>
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
  <a class="btn btn-ember" href="analogs.html">Далее: аналоги →</a>
</div>
""",
    logo="assets/logos/inall.jpg",
    lockup_alt="INALL",
)

ANALOGS = shell(
    "Бренды-аналоги",
    "analogs",
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
        <tr><th>Наша марка</th><th>С чем сравнивают</th><th>Как говорить</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>INALL</strong> инструмент</td>
          <td>Makita, Bosch и др.</td>
          <td>«Рабочий бесщеточный инструмент, эксклюзив сети, с гарантией. Давайте подберём по задаче и моменту (Н·м)».</td>
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
      <li>Предлагайте свою марку как основной вариант + 1 альтернативу при необходимости.</li>
      <li>Фиксируйте артикул и наличие перед обещанием.</li>
    </ul>
  </div>
  <div class="prose">
    <h2 style="margin-top:0;font-family:var(--display);font-size:1.25rem">Когда НЕ давить свою марку</h2>
    <ul>
      <li>Покупателю нужен именно совместимый расходник к уже купленному инструменту другой марки.</li>
      <li>Нет нужной фасовки/размера — честно предложите аналог из общего ассортимента.</li>
      <li>Гарантийный/сервисный кейс по другой марке — не подменяйте товар.</li>
    </ul>
  </div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="brand-inall.html" style="color:inherit;border-color:var(--line);background:#fff">← INALL</a>
  <a class="btn btn-ember" href="test.html">К тесту →</a>
</div>
""",
)

QUESTIONS = [
    {
        "q": "Что такое собственные бренды сети для продавца?",
        "options": {
            "a": "Только сантехнические краны",
            "b": "Свои торговые марки (MIKA, TORRA, INALL), которые рекомендуем в первую очередь",
            "c": "Только импортный инструмент",
            "d": "Название акции на выходные",
        },
        "answer": "b",
    },
    {
        "q": "Какой бренд — основной и самый широкий?",
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
            "a": "отдельный бренд",
            "b": "серия/исполнение внутри TORRA",
            "c": "бренд масел",
            "d": "название пистолета",
        },
        "answer": "b",
    },
    {
        "q": "Для щелей без пистолета лучше предложить:",
        "options": {
            "a": "только огнестойкую пену",
            "b": "бытовую монтажную пену",
            "c": "только клей-пену",
            "d": "масло 2T",
        },
        "answer": "b",
    },
    {
        "q": "Самый быстрый способ разжечь плотные угольные брикеты MIKA:",
        "options": {
            "a": "сразу раздувать мехами и лить жидкость",
            "b": "стартером: брикеты сверху, снизу 1–2 спиртовых тюбика, 15–20 минут",
            "c": "только сырые дрова без воздуха",
            "d": "подождать сутки без огня",
        },
        "answer": "b",
    },
    {
        "q": "Главное правило по брикетам MIKA для покупателя:",
        "options": {
            "a": "торопить и заливать жидкостью",
            "b": "не торопиться 15–20 минут, не лить жидкость и не раздувать сразу",
            "c": "использовать только газ",
            "d": "разжигать в закрытой комнате без тяги",
        },
        "answer": "b",
    },
    {
        "q": "Вибрационный насос «верхний забор» лучше, когда:",
        "options": {
            "a": "нужно забрать воду почти до дна с песком",
            "b": "берём более чистую воду сверху колодца/ёмкости",
            "c": "нужна станция с баком 24 л",
            "d": "режем металл кругом Torra",
        },
        "answer": "b",
    },
    {
        "q": "Круги по металлу/нержавейке своей марки чаще бренда:",
        "options": {"a": "INALL", "b": "только MIKA", "c": "Torra / TORRA", "d": "AOER как отдельный бренд"},
        "answer": "c",
    },
]

TEST = shell(
    "Тест самоконтроля",
    "test",
    f"""
<header class="page-head">
  <p class="eyebrow">Проверка знаний</p>
  <h1>Тест самоконтроля</h1>
  <p class="lead">Ответьте на вопросы по своим маркам. Нажмите «Проверить» — результат появится сразу на этой странице.</p>
</header>

<section class="quiz-block" id="quiz" data-questions='{json.dumps(QUESTIONS, ensure_ascii=False)}'>
  <h2>Вопросы</h2>
  <p class="hint">Выберите один вариант в каждом вопросе.</p>
  <div id="quiz-questions"></div>
  <div class="quiz-actions">
    <button type="button" class="btn btn-primary" id="quiz-check">Проверить</button>
    <button type="button" class="btn btn-ghost" id="quiz-reset">Сбросить</button>
  </div>
  <div class="quiz-result" id="quiz-result" aria-live="polite"></div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="analogs.html" style="color:inherit;border-color:var(--line);background:#fff">← Аналоги</a>
  <a class="btn btn-ember" href="index.html">На главную</a>
</div>
""",
)


CSS_EXTRA = """
/* Убрана тема СТМ-сантехники */
body.theme-torra {
  --brand: #f07a1a;
  --brand-strong: #c45a00;
  --brand-soft: #ffffff;
  --on-brand: #ffffff;
  --ember: #f07a1a;
  background: #ffffff;
}

.hero-logo {
  background: #ffffff;
  min-height: 220px;
}
.hero-logo img {
  max-height: 140px;
  width: auto;
  max-width: 100%;
  object-fit: contain;
}

.brand-lockup img[src*="umih"] {
  width: auto;
  height: 2.4rem;
  max-width: 9rem;
  object-fit: contain;
  padding: 0.2rem 0.35rem;
}

.topic-icon .icon-box {
  background: #f7f7f7;
  min-height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--brand-strong);
  padding: 1.2rem;
}
.topic-icon .icon-box svg {
  width: 64px;
  height: 64px;
}
.topic-icon .img-box { display: none; }

.split-cheat {
  grid-template-columns: 0.85fr 1.15fr;
  align-items: start;
}
@media (max-width: 860px) {
  .split-cheat { grid-template-columns: 1fr; }
}

.media-frame-lg {
  min-height: 420px;
  padding: 0.75rem;
}
.media-frame-lg img {
  max-height: none;
  width: 100%;
  height: auto;
  object-fit: contain;
}

.gallery-2 {
  grid-template-columns: repeat(2, 1fr);
}
.gallery-products {
  grid-template-columns: repeat(3, 1fr);
}
@media (max-width: 720px) {
  .gallery-2,
  .gallery-products { grid-template-columns: 1fr; }
}

.img-box-lg {
  min-height: 320px !important;
  background: #ffffff !important;
}
.img-box-lg img,
.gallery .img-box-lg img {
  max-height: 380px !important;
}

.gallery figcaption .art {
  display: block;
  font-weight: 600;
  color: #888;
  font-size: 0.8rem;
  margin-top: 0.2rem;
}

body.theme-torra .page-head,
body.theme-torra .prose,
body.theme-torra .gallery figure,
body.theme-torra .media-frame,
body.theme-torra .topnav {
  background: #ffffff;
}
body.theme-torra .page-head {
  border: 1px solid var(--line);
  border-left: 6px solid var(--brand);
}
"""


def patch_css():
    css_path = ROOT / "site.css"
    css = css_path.read_text(encoding="utf-8")
    # remove stm theme block
    start = css.find("/* СТМ сантехника")
    if start != -1:
        end = css.find("/* Аналоги", start)
        if end != -1:
            css = css[:start] + css[end:]
    marker = "/* PATCH_UMIH_2026 */"
    if marker not in css:
        css = css.rstrip() + "\n\n" + marker + "\n" + CSS_EXTRA
    else:
        pre = css.split(marker)[0]
        css = pre.rstrip() + "\n\n" + marker + "\n" + CSS_EXTRA
    # bump gallery sizes a bit for all
    css = css.replace("min-height: 260px;", "min-height: 280px;")
    css = css.replace("max-height: 320px;", "max-height: 360px;")
    css_path.write_text(css, encoding="utf-8")


def main():
    (ROOT / "index.html").write_text(INDEX, encoding="utf-8")
    (ROOT / "brand-mika.html").write_text(MIKA, encoding="utf-8")
    (ROOT / "brand-torra.html").write_text(TORRA, encoding="utf-8")
    (ROOT / "brand-inall.html").write_text(INALL, encoding="utf-8")
    (ROOT / "analogs.html").write_text(ANALOGS, encoding="utf-8")
    (ROOT / "test.html").write_text(TEST, encoding="utf-8")
    stm = ROOT / "brand-stm.html"
    if stm.exists():
        stm.unlink()
        print("deleted brand-stm.html")
    patch_css()
    # ensure site.js works with data-questions on #quiz
    print("pages written")


if __name__ == "__main__":
    main()
