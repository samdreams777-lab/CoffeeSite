# Локальная копия сайта Le Mugs (le-mugs.com)

Полная статическая локальная копия сайта Le Mugs — «Flagrant délit de gourmandise»,
кафе-кантеен в Сен-Рафаэль (Франция). Сайт построен на WordPress (тема «mugs»),
с анимациями GSAP + ScrollMagic, параллакс-фоном, вертикальным snap-меню по секциям
и адаптивным дизайном (desktop / tablet / mobile).

## Структура

```
D:\HERMES\CoffeeSite\
├── site\                     # готовая локальная копия (статический сайт)
│   ├── index.html            # французская главная (язык FR)
│   ├── en\index.html         # английская главная (язык EN)
│   ├── en\concept\           # подстраница: The concept
│   ├── en\pictures\          # подстраница: Pictures
│   ├── en\events\            # подстраница: Events
│   ├── en\contact\           # подстраница: Contact
│   ├── concept\              # французские версии подстраниц
│   ├── pictures\
│   ├── les-evenements\
│   ├── contact\
│   ├── wp-content\           # тема WordPress (css/js/images/fonts), uploads
│   ├── wp-includes\          # jQuery и пр. (локально)
│   └── vendor\gsap\          # GSAP 1.17 (локально)
├── crawl.py                  # краулер (исходный сбор)
├── crawl_fr.py               # докачка французских подстраниц
├── postprocess.py            # перепись абсолютных URL -> локальные
├── cleanup_meta.py           # финальная зачистка meta/og
├── fix_fr_meta.py            # перепись alternate/canonical (FR)
├── qa_playwright.py          # автотест: скриншоты + console/network errors
├── find_404.py               # поиск битых ресурсов (404)
├── compare.py                # визуальное сравнение с оригиналом
└── qa\ , compare\            # результаты QA и сравнения
```

## Как запустить (локально)

Любой статический HTTP-сервер из папки `site`. Например, встроенный Python:

```bash
cd D:\HERMES\CoffeeSite\site
python -m http.server 8099 --bind 127.0.0.1
```

Затем открыть в браузере:

- Английская версия:  http://127.0.0.1:8099/en/
- Французская версия: http://127.0.0.1:8099/

Подстраницы доступны по адресам:
`/en/concept/`, `/en/pictures/`, `/en/events/`, `/en/contact/`
(и французские: `/concept/`, `/pictures/`, `/les-evenements/`, `/contact/`).

> Важно: открывать строго через HTTP-сервер (не `file://`), иначе относительные
> пути к JS/CSS и AJAX-запросы (`ajax-menu.php`) не сработают.

## Что реализовано

- ✅ Полная визуальная структура (one-pager с 8 секциями + отдельные подстраницы)
- ✅ Все изображения, SVG, видео-постеры, шрифты (Bernardo Moda, Roboto) — локально
- ✅ CSS (style.css + плагины WPML/ResponsiveSlides/block-library) — локально
- ✅ JavaScript (jQuery, GSAP 1.17, ScrollMagic, parallax, responsiveslides, Pace,
  prefixfree, main.min.js / mainmobile.min.js) — локально
- ✅ Параллакс-фон, слайдер, scroll-анимации, hover-эффекты
- ✅ Вертикальное меню-навигация по секциям (дублирует поведение оригинала)
- ✅ Переключатель языка Français ⇄ English (ведёт на локальные страницы)
- ✅ Responsive (desktop / tablet / mobile) — подтверждено скриншотами
- ✅ 0 console errors, 0 failed requests, 0 битых 404 при загрузке
- ✅ Визуальное сходство с оригиналом: 100% (tablet/FR) и ~92–100% (desktop/mobile)

## Известные особенности (унаследованы от оригинала)

- `home_bg_far.png` — в оригинале ссылка ведёт на несуществующий файл (баг исходного
  сайта, 404). Локально создан fallback-файл (копия `.jpg`), чтобы устранить 404.
- Google Maps iframe и Facebook-ссылки — внешние; требуют интернета (не ломают локальную работу).
- Форма подписки / контактная форма в оригинале отправляются на backend WordPress
  (wp-ajax). Локально форма присутствует визуально, но отправка не работает без бэкенда
  (это соответствует статическому зеркалу).

## Проверка (QA)

```bash
# из D:\HERMES\CoffeeSite
python qa_playwright.py   # скриншоты + сбор ошибок -> qa\ и qa.log
python find_404.py         # список битых ресурсов (должен быть пустым)
python compare.py         # сравнение с оригиналом -> compare\ и compare.log
```
