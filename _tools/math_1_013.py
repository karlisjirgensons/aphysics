# -*- coding: utf-8 -*-
"""1. klase, 13. stunda: «Kā pateikt tā, lai otrs uzzīmē to pašu?»

Figūru apraksta ar tās būtiskajām pazīmēm - stūru skaitu, lielumu rūtiņās,
novietojumu -, lai otrs to var uzzīmēt, neredzot. Pārī salīdzina: vai
sanāca tas pats?
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, figura)

TEMA = "Kā pateikt tā, lai otrs uzzīmē to pašu?"

MERKIS = ("Šodien aprakstīsim figūru tā, lai draugs to uzzīmē, neredzot.")

_KV3 = figura([(0, 0), (3, 0), (3, 3), (0, 3)])
_TS42 = figura([(0, 0), (4, 0), (4, 2), (0, 2)])
_TR = figura([(0, 0), (4, 0), (0, 3)])
_TR2 = figura([(0, 0), (4, 0), (2, 3)])

SATURS = [
    Sakums("Pasaki, bet neparādi!",
           zimejums=_TS42,
           paraksts="Četrstūris: 4 rūtiņas garš un 2 rūtiņas augsts.",
           fakti=["Pasaki, cik stūru.",
                  "Pasaki, cik rūtiņu gara katra mala.",
                  "Pēc tam salīdziniet zīmējumus."]),

    Doma("Labs apraksts",
         "Labs apraksts pasaka visu, kas vajadzīgs, lai uzzīmētu - un nekā "
         "lieka.",
         soli=[
             "Nosauc figūru: cik stūru.",
             "Pasaki malu garumu rūtiņās.",
             "Pasaki, kur sākt: piemēram, lapas kreisajā stūrī.",
         ],
         pieze="Krāsa ir skaista, bet zīmēšanai svarīgāki ir stūri un "
               "malas."),

    Varianti("Kurš apraksts der?", [
        {"jaut": "Kurš apraksts der šai figūrai?", "zim": _KV3,
         "opcijas": ["4 stūri, visas malas 3 rūtiņas",
                     "3 stūri, malas 3 rūtiņas",
                     "4 stūri, 4 un 2 rūtiņas"],
         "pareizi": 0, "padoms": "Saskaiti rūtiņas katrā malā."},
        {"jaut": "Kurš apraksts der šai figūrai?", "zim": _TS42,
         "opcijas": ["4 stūri, garums 4, augstums 2 rūtiņas",
                     "4 stūri, visas malas 4 rūtiņas",
                     "3 stūri, garums 4 rūtiņas"],
         "pareizi": 0, "padoms": "Garums un augstums atšķiras."},
        {"jaut": "Kurš apraksts der šai figūrai?", "zim": _TR,
         "opcijas": ["3 stūri, apakšā 4, sānā 3 rūtiņas",
                     "4 stūri, apakšā 4 rūtiņas",
                     "3 stūri, visas malas vienādas"],
         "pareizi": 0, "padoms": "Viena mala stāv taisni uz augšu."},
    ]),

    Varianti("Kas pietrūkst aprakstā?", [
        {"jaut": "«Uzzīmē trijstūri.» Vai draugs uzzīmēs tieši šo?",
         "zim": _TR2,
         "opcijas": ["Nē, nav pateikts izmērs", "Jā, noteikti"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Trijstūru ir ļoti dažādu."},
        {"jaut": "«Uzzīmē violetu četrstūri.» Kas ir lieks?",
         "opcijas": ["krāsa", "stūru skaits"], "jaukt": False,
         "pareizi": 0, "padoms": "Formu krāsa nemaina."},
    ]),

    Petijums("Spēle pārī", [
        "Viens uzzīmē figūru rūtiņās un to neparāda.",
        "Viņš apraksta figūru: stūri, malas, kur sākt.",
        "Otrs zīmē pēc apraksta.",
        "Salīdziniet! Ja atšķiras - ko aprakstā vajadzēja pateikt?",
    ], vajag="2 rūtiņu lapas, zīmulis"),

    Pasaule("Ceļa zīme pa telefonu",
            Varianti("", [
                {"jaut": "Tu stāsti draugam par zīmi «STOP». Kas ir svarīgi?",
                 "opcijas": ["8 stūri un uzraksts STOP",
                             "ka tā ir pie veikala",
                             "ka tā ir skaista"],
                 "pareizi": 0, "padoms": "Forma un uzraksts."},
            ]),
            pavediens="celojums",
            konteksts="Draugs nevar redzēt zīmi - tikai dzirdēt tavu "
                      "aprakstu.",
            kapec="Precīzs apraksts ļauj otram uzzīmēt to pašu."),

    Kopsavilkums([
        "Aprakstu figūru ar stūriem un malu garumiem.",
        "Zīmēju pēc drauga apraksta.",
        "Pamanu, kas aprakstā pietrūkst.",
    ]),

    Majas([
        "Apraksti mājiniekam savu logu - lai viņš to uzzīmē.",
        "Uzzīmē figūru pēc mājinieka apraksta.",
        "Kas aprakstā bija visgrūtāk?",
    ]),
]
