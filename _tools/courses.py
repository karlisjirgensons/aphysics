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
SITE_TITLE = "PD un nodarbības"
SITE_LEAD = ("Pārbaudes darbu ģenerators un stundu prezentācijas telefonam "
             "un datoram. Izvēlies, ko vajag.")
# Kursa stundu sarakstam paskaidrojums nav vajadzīgs - virsraksts un
# tematu saraksts pasaka visu. Tukša rinda nozīmē "bez paskaidrojuma".
LESSONS_LEAD = ""

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

# Lapas, kas mapē stāv blakus stundām, bet nav prezentācijas: rīki, ko atver
# temata beigās. Atslēga ir faila nosaukums bez "_tt", vērtība - uzraksts
# sarakstā. Šo lasa gan site_index.py (kur rīku likt), gan fd_common.py (ar
# kādu vārdu failu saukt), tāpēc nosaukums ir vienā vietā (DRY).
RIKI = {
    "Formatīvais darbs": "Ģenerēt formatīvo darbu",
}


def ordered():
    """Kursi sākumlapas secībā."""
    return sorted(COURSES.items(), key=lambda kv: kv[1]["order"])
