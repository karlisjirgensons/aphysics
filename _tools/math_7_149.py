# -*- coding: utf-8 -*-
"""7. klase, 149. stunda: «Kāds uzdevums sanāk tev?»

Otrādi: dots vienādojums, jāizdomā situācija. Tas pārbauda, vai skolēns
saprot, ko nozīmē katrs vienādojuma loceklis. Stunda beidzas ar klasesbiedra
uzdevuma risināšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kāds uzdevums sanāk tev?"

MERKIS = ("Veidosim savu uzdevumu dotam vienādojumam un risināsim "
          "klasesbiedra uzdevumu.")

SATURS = [
    Sakums("Vienādojums 2x + 5 = 21 - kāds stāsts?",
           fakti=["2 vienādas preces un 5 € piegāde - 21 €.",
                  "2 vienādi posmi un 5 km - kopā 21 km.",
                  "Viens vienādojums - daudz stāstu."]),

    Doma("No vienādojuma uz stāstu",
         "Lai izdomātu uzdevumu vienādojumam, katram loceklim piešķir "
         "nozīmi: x - nezināmais lielums, koeficients - skaits, brīvais "
         "loceklis - fiksēts lielums, labā puse - kopsumma.",
         soli=[
             "Izvēlies tematu (veikals, ceļojums, sports).",
             "Kas ir x? Kas ir koeficients?",
             "Kas ir brīvais loceklis un labā puse?",
             "Uzraksti jautājumu un pārbaudi, vai atbilde ir reāla.",
         ]),

    Paraugs("Uzdevums vienādojumam 3x − 4 = 20",
            uzd="Izdomā situāciju un atrisini.",
            soli=[
                ("Stāsts: 3 draugi pērk pa biļetei x €, atlaide grupai 4 €, "
                 "samaksāja 20 €", "Nozīme."),
                ("3x = 24", "Atrisina."),
                ("x = 8 (€)", "Biļetes cena."),
                ("8 € - reāla cena", "Pārbaude situācijā."),
            ],
            atbilde="Biļete maksā 8 €."),

    Varianti("Kurš stāsts atbilst x + (x + 7) = 45?", [
        {"jaut": "Izvēlies pareizo stāstu.",
         "opcijas": ["Divi brāļi, viens par 7 gadiem vecāks, kopā 45 gadi",
                     "7 grāmatas par x €, kopā 45 €",
                     "x km un vēl 45 km, kopā 7 km",
                     "Skaitli reizina ar 7 un iegūst 45"],
         "pareizi": 0, "padoms": "Divi lielumi, viens par 7 lielāks."},
        {"jaut": "Kurš stāsts atbilst 4x = 60?",
         "opcijas": ["Kvadrāta perimetrs 60 cm - kāda mala?",
                     "Skaitlis par 4 lielāks nekā 60",
                     "4 cilvēki un 60 €",
                     "60 − 4 = x"],
         "pareizi": 0, "padoms": "4 vienādas malas."},
    ]),

    Ievadi("Atrisini klasesbiedra uzdevumu", [
        {"jaut": "«Es nopirku 5 saldējumus pa x € un saņēmu 1,50 € atlikumu "
                 "no 10 €.» 5x + 1,5 = 10. x = ?",
         "atb": ["1,7"], "padoms": "5x = 8,5."},
        {"jaut": "«Riteņbraucējs brauca 2 h ar x km/h un vēl 15 km, kopā "
                 "55 km.» x = ?",
         "atb": ["20"], "padoms": "2x = 40."},
        {"jaut": "«Plauktā x grāmatas, otrā - divreiz vairāk, kopā 36.» x?",
         "atb": ["12"], "padoms": "3x = 36."},
    ]),

    Pasaule("Savs kvests",
            Ievadi("", [
                {"jaut": "Kvestā: «Mans kods ir skaitlis, kuru reizinot ar 4 "
                         "un atņemot 7, iegūst 57.» Kods?",
                 "atb": ["16"], "padoms": "4x − 7 = 57."},
                {"jaut": "«Otrais kods ir par 9 mazāks nekā trīs reizes "
                         "pirmais.» Kods?",
                 "atb": ["39"], "padoms": "3 · 16 − 9."},
                {"jaut": "Abu kodu summa?",
                 "atb": ["55"], "padoms": "16 + 39."},
            ]),
            pavediens="kodi",
            konteksts="Escape room spēlēs kodi bieži ir vienādojumu "
                      "atrisinājumi.",
            kapec="Savs uzdevums - labākā sapratnes pārbaude."),

    Kopsavilkums([
        "Izdomāju situāciju dotam vienādojumam.",
        "Piešķiru nozīmi katram loceklim.",
        "Pārbaudu, vai atbilde ir reāla.",
        "Risinu klasesbiedra uzdevumu.",
    ]),

    Majas([
        "Izdomā uzdevumus vienādojumiem 2x + 3 = 15 un 5(x − 1) = 30.",
        "Samainies ar klasesbiedru un atrisini.",
        "Izveido kvesta kodu ar vienādojumu.",
    ]),
]
