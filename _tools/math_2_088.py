# -*- coding: utf-8 -*-
"""2. klase, 88. stunda: «Kurš skaitlis der?»

Paņēmiens «mēģinu un pārbaudu»: izvēlas skaitli, ieliek □ vietā, pārbauda.
Ja par daudz - mēģina mazāku, ja par maz - lielāku. Tā atrod nezināmo arī
tad, ja pretējo darbību vēl neredz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti)

TEMA = "Kurš skaitlis der?"

MERKIS = ("Šodien noteiksim nezināmo darbības locekli ar paņēmienu «mēģinu "
          "un pārbaudu» un pamatosim izvēli.")

SATURS = [
    Sakums("Kā atrast □ vienādībā □ + 27 = 65, ja negribas rēķināt "
           "atņemšanu?",
           fakti=["Mēģini 30: 30 + 27 = 57 - par maz.",
                  "Mēģini 40: 40 + 27 = 67 - mazliet par daudz.",
                  "Mēģini 38: 38 + 27 = 65 - der!"]),

    Doma("Mēģinu un pārbaudu",
         "Izvēlies skaitli, pārbaudi un pielāgo nākamo mēģinājumu.",
         soli=[
             "Izvēlies apaļu skaitli, kas varētu derēt.",
             "Ieliec to □ vietā un aprēķini.",
             "Par daudz - ņem mazāku; par maz - lielāku.",
             "Kad der - atbilde atrasta.",
         ]),

    Paraugs("□ + 27 = 65",
            uzd="Atrodi □ ar mēģinājumiem.",
            soli=[("30 + 27 = 57", "Par maz par 8."),
                  ("38 + 27 = 65", "Der!")],
            atbilde="□ = 38"),

    Kustiba("Trāpi mērķī", [
        {"jaut": "□ + 27 = 65. Ieraksti □.", "atb": 38, "beigas": 60,
         "iedala": 10, "objekts": "bumba", "merkis": "□",
         "padoms": "65 − 27."},
        {"jaut": "□ − 15 = 30. Ieraksti □.", "atb": 45, "beigas": 60,
         "iedala": 10, "objekts": "bumba", "merkis": "□",
         "padoms": "30 + 15."},
        {"jaut": "70 − □ = 52. Ieraksti □.", "atb": 18, "beigas": 60,
         "iedala": 10, "objekts": "bumba", "merkis": "□",
         "padoms": "70 − 52."},
    ], ievads="Bumba aizripos tik tālu, cik ieraksti."),

    Varianti("Pārbaudi mēģinājumu", [
        {"jaut": "□ + 18 = 50. Mēģināja 30. Kas tālāk?",
         "opcijas": ["ņemt lielāku", "ņemt mazāku", "der"],
         "pareizi": 0, "padoms": "30 + 18 = 48 - par maz."},
        {"jaut": "□ − 20 = 25. Mēģināja 50. Kas tālāk?",
         "opcijas": ["ņemt mazāku", "ņemt lielāku", "der"],
         "pareizi": 0, "padoms": "50 − 20 = 30 - par daudz."},
    ]),

    Ievadi("Atrodi □", [
        {"jaut": "□ + 18 = 50", "atb": ["32"], "padoms": "Mēģini 32."},
        {"jaut": "□ − 20 = 25", "atb": ["45"], "padoms": "Mēģini 45."},
        {"jaut": "56 + □ = 80", "atb": ["24"], "padoms": "80 − 56."},
        {"jaut": "90 − □ = 64", "atb": ["26"], "padoms": "90 − 64."},
    ]),

    Pasaule("Cik svēra kaķis?",
            Ievadi("", [
                {"jaut": "Tētis ar kaķi uz svariem - 84 kg. Tētis bez kaķa - "
                         "79 kg. □ + 79 = 84. Cik kg sver kaķis?",
                 "atb": ["5"], "mers": "kg", "padoms": "84 − 79."},
            ]),
            pavediens="maja",
            konteksts="Kaķi nevar nosvērt vienu - tas nestāv mierā.",
            kapec="Nezināmais kļūst zināms ar vienu vienādību."),

    Kopsavilkums([
        "Atrodu □ ar paņēmienu «mēģinu un pārbaudu».",
        "Pielāgoju nākamo mēģinājumu.",
        "Pamatoju, kāpēc skaitlis der.",
    ]),

    Majas([
        "Iedomājies skaitli, pieskaiti 25 un pasaki rezultātu mājiniekam.",
        "Lai viņš atrod tavu skaitli.",
        "Tad otrādi.",
    ]),
]
