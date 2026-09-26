# -*- coding: utf-8 -*-
"""3. klase, 166. stunda: «Kā uzbūvēt figūru pēc skatiem?»

Apgrieztais uzdevums iepriekšējai stundai: skati doti, figūra jāsaliek. Tas
ir grūtāk un arī vērtīgāk - tieši tā strādā katrs, kas būvē pēc rasējuma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā uzbūvēt figūru pēc skatiem?"

MERKIS = ("Veidosim figūru no kubiem, ja doti skati no augšas, priekšas un "
          "sāniem.")

SATURS = [
    Sakums("Vai pēc trim skatiem var uzbūvēt figūru?",
           zimejums=restis([["skats", "izmēri"],
                            ["no augšas", "3 x 2"],
                            ["no priekšas", "3 x 2"],
                            ["no sāniem", "2 x 2"]],
                           "trīs skati"),
           paraksts="No šiem skatiem sanāk kaste 3 x 2 x 2.",
           fakti=["Trīs skati dod visus trīs izmērus.",
                  "No tiem figūru var uzbūvēt, pašu figūru neredzot."]),

    Doma("Izlasi izmērus no skatiem",
         "Skats no augšas dod garumu un platumu, skats no priekšas - "
         "augstumu; ar to pietiek.",
         soli=[
             "No skata no augšas nolasi garumu un platumu.",
             "No skata no priekšas nolasi augstumu.",
             "Saliec apakšējo slāni pēc skata no augšas.",
             "Uzliec tik slāņu, cik pasaka augstums.",
         ],
         pieze="Ja skati nesader - piemēram, garums divos skatos ir "
               "dažāds -, figūru uzbūvēt nevar; kaut kur ir kļūda."),

    Petijums("Uzbūvē pēc skatiem",
             vajag="kubiņi un lapa ar skatiem",
             soli=[
                 "Nolasi izmērus no trim skatiem.",
                 "Saliec apakšējo slāni.",
                 "Uzliec pārējos slāņus.",
                 "Pārbaudi, vai uzbūvētā figūra tiešām izskatās tāpat no "
                 "visām trim pusēm.",
             ],
             secinajums="Ja visi trīs skati sakrīt, figūra ir uzbūvēta "
                        "pareizi."),

    Paraugs("Kāda figūra sanāks?",
            uzd="No augšas 3 x 2, no priekšas 3 x 2, no sāniem 2 x 2. Kāda "
                "figūra tā ir?",
            soli=[
                ("Garums 3, platums 2",
                 "No skata no augšas."),
                ("Augstums 2",
                 "No skata no priekšas."),
                ("Kaste 3 x 2 x 2",
                 "Tilpums: 3 · 2 · 2 = 12 kubi."),
            ],
            atbilde="kaste 3 x 2 x 2, 12 kubi"),

    Ievadi("Izlasi izmērus", [
        {"jaut": "No augšas 3 x 2, augstums 2. Cik kubu ir figūrā?",
         "atb": ["12"], "padoms": "3 · 2 · 2."},
        {"jaut": "No augšas 4 x 3, augstums 2. Cik kubu?", "atb": ["24"],
         "padoms": "12 · 2."},
        {"jaut": "No augšas 5 x 2, augstums 3. Cik kubu?", "atb": ["30"],
         "padoms": "10 · 3."},
        {"jaut": "Figūrā 24 kubi, apakšējā slānī 8. Cik slāņu ir?",
         "atb": ["3"], "padoms": "24 : 8."},
        {"jaut": "Figūrā 36 kubi, 3 slāņi. Cik kubu ir vienā slānī?",
         "atb": ["12"], "padoms": "36 : 3."},
        {"jaut": "Kubs 3 x 3 x 3. Cik kubiņu tajā ir?", "atb": ["27"],
         "padoms": "9 · 3."},
    ], pamats=4),

    Zimejums("Kad skati nesader",
             restis([["skats", "garums"],
                     ["no augšas", 3],
                     ["no priekšas", 4]],
                    "kļūda rasējumā"),
             paskaidro="Abos skatos garumam jābūt vienādam - ja nav, kaut "
                       "kur ir kļūda.",
             ievads="Pārbaude pirms būves."),

    Varianti("Ko rāda skati?", [
        {"jaut": "Kurš skats dod garumu un platumu?",
         "opcijas": ["No augšas", "No priekšas", "No sāniem", "Neviens"],
         "pareizi": 0, "padoms": "Skatās tieši uz leju."},
        {"jaut": "No augšas 4 x 3, augstums 2. Cik kubu ir figūrā?",
         "opcijas": ["24", "12", "9", "14"],
         "pareizi": 0, "padoms": "12 · 2."},
        {"jaut": "Ko nozīmē, ja garums divos skatos atšķiras?",
         "opcijas": ["Kaut kur ir kļūda", "Figūra ir sarežģīta",
                     "Jāņem lielākais", "Nekas"],
         "pareizi": 0, "padoms": "Viens ķermenis - viens garums."},
        {"jaut": "Ar ko sāk būvi?",
         "opcijas": ["Ar apakšējo slāni", "Ar augšējo slāni",
                     "Ar sāniem", "Vienalga"],
         "pareizi": 0, "padoms": "Pamats notur pārējos."},
    ], pamats=4),

    Pasaule("Kā uzbūvē pēc rasējuma?",
            Ievadi("", [
                {"jaut": "Detaļa 6 x 4 x 2 kubi. Cik kubu tajā ir?",
                 "atb": ["48"], "padoms": "24 · 2."},
                {"jaut": "Cik kubu ir vienā slānī?", "atb": ["24"],
                 "padoms": "6 · 4."},
                {"jaut": "Cik kubu vajag 5 tādām detaļām?", "atb": ["240"],
                 "padoms": "5 · 48."},
                {"jaut": "Noliktavā ir 200 kubi. Cik pilnu detaļu var "
                         "salikt?",
                 "atb": ["4"], "padoms": "200 : 48 ar atlikumu."},
            ]),
            pavediens="dati",
            konteksts="Programmā modeli apraksta ar skatiem, un printeris pēc "
                      "tiem izdrukā detaļu slāni pa slānim.",
            kapec="Ja skati nesader, printeris apstājas - tāpat kā tu ar "
                  "kubiņiem."),

    Kopsavilkums([
        "Veidoju figūru no kubiem pēc dotiem skatiem.",
        "Nolasu izmērus no trim skatiem.",
        "Būvēju slāni pa slānim.",
        "Pārbaudu, vai skati sader savā starpā.",
    ]),

    Majas([
        "Uzzīmē trīs skatus kādai figūrai un iedod tos mājiniekiem.",
        "Palūdz, lai viņi uzzīmē figūru pēc taviem skatiem.",
        "Salīdziniet rezultātu ar to, ko tu domāji.",
    ]),
]
