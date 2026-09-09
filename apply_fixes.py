# -*- coding: utf-8 -*-
"""Apply latest content/image/CSS fixes to training site."""
from __future__ import annotations

import json
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

FAV = '  <link rel="icon" href="assets/favicon.png" type="image/png" />\n  <link rel="shortcut icon" href="favicon.ico" />'

FOOT = """    <footer class="foot">
      Материалы для продавцов розницы сети «У Михалыча» · собственные бренды MIKA / TORRA / INALL
      <a href="https://gvozditut.ru/brands/mika/" target="_blank" rel="noopener">gvozditut.ru</a>
    </footer>"""


def shell(title: str, theme: str, body: str, logo: str, alt: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — Обучение «У Михалыча»</title>
{FAV}
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
          <img src="{logo}" alt="{alt}" />
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


SELL = {
    "Пены": "Спросите задачу (щели / двери / окна / огонь / приклейка). Предложите бытовую или проф, пистолет к проф-пене, очиститель.",
    "МАСЛА": "Уточните технику: 2T или 4T — не взаимозаменяемы. Цепь / компрессор / ТАД-17 — только по назначению. Сверьте фасовку 100 мл / 1 л.",
    "НАСОСЫ": "Верхний или нижний забор, глубина, напор, чистая или грязная вода. Скважина — винтовой (примеси) или центробежный (чище, больше л/мин).",
    "РАСТВОРИТЕЛИ, огнебио, грунтовк": "Под задачу: обезжирить / разбавить ЛКМ / снять / защитить дерево. Напомните про вентиляцию и перчатки.",
    "ПИСТОЛЕТЫ": "К проф-пене предложите пистолет: эконом / металл / тефлон. Скажите про промывку очистителем после работы.",
    "ТАЧКИ": "Объём кузова, колесо (пневмо/литое), для сада или стройки. Сверьте наличие на складе.",
    "КАТУШКИ": "Под триммер: диаметр лески и тип головки. Можно сразу предложить запас лески MIKA.",
    "МЕТИЗЫ": "Тип крепежа, диаметр, длина, покрытие. Не смешивайте «похожее» без сверки размера.",
    "ЛЕСКА": "Диаметр и сечение (круг / квадрат / витой). Сверьте с катушкой и моделью триммера.",
    "БИТЫ": "К шуруповёрту / INALL: тип шлица, длина, магнит. Наборы выгоднее по цене за единицу.",
    "БЕТОНОСМЕСИТЕЛИ": "Объём барабана под объём работ. Рядом покажите TORRA как альтернативу по цене/наличию.",
    "МЕМБРАНЫ И ПЛЕНКИ": "Паро/гидро/ветрозащита — по узлу кровли или каркаса. Не путайте стороны укладки.",
    "МЫЛО И АВТОШАМПУНИ": "Тип мойки и объём. Линейки EFFECT / Prof / STANDART — под интенсивность.",
    "СТАНКИ": "Задача: заточка / резка / сверление. Уточните питание и комплектность.",
    "РУЛЕТКИ НОЖИ ЛЕЗВИЯ": "Длина ленты / тип ножа. Предложите запасные лезвия к ножу.",
    "ДИСКИ АЛМАЗНЫЕ И КРУГИ ОТРЕЗНЫЕ": "Материал: бетон/камень/плитка → алмаз MIKA; металл/нерж → круги TORRA.",
    "ТЕПЛОНОСИТЕЛЬ": "Объём системы, температура, материал труб. Не смешивайте разные составы без инструкции.",
    "ЛОПАТЫ": "Садовая / снег / штыковая — под задачу и рукоять.",
    "ЭЛЕКТРОДЫ": "Диаметр и тип покрытия под металл и аппарат. Сверьте ток.",
    "ШЛАНГИ": "Диаметр, длина, давление/назначение (полив / воздух).",
}

IMG = {
    "Пены": "assets/web/mika/foam_mika65.jpg",
    "МАСЛА": "assets/products/masla_1.jpg",
    "НАСОСЫ": "assets/products/nasosy_1.jpg",
    "РАСТВОРИТЕЛИ, огнебио, грунтовк": "assets/products/rastvoriteli_1.jpg",
    "ПИСТОЛЕТЫ": "assets/web/mika/foam_mika65.jpg",
    "ТАЧКИ": "assets/products/tachki_1.jpg",
    "КАТУШКИ": "assets/products/masla_2.jpg",
    "МЕТИЗЫ": "assets/products/bity_2.jpg",
    "ЛЕСКА": "assets/products/masla_3.jpg",
    "БИТЫ": "assets/products/bity_1.jpg",
    "БЕТОНОСМЕСИТЕЛИ": "assets/products/betono_1.jpg",
    "МЕМБРАНЫ И ПЛЕНКИ": "assets/products/membrany_1.jpg",
    "МЫЛО И АВТОШАМПУНИ": "assets/products/myla_1.jpg",
    "СТАНКИ": "assets/products/stanki_1.jpg",
    "РУЛЕТКИ НОЖИ ЛЕЗВИЯ": "assets/products/bity_3.jpg",
    "ДИСКИ АЛМАЗНЫЕ И КРУГИ ОТРЕЗНЫЕ": "assets/products/diski_1.jpg",
    "ТЕПЛОНОСИТЕЛЬ": "assets/products/rastvoriteli_2.jpg",
    "ЛОПАТЫ": "assets/products/tachki_2.jpg",
    "ЭЛЕКТРОДЫ": "assets/products/stanki_2.jpg",
    "ШЛАНГИ": "assets/products/tachki_3.jpg",
}

TITLES = {
    "Пены": "Монтажные пены и клей-пена",
    "МАСЛА": "Масла",
    "НАСОСЫ": "Насосы",
    "РАСТВОРИТЕЛИ, огнебио, грунтовк": "Растворители, огнебио, грунтовки",
    "ПИСТОЛЕТЫ": "Пистолеты для пены",
    "ТАЧКИ": "Тачки",
    "КАТУШКИ": "Катушки для триммера",
    "МЕТИЗЫ": "Метизы",
    "ЛЕСКА": "Леска для триммера",
    "БИТЫ": "Биты",
    "БЕТОНОСМЕСИТЕЛИ": "Бетоносмесители MIKA",
    "МЕМБРАНЫ И ПЛЕНКИ": "Мембраны и плёнки",
    "МЫЛО И АВТОШАМПУНИ": "Автохимия и мойка",
    "СТАНКИ": "Станки",
    "РУЛЕТКИ НОЖИ ЛЕЗВИЯ": "Рулетки, ножи, лезвия",
    "ДИСКИ АЛМАЗНЫЕ И КРУГИ ОТРЕЗНЫЕ": "Алмазные диски MIKA",
    "ТЕПЛОНОСИТЕЛЬ": "Теплоноситель",
    "ЛОПАТЫ": "Лопаты",
    "ЭЛЕКТРОДЫ": "Электроды",
    "ШЛАНГИ": "Шланги",
}


def table_items(items, limit=None):
    rows = items if limit is None else items[:limit]
    tr = []
    for it in rows:
        art = it.get("art") or "—"
        name = it["name"]
        tr.append(f"<tr><td>{art}</td><td>{name}</td></tr>")
    more = ""
    if limit and len(items) > limit:
        more = f"<p class=\"muted\">В каталоге ещё {len(items) - limit} позиций — сверяйте артикул и наличие.</p>"
    return (
        '<div class="prose" style="overflow:auto"><table class="cmp"><thead><tr><th>Артикул</th><th>Наименование</th></tr></thead><tbody>'
        + "".join(tr)
        + "</tbody></table></div>"
        + more
    )


def assort_sections():
    # Skip foams and pumps — already detailed above on page
    order = [
        "БЕТОНОСМЕСИТЕЛИ",
        "МАСЛА",
        "РАСТВОРИТЕЛИ, огнебио, грунтовк",
        "ПИСТОЛЕТЫ",
        "ТАЧКИ",
        "КАТУШКИ",
        "ЛЕСКА",
        "МЕТИЗЫ",
        "БИТЫ",
        "МЕМБРАНЫ И ПЛЕНКИ",
        "ДИСКИ АЛМАЗНЫЕ И КРУГИ ОТРЕЗНЫЕ",
        "СТАНКИ",
        "РУЛЕТКИ НОЖИ ЛЕЗВИЯ",
        "МЫЛО И АВТОШАМПУНИ",
        "ТЕПЛОНОСИТЕЛЬ",
        "ЛОПАТЫ",
        "ЭЛЕКТРОДЫ",
        "ШЛАНГИ",
    ]
    blocks = []
    for key in order:
        items = [x for x in ASSORT.get(key, []) if "TORRA" not in x["name"].upper() or "MIKA" in x["name"].upper()]
        if key == "Пены":
            items = [x for x in items if "TORRA" not in x["name"].upper()]
        if not items:
            continue
        title = TITLES.get(key, key)
        sell = SELL.get(key, "Уточните задачу и сверьте артикул.")
        img = IMG.get(key, "assets/logos/mika.jpg")
        # large groups: show all but compact; metizy/leska/bits show all
        lim = None
        blocks.append(
            f"""
<section class="section assort-block">
  <h2>{title}</h2>
  <div class="split">
    <div class="prose">
      <p><strong>Как продавать:</strong> {sell}</p>
    </div>
    <div class="media-frame"><img src="{img}" alt="{title}" loading="lazy" /></div>
  </div>
  {table_items(items, lim)}
</section>"""
        )
    return "\n".join(blocks)


MIKA = shell(
    "Бренд MIKA",
    "mika",
    f"""
<header class="page-head">
  <p class="eyebrow">Своя марка · розница</p>
  <h1>MIKA</h1>
  <p class="lead">Главный собственный бренд. Если покупатель спрашивает «что у вас своё / посоветуйте нормальное недорого» — чаще начинайте с MIKA.</p>
</header>

<section class="section split">
  <div class="prose">
    <p><img src="assets/logos/mika.jpg" alt="Логотип MIKA" style="width:170px;background:#fff;padding:.55rem;border:1px solid var(--line);border-radius:.7rem" /></p>
    <p>По материалам сайта «У Михалыча»: марка относительно новая, но уже с хорошими отзывами. Баланс <strong>качество + доступная цена + широкий ассортимент</strong>.</p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что сказать покупателю</h3>
    <ul>
      <li>«Это наша собственная марка — без переплаты за громкое имя».</li>
      <li>«Можно собрать всё нужное в одной линейке».</li>
      <li>«Подходит и для дома/дачи, и для рабочих задач».</li>
    </ul>
  </div>
  <div class="gallery gallery-2">
    <figure><div class="img-box"><img src="assets/web/mika/foam_mika65.jpg" alt="Пена MIKA PRO 65" loading="lazy" /></div><figcaption>Пена проф. MIKA PRO 65</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/nasosy_1.jpg" alt="Насосы MIKA" loading="lazy" /></div><figcaption>Насосы MIKA</figcaption></figure>
  </div>
</section>

<section class="section">
  <h2>Монтажные пены</h2>
  <div class="gallery">
    <figure><div class="img-box"><img src="assets/web/mika/foam_mika65.jpg" alt="MIKA PRO 65" loading="lazy" /></div><figcaption>Проф. всесезонная MIKA PRO 65</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_site_glue.jpg" alt="Клей-пена" loading="lazy" /></div><figcaption>Клей-пена проф. MIKA</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_winter.jpg" alt="Зимняя пена" loading="lazy" /></div><figcaption>Зимняя пена MIKA 65</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_fire.jpg" alt="Огнестойкая MIKA B1" loading="lazy" /></div><figcaption>Огнестойкая MIKA B1</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/mika/foam_50.jpg" alt="MIKA 50" loading="lazy" /></div><figcaption>Бытовая MIKA 50</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/peny_2.jpg" alt="Сравнение выхода пены MIKA" loading="lazy" /></div><figcaption>Выход пены MIKA PRO 65</figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <p><strong>Как продавать:</strong> щели → бытовая; двери/окна → проф под пистолет; мороз → зимняя; огонь → огнестойкая B1; плиты/блоки → клей-пена. К проф-пене предложите пистолет и очиститель. Шпаргалка — на <a href="index.html">главной</a>.</p>
  </div>
</section>

<section class="section">
  <h2>Все насосы MIKA</h2>
  <p>Полный список из каталога. Уточняйте наличие и артикул на складе.</p>
  <div class="prose" style="overflow:auto">
    <table class="cmp">
      <thead><tr><th>Артикул</th><th>Наименование</th><th>Ключевое</th></tr></thead>
      <tbody>
        <tr><td>335110В</td><td>Вибрационный ВПН-10В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 10 м · напор 60–70 м</td></tr>
        <tr><td>335110Н</td><td>Вибрационный ВПН-10Н (нижний забор)</td><td>280 Вт · 18 л/мин · кабель 10 м · напор 60–70 м</td></tr>
        <tr><td>335115В</td><td>Вибрационный ВПН-15В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 15 м</td></tr>
        <tr><td>335115Н</td><td>Вибрационный ВПН-15Н (нижний забор)</td><td>280 Вт · 18 л/мин · кабель 15 м</td></tr>
        <tr><td>335125В</td><td>Вибрационный ВПН-25В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 25 м</td></tr>
        <tr><td>335125Н</td><td>Вибрационный ВПН-25Н (нижний забор)</td><td>280 Вт · 18 л/мин · кабель 25 м</td></tr>
        <tr><td>335140В</td><td>Вибрационный ВПН-40В (верхний забор)</td><td>280 Вт · 18 л/мин · кабель 40 м · выход ¾″</td></tr>
        <tr><td>33528D</td><td>Дренажный ДН-750 Вт (грязная вода)</td><td>750 Вт · 10 м³/ч · напор 10 м</td></tr>
        <tr><td>335275D</td><td>Дренажный НД-750</td><td>750 Вт · 13 000 л/ч · напор 7,5 м · частицы до 30 мм</td></tr>
        <tr><td>335324L</td><td>Насосная станция НС-750 · 24 л</td><td>750 Вт · напор 50 м · 3600 л/ч · бак 24 л</td></tr>
        <tr><td>3354370В</td><td>Скважинный винтовой СН-В 370 Вт</td><td>25 л/мин · напор 45 м · Ø 3,5″</td></tr>
        <tr><td>3354550В</td><td>Скважинный винтовой СН-В 550 Вт</td><td>30 л/мин · напор 90 м</td></tr>
        <tr><td>335430Ц</td><td>Скважинный центробежный СН-Ц 370 Вт</td><td>47 л/мин · напор 50 м · Ø 3″</td></tr>
        <tr><td>335450Ц</td><td>Скважинный центробежный СН-Ц 550 Вт</td><td>47 л/мин · напор 70 м · кабель 50 м</td></tr>
        <tr><td>335543П</td><td>Поверхностный ПН-800</td><td>800 Вт · напор 43 м · 5000 л/ч</td></tr>
      </tbody>
    </table>
  </div>
  <div class="gallery" style="margin-top:1rem">
    <figure><div class="img-box"><img src="assets/products/nasosy_1.jpg" alt="Насос MIKA" loading="lazy" /></div><figcaption>Вибрационные</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/nasosy_2.jpg" alt="Насос MIKA" loading="lazy" /></div><figcaption>Скважинные / станции</figcaption></figure>
    <figure><div class="img-box"><img src="assets/products/nasosy_3.jpg" alt="Насос MIKA" loading="lazy" /></div><figcaption>Поверхностные / дренаж</figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <p><strong>Как продавать:</strong> верхний забор — более чистая вода сверху; нижний — забрать почти до дна. Скважинный винтовой терпит больше примесей; центробежный — чище вода и выше производительность.</p>
  </div>
</section>

<section class="section">
  <h2>Угольные брикеты MIKA, 3 кг</h2>
  <p>Арт. 331113. Плотные брикеты — разжигать иначе, чем обычный уголь из пыли.</p>
  <div class="gallery gallery-1">
    <figure><div class="img-box"><img src="assets/web/mika/briquettes.jpg" alt="Угольные брикеты MIKA" loading="lazy" /></div><figcaption>Угольные брикеты MIKA, 3 кг</figcaption></figure>
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
  <h2>Весь остальной ассортимент MIKA</h2>
  <p>Ниже — позиции из каталога по группам и короткие подсказки, как предлагать в зале.</p>
</section>
{assort_sections()}

<div class="pager">
  <a class="btn btn-ghost" href="index.html" style="color:inherit;border-color:var(--line);background:#fff">← Главная</a>
  <a class="btn btn-ember" href="brand-torra.html">Далее: TORRA →</a>
</div>
""",
    "assets/logos/mika.jpg",
    "MIKA",
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
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_140.jpg" alt="TORRA 140L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 140L<br /><span class="art">арт. 84040CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_160.jpg" alt="TORRA 160L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 160L<br /><span class="art">арт. 84050CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_180.jpg" alt="TORRA 180L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 180L<br /><span class="art">арт. 84060CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_200.jpg" alt="TORRA 200L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 200L<br /><span class="art">арт. 84070CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_220.jpg" alt="TORRA 220L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 220L<br /><span class="art">арт. 84072CE</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/mixer_65.jpg" alt="TORRA 65L" loading="lazy" /></div><figcaption>Бетоносмеситель TORRA 65L<br /><span class="art">арт. 84009</span></figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <p>Также исполнения <strong>TORRA …L (AOER)</strong>: 140 / 160 / 180 / 200 / 220 / 240 л — уточняйте наличие.</p>
  </div>
</section>

<section class="section">
  <h2>Пена TORRA PRO 65</h2>
  <div class="gallery gallery-1">
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/foam_pro65.jpg" alt="TORRA PRO 65" loading="lazy" /></div><figcaption>Пена монтажная проф. TORRA PRO 65</figcaption></figure>
  </div>
  <div class="prose" style="margin-top:1rem">
    <p><strong>Как продавать:</strong> двери/окна под пистолет — предложите выбор между MIKA PRO 65 и TORRA PRO 65 по наличию и цене.</p>
  </div>
</section>

<section class="section">
  <h2>Отрезные круги Torra</h2>
  <div class="gallery">
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/disc_125_10.jpg" alt="Круг Torra 125×1,0" loading="lazy" /></div><figcaption>Круг 125×1,0×22,2 мм · металл / нерж.<br /><span class="art">арт. 338142125-10</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/disc_125_12.jpg" alt="Круг Torra 125×1,2" loading="lazy" /></div><figcaption>Круг 125×1,2×22,2 мм · металл / нерж.<br /><span class="art">арт. 338142125-12</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/disc_230_16.jpg" alt="Круг Torra 230×1,6" loading="lazy" /></div><figcaption>Круг 230×1,6×22,2 мм · металл / нерж.<br /><span class="art">арт. 338142230-16</span></figcaption></figure>
    <figure><div class="img-box img-box-lg"><img src="assets/web/torra/disc_230_20.jpg" alt="Круг Torra 230×2,0" loading="lazy" /></div><figcaption>Круг 230×2,0×22,2 мм · металл / нерж.<br /><span class="art">арт. 338142230-20</span></figcaption></figure>
  </div>
</section>

<section class="section">
  <h2>Как продавать рядом с MIKA</h2>
  <div class="prose">
    <ul>
      <li>Бетоносмеситель — уточните объём барабана, сравните MIKA и TORRA.</li>
      <li>Двери/окна — MIKA 65 проф или TORRA PRO 65.</li>
      <li>Резка металла — круги Torra; камень/бетон/плитка — алмазные диски MIKA.</li>
    </ul>
    <p>Каталог: <a href="https://gvozditut.ru/brands/torra/" target="_blank" rel="noopener">gvozditut.ru/brands/torra</a></p>
  </div>
</section>

<div class="pager">
  <a class="btn btn-ghost" href="brand-mika.html" style="color:inherit;border-color:var(--line);background:#fff">← MIKA</a>
  <a class="btn btn-ember" href="brand-inall.html">Далее: INALL →</a>
</div>
""",
    "assets/logos/torra.jpg",
    "TORRA",
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
    <p>Инструмент ориентирован на надёжную работу; перед продажей проходит проверку. По заявлениям бренда — уровень, сопоставимый с известными марками, за счёт тех же поставщиков комплектующих и контроля качества.</p>
    <h3 style="font-family:var(--display);font-size:1.05rem">Что в линейке</h3>
    <ul>
      <li>Дрели-шуруповёрты (разный вольтаж и момент)</li>
      <li>УШМ (болгарка) аккумуляторная</li>
      <li>Винтовёрт и гайковёрт ударные</li>
      <li>Аккумуляторы (в т.ч. аналоги популярных типоразмеров)</li>
    </ul>
  </div>
  <div class="gallery">
    <figure><div class="img-box"><img src="assets/web/inall/tool_0.jpg" alt="Шуруповёрт INALL" loading="lazy" /></div><figcaption>Шуруповёрт INALL 20V</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/inall/tool_4.jpg" alt="УШМ INALL" loading="lazy" /></div><figcaption>УШМ INALL 125 мм</figcaption></figure>
    <figure><div class="img-box"><img src="assets/web/inall/tool_3.jpg" alt="Гайковёрт INALL" loading="lazy" /></div><figcaption>Гайковёрт ударный INALL</figcaption></figure>
  </div>
</section>

<section class="section">
  <h2>Скрипт продавца</h2>
  <div class="prose">
    <ul>
      <li>Спросите задачу: мебель / стройка / авто / резка.</li>
      <li>Уточните момент (Н·м), напряжение, комплектацию (2 АКБ + ЗУ + кейс).</li>
      <li>Дополнительно предложите биты и расходники MIKA под инструмент.</li>
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
    "assets/logos/inall.jpg",
    "INALL",
)


def patch_other_pages():
    for name in ["index.html", "analogs.html", "test.html"]:
        p = ROOT / name
        t = p.read_text(encoding="utf-8")
        if 'rel="icon"' not in t:
            t = t.replace(
                '<link rel="stylesheet" href="site.css" />',
                FAV + '\n  <link rel="stylesheet" href="site.css" />',
            )
        t = t.replace("Апселл:", "Дополнительно:")
        t = t.replace("апселл", "дополнительно")
        t = t.replace("Апселл", "Дополнительно")
        p.write_text(t, encoding="utf-8")


def patch_css():
    css = (ROOT / "site.css").read_text(encoding="utf-8")
    # force white soft panels
    for theme in ["mika", "torra", "inall", "home", "analogs", "test"]:
        pass
    extra = """
/* WHITE_BG_ALL_2026 */
body, .site, .topnav, .prose, .page-head, .gallery figure,
.media-frame, .hero, .hero-visual, .topic-link, .logo-pill,
.img-box {
  background-color: #ffffff !important;
}
body.theme-mika, body.theme-torra, body.theme-inall,
body.theme-home, body.theme-analogs, body.theme-test {
  --brand-soft: #ffffff;
  background: #ffffff;
}
.gallery .img-box, .topic-link .img-box, .media-frame, .hero-visual {
  background: #ffffff !important;
}
.gallery-1 { grid-template-columns: minmax(220px, 420px); }
.muted { color: var(--muted); font-size: 0.9rem; }
.assort-block h2 { margin-bottom: 0.6rem; }
.page-head {
  border: 1px solid var(--line);
}
"""
    marker = "/* WHITE_BG_ALL_2026 */"
    if marker in css:
        css = css.split(marker)[0].rstrip() + "\n" + extra
    else:
        css = css.rstrip() + "\n" + extra
    (ROOT / "site.css").write_text(css, encoding="utf-8")


def main():
    (ROOT / "brand-mika.html").write_text(MIKA, encoding="utf-8")
    (ROOT / "brand-torra.html").write_text(TORRA, encoding="utf-8")
    (ROOT / "brand-inall.html").write_text(INALL, encoding="utf-8")
    patch_other_pages()
    patch_css()
    print("updated pages")
    print("mika size", (ROOT / "brand-mika.html").stat().st_size)


if __name__ == "__main__":
    main()
