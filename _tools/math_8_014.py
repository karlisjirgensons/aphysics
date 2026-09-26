# -*- coding: utf-8 -*-
"""8. klase, 14. stunda: «Vai ziņās parādītie dati ir godīgi?»

Diagramma var melot ar patiesiem skaitļiem: ass, kas nesākas no nulles,
padara mazu izmaiņu milzīgu. Slīdnis parāda tos pašus datus ar divām
skalām. Skolēns mācās vispirms paskatīties uz asi, tikai tad uz līniju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, plakne, sektori)

TEMA = "Vai ziņās parādītie dati ir godīgi?"

MERKIS = ("Izvērtēsim, kā diagrammas un statistiku lieto plašsaziņas "
          "līdzekļos, un atpazīsim maldinošu attēlojumu.")

_CENA = [(1, 52), (2, 53), (3, 53), (4, 54), (5, 55)]


def _cena(no_y, lidz_y, solis_y):
    return plakne(lauzta=_CENA, punkti=_CENA, no_x=0, lidz_x=6, no_y=no_y,
                  lidz_y=lidz_y, solis=1, solis_y=solis_y, x_nos="mēn.",
                  y_nos="€")


SATURS = [
    Sakums("«Cenas strauji aug!»",
           zimejums=_cena(51, 56, 1),
           paraksts="Ass sākas no 51 € - līnija izskatās kā kalns.",
           fakti=["Cena pieauga no 52 € līdz 55 €.",
                  "Tas ir apmēram 6 % piecos mēnešos.",
                  "Vispirms skaties uz asi, tad uz līniju."]),

    Slidnis("Tie paši dati - divas skalas", [
        {"v": "Ass no 51", "teksts": "Izskatās: cena lec uz augšu",
         "zim": _cena(51, 56, 1)},
        {"v": "Ass no 0", "teksts": "Patiesībā: neliels pieaugums",
         "zim": _cena(0, 60, 10)},
    ], ievads="Mainās tikai y ass sākums."),

    Doma("Pieci jautājumi katrai diagrammai",
         "Pirms tici diagrammai, pārbaudi, kā tā uzzīmēta un no kurienes nāk "
         "dati.",
         soli=[
             "Vai ass sākas no nulles? Ja nē - izmaiņa izskatās lielāka.",
             "Vai iedaļas ir vienādas?",
             "Vai sektoru procenti kopā dod 100 %?",
             "Kas ir izlase un cik tā liela?",
             "Vai ir norādīts avots?",
         ],
         pieze="Līniju diagrammā ass ne no nulles ir pieņemama, ja to skaidri "
               "parāda - svarīgi ir nesaukt mazu izmaiņu par «strauju»."),

    Ievadi("Aprēķini patieso izmaiņu", [
        {"jaut": "Cena no 52 € uz 55 €. Par cik procentiem? Noapaļo līdz "
                 "veseliem.",
         "atb": ["6", "6 %", "6%"], "padoms": "3 : 52 ≈ 0,058."},
        {"jaut": "Virsraksts: «bezdarbs dubultojās!» - no 0,5 % uz 1 %. Par "
                 "cik procentpunktiem pieauga?",
         "atb": ["0,5", "0.5"], "padoms": "1 − 0,5."},
        {"jaut": "Sektoru diagrammā 45 %, 30 %, 20 % un 15 %. Cik procentu "
                 "par daudz?",
         "atb": ["10", "10 %", "10%"], "padoms": "Summa 110 %."},
        {"jaut": "«3 no 4 zobārstiem iesaka» - aptaujāja 8 zobārstus. Cik "
                 "ieteica?",
         "atb": ["6"], "padoms": "{3|4} no 8."},
    ]),

    Varianti("Kas te maldina?", [
        {"jaut": "Stabiņi 98 un 100 uzzīmēti ar asi no 97.",
         "opcijas": ["Ass nesākas no nulles", "Nav avota",
                     "Nepareizi skaitļi", "Nekas"],
         "pareizi": 0, "padoms": "Stabiņš 100 izskatās 3 reizes augstāks."},
        {"jaut": "«Jaunais dzēriens - 50 % vairāk vitamīnu!»",
         "opcijas": ["Nav teikts, salīdzinājumā ar ko",
                     "50 % ir par daudz", "Vitamīni nav dati",
                     "Nekas nemaldina"],
         "pareizi": 0, "padoms": "Vairāk nekā kas?"},
        {"jaut": "Diagrammā sektori kopā dod 100 %, bet izlase - 12 "
                 "cilvēki.",
         "opcijas": ["Izlase par mazu secinājumiem par visiem",
                     "Sektori uzzīmēti nepareizi", "Nekas", "Jābūt 120 %"],
         "pareizi": 0, "padoms": "Zīmējums pareizs, dati vāji."},
    ]),

    Pasaule("Reklāmas diagramma",
            Ievadi("", [
                {"jaut": "Diagrammā: cik procentu kopā norādīts?",
                 "atb": ["110", "110 %", "110%"], "padoms": "55 + 35 + 20."},
                {"jaut": "Aptaujāja 40 cilvēkus, «iesaka» 22. Cik procentu "
                         "patiesībā?",
                 "atb": ["55", "55 %", "55%"], "padoms": "22 : 40."},
                {"jaut": "«Neiesaka» patiesībā 10 cilvēki. Cik procentu?",
                 "atb": ["25", "25 %", "25%"], "padoms": "10 : 40."},
            ]),
            pavediens="dati",
            konteksts="Reklāmā «iesaka» 55 %, «neiesaka» 35 %, «nezina» 20 % - "
                      "kopā vairāk par 100 %. Kaut kas nav kārtībā.",
            kapec="Pārbaudi summu - tas prasa 5 sekundes.",
            zimejums=sektori([("iesaka", 55), ("neiesaka", 35),
                              ("nezina", 20)], procenti=False)),

    Kopsavilkums([
        "Pārbaudu, vai ass sākas no nulles.",
        "Pārbaudu, vai sektoru procenti kopā dod 100 %.",
        "Aprēķinu patieso izmaiņu procentos.",
        "Jautāju par izlasi un avotu.",
    ]),

    Majas([
        "Atrodi internetā vai avīzē vienu maldinošu diagrammu.",
        "Uzraksti, kas tajā maldina.",
        "Uzzīmē to pašu godīgi.",
    ]),
]
