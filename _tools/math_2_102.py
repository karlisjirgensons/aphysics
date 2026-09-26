# -*- coding: utf-8 -*-
"""2. klase, 102. stunda: «Kā uzzīmēt pēc pieraksta?»

Lauzta līnija rūtiņu lapā pēc algoritma ar atkārtojumu: «atkārto 3 reizes:
2 pa labi, 1 uz augšu». Atkārtojums (cikls) saīsina pierakstu - to pašu
lieto programmēšanā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, celjs)

TEMA = "Kā uzzīmēt pēc pieraksta?"

MERKIS = ("Šodien rūtiņu lapā veidosim lauztu līniju pēc dota algoritma ar "
          "atkārtojumu.")

SATURS = [
    Sakums("Kā ar vienu teikumu aprakstīt kāpnes?",
           zimejums=celjs(7, 4, (0, 3), None, "→→↑→→↑→→↑"),
           paraksts="Atkārto 3 reizes: 2 pa labi, 1 uz augšu.",
           fakti=["Vienādas daļas atkārtojas.",
                  "Pieraksts ar atkārtojumu ir īsāks.",
                  "Programmētāji to sauc par ciklu."]),

    Doma("Atkārtojums",
         "«Atkārto N reizes: ...» nozīmē izpildīt tos pašus soļus N reizes.",
         soli=[
             "Izlasi, kas jāatkārto.",
             "Izpildi šos soļus vienu reizi.",
             "Atkārto, līdz izpildīts N reizes.",
             "Saskaiti, cik soļu kopā.",
         ]),

    Slidnis("Kāpnes aug", [
        {"v": "1 reize", "teksts": "→→↑", "zim": celjs(7, 4, (0, 3), None,
                                                       "→→↑")},
        {"v": "2 reizes", "teksts": "→→↑ →→↑",
         "zim": celjs(7, 4, (0, 3), None, "→→↑→→↑")},
        {"v": "3 reizes", "teksts": "→→↑ →→↑ →→↑",
         "zim": celjs(7, 4, (0, 3), None, "→→↑→→↑→→↑")},
    ]),

    Ievadi("Cik soļu?", [
        {"jaut": "«Atkārto 3 reizes: 2 pa labi, 1 uz augšu.» Cik soļu "
                 "kopā?", "atb": ["9"], "padoms": "3 soļi, 3 reizes."},
        {"jaut": "«Atkārto 4 reizes: 1 pa labi, 1 uz leju.» Cik soļu?",
         "atb": ["8"], "padoms": "2 + 2 + 2 + 2."},
        {"jaut": "«Atkārto 5 reizes: 2 pa labi.» Cik rūtiņas pa labi?",
         "atb": ["10"], "padoms": "2 + 2 + 2 + 2 + 2."},
        {"jaut": "Kāpnes ar 3 pakāpieniem pa 2 rūtiņām. Cik rūtiņu augstas?",
         "zim": celjs(7, 4, (0, 3), None, "→→↑→→↑→→↑"), "atb": ["3"],
         "padoms": "Katrā reizē 1 uz augšu."},
    ]),

    Varianti("Kurš pieraksts der?", [
        {"jaut": "Līnija: →↑→↑→↑→↑",
         "opcijas": ["Atkārto 4 reizes: →↑", "Atkārto 2 reizes: →↑",
                     "Atkārto 4 reizes: ↑↑"], "pareizi": 0,
         "padoms": "«→↑» ir 4 reizes."},
        {"jaut": "Līnija: →→↓→→↓",
         "opcijas": ["Atkārto 2 reizes: →→↓", "Atkārto 3 reizes: →→↓",
                     "Atkārto 2 reizes: →↓"], "pareizi": 0,
         "padoms": "«→→↓» ir 2 reizes."},
    ]),

    Pasaule("Robots krāso žogu",
            Ievadi("", [
                {"jaut": "Robots: «Atkārto 6 reizes: nokrāso dēli, pārej "
                         "uz nākamo.» Cik dēļu nokrāsos?", "atb": ["6"],
                 "padoms": "Viens katrā reizē."},
                {"jaut": "Žogā 20 dēļi. Cik reizes jāatkārto?", "atb": ["20"],
                 "padoms": "Katram dēlim viena reize."},
            ]),
            pavediens="tehnika",
            konteksts="Roboti bieži dara vienu un to pašu daudzas reizes.",
            kapec="Cikls ļauj uzrakstīt garu darbu ar vienu rindu."),

    Kopsavilkums([
        "Izpildu algoritmu ar atkārtojumu.",
        "Zīmēju lauztu līniju rūtiņu lapā.",
        "Saskaitu soļus.",
    ]),

    Majas([
        "Rūtiņu lapā izpildi: atkārto 4 reizes: 1 pa labi, 2 uz augšu, "
        "1 pa labi, 2 uz leju.",
        "Ko tu uzzīmēji?",
        "Izdomā savu atkārtojuma algoritmu.",
    ]),
]
