# -*- coding: utf-8 -*-
"""3. klase, 111. stunda: «Kā uzzīmēt četrstūri ar diviem taisniem leņķiem?»

Zīmēšana pēc nosacījumiem. Uzdevums ir atvērts - atbilstošu figūru ir daudz -,
un tieši tas māca lasīt nosacījumus precīzi: «divi taisni leņķi» nenozīmē ne
«tikai divi blakus», ne «taisnstūris».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kā uzzīmēt četrstūri ar diviem taisniem leņķiem?"

MERKIS = ("Zīmēsim vai veidosim daudzstūrus pēc dotām pazīmēm.")

SATURS = [
    Sakums("Vai četrstūrim visiem leņķiem jābūt taisniem?",
           zimejums=figura([(0, 0), (7, 0), (7, 4), (0, 6)],
                           [(3.5, -0.7, "a"), (7.8, 2, "b")],
                           "divi taisni leņķi"),
           paraksts="Kreisajā apakšā un labajā apakšā leņķi ir taisni, "
                    "augšējie - nē.",
           fakti=["Četrstūrim var būt 0, 1, 2, 3 vai 4 taisni leņķi.",
                  "Ja taisni ir visi četri, tas ir taisnstūris."]),

    Doma("Zīmē pa vienam nosacījumam",
         "Vispirms izpildi pirmo nosacījumu, tad otro - un tikai beigās "
         "pārbaudi visus kopā.",
         soli=[
             "Izlasi visus nosacījumus un pieraksti tos.",
             "Uzzīmē pirmo malu.",
             "Pievieno malu, kas veido prasīto leņķi.",
             "Noslēdz figūru un pārbaudi katru nosacījumu.",
         ],
         pieze="Ja atbilstošas figūras ir vairākas, tas nav trūkums - "
               "uzzīmē divas un salīdzini tās."),

    Petijums("Uzzīmē trīs dažādas figūras",
             vajag="rūtiņu lapa, lineāls un uzstūris",
             soli=[
                 "Uzzīmē četrstūri ar diviem taisniem leņķiem.",
                 "Uzzīmē otru, kas izskatās pavisam citādi.",
                 "Uzzīmē trešo ar tieši vienu taisnu leņķi.",
                 "Pārbaudi visus leņķus ar uzstūri.",
             ],
             secinajums="Vieniem un tiem pašiem nosacījumiem atbilst daudzas "
                        "dažādas figūras."),

    Paraugs("Kā uzzīmēt šādu figūru?",
            uzd="Uzzīmē četrstūri, kuram ir tieši divi taisni leņķi.",
            soli=[
                ("Uzzīmē apakšējo malu",
                 "No tās augs abi taisnie leņķi."),
                ("No abiem galiem uzzīmē malas uz augšu",
                 "Tie ir divi taisni leņķi."),
                ("Savieno augšējos galus ar slīpu malu",
                 "Augšējie leņķi nav taisni - nosacījums izpildīts."),
            ],
            atbilde="figūra ar diviem taisniem leņķiem"),

    Ievadi("Leņķi figūrās", [
        {"jaut": "Cik taisnu leņķu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Visi."},
        {"jaut": "Cik leņķu kopā ir četrstūrim?", "atb": ["4"],
         "padoms": "Tik, cik virsotņu."},
        {"jaut": "Cik leņķu nav taisni, ja no četriem divi ir taisni?",
         "atb": ["2"], "padoms": "4 − 2."},
        {"jaut": "Cik malu ir četrstūrim?", "atb": ["4"],
         "padoms": "Četras."},
        {"jaut": "Figūras malas 7, 4, 7 un 6 cm. Cik ir perimetrs?",
         "atb": ["24"], "padoms": "7 + 4 + 7 + 6."},
        {"jaut": "Cik virsotņu ir piecstūrim?", "atb": ["5"],
         "padoms": "Tik, cik malu."},
    ], pamats=4),

    Zimejums("Cita figūra ar to pašu pazīmi",
             figura([(0, 0), (6, 0), (6, 5), (3, 3)],
                    [(3, -0.7, "a"), (6.8, 2.5, "b")],
                    "arī divi taisni leņķi"),
             paskaidro="Nosacījums ir tas pats, bet figūra izskatās pavisam "
                       "citāda.",
             ievads="Salīdzini ar stundas sākuma zīmējumu."),

    Varianti("Vai figūra atbilst nosacījumam?", [
        {"jaut": "Cik taisnu leņķu var būt četrstūrim?",
         "opcijas": ["No 0 līdz 4", "Tikai 4", "Tikai 2", "Tikai 0"],
         "pareizi": 0, "padoms": "Visi varianti iespējami."},
        {"jaut": "Ja četrstūrim visi četri leņķi ir taisni, kas tas ir?",
         "opcijas": ["Taisnstūris", "Rombs", "Trīsstūris", "Trapece"],
         "pareizi": 0, "padoms": "Tā ir taisnstūra pazīme."},
        {"jaut": "Cik dažādu figūru atbilst nosacījumam «divi taisni "
                 "leņķi»?",
         "opcijas": ["Daudz", "Viena", "Divas", "Neviena"],
         "pareizi": 0, "padoms": "Malu garumi var būt dažādi."},
        {"jaut": "Ar ko pārbauda uzzīmēto leņķi?",
         "opcijas": ["Ar uzstūri", "Ar cirkuli", "Ar aci", "Ar lineālu"],
         "pareizi": 0, "padoms": "Uzstūrim ir taisns leņķis."},
    ], pamats=4),

    Pasaule("Kāda forma ir detaļai?",
            Ievadi("", [
                {"jaut": "Detaļai malas 12, 8, 12 un 5 cm. Cik ir perimetrs?",
                 "atb": ["37"], "padoms": "12 + 8 + 12 + 5."},
                {"jaut": "Cik tādu detaļu var izgriezt no 300 cm līstes?",
                 "atb": ["8"], "padoms": "8 · 37 = 296."},
                {"jaut": "Cik centimetru paliks pāri?", "atb": ["4"],
                 "padoms": "300 − 296."},
                {"jaut": "Cik taisnu leņķu ir 8 detaļām, ja katrai ir 2?",
                 "atb": ["16"], "padoms": "8 · 2."},
            ]),
            pavediens="tehnika",
            konteksts="Ne visas detaļas ir taisnstūri - daudzām ir arī slīpas "
                      "malas, lai tās ietilptu savā vietā.",
            kapec="Nosacījumi detaļai ir tie paši, kas uzdevumā: tie jāizpilda "
                  "visi."),

    Kopsavilkums([
        "Zīmēju daudzstūrus pēc dotām pazīmēm.",
        "Izpildu nosacījumus pa vienam.",
        "Pārbaudu visus nosacījumus gatavā zīmējumā.",
        "Zinu, ka vieniem nosacījumiem var atbilst daudzas figūras.",
    ]),

    Majas([
        "Uzzīmē četrstūri ar tieši vienu taisnu leņķi.",
        "Uzzīmē piecstūri ar diviem taisniem leņķiem.",
        "Pārbaudi visus leņķus ar papīra stūri.",
    ]),
]
