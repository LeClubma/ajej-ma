"""Build the two public activity detail pages from the verified event poster."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "activities/youth-university-2026"
poster = "/assets/youth-university-2026.webp"

content = {
    "ar": {
        "dir": "rtl",
        "title": "جامعة الشباب | جمعية جسر الطفولة والشباب",
        "description": "جامعة الشباب من 20 إلى 24 أكتوبر 2026 بالمركز الوطني للتخييم بالسعيدية، لفائدة الشباب من 18 إلى 35 سنة.",
        "skip": "تجاوز إلى المحتوى",
        "home": "الرئيسية",
        "about": "من نحن",
        "areas": "مجالات العمل",
        "news": "الأخبار",
        "join": "ساهم معنا",
        "contact": "اتصل بنا",
        "switch": "FR",
        "switch_label": "Passer en français",
        "menu": "القائمة الرئيسية",
        "nav": "التنقل الرئيسي",
        "section": "نشاط جمعوي",
        "name": "جامعة الشباب",
        "intro": "تُعلن جمعية جسر الطفولة والشباب عن جامعة الشباب، الموجهة إلى الشباب من 18 إلى 35 سنة.",
        "facts": "معلومات النشاط",
        "date_label": "التاريخ",
        "date": "من 20 إلى 24 أكتوبر 2026",
        "place_label": "المكان",
        "place": "المركز الوطني للتخييم بالسعيدية",
        "audience_label": "الفئة المستهدفة",
        "audience": "الشباب من 18 إلى 35 سنة",
        "slogan_label": "تحت شعار",
        "slogan": "المخيمات التربوية.. رؤية جديدة لصناعة الحياة",
        "contact_title": "للمشاركة أو الاستفسار",
        "caption": "الملصق الكامل لجامعة الشباب.",
        "poster_alt": "ملصق جامعة الشباب، 20 إلى 24 أكتوبر 2026 بالمركز الوطني للتخييم بالسعيدية.",
        "person1": "لحبيب آيت لحبيب",
        "person2": "عبد الرحيم آيت احميد",
        "footer": "معاً نحو مستقبل أفضل للطفولة والشباب.",
        "brand": "جمعية جسر الطفولة والشباب",
    },
    "fr": {
        "dir": "ltr",
        "title": "Université des jeunes | Association Jisr",
        "description": "Université des jeunes du 20 au 24 octobre 2026 au Centre national de camping de Saïdia, pour les jeunes de 18 à 35 ans.",
        "skip": "Aller au contenu",
        "home": "Accueil",
        "about": "À propos",
        "areas": "Nos domaines",
        "news": "Actualités",
        "join": "S’engager",
        "contact": "Contact",
        "switch": "العربية",
        "switch_label": "التبديل إلى العربية",
        "menu": "Menu principal",
        "nav": "Navigation principale",
        "section": "Activité associative",
        "name": "Université des jeunes",
        "intro": "L’Association Jisr pour l’Enfance et la Jeunesse annonce l’Université des jeunes, destinée aux 18–35 ans.",
        "facts": "Informations pratiques",
        "date_label": "Dates",
        "date": "Du 20 au 24 octobre 2026",
        "place_label": "Lieu",
        "place": "Centre national de camping de Saïdia",
        "audience_label": "Public",
        "audience": "Jeunes de 18 à 35 ans",
        "slogan_label": "Sous le thème",
        "slogan": "Les colonies éducatives : une nouvelle vision pour façonner la vie",
        "contact_title": "Participation et renseignements",
        "caption": "Affiche complète de l’Université des jeunes.",
        "poster_alt": "Affiche de l’Université des jeunes, du 20 au 24 octobre 2026 au Centre national de camping de Saïdia.",
        "person1": "لحبيب آيت لحبيب",
        "person2": "عبد الرحيم آيت احميد",
        "footer": "Ensemble pour l’avenir de l’enfance et de la jeunesse.",
        "brand": "Association Jisr pour l’Enfance et la Jeunesse",
    },
}

for lang, raw in content.items():
    c = {key: escape(value, quote=True) for key, value in raw.items()}
    other = "fr" if lang == "ar" else "ar"
    page_url = f"https://ajej.ma/{lang}/{SLUG}/"
    html = f"""<!doctype html>
<html lang="{lang}" dir="{c['dir']}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{c['description']}">
<meta name="theme-color" content="#123a65">
<meta property="og:type" content="article"><meta property="og:title" content="{c['title']}">
<meta property="og:image" content="https://ajej.ma{poster}">
<title>{c['title']}</title>
<link rel="canonical" href="{page_url}">
<link rel="alternate" hreflang="ar" href="https://ajej.ma/ar/{SLUG}/">
<link rel="alternate" hreflang="fr" href="https://ajej.ma/fr/{SLUG}/">
<style>.brand-logo{{display:block;width:180px;max-width:100%;height:auto}}.event-poster img{{display:block;width:100%;height:auto}}@media(max-width:560px){{.brand-logo{{width:135px}}}}</style>
<link rel="stylesheet" href="/assets/style-2026-10-activity.css">
<script defer src="/assets/event-2026.js"></script>
</head>
<body>
<a class="skip" href="#main">{c['skip']}</a>
<header class="site-header"><div class="container header-inner">
<a class="brand" href="/{lang}/" aria-label="{c['home']}"><img class="brand-logo" src="/assets/logo-jisr-original-2026-10.png" alt="{c['brand']}" width="180" height="101"></a>
<button class="menu-button" id="menu-button" type="button" aria-expanded="false" aria-controls="nav" aria-label="{c['menu']}"><span aria-hidden="true">☰</span></button>
<nav class="nav" id="nav" aria-label="{c['nav']}">
<a href="/{lang}/#about">{c['about']}</a><a href="/{lang}/#areas">{c['areas']}</a><a href="/{lang}/#news">{c['news']}</a><a href="/{lang}/#join">{c['join']}</a><a href="/{lang}/#contact">{c['contact']}</a>
</nav><a class="lang" href="/{other}/{SLUG}/" aria-label="{c['switch_label']}">{c['switch']}</a>
</div></header>
<main id="main">
<section class="event-page-hero"><div class="container">
<div class="breadcrumbs"><a href="/{lang}/">{c['home']}</a> / <span>{c['name']}</span></div>
<span class="section-tag">{c['section']}</span><h1>{c['name']}</h1><p>{c['intro']}</p>
</div></section>
<section class="section"><div class="container event-layout">
<figure class="event-poster"><img src="{poster}" alt="{c['poster_alt']}" width="1414" height="2000"><figcaption>{c['caption']}</figcaption></figure>
<aside class="event-details"><h2>{c['facts']}</h2>
<dl>
<div><dt>{c['date_label']}</dt><dd><time datetime="2026-10-20">{c['date']}</time></dd></div>
<div><dt>{c['place_label']}</dt><dd>{c['place']}</dd></div>
<div><dt>{c['audience_label']}</dt><dd>{c['audience']}</dd></div>
<div><dt>{c['slogan_label']}</dt><dd class="slogan">{c['slogan']}</dd></div>
</dl>
<div class="event-contact"><h3>{c['contact_title']}</h3>
<p><span lang="ar" dir="rtl">{c['person1']}</span><br><a href="tel:+212667082383">0667 08 23 83</a></p>
<p><span lang="ar" dir="rtl">{c['person2']}</span><br><a href="tel:+212762248173">0762 24 81 73</a></p>
</div></aside></div></section>
</main>
<footer class="footer"><div class="container footer-inner"><div><strong>{c['brand']}</strong><p>{c['footer']}</p></div><p>© <span id="year">2026</span> Association Jisr</p></div></footer>
</body></html>"""
    out = ROOT / lang / SLUG / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(out.relative_to(ROOT))
