# -*- coding: utf-8 -*-
"""8. klase, 12. stunda: «Kā savākt un apstrādāt datus?»

Datu vākšana ar īstu mērījumu - reakcijas laika eksperimentu ar lineālu.
Datus sagrupē intervālos, saskaita biežumus un attēlo stabiņos. Tā ir tā
pati ķēde, ko skolēns izies ar sava pētījuma datiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, kolonnas,
                         restis)

TEMA = "Kā savākt un apstrādāt datus?"

MERKIS = ("Iegūsim datus, apstrādāsim tos un attēlosim uzskatāmi.")

_GRUPAS = [("5-9", 3), ("10-14", 8), ("15-19", 11), ("20-24", 6),
           ("25-29", 2)]

SATURS = [
    Sakums("Cik ātri tu noķer krītošu lineālu?",
           zimejums=kolonnas(_GRUPAS),
           paraksts="30 skolēnu rezultāti: cik cm lineāls paspēja nokrist.",
           fakti=["Jo mazāk centimetru, jo ātrāka reakcija.",
                  "30 dažādus skaitļus grūti aptvert - grupas palīdz.",
                  "Visbiežāk - no 15 līdz 19 cm."]),

    Doma("No mērījuma līdz diagrammai",
         "Neapstrādāti dati ir garš skaitļu saraksts. Lai tos saprastu, tos "
         "sakārto, sagrupē un attēlo.",
         soli=[
             "Pieraksti katru mērījumu tabulā uzreiz - neko neaizmirsti.",
             "Ja vērtību daudz un visas dažādas - sagrupē intervālos.",
             "Intervāliem jābūt vienāda garuma un nepārklājas.",
             "Saskaiti biežumu katrā intervālā; summa = N.",
             "Uzzīmē stabiņu diagrammu un aprēķini rādītājus.",
         ],
         pieze="Svītriņu metode: katru vērtību atzīmē ar svītriņu, piekto "
               "svītriņu velk šķērsām - tā ātri skaita pa pieci."),

    Petijums("Reakcijas laika eksperiments",
             vajag="30 cm lineāls un pāris",
             soli=[
                 "Pāris tur lineālu pie 30 cm atzīmes; tavi pirksti pie 0.",
                 "Pāris bez brīdinājuma lineālu palaiž; tu to noķer.",
                 "Pieraksti, pie kuras atzīmes noķēri (cm).",
                 "Atkārto 5 reizes un pieraksti visus rezultātus.",
                 "Apkopo klases datus un sagrupē pa 5 cm.",
             ],
             secinajums="Lineāls krīt arvien ātrāk, tāpēc 20 cm atbilst ap "
                        "0,2 s, bet 5 cm - ap 0,1 s."),

    Paraugs("Biežumu tabula no datiem",
            uzd="Rezultāti (cm): 12, 18, 7, 21, 15, 16, 9, 14, 17, 25. "
                "Sagrupē pa 5 cm.",
            soli=[
                ("5-9: 7, 9", "biežums 2"),
                ("10-14: 12, 14", "biežums 2"),
                ("15-19: 18, 15, 16, 17", "biežums 4"),
                ("20-24: 21; 25-29: 25", "pa 1"),
                ("2 + 2 + 4 + 1 + 1 = 10", "Pārbaude: N = 10."),
            ],
            atbilde="Visbiežākais intervāls ir 15-19 cm"),

    Ievadi("Lasi sagrupētos datus", [
        {"jaut": "Diagrammā: cik skolēnu noķēra ātrāk par 15 cm?",
         "atb": ["11"], "padoms": "3 + 8."},
        {"jaut": "Cik procentu klases ir intervālā 15-19? Noapaļo līdz "
                 "veseliem.",
         "atb": ["37", "37 %", "37%"], "padoms": "11 : 30."},
        {"jaut": "Kurā intervālā ir mediāna (15. un 16. vērtība)? Ieraksti "
                 "intervāla sākumu.",
         "atb": ["15"], "padoms": "3 + 8 = 11, tālāk 12.-22. vērtība."},
        {"jaut": "Cik skolēnu noķēra pie 20 cm vai vēlāk?",
         "atb": ["8"], "padoms": "6 + 2."},
    ]),

    Varianti("Vai grupas ir pareizas?", [
        {"jaut": "Kuri intervāli der?",
         "opcijas": ["0-9, 10-19, 20-29", "0-10, 10-20, 20-30",
                     "0-5, 5-20, 20-30", "0-9, 5-14, 10-19"],
         "pareizi": 0, "padoms": "Vienāda garuma un nepārklājas."},
        {"jaut": "Intervālos «0-10» un «10-20» kur ieskaita 10?",
         "opcijas": ["Neskaidrs - intervāli pārklājas", "Pirmajā",
                     "Otrajā", "Abos"],
         "pareizi": 0, "padoms": "Robežas nedrīkst pārklāties."},
    ]),

    Zimejums("Svītriņu tabula",
             restis([["intervāls", "svītriņas", "biežums"],
                     ["5-9", "|||", "3"],
                     ["10-14", "||||/ |||", "8"],
                     ["15-19", "||||/ ||||/ |", "11"]]),
             paskaidro="Piektā svītriņa (/) pārsvītro četras - tā ātrāk "
                       "saskaitīt."),

    Pasaule("Vai reakcija mainās pēc treniņa?",
            Ievadi("", [
                {"jaut": "Pirms treniņa vidēji 18 cm, pēc nedēļas - 15 cm. "
                         "Par cik cm uzlabojās?",
                 "atb": ["3"], "padoms": "18 − 15."},
                {"jaut": "Par cik procentiem tas ir mazāk?",
                 "atb": ["16,7", "16.7", "17"],
                 "padoms": "3 : 18 ≈ 0,167."},
                {"jaut": "Vārtsargs noķer pie 8 cm. Cik reižu tas ir mazāk "
                         "par 16 cm?",
                 "atb": ["2"], "padoms": "16 : 8."},
            ]),
            pavediens="sports",
            konteksts="Vārtsargi un sacīkšu braucēji trenē reakciju - un mēra "
                      "to tieši ar šādiem testiem.",
            kapec="Sagrupēti dati parāda, vai uzlabojums ir visai grupai."),

    Kopsavilkums([
        "Pierakstu mērījumus tabulā.",
        "Sagrupēju datus vienāda garuma intervālos.",
        "Aizpildu biežumu tabulu un pārbaudu N.",
        "Attēloju datus stabiņu diagrammā.",
    ]),

    Majas([
        "Savāc datus savam pētījumam (vismaz 20 vērtību).",
        "Sagrupē tos un aizpildi biežumu tabulu.",
        "Uzzīmē stabiņu diagrammu.",
    ]),
]
