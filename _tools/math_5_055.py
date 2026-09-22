# -*- coding: utf-8 -*-
"""5. klase, 55. stunda: «Ko nozīmē paplašināt daļu?»

Pamatīpašība jau ir zināma; te tai tiek dots vārds un uzdevums ar nosacījumu.
Paplašināšana skolēnam šķiet dīvaina - skaitļi kļūst lielāki, bet daļa nekļūst
lielāka. Tāpēc katrā uzdevumā te ir pateikts, *kāpēc* to dara: lai saucējs
kļūtu tāds, kāds vajadzīgs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Ko nozīmē paplašināt daļu?"

MERKIS = ("Iemācīsimies paplašināt daļu un izpildīt nosacījumu par tās "
          "skaitītāju vai saucēju.")

SATURS = [
    Sakums("Cena uz cenu zīmes",
           zimejums=dala(10, 3, "3/10"),
           paraksts="Trīs desmitdaļas - tā atlaidi raksta veikalā.",
           fakti=["Veikals atlaidi raksta ar saucēju 10 vai 100.",
                  "Tavs aprēķins bieži dod saucēju 5 vai 20.",
                  "Tāpēc daļu pārraksta ar to saucēju, kāds vajadzīgs."]),

    Doma("Paplašināt nozīmē reizināt abus locekļus",
         "Daļu paplašina, reizinot skaitītāju un saucēju ar vienu un to pašu "
         "skaitli; daļas vērtība nemainās, tikai skaitļi kļūst lielāki.",
         soli=[
             "Izlasi nosacījumu: kādam jābūt jaunajam saucējam vai "
             "skaitītājam.",
             "Izdali jauno skaitli ar veco - tas ir reizinātājs.",
             "Reizini ar to abus daļas locekļus.",
             "Pieraksti rezultātu kā vienādību.",
             "Pārbaudi, vai nosacījums tiešām izpildīts.",
         ],
         pieze="Paplašināt drīkst ar jebkuru skaitli, tāpēc vienai daļai ir "
               "bezgalīgi daudz pierakstu: {1|2} = {2|4} = {3|6} = {50|100}. "
               "Nosacījums pasaka, kuru no tiem šoreiz vajag."),

    Paraugs("Paplašini {2|5} tā, lai saucējs būtu 100",
            uzd="Uzraksti daļu {2|5} ar saucēju 100.",
            soli=[
                ("100 : 5 = 20",
                 "Cik reižu jaunais saucējs lielāks par veco."),
                ("2 · 20 = 40",
                 "Ar to pašu skaitli reizina skaitītāju."),
                ("{2|5} = {40|100}",
                 "Nosacījums izpildīts: saucējs ir 100."),
                ("Pārbaude: 40 : 20 = 2 un 100 : 20 = 5",
                 "Atgriežamies pie sākotnējās daļas."),
            ],
            atbilde="{2|5} = {40|100}"),

    Ievadi("Izpildi nosacījumu", [
        {"jaut": "Paplašini {1|5} tā, lai saucējs būtu 10. Kāds ir "
                 "skaitītājs?",
         "atb": ["2"], "padoms": "10 : 5 = 2."},
        {"jaut": "Paplašini {3|4} tā, lai saucējs būtu 100. Kāds ir "
                 "skaitītājs?",
         "atb": ["75"], "padoms": "100 : 4 = 25; 3 · 25."},
        {"jaut": "Paplašini {1|4} tā, lai skaitītājs būtu 5. Kāds ir "
                 "saucējs?",
         "atb": ["20"], "padoms": "5 : 1 = 5; 4 · 5."},
        {"jaut": "Paplašini {2|3} tā, lai skaitītājs būtu 10. Kāds ir "
                 "saucējs?",
         "atb": ["15"], "padoms": "10 : 2 = 5; 3 · 5."},
        {"jaut": "Paplašini {7|20} tā, lai saucējs būtu 100. Kāds ir "
                 "skaitītājs?",
         "atb": ["35"], "padoms": "100 : 20 = 5; 7 · 5."},
        {"jaut": "Paplašini {5|6} tā, lai saucējs būtu 30. Kāds ir "
                 "skaitītājs?",
         "atb": ["25"], "padoms": "30 : 6 = 5; 5 · 5."},
        {"jaut": "Paplašini {3|8} tā, lai skaitītājs būtu 9. Kāds ir "
                 "saucējs?",
         "atb": ["24"], "padoms": "9 : 3 = 3; 8 · 3."},
        {"jaut": "Paplašini {1|2} tā, lai saucējs būtu 1000. Kāds ir "
                 "skaitītājs?",
         "atb": ["500"], "padoms": "1000 : 2."},
    ], pamats=4,
        ievads="Vispirms reizinātājs, tikai tad rēķins - citādi nosacījums "
               "netiek izpildīts."),

    Zimejums("Viena un tā pati daļa ar saucēju 10",
             dala(10, 4, "4/10"),
             paskaidro="Tā ir {2|5}: katra piektdaļa sadalīta divās "
                       "desmitdaļās, tāpēc arī paņemto gabalu ir divreiz "
                       "vairāk.",
             ievads="Paplašinot gabali kļūst sīkāki, nevis daļa - lielāka."),

    Varianti("Vai nosacījums izpildīts?", [
        {"jaut": "Kas notiek ar daļas vērtību, kad to paplašina?",
         "opcijas": ["Nekas, tā paliek tā pati", "Tā kļūst lielāka",
                     "Tā kļūst mazāka", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Mainās pieraksts, nevis daudzums."},
        {"jaut": "Vai {3|7} var paplašināt tā, lai saucējs būtu 20?",
         "opcijas": ["Nevar, jo 20 nedalās ar 7", "Var, skaitītājs būs 6",
                     "Var, skaitītājs būs 9", "Var vienmēr"],
         "pareizi": 0,
         "padoms": "Reizinātājam jābūt veselam skaitlim."},
        {"jaut": "{4|9} paplašināja kā {12|27}. Ar cik reizināja?",
         "opcijas": ["Ar 3", "Ar 4", "Ar 9", "Ar 12"],
         "pareizi": 0,
         "padoms": "27 : 9."},
        {"jaut": "Cik dažādu pierakstu ir daļai {1|3}?",
         "opcijas": ["Bezgalīgi daudz", "Trīs", "Deviņi", "Tikai viens"],
         "pareizi": 0,
         "padoms": "Reizināt var ar jebkuru skaitli."},
        {"jaut": "Kurš pieraksts *nav* {3|5} paplašinājums?",
         "opcijas": ["{9|10}", "{6|10}", "{9|15}", "{12|20}"],
         "pareizi": 0,
         "padoms": "Skaties, vai abi locekļi reizināti vienādi."},
        {"jaut": "Kāpēc veikalā atlaidi raksta ar saucēju 100?",
         "opcijas": ["Tā visas atlaides var salīdzināt",
                     "Tā skaitļi ir mazāki",
                     "Tā daļa kļūst lielāka",
                     "Tāds ir likums"],
         "pareizi": 0,
         "padoms": "Vienāds saucējs - salīdzina skaitītājus."},
    ], pamats=4),

    Pasaule("Kura atlaide ir lielāka?",
            Ievadi("", [
                {"jaut": "Vienā veikalā atlaide ir {1|5} no cenas. Cik tas "
                         "ir simtdaļu?",
                 "atb": ["20"], "padoms": "100 : 5 = 20."},
                {"jaut": "Citā veikalā atlaide ir {1|4} no cenas. Cik tas ir "
                         "simtdaļu?",
                 "atb": ["25"], "padoms": "100 : 4 = 25."},
                {"jaut": "Trešajā veikalā atlaide ir {3|10}. Cik tas ir "
                         "simtdaļu?",
                 "atb": ["30"], "padoms": "Abus locekļus reizina ar 10."},
                {"jaut": "Ceturtajā veikalā atlaide ir {2|5}. Cik tas ir "
                         "simtdaļu?",
                 "atb": ["40"], "padoms": "2 · 20."},
            ]),
            pavediens="veikals",
            konteksts="Katrs veikals atlaidi raksta savādāk, bet salīdzināt "
                      "var tikai tad, ja saucējs ir viens.",
            kapec="Paplašināšana pārvērš visas atlaides vienā mērogā."),

    Kopsavilkums([
        "Zinu, ka paplašināt nozīmē reizināt abus daļas locekļus.",
        "Paplašinu daļu tā, lai saucējs būtu dotais skaitlis.",
        "Paplašinu daļu tā, lai skaitītājs būtu dotais skaitlis.",
        "Pārbaudu, vai nosacījums tiešām ir izpildīts.",
    ]),

    Majas([
        "Uzraksti {3|4} ar saucējiem 8, 16 un 100.",
        "Atrodi veikala reklāmā atlaidi un pieraksti to kā daļu ar "
        "saucēju 100.",
        "Padomā, vai {5|6} var paplašināt tā, lai saucējs būtu 100.",
    ]),
]
