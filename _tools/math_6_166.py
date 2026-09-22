# -*- coding: utf-8 -*-
"""6. klase, 166. stunda: «Vai atbilde ir ticama?»

Pēdējā pārbaudes stunda pirms gada noslēguma. Tagad pārbaudāmi ir visu veidu
rezultāti: skaitļi, procenti, laukumi un tilpumi. Katram ir savas robežas,
un tieši tās pasaka, vai atbilde vispār ir iespējama.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Vai atbilde ir ticama?"

MERKIS = ("Pārbaudīsim rezultāta atbilstību reālajam kontekstam.")

SATURS = [
    Sakums("Katram lielumam savas robežas",
           fakti=["Laukums un tilpums nevar būt negatīvs.",
                  "Cilvēku skaits nevar būt daļskaitlis.",
                  "Atlaide nevar pārsniegt sākotnējo cenu."]),

    Doma("Pārbaudi zīmi, veselumu un lielumu",
         "Katru atbildi pārbauda pēc trim jautājumiem: vai zīme ir "
         "iespējama, vai skaitlim jābūt veselam un vai lielums ir ticams.",
         soli=[
             "Nosaki, kāda veida lielums ir atbilde.",
             "Pārbaudi zīmi: vai tas vispār var būt negatīvs?",
             "Pārbaudi veselumu: vai to mēra veselos?",
             "Pārbaudi lielumu: vai tas iekļaujas saprātīgās robežās?",
             "Ja kaut kas nesaiet kopā, meklē kļūdu risinājumā.",
         ],
         pieze="Negatīvs rezultāts ne vienmēr ir kļūda: temperatūra, "
               "dziļums un konta atlikums var būt zem nulles. Bet laukums, "
               "tilpums un cena - nē."),

    Paraugs("Trīs pārbaudes",
            uzd="Vai šīs atbildes ir ticamas: laukums −12 m²; 7,5 skolēni; "
                "atlaide 60 € precei par 50 €?",
            soli=[
                ("Laukums −12 m²: laukums nevar būt negatīvs",
                 "Nav ticami."),
                ("7,5 skolēni: cilvēkus skaita veselos",
                 "Nav ticami."),
                ("Atlaide 60 € precei par 50 €",
                 "Atlaide nevar pārsniegt cenu - nav ticami."),
                ("Visās trijās ir kļūda risinājumā",
                 "Katrai savs iemesls."),
            ],
            atbilde="neviena nav ticama"),

    Ievadi("Vai atbilde ir iespējama?", [
        {"jaut": "Laukums −12 m². Vai tas ir iespējams? Raksti «jā» vai "
                 "«nē».",
         "atb": ["nē", "ne"], "padoms": "Laukums nav negatīvs."},
        {"jaut": "Temperatūra −12 °C. Vai tas ir iespējams?",
         "atb": ["jā", "ja"], "padoms": "Zem nulles."},
        {"jaut": "7,5 skolēni. Vai tas ir iespējams?",
         "atb": ["nē", "ne"], "padoms": "Cilvēkus skaita veselos."},
        {"jaut": "Tilpums 7,5 l. Vai tas ir iespējams?",
         "atb": ["jā", "ja"], "padoms": "Tilpumu mēra daļās."},
        {"jaut": "Prece maksā 50 €, atlaide 60 €. Vai tas ir iespējams?",
         "atb": ["nē", "ne"], "padoms": "Cena kļūtu negatīva."},
        {"jaut": "Konta atlikums −60 €. Vai tas ir iespējams?",
         "atb": ["jā", "ja"], "padoms": "Parāds."},
    ], pamats=4),

    Varianti("Kura atbilde nav ticama?", [
        {"jaut": "Kurš lielums nevar būt negatīvs?",
         "opcijas": ["laukums", "temperatūra",
                     "konta atlikums", "dziļums"],
         "pareizi": 0,
         "padoms": "Laukumu mēra kvadrātvienībās."},
        {"jaut": "Kurš lielums vienmēr ir vesels skaitlis?",
         "opcijas": ["cilvēku skaits", "masa",
                     "garums", "temperatūra"],
         "pareizi": 0,
         "padoms": "Cilvēkus neskaita ar komatu."},
        {"jaut": "Kastes tilpums 5000 m³. Vai tas ir ticami?",
         "opcijas": ["Nē, tas ir par lielu kastei",
                     "Jā", "Nevar zināt", "Jā, ja kaste ir liela"],
         "pareizi": 0,
         "padoms": "Tas ir vairāk nekā māja."},
        {"jaut": "Ko darīt, ja atbilde nav ticama?",
         "opcijas": ["Meklēt kļūdu risinājumā", "Noapaļot",
                     "Atstāt kā ir", "Mainīt uzdevumu"],
         "pareizi": 0,
         "padoms": "Neticama atbilde ir signāls."},
    ], pamats=4),

    Petijums("Pārbaudi piecas atbildes",
             vajag="pieci atrisināti uzdevumi",
             soli=[
                 "Paņem piecus savus atrisinātos uzdevumus.",
                 "Katram pieraksti, kāda veida lielums ir atbilde.",
                 "Pārbaudi zīmi, veselumu un lielumu.",
                 "Atzīmē tās atbildes, kas neiztur pārbaudi.",
                 "Atrodi, kurā solī radusies kļūda.",
             ],
             secinajums="Ticamības pārbaude aizņem vienu rindu, bet pamana "
                        "tieši tās kļūdas, kuras pārrēķināšana nepamana."),

    Pasaule("Vai aprēķins ir iespējams?",
            Ievadi("", [
                {"jaut": "Istaba 4 m x 3 m. Kāds ir grīdas laukums m²?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Aprēķins deva 120 m². Cik reižu tas ir par lielu?",
                 "atb": ["10"], "padoms": "120 : 12."},
                {"jaut": "Kastes tilpums 50 cm x 40 cm x 30 cm. Cik litru?",
                 "atb": ["60"], "padoms": "60 000 cm³."},
                {"jaut": "Aprēķins deva 60 000 l. Vai tas ir ticami? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Tas būtu baseins."},
            ]),
            pavediens="maja",
            konteksts="Būvniecībā neticams aprēķins nozīmē nepareizi "
                      "pasūtītu materiālu - un to pamana tikai pārbaude.",
            kapec="Mērvienību kļūda maina atbildi tūkstoškārt."),

    Kopsavilkums([
        "Pārbaudu atbildes zīmi, veselumu un lielumu.",
        "Zinu, kuri lielumi nevar būt negatīvi.",
        "Atpazīstu mērvienību kļūdu pēc neticama rezultāta.",
        "Meklēju kļūdu risinājumā, ja atbilde nav iespējama.",
    ]),

    Majas([
        "Pārbaudi trīs savas atbildes pēc visiem trim jautājumiem.",
        "Atrodi vienu neticamu atbildi un tās cēloni.",
        "Pieraksti, kuri lielumi tavos uzdevumos nevar būt negatīvi.",
    ]),
]
