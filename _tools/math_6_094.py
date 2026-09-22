# -*- coding: utf-8 -*-
"""6. klase, 94. stunda: «Vai rezultāts ir ticams?»

Stunda par pēdējo soli, kuru visbiežāk izlaiž. Atbilde var būt aritmētiski
pareiza un tomēr neiespējama: 120 % no klases, 0,3 cilvēki vai negatīva
cena. Pārbaude pret kontekstu ir tikpat svarīga kā pati rēķināšana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Vai rezultāts ir ticams?"

MERKIS = ("Pārbaudīsim iegūtā rezultāta atbilstību reālajam kontekstam.")

SATURS = [
    Sakums("Pareizs rēķins var dot neiespējamu atbildi",
           fakti=["Skolēnu skaits nevar būt 12,5.",
                  "Atlaide nevar būt lielāka par pašu cenu.",
                  "Daļa nevar būt vairāk par 100 % no kopuma."]),

    Doma("Pārbaudi pret dzīvi, ne tikai pret rēķinu",
         "Pēc aprēķina vienmēr pārbauda, vai atbilde vispār ir iespējama: "
         "vai tā ir vesela, vai tā iekļaujas robežās un vai tai ir jēga.",
         soli=[
             "Paskaties, kāda veida lielums ir atbilde.",
             "Pārbaudi, vai tai jābūt veselam skaitlim.",
             "Pārbaudi robežas: vai daļa nav lielāka par kopumu?",
             "Pārbaudi zīmi: vai lielums vispār var būt negatīvs?",
             "Ja kaut kas nesaiet kopā, meklē kļūdu risinājumā.",
         ],
         pieze="Reizēm neiespējama atbilde nozīmē nevis kļūdu rēķinā, bet "
               "to, ka uzdevuma dati ir pretrunīgi. Arī to var pateikt - un "
               "tā ir pilnvērtīga atbilde."),

    Paraugs("Kura atbilde nav iespējama?",
            uzd="Klasē 24 skolēni. Skolēns aprēķināja, ka 55 % no viņiem "
                "apmeklē pulciņu, un ieguva 13,2 skolēnus. Kas nav labi?",
            soli=[
                ("55 % no 24 ir 13,2",
                 "Rēķins ir pareizs."),
                ("Skolēnu skaits nevar būt daļskaitlis",
                 "Atbilde nav iespējama."),
                ("Tātad 55 % nav precīzs skaitlis",
                 "Dati ir noapaļoti."),
                ("Iespējamie skaitļi ir 13 vai 14 skolēni",
                 "Tie ir 54 % un 58 %."),
            ],
            atbilde="skolēnu skaits ir 13 vai 14, nevis 13,2"),

    Ievadi("Vai atbilde ir iespējama?", [
        {"jaut": "Klasē 24 skolēni, 55 % apmeklē pulciņu. Cik tas ir? "
                 "Noapaļo līdz veselam.",
         "atb": ["13"], "padoms": "13,2 noapaļo uz leju."},
        {"jaut": "Prece maksā 50 €, atlaide 120 %. Vai tas ir iespējams? "
                 "Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Atlaide nevar pārsniegt cenu."},
        {"jaut": "Klasē 25 skolēni, sporto 30. Vai tas ir iespējams?",
         "atb": ["nē", "ne"], "padoms": "Daļa nevar būt lielāka par kopumu."},
        {"jaut": "Cik procentu ir 30 no 25?",
         "atb": ["120"], "padoms": "Vairāk par 100 % - dati ir pretrunīgi."},
        {"jaut": "Skolēnu skaits pieauga par 10 % no 20. Cik tas ir?",
         "atb": ["22"], "padoms": "20 · 1,1."},
        {"jaut": "Klasē 22 skolēni, 30 % apmeklē kori. Vai atbilde sanāk "
                 "vesels skaitlis? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "22 · 0,3 = 6,6 - cilvēkus tā "
                                        "neskaita."},
    ], pamats=4),

    Varianti("Kura atbilde nav ticama?", [
        {"jaut": "Kura atbilde nav iespējama?",
         "opcijas": ["12,5 skolēni", "12 skolēni",
                     "25 % no klases", "60 €"],
         "pareizi": 0,
         "padoms": "Cilvēkus neskaita ar komatu."},
        {"jaut": "Prece maksāja 40 €, pēc atlaides 45 €. Kas nav labi?",
         "opcijas": ["Pēc atlaides cenai jābūt mazākai",
                     "Cena nevar būt 45 €",
                     "Atlaide bija par lielu", "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Atlaide samazina cenu."},
        {"jaut": "Kad daļa drīkst būt vairāk par 100 %?",
         "opcijas": ["Kad runa ir par pieaugumu",
                     "Nekad", "Vienmēr", "Kad kopums ir mazs"],
         "pareizi": 0,
         "padoms": "«Par 120 % vairāk» ir iespējams."},
        {"jaut": "Ko darīt, ja atbilde nav iespējama?",
         "opcijas": ["Meklēt kļūdu vai pateikt, ka dati ir pretrunīgi",
                     "Noapaļot un iet tālāk",
                     "Atstāt kā ir", "Mainīt uzdevumu"],
         "pareizi": 0,
         "padoms": "Neiespējama atbilde ir informācija."},
    ], pamats=4),

    Petijums("Pārbaudi trīs atbildes",
             vajag="trīs atrisināti uzdevumi",
             soli=[
                 "Paņem trīs savus atrisinātos procentu uzdevumus.",
                 "Katram pieraksti, kāda veida lielums ir atbilde.",
                 "Pārbaudi, vai atbildei jābūt veselai un kādās robežās tā "
                 "var būt.",
                 "Pieraksti, vai visas trīs atbildes ir ticamas.",
             ],
             secinajums="Ticamības pārbaude aizņem vienu rindu, bet pamana "
                        "kļūdas, kuras pārrēķināšana nepamana."),

    Pasaule("Vai reklāma runā patiesību?",
            Ievadi("", [
                {"jaut": "«Atlaide līdz 80 %!» Prece maksāja 50 €. Kāda ir "
                         "lielākā iespējamā jaunā cena eiro?",
                 "atb": ["10"], "padoms": "20 % no 50."},
                {"jaut": "«Par 200 % vairāk produkta!» Bija 100 g. Cik gramu "
                         "ir tagad?",
                 "atb": ["300"], "padoms": "100 · 3."},
                {"jaut": "«Par 120 % mazāk cukura.» Vai tas ir iespējams? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Nevar samazināt vairāk par "
                                                "visu."},
                {"jaut": "Bija 20 g cukura, tagad par 100 % mazāk. Cik "
                         "gramu ir tagad?",
                 "atb": ["0"], "padoms": "Viss ir noņemts."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmā procenti mēdz būt izvēlēti tā, lai skanētu "
                      "iespaidīgi - pārbaude parāda, kas ir iespējams.",
            kapec="Neiespējams procents ir pirmā pazīme, ka kaut kas nav "
                  "kārtībā."),

    Kopsavilkums([
        "Pārbaudu, vai atbildei jābūt veselam skaitlim.",
        "Pārbaudu, vai atbilde iekļaujas iespējamās robežās.",
        "Atpazīstu pretrunīgus datus.",
        "Pasaku, kad atbilde nav iespējama, un pamatoju kāpēc.",
    ]),

    Majas([
        "Atrodi reklāmu ar procentiem un pārbaudi, vai tā ir iespējama.",
        "Izdomā uzdevumu, kura atbilde nav iespējama, un paskaidro, kāpēc.",
        "Pārbaudi trīs savas vecās atbildes pret kontekstu.",
    ]),
]
