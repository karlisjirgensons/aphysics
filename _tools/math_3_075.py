# -*- coding: utf-8 -*-
"""3. klase, 75. stunda: «Kur uz lineāla ir desmitdaļas?»

Lineāls ir daļskaitļu modelis, kas jau ir katra skolēna penālī: centimetrs
sadalīts desmit vienādās daļās, un viena no tām ir milimetrs. Tieši no šī
modeļa 97. stundā izaugs decimāldaļa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala, taisne)

TEMA = "Kur uz lineāla ir desmitdaļas?"

MERKIS = ("Parādīsim, ka 1 cm ir sadalīts 10 vienādās daļās, un nosauksim "
          "vienu daļu.")

SATURS = [
    Sakums("Cik mazu iedaļu ir starp diviem cipariem uz lineāla?",
           zimejums=dala(10, 1, "1/10", "centimetrs sadalīts desmit daļās"),
           paraksts="Viena mazā iedaļa ir viena desmitdaļa no centimetra.",
           fakti=["Starp diviem cipariem uz lineāla ir 10 mazas iedaļas.",
                  "Viena mazā iedaļa ir 1 mm jeb {1|10} cm."]),

    Doma("Milimetrs ir centimetra desmitdaļa",
         "1 cm = 10 mm, tāpēc viens milimetrs ir {1|10} no centimetra.",
         soli=[
             "Atrodi uz lineāla divus blakus ciparus.",
             "Saskaiti mazās iedaļas starp tiem - to ir 10.",
             "Viena iedaļa ir {1|10} cm jeb 1 mm.",
             "Piecas iedaļas ir {5|10} cm jeb puse centimetra.",
         ],
         pieze="Tieši tāpēc {5|10} un {1|2} ir viens un tas pats: puse "
               "centimetra ir 5 mm."),

    Petijums("Atrodi desmitdaļas uz lineāla",
             vajag="lineāls un zīmulis",
             soli=[
                 "Atrodi uz lineāla atzīmi 3 cm.",
                 "Saskaiti mazās iedaļas līdz 4 cm.",
                 "Uzzīmē nogriezni, kas ir 3 cm un vēl 7 mazās iedaļas.",
                 "Pieraksti tā garumu milimetros.",
             ],
             secinajums="3 cm 7 mm ir 37 mm - tāpēc garumu vienmēr var "
                        "izteikt vienā mērvienībā."),

    Paraugs("Cik ir 2 cm un 4 iedaļas?",
            uzd="Nogrieznis ir 2 cm un vēl 4 mazās iedaļas. Cik milimetru "
                "tas ir?",
            soli=[
                ("2 cm = 20 mm",
                 "Katrā centimetrā ir 10 milimetru."),
                ("4 iedaļas = 4 mm",
                 "Viena iedaļa ir viens milimetrs."),
                ("20 + 4 = 24",
                 "Nogrieznis ir 24 mm garš."),
            ],
            atbilde="24 mm"),

    Ievadi("Lasi lineālu", [
        {"jaut": "Cik milimetru ir 3 cm?", "atb": ["30"],
         "padoms": "3 · 10."},
        {"jaut": "Cik milimetru ir 2 cm 5 mm?", "atb": ["25"],
         "padoms": "20 + 5."},
        {"jaut": "Cik centimetru ir 40 mm?", "atb": ["4"],
         "padoms": "40 : 10."},
        {"jaut": "Cik milimetru ir {1|2} cm?", "atb": ["5"],
         "padoms": "Puse no 10."},
        {"jaut": "Cik milimetru ir {3|10} cm?", "atb": ["3"],
         "padoms": "Trīs desmitdaļas ir trīs milimetri."},
        {"jaut": "Cik milimetru ir 7 cm 8 mm?", "atb": ["78"],
         "padoms": "70 + 8."},
    ], pamats=4),

    Zimejums("Puse centimetra",
             dala(10, 5, "5/10 = 1/2", "pieci milimetri no desmit"),
             paskaidro="Piecas desmitdaļas aizpilda tieši pusi - tāpēc abi "
                       "pieraksti nozīmē vienu un to pašu.",
             ievads="Iekrāsotas ir piecas desmitdaļas."),

    Varianti("Ko rāda iedaļa?", [
        {"jaut": "Cik mazu iedaļu ir vienā centimetrā?",
         "opcijas": ["10", "5", "100", "2"],
         "pareizi": 0, "padoms": "Tik, cik milimetru."},
        {"jaut": "Kāda daļa no centimetra ir viens milimetrs?",
         "opcijas": ["{1|10}", "{1|2}", "{1|100}", "{1|5}"],
         "pareizi": 0, "padoms": "Viena no desmit vienādām daļām."},
        {"jaut": "Cik milimetru ir {1|2} cm?",
         "opcijas": ["5 mm", "2 mm", "10 mm", "50 mm"],
         "pareizi": 0, "padoms": "Puse no 10 mm."},
        {"jaut": "Nogrieznis ir 56 mm. Cik tas ir centimetros un "
                 "milimetros?",
         "opcijas": ["5 cm 6 mm", "56 cm", "6 cm 5 mm", "5 cm 60 mm"],
         "pareizi": 0, "padoms": "50 mm ir 5 cm."},
    ], pamats=4),

    Pasaule("Cik precīzi jāgriež mīkla?",
            Ievadi("", [
                {"jaut": "Mīklas kārtai jābūt 5 mm biezai. Cik centimetru "
                         "tas ir? Raksti ar komatu.",
                 "atb": ["0,5", "0.5"], "padoms": "Puse centimetra."},
                {"jaut": "Cepums ir 4 cm plats. Cik milimetru tas ir?",
                 "atb": ["40"], "padoms": "4 · 10."},
                {"jaut": "Starp cepumiem jāatstāj 25 mm. Cik centimetru tas "
                         "ir? Raksti ar komatu.",
                 "atb": ["2,5", "2.5"], "padoms": "20 mm ir 2 cm."},
                {"jaut": "Uz plāksnes rindā ir 6 cepumi pa 40 mm. Cik "
                         "milimetru tie aizņem?",
                 "atb": ["240"], "padoms": "6 · 40."},
            ]),
            pavediens="virtuve",
            konteksts="Receptēs biezumu raksta milimetros - tā ir "
                      "centimetra desmitdaļa, ko var izmērīt ar lineālu.",
            kapec="Desmitdaļas ļauj būt precīzākam, nekā to atļauj veseli "
                  "centimetri."),

    Kopsavilkums([
        "Zinu, ka 1 cm ir sadalīts 10 vienādās daļās.",
        "Nosaucu vienu daļu: {1|10} cm jeb 1 mm.",
        "Pārvēršu centimetrus milimetros un otrādi.",
        "Zinu, ka {5|10} ir tas pats, kas {1|2}.",
    ]),

    Majas([
        "Izmēri piecus mājas priekšmetus milimetros.",
        "Uzzīmē nogriezni, kas ir 6 cm 4 mm garš.",
        "Atrodi lineālā atzīmi, kas ir tieši puse centimetra.",
    ]),
]
