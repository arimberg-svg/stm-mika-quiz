# -*- coding: utf-8 -*-
"""Rebuild brand-mika.html as tabbed catalog with sell tips on every product."""
from __future__ import annotations

import html as H
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


def sell_blurb(name: str, kind: str = "") -> str:
    """2–3 plain Russian sentences: for what, how to offer, how to sell."""
    n = name.lower()
    kind = kind or ""

    # --- foams ---
    if kind == "foam" or "пена" in n or "клей-пена" in n or "клей пена" in n:
        if "огнестой" in n or "b1" in n:
            return (
                "Огнестойкая пена нужна там, где важна пожарная безопасность: проёмы, коммуникации, зоны с риском огня. "
                "Предлагайте, если покупатель говорит про новостройку, котельную, щиток или «по нормам». "
                "Объясните: это профпод пистолет, не обычная бытовая — и дайте 15–20 минут на понимание задачи, не давите «любой баллон»."
            )
        if "клей" in n:
            return (
                "Клей-пена — чтобы клеить блоки, панели, утеплитель, а не просто заполнять щели. "
                "Спросите, что клеят и на какую площадь: так проще объяснить расход и почему это удобнее мешков раствора. "
                "Предложите вместе пистолет и очиститель, если человек берёт впервые."
            )
        if "зимн" in n:
            return (
                "Зимняя пена — для работ на морозе, когда обычная «не берётся». "
                "Уточните температуру на улице и задачу (окна, двери, щели). "
                "Говорите просто: «если холодно — берите зимнюю, иначе пена может не вспениться как надо»."
            )
        if "бытов" in n or "mika 50" in n or " 50 " in n:
            return (
                "Бытовая пена с трубочкой — для небольших щелей и разовых работ дома без пистолета. "
                "Предлагайте, если человек говорит «чуть запенить», «дырка», «подоконник». "
                "Если работы много или ставят двери/окна — мягко переведите на профессиональную под пистолет."
            )
        return (
            "Профессиональная пена под пистолет — для дверей, окон и серьёзного монтажа. "
            "Спросите задачу: межкомнатные или входные, окна, объём работ. "
            "Предложите пистолет и очиститель «в комплект», чтобы баллон было удобно использовать и не засорить клапан."
        )

    # --- oils ---
    if kind == "oil" or "масло" in n:
        if "2" in n and ("такт" in n or "2t" in n or "2х" in n or "2-х" in n):
            dose = " С дозатором удобнее отмерять порцию." if "дозатор" in n else ""
            return (
                "Масло для двухтактных двигателей: бензокосы, некоторые пилы и мототехника с 2T. "
                f"Спросите технику и смешивают ли бензин с маслом — 2T и 4T нельзя путать.{dose} "
                "Предложите нужную фасовку (100 мл или 1 л) под объём работ."
            )
        if "4" in n and ("такт" in n or "4t" in n or "4х" in n or "4-х" in n):
            return (
                "Масло для четырёхтактных двигателей — в картер, без смешивания с бензином. "
                "Уточните технику (генератор, мотоблок, газонокосилка 4T). "
                "Коротко: «если в инструкции 4T — берите это, двухтактное сюда не подойдёт»."
            )
        if "цеп" in n or "шин" in n:
            return (
                "Масло для смазки цепи и шины бензопилы. "
                "Предлагайте каждому, кто берёт пилу, цепь или говорит, что пила «сухая/дымит». "
                "Объясните: это не моторное масло — льётся в бачок смазки цепи."
            )
        if "компрессор" in n:
            return (
                "Масло для поршневого компрессора — в картер компрессора по уровню. "
                "Спросите модель и что написано в инструкции. "
                "Не предлагайте вместо моторного 2T/4T для садовой техники."
            )
        if "тад" in n or "трансмисс" in n:
            return (
                "Трансмиссионное ТАД-17 — для редукторов и узлов, где указано такое масло. "
                "Сверьте назначение по технике покупателя. "
                "Не путайте с моторным маслом для двигателя."
            )
        return (
            "Масло MIKA — под конкретный тип техники. "
            "Сначала спросите, куда льют: двигатель 2T/4T, цепь, компрессор или редуктор. "
            "Потом предложите нужную канистру и фасовку."
        )

    # --- pumps ---
    if kind == "pump" or "насос" in n or "впн" in n or "дренаж" in n or "скважин" in n or "станци" in n:
        if "верхн" in n:
            return (
                "Вибрационный насос с верхним забором берёт более чистую воду сверху колодца или бочки. "
                "Предлагайте, если вода относительно чистая и важно не хватать песок со дна. "
                "Уточните глубину и длину кабеля — берите с запасом по проводу."
            )
        if "нижн" in n:
            return (
                "Вибрационный насос с нижним забором забирает воду почти до дна. "
                "Удобно, когда нужно выкачать ёмкость по максимуму. "
                "Предупредите: если на дне много песка — лучше фильтр и аккуратная установка."
            )
        if "дренаж" in n or "нд-" in n or "дн-" in n:
            return (
                "Дренажный насос — для грязной воды, луж, подтоплений, откачки с частицами. "
                "Спросите, насколько грязная вода и какой напор/расход нужен. "
                "Объясните просто: «это не для питьевого колодца, а чтобы откачать грязь и воду с мусором»."
            )
        if "станци" in n:
            return (
                "Насосная станция с баком держит давление в домашнем водопроводе. "
                "Предлагайте, если нужен постоянный напор в доме/на даче из колодца или ёмкости. "
                "Уточните глубину всасывания и напор — и проверьте наличие на складе."
            )
        if "винтов" in n:
            return (
                "Скважинный винтовой насос лучше переносит воду с примесями, чем центробежный. "
                "Спросите глубину скважины, дебит и насколько «песчаная» вода. "
                "Подбирайте мощность и напор с запасом, не «впритык»."
            )
        if "центробеж" in n:
            return (
                "Скважинный центробежный — выше производительность на более чистой воде. "
                "Если вода мутная/с песком — честно скажите, что винтовой может подойти лучше. "
                "Сверьте диаметр скважины, кабель и напор."
            )
        if "поверхност" in n or "пн-" in n:
            return (
                "Поверхностный насос стоит рядом с источником и тянет воду с небольшой глубины. "
                "Подходит для полива, ёмкостей, неглубоких колодцев. "
                "Уточните глубину всасывания и нужный расход — не обещайте «со скважины 30 метров»."
            )
        return (
            "Насос MIKA подбирают под задачу: колодец, скважина, дренаж или дом. "
            "Спросите, откуда вода и насколько она чистая. "
            "Потом предложите модель по напору, кабелю и типу забора."
        )

    # --- mixers ---
    if kind == "mixer" or "бетоносмес" in n:
        m = re.search(r"(\d{2,3})\s*л", n)
        vol = m.group(1) + " л" if m else "нужный объём"
        return (
            f"Бетоносмеситель {vol} — чтобы мешать бетон и раствор без лопаты «на глазок». "
            "Спросите объём работ: дорожка, фундамент, стяжка. "
            "Предложите сравнить с TORRA по цене и наличию, если покупатель выбирает."
        )

    # --- solvents ---
    if kind.startswith("solv") or any(
        x in n
        for x in [
            "уайт",
            "растворител",
            "ацетон",
            "сольвент",
            "керосин",
            "обезжир",
            "огнебио",
            "грунтов",
        ]
    ):
        if "огнебио" in n:
            return (
                "Огнебиозащита для древесины — снижает риск возгорания и защищает от плесени/жука. "
                "Предлагайте на бани, стропила, чердаки, каркас. "
                "Скажите про расход и что важно нанести по инструкции, а не «чуть сбрызнуть»."
            )
        if "грунтов" in n:
            return (
                "Грунтовка глубокого проникновения готовит поверхность под покраску или отделку. "
                "Предлагайте, если стены пылят, впитывают или «краска не ляжет». "
                "Сверьте объём 5 или 10 л под площадь."
            )
        if "обезжир" in n:
            return (
                "Обезжириватель нужен перед покраской, склейкой и антикором. "
                "Спросите, что обезжиривают: металл, пластик, детали авто. "
                "Коротко: «сначала обезжирить — потом краска/клей держатся лучше»."
            )
        if "646" in n:
            return (
                "Растворитель 646 — для разбавления эмалей и промывки инструмента после ЛКМ. "
                "Уточните, какую краску/эмаль используют. "
                "Предложите фасовку под объём и напомните про проветривание."
            )
        if "650" in n:
            return (
                "Растворитель 650 чаще берут под определённые эмали и ремонтные работы. "
                "Сверьте с тем, что написано на банке краски покупателя. "
                "Не подменяйте «любым растворителем» без уточнения."
            )
        if "ацетон" in n:
            return (
                "Ацетон сильно обезжиривает и растворяет многие загрязнения. "
                "Предлагайте для очистки, снятия остатков клея/краски (где допустимо). "
                "Предупредите: резкий запах, нужна вентиляция и осторожность с пластиком."
            )
        if "уайт" in n:
            return (
                "Уайт-спирит — для разбавления масляных составов и очистки кистей/поверхностей. "
                "Частый запрос «чем развести» и «чем отмыть». "
                "Подберите литраж: от 0,5 л для дома до канистры для объекта."
            )
        if "керосин" in n:
            return (
                "Керосин ТС-1 — для технических нужд: очистка, некоторые горелки и хозработы. "
                "Уточните назначение, не предлагайте «как топливо куда угодно». "
                "Сверьте фасовку 1 или 5 л."
            )
        if "сольвент" in n:
            return (
                "Сольвент — растворитель для ЛКМ и очистки. "
                "Спросите, под какую работу и какую краску. "
                "Предложите вместе перчатки и напомните про запах/проветривание."
            )
        return (
            "Это подготовка поверхности или растворитель под задачу с краской/очисткой. "
            "Сначала спросите, что делают: разводят, моют или защищают дерево. "
            "Потом дайте нужный состав и удобную фасовку."
        )

    # --- wheelbarrows ---
    if kind == "wheel" or "тачк" in n:
        return (
            "Тачка — возить сыпучее, раствор, мусор по участку и стройке. "
            "Спросите: сад или стройка, какой объём кузова нужен, какое колесо удобнее. "
            "Предложите модель по наличию и не обещайте «потянет тонну», если человек берёт лёгкую садовую."
        )

    # --- reels / line ---
    if kind == "reel" or "катушк" in n:
        return (
            "Катушка (головка) для триммера — куда заправляется леска. "
            "Сверьте посадку/резьбу с его триммером, иначе «не встанет». "
            "Сразу предложите леску нужного диаметра «в запас»."
        )
    if kind == "line" or "леска" in n:
        diam = re.search(r"(\d+[.,]\d+)\s*\*?\s*\d*\s*м?", n)
        profile = "нужного профиля"
        for p, label in [
            ("круг", "круглого сечения"),
            ("квадрат", "квадратного сечения"),
            ("звезд", "сечения «звезда»"),
            ("семиуг", "семиугольного сечения"),
            ("кручен", "кручёного профиля"),
        ]:
            if p in n:
                profile = label
                break
        dtxt = diam.group(1).replace(",", ".") + " мм" if diam else "нужного диаметра"
        return (
            f"Леска {dtxt}, {profile} — расходник для триммера. "
            "Спросите диаметр, который стоял раньше, и мощность косы: толще — для жёсткой травы, но тяжелее двигателю. "
            "Предложите моток с запасом, чтобы не бегать за леской в сезон."
        )

    # --- fasteners ---
    if kind == "metiz" or "саморез" in n or "метиз" in n:
        size = re.search(r"(\d+[.,]?\d*)\s*\*\s*(\d+)", n)
        size_txt = f"{size.group(1)}×{size.group(2)} мм" if size else "нужного размера"
        pack = "В фасовке по килограмму/упаковке — удобно для объёма работ." if ("кг" in n or "уп" in n) else "Сверьте фасовку под объём."
        return (
            f"Саморезы MIKA {size_txt} — крепёж под дерево/монтаж (смотрите тип головки и шаг). "
            f"Спросите, во что крутят и какой длины нужен выход. {pack} "
            "Предлагайте сразу биту PH/PZ под шляпку, чтобы не сорвать шлиц."
        )

    # --- bits ---
    if kind == "bit" or "бита" in n or "бит " in n or "головка магнит" in n or "адаптер" in n or "набор бит" in n:
        if "набор" in n:
            return (
                "Набор бит — чтобы дома/в бригаде был базовый комплект под разные шлицы. "
                "Предлагайте, если человек собирает первый набор к шуруповёрту. "
                "Коротко покажите, что внутри, и предложите отдельно самые ходовые PH2/PZ2 «на износ»."
            )
        if "головка" in n:
            return (
                "Магнитная головка держит болт/саморез с шестигранной головкой. "
                "Спросите размер под ключ (8, 10, 13, 17). "
                "Удобно предлагать к шуруповёрту для кровли, заборов, сборки на шестиграннике."
            )
        if "адаптер" in n:
            return (
                "Адаптеры под торцевые головки — чтобы шуруповёртом крутить головки 1/4, 3/8, 1/2. "
                "Предлагайте, если есть набор головок или работа с крепежом авто/механики. "
                "Уточните нужный хвостовик."
            )
        if "красн" in n or "торсион" in n:
            return (
                "Торсионная бита пружинит при ударе и реже ломается на плотных саморезах. "
                "Предлагайте к ударным шуруповёртам и жёсткому крепежу. "
                "Сверьте шлиц PH/PZ и длину."
            )
        if "магнитн" in n and "огранич" in n:
            return (
                "Бита с магнитным ограничителем помогает не утопить саморез слишком глубоко. "
                "Отлично для гипсокартона и чистовой отделки. "
                "Предложите, если покупатель жалуется, что «шляпку продирает»."
            )
        if "двухсторон" in n or "коричне" in n or "черн" in n:
            return (
                "Двухсторонняя бита — два рабочих конца, удобно носить с собой. "
                "Спросите шлиц и нужен ли торсион. "
                "Для ежедневного монтажа это простой и понятный расходник."
            )
        return (
            "Бита под конкретный шлиц (PH или PZ) и длину. "
            "Спросите, какой саморез и какой инструмент — ударный или обычный. "
            "Не путайте PH и PZ: из-за этого срывает шлицы."
        )

    # --- membranes ---
    if kind == "membrane" or "мембран" in n or "пленк" in n or "плёнк" in n:
        return (
            "Мембрана/плёнка защищает конструкцию от влаги или пара — зависит от типа. "
            "Спросите узел: кровля, каркас, пол, какой «пирог». "
            "Важно не перепутать стороны укладки — покажите по маркировке на рулоне."
        )

    # --- diamond discs ---
    if kind == "disc" or "диск" in n or "алмаз" in n:
        if "segment" in n or "сегмент" in n and "turbo" not in n and "alligator" not in n:
            return (
                "Сегментный алмазный диск — для бетона, кирпича, плитки тротуарной. "
                "Предлагайте на резку камня/бетона болгаркой. "
                "Для металла скажите честно: нужен отрезной круг TORRA, не алмаз."
            )
        if "сплошн" in n or "blade" in n or "супертонк" in n:
            return (
                "Сплошной/супертонкий диск — аккуратный рез керамики и керамогранита. "
                "Спросите материал плитки и сухой или мокрый рез. "
                "Для бетона грубее лучше сегмент/турбо."
            )
        if "ceramic" in n or "керами" in n:
            return (
                "Диск Ceramic — под плитку, керамогранит и камень. "
                "Уточните, что режут и какой диаметр под УШМ. "
                "Предложите диск «в пару» к новой болгарке или если старый стерся."
            )
        if "turbo" in n or "турбо" in n:
            return (
                "Турбо-диск универсальнее режет бетон, кирпич, камень. "
                "Хороший выбор, если задач несколько и нужен «один диск на объект». "
                "Сверьте диаметр 125/230 под инструмент."
            )
        if "alligator" in n or "armir" in n or "армир" in n:
            return (
                "Alligator — под армированный бетон и тяжёлые материалы. "
                "Предлагайте, когда обычный сегмент «не берёт» или много арматуры. "
                "Уточните диаметр и режим сухой/мокрый."
            )
        if "grizzly" in n:
            return (
                "Grizzly — турбосегмент для гранита и железобетона. "
                "Для тяжёлого реза на объекте. "
                "Спросите материал и диаметр диска."
            )
        if "longlife" in n or "мульти" in n:
            return (
                "Мультифункциональный Longlife — когда нужно резать разное, включая металл/камень/дерево по задаче диска. "
                "Уточните, что именно режут чаще всего. "
                "Если только металл пачками — лучше отдельные круги TORRA."
            )
        return (
            "Алмазный диск MIKA подбирают под материал: бетон, плитка, гранит. "
            "Спросите, чем режут и какой диаметр нужен. "
            "Металл и нержавейку обычно ведём на круги TORRA."
        )

    # --- bench grinders ---
    if kind == "bench" or "станок" in n or "точильн" in n:
        if "ленточ" in n or "дисково" in n:
            return (
                "Дисково-ленточный станок — и круг, и лента для заточки/шлифовки. "
                "Предлагайте, если нужен универсальный настольный помощник в мастерской. "
                "Покажите отличие от обычного точила с двумя кругами."
            )
        lamp = " С лампой удобнее контролировать зону заточки." if "ламп" in n else ""
        return (
            f"Точильный станок MIKA — заточка инструмента дома и в мастерской.{lamp} "
            "Спросите, что точат и какой диаметр круга нужен. "
            "Напомните про очки и аккуратную подачу заготовки."
        )

    # --- tape / knives ---
    if kind == "tape" or "рулетк" in n or "нож" in n or "лезви" in n:
        if "лезви" in n:
            return (
                "Сменные лезвия — расходник к ножу того же размера (18 или 25 мм). "
                "Предлагайте сразу к ножу или если жалуются, что «тупой/ломается». "
                "Сверьте ширину лезвия один в один."
            )
        if "нож" in n:
            return (
                "Нож с сегментированным лезвием — для гипсокартона, плёнки, упаковки, обоев. "
                "Спросите толщину работ: 18 мм или более мощный 25 мм. "
                "Предложите запасные лезвия в той же ширине."
            )
        length = re.search(r"(\d)\s*м", n)
        ltxt = length.group(1) + " м" if length else "нужной длины"
        return (
            f"Рулетка {ltxt} — замеры на объекте и дома. "
            "Магнитный зацеп удобен на металле. "
            "Спросите, какая длина нужна чаще: 3, 5 или 8 метров."
        )

    # --- auto chemistry ---
    if kind == "auto" or "мыло" in n or "шампунь" in n or "мойк" in n or "effect" in n or "standart" in n or "prof" in n:
        if "effect" in n:
            return (
                "Бесконтактная химия EFFECT — для мойки кузова без жёсткого контакта. "
                "Спросите, домашний объём или чаще моет. "
                "Предложите 1 кг попробовать или 5 кг, если моет регулярно."
            )
        if "prof" in n:
            return (
                "Линейка Prof — более «рабочий» вариант для частой/интенсивной мойки. "
                "Уточните, чем моют сейчас и какой эффект ждут. "
                "Объясните разницу фасовок 1 и 5 кг по цене за литр."
            )
        if "standart" in n:
            return (
                "STANDART — базовый вариант бесконтактной мойки. "
                "Хорош как понятный старт без переплаты. "
                "Спросите объём и предложите удобную фасовку."
            )
        return (
            "Жидкое мыло/автохимия MIKA — для рук или мойки авто (смотрите название). "
            "Уточните задачу: руки в гараже или бесконтактная мойка машины. "
            "Подберите объём канистры под расход."
        )

    # --- shovel ---
    if kind == "shovel" or "лопат" in n:
        return (
            "Снеговая морозоустойчивая лопата — убирать снег зимой, пластик не обязан «дубеть» на морозе. "
            "Предлагайте сезонно и тем, кто обновляет старую треснувшую. "
            "Уточните комплектацию черенка/рукояти по факту на складе."
        )

    # --- electrodes ---
    if kind == "electrode" or "электрод" in n:
        pack = "5,5 кг" if "5" in n else "1 кг"
        return (
            f"Электроды MIKA-46 фасовкой {pack} — для ручной дуговой сварки. "
            "Спросите диаметр электродов и какой аппарат/ток. "
            "Маленькая пачка — попробовать/добить работу; большая — если варят часто."
        )

    # --- hose ---
    if kind == "hose" or "шланг" in n:
        return (
            "Поливочный армированный шланг 3/4″ на 25 м — полив огорода и участка. "
            "Морозостойкий и многослойный: меньше перегибов и дольше служит. "
            "Предложите сразу соединители/пистолет полива, если их нет."
        )

    # --- briquettes ---
    if kind == "briq" or "брикет" in n or "уголь" in n:
        return (
            "Плотные угольные брикеты — для мангала, дают ровный жар, но разжигаются дольше обычного угля. "
            "Объясните: 15–20 минут, без жидкости и без «раздуть сразу». "
            "Предложите стартер или спиртовые тюбики, если человек торопится."
        )

    return (
        f"«{name}» — позиция своей марки MIKA под задачу покупателя. "
        "Спросите, для чего берут, и предложите эту позицию как понятный вариант по цене. "
        "Перед обещанием сверьте артикул и наличие на складе."
    )


def cards(rows, kind: str = "", show_art: bool = True):
    parts = ['<div class="prod-grid">']
    for it in rows:
        art = (it.get("art") or "").strip()
        name = it["name"]
        if art.lower().startswith("руб") or art == "None":
            art = ""
        tip = it.get("sell") or sell_blurb(name, kind)
        art_html = f'<span class="art">арт. {H.escape(art)}</span>' if show_art and art else ""
        parts.append(
            "<article class=\"prod-card\">"
            f"<strong>{H.escape(name)}</strong>"
            f"{art_html}"
            f"<p class=\"how\">{H.escape(tip)}</p>"
            "</article>"
        )
    parts.append("</div>")
    return "\n".join(parts)


def metizy_mika():
    rows = []
    for it in ASSORT.get("МЕТИЗЫ", []):
        if "MIKA" not in it["name"].upper():
            continue
        art = it.get("art") or ""
        if art.lower().startswith("руб"):
            art = ""
        rows.append({"art": art, "name": it["name"]})
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


PUMPS = [
    ("Вибрационный ВПН-10В (верхний забор)", "335110В", "pump"),
    ("Вибрационный ВПН-10Н (нижний забор)", "335110Н", "pump"),
    ("Вибрационный ВПН-15В (верхний забор)", "335115В", "pump"),
    ("Вибрационный ВПН-15Н (нижний забор)", "335115Н", "pump"),
    ("Вибрационный ВПН-25В (верхний забор)", "335125В", "pump"),
    ("Вибрационный ВПН-25Н (нижний забор)", "335125Н", "pump"),
    ("Вибрационный ВПН-40В (верхний забор)", "335140В", "pump"),
    ("Дренажный ДН-750 (грязная вода)", "33528D", "pump"),
    ("Дренажный НД-750", "335275D", "pump"),
    ("Насосная станция НС-750 · 24 л", "335324L", "pump"),
    ("Скважинный винтовой СН-В 370 Вт", "3354370В", "pump"),
    ("Скважинный винтовой СН-В 550 Вт", "3354550В", "pump"),
    ("Скважинный центробежный СН-Ц 370 Вт", "335430Ц", "pump"),
    ("Скважинный центробежный СН-Ц 550 Вт", "335450Ц", "pump"),
    ("Поверхностный ПН-800", "335543П", "pump"),
]
PUMPS_HTML = cards([{"name": n, "art": a} for n, a, _ in PUMPS], kind="pump")

solv = solvent_groups()
solv_html = []
for title, rows in solv.items():
    if not rows:
        continue
    solv_html.append(f'<h3 class="subhead">{title}</h3>{cards(rows, kind="solv")}')

bits_guide = """
<div class="prose bits-guide">
  <h3 style="margin-top:0;font-family:var(--display);font-size:1.05rem">Как подбирать биты MIKA</h3>
  <ol>
    <li><strong>Шлиц</strong> — PH (крестовой Philips), PZ (Pozidriv). PH2 / PZ2 — самые ходовые.</li>
    <li><strong>Длина</strong> — 50 мм обычно; 70–90 мм — если нужен вылет.</li>
    <li><strong>Под инструмент</strong> — для удара лучше торсионные.</li>
  </ol>
  <h3 style="font-family:var(--display);font-size:1.05rem">Цвет / тип — для чего</h3>
  <ul>
    <li><strong>Красные торсионные</strong> — удар, плотные саморезы.</li>
    <li><strong>Коричневые двухсторонние</strong> — повседневный монтаж.</li>
    <li><strong>Чёрные двухсторонние торсионные</strong> — два конца + запас прочности.</li>
    <li><strong>С магнитным ограничителем</strong> — гипсокартон, контроль глубины.</li>
    <li><strong>Магнитные головки</strong> — шестигранный крепёж.</li>
    <li><strong>Наборы</strong> — стартовый комплект к шуруповёрту.</li>
  </ul>
</div>
"""

tabs = [
    (
        "about",
        "О бренде",
        """
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
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/foam_mika65.jpg" alt="MIKA PRO 65" loading="lazy" /></div><figcaption>Проф. MIKA PRO 65</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_site_glue.jpg" alt="Клей-пена" loading="lazy" /></div><figcaption>Клей-пена</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_winter.jpg" alt="Зимняя" loading="lazy" /></div><figcaption>Зимняя</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_fire.jpg" alt="Огнестойкая" loading="lazy" /></div><figcaption>Огнестойкая B1</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/foam_50.jpg" alt="MIKA 50" loading="lazy" /></div><figcaption>Бытовая MIKA 50</figcaption></figure>
  <figure><div class="img-box"><img src="assets/products/peny_2.jpg" alt="Выход пены" loading="lazy" /></div><figcaption>Выход пены PRO 65</figcaption></figure>
</div>
{cards([x for x in items('Пены') if 'TORRA' not in x['name'].upper()], kind='foam')}
""",
    ),
    (
        "pumps",
        "Насосы",
        f"""
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
<div class="gallery gallery-1">
  <figure><div class="img-box"><img src="assets/web/mika/briquettes.jpg" alt="Брикеты" loading="lazy" /></div><figcaption>Угольные брикеты MIKA, 3 кг</figcaption></figure>
</div>
"""
        + cards([{"art": "331113", "name": "Угольные брикеты MIKA, 3 кг"}], kind="briq")
        + """
<div class="prose" style="margin-top:1rem">
  <h3 style="margin-top:0;font-family:var(--display);font-size:1.05rem">Как разжигать</h3>
  <p><strong>Стартером:</strong> брикеты сверху, снизу 1–2 спиртовых тюбика, 15–20 минут.</p>
  <p><strong>«Домиком»:</strong> колодец из брикетов, внутрь щепа/лучина или тюбики на дно. Не лить жидкость и не раздувать сразу.</p>
</div>
""",
    ),
    (
        "mixers",
        "Бетоносмесители",
        f"""
<div class="media-frame"><img src="assets/web/mika/mixer.jpg" alt="Бетоносмеситель MIKA" loading="lazy" /></div>
{cards(items('БЕТОНОСМЕСИТЕЛИ'), kind='mixer')}
""",
    ),
    (
        "oils",
        "Масла",
        f"""
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/oil_1.jpg" alt="Масло MIKA" loading="lazy" /></div><figcaption>Масла MIKA</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/oil_2.jpg" alt="Масло MIKA" loading="lazy" /></div><figcaption>2T / 4T</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/oil_3.jpg" alt="Масло MIKA" loading="lazy" /></div><figcaption>Цепь / спецмасла</figcaption></figure>
</div>
{cards(items('МАСЛА'), kind='oil')}
""",
    ),
    (
        "solvents",
        "Растворители и подготовка",
        f"""
<div class="media-frame"><img src="assets/web/mika/solvents.jpg" alt="Растворители MIKA" loading="lazy" /></div>
{''.join(solv_html)}
""",
    ),
    (
        "wheel",
        "Тачки",
        f"""
<div class="media-frame"><img src="assets/web/mika/wheelbarrow.jpg" alt="Тачка MIKA" loading="lazy" /></div>
{cards(items('ТАЧКИ'), kind='wheel')}
""",
    ),
    (
        "reels",
        "Катушки",
        f"""
<div class="media-frame"><img src="assets/web/mika/reels.jpg" alt="Катушка MIKA" loading="lazy" /></div>
{cards(items('КАТУШКИ'), kind='reel')}
""",
    ),
    (
        "line",
        "Леска",
        f"""
<div class="media-frame"><img src="assets/web/mika/line.jpg" alt="Леска MIKA" loading="lazy" /></div>
{cards(items('ЛЕСКА'), kind='line')}
""",
    ),
    (
        "metizy",
        "Метизы MIKA",
        f"""
{cards(metizy_mika(), kind='metiz')}
""",
    ),
    (
        "bits",
        "Биты",
        f"""
{bits_guide}
<div class="media-frame"><img src="assets/web/mika/bits.jpg" alt="Биты MIKA" loading="lazy" /></div>
{cards(items('БИТЫ'), kind='bit')}
""",
    ),
    (
        "membrane",
        "Мембраны и плёнки",
        f"""
<div class="media-frame"><img src="assets/web/mika/membrane.jpg" alt="Мембрана MIKA" loading="lazy" /></div>
{cards(items('МЕМБРАНЫ И ПЛЕНКИ'), kind='membrane')}
""",
    ),
    (
        "discs",
        "Алмазные диски",
        f"""
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/disc_diamond.jpg" alt="Диск MIKA" loading="lazy" /></div><figcaption>Алмазные диски MIKA</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/disc_mika_0.jpg" alt="Segment" loading="lazy" /></div><figcaption>Segment / бетон</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/disc_mika_2.jpg" alt="Turbo" loading="lazy" /></div><figcaption>Turbo / универсальный</figcaption></figure>
</div>
{cards(items('ДИСКИ АЛМАЗНЫЕ И КРУГИ ОТРЕЗНЫЕ'), kind='disc')}
""",
    ),
    (
        "bench",
        "Станки",
        f"""
<div class="media-frame"><img src="assets/web/mika/bench.jpg" alt="Станок MIKA" loading="lazy" /></div>
{cards(items('СТАНКИ'), kind='bench')}
""",
    ),
    (
        "tape",
        "Рулетки и ножи",
        f"""
<div class="media-frame"><img src="assets/web/mika/tape_knife.jpg" alt="Рулетка MIKA" loading="lazy" /></div>
{cards(items('РУЛЕТКИ НОЖИ ЛЕЗВИЯ'), kind='tape')}
""",
    ),
    (
        "auto",
        "Автохимия",
        f"""
<div class="gallery">
  <figure><div class="img-box"><img src="assets/web/mika/auto_1.jpg" alt="Автошампунь" loading="lazy" /></div><figcaption>Автошампунь MIKA</figcaption></figure>
  <figure><div class="img-box"><img src="assets/web/mika/auto_2.jpg" alt="Автохимия" loading="lazy" /></div><figcaption>Линейки мойки</figcaption></figure>
</div>
{cards(items('МЫЛО И АВТОШАМПУНИ'), kind='auto')}
""",
    ),
    (
        "shovel",
        "Лопаты",
        f"""
<div class="media-frame"><img src="assets/web/mika/shovel.jpg" alt="Лопата MIKA" loading="lazy" /></div>
{cards(items('ЛОПАТЫ'), kind='shovel')}
""",
    ),
    (
        "electrodes",
        "Электроды",
        f"""
<div class="media-frame"><img src="assets/web/mika/electrodes.jpg" alt="Электроды MIKA" loading="lazy" /></div>
{cards(items('ЭЛЕКТРОДЫ'), kind='electrode')}
""",
    ),
    (
        "hose",
        "Шланги",
        f"""
<div class="media-frame"><img src="assets/web/mika/hose.jpg" alt="Шланг MIKA" loading="lazy" /></div>
{cards(items('ШЛАНГИ'), kind='hose')}
""",
    ),
]

tab_btns = []
tab_panels = []
for i, (tid, label, body) in enumerate(tabs):
    active = " is-active" if i == 0 else ""
    tab_btns.append(
        f'<button type="button" class="tab-btn{active}" role="tab" aria-selected="{"true" if i==0 else "false"}" data-tab="{tid}">{label}</button>'
    )
    hidden = "" if i == 0 else " hidden"
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
  <p class="lead">Откройте вкладку товара. У каждой позиции — коротко: для чего, как предложить и как продать.</p>
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
# sanity: every prod-card has .how
assert html.count("prod-card") == html.count('class="how"')
print("ok cards", html.count("prod-card"), "bytes", len(html))
