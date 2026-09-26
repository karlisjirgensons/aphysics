# -*- coding: utf-8 -*-
"""3. klase, 143. stunda: «Kad simts jāsadala desmitos?»

Aizņēmums ir atņemšanas grūtākā vieta. Modelis to padara redzamu: simtu
apmaina pret desmit desmitiem, tieši tāpat kā eiro pret desmit desmitcentu
monētām. Bez šī modeļa aizņēmums paliek burvju triks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         Zimejums, restis)

TEMA = "Kad simts jāsadala desmitos?"

MERKIS = ("Atņemsim ar aizņēmumu, modelējot simta sadalīšanu desmitos.")

SATURS = [
    Sakums("Ko darīt, ja atņemt nevar?",
           zimejums=restis([["", 4, 2, 5],
                            ["−", 1, 8, 3],
                            ["", 2, 4, 2]],
                           "425 − 183"),
           paraksts="Desmitu vietā 2 mīnus 8 nesanāk - jāaizņemas simts.",
           fakti=["Ja vietā nepietiek, aizņemas no nākamās pa kreisi.",
                  "Viens simts ir desmit desmiti."]),

    Doma("Simtu apmaina pret desmit desmitiem",
         "Ja desmitu nepietiek, paņem vienu simtu un pārvērt to par desmit "
         "desmitiem.",
         soli=[
             "Paskaties, vai vietā pietiek, lai atņemtu.",
             "Ja nepietiek, samazini nākamo vietu pa kreisi par 1.",
             "Tai vietai, kur trūka, pieskaiti 10.",
             "Tagad atņem un turpini ar nākamo vietu.",
         ],
         pieze="Tas ir tas pats, ko dara veikalā: ja nepietiek sīknaudas, "
               "vienu eiro apmaina pret desmit desmitcentu monētām."),

    Slidnis("Kā notiek aizņēmums",
            soli=[
                {"v": "425 = 4 simti, 2 desmiti, 5 vieni",
                 "teksts": "Sākuma skaitlis.", "josla": 33},
                {"v": "= 3 simti, 12 desmiti, 5 vieni",
                 "teksts": "Vienu simtu apmaina pret 10 desmitiem.",
                 "josla": 66},
                {"v": "12 − 8 = 4 desmiti",
                 "teksts": "Tagad atņemt var.", "josla": 100},
            ],
            ievads="425 − 183 pa vietām."),

    Paraugs("Cik ir 425 − 183?",
            uzd="Atņem stabiņā 425 − 183.",
            soli=[
                ("Vieni: 5 − 3 = 2",
                 "Te viss kārtībā."),
                ("Desmiti: 2 − 8 nesanāk",
                 "Aizņemas simtu: 12 − 8 = 4."),
                ("Simti: 3 − 1 = 2",
                 "Simtu vietā tagad ir 3, ne 4; atbilde ir 242."),
            ],
            atbilde="242"),

    Petijums("Apmaini naudu",
             vajag="naudas modeļi: eiro, desmitcentu un viencentu monētas",
             soli=[
                 "Saliec 425 centus: 4 eiro, 2 desmitnieki, 5 centi.",
                 "Mēģini atņemt 183 centus.",
                 "Kad desmitnieku nepietiek, apmaini eiro pret desmit "
                 "desmitniekiem.",
                 "Atņem un saskaiti, kas palika.",
             ],
             secinajums="Aizņēmums ir tieši tā pati apmaiņa - tikai "
                        "pierakstīta ar cipariem."),

    Ievadi("Atņem ar aizņēmumu", [
        {"jaut": "425 − 183 = ?", "atb": ["242"], "padoms": "Aizņemas simtu."},
        {"jaut": "531 − 274 = ?", "atb": ["257"], "padoms": "Divi aizņēmumi."},
        {"jaut": "640 − 156 = ?", "atb": ["484"], "padoms": "Divi aizņēmumi."},
        {"jaut": "802 − 347 = ?", "atb": ["455"], "padoms": "Aizņemas caur "
                                                            "nulli."},
        {"jaut": "715 − 208 = ?", "atb": ["507"], "padoms": "Vienu vietā "
                                                            "nepietiek."},
        {"jaut": "900 − 432 = ?", "atb": ["468"], "padoms": "Divi aizņēmumi."},
    ], pamats=4),

    Zimejums("Kad aizņēmuma nav",
             restis([["", 5, 6, 8],
                     ["−", 2, 3, 4],
                     ["", 3, 3, 4]],
                    "568 − 234"),
             paskaidro="Te katrā vietā augšējais cipars ir lielāks, tāpēc "
                       "aizņemties nav vajadzības.",
             ievads="Salīdzini ar stundas sākuma zīmējumu."),

    Varianti("Kad jāaizņemas?", [
        {"jaut": "Kad vietā jāaizņemas?",
         "opcijas": ["Kad augšējais cipars ir mazāks",
                     "Vienmēr", "Kad cipari vienādi", "Nekad"],
         "pareizi": 0, "padoms": "Atņemt nevar."},
        {"jaut": "Par cik samazinās nākamā vieta pa kreisi?",
         "opcijas": ["Par 1", "Par 10", "Par 100", "Nemainās"],
         "pareizi": 0, "padoms": "Viena vienība pārceļas."},
        {"jaut": "Cik pieskaita tai vietai, kur trūka?",
         "opcijas": ["10", "1", "100", "5"],
         "pareizi": 0, "padoms": "Viens simts ir desmit desmiti."},
        {"jaut": "Cik ir 523 − 267?",
         "opcijas": ["256", "266", "246", "356"],
         "pareizi": 0, "padoms": "Divi aizņēmumi."},
    ], pamats=4),

    Pasaule("Cik punktu pietrūka?",
            Ievadi("", [
                {"jaut": "Komanda guva 425 punktus, pretinieki 183. Par cik "
                         "vairāk guva pirmā?",
                 "atb": ["242"], "padoms": "425 − 183."},
                {"jaut": "Rekords ir 531 punkts. Cik punktu pietrūka?",
                 "atb": ["106"], "padoms": "531 − 425."},
                {"jaut": "Nākamajā spēlē guva 274 punktus. Cik punktu abās "
                         "spēlēs?",
                 "atb": ["699"], "padoms": "425 + 274."},
                {"jaut": "Cik punktu pietrūkst līdz 1000?", "atb": ["301"],
                 "padoms": "1000 − 699."},
            ]),
            pavediens="sports",
            konteksts="Sezonas punktu tabulā starpības rēķina katru nedēļu - "
                      "un gandrīz vienmēr ar aizņēmumu.",
            kapec="Bez aizņēmuma starpība iznāk par lielu, un tabula melo."),

    Kopsavilkums([
        "Atņemu ar aizņēmumu no nākamās vietas.",
        "Zinu, ka viens simts ir desmit desmiti.",
        "Modelēju aizņēmumu ar naudu.",
        "Pārbaudu rezultātu ar saskaitīšanu.",
    ]),

    Majas([
        "Izrēķini 634 − 258 un 703 − 419.",
        "Atzīmē katrā, kur notika aizņēmums.",
        "Pārbaudi abas atbildes ar saskaitīšanu.",
    ]),
]
