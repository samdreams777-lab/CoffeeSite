# COMMON COFFEE — PROJECT CONTEXT

> Самодостаточный контекст для передачи работы между AI-агентами.
> Создан: 2026-09-03
> Основа: реальный код, не предположения.

---

## Current State

**Проект:** Common Coffee (ранее "Le Mugs", кафе-кантен во Франции)
**Локальный путь:** `D:\HERMES\CoffeeSite`
**Рабочая директория:** `D:\HERMES\CoffeeSite\site`
**Репозиторий:** https://github.com/samdreams777-lab/CoffeeSite
**Ветка:** `main`
**Статус:** Есть незакоммиченные изменения (3 файла)

### Что работает
- EN и VI загружаются локально
- Loading screen с GSAP-анимацией
- Hero / titleslide с анимацией
- Parallax scroll работает
- Все секции отображаются
- Fonts: Be Vietnam Pro (headings), Manrope (body), BernardoModaSemibold (logo)
- Google Maps через iframe embed
- 4 image 404 исправлены (filename corrections)

### Что проблемно
- Logo визуально не perfect centered: offset ~9.5px от viewport center (системное поведение GSAP, присутствует во всех языках одинаково)
- Responsive behavior НЕ проверен автоматически (Playwright limitations)
- Pre-existing passive event listener errors (jQuery/Chrome, не влияет на функциональность)

### Над чем ведётся работа
- Визуальное выравнивание EN ↔ VI
- Loading screen и logo centering
- Vietnamese typography readability

### Наиболее важные файлы
- `site/en/index.html` — English entry point
- `site/vi/index.html` — Vietnamese entry point
- `site/wp-content/themes/mugs/style.css` — main stylesheet
- `site/wp-content/themes/mugs/js/main.min.js` — GSAP/ScrollMagic logic

---

## Architecture

### Entry Points

| URL | Файл | Язык |
|-----|------|------|
| `/` | `site/index.html` | FR (default) |
| `/en/index.html` | `site/en/index.html` | EN |
| `/vi/index.html` | `site/vi/index.html` | VI |

### Directory Structure

```
D:\HERMES\CoffeeSite\
├── site\                          # статический сайт (всё здесь)
│   ├── index.html                 # FR (default)
│   ├── en\
│   │   ├── index.html             # EN
│   │   ├── concept\
│   │   ├── pictures\
│   │   ├── events\
│   │   └── contact\
│   ├── vi\
│   │   └── index.html             # VI
│   ├── concept\                   # FR subpages
│   ├── pictures\
│   ├── les-evenements\
│   ├── contact\
│   ├── wp-content\
│   │   └── themes\mugs\
│   │       ├── style.css          # main stylesheet (2746 lines)
│   │       ├── js\
│   │       │   ├── main.min.js    # main JS (GSAP + ScrollMagic)
│   │       │   ├── mainmobile.min.js
│   │       │   ├── scrollmagic\   # ScrollMagic plugin
│   │       │   └── pace.min.js    # loading progress
│   │       └── images\            # all images
│   ├── wp-includes\               # jQuery local copy
│   └── vendor\gsap\               # GSAP 1.17 local
│       └── TweenMax.min.js
└── README.md
```

### Key Dependencies

| Library | Version | Purpose | Source |
|---------|---------|---------|--------|
| GSAP (TweenMax) | 1.17 | Animations | Local vendor |
| ScrollMagic | — | Scroll-triggered animations | Local wp-content |
| jQuery | 3.x | DOM manipulation | Local wp-includes |
| Pace.js | — | Loading progress | Local wp-content |
| Be Vietnam Pro | — | Headings font | Google Fonts |
| Manrope | — | Body font | Google Fonts |
| BernardoModaSemibold | — | Logo font | Google Fonts |

---

## Page Structure

### Sections (EN)

| Section | ID | Content | Animation | Parallax |
|---------|-----|---------|-----------|----------|
| Loading | `.blackscreen2` | SVG logo CAMON | GSAP fade-out on load | — |
| Hero | `.section1` | Titleslide + logo | Fade + slide up | Yes (layers) |
| Section 2 | `.section2` | Intro text | — | — |
| Section 3 | `.section3` | Text + lampe image | Reveal on scroll | Yes |
| Section 4 | `.section4` | Parallax background | Reveal on scroll | Yes |
| Section 5 | `.section5` | Menu content | — | Yes |
| Section 6 | `.section6` | Large content | — | — |
| Section 7 | `.section7` | Text content | — | — |
| Section 8 | `.section8` | Additional content | — | — |
| Section 9 | `.section9` | Team (equipe) | Mobile reset JS | — |
| Section 10 | `.section10` | Schedule | — | — |
| Section 11 | `.section11` | Background image | — | Yes |
| Section 12 | `.section12` | Menu items | — | — |
| Footer | `.section13` | Footer | — | — |

### Navigation

- Vertical snap scrolling между секциями
- ScrollMagic Controller управляет transitions
- Desktop: arrow navigation в section1
- Mobile: scroll, no snap

---

## Visual System

### Color Palette (verified from code)

| Color | Hex | Usage |
|-------|-----|-------|
| Dark teal | `#0f5152` | Section 2 heading, footer background |
| Light peach | `#f4c9c0` | Section 2 body, accent |
| White | `#ffffff` | Body text on dark |
| Black | `#000000` | Loading overlay |

### Typography System

**Headings:** `Be Vietnam Pro` (Google Fonts) — supports Vietnamese diacritics

**Body:** `Manrope` (Google Fonts) — supports Vietnamese diacritics

**Logo:** `BernardoModaSemibold` (Google Fonts) — logo/SVG text only

**Loading logo:** Same SVG font as main logo, inherits BernardoModaSemibold

**Inline CSS override (EN + VI):**
```css
p, .paragraph p, .textOverparallax p, .section p {
  font-family: 'Manrope', sans-serif !important;
  font-weight: 400;
  line-height: 1.65 !important;
  font-size: 16px !important;
}
.blackscreen2 #logoLoading text,
.section1 .titleslide,
.section1 .titleslide * {
  font-family: 'BernardoModaSemibold', 'BernardoModa', sans-serif !important;
}
```

### Animation Philosophy

- Loading screen: fade out via GSAP, then DOM removal
- Hero: titleslide slides up + fades, textIntro reveals
- Sections: opacity + transform reveals on scroll (ScrollMagic)
- Parallax: background layers move at different speeds
- Mobile: GSAP transforms reset via inline JS to prevent conflicts

---

## Responsive

### Breakpoints (from CSS)

| Breakpoint | Behavior |
|------------|----------|
| `max-width: 768px` | Mobile layout: full-width layers, relative positioning, no snap |
| `max-width: 480px` | Small mobile: smaller parasols, adjusted text |
| `min-width: 481px and max-width: 768px` | Tablet adjustments |

### Mobile-Specific Fixes (inline CSS in HTML)

```css
/* Mobile reset for GSAP transforms */
.equipe1, .equipe2, .equipe3 {
  position: relative !important;
  left: auto !important;
  right: auto !important;
  top: auto !important;
  transform: none !important;
}
```

**Note:** Responsive на 375/430/768/1024/1366/1440/1920 НЕ проверен автоматически в текущем окружении.

---

## Assets

### Image Paths (verified)

| HTML Reference | Actual File | Status |
|----------------|-------------|--------|
| `wasabi.png` | `sauce-soja.png` | FIXED (now uses correct path) |
| `Legume-2.png` | `Legume-1.png` | FIXED |
| `Salade.png` | `salade-lentilles.png` | FIXED |
| `section11-2.png` (CSS) | `section11-1.png` | FIXED |

### Verified Existing Images

```
wp-content/themes/mugs/images/
├── Legume-1.png         (163×436)
├── Legume-2.png        (NOT USED)
├── sauce-soja.png       (2400×2400)
├── salade-lentilles.png (525×525)
├── section11-1.png
├── section11-3.jpg
├── FDDG-en.svg
├── FDDG-fr.svg
├──lampe-section3.png
├── section4_1stplan.jpg
└── ... (many more)
```

### Menu Item Images (section12)

Images are SVG paths embedded directly in HTML, NOT external files.

---

## Loading Screen

### Structure

```html
<div class="blackscreen2">
  <svg id="logoLoading" class="brand-logo-svg" viewBox="0 0 758 254.5">
    <text font-family="BernardoModaSemibold">CAMON</text>
  </svg>
</div>
```

### Animation

GSAP timeline:
1. `.blackscreen2` opacity → 0
2. `.section1 .titleslide` opacity → 0, y → -300
3. `.textIntro` y → 0
4. `.blackscreen2` removed from DOM after transition

Fallback: `setInterval` removes `.blackscreen2` after 5s if not removed by GSAP.

### Font

Loading logo uses `BernardoModaSemibold` via inline CSS override:
```css
.blackscreen2 #logoLoading text {
  font-family: 'BernardoModaSemibold', 'BernardoModa', sans-serif !important;
}
```

---

## Logo

### Structure

- SVG element with `id="logo"` and `id="logoLoading"`
- Text element "CAMON" inside
- ViewBox: `0 0 758 254.5`
- Rendered width: 250px (CSS)

### Positioning

CSS (from style.css):
```css
.titleslide {
  position: absolute;
  left: 50%;
  top: calc(50% - 190px);
  z-index: 10002;
}
```

GSAP overrides at runtime with calculated values.

### Known Issue: Centering

**Symptom:** Logo centerX = 1319px, viewport center = 960px, offset = 9.5px

**Root cause:** GSAP dynamically calculates `left` position based on SVG dimensions. CSS `left: 50%` gets overridden.

**Behavior:** Same offset in EN and VI (verified). This is NOT an EN-specific bug.

**Fix required:** Modify GSAP calculation in `main.min.js` — NOT a CSS fix.

---

## QA History

### Previously Reported → Currently Verified

| Issue | Status | Notes |
|-------|--------|-------|
| Loading logo font = Pacifico | ✅ FIXED | Now BernardoModaSemibold |
| S3/S4 font-size = 14px | ✅ FIXED | Now 16px with line-height 1.65 |
| wasabi.png 404 | ✅ FIXED | → sauce-soja.png |
| Legume-2.png 404 | ✅ FIXED | → Legume-1.png |
| Salade.png 404 | ✅ FIXED | → salade-lentilles.png |
| section11-2.png 404 | ✅ FIXED | → section11-1.png |
| Google Maps JS unused | ✅ REMOVED | iframe map works without it |
| EN ↔ VI geometry | ✅ IDENTICAL | Both show same offset from center |
| Logo not centered | ⚠️ UNRESOLVED | 9.5px offset in all languages |

### Currently Unresolved

1. **Logo centering** — requires JS fix in main.min.js, not CSS
2. **Responsive** — not automatically tested (Playwright limitations)
3. **Passive event listener** — pre-existing jQuery issue, not our code

---

## Rules For Future Changes

1. **EN и VI тестируются параллельно** — нельзя менять одну локализацию без проверки другой
2. **Визуальное ≠ DOM presence** — элемент может быть в DOM, но анимация может не работать
3. **HTTP 200 ≠ визуально корректно** — всегда проверять реальное отображение
4. **Logo centering = JS problem** — не пытаться чинить CSS offsets
5. **No hardcoded language offsets** — не добавлять `left: -9px` и т.п.
6. **Typography = не только font-size** — line-height, font-weight, contrast тоже важны
7. **Vietnamese = Manrope + Be Vietnam Pro** — не использовать BernardoModa для body
8. **No `!important` без необходимости** — cascade-first
9. **No blind rollback** — сначала определить причину
10. **Visual QA после изменений** — не ограничиваться DOM inspection
11. **Assets проверять по реальным путям** — не предполагать что файл существует
12. **Responsive проверять на реальных viewport** — 375, 430, 768, 1024, 1366, 1440, 1920
13. **Commit только после approval** — никаких push до явного разрешения
14. **Сохранять stash перед экспериментами** — не терять работающий код
15. **Loading screen = GSAP timeline** — не ломать CSS transition без проверки GSAP

---

## Local Development

### Server

```bash
cd D:\HERMES\CoffeeSite\site
python -m http.server 8080
# или
node -e "require('http').createServer((req,res)=>{res.writeHead(200,{'Content-Type':'text/html'});require('fs').createReadStream(req.url==='/'?'index.html':req.url).pipe(res)}).listen(8080)"
```

### URLs

| URL | Content |
|-----|---------|
| http://localhost:8080/ | VI (default) |
| http://localhost:8080/en/index.html | EN |
| http://localhost:8080/vi/index.html | VI |

### Verification Commands

```bash
# Check HTTP status
curl -o /dev/null -w "%{http_code}" http://localhost:8080/en/index.html
# Should return: 200

# Check for syntax errors
node -e "require('fs').readFileSync('en/index.html','utf8')" 2>&1
```

---

## Git & Deployment

### Repository

```
https://github.com/samdreams777-lab/CoffeeSite
```

### Branches

| Branch | Purpose |
|--------|---------|
| `main` | Current working branch |
| `dash` | Old/alternative branch |

### Deployment

GitHub Pages — файлы из `site/` деploятся на https://samdreams777-lab.github.io/CoffeeSite/

EN: https://samdreams777-lab.github.io/CoffeeSite/en/
VI: https://samdreams777-lab.github.io/CoffeeSite/vi/

### Current Uncommitted Changes

```
M en/index.html
M vi/index.html
M wp-content/themes/mugs/style.css
```

**NO COMMIT / NO PUSH — awaiting user approval**

---

## Critical Files

| File | Purpose | Criticality |
|------|---------|------------|
| `site/en/index.html` | EN entry point | HIGH |
| `site/vi/index.html` | VI entry point | HIGH |
| `site/wp-content/themes/mugs/style.css` | Main stylesheet | HIGH |
| `site/wp-content/themes/mugs/js/main.min.js` | GSAP + ScrollMagic logic | HIGH |
| `site/vendor/gsap/TweenMax.min.js` | GSAP core | HIGH |
| `site/index.html` | FR entry point (default) | MEDIUM |
| `site/wp-content/themes/mugs/js/scrollmagic/` | ScrollMagic plugin | HIGH |
| `site/wp-content/themes/mugs/images/*` | All images | MEDIUM |

---

## Context For New Chat

> Ты продолжаешь работу над проектом Common Coffee.
> Это НЕ новый проект — не начинай с нуля.
>
> **Сначала прочитай этот файл (PROJECT_CONTEXT.md).**
> Затем проверь текущий код прежде чем делать предположения.
>
> **Приоритет источников:**
> 1. Текущий код проекта (реальные файлы)
> 2. Структура файлов
> 3. Конфигурация
> 4. Фактически проверенное поведение
> 5. Этот контекстный файл
>
> **Не доверяй автоматически:**
> - Статусам "FIXED" из старых QA
> - Предположениям о том, как должно работать
> - Значениям, которые не проверены в коде
>
> **Всегда проверяй:**
> - EN и VI вместе (не по отдельности)
> - Реальные пути к файлам
> - Визуальное поведение, не только DOM
> - Console + Network в браузере
>
> **Ключевое правило:** EN и VI должны выглядеть и вести себя идентично по геометрии, анимациям и функциональности.
