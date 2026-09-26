# -*- coding: utf-8 -*-
"""1. klase, 42. stunda: «Cik zīmuļu garš ir galds?»

Mērīt nozīmē noskaidrot, cik reižu vienība ietilpst garumā. Ar zīmuli galds
ir 6 garumi, ar dzēšgumiju - 12: jo mazāka vienība, jo lielāks skaitlis.
Laba vienība ir tāda, kas der mērāmajam priekšmetam un visiem ir vienāda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, vienibas)

TEMA = "Cik zīmuļu garš ir galds?"

MERKIS = ("Šodien mērīsim ar zīmuli, dzēšgumiju un plaukstu un spriedīsim, "
          "kura vienība ir laba.")

SATURS = [
    Sakums("Galds ir 6 zīmuļus garš. Cik dzēšgumiju?",
           zimejums=vienibas(6, "6 zīmuļi"),
           paraksts="Tas pats galds, bet vienība cita - cits skaitlis.",
           fakti=["Mērīt - noskaidrot, cik reižu vienība ietilpst.",
                  "Vienības liek cieši vienu aiz otras.",
                  "Mazāka vienība - lielāks skaitlis."]),

    Slidnis("Viens galds, trīs vienības", [
        {"v": "3", "teksts": "3 plaukstas", "zim": vienibas(3, "3 plaukstas")},
        {"v": "6", "teksts": "6 zīmuļi", "zim": vienibas(6, "6 zīmuļi")},
        {"v": "12", "teksts": "12 dzēšgumiju",
         "zim": vienibas(12, "12 dzēšgumiju")},
    ]),

    Doma("Kā mēra ar vienību",
         "Vienību liek no viena gala līdz otram bez spraugām un skaita.",
         soli=[
             "Noliec vienību pie paša galda gala.",
             "Nākamo liec cieši blakus - bez spraugas.",
             "Skaiti, cik vienību ietilpa.",
             "Pieraksti skaitli un vienību: 6 zīmuļi.",
         ]),

    Ievadi("Nolasi mērījumu", [
        {"jaut": "Cik zīmuļu garš ir sols?", "zim": vienibas(8), "atb": ["8"],
         "padoms": "Saskaiti daļas."},
        {"jaut": "Cik plaukstu garš ir plaukts?", "zim": vienibas(5),
         "atb": ["5"], "padoms": "Saskaiti daļas."},
        {"jaut": "Galds ir 3 plaukstas. Vienā plaukstā ietilpst 2 zīmuļi. Cik "
                 "zīmuļu?", "atb": ["6"], "padoms": "2 + 2 + 2."},
    ]),

    Varianti("Kura vienība laba?", [
        {"jaut": "Ar ko mērīt klases garumu?",
         "opcijas": ["ar soļiem", "ar dzēšgumiju", "ar pirkstu"],
         "pareizi": 0, "padoms": "Garam - liela vienība."},
        {"jaut": "Ar ko mērīt grāmatas platumu?",
         "opcijas": ["ar dzēšgumiju", "ar soļiem", "ar galdu"],
         "pareizi": 0, "padoms": "Mazam - maza vienība."},
        {"jaut": "Kurā mērījumā būs lielāks skaitlis - ar zīmuli vai "
                 "dzēšgumiju?",
         "opcijas": ["ar dzēšgumiju", "ar zīmuli", "vienāds"],
         "pareizi": 0, "padoms": "Mazāka vienība ietilpst vairāk reižu."},
    ]),

    Petijums("Izmēri savu solu", [
        "Izmēri sola garumu ar zīmuli.",
        "Izmēri to pašu ar plaukstu.",
        "Salīdzini ar blakus sēdētāja plaukstu mērījumu.",
        "Kāpēc skaitļi atšķiras?",
    ], vajag="zīmulis, dzēšgumija, tava plauksta"),

    Pasaule("Paklājs istabā",
            Ievadi("", [
                {"jaut": "Tētis izmērīja paklāju: 4 soļi. Dēls - 6 soļi. Kurš "
                         "skaitlis lielāks?", "atb": ["6"],
                 "padoms": "Bērna solis ir īsāks."},
                {"jaut": "Par cik soļiem vairāk nomēra dēls?", "atb": ["2"],
                 "padoms": "6 − 4."},
            ]),
            pavediens="maja",
            konteksts="Tētis un dēls mēra vienu paklāju ar saviem soļiem.",
            kapec="Dažādi soļi - dažādi skaitļi: vienībai jābūt vienādai."),

    Kopsavilkums([
        "Mēru ar izvēlētu vienību.",
        "Lieku vienības cieši vienu aiz otras.",
        "Zinu, ka mazāka vienība dod lielāku skaitli.",
    ]),

    Majas([
        "Izmēri gultas garumu ar pēdām. Cik sanāca?",
        "Lai mājinieks izmēra to pašu ar savām pēdām.",
        "Kāpēc skaitļi atšķiras?",
    ]),
]
