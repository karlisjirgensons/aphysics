# -*- coding: utf-8 -*-
"""5. klase, 167. stunda: «Kas notiek starp diviem punktiem?»

Temata pēdējā stunda pirms pārbaudes darba. Tā atgriežas pie 158. stundas
jautājuma, bet no otras puses: ja punkti ir savienoti, ko tieši šī līnija
apgalvo? Atbilde ir godīgāka, nekā gaidīts - tā ir pieņēmums, ne mērījums,
un tieši to skolēns arī iemācās pateikt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kas notiek starp diviem punktiem?"

MERKIS = ("Mācīsimies spriest, kā mainās lielums starp diviem attēlotajiem "
          "punktiem, un pamatot savu pieņēmumu.")

SATURS = [
    Sakums("Divi mērījumi, viena līnija",
           zimejums=plakne(lauzta=[(0, 4), (3, 16)], no_x=0, lidz_x=5,
                           no_y=0, lidz_y=20, solis=4,
                           virsraksts="Tikai divi mērījumi"),
           paraksts="Līnija starp tiem ir pieņēmums, nevis mērījums.",
           fakti=["Izmērīti tikai divi punkti.",
                  "Starp tiem temperatūra varēja mainīties dažādi.",
                  "Taisna līnija ir vienkāršākais pieņēmums."]),

    Doma("Līnija starp punktiem ir pieņēmums",
         "Savienojot divus mērījumus ar taisnu līniju, pieņem, ka lielums "
         "starp tiem mainījās vienmērīgi; patiesībā tā var arī nebūt.",
         soli=[
             "Atrodi abus izmērītos punktus.",
             "Novērtē, kā lielums varētu mainīties starp tiem.",
             "Taisna līnija nozīmē vienmērīgu izmaiņu.",
             "Pārbaudi, vai tas ir ticams šim lielumam.",
             "Pieraksti savu pieņēmumu vārdiem.",
         ],
         pieze="Jo biežāk mēra, jo mazāk jāpieņem. Ar mērījumu katru stundu "
               "līnija ir gandrīz patiesa; ar diviem mērījumiem dienā tā ir "
               "tikai minējums."),

    Paraugs("No 4° līdz 16°",
            uzd="Rītā 4°, pēcpusdienā 16°. Ko var pateikt par vidu?",
            soli=[
                ("Izmērīti tikai divi punkti",
                 "Rīts un pēcpusdiena."),
                ("Ja pieņem vienmērīgu siltēšanu, vidū bija 10°",
                 "Taisna līnija."),
                ("Bet varēja būt arī citādi",
                 "Piemēram, strauja siltēšana no rīta."),
                ("Tas ir pieņēmums, ne mērījums",
                 "To jāpasaka atklāti."),
            ],
            atbilde="Vidū apmēram 10°, ja izmaiņa bija vienmērīga"),

    Ievadi("Novērtē starpvērtību", [
        {"jaut": "Rītā 4°, pēcpusdienā 16°. Cik grādu ir starpība?",
         "atb": ["12"], "padoms": "16 - 4."},
        {"jaut": "Ja izmaiņa bija vienmērīga, cik grādu bija vidū?",
         "atb": ["10"], "padoms": "(4 + 16) : 2."},
        {"jaut": "Sākumā 10 km, beigās 50 km. Cik kilometru ir starpība?",
         "atb": ["40"], "padoms": "50 - 10."},
        {"jaut": "Ja kustība bija vienmērīga, cik kilometru bija vidū?",
         "atb": ["30"], "padoms": "(10 + 50) : 2."},
        {"jaut": "Sākumā 0 €, beigās 20 €. Cik eiro bija vidū?",
         "atb": ["10"], "padoms": "(0 + 20) : 2."},
        {"jaut": "Vai starpvērtība ir izmērīta? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Tas ir pieņēmums."},
        {"jaut": "Sākumā 6°, beigās 14°. Cik grādu bija vidū, ja izmaiņa "
                 "vienmērīga?",
         "atb": ["10"], "padoms": "(6 + 14) : 2."},
        {"jaut": "Kas padara pieņēmumu drošāku - biežāki vai retāki "
                 "mērījumi? Raksti «biežāki» vai «retāki».",
         "atb": ["biežāki", "biezaki"], "padoms": "Mazāk jāpieņem."},
    ], pamats=4,
        ievads="Vidējo starp diviem punktiem atrod kā to summas pusi."),

    Zimejums("Ar vairāk mērījumiem",
             plakne(lauzta=[(0, 4), (1, 6), (2, 13), (3, 16)], no_x=0,
                    lidz_x=5, no_y=0, lidz_y=20, solis=4,
                    virsraksts="Četri mērījumi tajā pašā dienā"),
             paskaidro="Ar četriem mērījumiem redzams, ka siltēšana nebija "
                       "vienmērīga: starp otro un trešo tā bija daudz "
                       "straujāka.",
             ievads="Tā pati diena, bet mērīts biežāk."),

    Varianti("Ko līnija apgalvo?", [
        {"jaut": "Ko nozīmē taisna līnija starp diviem mērījumiem?",
         "opcijas": ["Pieņēmumu, ka izmaiņa bija vienmērīga",
                     "Ka starp tiem mērīts katru minūti",
                     "Ka lielums nemainījās",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Mērījumu tur nav."},
        {"jaut": "Rītā 4°, pēcpusdienā 16°. Cik bija vidū, ja izmaiņa "
                 "vienmērīga?",
         "opcijas": ["10°", "12°", "8°", "20°"],
         "pareizi": 0,
         "padoms": "(4 + 16) : 2."},
        {"jaut": "Kas padara pieņēmumu drošāku?",
         "opcijas": ["Biežāki mērījumi", "Garāka līnija",
                     "Lielākas iedaļas", "Nekas"],
         "pareizi": 0,
         "padoms": "Mazāk neizmērītu vietu."},
        {"jaut": "Vai starpvērtība ir mērījums?",
         "opcijas": ["Nav, tas ir pieņēmums", "Ir", "Ir, ja līnija ir taisna",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Mērīti tikai divi punkti."},
        {"jaut": "Sākumā 10 km, beigās 50 km. Cik bija vidū vienmērīgā "
                 "kustībā?",
         "opcijas": ["30 km", "40 km", "25 km", "60 km"],
         "pareizi": 0,
         "padoms": "(10 + 50) : 2."},
        {"jaut": "Kas jāpieraksta pie secinājuma?",
         "opcijas": ["Ka tas ir pieņēmums", "Ka tas ir mērījums",
                     "Mērvienība", "Nekas"],
         "pareizi": 0,
         "padoms": "Godīgs secinājums nosauc savu pamatu."},
    ], pamats=4),

    Pasaule("Cik silts bija pusdienlaikā?",
            Ievadi("", [
                {"jaut": "Rītā 6°, vakarā 14°. Cik grādu ir starpība?",
                 "atb": ["8"], "padoms": "14 - 6."},
                {"jaut": "Cik grādu bija vidū, ja izmaiņa vienmērīga?",
                 "atb": ["10"], "padoms": "(6 + 14) : 2."},
                {"jaut": "Nākamajā dienā rītā 2°, vakarā 12°. Cik bija vidū?",
                 "atb": ["7"], "padoms": "(2 + 12) : 2."},
                {"jaut": "Cik grādu ir šīs dienas svārstība?",
                 "atb": ["10"], "padoms": "12 - 2."},
            ]),
            pavediens="planeta",
            konteksts="Laika stacijas mēra reizi stundā, bet ziņās rāda "
                      "gludu līniju - starp mērījumiem tā ir uzzīmēta.",
            kapec="Zināt, kur beidzas mērījums un sākas pieņēmums, ir daļa "
                  "no prasmes lasīt grafiku."),

    Kopsavilkums([
        "Spriežu, kā lielums mainās starp diviem attēlotajiem punktiem.",
        "Aprēķinu starpvērtību, pieņemot vienmērīgu izmaiņu.",
        "Pamatoju savu pieņēmumu vārdiem.",
        "Atšķiru mērījumu no pieņēmuma.",
    ]),

    Majas([
        "Atrodi grafiku ar diviem mērījumiem un novērtē starpvērtību.",
        "Pieraksti, kāds pieņēmums tam vajadzīgs.",
        "Sagatavojies pārbaudes darbam: pārskati 156.-166. stundas "
        "kopsavilkumus.",
    ]),
]
