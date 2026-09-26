# -*- coding: utf-8 -*-
"""7. klase, 75. stunda: «Kā konstruēt vienādu leņķi?»

Konstrukcijā lieto tikai cirkuli un lineālu (bez iedaļām). Vienādu leņķi
konstruē, pārnesot loka «atvērumu»: ar vienu un to pašu rādiusu un to pašu
hordu. Stunda iemāca soļus un to pamatojumu.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā konstruēt vienādu leņķi?"

MERKIS = ("Ar cirkuli un lineālu konstruēsim leņķi, kas vienāds ar doto.")


def _solis(n):
    """Konstrukcija pa soļiem: dotais leņķis A un jaunais pie O."""
    p = [("A", 0, 0), ("_B", 4, 0), ("_C", 2.4, 2.4),
         ("O", 7, 0), ("_D", 11, 0)]
    nog, izc, stari = [("A", "_B"), ("A", "_C")], [], [("O", "_D")]
    lenki = [(("_B", "A", "_C"), "α")]
    if n >= 2:
        p += [("M", 2.5, 0, -60), ("N", 1.77, 1.77, 135)]
        izc += [("M", "N")]
    if n >= 3:
        p += [("K", 9.5, 0, -60)]
    if n >= 4:
        p += [("L", 8.77, 1.77, 135)]
        izc += [("K", "L")]
    if n >= 5:
        stari += [("O", "L")]
        lenki += [(("_D", "O", "L"), "α")]
    return geometrija(p, nogriezni=nog, stari=stari, izcelti=izc,
                      lenki=lenki)


SATURS = [
    Sakums("Bez transportiera - tikai cirkulis",
           zimejums=_solis(5),
           paraksts="Leņķis pie O ir tieši tāds pats kā pie A.",
           fakti=["Senie grieķi konstruēja tikai ar cirkuli un lineālu.",
                  "Transportieris mēra aptuveni, konstrukcija - precīzi.",
                  "Leņķi pārnes kā «vienādu trijstūri»."]),

    Doma("Pārnes rādiusu un hordu",
         "Lai konstruētu leņķi, kas vienāds ar doto, ar vienu un to pašu "
         "cirkuļa atvērumu novelk lokus abās virsotnēs un pārnes attālumu "
         "starp loka krustpunktiem.",
         soli=[
             "No A novelc loku - tas krusto leņķa malas M un N.",
             "Ar to pašu rādiusu no O novelc loku - tas krusto staru K.",
             "Ar cirkuli izmēri MN.",
             "No K ar rādiusu MN novelc loku - krustpunkts L.",
             "Novelc staru OL: ∠KOL = ∠MAN.",
         ],
         pieze="Pamatojums: △AMN un △OKL ir vienādas visas trīs malas, "
               "tāpēc arī leņķi A un O ir vienādi (pazīme mmm)."),

    Slidnis("Soli pa solim", [
        {"v": "1. solis", "teksts": "Dots leņķis α un stars no O.",
         "zim": _solis(1)},
        {"v": "2. solis", "teksts": "Loks no A: punkti M un N.", "zim": _solis(2)},
        {"v": "3. solis", "teksts": "Tāds pats loks no O: punkts K.",
         "zim": _solis(3)},
        {"v": "4. solis", "teksts": "No K rādiuss MN: punkts L.", "zim": _solis(4)},
        {"v": "5. solis", "teksts": "Stars OL - gatavs.", "zim": _solis(5)},
    ]),

    Paraugs("Kāpēc tas strādā?",
            uzd="Pamato, ka ∠KOL = ∠MAN.",
            soli=[
                ("AM = OK, AN = OL", "(viens cirkuļa atvērums)"),
                ("MN = KL", "(pārnests ar cirkuli)"),
                ("△AMN = △OKL", "(trīs malas - pazīme mmm)"),
                ("∠MAN = ∠KOL", "(atbilstošie leņķi)"),
            ],
            atbilde="Leņķi vienādi, jo trijstūri vienādi."),

    Varianti("Konstrukcijas noteikumi", [
        {"jaut": "Kādus rīkus drīkst lietot konstrukcijā?",
         "opcijas": ["Cirkuli un lineālu bez mērīšanas",
                     "Transportieri", "Kalkulatoru", "Jebkurus"],
         "pareizi": 0, "padoms": "Tā ir klasiskā konstrukcija."},
        {"jaut": "Kas notiks, ja otrajā solī paņems citu rādiusu?",
         "opcijas": ["Leņķis sanāks nepareizs",
                     "Nekas - leņķis vienāds",
                     "Leņķis būs divreiz lielāks",
                     "Konstrukcija nav iespējama"],
         "pareizi": 0, "padoms": "Rādiusiem jāsakrīt."},
        {"jaut": "Kurš solis «pārnes» leņķa atvērumu?",
         "opcijas": ["Horda MN pārnesta uz KL", "Pirmais loks",
                     "Stara novilkšana", "Neviens"],
         "pareizi": 0, "padoms": "Attālums starp malām."},
    ]),

    Petijums("Konstruē pats",
             ["Uzzīmē jebkuru leņķi un staru blakus.",
              "Izpildi konstrukcijas 5 soļus.",
              "Izmēri abus leņķus ar transportieri.",
              "Salīdzini: cik grādu starpība?"],
             vajag="cirkulis, lineāls, transportieris",
             secinajums="Ja konstruēts rūpīgi, starpība nav lielāka par 1° - "
                         "tā ir mērīšanas neprecizitāte."),

    Pasaule("Galdnieka leņķa pārnesējs",
            Varianti("", [
                {"jaut": "Galdniekam jāpārnes sienas stūra leņķis uz dēli. "
                         "Kurš rīks dara to pašu, ko konstrukcija?",
                 "opcijas": ["Bīdāmais leņķmērs (malka)", "Zāģis",
                             "Āmurs", "Svari"],
                 "pareizi": 0, "padoms": "Tas «nokopē» leņķi."},
                {"jaut": "Kāpēc galdnieks nemēra grādos?",
                 "opcijas": ["Pārnesot ir precīzāk un ātrāk",
                             "Grādi neeksistē", "Tas ir aizliegts",
                             "Viņš nezina skaitļus"],
                 "pareizi": 0, "padoms": "Nav starpmērījuma kļūdas."},
                {"jaut": "Ja siena nav precīzi 90°, ko dos pārnešana?",
                 "opcijas": ["Tieši sienas īsto leņķi",
                             "Vienmēr 90°", "Nepareizu leņķi",
                             "Nekā"],
                 "pareizi": 0, "padoms": "Nokopē to, kas ir."},
            ]),
            pavediens="maja",
            konteksts="Vecās mājās stūri reti ir taisni - leņķi pārnes, "
                      "nevis mēra.",
            kapec="Konstrukcija ir kopēšana bez skaitļiem."),

    Kopsavilkums([
        "Konstruēju leņķi, vienādu ar doto.",
        "Lietoju tikai cirkuli un lineālu.",
        "Pamatoju konstrukciju ar trijstūru vienādību.",
        "Pārbaudu rezultātu ar transportieri.",
    ]),

    Majas([
        "Konstruē leņķi, vienādu ar tavas grāmatas stūra leņķi.",
        "Konstruē leņķi, divreiz lielāku par doto.",
        "Uzraksti konstrukcijas soļus saviem vārdiem.",
    ]),
]
