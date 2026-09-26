# -*- coding: utf-8 -*-
"""4. klase, 95. stunda: «Kā rīkoties, ja taisne nav gatava?»

Ne vienmēr taisne jau ir sadalīta. Skolēns pats izvēlas vienības garumu
(rūtiņās) tā, lai to var sadalīt saucēja daļās: {2|3} - vienība 3, 6 vai 9
rūtiņas; {3|4} un {1|6} vienā taisnē - 12 rūtiņas. Tā ir kopsaucēja ideja
bez vārda «kopsaucējs».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā rīkoties, ja taisne nav gatava?"

MERKIS = ("Papildināsim vai veidosim skaitļu taisni, lai atliktu doto "
          "daļu.")

SATURS = [
    Sakums("Cik rūtiņu ņemt vienībai?",
           zimejums=taisne(0, 1, 1, [(0.5, "1/2"), (1 / 3.0, "1/3")],
                           sikas=6),
           paraksts="6 rūtiņas dalās gan ar 2, gan ar 3.",
           fakti=["Ja vienība ir 5 rūtiņas, trešdaļu uzzīmēt nevar.",
                  "Izvēlies vienību, kas dalās ar visiem saucējiem."]),

    Doma("Vienības garums jādala ar saucēju",
         "Izvēlies vienības garumu rūtiņās, kas dalās ar saucēju (vai ar "
         "visiem saucējiem), tad sadali un atliec.",
         soli=[
             "Paskaties uz saucējiem: 3 un 4.",
             "Atrodi skaitli, kas dalās ar abiem: 12.",
             "Vienība - 12 rūtiņas; {1|3} = 4 rūtiņas, {1|4} = 3 rūtiņas.",
             "Atliec daļas un uzraksti tās.",
         ],
         pieze="Tā pati doma vēlāk palīdzēs daļas salīdzināt un saskaitīt."),

    Paraugs("{2|3} un {3|4} vienā taisnē",
            uzd="Uzzīmē taisni, kurā var atlikt gan {2|3}, gan {3|4}.",
            soli=[
                ("vienība 12 rūtiņas", "12 dalās ar 3 un 4."),
                ("{1|3} = 4 rūtiņas → {2|3} = 8 rūtiņas", None),
                ("{1|4} = 3 rūtiņas → {3|4} = 9 rūtiņas", None),
            ],
            atbilde="{2|3} pie 8., {3|4} pie 9. rūtiņas"),

    Zimejums("Taisne ar 12 iedaļām",
             taisne(0, 1, 1, [(8 / 12.0, "2/3"), (9 / 12.0, "3/4")],
                    sikas=12),
             paskaidro="{3|4} ir mazliet tālāk par {2|3} - par vienu "
                       "divpadsmitdaļu.",
             ievads="Divas daļas uz vienas taisnes."),

    Ievadi("Izvēlies vienību", [
        {"jaut": "Cik rūtiņu mazākais vienībai, lai atliktu {1|2} un {1|5}?",
         "atb": ["10"], "padoms": "Dalās ar 2 un 5."},
        {"jaut": "Vienība 12 rūtiņas. Cik rūtiņu ir {5|6}?", "atb": ["10"],
         "padoms": "{1|6} = 2 rūtiņas."},
        {"jaut": "Vienība 12 rūtiņas. Cik rūtiņu ir {1|4}?", "atb": ["3"],
         "padoms": "12 : 4."},
        {"jaut": "Mazākais vienības garums {1|3} un {1|4} kopā?",
         "atb": ["12"], "padoms": "Dalās ar 3 un 4."},
    ]),

    Varianti("Vai der?", [
        {"jaut": "Vienība 8 rūtiņas. Vai var atlikt {1|3}?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "8 nedalās ar 3."},
        {"jaut": "Vienība 8 rūtiņas. Vai var atlikt {3|4}?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "8 : 4 = 2."},
        {"jaut": "Kura vienība der {1|2}, {1|3} un {1|6}?",
         "opcijas": ["6 rūtiņas", "4 rūtiņas", "5 rūtiņas", "9 rūtiņas"],
         "pareizi": 0, "padoms": "6 dalās ar 2, 3 un 6."},
    ]),

    Pasaule("Mūzikas takts",
            Ievadi("", [
                {"jaut": "Takts ir vienība, sadalīta 4 ceturtdaļnotīs. Cik "
                         "ceturtdaļnošu vienā taktī?",
                 "atb": ["4"], "padoms": "{4|4} = 1."},
                {"jaut": "Astotdaļnots ir puse no ceturtdaļnots. Cik "
                         "astotdaļnošu taktī?",
                 "atb": ["8"], "padoms": "4 · 2."},
                {"jaut": "Taktī spēlēja 3 ceturtdaļnotis. Kāda daļa takts?",
                 "atb": ["3/4"], "vieta": "piem., 1/2",
                 "padoms": "3 no 4."},
                {"jaut": "Cik astotdaļnošu vēl trūkst līdz pilnai taktij?",
                 "atb": ["2"], "padoms": "Vēl viena ceturtdaļa = 2 "
                 "astotdaļas."},
            ]),
            pavediens="skola",
            konteksts="Mūzikā takts ir skaitļu taisne: ceturtdaļnotis un "
                      "astotdaļnotis ir tās daļas.",
            kapec="Pareizs dalījums ļauj ielikt taktī visas notis."),

    Kopsavilkums([
        "Izvēlos vienības garumu, kas dalās ar saucēju.",
        "Veidoju taisni, uz kuras var atlikt vairākas daļas.",
        "Paskaidroju, kāpēc 12 rūtiņas der trešdaļām un ceturtdaļām.",
    ]),

    Majas([
        "Uzzīmē taisni, uz kuras var atlikt {1|2}, {2|5} un {7|10}.",
        "Klausies dziesmu un sit taktī: 1, 2, 3, 4 - tās ir ceturtdaļas.",
        "Paskaidro, kāpēc vienība 10 rūtiņas neder trešdaļām.",
    ]),
]
