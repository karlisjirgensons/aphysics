# -*- coding: utf-8 -*-
"""5. klase, 12. stunda: «Kad precīzs skaitlis nav vajadzīgs?»

Mikrotemata pirmā stunda. Noapaļošanas kārtulu te vēl nav - vispirms jāsaprot,
kāpēc to vispār vajag: skaitlim ir uzdevums, un no uzdevuma atkarīgs, cik
precīzam tam jābūt. Pati kārtula nāk 14. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kad precīzs skaitlis nav vajadzīgs?"

MERKIS = ("Mācīsimies izvērtēt, vai situācijā vajadzīgs precīzs skaitlis vai "
          "pietiek ar aptuvenu, un pamatot savu izvēli.")

SATURS = [
    Sakums("Cik cilvēku bija koncertā?",
           fakti=["Rīkotājs saka: «Pārdotas 4 812 biļetes.»",
                  "Draugs stāsta: «Tur bija kādi pieci tūkstoši!»",
                  "Abi runā par vienu koncertu. Kurš melo?"]),

    Doma("Cik precīzs skaitlis, tik, cik prasa darbs",
         "Precizitāti izlemj nevis skaitlis, bet tas, ko ar to darīsi.",
         soli=[
             "Pajautā: ko es ar šo skaitli izdarīšu?",
             "Ja par to jāmaksā vai jāatskaitās - vajag precīzu.",
             "Ja tas jāizstāsta vai jāsalīdzina - pietiek ar aptuvenu.",
             "Aptuveno skaitli izvēlas apaļu, lai to var paturēt prātā.",
         ],
         pieze="Aptuvens skaitlis nav nepareizs skaitlis. Nepareizi ir tikai "
               "tad, ja aptuveno lieto tur, kur vajag precīzu - piemēram, "
               "atdodot naudu."),

    Varianti("Precīzs vai aptuvens?", [
        {"jaut": "Veikalā jāsamaksā par pirkumu. Kāds skaitlis vajadzīgs?",
         "opcijas": ["Precīzs", "Aptuvens", "Jebkurš", "Nekāds"],
         "pareizi": 0,
         "padoms": "Kasē pietrūkstošos centus neviens neaizmirsīs."},
        {"jaut": "Stāsti draugam, cik skatītāju bija spēlē. Kāds skaitlis "
                 "vajadzīgs?",
         "opcijas": ["Aptuvens", "Precīzs līdz vienam",
                     "Precīzs līdz desmitam", "Nekāds"],
         "pareizi": 0,
         "padoms": "Draugs grib zināt, vai bija daudz, nevis cik tieši."},
        {"jaut": "Aptiekā jāizmēra zāļu deva bērnam. Kāds skaitlis "
                 "vajadzīgs?",
         "opcijas": ["Precīzs", "Aptuvens", "Apaļš", "Jebkurš"],
         "pareizi": 0,
         "padoms": "Šeit kļūda maksā veselību."},
        {"jaut": "Jānovērtē, cik ilgi ilgs brauciens pa 213 km garu ceļu. "
                 "Kāds skaitlis noder?",
         "opcijas": ["Aptuvens - ap 200 km", "Tikai precīzs 213 km",
                     "Nekāds", "Vienalga kāds"],
         "pareizi": 0,
         "padoms": "Braukšanas laiku tik un tā neviens nezina līdz minūtei."},
        {"jaut": "Kāpēc laikraksti raksta «ap 20 000 dalībnieku», nevis "
                 "«20 137»?",
         "opcijas": ["Apaļu skaitli vieglāk uztvert",
                     "Precīzu skaitli aizliegts rakstīt",
                     "Precīzs skaitlis vienmēr ir nepareizs",
                     "Tā ir īsāk par vienu burtu"],
         "pareizi": 0,
         "padoms": "Padomā, kuru skaitli atcerēsies pēc stundas."},
        {"jaut": "Kurš aptuvenais skaitlis skaitlim 4 812 ir labākais "
                 "stāstam?",
         "opcijas": ["Ap 5 000", "Ap 4 000", "Ap 4 812", "Ap 50 000"],
         "pareizi": 0,
         "padoms": "Apaļš un pēc iespējas tuvāks īstajam."},
    ], pamats=4),

    Paraugs("Viens skaitlis, divas atbildes",
            uzd="Skolā ir 1 038 skolēni. Kā šo skaitli nosauc direktors "
                "atskaitē un kā - tu draugam?",
            soli=[
                ("Atskaitē: 1 038",
                 "Par katru skolēnu skola saņem naudu, tāpēc te der tikai "
                 "precīzs skaitlis."),
                ("Sarunā: ap tūkstoti",
                 "Draugam svarīgi, vai skola liela vai maza."),
                ("Abi skaitļi apraksta to pašu skolu",
                 "Atšķiras tikai tas, kam skaitlis vajadzīgs."),
            ],
            atbilde="atskaitē 1 038, sarunā - ap 1 000"),

    Ievadi("Kādu apaļu skaitli tu nosauktu?", [
        {"jaut": "Stadionā bija 1 987 skatītāji. Cik apmēram? (tūkstošos)",
         "atb": ["2000"], "padoms": "Pavisam nedaudz pietrūkst līdz diviem "
                                    "tūkstošiem."},
        {"jaut": "Ezera dziļums ir 31 m. Cik apmēram? (desmitos)",
         "atb": ["30"], "padoms": "Tuvākais desmits."},
        {"jaut": "Ceļš ir 296 km garš. Cik apmēram? (simtos)",
         "atb": ["300"], "padoms": "Līdz trim simtiem trūkst tikai 4 km."},
        {"jaut": "Bibliotēkā ir 5 104 grāmatas. Cik apmēram? (tūkstošos)",
         "atb": ["5000"], "padoms": "Pāri pieciem tūkstošiem ir tikai 104."},
        {"jaut": "Koncertā bija 4 812 cilvēku. Cik apmēram? (tūkstošos)",
         "atb": ["5000"], "padoms": "Kurš tūkstotis ir tuvāk - 4 vai 5?"},
        {"jaut": "Skrējiena distance ir 10 038 m. Cik apmēram? (tūkstošos)",
         "atb": ["10000"], "padoms": "Desmit tūkstoši un vēl mazliet."},
    ], pamats=4,
        ievads="Izvēlies tuvāko apaļo skaitli - tādu, ko var paturēt prātā."),

    Pasaule("Cik koku ir mežā?",
            Ievadi("", [
                {"jaut": "Mežsargs saskaitījis 2 973 kokus. Ko viņš teiks "
                         "ziņās? (tūkstošos)",
                 "atb": ["3000"], "padoms": "Gandrīz trīs tūkstoši."},
                {"jaut": "Cik koku viņš ierakstīs mežu reģistrā?",
                 "atb": ["2973"],
                 "padoms": "Reģistrā vajag precīzu skaitli."},
                {"jaut": "Putnu vērotāji saskaitīja 418 gulbjus. Cik "
                         "apmēram? (simtos)",
                 "atb": ["400"], "padoms": "Tuvākais simts."},
                {"jaut": "Dabas parka platība ir 4 187 ha. Cik apmēram? "
                         "(tūkstošos)",
                 "atb": ["4000"], "padoms": "Četri tūkstoši ar nelielu "
                                            "pārpalikumu."},
            ]),
            pavediens="daba",
            konteksts="Dabā neko nevar saskaitīt līdz pēdējam kokam, tāpēc "
                      "pētnieki paši izlemj, cik precīzi rakstīt.",
            kapec="Reģistrā vajag precīzu skaitli, stāstā - apaļu."),

    Kopsavilkums([
        "Izvērtēju, vai situācijā vajadzīgs precīzs vai aptuvens skaitlis.",
        "Pamatoju savu izvēli ar to, ko ar skaitli darīs.",
        "Nosaucu tuvāko apaļo skaitli un paskaidroju, kāpēc tieši to.",
    ]),

    Majas([
        "Atrodi mājās trīs skaitļus (čekā, uz iepakojuma, telefonā) un "
        "pieraksti, kurš no tiem ir precīzs un kurš aptuvens.",
        "Izstāsti kādam savu dienu, lietojot tikai apaļus skaitļus.",
        "Padomā, kur aptuvens skaitlis varētu izraisīt nepatikšanas.",
    ]),
]
