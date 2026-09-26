# -*- coding: utf-8 -*-
"""2. klase, 11. stunda: «Ar ko mērīsi stadionu un ar ko - grāmatu?»

Mērinstruments jāizvēlas pēc tā, ko mēra: lineāls der grāmatai, mērlente -
cilvēka augumam, mērrats vai rulete - stadionam. Līdz ar instrumentu izvēlas
arī mērvienību - centimetrus vai metrus.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, lineals)

TEMA = "Ar ko mērīsi stadionu un ar ko - grāmatu?"

MERKIS = ("Šodien izvēlēsimies garumam piemērotu mērinstrumentu un "
          "mērvienību un pamatosim izvēli.")

_CM_M = ["centimetros", "metros"]

SATURS = [
    Sakums("Cik reižu jāpārliek lineāls, lai izmērītu futbola laukumu?",
           zimejums=lineals(10),
           paraksts="Skolas lineāls ir tikai 20 vai 30 cm garš.",
           fakti=["Futbola laukums ir apmēram 100 m garš.",
                  "Ar 20 cm lineālu tas būtu jāpārliek 500 reižu!",
                  "Tāpēc garam attālumam ņem garu instrumentu."]),

    Doma("Instruments pēc garuma",
         "Īsu lietu mēra ar lineālu centimetros, garu - ar mērlenti vai "
         "ruleti metros.",
         soli=[
             "Novērtē: vai tas ir īsāks par lineālu vai garāks?",
             "Īss - lineāls, mērvienība cm.",
             "Garāks par metru - mērlente vai rulete, mērvienība m.",
             "Rezultātu raksta ar mērvienību: 25 cm, 40 m.",
         ],
         pieze="Skaitlis bez mērvienības neko nepasaka: «5» var būt 5 cm "
               "vai 5 m."),

    Varianti("Ko ņemsi?", [
        {"jaut": "Grāmatas garums",
         "opcijas": ["lineāls", "rulete", "mērrats"], "pareizi": 0,
         "padoms": "Grāmata ir īsāka par lineālu."},
        {"jaut": "Skolas stadiona garums",
         "opcijas": ["mērrats vai garā rulete", "lineāls", "zīmulis"],
         "pareizi": 0, "padoms": "Stadions ir ļoti garš."},
        {"jaut": "Tava auguma garums",
         "opcijas": ["mērlente", "lineāls", "mērrats"], "pareizi": 0,
         "padoms": "Mērlente ir mīksta un pietiekami gara."},
        {"jaut": "Dzēšgumijas garums",
         "opcijas": ["lineāls", "mērlente", "rulete"], "pareizi": 0,
         "padoms": "Mazu lietu mēra ar lineālu."},
        {"jaut": "Klases garums",
         "opcijas": ["rulete", "lineāls", "zīmulis"], "pareizi": 0,
         "padoms": "Klase ir vairākus metrus gara."},
        {"jaut": "Galvas apkārtmērs cepurei",
         "opcijas": ["mērlente", "lineāls", "mērrats"], "pareizi": 0,
         "padoms": "Apkārt galvai liecas tikai mīksta lente."},
    ], pamats=4),

    Varianti("Kurā mērvienībā?", [
        {"jaut": "Zīmuļa garums", "opcijas": _CM_M, "jaukt": False,
         "pareizi": 0, "padoms": "Zīmulis ir īss."},
        {"jaut": "Peldbaseina garums", "opcijas": _CM_M, "jaukt": False,
         "pareizi": 1, "padoms": "Baseins ir 25 vai 50 m garš."},
        {"jaut": "Tava plaukstas platums", "opcijas": _CM_M,
         "jaukt": False, "pareizi": 0, "padoms": "Plauksta ir šaura."},
        {"jaut": "Attālums līdz skolas vārtiem", "opcijas": _CM_M,
         "jaukt": False, "pareizi": 1, "padoms": "Tas ir tālu."},
    ]),

    Varianti("Vai ticams?", [
        {"jaut": "Grāmata ir 25 m gara.",
         "opcijas": ["Neticams - jābūt 25 cm", "Ticams"], "jaukt": False,
         "pareizi": 0, "padoms": "25 m ir garāk nekā klase."},
        {"jaut": "Skolas koridors ir 40 m garš.",
         "opcijas": ["Neticams", "Ticams"], "jaukt": False, "pareizi": 1,
         "padoms": "Koridors var būt garš."},
    ]),

    Pasaule("Kā sagatavot sporta dienu?",
            Varianti("", [
                {"jaut": "Jāatzīmē 60 m skrējiena celiņš. Ko ņemsi?",
                 "opcijas": ["garo ruleti", "lineālu", "mērlenti no "
                             "šūšanas kastes"], "pareizi": 0,
                 "padoms": "60 m - ļoti garš."},
                {"jaut": "Tāllēkšanas rezultātus raksta centimetros vai "
                         "metros un centimetros. Kāpēc ne tikai metros?",
                 "opcijas": ["Lēcieni atšķiras par dažiem centimetriem",
                             "Metru nav", "Tā ir ātrāk"], "pareizi": 0,
                 "padoms": "Uzvar tas, kurš aizlēca kaut par 1 cm tālāk."},
            ]),
            pavediens="sports",
            konteksts="Skolotājam jāsagatavo skrējiena celiņš un "
                      "tāllēkšanas bedre.",
            kapec="Pareizs instruments ietaupa laiku un dod precīzu "
                  "rezultātu."),

    Kopsavilkums([
        "Izvēlos mērinstrumentu pēc tā, cik garš ir priekšmets.",
        "Īsas lietas mēru centimetros, garas - metros.",
        "Rakstu rezultātu ar mērvienību.",
    ]),

    Majas([
        "Atrodi mājās mērinstrumentus: lineālu, mērlenti, ruleti.",
        "Ar katru izmēri vienu piemērotu lietu.",
        "Pieraksti rezultātus ar mērvienību.",
    ]),
]
