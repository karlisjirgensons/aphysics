# -*- coding: utf-8 -*-
"""5. klase, 171. stunda: «Kā lasu diagrammas un grafikus?»

Trešā noslēguma stunda apvieno abus datu attēlus: sektoru diagrammu no
5.7. temata un sakarības grafiku no 5.8. Abi rāda datus, bet atbild uz
dažādiem jautājumiem - viens uz «kura daļa», otrs uz «kā mainās». Tieši šo
atšķirību ir vērts paturēt prātā, ejot uz 6. klasi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, rinkis)

TEMA = "Kā lasu diagrammas un grafikus?"

MERKIS = ("Nolasīsim datus no sektoru diagrammas un sakarības grafika un "
          "formulēsim secinājumus.")

SATURS = [
    Sakums("Divi attēli, divi jautājumi",
           zimejums=rinkis(sektors=180, virsraksts="50 % izvēlējās futbolu"),
           paraksts="Sektors rāda daļu; grafiks rādītu izmaiņu.",
           fakti=["Sektoru diagramma atbild: kura daļa ir lielāka.",
                  "Sakarības grafiks atbild: kā lielums mainās.",
                  "Abi ir dati, bet par dažādām lietām."]),

    Doma("Katram attēlam savs jautājums",
         "Sektoru diagrammu lasa, salīdzinot daļas no viena veselā; "
         "sakarības grafiku - sekojot, kā viens lielums mainās līdz ar otru.",
         soli=[
             "Diagrammā atrodi lielāko sektoru.",
             "Pārbaudi, vai procenti kopā dod 100 %.",
             "Grafikā atrodi augstāko un zemāko punktu.",
             "Nosaki, kuros posmos lielums aug un kuros sarūk.",
             "Formulē secinājumu pilnā teikumā.",
         ],
         pieze="Sektoru diagramma nerāda skaitu, bet sakarības grafiks "
               "nerāda daļas no veselā. Tāpēc izvēle starp tiem ir atkarīga "
               "no jautājuma, nevis no gaumes."),

    Paraugs("Ko pasaka katrs attēls?",
            uzd="Diagrammā: futbols 50 %, basketbols 25 %, volejbols 25 %. "
                "Grafikā: 4°, 8°, 14°, 16°. Kādus secinājumus var izdarīt?",
            soli=[
                ("Futbolu izvēlējās puse",
                 "Lielākais sektors."),
                ("Pārējos - pa ceturtdaļai",
                 "Abi sektori vienādi."),
                ("Grafikā temperatūra auga no 4° līdz 16°",
                 "Līnija ceļas."),
                ("Pieaugums ir 12 grādi",
                 "16 - 4."),
            ],
            atbilde="Diagramma rāda daļas, grafiks - pieaugumu"),

    Ievadi("Nolasi no attēliem", [
        {"jaut": "Sektori 50 %, 25 % un 25 %. Cik procentu ir lielākais?",
         "atb": ["50"], "padoms": "Puse riņķa."},
        {"jaut": "Cik grādu ir 50 % sektoram?",
         "atb": ["180"], "padoms": "360 : 2."},
        {"jaut": "Aptaujāti 20 skolēni, 50 % izvēlējās futbolu. Cik skolēnu?",
         "atb": ["10"], "padoms": "20 : 2."},
        {"jaut": "Sektori 40 % un 35 %. Cik procentu ir trešais?",
         "atb": ["25"], "padoms": "100 - 75."},
        {"jaut": "Temperatūras 4, 8, 14, 16. Kāda ir augstākā?",
         "atb": ["16"], "padoms": "Lielākais skaitlis."},
        {"jaut": "Par cik grādiem tā pieauga no pirmā līdz pēdējam?",
         "atb": ["12"], "padoms": "16 - 4."},
        {"jaut": "1 kg maksā 2 €. Cik maksā 4 kg?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Cik kilogramu var nopirkt par 10 €?",
         "atb": ["5"], "padoms": "10 : 2."},
    ], pamats=4,
        ievads="Vispirms izlem, kāda veida attēls tev priekšā."),

    Zimejums("Grafiks rāda izmaiņu",
             plakne(lauzta=[(0, 4), (1, 8), (2, 14), (3, 16)], no_x=0,
                    lidz_x=4, no_y=0, lidz_y=20, solis=4,
                    virsraksts="Temperatūra aug"),
             paskaidro="Šo pašu informāciju sektoru diagrammā parādīt "
                       "nevarētu: tā rāda daļas, nevis izmaiņu laikā.",
             ievads="Otrs attēlu veids un otrs jautājums."),

    Varianti("Kurš attēls te der?", [
        {"jaut": "Uz ko atbild sektoru diagramma?",
         "opcijas": ["Kura daļa ir lielāka", "Kā lielums mainās",
                     "Cik cilvēku aptaujāti", "Kāpēc tā notika"],
         "pareizi": 0,
         "padoms": "Daļas no viena veselā."},
        {"jaut": "Uz ko atbild sakarības grafiks?",
         "opcijas": ["Kā viens lielums mainās līdz ar otru",
                     "Kura daļa ir lielāka",
                     "Cik ir procentu",
                     "Kāpēc tā notika"],
         "pareizi": 0,
         "padoms": "Izmaiņa."},
        {"jaut": "Vai no diagrammas var uzzināt aptaujāto skaitu?",
         "opcijas": ["Nevar, ja tas nav uzrakstīts", "Var vienmēr",
                     "Var no sektora lieluma", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "153. stunda."},
        {"jaut": "Sektori 50 %, 25 % un 25 %. Cik grādu ir lielākajam?",
         "opcijas": ["180°", "90°", "50°", "360°"],
         "pareizi": 0,
         "padoms": "Puse riņķa."},
        {"jaut": "Temperatūras 4, 8, 14, 16. Par cik tā pieauga?",
         "opcijas": ["12", "16", "4", "20"],
         "pareizi": 0,
         "padoms": "16 - 4."},
        {"jaut": "Ar ko beidzas datu lasīšana?",
         "opcijas": ["Ar secinājumu pilnā teikumā", "Ar skaitli",
                     "Ar zīmējumu", "Ar tabulu"],
         "pareizi": 0,
         "padoms": "Skaitlis pats neko nepasaka."},
    ], pamats=4),

    Pasaule("Skolas dati divos attēlos",
            Ievadi("", [
                {"jaut": "Aptaujāti 40 skolēni, 25 % brauc ar autobusu. Cik "
                         "skolēnu?",
                 "atb": ["10"], "padoms": "40 : 4."},
                {"jaut": "Cik grādu ir šis sektors?",
                 "atb": ["90"], "padoms": "360 : 4."},
                {"jaut": "Skolēnu skaits klasēs: 20, 22, 25, 21. Kāds ir "
                         "vidējais?",
                 "atb": ["22"], "padoms": "88 : 4."},
                {"jaut": "Par cik lielākā klase pārsniedz mazāko?",
                 "atb": ["5"], "padoms": "25 - 20."},
            ]),
            pavediens="skola",
            konteksts="Vienus un tos pašus skolas datus var parādīt gan ar "
                      "diagrammu, gan ar grafiku - atkarībā no jautājuma.",
            kapec="Attēla izvēle ir daļa no atbildes."),

    Kopsavilkums([
        "Nolasu datus no sektoru diagrammas.",
        "Nolasu datus no sakarības grafika.",
        "Zinu, uz kādiem jautājumiem katrs attēls atbild.",
        "Formulēju secinājumus pilnos teikumos.",
    ]),

    Majas([
        "Atrodi vienu diagrammu un vienu grafiku.",
        "Pieraksti katram divus secinājumus.",
        "Pieraksti, ko no katra uzzināt nevar.",
    ]),
]
