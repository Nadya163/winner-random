#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_pages.py — генератор страниц сайта «Winner Random».

Запуск: python generate_pages.py

Генерирует 6 HTML-страниц + sitemap.xml + robots.txt.
Перед деплоем: вставьте код Яндекс.Метрики вместо <!-- YANDEX_METRIKA -->.
"""

import os, json

BASE_URL   = "https://winner-random.ru"
SITE_NAME  = "Winner Random"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    {
        "slug": "index", "filename": "index.html", "nav_label": "Рандомайзер",
        "title": "Рандомайзер победителя — выбрать победителя розыгрыша онлайн",
        "description": "Бесплатный онлайн-рандомайзер для розыгрышей и конкурсов. Вставьте список участников — сервис выберет случайного победителя. Без регистрации.",
        "h1": "Рандомайзер победителя розыгрыша",
        "lead": "Вставьте список участников — по одному на строке — и нажмите кнопку. Сервис случайно выберет победителя за секунду. Без регистрации, без рекламы результата.",
        "article": """<h2>Как провести честный розыгрыш онлайн</h2>
<p>Вставьте имена или никнеймы участников в поле — каждый с новой строки. Нажмите «Выбрать победителя». Сервис использует криптографически случайный алгоритм перемешивания — результат нельзя предсказать или подтасовать.</p>
<h2>Можно ли выбрать нескольких победителей</h2>
<p>Да — укажите количество победителей в поле «Количество победителей». Сервис выберет нужное число участников без повторений.</p>
<h2>Нужна ли регистрация</h2>
<p>Нет. Всё работает прямо в браузере, данные участников никуда не отправляются и не сохраняются.</p>""",
    },
    {
        "slug": "randomaizer-vk", "filename": "randomaizer-vk.html", "nav_label": "ВКонтакте",
        "title": "Рандомайзер для конкурса ВКонтакте — выбрать победителя в ВК",
        "description": "Выберите победителя конкурса или розыгрыша ВКонтакте. Скопируйте список участников и нажмите кнопку — рандомайзер выберет победителя честно и случайно.",
        "h1": "Рандомайзер для конкурса ВКонтакте",
        "lead": "Скопируйте комментарии или список участников из поста ВКонтакте, вставьте сюда — по одному на строке — и нажмите «Выбрать победителя».",
        "article": """<h2>Как провести розыгрыш в ВКонтакте</h2>
<p>Соберите список участников из комментариев под постом. Скопируйте имена, вставьте в поле выше каждый с новой строки и запустите рандомайзер. Результат можно сделать скриншот и опубликовать в ВК как доказательство честного розыгрыша.</p>
<h2>Сколько участников можно добавить</h2>
<p>Ограничений нет — рандомайзер работает с любым количеством имён.</p>""",
    },
    {
        "slug": "randomaizer-konkurs", "filename": "randomaizer-konkurs.html", "nav_label": "Конкурс",
        "title": "Рандомайзер для конкурса — выбрать случайного победителя онлайн",
        "description": "Онлайн-рандомайзер для конкурсов и гивэев. Вставьте участников списком и выберите одного или нескольких победителей случайно и честно.",
        "h1": "Рандомайзер для конкурса — случайный выбор победителя",
        "lead": "Проведите честный конкурс: вставьте список участников, укажите сколько победителей нужно выбрать, и нажмите кнопку.",
        "article": """<h2>Почему важно использовать рандомайзер для конкурса</h2>
<p>Случайный выбор победителя через рандомайзер — это прозрачно и честно. Подписчики доверяют результату больше, когда видят, что выбор был автоматическим, а не ручным.</p>
<h2>Как оформить результат конкурса</h2>
<p>Сделайте скриншот экрана с именем победителя и опубликуйте его вместе с объявлением результатов. Это повышает доверие аудитории к вашим будущим конкурсам.</p>""",
    },
    {
        "slug": "sluchain-vybor-cheloveka", "filename": "sluchain-vybor-cheloveka.html", "nav_label": "Случайный выбор",
        "title": "Случайный выбор человека из списка онлайн — рандомайзер имён",
        "description": "Выберите случайного человека из любого списка онлайн. Введите имена, нажмите кнопку — рандомайзер выберет одно случайное имя из списка.",
        "h1": "Случайный выбор человека из списка",
        "lead": "Нужно случайно выбрать человека из группы, команды или списка участников? Вставьте имена и нажмите кнопку — выбор займёт секунду.",
        "article": """<h2>Где пригодится случайный выбор человека</h2>
<p>Случайный выбор из списка нужен не только в розыгрышах. Его используют учителя для выбора отвечающего, менеджеры для распределения задач, организаторы мероприятий для формирования команд.</p>
<h2>Как работает алгоритм</h2>
<p>Рандомайзер использует алгоритм Фишера-Йейтса для перемешивания списка. Каждый запуск даёт независимый случайный результат.</p>""",
    },
    {
        "slug": "giveaway-randomaizer", "filename": "giveaway-randomaizer.html", "nav_label": "Giveaway",
        "title": "Рандомайзер для гивэея — выбрать победителя гивэей онлайн бесплатно",
        "description": "Бесплатный рандомайзер для гивэея. Вставьте список участников и выберите победителя честно и случайно. Без регистрации, без установки приложений.",
        "h1": "Рандомайзер для гивэея — выбрать победителя",
        "lead": "Проведите гивэей честно: вставьте список участников и нажмите кнопку. Рандомайзер выберет победителя случайно — без регистрации и без приложений.",
        "article": """<h2>Как провести гивэей честно</h2>
<p>Соберите список всех участников гивэея, вставьте их имена в поле выше. Нажмите «Выбрать победителя» и сделайте скриншот результата для публикации.</p>
<h2>Можно ли доверять результату</h2>
<p>Да. Рандомайзер работает полностью в вашем браузере — никакого сервера, который мог бы влиять на результат. Алгоритм использует встроенный генератор случайных чисел браузера.</p>""",
    },
    {
        "slug": "rozygrysh-pobediteley", "filename": "rozygrysh-pobediteley.html", "nav_label": "Розыгрыш",
        "title": "Розыгрыш победителей онлайн — рандомайзер для розыгрыша призов",
        "description": "Проведите розыгрыш призов онлайн. Вставьте список участников и выберите одного или нескольких победителей случайным образом. Бесплатно.",
        "h1": "Розыгрыш победителей онлайн",
        "lead": "Вставьте список участников розыгрыша и выберите сколько победителей нужно. Рандомайзер выберет их честно и случайно — результат можно сразу опубликовать.",
        "article": """<h2>Как провести розыгрыш призов</h2>
<p>Соберите полный список участников розыгрыша. Укажите количество призовых мест. Нажмите кнопку — рандомайзер выберет победителей без повторений и выдаст пронумерованный список мест.</p>
<h2>Несколько призов и мест</h2>
<p>Если у вас несколько призов — укажите количество победителей, равное числу призов. Первый в списке получает главный приз, второй — второе место и так далее.</p>""",
    },
]

TOOL_HTML = """\
    <div class="tool-card">
      <div class="field">
        <label for="participants">Список участников <span>— каждый с новой строки</span></label>
        <textarea id="participants" placeholder="Иван Иванов&#10;Мария Петрова&#10;Алексей Сидоров&#10;..."></textarea>
      </div>
      <p class="counter">Участников: <span id="participantCount">0</span></p>
      <div class="options-row">
        <label>Победителей:
          <input type="number" id="winnerCount" value="1" min="1" max="100">
        </label>
        <label>
          <input type="checkbox" id="removeWinner">
          Удалить победителя из списка
        </label>
      </div>
      <button class="btn-draw" id="btnDraw">🎲 Выбрать победителя</button>

      <div class="result-wrap" id="resultWrap">
        <div class="winner-display" id="winnerDisplay">
          <span class="winner-emoji">🏆</span>
          <div id="singleWinner">
            <p class="winner-label">Победитель</p>
            <div class="winner-name" id="winnerName"></div>
          </div>
          <div class="multiple-winners" id="multipleWinners" style="display:none;"></div>
        </div>
        <button class="btn-again" id="btnAgain">↩ Провести ещё раз</button>
      </div>

      <p class="security-badge">🔒 Данные участников не отправляются на сервер — всё работает в браузере</p>
    </div>"""

TEMPLATE = """\
<!doctype html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<link rel="icon" type="image/svg+xml" href="./favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Manrope:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./assets/style.css">
</head>
<body>
<!-- YANDEX_METRIKA -->

<header class="site-header">
  <div class="container">
    <a href="./index.html" class="brand">
      <img src="./favicon.svg" alt="{site_name}">
      <span>{site_name}</span>
    </a>
    <nav class="site-nav">
{nav}
    </nav>
  </div>
</header>

<main>
  <section class="hero container">
    <h1><span>{h1}</span></h1>
    <p class="lead">{lead}</p>
  </section>

  <div class="container">
{tool}

    <article class="article">
{article}
    </article>

    <div class="related">
      <h2>Другие инструменты</h2>
      <ul>
{related}
      </ul>
    </div>
  </div>
</main>

<footer class="site-footer">
  <div class="container">{site_name} · случайный выбор честно и прозрачно</div>
</footer>

<script src="./assets/tool.js"></script>
</body>
</html>"""

def page_url(p):
    return BASE_URL + "/" if p["slug"] == "index" else BASE_URL + "/" + p["filename"]

def nav(current):
    return "\n".join(
        '      <a href="./{f}"{a}>{l}</a>'.format(
            f=p["filename"], l=p["nav_label"],
            a=' class="active"' if p["slug"] == current else "")
        for p in PAGES)

def related(current):
    return "\n".join(
        '      <li><a href="./{f}">{t}</a></li>'.format(f=p["filename"], t=p["title"])
        for p in PAGES if p["slug"] != current)

def generate():
    for p in PAGES:
        html = TEMPLATE.format(
            title=p["title"], description=p["description"],
            canonical=page_url(p), site_name=SITE_NAME,
            nav=nav(p["slug"]), h1=p["h1"], lead=p["lead"],
            tool=TOOL_HTML,
            article=p["article"].strip(),
            related=related(p["slug"]),
        )
        out = os.path.join(OUTPUT_DIR, p["filename"])
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print("OK  " + p["filename"])

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in PAGES:
            f.write("  <url><loc>{}</loc></url>\n".format(page_url(p)))
        f.write("</urlset>")
    print("OK  sitemap.xml")

    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(BASE_URL))
    print("OK  robots.txt")

if __name__ == "__main__":
    generate()
    print("\nГотово! Вставь код Яндекс.Метрики вместо <!-- YANDEX_METRIKA --> в каждом файле.")
