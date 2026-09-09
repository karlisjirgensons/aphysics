# -*- coding: utf-8 -*-
"""Fizika I prezentāciju darbu (PR) vērtēšanas lapas.

Katram PR uzbūvē vienu .docx failu temata mapē: uzdevums skolēnam,
prezentācijas struktūra, vērtēšanas kritēriju tabula un skala.

Palaiž:  .venv/Scripts/python.exe _tools/gen_fiz_pr.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")

from docx.enum.table import WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH                        # noqa: E402
from docx.shared import Cm, Pt                                       # noqa: E402

import pd_common as C                                                # noqa: E402
from pd_common import (GREY, NAVY, WHITE, TEKSTA_PLATUMS, cell_text,  # noqa: E402
                       new_doc, para, shade, skala)
import fiz_ld_common as LDC                                          # noqa: E402

SAKNE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIZIKA = os.path.join(SAKNE, "Fizika_1")


PR10 = {
    "nr": 1,
    "klase": "10. klase",
    "nosaukums": "Pētījuma rezultātu prezentācija",
    "mape": "1. Ievads pētniecībā. Vienmērīga un nevienmērīga kustība",
    "fails": "PR1. Pētījuma rezultātu prezentācija_tt",
    "datums": "14.10.2026.",
    "svars": 5,
    "kopa": 20,
    "ilgums": 5,
    "pamats": "LD1 «Lodītes vidējais ātrums uz slīpas renītes» dati",
    "uzdevums": "Grupa 5 minūtēs izklāsta savu pētījumu: ko pētīja, kā "
                "mērīja, ko parāda grafiks un kāds ir secinājums. Pēc tam "
                "katrs grupas dalībnieks individuāli atbild uz vienu "
                "klases vai skolotāja jautājumu.",
    "struktura": [
        ("1. Pētāmais jautājums un hipotēze", "Ko tieši pētījāt un ko "
         "prognozējāt. Nosauc neatkarīgo un atkarīgo lielumu."),
        ("2. Metode", "Kā mērījāt: iekārta, ceļš s, augstumi, atkārtojumu "
         "skaits. Nosauc, kurus lielumus saglabājāt nemainīgus."),
        ("3. Dati un grafiks", "Rādi grafiku v(h) ar apzīmētām asīm. "
         "Nenolasi visu tabulu - parādi tendenci."),
        ("4. Secinājums", "Atbildi uz pētāmo jautājumu ar diviem "
         "konkrētiem skaitļiem no saviem datiem."),
        ("5. Kļūdas un uzlabojumi", "Viens kļūdu avots un viens konkrēts "
         "priekšlikums, kā pētījumu uzlabot."),
    ],
    "kriteriji": [
        ("Skaidri formulēts pētāmais jautājums un hipotēze", 3),
        ("Metode aprakstīta tā, ka pētījumu varētu atkārtot", 3),
        ("Parādīts grafiks ar apzīmētām asīm un mērvienībām", 3),
        ("Secinājums pamatots ar konkrētiem datiem, nevis vispārīgi", 4),
        ("Nosaukts kļūdu avots un konkrēts uzlabojums", 2),
        ("Ievērots laiks (5 min) un runa saprotama klasei", 2),
        ("Katrs dalībnieks individuāli atbild uz jautājumu par darbu", 3),
    ],
    "piezimes": [
        "Prezentācijas notiek pirmajā stundā pēc laboratorijas darba; "
        "katrai grupai 5 min uzstāšanās un 2 min jautājumiem.",
        "Vērtē gan grupas kopdarbu (1.-6. kritērijs), gan individuālo "
        "atbildi (7. kritērijs) - tāpēc atzīme var atšķirties grupas "
        "ietvaros.",
        "Slaidi nav obligāti; pietiek ar uz papīra uzzīmētu grafiku, ja tas "
        "ir salasāms no klases pēdējā sola.",
    ],
}

PR11 = {
    "nr": 1,
    "klase": "11. klase",
    "nosaukums": "Siltuma mājas rezultātu prezentācija",
    "mape": "8. Siltums un siltuma procesi",
    "fails": "PR1. Siltuma mājas rezultātu prezentācija_tt",
    "datums": "28.10.2026.",
    "svars": 4,
    "kopa": 20,
    "ilgums": 5,
    "pamats": "LD1 «Siltuma māja: siltumizolācijas pētīšana» dati",
    "uzdevums": "Grupa 5 minūtēs izklāsta siltumizolācijas pētījumu: "
                "jautājumu, metodi, atdzišanas līknes un ieteikumu, kuru "
                "materiālu izvēlēties. Pēc tam katrs grupas dalībnieks "
                "individuāli atbild uz vienu jautājumu.",
    "struktura": [
        ("1. Pētāmais jautājums un hipotēze", "Kuru materiālu salīdzinājāt "
         "un ko prognozējāt."),
        ("2. Godīgs salīdzinājums", "Kā nodrošinājāt salīdzināmus "
         "apstākļus: vienāds ūdens daudzums, sākuma temperatūra, "
         "izolācijas biezums, kontroles makets."),
        ("3. Dati un grafiks", "Rādi visu maketu atdzišanas līknes vienā "
         "grafikā ar leģendu."),
        ("4. Fizikālais skaidrojums", "Ar daļiņu modeli paskaidro, kāpēc "
         "labākais materiāls izolē labāk; nosauc aprēķināto Q = cmΔT."),
        ("5. Ieteikums un izvērtējums", "Kuru materiālu ieteiktu īstai "
         "mājai un kāpēc; nosauc vienu kļūdu avotu."),
    ],
    "kriteriji": [
        ("Skaidri formulēts pētāmais jautājums un hipotēze", 2),
        ("Pamatots, kā nodrošināts godīgs salīdzinājums", 3),
        ("Parādīts grafiks ar visām līknēm, asīm un leģendu", 3),
        ("Secinājums pamatots ar konkrētiem datiem", 3),
        ("Rezultāts izskaidrots ar daļiņu modeli un siltuma pārnesi", 3),
        ("Ieteikums īstai mājai pamatots ar vismaz diviem apsvērumiem", 2),
        ("Ievērots laiks (5 min) un runa saprotama klasei", 1),
        ("Katrs dalībnieks individuāli atbild uz jautājumu par darbu", 3),
    ],
    "piezimes": [
        "Prezentācijas notiek pirmajā stundā pēc rudens brīvlaika; katrai "
        "grupai 5 min uzstāšanās un 2 min jautājumiem.",
        "Šis vērtējums ir atsevišķs no LD1 protokola vērtējuma un no PD3 - "
        "e-klasē tos neapvieno.",
        "Ja grupas dati ir neizdevušies, prezentāciju vērtē pēc analīzes "
        "kvalitātes: kļūdas atpazīšana un pamatots uzlabojums dod pilnu "
        "punktu skaitu 5. un 6. kritērijā.",
    ],
}


def build(pr):
    mape = os.path.join(FIZIKA, pr["mape"])
    if not os.path.isdir(mape):
        raise SystemExit("Nav atrasta mape: %s" % mape)
    kopa = sum(p for _, p in pr["kriteriji"])
    assert kopa == pr["kopa"], "%s: kritēriju summa %d" % (pr["fails"], kopa)

    doc = new_doc()
    para(doc, "Fizika I  |  %s  |  %s  |  %s"
         % (pr["klase"], C.SKOLA, C.GADS), size=9, color=GREY, after=1)
    para(doc, "Prezentācijas darbs Nr. %d.  %s"
         % (pr["nr"], pr["nosaukums"]), size=16, bold=True, color=NAVY,
         after=1)
    para(doc, "Uzdevums, struktūra un vērtēšanas kritēriji", size=13,
         bold=True, color=NAVY, after=4)

    LDC.kaste(doc, "DARBA UZDEVUMS", [
        pr["uzdevums"],
        "Pamatā:  %s." % pr["pamats"],
        "Norise:  %s.   Ilgums:  %d min + 2 min jautājumiem."
        % (pr["datums"], pr["ilgums"]),
        "Vērtējums:  %d %% no gada atzīmes,  kopā %d punkti."
        % (pr["svars"], pr["kopa"]),
    ])

    para(doc, "Prezentācijas struktūra", size=12, bold=True, color=NAVY,
         before=8, after=3)
    for virs, apr in pr["struktura"]:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Cm(0.4)
        r = p.add_run(virs + "  ")
        r.font.size = Pt(11)
        r.font.bold = True
        r.font.name = "Calibri"
        r2 = p.add_run(apr)
        r2.font.size = Pt(10.5)
        r2.font.name = "Calibri"

    para(doc, "Vērtēšanas kritēriji", size=12, bold=True, color=NAVY,
         before=10, after=3)
    t = doc.add_table(rows=len(pr["kriteriji"]) + 2, cols=3)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, g in enumerate(["Nr.", "Kritērijs", "Punkti"]):
        shade(t.rows[0].cells[i], "1F3864")
        cell_text(t.rows[0].cells[i], g, size=9.5, bold=True, color=WHITE)
    for i, (kr, p) in enumerate(pr["kriteriji"], 1):
        cell_text(t.rows[i].cells[0], "%d." % i, size=10)
        cell_text(t.rows[i].cells[1], kr, size=10)
        cell_text(t.rows[i].cells[2], str(p), size=10,
                  align=WD_ALIGN_PARAGRAPH.CENTER)
    r = t.rows[len(pr["kriteriji"]) + 1]
    shade(r.cells[1], "EEF2F8")
    shade(r.cells[2], "EEF2F8")
    cell_text(r.cells[1], "KOPĀ", size=10, bold=True)
    cell_text(r.cells[2], str(pr["kopa"]), size=10, bold=True,
              align=WD_ALIGN_PARAGRAPH.CENTER)
    for i, w in enumerate([1.2, 14.0, 2.8]):
        for row in t.rows:
            row.cells[i].width = Cm(w)
    para(doc, after=2)

    para(doc, "Vērtēšanas skala", size=12, bold=True, color=NAVY, before=8,
         after=3)
    robezas = skala(pr["kopa"])
    t2 = doc.add_table(rows=2, cols=len(robezas))
    t2.style = "Table Grid"
    t2.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, (balle, apaksa, augsa) in enumerate(robezas):
        shade(t2.rows[0].cells[i], "EEF2F8")
        cell_text(t2.rows[0].cells[i], str(balle), size=9.5, bold=True,
                  color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER)
        cell_text(t2.rows[1].cells[i], "%d-%d" % (apaksa, augsa), size=9.5,
                  align=WD_ALIGN_PARAGRAPH.CENTER)
        for row in t2.rows:
            row.cells[i].width = Cm(TEKSTA_PLATUMS / len(robezas))
    para(doc, "Augšējā rindā - balle, apakšējā - punktu intervāls.",
         size=9, italic=True, color=GREY, after=2)

    para(doc, "Piezīmes skolotājam", size=12, bold=True, color=NAVY,
         before=8, after=2)
    for x in pr["piezimes"]:
        para(doc, "•  " + x, size=10.5, after=2, left=0.4)

    para(doc, "Grupas vērtējums", size=11, bold=True, color=NAVY, before=10,
         after=2)
    t3 = doc.add_table(rows=6, cols=4)
    t3.style = "Table Grid"
    t3.alignment = WD_TABLE_ALIGNMENT.LEFT
    for i, g in enumerate(["Skolēns", "Grupas daļa (p.)",
                           "Individuālā atbilde (p.)", "Kopā / balle"]):
        shade(t3.rows[0].cells[i], "EEF2F8")
        cell_text(t3.rows[0].cells[i], g, size=9.5, bold=True, color=NAVY)
    for r_ in t3.rows[1:]:
        r_.height = Cm(0.85)
        r_.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
    for i, w in enumerate([6.5, 3.8, 4.5, 3.2]):
        for row in t3.rows:
            row.cells[i].width = Cm(w)

    out = os.path.join(mape, "%s.docx" % pr["fails"])
    doc.save(out)
    print("Izveidots: %s" % os.path.relpath(out, SAKNE))
    return out


if __name__ == "__main__":
    for pr in (PR10, PR11):
        build(pr)
