# -*- coding: utf-8 -*-
"""9. klase, 3. stunda: «Kā sadalīt nogriezni vienādās daļās?»

Konstrukcija ar cirkuli un lineālu: palīgstarā atliek n vienādus nogriežņus,
pēdējo galu savieno ar nogriežņa galu un velk tam paralēles. Talesa
teorēma garantē, ka daļas ir vienādas - arī tad, ja garums nedalās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā sadalīt nogriezni vienādās daļās?"

MERKIS = ("Sadalīsim nogriezni vienādās daļās ar cirkuli un lineālu un "
          "pamatosim to ar Talesa teorēmu.")

# Nogrieznis AB (garums 10) un palīgstars AC; uz stara trīs vienādi soļi.
_B = 10.0
_SOLIS = (2.2, 1.6)


def _konstrukcija(solis):
    """Konstrukcijas stāvoklis: 1 - stars, 2 - atzīmes, 3 - BC, 4 - paralēles."""
    punkti = [("A", 0, 0), ("B", _B, 0)]
    nogr, izc, svitras = [("A", "B")], [], []
    uz_stara = [("_1", _SOLIS[0], _SOLIS[1]),
                ("_2", 2 * _SOLIS[0], 2 * _SOLIS[1]),
                ("C", 3 * _SOLIS[0], 3 * _SOLIS[1])]
    punkti += uz_stara if solis >= 2 else [("_C", 3.6 * _SOLIS[0],
                                            3.6 * _SOLIS[1])]
    stari = [("A", "C" if solis >= 2 else "_C")]
    if solis >= 2:
        svitras = [(("A", "_1"), 1), (("_1", "_2"), 1), (("_2", "C"), 1)]
    if solis >= 3:
        izc.append(("C", "B"))
    if solis >= 4:
        for i, p in ((1, "_1"), (2, "_2")):
            punkti.append(("_P%d" % i, _B * i / 3.0, 0))
            izc.append((p, "_P%d" % i))
        svitras += [(("A", "_P1"), 2), (("_P1", "_P2"), 2),
                    (("_P2", "B"), 2)]
    return geometrija(punkti, nogriezni=nogr, stari=stari, izcelti=izc,
                      svitras=svitras)


SATURS = [
    Sakums("Kā 1 m garu dēli sadalīt 3 vienādās daļās?",
           zimejums=_konstrukcija(4),
           paraksts="100 : 3 = 33,333... cm - ar lineālu precīzi neatliksi.",
           fakti=["Ar cirkuli un lineālu to var izdarīt precīzi.",
                  "Skaitļi nav vajadzīgi - tikai paralēles.",
                  "To garantē Talesa teorēma."]),

    Slidnis("Konstrukcija pa soļiem", [
        {"v": "1. solis", "teksts": "No A velk palīgstaru jebkurā virzienā.",
         "zim": _konstrukcija(1)},
        {"v": "2. solis", "teksts": "Ar cirkuli uz stara atliek 3 vienādus "
                                    "nogriežņus.",
         "zim": _konstrukcija(2)},
        {"v": "3. solis", "teksts": "Pēdējo punktu C savieno ar B.",
         "zim": _konstrukcija(3)},
        {"v": "4. solis", "teksts": "Caur pārējiem punktiem velk paralēles "
                                    "BC. AB ir sadalīts 3 daļās.",
         "zim": _konstrukcija(4)},
    ]),

    Doma("Kāpēc daļas ir vienādas",
         "Paralēlas taisnes uz stara nogrieza vienādus nogriežņus - tātad "
         "arī uz AB tie ir vienādi (Talesa teorēma).",
         soli=[
             "Palīgstara virziens un soļa garums var būt jebkurš.",
             "Soļu skaits = daļu skaits.",
             "Paralēles velk ar lineālu un trijstūri vai konstruē leņķi.",
         ]),

    Petijums("Sadali pats", [
        "Uzzīmē nogriezni AB = 11 cm.",
        "Sadali to 5 vienādās daļās ar konstrukciju.",
        "Izmēri daļas ar lineālu. Cik cm tās ir?",
        "Salīdzini ar aprēķinu 11 : 5.",
    ], vajag="cirkulis, lineāls, zīmēšanas trijstūris",
       secinajums="Konstrukcija dod 2,2 cm daļas bez neviena aprēķina."),

    Varianti("Konstrukcijas jautājumi", [
        {"jaut": "Nogriezni dala 7 daļās. Cik nogriežņu atliek uz stara?",
         "opcijas": ["7", "6", "8", "Cik gribi"],
         "pareizi": 0, "padoms": "Soļu skaits = daļu skaits."},
        {"jaut": "Cik paralēles jāvelk, lai iegūtu 7 daļas (bez BC)?",
         "opcijas": ["6", "7", "5", "8"],
         "pareizi": 0, "padoms": "Starp 7 daļām ir 6 dalījuma punkti."},
        {"jaut": "Vai soļiem uz stara jābūt 1 cm gariem?",
         "opcijas": ["Nē, tikai vienādiem", "Jā", "Tie jāizmēra",
                     "Tiem jābūt garākiem par AB"],
         "pareizi": 0, "padoms": "Svarīgi, lai tie būtu vienādi."},
        {"jaut": "Kas notiks, ja līnijas nav paralēlas BC?",
         "opcijas": ["Daļas nebūs vienādas", "Nekas", "AB kļūs garāks",
                     "Daļas būs vienādas"],
         "pareizi": 0, "padoms": "Teorēmai vajag paralēles."},
    ]),

    Ievadi("Aprēķini daļu", [
        {"jaut": "AB = 14 cm dala 5 daļās. Viena daļa (cm)?", "atb": ["2,8"],
         "padoms": "14 : 5."},
        {"jaut": "AB = 10 cm dala 4 daļās. Cik cm ir no A līdz 3. dalījuma "
                 "punktam?", "atb": ["7,5"],
         "padoms": "3 daļas pa 2,5 cm."},
        {"jaut": "Nogrieznis sadalīts 6 daļās, katra 1,5 cm. AB (cm)?",
         "atb": ["9"], "padoms": "6 · 1,5."},
        {"jaut": "AB dala attiecībā 2 : 3. Cik soļu atliek uz stara?",
         "atb": ["5"], "padoms": "2 + 3."},
    ]),

    Pasaule("Plaukts trīs nodalījumos",
            Ievadi("", [
                {"jaut": "Plaukta iekšējais platums 100 cm. Starpsienas ir "
                         "plānas. Cik cm platas ir 3 vienādas daļas "
                         "(līdz desmitdaļām)?",
                 "atb": ["33,3"], "padoms": "100 : 3."},
                {"jaut": "Cik starpsienu vajag?", "atb": ["2"],
                 "padoms": "3 daļas - 2 robežas."},
                {"jaut": "Plauktu dala 4 daļās. Cik cm katra?", "atb": ["25"],
                 "padoms": "100 : 4."},
            ]),
            pavediens="maja",
            konteksts="Galdnieks uz dēļa slīpi pieliek mērlenti tā, lai 0 un "
                      "30 cm būtu pie malām, un atzīmē 10 un 20 cm.",
            kapec="Tā ir tā pati Talesa konstrukcija, tikai ar mērlenti."),

    Kopsavilkums([
        "Sadalu nogriezni n vienādās daļās ar cirkuli un lineālu.",
        "Pamatoju konstrukciju ar Talesa teorēmu.",
        "Sadalu nogriezni dotā attiecībā.",
    ]),

    Majas([
        "Sadali 13 cm nogriezni 3 vienādās daļās ar konstrukciju.",
        "Sadali 10 cm nogriezni attiecībā 2 : 3.",
        "Izmēģini galdnieka triku ar lineālu uz rūtiņu lapas.",
    ]),
]
