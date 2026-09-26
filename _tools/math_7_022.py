# -*- coding: utf-8 -*-
"""7. klase, 22. stunda: «Vai šī definīcija ir laba?»

Laba definīcija der visām definējamām figūrām un nevienai citai. Ja
definīcijai atbilst figūra, kas nav domāta, - viens pretpiemērs to atspēko.
Stunda trenē tieši to: meklēt pretpiemēru.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, figura)

TEMA = "Vai šī definīcija ir laba?"

MERKIS = ("Iemācīsimies izvērtēt definīcijas un atspēkot nepilnīgas ar "
          "pretpiemēru.")

SATURS = [
    Sakums("«Kvadrāts ir četrstūris ar vienādām malām.» Vai tā ir?",
           zimejums=figura([(0, 0), (5, 0), (8, 4), (3, 4)],
                           platums=9, augstums=5),
           paraksts="Rombam arī visas malas ir vienādas, bet tas nav "
                    "kvadrāts.",
           fakti=["Definīcijai atbilst figūra, kas nav kvadrāts.",
                  "Tātad definīcija nav laba - trūkst pazīmes.",
                  "Pareizi: četrstūris ar vienādām malām un taisniem "
                  "leņķiem."]),

    Doma("Viens pretpiemērs atspēko definīciju",
         "Definīcija ir laba, ja tai atbilst visas definējamās figūras un "
         "neatbilst neviena cita. Ja atrodas kaut viena figūra, kas atbilst "
         "definīcijai, bet nav definējamā, - tas ir pretpiemērs.",
         soli=[
             "Izlasi definīciju un uzraksti tās pazīmes.",
             "Mēģini uzzīmēt figūru ar šīm pazīmēm, kas NAV definējamā.",
             "Ja izdodas - tas ir pretpiemērs; papildini definīciju.",
             "Pārbaudi arī otrādi: vai visas definējamās figūras atbilst?",
         ],
         pieze="Pārāk plaša definīcija ielaiž liekas figūras; pārāk šaura "
               "izslēdz vajadzīgās. Abas ir sliktas."),

    Paraugs("Taisnstūra definīcija",
            uzd="«Taisnstūris ir četrstūris, kuram ir taisns leņķis.» Vai "
                "definīcija ir laba?",
            soli=[
                ("Meklē četrstūri ar vienu taisnu leņķi, kas nav taisnstūris",
                 "Pretpiemēra meklēšana."),
                ("Taisnleņķa trapece: viens taisns leņķis, pārējie nav",
                 "Atbilst definīcijai."),
                ("Tā nav taisnstūris", "Pretpiemērs atrasts."),
                ("Labojums: četrstūris, kura visi leņķi ir taisni",
                 "Pietiek pat ar trim taisniem leņķiem."),
            ],
            atbilde="Nav laba; pretpiemērs - taisnleņķa trapece."),

    Zimejums("Pretpiemērs taisnstūrim",
             figura([(0, 0), (6, 0), (4, 3), (0, 3)], platums=7, augstums=4),
             paskaidro="Divi taisni leņķi (pie kreisās malas), bet malas nav "
                       "paralēlas pa pāriem."),

    Varianti("Atrodi pretpiemēru", [
        {"jaut": "«Trijstūris ir figūra ar trim virsotnēm.» Pretpiemērs?",
         "opcijas": ["Trīs punkti uz vienas taisnes, savienoti",
                     "Vienādmalu trijstūris", "Taisnleņķa trijstūris",
                     "Kvadrāts"],
         "pareizi": 0,
         "padoms": "Tad «trijstūris» ir tikai nogrieznis."},
        {"jaut": "«Rombs ir četrstūris ar vienādām diagonālēm.» Pretpiemērs?",
         "opcijas": ["Taisnstūris (ne kvadrāts)", "Kvadrāts",
                     "Rombs ar asu leņķi", "Trijstūris"],
         "pareizi": 0,
         "padoms": "Taisnstūrim diagonāles ir vienādas."},
        {"jaut": "«Riņķa līnija ir līnija bez stūriem.» Pretpiemērs?",
         "opcijas": ["Elipse (ovāls)", "Riņķa līnija ar r = 5",
                     "Kvadrāts", "Nogrieznis ar diviem galiem"],
         "pareizi": 0,
         "padoms": "Ovālam nav stūru, bet tas nav riņķa līnija."},
        {"jaut": "Kura definīcija ir pārāk šaura?",
         "opcijas": ["«Pāra skaitlis ir skaitlis, kas beidzas ar 2»",
                     "«Pāra skaitlis dalās ar 2»",
                     "«Kvadrātam visas malas un leņķi ir vienādi»",
                     "«Nogrieznim ir divi gali un visi punkti starp tiem»"],
         "pareizi": 0,
         "padoms": "4, 6, 8 un 10 arī ir pāra."},
    ], pamats=4),

    Pasaule("Kas ir «viedierīce»?",
            Varianti("", [
                {"jaut": "Noteikumos: «Viedierīce ir ierīce ar ekrānu.» "
                         "Pretpiemērs?",
                 "opcijas": ["Veca kalkulatora displejs",
                             "Viedtālrunis", "Planšete", "Viedpulkstenis"],
                 "pareizi": 0,
                 "padoms": "Ekrāns ir, bet «vieds» tas nav."},
                {"jaut": "Kā šo definīciju uzlabot?",
                 "opcijas": ["Pievienot: pieslēdzas internetam un var "
                             "instalēt lietotnes",
                             "Pievienot: ir melnā krāsā",
                             "Izņemt vārdu «ekrāns»",
                             "Nekā - tā ir laba"],
                 "pareizi": 0,
                 "padoms": "Vajag pazīmi, kas atšķir."},
                {"jaut": "Kāpēc likumos definīcijas ir tik garas?",
                 "opcijas": ["Lai neviens neatrastu pretpiemēru",
                             "Lai būtu grūti lasīt",
                             "Tā ir tradīcija",
                             "Lai būtu vairāk lapu"],
                 "pareizi": 0,
                 "padoms": "Pretpiemērs likumā ir «caurums»."},
            ]),
            pavediens="dati",
            konteksts="Likumos un lietošanas noteikumos definīcijas raksta "
                      "tikpat rūpīgi kā matemātikā.",
            kapec="Pretpiemēra meklēšana ir jurista un matemātiķa darbs."),

    Kopsavilkums([
        "Zinu, kāda ir laba definīcija.",
        "Atspēkoju definīciju ar vienu pretpiemēru.",
        "Atšķiru pārāk plašu un pārāk šauru definīciju.",
        "Papildinu definīciju ar trūkstošo pazīmi.",
    ]),

    Majas([
        "Uzraksti kvadrāta definīciju un palūdz kādam atrast pretpiemēru.",
        "Atrodi vārdnīcā vienu definīciju un pārbaudi, vai tā ir laba.",
        "Uzraksti pārāk plašu un pārāk šauru definīciju vārdam «krēsls».",
    ]),
]
