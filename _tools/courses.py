# -*- coding: utf-8 -*-
"""Kursu reģistrs - viena vieta, kur zināms, kas ir vietnē (SRP).

Šo importē gan html_deck.py (prezentāciju būvēšanai), gan site_index.py
(sarakstu un sākumlapas būvēšanai), lai ceļi un nosaukumi nebūtu ierakstīti
divās vietās (DRY).

Lauki:
    root     - mape ar tematu apakšmapēm
    title    - kursa nosaukums (parasts teksts, HTML aizsargā attēlotājs)
    kicker   - paskaidrojums zem nosaukuma
    label    - uzraksts uz sākumlapas pogas
    pattern  - kuras .pptx konvertēt
    order    - secība sākumlapā
"""

SITE_ROOT = "C:/aphysics"
SITE_TITLE = "Fizika un dabaszinības"
SITE_LEAD = ("Stundu prezentācijas telefonam un datoram. "
             "Izvēlies mācību priekšmetu.")
LESSONS_LEAD = ("Prezentācijas telefonam un datoram. Uz telefona saturs "
                "sakārtojas vienā slejā; uz datora rādās parastais "
                "platais slaida skats.")

COURSES = {
    "dabaszinibas": {
        "root": SITE_ROOT + "/Dabaszinibas",
        "title": "Dabaszinības",
        "kicker": "fizikas daļa · 10.-12. klase",
        "label": "Dabaszinības",
        "pattern": "*.pptx",
        "order": 1,
    },
    "fizika": {
        "root": SITE_ROOT + "/Fizika_1",
        "title": "Fizika I",
        "kicker": "10.-11. klase · 3 stundas nedēļā",
        "label": "Fizika 1 (3x ned.)",
        "pattern": "*_tt.pptx",
        "order": 2,
    },
}

DEFAULT_COURSE = "dabaszinibas"


def ordered():
    """Kursi sākumlapas secībā."""
    return sorted(COURSES.items(), key=lambda kv: kv[1]["order"])
