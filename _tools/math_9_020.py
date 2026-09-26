# -*- coding: utf-8 -*-
"""9. klase, 20. stunda: «Kā definē trapeci?»

Trapece ir četrstūris ar tieši vienu paralēlu malu pāri. Stunda sākas ar
dambi: tā šķērsgriezums ir trapece, jo ūdens spiediens apakšā ir lielāks.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija,
                         trapece)

TEMA = "Kā definē trapeci?"

MERKIS = ("Definēsim trapeci un nosauksim tās pamatus, sānu malas un "
          "augstumu.")

def _trapece(izcelti=(), malas=(), augstums=False):
    return geometrija(trapece(10, 5, 4, nobide=2, pedas=augstums)
                      [:5 if augstums else 4],
                      nogriezni=TRAPECES_MALAS,
                      izcelti=list(izcelti) + (["DH"] if augstums else []),
                      taisni=["DHB"] if augstums else [],
                      malas=list(malas))


SATURS = [
    Sakums("Kāpēc dambis apakšā ir platāks?",
           zimejums=_trapece(malas=[("AB", "plats"),
                                    ("DC", "šaurs")]),
           paraksts="Dambja šķērsgriezums - trapece.",
           fakti=["Dziļumā ūdens spiež stiprāk - vajag biezāku sienu.",
                  "Tāpēc dambja siena lejup kļūst arvien biezāka.",
                  "Trapecei tieši divas malas ir paralēlas."]),

    Doma("Trapece",
         "Trapece ir četrstūris, kuram tieši divas malas ir paralēlas.",
         soli=[
             "Paralēlās malas sauc par pamatiem: AB ∥ DC.",
             "Pārējās divas malas (AD un BC) - sānu malas.",
             "Augstums - perpendikuls starp pamatiem (DH).",
             "Paralelograms NAV trapece: tam paralēli ir divi malu pāri.",
         ]),

    Slidnis("Trapeces elementi", [
        {"v": "Pamati", "teksts": "AB un DC ir paralēli - tie ir pamati",
         "zim": _trapece(izcelti=["AB", "DC"])},
        {"v": "Sānu malas", "teksts": "AD un BC nav paralēlas - sānu malas",
         "zim": _trapece(izcelti=["AD", "BC"])},
        {"v": "Augstums", "teksts": "DH ⊥ AB - trapeces augstums",
         "zim": _trapece(augstums=True)},
    ]),

    Varianti("Trapece vai nē?", [
        {"jaut": "Četrstūrim tieši divas malas ir paralēlas.",
         "opcijas": ["Trapece", "Paralelograms", "Rombs", "Nav četrstūris"],
         "pareizi": 0, "padoms": "Definīcija."},
        {"jaut": "Četrstūrim abi pretējo malu pāri ir paralēli.",
         "opcijas": ["Paralelograms, nevis trapece", "Trapece",
                     "Vienādsānu trapece", "Trijstūris"],
         "pareizi": 0, "padoms": "Tieši vienam pārim jābūt paralēlam."},
        {"jaut": "Kas ir trapeces augstums?",
         "opcijas": ["Perpendikuls starp pamatiem", "Sānu mala",
                     "Diagonāle", "Garākais pamats"],
         "pareizi": 0, "padoms": "Attālums starp paralēlajām taisnēm."},
        {"jaut": "Vai kvadrāts ir trapece?",
         "opcijas": ["Nē", "Jā", "Tikai liels", "Dažreiz"],
         "pareizi": 0, "padoms": "Tam ir divi paralēlu malu pāri."},
    ]),

    Ievadi("Nosauc un aprēķini", [
        {"jaut": "Trapecē ABCD AB ∥ DC. Kura mala ir otrs pamats, ja viens "
                 "ir AB?", "atb": ["DC", "CD"], "tastatura": "text",
         "padoms": "Paralēlā mala."},
        {"jaut": "Pamati 10 cm un 6 cm, sānu malas 5 cm un 4 cm. Perimetrs "
                 "(cm)?", "atb": ["25"], "padoms": "10 + 6 + 5 + 4."},
        {"jaut": "Perimetrs 30 cm, pamati 12 cm un 8 cm, sānu malas vienādas. "
                 "Sānu mala (cm)?", "atb": ["5"], "padoms": "(30 − 20) : 2."},
        {"jaut": "Cik virsotņu ir trapecei?", "atb": ["4"],
         "padoms": "Četrstūris."},
    ]),

    Pasaule("Dambja šķērsgriezums",
            Ievadi("", [
                {"jaut": "Dambja apakšējais pamats 60 m, augšējais 10 m. Par "
                         "cik m apakšā ir platāks?", "atb": ["50"],
                 "padoms": "60 − 10."},
                {"jaut": "Dambis simetrisks. Cik m katrā pusē apakšā "
                         "«izvirzās» ārpus augšas?", "atb": ["25"],
                 "padoms": "50 : 2."},
            ]),
            pavediens="planeta",
            konteksts="Hidroelektrostacijas dambis notur ūdens spiedienu, kas "
                      "ar dziļumu pieaug.",
            kapec="Trapece ir izturīga forma: plata tur, kur slodze lielāka."),

    Kopsavilkums([
        "Definēju trapeci.",
        "Nosaucu pamatus, sānu malas un augstumu.",
        "Atšķiru trapeci no paralelograma.",
    ]),

    Majas([
        "Atrodi trīs trapeces savā apkārtnē (soma, logs, jumts).",
        "Uzzīmē trapeci un novelc divus dažādus augstumus.",
        "Vai trapecei var būt trīs vienādas malas? Uzzīmē.",
    ]),
]
