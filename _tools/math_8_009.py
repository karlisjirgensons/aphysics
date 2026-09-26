# -*- coding: utf-8 -*-
"""8. klase, 9. stunda: «Kad vidējais maldina?»

Viena ļoti liela vai ļoti maza vērtība (novirze) pavelk vidējo sev līdzi,
bet mediānu gandrīz nemaina. Slīdnis pievieno vienu lielu algu un rāda, kā
abi rādītāji uz to reaģē. Tā sapratīs, kāpēc algas ziņās raksta mediānu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, kolonnas)

TEMA = "Kad vidējais maldina?"

MERKIS = ("Salīdzināsim aritmētisko vidējo un mediānu datu kopā ar "
          "novirzēm.")

_ALGAS = [("A", 1100), ("B", 1200), ("C", 1300), ("D", 1300), ("E", 1400)]

SATURS = [
    Sakums("«Mūsu uzņēmumā vidējā alga ir 3000 €!»",
           zimejums=kolonnas(_ALGAS + [("vadītājs", 11700)], " €"),
           paraksts="Pieci darbinieki un vadītājs - mēneša algas.",
           fakti=["Neviens darbinieks nesaņem ne tuvu 3000 €.",
                  "Vidējo uzpūš viena liela alga.",
                  "Mediāna - 1300 € - parāda parasto algu."]),

    Slidnis("Pievieno vienu lielu algu", [
        {"v": "5 darbinieki", "teksts": "Vidējais 1260 €, mediāna 1300 €",
         "zim": kolonnas(_ALGAS)},
        {"v": "+ vadītājs 11 700 €",
         "teksts": "Vidējais 3000 €, mediāna 1300 €",
         "zim": kolonnas(_ALGAS + [("vad.", 11700)])},
    ], ievads="Viena vērtība pavelk vidējo, mediāna paliek vietā."),

    Doma("Novirze un tās ietekme",
         "Novirze ir vērtība, kas krasi atšķiras no pārējām. Tā stipri maina "
         "aritmētisko vidējo, bet mediānu - maz vai nemaz.",
         soli=[
             "Sakārto datus un paskaties uz abiem galiem.",
             "Ja kāda vērtība ir krasi lielāka vai mazāka - tā ir novirze.",
             "Aprēķini gan vidējo, gan mediānu.",
             "Ja tie stipri atšķiras - «parasto» vērtību labāk rāda mediāna.",
         ],
         pieze="Tāpēc Latvijas Centrālā statistikas pārvalde līdzās vidējai "
               "algai publicē arī algu mediānu."),

    Ievadi("Salīdzini abus rādītājus", [
        {"jaut": "2, 3, 3, 4, 38. Vidējais?",
         "atb": ["10"], "padoms": "50 : 5."},
        {"jaut": "Tai pašai kopai - mediāna?",
         "atb": ["3"], "padoms": "Trešā vērtība."},
        {"jaut": "Bez 38: 2, 3, 3, 4. Vidējais?",
         "atb": ["3"], "padoms": "12 : 4."},
        {"jaut": "Laiki (min): 12, 14, 13, 15, 46. Par cik vidējais "
                 "lielāks par mediānu?",
         "atb": ["6"], "padoms": "Vidējais 20, mediāna 14."},
    ]),

    Varianti("Kuru rādītāju ziņot?", [
        {"jaut": "Mājas cenas ciemā, kur viena ir pils par 5 milj. €.",
         "opcijas": ["Mediānu", "Vidējo", "Amplitūdu", "Lielāko vērtību"],
         "pareizi": 0, "padoms": "Pils ir novirze."},
        {"jaut": "Klases vidējā atzīme, ja atzīmes ir 6-9 bez novirzēm.",
         "opcijas": ["Der abi - tie būs tuvu", "Tikai mediāna",
                     "Tikai moda", "Neviens"],
         "pareizi": 0, "padoms": "Bez novirzēm tie sakrīt aptuveni."},
        {"jaut": "Kāpēc reklāmā mīl rakstīt «vidēji»?",
         "opcijas": ["Viena liela vērtība var to uzpūst",
                     "Tas vienmēr ir precīzāk",
                     "Mediānu nav iespējams aprēķināt",
                     "Tā prasa likums"],
         "pareizi": 0, "padoms": "Novirze pavelk vidējo."},
    ]),

    Pasaule("Algu sludinājums",
            Ievadi("", [
                {"jaut": "Kafejnīcā algas (€): 900, 950, 1000, 1000, 1050, "
                         "4100. Kāds ir vidējais?",
                 "atb": ["1500"], "padoms": "9000 : 6."},
                {"jaut": "Kāda ir mediāna?",
                 "atb": ["1000"], "padoms": "(1000 + 1000) : 2."},
                {"jaut": "Cik darbinieku no sešiem pelna vairāk par "
                         "vidējo?",
                 "atb": ["1"], "padoms": "Tikai 4100."},
            ]),
            pavediens="dati",
            konteksts="Darba sludinājumā «vidējā alga 1500 €» izklausās labi, "
                      "bet pieci no sešiem pelna ap 1000 €.",
            kapec="Pajautā mediānu - tā ir godīgāka."),

    Kopsavilkums([
        "Atpazīstu novirzi datu kopā.",
        "Saprotu, ka novirze stipri maina vidējo, bet mediānu - maz.",
        "Izvēlos godīgāko rādītāju situācijai.",
    ]),

    Majas([
        "Atrodi ziņās «vidējo» un pārdomā, vai tur varētu būt novirzes.",
        "Izdomā 5 skaitļus, kuru vidējais ir 20, bet mediāna 5.",
        "Paskaidro ģimenei, kāpēc vidējā alga var maldināt.",
    ]),
]
