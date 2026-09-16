# -*- coding: utf-8 -*-
"""Dabaszinības (fizikas daļa). ĀT1 — Matērija, mērogi un mērvienības.

Ātrais tests pirms PD1 «Pasaule ap mums un tās pētīšana» (1.1.-1.5.
stunda). Jautājumi neatkārto PD1 abu variantu testa daļu.
"""

AT = {
    "nr": 1,
    "nosaukums": "Matērija, mērogi un mērvienības",
    "mape": "1. Pasaule ap mums un tās pētīšana",
    "fails": "ĀT1. Matērija, mērogi un mērvienības",
    "stundas": "1.1.-1.5.",
    "datums": "16.09.2026.",
    "laiks": 15,
    "apraksts": "Ātrais tests pirms temata pārbaudes darba. Pārbauda "
                "matērijas jēdzienu, pasaules mērogus, mērvienību priedēkļus "
                "un standartformu, mikroskopa palielinājumu un patiesā "
                "izmēra aprēķinu, mērierīces izvēli un mērījuma kļūdu.",
    "atgadne": [
        "Priedēkļi:  k = 10³  ·  M = 10⁶  ·  c = 10⁻²  ·  m = 10⁻³  ·  "
        "µ = 10⁻⁶  ·  n = 10⁻⁹   ·   1 t = 10³ kg",
        "Γ = Γ(objektīva) · Γ(okulāra)   ·   patiesais izmērs = attēla "
        "izmērs / Γ   ·   R = Δx / x · 100 %",
    ],
    "struktura": [
        ("1., 2.", "Skaidro matēriju kā vielu un lauku; atpazīst lauka "
                   "piemērus", "1.1."),
        ("3.", "Sakārto objektus pēc mēroga un saista tos ar pasaules "
               "organizācijas līmeņiem", "1.2."),
        ("4.-6.", "Lieto mērvienību priedēkļus, standartformu un pārvērš "
                  "lielumus SI vienībās", "1.3."),
        ("7., 8.", "Aprēķina mikroskopa palielinājumu un objekta patieso "
                   "izmēru", "1.4."),
        ("9.-12.", "Izvēlas piemērotu mērierīci, nosaka absolūto un relatīvo "
                   "kļūdu un lasa pierakstu x = (x ± Δx)", "1.5."),
    ],
    "jautajumi": [
        ("Kas fizikā ir matērija?",
         ["tikai vielas, no kurām sastāv ķermeņi",
          "viss, kas pastāv objektīvi: gan viela, gan lauks",
          "tikai cietas vielas",
          "enerģijas mērvienība"], 1),

        ("Kurš no minētajiem ir lauka piemērs?",
         ["gaiss", "ūdens piliens", "magnētiskais lauks",
          "stikla plāksne"], 2),

        ("Kurā rindā objekti sakārtoti no mazākā uz lielāko?",
         ["atoms, molekula, asins šūna, matu diametrs",
          "molekula, atoms, asins šūna, matu diametrs",
          "atoms, asins šūna, molekula, matu diametrs",
          "asins šūna, atoms, molekula, matu diametrs"], 0),

        ("Kā standartformā metros pieraksta 2,5 mm?",
         ["2,5 · 10⁻² m", "25 · 10⁻² m", "2,5 · 10³ m",
          "2,5 · 10⁻³ m"], 3),

        ("Cik reižu 1 µm ir lielāks par 1 nm?",
         ["10 reižu", "1000 reižu", "100 reižu",
          "tās ir vienādas mērvienības"], 1),

        ("Cik kilogramu ir 2,4 t?",
         ["24 kg", "240 kg", "2400 kg", "0,0024 kg"], 2),

        ("Mikroskopa objektīva palielinājums ir 40×, okulāra — 10×. Cik "
         "liels ir kopējais palielinājums?",
         ["4×", "50×", "4000×", "400×"], 3),

        ("Mikroskopā šūnas attēla garums ir 4 mm, palielinājums — 200×. Cik "
         "liels ir šūnas patiesais garums?",
         ["0,02 mm", "0,2 mm", "50 mm", "800 mm"], 0),

        ("Ar kuru mērierīci visprecīzāk izmērīs monētas biezumu?",
         ["ar mērlenti", "ar bīdmēru", "ar lineālu, kura iedaļas ir 1 cm",
          "ar mērcilindru"], 1),

        ("Mērījuma rezultāts pierakstīts kā l = (12,4 ± 0,1) cm. Ko nozīmē "
         "0,1 cm?",
         ["relatīvo kļūdu", "vidējo vērtību", "mērīto garumu",
          "absolūto kļūdu"], 3),

        ("Cik liela ir relatīvā kļūda mērījumam l = (20,0 ± 0,5) cm?",
         ["0,5 %", "5 %", "2,5 %", "25 %"], 2),

        ("Ar kuru mērierīci visprecīzāk izmērīs apmēram 25 ml šķidruma "
         "tilpumu?",
         ["ar mērcilindru, kura iedaļa ir 1 ml",
          "ar mērglāzi, kuras iedaļa ir 50 ml",
          "ar virtuves karoti",
          "ar mērlenti"], 0),
    ],
}
