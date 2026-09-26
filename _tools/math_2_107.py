# -*- coding: utf-8 -*-
"""2. klase, 107. stunda: «Cik dažādi var dalīt uz pusēm?»

Figūru var sadalīt divās vienādās daļās dažādos veidos: kvadrātu - pa
vidu (divi veidi) un pa diagonālēm (vēl divi). Rūtiņu tīklā ir arī
«kāpņu» griezumi, kas dod vienādas, bet neregulāras puses.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija,
                         restis)

TEMA = "Cik dažādi var dalīt uz pusēm?"

MERKIS = ("Šodien dalīsim figūru divās vienādās daļās dažādos veidos un "
          "salīdzināsim risinājumus.")

_KV = [("_A", 0, 0), ("_B", 4, 0), ("_C", 4, 4), ("_D", 0, 4),
       ("_M", 2, 0), ("_N", 2, 4), ("_K", 0, 2), ("_L", 4, 2)]
_MALAS = [("_A", "_B"), ("_B", "_C"), ("_C", "_D"), ("_D", "_A")]


def _kvadrats(griezums):
    return geometrija(_KV, nogriezni=_MALAS + [griezums],
                      iekrasot=[(["_A", "_B", "_C", "_D"], 0)])


SATURS = [
    Sakums("Cik veidos var pārgriezt maizes šķēli uz pusēm?",
           zimejums=_kvadrats(("_A", "_C")),
           paraksts="Pa diagonāli - divi vienādi trijstūri.",
           fakti=["Kvadrātu var pārgriezt pa vidu - stateniski vai "
                  "līmeniski.",
                  "Var arī pa abām diagonālēm.",
                  "Rūtiņās ir vēl citi veidi!"]),

    Doma("Uz pusēm",
         "Abām daļām jābūt vienādām - tām jāsakrīt, uzliekot vienu uz otras.",
         soli=[
             "Novelc griezuma līniju.",
             "Saskaiti katras daļas rūtiņas - jābūt vienādi.",
             "Pārbaudi, vai daļas sakrīt, pagriežot.",
             "Meklē vēl citu veidu.",
         ]),

    Slidnis("Četri vienkāršie veidi", [
        {"v": "stateniski", "teksts": "Divi taisnstūri.",
         "zim": _kvadrats(("_M", "_N"))},
        {"v": "līmeniski", "teksts": "Divi taisnstūri.",
         "zim": _kvadrats(("_K", "_L"))},
        {"v": "diagonāle", "teksts": "Divi trijstūri.",
         "zim": _kvadrats(("_A", "_C"))},
        {"v": "otra diagonāle", "teksts": "Atkal divi trijstūri.",
         "zim": _kvadrats(("_B", "_D"))},
    ]),

    Varianti("Vai tās ir puses?", [
        {"jaut": "Rūtiņas: 1 - pirmā daļa, 2 - otrā. Vai puses?",
         "zim": restis([[1, 1, 1, 2], [1, 2, 2, 2]]),
         "opcijas": ["Jā - katrā 4 rūtiņas", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "Saskaiti 1 un 2."},
        {"jaut": "Vai šīs ir puses?",
         "zim": restis([[1, 1, 1, 2], [1, 1, 2, 2]]),
         "opcijas": ["Nē - 5 un 3", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Saskaiti 1 un 2."},
    ]),

    Ievadi("Cik rūtiņu pusē?", [
        {"jaut": "Taisnstūrī 8 rūtiņas. Cik rūtiņu katrā pusē?",
         "atb": ["4"], "padoms": "4 + 4."},
        {"jaut": "Taisnstūrī 16 rūtiņas. Cik rūtiņu pusē?", "atb": ["8"],
         "padoms": "8 + 8."},
        {"jaut": "Cik vienkāršos veidos kvadrātu var pārgriezt uz pusēm ar "
                 "vienu taisnu griezienu caur vidu, ja skaita tikai "
                 "stateniski, līmeniski un pa diagonālēm?", "atb": ["4"],
         "padoms": "2 pa vidu un 2 pa diagonālēm."},
    ]),

    Petijums("Kāpņu griezumi", [
        "Uzzīmē taisnstūri 4 rūtiņas garu un 2 augstu.",
        "Sadali to uz pusēm pa rūtiņu līnijām - kā kāpnes.",
        "Atrodi vēl vismaz 2 citus veidus.",
        "Salīdzini ar klasesbiedru - kuram vairāk veidu?",
    ], vajag="rūtiņu lapa, krāsainie zīmuļi"),

    Pasaule("Pica diviem",
            Varianti("", [
                {"jaut": "Kvadrātveida picu jāsadala 2 draugiem. Kurš "
                         "griezums nav godīgs?",
                 "opcijas": ["tuvu pie malas", "pa vidu", "pa diagonāli"],
                 "pareizi": 0, "padoms": "Daļas nesanāks vienādas."},
            ]),
            pavediens="virtuve",
            konteksts="Pica jāsadala tā, lai neviens nesūdzētos.",
            kapec="Uz pusēm - tas nozīmē vienādi."),

    Kopsavilkums([
        "Dalu figūru divās vienādās daļās dažādos veidos.",
        "Pārbaudu, vai daļas vienādas.",
        "Salīdzinu dažādus risinājumus.",
    ]),

    Majas([
        "Sagriez 3 papīra kvadrātus uz pusēm trīs dažādos veidos.",
        "Pārbaudi, uzliekot daļas vienu uz otras.",
        "Parādi mājiniekam.",
    ]),
]
