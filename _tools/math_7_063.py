# -*- coding: utf-8 -*-
"""7. klase, 63. stunda: «Kad funkcija ir pozitīva un kad negatīva?»

Funkcija ir pozitīva tur, kur grafiks ir virs x ass, un negatīva - kur zem
tās. Robeža ir funkcijas nulle. Stunda to lieto temperatūrai un bankas
kontam, kur zīme ir svarīgāka par skaitli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, taisne)

TEMA = "Kad funkcija ir pozitīva un kad negatīva?"

MERKIS = ("Noteiksim argumenta vērtības, kurām funkcija ir pozitīva vai "
          "negatīva.")

SATURS = [
    Sakums("Kad ledus sāks kust?",
           zimejums=plakne(grafiki=[(2, -6, "T = 2t − 6")],
                           punkti=[(3, 0, "(3; 0)")],
                           no_x=0, lidz_x=7, no_y=-6, lidz_y=8, solis=1,
                           solis_y=2, x_nos="h", y_nos="°C"),
           paraksts="Līdz 3. stundai zem nulles, pēc tam - virs.",
           fakti=["No rīta −6 °C, katru stundu +2 °C.",
                  "Negatīva temperatūra - ledus paliek.",
                  "Pozitīva - ledus kūst."]),

    Doma("Virs ass - pozitīva, zem ass - negatīva",
         "Funkcija ir pozitīva (y > 0) tiem argumentiem, kuriem grafiks ir "
         "virs x ass, un negatīva (y < 0) tiem, kuriem grafiks ir zem x ass. "
         "Robeža ir funkcijas nulle.",
         soli=[
             "Atrodi funkcijas nulli: kx + b = 0.",
             "Ja k > 0, pa labi no nulles funkcija ir pozitīva.",
             "Ja k < 0, pa labi no nulles funkcija ir negatīva.",
             "Pieraksti ar nevienādību: y > 0, ja x > 3.",
         ],
         pieze="Nullē funkcija nav ne pozitīva, ne negatīva - tā ir 0."),

    Paraugs("Nosaki zīmes",
            uzd="y = −x + 4. Kad funkcija ir pozitīva, kad - negatīva?",
            soli=[
                ("Nulle: −x + 4 = 0, x = 4", "Robeža."),
                ("k = −1 < 0 - taisne iet uz leju", "Pa kreisi augstāk."),
                ("y > 0, ja x < 4", "Pa kreisi no nulles."),
                ("y < 0, ja x > 4", "Pa labi."),
            ],
            atbilde="Pozitīva, ja x < 4; negatīva, ja x > 4"),

    Zimejums("y > 0, ja x < 4",
             taisne(-2, 8, 1, intervali=[(None, 4, False, False)]),
             paskaidro="Tukšs aplītis: nullē funkcija nav pozitīva."),

    Ievadi("Atrodi robežu", [
        {"jaut": "y = 2x − 6. Pie kāda x funkcija maina zīmi?",
         "atb": ["3"], "padoms": "2x = 6."},
        {"jaut": "y = 2x − 6. Vai f(10) ir pozitīva? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "20 − 6 = 14."},
        {"jaut": "y = −3x + 12. Pie kāda x maina zīmi?",
         "atb": ["4"], "padoms": "3x = 12."},
        {"jaut": "y = −3x + 12. Kāda zīme, ja x = 0? Raksti «pozitīva» "
                 "vai «negatīva».",
         "atb": ["pozitīva", "pozitiva"], "padoms": "y = 12.",
         "tastatura": "text"},
    ]),

    Varianti("Spried", [
        {"jaut": "y = 5x + 10. Kad y < 0?",
         "opcijas": ["x < −2", "x > −2", "x < 2", "x > 2"],
         "pareizi": 0,
         "padoms": "Nulle −2, k > 0."},
        {"jaut": "y = 3 visiem x. Kad funkcija ir negatīva?",
         "opcijas": ["Nekad", "Vienmēr", "x < 0", "x < 3"],
         "pareizi": 0,
         "padoms": "Vienmēr 3 > 0."},
        {"jaut": "Grafiks visur zem x ass. Ko zina par funkciju?",
         "opcijas": ["Tā ir negatīva visiem x",
                     "Tā ir pozitīva", "Tai ir nulle",
                     "Tā ir augoša"],
         "pareizi": 0,
         "padoms": "Zem ass - negatīva."},
    ]),

    Pasaule("Konta atlikums",
            Ievadi("", [
                {"jaut": "Kartē 45 €, katru dienu tērē 6 €: A = 45 − 6d. "
                         "Pēc cik pilnām dienām atlikums kļūs negatīvs?",
                 "atb": ["8"], "padoms": "45 − 48 < 0; 45 − 42 > 0."},
                {"jaut": "Kāds atlikums pēc 7 dienām (€)?",
                 "atb": ["3"], "padoms": "45 − 42."},
                {"jaut": "Pēc cik dienām atlikums ir tieši 0? (daļskaitlis)",
                 "atb": ["7,5"], "padoms": "45 : 6."},
            ]),
            pavediens="veikals",
            konteksts="Banka brīdina, pirms atlikums kļūst negatīvs - tā "
                      "zina funkcijas nulli.",
            kapec="Svarīga ir zīme: plusā vai mīnusā."),

    Kopsavilkums([
        "Atrodu funkcijas nulli.",
        "Nosaku, kur funkcija ir pozitīva un kur negatīva.",
        "Lietoju k zīmi, lai zinātu virzienu.",
        "Pierakstu rezultātu ar nevienādību.",
    ]),

    Majas([
        "Kad y = 4x − 2 ir pozitīva?",
        "Uzzīmē grafiku un iekrāso daļu virs x ass.",
        "Izdomā situāciju ar pozitīvu un negatīvu vērtību.",
    ]),
]
