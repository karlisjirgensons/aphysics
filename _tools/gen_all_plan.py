# -*- coding: utf-8 -*-
"""
Klase ALL - IZŅĒMUMA klase: 3 fizikas stundas nedēļā (pārējām klasēm 1),
un vienā mācību gadā jāapgūst viss 10., 11. un 12. klases fizikas saturs.

Stundas notiek TIKAI piektdienās - trīs stundas pēc kārtas.
Saturs ņemts no triju klašu plāniem (gen_dabaszinibas_plani.py) un salikts
secīgi: vispirms 10. klases, tad 11., tad 12. klases temati.

Centralizētais eksāmens šai klasei ir NĀKAMAJĀ mācību gadā, nevis
2027. gada maijā. Tāpēc mācību gads izmantojams pilnībā - stundas notiek
līdz maija beigām, un pēdējais pārbaudes darbs ir maija vidū. Saturs
netiek saīsināts: iekļauti visi triju klašu plānu temati un abu gadu
noslēguma nostiprināšanas bloki.
"""

import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_dabaszinibas_plani as G            # noqa: E402
from gen_dabaszinibas_plani import (          # noqa: E402
    Plans, NAVY, GREY, new_doc, para, kalendars, temata_tabula)


# ------------------------------------------- kalendārs: 3 stundas nedēļā
def slots_3x(sakums=dt.date(2026, 9, 1), beigas=dt.date(2027, 5, 31)):
    """Stundas notiek TIKAI piektdienās - trīs stundas pēc kārtas."""
    out, cur = [], sakums
    while cur <= beigas:
        if (cur.weekday() == 4
                and not any(a <= cur <= b for a, b in G.BRIVLAIKI)
                and cur not in G.SVETKI):
            out.extend([cur, cur, cur])
        cur += dt.timedelta(days=1)
    return out


class PDnum:
    """Vienai klasei PD jānumurē caurviju: PD1 ... PD9."""

    def __init__(self):
        self.n = 0

    def __call__(self, bloks):
        out = []
        for s in bloks:
            if s[0] == "PD":
                self.n += 1
                out.append(("PD", "PD%d" % self.n) + tuple(s[2:]))
            else:
                out.append(s)
        return out


def bez(bloks, *apakstemati):
    """Izņem stundas pēc apakštemata nosaukuma."""
    izn = set(apakstemati)
    out = [s for s in bloks if s[0] == "PD" or s[0] not in izn]
    atrasts = {s[0] for s in bloks if s[0] != "PD"}
    for a in izn:
        assert a in atrasts, "nav tāda apakštemata: %s" % a
    return out


# 11. klases vides faktoru bloks - četras stundas apvienotas divās
T9_APVIENOTS = [
    ("Troksnis un apgaismojums", "Kad skaņa un gaisma kļūst kaitīgas?",
     "Raksturo skaņas skaļumu decibelos un apgaismojuma atkarību no "
     "attāluma; izvērtē trokšņa ietekmi un darba vietas apgaismojumu."),
    ("Starojums vidē", "Kurš starojums ir bīstams?",
     "Salīdzina ultravioletā un elektromagnētiskā starojuma ietekmi; nošķir "
     "jonizējošu starojumu no nejonizējoša un izvērtē avota ticamību."),
]

EKS_PIEZ = ("Formatīvas stundas pēc pēdējā PD: apkopo visu gadu un iezīmē, "
            "kas jāatkārto pirms nākamā gada eksāmena. Jauns summatīvs "
            "darbs nav paredzēts.")


def build_all(path):
    G.DATUMI = slots_3x()

    p = Plans()
    nr = PDnum()

    # Eksāmens ir nākamajā mācību gadā, tāpēc saturu nesaīsina - iekļauti
    # visi triju klašu plānu temati un abu gadu noslēguma bloki.
    # ---------------------------------------------------------- 10. klase
    a1 = p.bloks(nr(G.K10_T1))
    a3 = p.bloks(nr(G.K10_T3))
    a5 = p.bloks(nr(G.K10_T5))
    a_nosl = p.bloks(nr(G.K10_NOSL))
    # ---------------------------------------------------------- 11. klase
    b7a = p.bloks(nr(G.K11_T7A))
    b7b = p.bloks(nr(G.K11_T7B))
    b8 = p.bloks(nr(G.K11_T8))
    b9 = p.bloks(nr(G.K11_T9 + G.K11_NOSL_PD))
    b_nosl = p.bloks(nr(G.K11_NOSL))
    # ---------------------------------------------------------- 12. klase
    c11 = p.bloks(nr(G.K12_T11))
    c13 = p.bloks(nr(G.K12_T13))
    c15 = p.bloks(nr(G.K12_T15))
    eks = p.bloks(G.K12_EKS)

    pedejais_pd = p.pd[-1][2]
    doc = new_doc("ALL (10.–12. klases saturs vienā gadā)", p.n)
    para(doc, "IZŅĒMUMA KLASE. Klasei ALL ir 3 fizikas stundas nedēļā "
              "(pārējām klasēm — 1), un vienā mācību gadā tiek apgūts viss "
              "10., 11. un 12. klases dabaszinību fizikas saturs — %d "
              "stundas, %d pārbaudes darbi. Stundas un pārbaudes darbi "
              "notiek TIKAI piektdienās — trīs mācību stundas "
              "pēc kārtas." % (p.n, len(p.pd)),
         size=9, bold=True, color=NAVY, after=4)
    para(doc, "Centralizētais eksāmens dabaszinībās šai klasei ir NĀKAMAJĀ "
              "mācību gadā, nevis 2027. gada maijā. Tāpēc mācību gads "
              "izmantots pilnībā — stundas notiek līdz maija beigām, un "
              "pēdējais pārbaudes darbs ir maija vidū (šajā plānā — %s). "
              "Saturs nav saīsināts: iekļauti visi triju klašu plānu temati "
              "un visas stundas, tostarp megapasaules pētīšana, atoma modeļu "
              "attīstība, šķidrumu plūsma, gravitācija un kosmiskie ātrumi, "
              "spēku shēmas un abu gadu noslēguma nostiprināšanas bloki. "
              "Kursa beigās ir trīs stundu bloks, kurā apkopo visu gadu un "
              "iezīmē, kas jāatkārto pirms nākamā gada eksāmena. Visi "
              "programmas temati un visas datu bukleta formulas "
              "saglabātas." % pedejais_pd,
         size=8.5, italic=True, color=GREY, after=8)

    kalendars(doc, p.pd)

    para(doc, "10. KLASES SATURS", size=11, bold=True, color=NAVY,
         before=10, after=2)
    temata_tabula(doc, "10.1. Pasaule ap mums un tās pētīšana (%d stundas)"
                  % len(a1),
                  "Matērija, mērogs, fizikālie lielumi un mērierīces — "
                  "pamats visam kursam.", a1)
    temata_tabula(doc, "10.3. Atoma uzbūve, vielas uzbūve, vielas stāvokļi "
                  "(%d stundas)" % len(a3),
                  "Atoma un kodola uzbūve, radioaktivitāte, vielas "
                  "daļiņveida uzbūve un kristālrežģi.", a3)
    temata_tabula(doc, "10.5. Materiālu veidi un īpašības (%d stundas)"
                  % len(a5),
                  "Materiālu fizikālās īpašības un to saistība ar uzbūvi.",
                  a5)
    temata_tabula(doc, "10. klases satura noslēgums (%d stundas)"
                  % len(a_nosl),
                  "Formatīvas nostiprināšanas stundas pirms pārejas uz "
                  "11. klases saturu. Jauns summatīvs vērtējums nav "
                  "paredzēts.", a_nosl)

    para(doc, "11. KLASES SATURS", size=11, bold=True, color=NAVY,
         before=10, after=2)
    temata_tabula(doc, "10.7. Cietu ķermeņu kustība un mijiedarbība "
                  "(%d stundas)" % (len(b7a) + len(b7b)),
                  "Kursa apjomīgākais aprēķinu temats. Divi pārbaudes darbi: "
                  "kustības apraksts un spēki.", b7a + b7b)
    temata_tabula(doc, "10.8. Šķidrumi dabā un tehnikā (%d stundas)"
                  % len(b8),
                  "Blīvums, spiediens un cēlējspēks.", b8)
    temata_tabula(doc, "10.9. Vides faktoru ietekme uz cilvēka organismu "
                  "(%d stundas)" % len(b9),
                  "Vides fizikālie faktori — troksnis, apgaismojums un "
                  "starojums; temata noslēguma pārbaudes darbs.", b9)
    temata_tabula(doc, "11. klases satura noslēgums (%d stundas)"
                  % len(b_nosl),
                  "Formatīvas nostiprināšanas stundas pirms pārejas uz "
                  "12. klases saturu. Jauns summatīvs vērtējums nav "
                  "paredzēts.", b_nosl)

    para(doc, "12. KLASES SATURS", size=11, bold=True, color=NAVY,
         before=10, after=2)
    temata_tabula(doc, "10.11. Visuma uzbūve un pētniecība (%d stundas)"
                  % len(c11),
                  "Astronomijas temats: Visuma uzbūve, attālumi, "
                  "gravitācija un kosmiskie ātrumi.", c11)
    temata_tabula(doc, "10.13. Viļņi dabā un tehnikā (%d stundas)"
                  % len(c13),
                  "Cieši saistīts ar eksāmena uzdevumiem par viļņiem un "
                  "starojumu.", c13)
    temata_tabula(doc, "10.14. un 10.15. Enerģija dabā un tehnikā; vides "
                  "tehnoloģijas (%d stundas)" % len(c15),
                  "Darbs, enerģija, jauda, elektroenerģija un tās pārvade.",
                  c15)
    temata_tabula(doc, "Kursa noslēgums un 10.16. temats (%d stundas)"
                  % len(eks), EKS_PIEZ, eks)

    para(doc, "Temati 10.2., 10.4., 10.6., 10.10. un 10.12. ir bioloģijas un "
              "ķīmijas daļā — fizikas stundās tos neapgūst.",
         size=8.5, italic=True, color=GREY, before=8)

    doc.save(path)
    return p


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = ("C:/aphysics/Dabaszinibas/"
           "Dabaszinības ALL klase - 10.-12. klases saturs vienā gadā.docx")
    p = build_all(out)
    print("ALL: %d stundas, %d PD  ->  %s"
          % (p.n, len(p.pd), os.path.basename(out)))
    for kods, tema, datums, _ in p.pd:
        print("      %-5s %-50s %s" % (kods, tema[:50], datums))
