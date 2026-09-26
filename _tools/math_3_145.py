# -*- coding: utf-8 -*-
"""3. klase, 145. stunda: «Kā pārbaudīt starpību?»

Atņemšanu pārbauda ar saskaitīšanu - un šī pārbaude ir pat drošāka nekā
saskaitīšanas pārbaude, jo aizņēmumu kļūdas tajā parādās uzreiz. Skolēns
iemācās arī otru pārbaudi: no mazinātāja atņem starpību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pārbaudīt starpību?"

MERKIS = ("Pārbaudīsim atņemšanu ar saskaitīšanu.")

SATURS = [
    Sakums("Kā pateikt, vai starpība ir pareiza?",
           zimejums=restis([["425", "−", "183", "=", "242"],
                            ["242", "+", "183", "=", "425"]],
                           "pārbaude ar saskaitīšanu"),
           paraksts="Starpība plus atņēmējs dod mazināmo.",
           fakti=["Atņemšanu pārbauda ar saskaitīšanu.",
                  "Starpība plus atņēmējs vienmēr dod sākotnējo skaitli."]),

    Doma("Starpība plus atņēmējs dod mazināmo",
         "Ja a − b = c, tad c + b jābūt tieši a - citādi kaut kur ir kļūda.",
         soli=[
             "Izrēķini starpību.",
             "Pieskaiti tai atņēmēju.",
             "Salīdzini rezultātu ar sākotnējo skaitli.",
             "Ja skaitļi nesakrīt, meklē kļūdu aizņēmumos.",
         ],
         pieze="Ir arī otra pārbaude: no mazināmā atņem starpību - jāsanāk "
               "atņēmējam. Abas der vienādi labi."),

    Paraugs("Vai 425 − 183 = 242?",
            uzd="Pārbaudi starpību 425 − 183 = 242.",
            soli=[
                ("242 + 183",
                 "Starpībai pieskaita atņēmēju."),
                ("242 + 183 = 425",
                 "Sanāca mazināmais."),
                ("Atbilde ir pareiza",
                 "Pārbaude izdevās."),
            ],
            atbilde="242 ir pareizi"),

    Ievadi("Izrēķini un pārbaudi", [
        {"jaut": "425 − 183 = ?", "atb": ["242"], "padoms": "Ar aizņēmumu."},
        {"jaut": "Pārbaude: 242 + 183 = ?", "atb": ["425"],
         "padoms": "Ja sanāk 425, atbilde bija pareiza."},
        {"jaut": "631 − 247 = ?", "atb": ["384"], "padoms": "Ar aizņēmumu."},
        {"jaut": "Pārbaude: 384 + 247 = ?", "atb": ["631"],
         "padoms": "Pretējā darbība."},
        {"jaut": "800 − 355 = ?", "atb": ["445"], "padoms": "Caur nulli."},
        {"jaut": "Pārbaude: 445 + 355 = ?", "atb": ["800"],
         "padoms": "Pretējā darbība."},
    ], pamats=4),

    Zimejums("Divas pārbaudes",
             restis([["pārbaude", "rēķins"],
                     ["ar saskaitīšanu", "242 + 183 = 425"],
                     ["ar atņemšanu", "425 − 242 = 183"]],
                    "425 − 183 = 242"),
             paskaidro="Abas pārbaudes lieto tos pašus trīs skaitļus, tikai "
                       "citā kārtībā.",
             ievads="Viena starpība, divas pārbaudes."),

    Varianti("Kura pārbaude der?", [
        {"jaut": "Ar ko pārbauda 631 − 247 = 384?",
         "opcijas": ["384 + 247", "631 + 247", "384 − 247", "631 · 247"],
         "pareizi": 0, "padoms": "Starpība plus atņēmējs."},
        {"jaut": "Skolēns uzrakstīja 500 − 176 = 434. Kā to pamanīt?",
         "opcijas": ["434 + 176 = 610, nevis 500", "Atbilde ir par mazu",
                     "Kļūdas nav", "Starpībai jābūt pāra skaitlim"],
         "pareizi": 0, "padoms": "Pārbaude nesakrīt."},
        {"jaut": "Kāda ir otra pārbaude?",
         "opcijas": ["Mazināmais mīnus starpība", "Starpība mīnus atņēmējs",
                     "Mazināmais plus atņēmējs", "Nekāda"],
         "pareizi": 0, "padoms": "Jāsanāk atņēmējam."},
        {"jaut": "Cik ir 712 − 358?",
         "opcijas": ["354", "364", "344", "454"],
         "pareizi": 0, "padoms": "Divi aizņēmumi."},
    ], pamats=4),

    Pasaule("Vai rezultātu tabula ir pareiza?",
            Ievadi("", [
                {"jaut": "Bija 425 punkti, zaudēja 183. Cik palika?",
                 "atb": ["242"], "padoms": "425 − 183."},
                {"jaut": "Pārbaude: 242 + 183 = ?", "atb": ["425"],
                 "padoms": "Jāsanāk sākotnējam skaitlim."},
                {"jaut": "Nākamajā kārtā ieguva 158 punktus. Cik tagad ir?",
                 "atb": ["400"], "padoms": "242 + 158."},
                {"jaut": "Cik punktu pietrūkst līdz sākotnējiem 425?",
                 "atb": ["25"], "padoms": "425 − 400."},
            ]),
            pavediens="sports",
            konteksts="Punktu tabulu pārbauda pēc katras kārtas - un "
                      "pārbaude ir tā pati pretējā darbība.",
            kapec="Tabula, kuru nepārbauda, ātri kļūst nepareiza."),

    Kopsavilkums([
        "Pārbaudu atņemšanu ar saskaitīšanu.",
        "Zinu, ka starpība plus atņēmējs dod mazināmo.",
        "Zinu arī otru pārbaudi ar atņemšanu.",
        "Meklēju kļūdu aizņēmumos, ja pārbaude nesakrīt.",
    ]),

    Majas([
        "Izrēķini piecas starpības un pārbaudi katru.",
        "Atrodi kļūdu rēķinā 700 − 268 = 542 un izlabo to.",
        "Pārbaudi mājas čeka atlikumu.",
    ]),
]
