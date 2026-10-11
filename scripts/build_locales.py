"""Generate the Arabic and French static pages from the shared homepage.

Run: python scripts/build_locales.py
The translated strings live in assets/main.js so the public pages and the
client-side language fallback use the same copy.
"""
from pathlib import Path
import json
import re

from lxml import html

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (ROOT / "index.html").read_text(encoding="utf-8")
JAVASCRIPT = (ROOT / "assets/main.js").read_text(encoding="utf-8")
match = re.search(r"^const translations=(\{.*?\});\s*const langButton=", JAVASCRIPT, re.S)
if not match:
    raise SystemExit("Could not find the shared translations")
translations = json.loads(match.group(1))

descriptions = {
    "ar": "الموقع الرسمي لجمعية جسر الطفولة والشباب بالمغرب، فضاء للتربية والتكوين والتطوع.",
    "fr": "Site officiel de l’Association Jisr pour l’Enfance et la Jeunesse au Maroc : éducation, formation et bénévolat.",
}
titles = {
    "ar": "جمعية جسر الطفولة والشباب | Association Jisr",
    "fr": "Association Jisr pour l’Enfance et la Jeunesse",
}

for lang in ("ar", "fr"):
    doc = html.fromstring(SOURCE)
    doc.set("lang", lang)
    doc.set("dir", "rtl" if lang == "ar" else "ltr")
    for el in doc.xpath("//*[@data-i18n]"):
        key = el.get("data-i18n")
        if key not in translations[lang]:
            raise SystemExit(f"Missing {lang} translation: {key}")
        el.text = translations[lang][key]

    doc.xpath("//title")[0].text = titles[lang]
    doc.xpath('//meta[@name="description"]')[0].set("content", descriptions[lang])
    doc.xpath('//link[@rel="canonical"]')[0].set("href", f"https://ajej.ma/{lang}/")
    for link in doc.xpath('//link[@rel="alternate"]'):
        target = link.get("hreflang")
        link.set("href", f"https://ajej.ma/{target if target in ('ar', 'fr') else 'ar'}/")
    for link in doc.xpath('//link[@rel="stylesheet"]'):
        link.set("href", "/" + link.get("href").lstrip("/"))
    for script in doc.xpath("//script[@src]"):
        script.set("src", "/" + script.get("src").lstrip("/"))
    for img in doc.xpath("//img"):
        img.set("src", "/" + img.get("src").lstrip("/"))
    for link in doc.xpath("//*[@data-event-link]"):
        link.set("href", f"/{lang}/activities/youth-university-2026/")
    doc.xpath("//aside[contains(concat(' ',normalize-space(@class),' '),' announcement-strip ')]")[0].set(
        "aria-label", "إعلان نشاط" if lang == "ar" else "Annonce d’activité"
    )
    doc.xpath("//a[contains(concat(' ',normalize-space(@class),' '),' event-card-image ')]")[0].set(
        "aria-label", translations[lang]["eventName"]
    )
    doc.xpath("//a[contains(concat(' ',normalize-space(@class),' '),' event-card-image ')]/img")[0].set(
        "alt", "ملصق جامعة الشباب، 20 إلى 24 أكتوبر 2026 بالسعيدية"
        if lang == "ar" else "Affiche de l’Université des jeunes, du 20 au 24 octobre 2026 à Saïdia"
    )
    doc.xpath("//a[contains(concat(' ',normalize-space(@class),' '),' brand ')]")[0].set("href", f"/{lang}/")
    doc.xpath("//a[contains(concat(' ',normalize-space(@class),' '),' brand ')]")[0].set(
        "aria-label", "الصفحة الرئيسية، جمعية جسر الطفولة والشباب" if lang == "ar" else "Accueil, Association Jisr"
    )
    doc.xpath("//nav")[0].set("aria-label", "التنقل الرئيسي" if lang == "ar" else "Navigation principale")
    doc.xpath("//button[@id='menu-button']")[0].set("aria-label", "القائمة الرئيسية" if lang == "ar" else "Menu principal")
    language_button = doc.xpath("//button[@id='lang']")[0]
    language_button.text = "FR" if lang == "ar" else "العربية"
    language_button.set("aria-label", "Passer en français" if lang == "ar" else "التبديل إلى العربية")
    doc.xpath("//img[contains(concat(' ',normalize-space(@class),' '),' brand-logo ')]")[0].set(
        "alt", "جمعية جسر الطفولة والشباب — Association Jisr pour l’Enfance et la Jeunesse"
    )
    doc.xpath("//div[contains(concat(' ',normalize-space(@class),' '),' hero-official-logo ')]/img")[0].set(
        "alt", "الشعار الرسمي لجمعية جسر الطفولة والشباب" if lang == "ar" else "Logo officiel de l’Association Jisr pour l’Enfance et la Jeunesse"
    )
    destination = ROOT / lang / "index.html"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(
        html.tostring(doc, encoding="unicode", method="html", doctype="<!doctype html>"),
        encoding="utf-8",
    )
    print(destination.relative_to(ROOT))
