# -*- coding: utf-8 -*-
"""3. klase, 126. stunda: «Kā izmērīt neregulāru ķermeni?»

Temata pēdējā mācību stunda. Akmeni ar kubiem nenomērīsi - bet ūdens līmeņa
celšanās dod precīzu atbildi. Šī ir pirmā reize, kad mērījumu iegūst
netieši, un tieši šī doma vēlāk atkārtosies fizikā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kā izmērīt neregulāru ķermeni?"

MERKIS = ("Izteiksim un pārbaudīsim idejas, kā salīdzināt tilpumu, ja kubi "
          "neder.")

SATURS = [
    Sakums("Cik liels ir akmens?",
           zimejums=kolonnas([("pirms", 300), ("pēc", 380)], " ml"),
           paraksts="Ūdens pacēlās par 80 ml - tāds ir akmens tilpums.",
           fakti=["Neregulāru ķermeni ar kubiem izmērīt nevar.",
                  "Ūdens paceļas tieši par ķermeņa tilpumu."]),

    Doma("Ūdens līmeņa starpība ir ķermeņa tilpums",
         "Ielaid ķermeni ūdenī un izmēri, par cik pacēlās līmenis - tas ir "
         "ķermeņa tilpums.",
         soli=[
             "Ielej mērtraukā ūdeni un pieraksti līmeni.",
             "Ielaid ķermeni tā, lai tas pilnībā ietu zem ūdens.",
             "Pieraksti jauno līmeni.",
             "Atņem: jaunais līmenis mīnus sākotnējais.",
         ],
         pieze="Ķermenim jābūt pilnībā zem ūdens. Ja daļa paliek virs, "
               "ūdens paceļas mazāk, un mērījums ir nepareizs."),

    Petijums("Izmēri akmens tilpumu",
             vajag="mērtrauks, ūdens un daži akmentiņi",
             soli=[
                 "Ielej mērtraukā 300 ml ūdens un pieraksti līmeni.",
                 "Ielaid akmeni un nolasi jauno līmeni.",
                 "Izrēķini starpību.",
                 "Atkārto ar otru akmeni un salīdzini tilpumus.",
             ],
             secinajums="Lielākam akmenim ūdens paceļas vairāk - starpība "
                        "tieši parāda tilpumu."),

    Paraugs("Cik liels ir akmens tilpums?",
            uzd="Traukā bija 300 ml ūdens. Ielaižot akmeni, līmenis kļuva "
                "380 ml. Cik liels ir akmens tilpums?",
            soli=[
                ("380 − 300 = 80",
                 "Līmenis pacēlās par 80 ml."),
                ("Akmens aizņēma tieši tik vietas",
                 "Ūdens pacēlās par akmens tilpumu."),
                ("80 ml",
                 "Tāds ir akmens tilpums."),
            ],
            atbilde="80 ml"),

    Ievadi("Izrēķini tilpumu", [
        {"jaut": "Bija 300 ml, kļuva 380 ml. Cik ir ķermeņa tilpums?",
         "atb": ["80"], "padoms": "380 − 300."},
        {"jaut": "Bija 250 ml, kļuva 400 ml. Cik ir tilpums?",
         "atb": ["150"], "padoms": "400 − 250."},
        {"jaut": "Bija 500 ml, kļuva 650 ml. Cik ir tilpums?",
         "atb": ["150"], "padoms": "650 − 500."},
        {"jaut": "Ķermeņa tilpums 120 ml, bija 400 ml. Kāds būs līmenis?",
         "atb": ["520"], "padoms": "400 + 120."},
        {"jaut": "Divi akmeņi pa 80 ml. Par cik pacelsies līmenis?",
         "atb": ["160"], "padoms": "2 · 80."},
        {"jaut": "Bija 200 ml, ielaida 3 akmeņus pa 50 ml. Kāds ir līmenis?",
         "atb": ["350"], "padoms": "200 + 150."},
    ], pamats=4),

    Zimejums("Divi akmeņi",
             kolonnas([("mazais", 40), ("lielais", 120)], " ml"),
             paskaidro="Lielākam akmenim ūdens līmenis paceļas trīs reizes "
                       "vairāk.",
             ievads="Divi mērījumi vienā traukā."),

    Varianti("Kā mēra neregulāru ķermeni?", [
        {"jaut": "Kā izmēra akmens tilpumu?",
         "opcijas": ["Pēc ūdens līmeņa celšanās", "Ar lineālu",
                     "Ar svariem", "Ar kubiem"],
         "pareizi": 0, "padoms": "Ūdens paceļas par ķermeņa tilpumu."},
        {"jaut": "Kas jāievēro, ielaižot ķermeni?",
         "opcijas": ["Tam jābūt pilnībā zem ūdens", "Tam jāpeld",
                     "Tam jābūt sausam", "Nekas"],
         "pareizi": 0, "padoms": "Citādi mērījums ir par mazu."},
        {"jaut": "Bija 400 ml, kļuva 470 ml. Cik ir tilpums?",
         "opcijas": ["70 ml", "870 ml", "30 ml", "470 ml"],
         "pareizi": 0, "padoms": "470 − 400."},
        {"jaut": "Kāpēc kubi te neder?",
         "opcijas": ["Ķermenis nav taisnstūrveida", "Kubi ir par maziem",
                     "Kubi ir par lieliem", "Kubi vienmēr der"],
         "pareizi": 0, "padoms": "Kubi neietilpst bez spraugām."},
    ], pamats=4),

    Pasaule("Cik liels ir ledus gabals?",
            Ievadi("", [
                {"jaut": "Traukā bija 500 ml, ar ledus gabalu 560 ml. Cik ir "
                         "ledus tilpums?",
                 "atb": ["60"], "padoms": "560 − 500."},
                {"jaut": "Cik mililitru ir 5 tādi gabali?", "atb": ["300"],
                 "padoms": "5 · 60."},
                {"jaut": "Cik gabalu ietilpst 1 litrā?", "atb": ["16"],
                 "padoms": "1000 : 60 ar atlikumu."},
                {"jaut": "Cik mililitru paliks pāri?", "atb": ["40"],
                 "padoms": "1000 − 960."},
            ]),
            pavediens="planeta",
            konteksts="Ledus gabalu formas ir neregulāras, tāpēc to tilpumu "
                      "mēra tieši ar ūdeni.",
            kapec="Tas pats paņēmiens der jebkuram ķermenim, kas negrimst "
                  "un neizšķīst."),

    Kopsavilkums([
        "Izmēru neregulāra ķermeņa tilpumu ar ūdeni.",
        "Aprēķinu tilpumu kā līmeņu starpību.",
        "Zinu, ka ķermenim jābūt pilnībā zem ūdens.",
        "Salīdzinu divu ķermeņu tilpumus.",
    ]),

    Majas([
        "Izmēri kāda mājas priekšmeta tilpumu ar ūdeni.",
        "Salīdzini divu dažādu priekšmetu tilpumus.",
        "Pārlasi tematu un atzīmē, kas vēl jāatkārto pirms pārbaudes darba.",
    ], ievads="Šī ir pēdējā stunda pirms pārbaudes darba."),
]
