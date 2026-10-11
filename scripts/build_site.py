"""Build the bilingual, static Association Jisr website."""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVENT = "activities/youth-university-2026"

COPY = {
    "ar": {
        "name": "جمعية جسر الطفولة والشباب",
        "short": "جمعية جسر",
        "tagline": "جسور للطفولة والشباب",
        "nav": [("من نحن", "about"), ("مجالات العمل", "programs"), ("الأنشطة", "activities"), ("شارك معنا", "participate"), ("تواصل", "contact")],
        "home": "الرئيسية", "lang": "Français", "skip": "تجاوز إلى المحتوى", "menu": "فتح القائمة", "close": "إغلاق القائمة",
        "footer_text": "فضاء للتربية والمبادرة والمشاركة، من أجل طفولة وشباب يملكان فرصاً أوسع.",
        "footer_place": "المقر الوطني · مكناس، المغرب", "footer_event": "نشاطنا المقبل", "footer_more": "اكتشف النشاط", "footer_rights": "جميع الحقوق محفوظة",
        "notice": "النشاط المقبل", "notice_title": "جامعة الشباب", "notice_date": "20–24 أكتوبر 2026", "notice_link": "تفاصيل النشاط",
        "pages": {
            "home": ("الرئيسية", "جمعية جسر الطفولة والشباب: مبادرات تربوية وثقافية وتطوعية، وأنشطة للطفولة والشباب في المغرب."),
            "about": ("من نحن", "تعرّف إلى تأسيس جمعية جسر الطفولة والشباب وتاريخ اسمها ورسالتها التربوية ومقرها الوطني بمكناس."),
            "programs": ("مجالات العمل", "أهداف جمعية جسر: التربية والتخييم والشباب، دعم التعلم والنساء والفتيات، الرياضة والتضامن والشراكات."),
            "activities": ("الأنشطة", "تابع أنشطة جمعية جسر الطفولة والشباب، ومنها جامعة الشباب من 20 إلى 24 أكتوبر 2026 بالسعيدية."),
            "participate": ("شارك معنا", "تعرّف إلى طرق المشاركة في أنشطة جمعية جسر: التطوع، الانخراط والتعاون."),
            "contact": ("تواصل", "معلومات التواصل المتاحة لجمعية جسر الطفولة والشباب ولنشاط جامعة الشباب."),
            EVENT: ("جامعة الشباب", "جامعة الشباب من 20 إلى 24 أكتوبر 2026 بالمركز الوطني للتخييم بالسعيدية، لفائدة الشباب من 18 إلى 35 سنة."),
        },
    },
    "fr": {
        "name": "Association Jisr pour l’Enfance et la Jeunesse",
        "short": "Association Jisr", "tagline": "Des passerelles pour grandir et agir",
        "nav": [("L’association", "about"), ("Nos domaines", "programs"), ("Activités", "activities"), ("S’engager", "participate"), ("Contact", "contact")],
        "home": "Accueil", "lang": "العربية", "skip": "Aller au contenu", "menu": "Ouvrir le menu", "close": "Fermer le menu",
        "footer_text": "Un espace d’éducation, d’initiative et de participation pour ouvrir de nouvelles perspectives aux enfants et aux jeunes.",
        "footer_place": "Siège national · Meknès, Maroc", "footer_event": "À venir", "footer_more": "Découvrir l’activité", "footer_rights": "Tous droits réservés",
        "notice": "À venir", "notice_title": "Université des jeunes", "notice_date": "20–24 octobre 2026", "notice_link": "Voir l’activité",
        "pages": {
            "home": ("Accueil", "Association Jisr pour l’Enfance et la Jeunesse : initiatives éducatives, culturelles et bénévoles au Maroc."),
            "about": ("L’association", "Découvrez la création, l’évolution du nom et la mission éducative de l’Association Jisr, dont le siège national est à Meknès."),
            "programs": ("Nos domaines", "Les objectifs de Jisr : éducation, enfance et jeunesse, soutien scolaire, femmes et filles, sport, solidarité et coopération."),
            "activities": ("Activités", "Découvrez les activités de Jisr, notamment l’Université des jeunes du 20 au 24 octobre 2026 à Saïdia."),
            "participate": ("S’engager", "Découvrez les façons de participer aux activités de Jisr : bénévolat, adhésion et coopération."),
            "contact": ("Contact", "Les coordonnées disponibles pour l’Association Jisr et l’Université des jeunes."),
            EVENT: ("Université des jeunes", "Université des jeunes du 20 au 24 octobre 2026 au Centre national de camping de Saïdia, pour les 18 à 35 ans."),
        },
    },
}


def url(lang: str, page: str = "home") -> str:
    return f"/{lang}/" if page == "home" else f"/{lang}/{page}/"


def a(lang: str, page: str, label: str, cls: str = "") -> str:
    return f'<a class="{cls}" href="{url(lang, page)}">{label}</a>'


def header(lang: str, active: str) -> str:
    t = COPY[lang]
    other = "fr" if lang == "ar" else "ar"
    nav = "".join(
        f'<a href="{url(lang, slug)}" {"aria-current=\"page\"" if active == slug else ""}>{label}</a>'
        for label, slug in t["nav"]
    )
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<div class="topline"><div class="wrap topline-inner"><span>{t["notice"]} <span class="topline-dot">✦</span> {t["notice_title"]} <span class="topline-date">· {t["notice_date"]}</span></span><a href="{url(lang, EVENT)}">{t["notice_link"]} <span aria-hidden="true">↗</span></a></div></div>
<header class="site-header"><div class="wrap header-inner">
  <a class="brand" href="{url(lang)}" aria-label="{t["home"]} — {t["name"]}"><img src="/assets/logo-jisr-original-2026-10.png" width="225" height="127" alt="{t["name"]}"></a>
  <button class="menu-toggle" type="button" aria-controls="site-nav" aria-expanded="false" data-open="{t["menu"]}" data-close="{t["close"]}" aria-label="{t["menu"]}"><span></span><span></span><span></span></button>
  <nav id="site-nav" class="site-nav" aria-label="{ 'التنقل الرئيسي' if lang == 'ar' else 'Navigation principale' }">{nav}</nav>
  <a class="language" href="{url(other, active)}" lang="{other}" hreflang="{other}" aria-label="{ 'انتقل إلى الفرنسية' if lang == 'ar' else 'Passer en arabe' }">{t["lang"]}</a>
</div></header>'''


def footer(lang: str) -> str:
    t = COPY[lang]
    links = "".join(f'<a href="{url(lang, slug)}">{label}</a>' for label, slug in t["nav"])
    return f'''<footer class="site-footer"><div class="wrap footer-grid">
  <div><a class="footer-name" href="{url(lang)}">{t["name"]}</a><p>{t["footer_text"]}</p><span class="footer-place">{t["footer_place"]}</span></div>
  <div><h2>{'استكشف الموقع' if lang == 'ar' else 'Explorer le site'}</h2><nav class="footer-links" aria-label="{ 'روابط أسفل الصفحة' if lang == 'ar' else 'Liens de pied de page' }">{links}</nav></div>
  <div class="footer-feature"><span class="eyebrow">{t["footer_event"]}</span><h2>{t["notice_title"]}</h2><p>{t["notice_date"]} · { 'السعيدية' if lang == 'ar' else 'Saïdia' }</p>{a(lang, EVENT, t["footer_more"] + ' ↗', 'footer-action')}</div>
</div><div class="wrap footer-bottom"><span>© <span id="year">2026</span> {t["short"]}. {t["footer_rights"]}.</span><span dir="ltr">ajej.ma</span></div></footer>'''


def layout(lang: str, page: str, body: str) -> str:
    t = COPY[lang]
    title, description = t["pages"][page]
    direction = "rtl" if lang == "ar" else "ltr"
    current = "https://ajej.ma" + url(lang, page)
    image = "https://ajej.ma/assets/youth-university-2026.webp" if page in ("activities", EVENT) else "https://ajej.ma/assets/logo-jisr-original-2026-10.png"
    return f'''<!doctype html>
<html lang="{lang}" dir="{direction}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{escape(description, quote=True)}"><meta name="theme-color" content="#0a3261"><meta name="color-scheme" content="light">
<meta property="og:type" content="website"><meta property="og:site_name" content="Association Jisr"><meta property="og:title" content="{escape(title, quote=True)} | {escape(t['short'], quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:image" content="{image}"><meta property="og:url" content="{current}">
<title>{escape(title)} | {escape(t['short'])}</title>
<link rel="canonical" href="{current}"><link rel="alternate" hreflang="ar" href="https://ajej.ma{url('ar', page)}"><link rel="alternate" hreflang="fr" href="https://ajej.ma{url('fr', page)}"><link rel="alternate" hreflang="x-default" href="https://ajej.ma{url('ar', page)}">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site-2026-statute.css"><script defer src="/assets/site-2026.js"></script>
</head><body>{header(lang, page)}<main id="main">{body}</main>{footer(lang)}</body></html>'''


def page_hero(lang: str, eyebrow: str, title: str, lead: str, crumb: str = "") -> str:
    home = COPY[lang]["home"]
    breadcrumb = f'<nav class="breadcrumbs" aria-label="{ "مسار الصفحة" if lang == "ar" else "Fil d’Ariane" }"><a href="{url(lang)}">{home}</a><span aria-hidden="true">/</span><span>{crumb or title}</span></nav>'
    return f'<section class="interior-hero"><div class="wrap">{breadcrumb}<span class="eyebrow">{eyebrow}</span><h1>{title}</h1><p>{lead}</p></div><div class="hero-orbit" aria-hidden="true"></div></section>'


def home(lang: str) -> str:
    if lang == "ar":
        return f'''<section class="home-hero"><div class="wrap hero-layout"><div class="hero-content"><span class="eyebrow"><span class="tiny-star">✦</span> جمعية جسر الطفولة والشباب · المغرب</span><h1>نفتح <em>جسوراً</em> تعبر بها الطفولة والشباب نحو الفرص.</h1><p class="hero-lead">نلتقي حول التربية والتخييم والمبادرة والعمل التطوعي، لنمنح الأطفال والشباب مساحة يكتشفون فيها قدراتهم ويشاركون في بناء مجتمعهم.</p><div class="hero-actions">{a(lang,'activities','اكتشف أنشطتنا <span aria-hidden="true">↗</span>','btn btn-primary')}{a(lang,'about','تعرّف إلى الجمعية','btn btn-ghost')}</div><div class="hero-note"><span class="note-line"></span> من مكناس إلى فضاءات العمل الجمعوي بالمغرب</div></div><figure class="hero-visual"><img src="/assets/workshop-morocco-2026.webp" alt="صورة تعبيرية لشباب في ورشة عمل تعاونية بالمغرب" width="1200" height="900" fetchpriority="high"></figure></div></section>
<section class="ticker" aria-label="مجالات اهتمامنا"><div class="wrap ticker-inner"><span>الطفولة والتخييم</span><b>✦</b><span>التربية والتكوين</span><b>✦</b><span>المبادرة الشبابية</span><b>✦</b><span>التطوع والمواطنة</span></div></section>
<section class="section featured-section"><div class="wrap featured-layout"><div class="featured-copy"><span class="eyebrow">على الرزنامة · أكتوبر 2026</span><h2>جامعة الشباب <span>في السعيدية</span></h2><p>لقاء لفائدة الشباب من 18 إلى 35 سنة تحت شعار «المخيمات التربوية.. رؤية جديدة لصناعة الحياة».</p><div class="event-facts"><span><b>20–24</b> أكتوبر 2026</span><span><b>18–35</b> سنة</span><span><b>السعيدية</b> المركز الوطني للتخييم</span></div>{a(lang,EVENT,'كل تفاصيل النشاط <span aria-hidden="true">↗</span>','text-action')}</div><a class="featured-poster" href="{url(lang,EVENT)}" aria-label="عرض ملصق جامعة الشباب وتفاصيلها"><img src="/assets/youth-university-2026.webp" alt="ملصق جامعة الشباب" width="1414" height="2000" loading="lazy"><span>عرض الإعلان الكامل ↗</span></a></div></section>
<section class="section areas-section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">مجالات عملنا</span><h2>مسارات متعددة، <em>غاية واحدة.</em></h2></div><p>نربط التعلم بالتجربة، ونهيئ فضاءات للمشاركة والتعبير والعمل الجماعي.</p></div><div class="area-grid"><article class="area-card"><span class="area-index">01 / تعلّم</span><div class="area-icon" aria-hidden="true">✳</div><h3>التربية والتكوين</h3><p>ورشات ومسارات تفتح المجال للتعلّم وتنمية المهارات والإبداع.</p></article><article class="area-card"><span class="area-index">02 / اكتشاف</span><div class="area-icon" aria-hidden="true">◌</div><h3>الطفولة والتخييم</h3><p>تجارب تربوية جماعية تجمع النشاط والترفيه والتعلّم بالحياة.</p></article><article class="area-card"><span class="area-index">03 / مبادرة</span><div class="area-icon" aria-hidden="true">↗</div><h3>الشباب والتطوع</h3><p>فرص للشباب كي يقودوا مبادرات ويشاركوا بمهاراتهم ووقتهم.</p></article><article class="area-card"><span class="area-index">04 / تعبير</span><div class="area-icon" aria-hidden="true">✦</div><h3>الثقافة والمواطنة</h3><p>فضاءات للحوار والتعبير والمساهمة الإيجابية في المجتمع.</p></article></div>{a(lang,'programs','تعرّف إلى مجالات عملنا <span aria-hidden="true">↗</span>','text-action centered-action')}</div></section>
<section class="section about-band"><div class="wrap about-band-layout"><div><span class="eyebrow">من نحن</span><h2>الجسر يبدأ <em>بالإنصات</em>، ويكبر بالفعل المشترك.</h2></div><div><p>جمعية جسر الطفولة والشباب إطار مدني يضع الأطفال والشباب في قلب المبادرة. مقرها الوطني بمكناس، وتعمل على بناء فرص للتعلم والمشاركة عبر العمل الجمعوي والتعاون.</p><div class="about-stat"><strong>2019</strong><span>سنة تأسيس الجمعية</span></div>{a(lang,'about','تعرف إلى قصتنا <span aria-hidden="true">↗</span>','text-action')}</div></div></section>
<section class="section steps-section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">طريقتنا</span><h2>من الفكرة إلى أثر يُعاش.</h2></div><p>تبدأ المبادرة من حاجات الأطفال والشباب، وتكتسب معناها بالمشاركة الفعلية.</p></div><div class="steps-grid"><article><span>01</span><h3>نستمع</h3><p>نفهم ما يهم الأطفال والشباب في محيطهم.</p></article><article><span>02</span><h3>نصمم معاً</h3><p>نحوّل الأفكار إلى أنشطة تربوية ومساحات للتجريب.</p></article><article><span>03</span><h3>نتحرك</h3><p>نتعاون مع المتطوعين والشركاء لإنجاز المبادرات.</p></article></div></div></section>
<section class="section join-section"><div class="wrap join-box"><div><span class="eyebrow">كن جزءاً من الجسر</span><h2>لديك وقت أو فكرة أو خبرة؟ <em>هناك مكان لمساهمتك.</em></h2><p>تعرّف إلى مسارات التطوع والانخراط والتعاون مع الجمعية.</p></div>{a(lang,'participate','طرق المشاركة <span aria-hidden="true">↗</span>','btn btn-light')}</div></section>'''
    return f'''<section class="home-hero"><div class="wrap hero-layout"><div class="hero-content"><span class="eyebrow"><span class="tiny-star">✦</span> Association Jisr · Maroc</span><h1>Des <em>passerelles</em> pour grandir, s’exprimer et agir.</h1><p class="hero-lead">Autour de l’éducation, des colonies, de l’initiative et du bénévolat, nous ouvrons aux enfants et aux jeunes des espaces où découvrir leurs capacités et prendre part à la vie de leur communauté.</p><div class="hero-actions">{a(lang,'activities','Découvrir nos activités <span aria-hidden="true">↗</span>','btn btn-primary')}{a(lang,'about','L’association','btn btn-ghost')}</div><div class="hero-note"><span class="note-line"></span> De Meknès aux espaces associatifs du Maroc</div></div><figure class="hero-visual"><img src="/assets/workshop-morocco-2026.webp" alt="Image illustrative de jeunes dans un atelier collaboratif au Maroc" width="1200" height="900" fetchpriority="high"></figure></div></section>
<section class="ticker" aria-label="Nos domaines"><div class="wrap ticker-inner"><span>Enfance et colonies</span><b>✦</b><span>Éducation et formation</span><b>✦</b><span>Initiative des jeunes</span><b>✦</b><span>Bénévolat et citoyenneté</span></div></section>
<section class="section featured-section"><div class="wrap featured-layout"><div class="featured-copy"><span class="eyebrow">À l’agenda · Octobre 2026</span><h2>L’Université des jeunes <span>à Saïdia</span></h2><p>Une rencontre destinée aux 18–35 ans, autour du thème « Les colonies éducatives : une nouvelle vision pour façonner la vie ».</p><div class="event-facts"><span><b>20–24</b> octobre 2026</span><span><b>18–35</b> ans</span><span><b>Saïdia</b> Centre national de camping</span></div>{a(lang,EVENT,'Tous les détails <span aria-hidden="true">↗</span>','text-action')}</div><a class="featured-poster" href="{url(lang,EVENT)}" aria-label="Voir l’affiche et les détails de l’Université des jeunes"><img src="/assets/youth-university-2026.webp" alt="Affiche de l’Université des jeunes" width="1414" height="2000" loading="lazy"><span>Voir l’affiche complète ↗</span></a></div></section>
<section class="section areas-section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">Nos domaines</span><h2>Plusieurs chemins, <em>une ambition.</em></h2></div><p>Relier apprentissage et expérience, ouvrir des espaces de participation, d’expression et d’action collective.</p></div><div class="area-grid"><article class="area-card"><span class="area-index">01 / Apprendre</span><div class="area-icon" aria-hidden="true">✳</div><h3>Éducation et formation</h3><p>Ateliers et parcours pour développer compétences, curiosité et créativité.</p></article><article class="area-card"><span class="area-index">02 / Explorer</span><div class="area-icon" aria-hidden="true">◌</div><h3>Enfance et colonies</h3><p>Expériences collectives associant activité, loisirs et apprentissage de la vie.</p></article><article class="area-card"><span class="area-index">03 / Initier</span><div class="area-icon" aria-hidden="true">↗</div><h3>Jeunesse et bénévolat</h3><p>Des occasions pour les jeunes de porter des initiatives et offrir leurs talents.</p></article><article class="area-card"><span class="area-index">04 / S’exprimer</span><div class="area-icon" aria-hidden="true">✦</div><h3>Culture et citoyenneté</h3><p>Des espaces de dialogue, d’expression et de contribution à la communauté.</p></article></div>{a(lang,'programs','Explorer nos domaines <span aria-hidden="true">↗</span>','text-action centered-action')}</div></section>
<section class="section about-band"><div class="wrap about-band-layout"><div><span class="eyebrow">L’association</span><h2>Tout commence par <em>l’écoute</em> et grandit dans l’action collective.</h2></div><div><p>L’Association Jisr pour l’Enfance et la Jeunesse place les enfants et les jeunes au cœur de l’initiative. Son siège national est à Meknès. Elle construit des occasions d’apprendre et de participer par l’action associative et la coopération.</p><div class="about-stat"><strong>2019</strong><span>Année de création</span></div>{a(lang,'about','Découvrir notre démarche <span aria-hidden="true">↗</span>','text-action')}</div></div></section>
<section class="section steps-section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">Notre démarche</span><h2>De l’idée à l’action concrète.</h2></div><p>Une initiative part des aspirations des enfants et des jeunes et prend forme avec leur participation.</p></div><div class="steps-grid"><article><span>01</span><h3>Écouter</h3><p>Comprendre ce qui compte pour les enfants et les jeunes.</p></article><article><span>02</span><h3>Construire ensemble</h3><p>Transformer des idées en expériences éducatives.</p></article><article><span>03</span><h3>Agir</h3><p>Coopérer avec bénévoles et partenaires sur le terrain.</p></article></div></div></section>
<section class="section join-section"><div class="wrap join-box"><div><span class="eyebrow">Faire partie du mouvement</span><h2>Du temps, une idée, une compétence ? <em>Votre place existe.</em></h2><p>Découvrez les chemins du bénévolat, de l’adhésion et de la coopération.</p></div>{a(lang,'participate','Comment participer <span aria-hidden="true">↗</span>','btn btn-light')}</div></section>'''


def about(lang: str) -> str:
    if lang == "ar":
        hero = page_hero(lang, "الجمعية · منذ 2019", "نلتقي لنمنح الفرص شكلاً حقيقياً.", "نؤمن بأن التربية والمشاركة تمنحان الأطفال والشباب القدرة على الاكتشاف والتعبير والمبادرة.", "من نحن")
        body = '''<section class="section"><div class="wrap editorial-grid"><div><span class="eyebrow">هويتنا</span><h2>جسر بين الإمكانات والفرص.</h2></div><div class="editorial-copy"><p>جمعية جسر الطفولة والشباب جمعية مدنية مغربية تأسست سنة 2019، ومقرها الوطني بمدينة مكناس. تجمعها رؤية تجعل الطفولة والشباب محوراً لبرامج تربوية وثقافية ومبادرات تشاركية.</p><p>نطمح إلى فضاءات يشعر فيها الطفل بالأمان للتجريب والتعلم، ويجد فيها الشاب فرصة لصناعة مبادرة والاشتغال إلى جانب الآخرين.</p></div></div></section><section class="section pale-section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">ما يوجّه عملنا</span><h2>مبادئ نترجمها في الميدان.</h2></div></div><div class="principles"><article><span>01</span><h3>الإنصات أولاً</h3><p>نبدأ من اهتمامات الأطفال والشباب وحاجات محيطهم.</p></article><article><span>02</span><h3>التعلّم بالمشاركة</h3><p>نمنح التجربة والعمل الجماعي مكاناً في الأنشطة التربوية.</p></article><article><span>03</span><h3>التعاون</h3><p>نبني المبادرات مع المتطوعين والفاعلين والشركاء.</p></article></div></div></section><section class="section"><div class="wrap editorial-grid"><div><span class="eyebrow">أين نحن</span><h2>مقر وطني في مكناس، وانفتاح على المبادرات المحلية.</h2></div><div class="editorial-copy"><p>توجد الجمعية وطنياً في مكناس، ولها فرع بميدلت. يتسع عملها لأنشطة وتعاونات تتجاوز مدينة أو فرعاً بعينه بحسب كل مبادرة.</p><p>نجمع في مجالات عملنا بين التربية والتكوين، الطفولة والتخييم، المبادرة الشبابية، الثقافة والمواطنة.</p>'''+a(lang,'programs','اكتشف مجالات عملنا ↗','text-action')+'''</div></div></section>'''
    else:
        hero = page_hero(lang, "L’association · depuis 2019", "Se rencontrer pour ouvrir des possibles.", "Nous croyons que l’éducation et la participation donnent aux enfants et aux jeunes les moyens de découvrir, de s’exprimer et d’agir.", "L’association")
        body = '''<section class="section"><div class="wrap editorial-grid"><div><span class="eyebrow">Notre identité</span><h2>Un pont entre les capacités et les possibilités.</h2></div><div class="editorial-copy"><p>Fondée en 2019, l’Association Jisr pour l’Enfance et la Jeunesse est une association marocaine dont le siège national est à Meknès. Elle place l’enfance et la jeunesse au centre d’initiatives éducatives, culturelles et participatives.</p><p>Nous aspirons à des espaces où les enfants peuvent explorer et apprendre, et où les jeunes peuvent initier des projets aux côtés d’autres acteurs.</p></div></div></section><section class="section pale-section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">Ce qui nous guide</span><h2>Des principes à mettre en pratique.</h2></div></div><div class="principles"><article><span>01</span><h3>Écouter d’abord</h3><p>Partir des intérêts des enfants et des jeunes et des besoins de leur environnement.</p></article><article><span>02</span><h3>Apprendre ensemble</h3><p>Donner une place à l’expérience et au collectif dans les activités éducatives.</p></article><article><span>03</span><h3>Coopérer</h3><p>Construire les initiatives avec les bénévoles, les acteurs et les partenaires.</p></article></div></div></section><section class="section"><div class="wrap editorial-grid"><div><span class="eyebrow">Notre ancrage</span><h2>Un siège à Meknès, des initiatives au-delà d’une seule ville.</h2></div><div class="editorial-copy"><p>Le siège national de l’association se trouve à Meknès et une section existe à Midelt. Les activités et collaborations peuvent dépasser le cadre d’une seule ville ou section, selon chaque initiative.</p><p>Nos domaines associent éducation et formation, enfance et colonies, initiative des jeunes, culture et citoyenneté.</p>'''+a(lang,'programs','Explorer nos domaines ↗','text-action')+'''</div></div></section>'''
    if lang == "ar":
        roots = '''<section class="section pale-section"><div class="wrap editorial-grid"><div><span class="eyebrow">جذور الجمعية</span><h2>من التأسيس إلى اسم جسر.</h2></div><div class="editorial-copy"><p>تأسست الجمعية يوم 19 أكتوبر 2019 باسم «وسيط الخير للتربية والتنمية». وفي المؤتمر الوطني المنعقد بمكناس يوم 20 غشت 2024 اعتمدت اسم «جمعية جسر الطفولة والشباب»، مواكبةً لاتساع مجالات عملها مع الأطفال والشباب.</p><p>يصفها قانونها الأساسي بأنها جمعية تربوية تنموية تطوعية، غير ربحية ومستقلة عن الأحزاب السياسية والهيئات النقابية. مقرها الوطني بمدينة مكناس.</p></div></div></section>'''
    else:
        roots = '''<section class="section pale-section"><div class="wrap editorial-grid"><div><span class="eyebrow">Nos origines</span><h2>De la création au nom Jisr.</h2></div><div class="editorial-copy"><p>Créée le 19 octobre 2019 sous le nom <span lang="ar" dir="rtl">«وسيط الخير للتربية والتنمية»</span>, l’association a adopté celui d’« Association Jisr pour l’Enfance et la Jeunesse » lors de son congrès national tenu à Meknès le 20 août 2024, en accord avec l’élargissement de ses champs d’action.</p><p>Ses statuts la définissent comme une association éducative, de développement et de bénévolat, sans but lucratif et indépendante des partis politiques et des organisations syndicales. Son siège national est à Meknès.</p></div></div></section>'''
    return hero + body + roots + cta(lang)


def programs(lang: str) -> str:
    if lang == "ar":
        hero = page_hero(lang, "ما نعمل من أجله", "التعلّم والتجربة والمبادرة، في مسارات تتكامل.", "أربعة مجالات تجمع أنشطة الجمعية حول حاجات الطفولة والشباب وإمكانات العمل المشترك.", "مجالات العمل")
        cards = [("01", "التربية والتكوين", "تعلم يمتد إلى الحياة.", "ورشات وأنشطة تتيح تنمية المهارات، التفكير الإبداعي، والتعاون. يهمنا أن يتعلم المشاركون بالفعل والتجربة، لا بالاستماع وحده."), ("02", "الطفولة والتخييم", "مساحة آمنة للاكتشاف.", "أنشطة تربوية وترفيهية وتجارب جماعية تساعد الأطفال على بناء الثقة بالنفس واحترام الآخرين والعيش المشترك."), ("03", "الشباب والتطوع", "الشباب شركاء في الفعل.", "فضاءات للمبادرة والتأطير والتطوع، تتيح للشباب اقتراح الأفكار والمشاركة في تنفيذها داخل مجتمعاتهم."), ("04", "الثقافة والمواطنة", "التعبير يصنع الانتماء.", "أنشطة للحوار والإبداع والمشاركة المدنية تمنح الأطفال والشباب فرصة للتعبير وتبادل الأفكار.")]
        after = '<section class="section pale-section"><div class="wrap editorial-grid"><div><span class="eyebrow">من المجالات إلى الأنشطة</span><h2>كل نشاط فرصة للقاء والتعلّم.</h2></div><div class="editorial-copy"><p>تتخذ هذه المجالات أشكالاً متعددة: لقاءات، ورشات، مخيمات، ومبادرات يقودها أو يشارك فيها الشباب. انظر الإعلان الحالي لمعرفة تفاصيل النشاط المتاح الآن.</p>'+a(lang,'activities','شاهد الأنشطة ↗','text-action')+'</div></div></section>'
    else:
        hero = page_hero(lang, "Nos champs d’action", "Apprendre, expérimenter et prendre l’initiative.", "Quatre domaines complémentaires articulent les activités de l’association autour des enfants, des jeunes et de l’action collective.", "Nos domaines")
        cards = [("01", "Éducation et formation", "Des apprentissages pour la vie.", "Ateliers et activités pour développer les compétences, la créativité et la coopération. L’expérience et la pratique y ont toute leur place."), ("02", "Enfance et colonies", "Un espace pour découvrir.", "Activités éducatives, loisirs et expériences collectives qui soutiennent la confiance en soi, le respect et la vie en groupe."), ("03", "Jeunesse et bénévolat", "Les jeunes acteurs du changement.", "Espaces d’initiative, d’accompagnement et de bénévolat où les jeunes peuvent proposer des idées et contribuer à les réaliser."), ("04", "Culture et citoyenneté", "L’expression crée des liens.", "Rencontres, créativité et participation citoyenne pour donner aux enfants et aux jeunes une place dans le dialogue.")]
        after = '<section class="section pale-section"><div class="wrap editorial-grid"><div><span class="eyebrow">Des domaines aux activités</span><h2>Chaque activité, une occasion de se rencontrer.</h2></div><div class="editorial-copy"><p>Ces domaines prennent la forme de rencontres, d’ateliers, de colonies et d’initiatives portées ou partagées par les jeunes. Retrouvez les détails de l’activité annoncée actuellement.</p>'+a(lang,'activities','Voir les activités ↗','text-action')+'</div></div></section>'
    content = ''.join(f'<article class="program-row"><span class="program-number">{n}</span><div><span class="eyebrow">{kicker}</span><h2>{title}</h2></div><p>{description}</p></article>' for n,title,kicker,description in cards)
    if lang == "ar":
        statutory = '''<section class="section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">من أهداف القانون الأساسي</span><h2>مجالات أخرى تتقاطع مع رسالتنا.</h2></div><p>تحدد هذه الأهداف اتجاه عمل الجمعية، وتتحول إلى أنشطة بحسب البرامج والشراكات المتاحة.</p></div><div class="principles"><article><span>01 / التعليم</span><h3>مساندة المسار الدراسي</h3><p>المساهمة في الحد من الهدر المدرسي، ودعم تكامل دور الأسرة والمدرسة، وتنمية مواهب الأطفال والشباب.</p></article><article><span>02 / التمكين</span><h3>النساء والفتيات</h3><p>دعم التعلم ومحو الأمية والتكوين، وتشجيع المبادرات التي توسع فرص النساء والفتيات.</p></article><article><span>03 / المجتمع</span><h3>الرياضة والسلامة والتضامن</h3><p>الأنشطة الرياضية والتوعية بالسلامة الطرقية والإسعافات الأولية، والمبادرات التضامنية والصحية.</p></article></div></div></section>'''
    else:
        statutory = '''<section class="section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">Objectifs inscrits dans les statuts</span><h2>D’autres champs liés à notre mission.</h2></div><p>Ces objectifs orientent l’action de l’association et peuvent prendre forme selon les programmes et partenariats disponibles.</p></div><div class="principles"><article><span>01 / Éducation</span><h3>Soutenir le parcours scolaire</h3><p>Contribuer à la lutte contre le décrochage scolaire, renforcer les liens entre famille et école et développer les talents des enfants et des jeunes.</p></article><article><span>02 / Autonomie</span><h3>Femmes et filles</h3><p>Soutenir l’apprentissage, l’alphabétisation et la formation, ainsi que les initiatives qui élargissent leurs possibilités.</p></article><article><span>03 / Communauté</span><h3>Sport, sécurité et solidarité</h3><p>Promouvoir les activités sportives, la sensibilisation à la sécurité routière et aux premiers secours, et les initiatives solidaires et de santé.</p></article></div></div></section>'''
    return hero + f'<section class="section"><div class="wrap program-list">{content}</div></section>' + statutory + after + cta(lang)


def activities(lang: str) -> str:
    if lang == "ar":
        hero = page_hero(lang, "الأنشطة والمستجدات", "حيث تتحول الأفكار إلى لقاءات وتجارب.", "تابع الأنشطة المعلنة وتعرّف إلى تفاصيل المشاركة والمواعيد والأماكن من مصدرها.", "الأنشطة")
        card = f'''<section class="section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">على الرزنامة</span><h2>النشاط المقبل</h2></div></div><article class="listing-card"><a class="listing-image" href="{url(lang,EVENT)}" aria-label="تفاصيل جامعة الشباب"><img src="/assets/youth-university-2026.webp" alt="ملصق جامعة الشباب" width="1414" height="2000"></a><div class="listing-body"><span class="status-pill">20–24 أكتوبر 2026 · السعيدية</span><h3>جامعة الشباب</h3><p>لقاء لفائدة الشباب من 18 إلى 35 سنة بالمركز الوطني للتخييم بالسعيدية، تحت شعار «المخيمات التربوية.. رؤية جديدة لصناعة الحياة».</p><dl><div><dt>المكان</dt><dd>السعيدية</dd></div><div><dt>الفئة</dt><dd>18–35 سنة</dd></div></dl>{a(lang,EVENT,'اطلع على الإعلان الكامل ↗','btn btn-primary')}</div></article></div></section>'''
    else:
        hero = page_hero(lang, "Activités et actualités", "Quand les idées deviennent des rencontres.", "Retrouvez les activités annoncées, leurs dates, leurs lieux et les informations utiles pour y participer.", "Activités")
        card = f'''<section class="section"><div class="wrap"><div class="section-heading"><div><span class="eyebrow">À l’agenda</span><h2>Notre prochaine activité</h2></div></div><article class="listing-card"><a class="listing-image" href="{url(lang,EVENT)}" aria-label="Détails de l’Université des jeunes"><img src="/assets/youth-university-2026.webp" alt="Affiche de l’Université des jeunes" width="1414" height="2000"></a><div class="listing-body"><span class="status-pill">20–24 octobre 2026 · Saïdia</span><h3>Université des jeunes</h3><p>Une rencontre pour les 18–35 ans au Centre national de camping de Saïdia, sous le thème « Les colonies éducatives : une nouvelle vision pour façonner la vie ».</p><dl><div><dt>Lieu</dt><dd>Saïdia</dd></div><div><dt>Public</dt><dd>18–35 ans</dd></div></dl>{a(lang,EVENT,'Voir l’annonce complète ↗','btn btn-primary')}</div></article></div></section>'''
    return hero + card


def participate(lang: str) -> str:
    if lang == "ar":
        hero = page_hero(lang, "كن جزءاً من الجسر", "لكل مساهمة مكان، ولكل مبادرة بداية.", "يمكن للشباب والمهتمين بالتربية والشركاء أن يساهموا بطرق مختلفة وفق الأنشطة المتاحة.", "شارك معنا")
        ways = [("01", "تطوّع", "ساهم بوقتك ومهاراتك في التأطير أو التنظيم أو الأنشطة الميدانية، بحسب احتياجات كل مبادرة."), ("02", "انخرط", "شارك في الحياة الجمعوية واقترح أفكاراً تنسجم مع مجالات عمل الجمعية."), ("03", "تعاون", "إذا كنت تمثل مؤسسة أو جمعية، يمكن بناء أنشطة مشتركة في التربية والطفولة والشباب.")]
        note = '<section class="section pale-section"><div class="wrap editorial-grid"><div><span class="eyebrow">فرصة حالية</span><h2>جامعة الشباب، 20–24 أكتوبر.</h2></div><div class="editorial-copy"><p>الإعلان الحالي موجّه للشباب من 18 إلى 35 سنة. تتضمن صفحة النشاط مكان اللقاء وأرقام التواصل المخصصة للاستفسار عن المشاركة فيه.</p>'+a(lang,EVENT,'تفاصيل جامعة الشباب ↗','text-action')+'</div></div></section>'
    else:
        hero = page_hero(lang, "Rejoindre le mouvement", "Chaque contribution compte. Chaque initiative commence quelque part.", "Les jeunes, les personnes engagées dans l’éducation et les partenaires peuvent contribuer selon les activités proposées.", "S’engager")
        ways = [("01", "Être bénévole", "Offrez du temps et des compétences pour l’animation, l’organisation ou les activités de terrain selon les besoins des initiatives."), ("02", "Adhérer", "Participez à la vie associative et proposez des idées en lien avec les domaines de l’association."), ("03", "Coopérer", "Vous représentez une institution ou une association ? Des actions communes peuvent réunir éducation, enfance et jeunesse.")]
        note = '<section class="section pale-section"><div class="wrap editorial-grid"><div><span class="eyebrow">Une occasion actuelle</span><h2>L’Université des jeunes, du 20 au 24 octobre.</h2></div><div class="editorial-copy"><p>L’annonce actuelle s’adresse aux 18–35 ans. Sa page présente le lieu et les numéros dédiés aux renseignements sur la participation à cette activité.</p>'+a(lang,EVENT,'Détails de l’activité ↗','text-action')+'</div></div></section>'
    cards = ''.join(f'<article class="way-card"><span>{n}</span><h2>{title}</h2><p>{body}</p></article>' for n,title,body in ways)
    if lang == "ar":
        membership = '''<div class="membership-note"><h2>الانخراط في الجمعية</h2><p>ينص القانون الأساسي على أعضاء نشيطين يشاركون بانتظام في عمل الجمعية، وأعضاء شرفيين يساندون أهدافها. يُدرس طلب الانخراط من طرف المكتب المختص وفق شروط العضوية، ولا تُعد الرغبة في المشاركة قبولاً تلقائياً للعضوية.</p></div>'''
    else:
        membership = '''<div class="membership-note"><h2>Adhérer à l’association</h2><p>Les statuts distinguent les membres actifs, qui participent régulièrement à la vie associative, et les membres d’honneur, qui soutiennent sa mission. Une demande d’adhésion est étudiée par le bureau compétent selon les conditions statutaires ; manifester son intérêt ne vaut pas admission automatique.</p></div>'''
    return hero + f'<section class="section"><div class="wrap ways-grid">{cards}</div><div class="wrap">{membership}</div></section>' + note + cta(lang)


def contact(lang: str) -> str:
    if lang == "ar":
        hero = page_hero(lang, "تواصل", "لنواصل الحديث ونبني فرص التعاون.", "تعرف إلى المعلومات المتاحة حالياً عن الجمعية وعن النشاط المقبل.", "تواصل")
        body = f'''<section class="section"><div class="wrap contact-grid"><div class="contact-panel"><span class="eyebrow">الجمعية</span><h2>جمعية جسر الطفولة والشباب</h2><div class="contact-line"><span>المقر الوطني</span><strong>مكناس، المغرب</strong></div><div class="contact-line"><span>الموقع الرسمي</span><strong dir="ltr">ajej.ma</strong></div><p class="contact-hint">للاستفسار عن النشاط المعلن، استعمل بيانات التواصل الواردة في الملصق والمبيّنة هنا.</p></div><div class="contact-panel contact-panel-blue"><span class="eyebrow">جامعة الشباب · 20–24 أكتوبر</span><h2>للمشاركة أو الاستفسار عن هذا النشاط</h2><div class="contact-line"><span>لحبيب آيت لحبيب</span><a href="tel:+212667082383" dir="ltr">0667 08 23 83</a></div><div class="contact-line"><span>عبد الرحيم آيت احميد</span><a href="tel:+212762248173" dir="ltr">0762 24 81 73</a></div>{a(lang,EVENT,'جميع تفاصيل النشاط ↗','btn btn-light')}</div></div></section>'''
    else:
        hero = page_hero(lang, "Contact", "Poursuivons la conversation et construisons des liens.", "Voici les informations actuellement disponibles sur l’association et son activité à venir.", "Contact")
        body = f'''<section class="section"><div class="wrap contact-grid"><div class="contact-panel"><span class="eyebrow">L’association</span><h2>Association Jisr pour l’Enfance et la Jeunesse</h2><div class="contact-line"><span>Siège national</span><strong>Meknès, Maroc</strong></div><div class="contact-line"><span>Site officiel</span><strong dir="ltr">ajej.ma</strong></div><p class="contact-hint">Pour toute question concernant l’activité annoncée, utilisez les coordonnées publiées sur son affiche et rappelées ici.</p></div><div class="contact-panel contact-panel-blue"><span class="eyebrow">Université des jeunes · 20–24 octobre</span><h2>Participer ou demander des renseignements sur cette activité</h2><div class="contact-line"><span>لحبيب آيت لحبيب</span><a href="tel:+212667082383" dir="ltr">0667 08 23 83</a></div><div class="contact-line"><span>عبد الرحيم آيت احميد</span><a href="tel:+212762248173" dir="ltr">0762 24 81 73</a></div>{a(lang,EVENT,'Tous les détails ↗','btn btn-light')}</div></div></section>'''
    return hero + body


def event(lang: str) -> str:
    if lang == "ar":
        hero = page_hero(lang, "نشاط قريب · 20–24 أكتوبر 2026", "جامعة الشباب", "من 20 إلى 24 أكتوبر 2026 بالمركز الوطني للتخييم بالسعيدية، لفائدة الشباب من 18 إلى 35 سنة.", "جامعة الشباب")
        title = "معلومات النشاط"
        fields = [("التاريخ", "من 20 إلى 24 أكتوبر 2026"), ("المكان", "المركز الوطني للتخييم بالسعيدية"), ("الفئة المستهدفة", "الشباب من 18 إلى 35 سنة"), ("تحت شعار", "المخيمات التربوية.. رؤية جديدة لصناعة الحياة")]
        contact_title = "للمشاركة أو الاستفسار عن النشاط"
        caption = "الملصق الكامل لجامعة الشباب"
        alt = "ملصق جامعة الشباب: 20 إلى 24 أكتوبر 2026 في السعيدية"
    else:
        hero = page_hero(lang, "À venir · 20–24 octobre 2026", "Université des jeunes", "Du 20 au 24 octobre 2026 au Centre national de camping de Saïdia, pour les jeunes de 18 à 35 ans.", "Université des jeunes")
        title = "Informations pratiques"
        fields = [("Dates", "Du 20 au 24 octobre 2026"), ("Lieu", "Centre national de camping de Saïdia"), ("Public", "Jeunes de 18 à 35 ans"), ("Thème", "Les colonies éducatives : une nouvelle vision pour façonner la vie")]
        contact_title = "Participation et renseignements sur l’activité"
        caption = "Affiche complète de l’Université des jeunes"
        alt = "Affiche de l’Université des jeunes : 20 au 24 octobre 2026 à Saïdia"
    dl = "".join(f'<div><dt>{key}</dt><dd>{value}</dd></div>' for key,value in fields)
    details = f'''<section class="section"><div class="wrap event-layout"><figure class="event-poster"><img src="/assets/youth-university-2026.webp" width="1414" height="2000" alt="{alt}"><figcaption>{caption}</figcaption></figure><div class="event-side"><span class="eyebrow">{COPY[lang]["notice"]}</span><h2>{title}</h2><dl class="event-data">{dl}</dl><div class="event-contact"><h3>{contact_title}</h3><p><span lang="ar">لحبيب آيت لحبيب</span><a href="tel:+212667082383" dir="ltr">0667 08 23 83</a></p><p><span lang="ar">عبد الرحيم آيت احميد</span><a href="tel:+212762248173" dir="ltr">0762 24 81 73</a></p></div></div></div></section>'''
    return hero + details


def cta(lang: str) -> str:
    if lang == "ar":
        return f'<section class="section join-section"><div class="wrap join-box"><div><span class="eyebrow">ابق قريباً من أنشطتنا</span><h2>اكتشف ما يحدث الآن، <em>وشارك بطريقتك.</em></h2></div>{a(lang,"activities","الأنشطة المعلنة ↗","btn btn-light")}</div></section>'
    return f'<section class="section join-section"><div class="wrap join-box"><div><span class="eyebrow">Suivre nos activités</span><h2>Découvrez ce qui se passe, <em>participez à votre façon.</em></h2></div>{a(lang,"activities","Les activités ↗","btn btn-light")}</div></section>'


BUILDERS = {"home": home, "about": about, "programs": programs, "activities": activities, "participate": participate, "contact": contact, EVENT: event}


def main() -> None:
    for lang in COPY:
        for page, build in BUILDERS.items():
            destination = ROOT / lang / ("" if page == "home" else page) / "index.html"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(layout(lang, page, build(lang)), encoding="utf-8")
    (ROOT / "index.html").write_text(layout("ar", "home", home("ar")), encoding="utf-8")
    entries = [f"  <url><loc>https://ajej.ma{url(lang, page)}</loc></url>" for lang in COPY for page in BUILDERS]
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(entries) + '\n</urlset>\n', encoding="utf-8")


if __name__ == "__main__":
    main()
