# -*- coding: utf-8 -*-
"""6. klase, 8. stunda: «Kā sadalīt nogriezni?»

Attiecība pārceļas uz garumu. Te pirmoreiz parādās kustīgs objekts: skolēns
izrēķina, kur uz nogriežņa jābūt atzīmei, palaiž zondi un *redz*, vai tā
apstājas pareizajā vietā. Kļūda vairs nav vārds uz papīra.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā sadalīt nogriezni?"

MERKIS = ("Iemācīsimies sadalīt nogriezni divās vai trīs daļās dotā "
          "attiecībā un pārbaudīt, kur atrodas dalījuma punkts.")

SATURS = [
    Sakums("Kur uz troses piestiprināt āķi?",
           zimejums=taisne(0, 20, 5, [(8, "atzīme")]),
           paraksts="20 m gara trose, sadalīta attiecībā 2 : 3. Atzīme ir "
                    "pie 8 m.",
           fakti=["Celtnī troses garums ir zināms, dalījuma vieta - nav.",
                  "Attiecība pasaka vietu, nevis garumu pati par sevi."]),

    Doma("Dalījuma punkts ir pirmās daļas galā",
         "Nogriezni sadala tāpat kā jebkuru kopumu: viena daļa, tad "
         "reizināšana - un atzīmi liek pirmās daļas galā.",
         soli=[
             "Saskaiti attiecības skaitļus - cik daļu ir visā nogrieznī.",
             "Izdali nogriežņa garumu ar daļu skaitu.",
             "Reizini vienu daļu ar pirmo attiecības skaitli.",
             "Atzīmi liec tieši tik tālu no sākuma.",
             "Pārbaudi: atlikums atbilst otrajam skaitlim.",
         ],
         pieze="Ja daļu ir trīs, atzīmes ir divas: pirmā pirmās daļas galā, "
               "otrā - pirmās un otrās daļas summas vietā."),

    Paraugs("20 m trose attiecībā 2 : 3",
            uzd="20 m garu trosi sadala attiecībā 2 : 3. Cik tālu no sākuma "
                "ir dalījuma vieta?",
            soli=[
                ("2 + 3 = 5 daļas",
                 "Tik vienādu gabalu ir visā trosē."),
                ("20 : 5 = 4 m",
                 "Tik garš ir viens gabals."),
                ("2 · 4 = 8 m",
                 "Pirmā daļa ir divi gabali."),
                ("3 · 4 = 12 m; 8 + 12 = 20 m",
                 "Pārbaude: abas daļas kopā dod visu trosi."),
            ],
            atbilde="atzīme ir 8 m no sākuma"),

    Pasaule("Kur apstāsies zonde?",
            Kustiba("", [
                {"jaut": "24 m garu trosi dala attiecībā 1 : 3. Cik metru no "
                         "sākuma ir atzīme?",
                 "atb": 6, "beigas": 24, "iedala": 4, "mers": "metri",
                 "merkis": "atzīme", "objekts": "Zonde",
                 "padoms": "4 daļas; 24 : 4 = 6; pirmā daļa ir viens gabals."},
                {"jaut": "Tā pati trose, attiecība 5 : 1. Cik metru no "
                         "sākuma ir atzīme?",
                 "atb": 20, "beigas": 24, "iedala": 4, "mers": "metri",
                 "merkis": "atzīme", "objekts": "Zonde",
                 "padoms": "6 daļas; viena daļa 4 m; 5 · 4."},
                {"jaut": "30 m trosi dala 2 : 3. Kur ir atzīme?",
                 "atb": 12, "beigas": 30, "iedala": 5, "mers": "metri",
                 "merkis": "atzīme", "objekts": "Zonde",
                 "padoms": "5 daļas; viena daļa 6 m; 2 · 6."},
                {"jaut": "36 m trosi dala 1 : 2 : 3. Kur ir *otrā* atzīme?",
                 "atb": 18, "beigas": 36, "iedala": 6, "mers": "metri",
                 "merkis": "2. atzīme", "objekts": "Zonde",
                 "padoms": "6 daļas; viena daļa 6 m; 1 + 2 = 3 daļas."},
            ]),
            pavediens="tehnika",
            konteksts="Zonde pa trosi aizbrauc tieši tik tālu, cik tu "
                      "pateici - ja aprēķins ir greizs, tas uzreiz redzams.",
            kapec="Attālums no sākuma ir pirmo daļu summa, nevis viena daļa."),

    Ievadi("Atrodi dalījuma vietu", [
        {"jaut": "10 cm nogriezni dala 1 : 4. Cik cm ir pirmā daļa?",
         "atb": ["2"], "padoms": "5 daļas; 10 : 5."},
        {"jaut": "15 cm nogriezni dala 2 : 3. Cik cm ir pirmā daļa?",
         "atb": ["6"], "padoms": "5 daļas; viena daļa 3 cm."},
        {"jaut": "Tas pats nogrieznis. Cik cm ir otrā daļa?",
         "atb": ["9"], "padoms": "15 − 6."},
        {"jaut": "24 cm nogriezni dala 1 : 2 : 3. Cik cm ir pirmā daļa?",
         "atb": ["4"], "padoms": "6 daļas; 24 : 6."},
        {"jaut": "Tas pats nogrieznis. Cik cm no sākuma ir otrā atzīme?",
         "atb": ["12"], "padoms": "Pirmās divas daļas: 4 + 8."},
        {"jaut": "Nogrieznis ir 21 cm, attiecība 3 : 4. Cik cm ir garākā "
                 "daļa?",
         "atb": ["12"], "padoms": "7 daļas; viena daļa 3 cm; 4 · 3."},
    ], pamats=4),

    Varianti("Vai atzīme ir vietā?", [
        {"jaut": "12 cm nogrieznis, attiecība 1 : 1. Kur ir atzīme?",
         "opcijas": ["Tieši vidū, 6 cm", "Pie 1 cm", "Pie 4 cm",
                     "Pie 12 cm"],
         "pareizi": 0,
         "padoms": "Vienādas daļas nozīmē pusi."},
        {"jaut": "Attiecība 1 : 5. Kura daļa ir garāka?",
         "opcijas": ["Otrā", "Pirmā", "Abas vienādas",
                     "Nevar zināt bez garuma"],
         "pareizi": 0,
         "padoms": "Vairāk daļu - garāks gabals."},
        {"jaut": "Nogriezni 20 cm dala 3 : 2. Cik cm ir *līdz* atzīmei?",
         "opcijas": ["12", "8", "4", "10"],
         "pareizi": 0,
         "padoms": "5 daļas; viena daļa 4 cm; 3 · 4."},
        {"jaut": "Kāpēc atzīmju skaits ir par vienu mazāks nekā daļu skaits?",
         "opcijas": ["Nogriežņa gali jau ir robežas",
                     "Viena atzīme vienmēr pazūd",
                     "Tā ir tikai sakritība",
                     "Atzīmju ir tikpat, cik daļu"],
         "pareizi": 0,
         "padoms": "Trīs daļas atdala divas iekšējas atzīmes."},
    ], pamats=4),

    Zimejums("Trīs daļas - divas atzīmes",
             taisne(0, 36, 6, [(6, "1."), (18, "2.")]),
             paskaidro="36 m attiecībā 1 : 2 : 3. Viena daļa ir 6 m, tāpēc "
                       "atzīmes ir pie 6 m un pie 18 m.",
             ievads="Otro atzīmi liek tur, kur beidzas *otrā* daļa."),

    Kopsavilkums([
        "Sadalu nogriezni dotā attiecībā, izmantojot vienas daļas garumu.",
        "Zinu, ka atzīme ir pirmo daļu summas vietā, nevis vienas daļas.",
        "Trim daļām atrodu abas atzīmes.",
        "Pārbaudu rezultātu: daļu summa ir viss nogrieznis.",
    ]),

    Majas([
        "Uzzīmē 12 cm nogriezni un sadali to attiecībā 1 : 3.",
        "Izmēri savu zīmuli un sadali to domās attiecībā 1 : 2.",
        "Atrodi mājās priekšmetu, kura garumu var sadalīt attiecībā 1 : 1 : 2 "
        "veselos centimetros.",
    ]),
]
