# -*- coding: utf-8 -*-
"""Matemātika, 3. klase. 3.7. Kā veido telpiskus modeļus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 3. klase, 3.7. temats): kubu, taisnstūru
skaldņu un piramīdu raksturošana ar terminiem virsotne, šķautne un skaldne,
telpisku figūru veidošana no izklājuma, cilindrs un konuss.
"""

PRIEKSMETS = "Matemātika  |  3. klase"
TEMATS = "3.7."
NOSAUKUMS = "Kā veido telpiskus modeļus?"

ATGADNE = [
    "Skaldne ir plaknes figūra uz virsmas   ·   šķautne ir divu skaldņu "
    "saskares līnija   ·   virsotne ir stūris",
    "Kubs:  6 skaldnes, 12 šķautnes, 8 virsotnes   ·   taisnstūru skaldnim "
    "tikpat",
    "Izklājums ir salocīta modeļa plaknes attēls; no tā salocot iegūst "
    "telpisku figūru.",
]

FD = {
    "veids": "fd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 3.7. temata beigās. Pārbauda telpisku "
                "figūru raksturošanu ar terminiem virsotne, šķautne un "
                "skaldne, kuba, taisnstūru skaldņa, piramīdas, cilindra un "
                "konusa atpazīšanu un izklājuma izpratni.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kas ir skaldne",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir skaldne?",
              ["plaknes figūra uz telpiskas figūras virsmas", "stūris",
               "līnija starp stūriem", "figūras krāsa"], 0),
             ("Cik skaldņu ir kubam?", ["4", "6", "8", "12"], 1),
             ("Kāda figūra ir kuba skaldne?",
              ["kvadrāts", "trijstūris", "riņķis", "piecstūris"], 0),
         ]},
        {"sr": "Zina, kas ir šķautne",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir šķautne?",
              ["divu skaldņu saskares līnija", "stūris", "skaldnes laukums",
               "figūras augstums"], 0),
             ("Cik šķautņu ir kubam?", ["6", "8", "12", "24"], 2),
             ("Cik šķautņu ir taisnstūru skaldnim?",
              ["6", "8", "12", "16"], 2),
         ]},
        {"sr": "Zina, kas ir virsotne",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir virsotne?",
              ["punkts, kur satiekas šķautnes", "skaldnes vidus", "līnija",
               "laukums"], 0),
             ("Cik virsotņu ir kubam?", ["4", "6", "8", "12"], 2),
             ("Cik virsotņu ir taisnstūru skaldnim?",
              ["4", "6", "8", "12"], 2),
         ]},
        {"sr": "Raksturo kubu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko kubs atšķiras no cita taisnstūru skaldņa?",
              ["visas skaldnes ir vienādi kvadrāti", "tam ir 4 skaldnes",
               "tam nav virsotņu", "tas ir apaļš"], 0),
             ("Cik kuba šķautņu ir vienāda garuma?",
              ["visas 12", "tikai 4", "tikai 6", "neviena"], 0),
             ("Kāda figūra rodas, ja kubu novieto uz galda un skatās no "
              "augšas?",
              ["kvadrāts", "trijstūris", "riņķis", "taisnstūris ar dažādām "
               "malām"], 0),
         ]},
        {"sr": "Raksturo taisnstūru skaldni",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir taisnstūru skaldņa skaldnes?",
              ["taisnstūri", "trijstūri", "riņķi", "piecstūri"], 0),
             ("Cik skaldņu ir taisnstūru skaldnim?", ["4", "6", "8", "12"],
              1),
             ("Kurš sadzīves priekšmets ir taisnstūru skaldnis?",
              ["kartona kaste", "bumba", "piltuve", "caurule"], 0),
         ]},
        {"sr": "Raksturo piramīdu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko piramīda atšķiras no skaldņa?",
              ["tai ir viena virsotne augšā", "tai nav skaldņu",
               "tā ir apaļa", "tai nav virsotņu"], 0),
             ("Kādas figūras ir piramīdas sānu skaldnes?",
              ["trijstūri", "kvadrāti", "riņķi", "sešstūri"], 0),
             ("Cik skaldņu ir piramīdai ar kvadrātveida pamatu?",
              ["4", "5", "6", "8"], 1),
         ]},
        {"sr": "Atpazīst cilindru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds sadzīves priekšmets ir cilindrs?",
              ["konservu kārba", "kartona kaste", "bumba", "piltuve"], 0),
             ("Kāda figūra ir cilindra pamats?",
              ["riņķis", "kvadrāts", "trijstūris", "taisnstūris"], 0),
             ("Cik virsotņu ir cilindram?", ["0", "2", "4", "8"], 0),
         ]},
        {"sr": "Atpazīst konusu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds priekšmets ir konuss?",
              ["saldējuma vafeles tūtiņa", "kartona kaste", "bumba",
               "konservu kārba"], 0),
             ("Kāds ir konusa pamats?",
              ["riņķis", "kvadrāts", "trijstūris", "piecstūris"], 0),
             ("Ar ko konuss beidzas augšā?",
              ["ar vienu virsotni", "ar kvadrātu", "ar riņķi",
               "ar taisnstūri"], 0),
         ]},
        {"sr": "Zina, kas ir izklājums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir izklājums?",
              ["plaknes attēls, no kura salocot iegūst telpisku figūru",
               "figūras ēna", "figūras laukums", "figūras tilpums"], 0),
             ("Cik kvadrātu ir kuba izklājumā?", ["4", "5", "6", "8"], 2),
             ("Ko dara ar izklājumu, lai iegūtu modeli?",
              ["saloka un salīmē", "sagriež gabalos", "nokrāso",
               "izmēra"], 0),
         ]},
        {"sr": "Nosaka figūru pēc izklājuma",
         "stunda": TEMATS,
         "jautajumi": [
             ("Izklājumā ir 6 vienādi kvadrāti. Kāda figūra sanāks?",
              ["kubs", "piramīda", "cilindrs", "konuss"], 0),
             ("Izklājumā ir kvadrāts un 4 trijstūri. Kāda figūra sanāks?",
              ["piramīda", "kubs", "cilindrs", "konuss"], 0),
             ("Izklājumā ir taisnstūris un 2 riņķi. Kāda figūra sanāks?",
              ["cilindrs", "kubs", "piramīda", "konuss"], 0),
         ]},
        {"sr": "Nosaka modelim vajadzīgo materiālu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik kociņu vajag kuba karkasam?", ["8", "10", "12", "16"], 2),
             ("Cik stiprinājumu (stūru) vajag kuba karkasam?",
              ["4", "6", "8", "12"], 2),
             ("Cik kociņu vajag taisnstūru skaldņa karkasam?",
              ["8", "10", "12", "16"], 2),
         ]},
        {"sr": "Salīdzina telpiskas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas kopīgs kubam un taisnstūru skaldnim?",
              ["6 skaldnes", "apaļa forma", "viena virsotne", "nav šķautņu"],
              0),
             ("Kura figūra var ripot?",
              ["cilindrs", "kubs", "taisnstūru skaldnis", "piramīda"], 0),
             ("Kurai figūrai nav neviena taisnstūra skaldnē?",
              ["konusam", "kubam", "skaldnim", "kastei"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 3,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 3.7. temata noslēgumā. "
                "Pārbauda telpisku figūru elementus (virsotne, šķautne, "
                "skaldne), kuba, skaldņa, piramīdas, cilindra un konusa "
                "atpazīšanu, izklājuma izpratni un modeļa veidošanai "
                "vajadzīgā materiāla aprēķinu.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Zīmē ar lineālu un risinājumu raksti tam atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina telpiskas figūras elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir šķautne?",
              ["divu skaldņu saskares līnija", "stūris", "laukums",
               "krāsa"], 0),
             ("Kas ir virsotne?",
              ["punkts, kur satiekas šķautnes", "skaldnes vidus", "līnija",
               "pamats"], 0),
             ("Kas ir skaldne?",
              ["plaknes figūra uz virsmas", "stūris", "līnija", "tilpums"],
              0),
         ]},
        {"sr": "Zina kuba elementu skaitu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik skaldņu ir kubam?", ["4", "6", "8", "12"], 1),
             ("Cik šķautņu ir kubam?", ["6", "8", "12", "24"], 2),
             ("Cik virsotņu ir kubam?", ["4", "6", "8", "12"], 2),
         ]},
        {"sr": "Atpazīst telpiskas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Konservu kārba ir …",
              ["cilindrs", "kubs", "piramīda", "konuss"], 0),
             ("Saldējuma tūtiņa ir …",
              ["konuss", "cilindrs", "kubs", "skaldnis"], 0),
             ("Kartona kaste ir …",
              ["taisnstūru skaldnis", "cilindrs", "konuss", "piramīda"], 0),
         ]},
        {"sr": "Raksturo piramīdu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir piramīdas sānu skaldnes?",
              ["trijstūri", "kvadrāti", "riņķi", "taisnstūri"], 0),
             ("Cik skaldņu ir piramīdai ar kvadrātveida pamatu?",
              ["4", "5", "6", "8"], 1),
             ("Ar ko piramīda beidzas augšā?",
              ["ar vienu virsotni", "ar kvadrātu", "ar riņķi",
               "ar šķautni"], 0),
         ]},
        {"sr": "Zina, kas ir izklājums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir izklājums?",
              ["plaknes attēls, no kura saloka telpisku figūru", "figūras ēna",
               "figūras laukums", "figūras tilpums"], 0),
             ("Cik kvadrātu ir kuba izklājumā?", ["4", "5", "6", "8"], 2),
             ("Izklājumā taisnstūris un 2 riņķi. Kāda figūra sanāks?",
              ["cilindrs", "kubs", "piramīda", "konuss"], 0),
         ]},
        {"sr": "Nosaka modeļa materiālu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik kociņu vajag kuba karkasam?", ["8", "10", "12", "16"], 2),
             ("Cik stūru stiprinājumu vajag kuba karkasam?",
              ["4", "6", "8", "12"], 2),
             ("Kura figūra var ripot?",
              ["cilindrs", "kubs", "skaldnis", "piramīda"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka telpisku figūru elementu skaitu",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Kubam ir …… skaldnes", "6"),
                         ("Kubam ir …… šķautnes", "12"),
                         ("Kubam ir …… virsotnes", "8"),
                         ("Piramīdai ar kvadrāta pamatu ir …… skaldnes",
                          "5")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Taisnstūru skaldnim ir …… skaldnes", "6"),
                         ("Taisnstūru skaldnim ir …… virsotnes", "8"),
                         ("Kuba izklājumā ir …… kvadrāti", "6"),
                         ("Cilindram ir …… virsotnes", "0")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Kuba karkasam vajag …… kociņus", "12"),
                         ("Kuba karkasam vajag …… stūra stiprinājumus", "8"),
                         ("Piramīdai ar kvadrāta pamatu ir …… virsotnes",
                          "5"),
                         ("Kubam ir …… šķautnes", "12")]},
         ]},
        {"sr": "Atpazīst figūru pēc izklājuma vai apraksta",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Uzraksti figūras nosaukumu",
              "note": "Ieraksti figūras nosaukumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Izklājumā 6 vienādi kvadrāti:  ……", "kubs"),
                         ("Izklājumā kvadrāts un 4 trijstūri:  ……",
                          "piramīda"),
                         ("Izklājumā taisnstūris un 2 riņķi:  ……",
                          "cilindrs")]},
             {"tips": "parveide", "virs": "Uzraksti figūras nosaukumu",
              "note": "Ieraksti figūras nosaukumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Visas skaldnes ir taisnstūri:  ……",
                          "taisnstūru skaldnis"),
                         ("Pamats ir riņķis, augšā viena virsotne:  ……",
                          "konuss"),
                         ("Visas skaldnes ir vienādi kvadrāti:  ……", "kubs")]},
             {"tips": "parveide", "virs": "Uzraksti figūras nosaukumu",
              "note": "Ieraksti figūras nosaukumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Konservu kārbas forma:  ……", "cilindrs"),
                         ("Saldējuma tūtiņas forma:  ……", "konuss"),
                         ("Kartona kastes forma:  ……",
                          "taisnstūru skaldnis")]},
         ]},
        {"sr": "Zīmē izklājumu un raksturo modeli",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Kuba modelis", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē kuba izklājumu (6 kvadrāti)!", 1),
                       ("Uzraksti, cik šķautņu ir kubam!", 1),
                       ("Uzraksti, cik virsotņu ir kubam!", 1),
                       ("Uzraksti, kāda figūra ir katra skaldne!", 1)],
              "atbildes": ["1) Uzzīmēti 6 vienādi kvadrāti izklājumā.   "
                           "(1 p.)",
                           "2) 12 šķautnes   (1 p.)", "3) 8 virsotnes   "
                           "(1 p.)",
                           "4) Katra skaldne ir kvadrāts.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Skaldņa modelis", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē taisnstūru skaldņa izklājumu!", 1),
                       ("Uzraksti, cik skaldņu ir skaldnim!", 1),
                       ("Uzraksti, cik šķautņu ir skaldnim!", 1),
                       ("Uzraksti, kāda figūra ir katra skaldne!", 1)],
              "atbildes": ["1) Uzzīmēts izklājums no 6 taisnstūriem.   "
                           "(1 p.)",
                           "2) 6 skaldnes   (1 p.)", "3) 12 šķautnes   "
                           "(1 p.)",
                           "4) Katra skaldne ir taisnstūris.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Piramīdas modelis", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē piramīdas izklājumu (kvadrāts un "
                        "4 trijstūri)!", 1),
                       ("Uzraksti, cik skaldņu ir piramīdai!", 1),
                       ("Uzraksti, cik virsotņu ir piramīdai!", 1),
                       ("Uzraksti, kāda figūra ir pamats!", 1)],
              "atbildes": ["1) Uzzīmēts kvadrāts ar 4 trijstūriem malās.   "
                           "(1 p.)",
                           "2) 5 skaldnes   (1 p.)", "3) 5 virsotnes   "
                           "(1 p.)",
                           "4) Pamats ir kvadrāts.   (1 p.)"]},
         ]},
        {"sr": "Plāno telpiska modeļa izveidi",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Modeļa plānošana", "vieta": 5.5,
              "ievads": "Kuba karkasu veido no kociņiem un plastilīna "
                        "bumbiņām stūros.",
              "jaut": [("Uzraksti, cik kociņu vajag!", 1),
                       ("Uzraksti, cik bumbiņu vajag!", 1),
                       ("Uzraksti, ko veido vispirms un ko pēc tam!", 1)],
              "atbildes": ["1) 12 kociņi   (1 p.)", "2) 8 bumbiņas   (1 p.)",
                           "3) Piemēram: vispirms pamata kvadrātu, tad sānu "
                           "šķautnes, tad augšu.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Modeļa plānošana", "vieta": 5.5,
              "ievads": "No kubiņiem jāsaliek taisnstūru skaldnis 3 × 2 × 2.",
              "jaut": [("Aprēķini, cik kubiņu ir vienā slānī!", 1),
                       ("Aprēķini, cik kubiņu vajag kopā!", 1),
                       ("Uzraksti, cik skaldņu ir gatavajam skaldnim!", 1)],
              "atbildes": ["1) 3 · 2 = 6   (1 p.)", "2) 6 · 2 = 12   (1 p.)",
                           "3) 6 skaldnes   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Modeļa plānošana", "vieta": 5.5,
              "ievads": "Cilindra modeli veido no papīra.",
              "jaut": [("Uzraksti, kādas figūras vajag izklājumā!", 1),
                       ("Uzraksti, cik riņķu vajag!", 1),
                       ("Uzraksti, ar ko cilindrs atšķiras no kuba!", 1)],
              "atbildes": ["1) Taisnstūris un divi riņķi.   (1 p.)",
                           "2) 2 riņķi   (1 p.)",
                           "3) Cilindram nav virsotņu un tas var ripot.   "
                           "(1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
