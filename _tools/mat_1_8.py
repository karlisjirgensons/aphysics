# -*- coding: utf-8 -*-
"""Matemātika, 1. klase. 1.8. Kā apraksta un veido figūras?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 1. klase, 1.8. temats): figūras būtiskās
un mazāk svarīgās īpašības, figūras apraksts un atpazīšana pēc apraksta,
simetrija (arī vairākas asis), četrstūru dažādība, figūras dalīšana vienādās
daļās, telpiskas figūras un to skati, algoritms kvadrāta zīmēšanai rūtiņu
lapā, figūru grupēšana.
"""

PRIEKSMETS = "Matemātika  |  1. klase"
TEMATS = "1.8."
NOSAUKUMS = "Kā apraksta un veido figūras?"

ATGADNE = [
    "Būtiskas īpašības:  malu un virsotņu skaits, vai figūra ir noslēgta   "
    "·   mazāk svarīgas:  krāsa, lielums, novietojums",
    "Trijstūris — 3 malas   ·   četrstūris — 4 malas   ·   kvadrāts — "
    "četrstūris ar vienāda garuma malām",
    "Figūra ir simetriska, ja to var pārlocīt uz pusēm tā, ka abas puses "
    "sakrīt.   ·   Algoritms ir soļu virkne.",
]

FD = {
    "veids": "fd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 1.8. temata beigās. Pārbauda figūras "
                "būtiskās un mazāk svarīgās īpašības, figūras atpazīšanu pēc "
                "apraksta, simetriju, četrstūru dažādību, figūras dalīšanu "
                "vienādās daļās, telpiskas figūras un algoritma pierakstu.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Atšķir figūras būtiskās īpašības no mazāk svarīgām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura īpašība trijstūrim ir būtiska?",
              ["tam ir 3 malas", "tas ir zils", "tas ir liels",
               "tas ir uzzīmēts lapas vidū"], 0),
             ("Kas notiek ar trijstūri, ja to nokrāso citā krāsā?",
              ["tas paliek trijstūris", "tas kļūst par četrstūri",
               "tas vairs nav figūra", "tam pazūd viena mala"], 0),
             ("Kura īpašība NAV būtiska četrstūrim?",
              ["tā lielums", "malu skaits", "virsotņu skaits",
               "tas ir noslēgts"], 0),
         ]},
        {"sr": "Atpazīst figūru pēc apraksta",
         "stunda": TEMATS,
         "jautajumi": [
             ("Figūrai ir 3 malas un 3 virsotnes. Kura tā ir?",
              ["trijstūris", "četrstūris", "piecstūris", "riņķis"], 0),
             ("Figūrai ir 4 vienāda garuma malas. Kura tā ir?",
              ["trijstūris", "kvadrāts", "piecstūris", "riņķis"], 1),
             ("Figūrai nav ne malu, ne virsotņu. Kura tā ir?",
              ["trijstūris", "četrstūris", "riņķis", "kvadrāts"], 2),
         ]},
        {"sr": "Apraksta figūru ar tās īpašībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā vislabāk aprakstīt figūru, lai cits to atpazītu?",
              ["nosaukt malu un virsotņu skaitu", "nosaukt tās krāsu",
               "pateikt, kur tā zīmēta", "pateikt, cik tā skaista"], 0),
             ("Cik virsotņu ir piecstūrim?", ["3", "4", "5", "6"], 2),
             ("Kurš apraksts der kvadrātam?",
              ["4 malas, visas vienāda garuma", "3 malas", "5 virsotnes",
               "nav malu"], 0),
         ]},
        {"sr": "Nosaka, vai figūra ir simetriska",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad figūra ir simetriska?",
              ["ja to var pārlocīt tā, ka abas puses sakrīt",
               "ja tā ir liela", "ja tai ir 3 malas", "ja tā ir krāsaina"], 0),
             ("Cik simetrijas asu ir kvadrātam?", ["1", "2", "3", "4"], 3),
             ("Kurai figūrai nav simetrijas ass?",
              ["kvadrāts", "riņķis", "figūra bez noteiktas formas",
               "taisnstūris"], 2),
         ]},
        {"sr": "Zina, ka viena veida daudzstūriem var būt dažādas īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai visi četrstūri ir vienādi?",
              ["nē, tiem var būt dažāda forma", "jā, visi ir kvadrāti",
               "jā, visi ir vienāda lieluma", "nē, tiem ir dažāds malu "
               "skaits"], 0),
             ("Kurš apgalvojums ir pareizs?",
              ["katrs kvadrāts ir četrstūris", "katrs četrstūris ir kvadrāts",
               "kvadrātam ir 3 malas", "četrstūrim ir 5 virsotnes"], 0),
             ("Ar ko taisnstūris atšķiras no patvaļīga četrstūra?",
              ["tam visi stūri ir taisni", "tam ir 3 malas",
               "tam nav virsotņu", "tas vienmēr ir sarkans"], 0),
         ]},
        {"sr": "Sadala figūru vienādās daļās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik vienādās daļās var sadalīt kvadrātu ar vienu taisnu "
              "līniju?",
              ["divās", "trijās", "četrās", "nevar sadalīt"], 0),
             ("Ar cik taisnām līnijām kvadrātu sadala četrās vienādās daļās?",
              ["ar vienu", "ar divām", "ar trim", "ar piecām"], 1),
             ("Ko nozīmē «vienādās daļās»?",
              ["daļas ir vienādas", "daļas ir dažādas",
               "daļas ir krāsainas", "daļu ir daudz"], 0),
         ]},
        {"sr": "Grupē figūras pēc pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pēc kā var sagrupēt figūras?",
              ["pēc malu skaita", "pēc svara", "pēc garšas", "pēc skaņas"], 0),
             ("Kura figūra ir lieka:  trijstūris, četrstūris, kvadrāts, "
              "riņķis?",
              ["trijstūris", "četrstūris", "kvadrāts", "riņķis"], 3),
             ("Grupā ir kvadrāts un taisnstūris. Kāda ir kopīgā pazīme?",
              ["4 malas", "3 malas", "nav virsotņu", "vienāda krāsa"], 0),
         ]},
        {"sr": "Atpazīst telpiskas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik skaldņu ir kubam?", ["4", "6", "8", "12"], 1),
             ("Kāda figūra ir kuba skaldne?",
              ["trijstūris", "kvadrāts", "riņķis", "piecstūris"], 1),
             ("Kura no figūrām ir telpiska?",
              ["kubs", "kvadrāts", "trijstūris", "riņķis"], 0),
         ]},
        {"sr": "Skaidro, ka telpiska figūra no dažādām pusēm izskatās "
               "atšķirīgi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā izskatās kubs, ja skatās tieši no priekšpuses?",
              ["kā kvadrāts", "kā trijstūris", "kā riņķis",
               "kā lauzta līnija"], 0),
             ("Kāpēc telpisku figūru zīmē no dažādām pusēm?",
              ["no katras puses redzams kas cits", "lai zīmējums būtu lielāks",
               "lai izmantotu vairāk krāsu", "citādi nedrīkst"], 0),
             ("Cik kubiņu vajag, lai izveidotu rindu no 4 kubiem?",
              ["2", "3", "4", "8"], 2),
         ]},
        {"sr": "Pieraksta algoritmu figūras zīmēšanai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir algoritms?",
              ["precīza soļu virkne", "figūras krāsa", "viena taisna līnija",
               "skaitļu virkne"], 0),
             ("Kurš solis kvadrāta zīmēšanā ir pirmais?",
              ["novilkt pirmo malu", "nokrāsot figūru", "uzrakstīt nosaukumu",
               "izdzēst līnijas"], 0),
             ("Kāpēc algoritmu jāpieraksta precīzi?",
              ["lai arī cits varētu to izpildīt", "lai būtu garāks",
               "lai neviens nesaprastu", "lai nevajadzētu lineālu"], 0),
         ]},
        {"sr": "Izpilda soļu virkni un pārbauda rezultātu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Soļi: novelc 4 vienāda garuma malas, katru stūri taisnu. Kāda "
              "figūra sanāk?",
              ["kvadrāts", "trijstūris", "riņķis", "lauzta līnija"], 0),
             ("Soļi: novelc 3 malas tā, lai figūra būtu noslēgta. Kāda figūra "
              "sanāk?",
              ["trijstūris", "četrstūris", "riņķis", "punkts"], 0),
             ("Kā pārbauda, vai algoritms uzrakstīts pareizi?",
              ["izpilda soļus", "izlasa to skaļi",
               "nokrāso to", "salīdzina krāsas"], 0),
         ]},
        {"sr": "Zīmē figūras rūtiņu lapā ar lineālu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko rūtiņu lapā zīmē taisnas malas?",
              ["ar lineālu", "ar brīvu roku", "ar dzēšgumiju",
               "ar šķērēm"], 0),
             ("Kvadrāta mala ir 3 rūtiņas. Cik rūtiņas ir katrai malai?",
              ["3", "4", "6", "12"], 0),
             ("Cik malu kopā jānovelk, zīmējot taisnstūri?",
              ["2", "3", "4", "5"], 2),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 1,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 1.8. temata noslēgumā. "
                "Pārbauda figūru īpašības un atpazīšanu pēc apraksta, "
                "simetriju, figūras dalīšanu vienādās daļās, telpiskas "
                "figūras, grupēšanu un algoritma pierakstu figūras "
                "zīmēšanai.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
              "Uzdevumu tekstu lasa skolotājs. Zīmē ar lineālu tam "
              "atvēlētajā vietā!",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Atpazīst figūru pēc malu un virsotņu skaita",
         "stunda": TEMATS,
         "jautajumi": [
             ("Figūrai ir 3 malas. Kura tā ir?",
              ["trijstūris", "četrstūris", "piecstūris", "riņķis"], 0),
             ("Cik virsotņu ir četrstūrim?", ["2", "3", "4", "5"], 2),
             ("Kurai figūrai nav virsotņu?",
              ["trijstūrim", "kvadrātam", "riņķim", "piecstūrim"], 2),
         ]},
        {"sr": "Atšķir būtiskas un mazāk svarīgas īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura īpašība kvadrātam ir būtiska?",
              ["4 vienāda garuma malas", "zila krāsa", "liels izmērs",
               "vieta lapā"], 0),
             ("Vai figūra mainās, ja to uzzīmē lielāku?",
              ["nē, tā paliek tā pati figūra", "jā, tā kļūst par citu figūru",
               "jā, tai rodas vairāk malu", "jā, tā vairs nav figūra"], 0),
             ("Kurš apgalvojums ir pareizs?",
              ["katrs kvadrāts ir četrstūris", "katrs četrstūris ir kvadrāts",
               "kvadrātam ir 5 malas", "trijstūrim ir 4 virsotnes"], 0),
         ]},
        {"sr": "Nosaka simetriskas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad figūra ir simetriska?",
              ["ja to var pārlocīt tā, ka puses sakrīt", "ja tā ir maza",
               "ja tā ir krāsaina", "ja tai ir 3 malas"], 0),
             ("Cik simetrijas asu ir kvadrātam?", ["1", "2", "3", "4"], 3),
             ("Kā sauc līniju, pa kuru figūru pārloka?",
              ["simetrijas ass", "mala", "virsotne", "diagonāle"], 0),
         ]},
        {"sr": "Sadala figūru vienādās daļās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik daļās sadala figūru viena taisna līnija?",
              ["divās", "trijās", "četrās", "piecās"], 0),
             ("Ko nozīmē «vienādas daļas»?",
              ["daļas ir vienāda lieluma", "daļas ir dažādas",
               "daļas ir krāsainas", "daļu ir daudz"], 0),
             ("Ar cik līnijām kvadrātu sadala 4 vienādās daļās?",
              ["ar vienu", "ar divām", "ar trim", "ar četrām"], 1),
         ]},
        {"sr": "Atpazīst telpiskas figūras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik skaldņu ir kubam?", ["4", "6", "8", "12"], 1),
             ("Kāda figūra ir kuba skaldne?",
              ["kvadrāts", "trijstūris", "riņķis", "piecstūris"], 0),
             ("Kura figūra ir telpiska?",
              ["kubs", "kvadrāts", "riņķis", "trijstūris"], 0),
         ]},
        {"sr": "Zina, kas ir algoritms",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir algoritms?",
              ["precīza soļu virkne", "figūras nosaukums", "skaitļu virkne",
               "viena mala"], 0),
             ("Kāpēc soļus jāpieraksta precīzi?",
              ["lai arī cits varētu izpildīt", "lai būtu garāks",
               "lai nevienam nebūtu skaidrs", "lai izmantotu krāsas"], 0),
             ("Kā pārbauda algoritmu?",
              ["izpilda soļus un skatās rezultātu", "izlasa to skaļi",
               "nokrāso to", "izdzēš to"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka figūras malu un virsotņu skaitu",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Trijstūrim ir …… malas", "3"),
                         ("Četrstūrim ir …… virsotnes", "4"),
                         ("Piecstūrim ir …… malas", "5"),
                         ("Kubam ir …… skaldnes", "6")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Kvadrātam ir …… malas", "4"),
                         ("Trijstūrim ir …… virsotnes", "3"),
                         ("Riņķim ir …… malas", "0"),
                         ("Kvadrātam ir …… simetrijas asis", "4")]},
             {"tips": "parveide", "virs": "Ieraksti skaitli",
              "note": "Ieraksti pareizo skaitli! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Piecstūrim ir …… virsotnes", "5"),
                         ("Taisnstūrim ir …… malas", "4"),
                         ("Sešstūrim ir …… malas", "6"),
                         ("Kubam ir …… kvadrātveida skaldnes", "6")]},
         ]},
        {"sr": "Atpazīst figūru pēc apraksta",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Uzraksti figūras nosaukumu",
              "note": "Ieraksti figūras nosaukumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Figūrai ir 3 malas un 3 virsotnes:  ……",
                          "trijstūris"),
                         ("Četrstūris, kuram visas malas vienāda garuma:  ……",
                          "kvadrāts"),
                         ("Figūra bez malām un virsotnēm:  ……", "riņķis")]},
             {"tips": "parveide", "virs": "Uzraksti figūras nosaukumu",
              "note": "Ieraksti figūras nosaukumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Figūrai ir 5 malas:  ……", "piecstūris"),
                         ("Četrstūris ar taisniem stūriem:  ……",
                          "taisnstūris"),
                         ("Telpiska figūra ar 6 kvadrātveida skaldnēm:  ……",
                          "kubs")]},
             {"tips": "parveide", "virs": "Uzraksti figūras nosaukumu",
              "note": "Ieraksti figūras nosaukumu! Par katru pareizu "
                      "atbildi — 1 punkts.",
              "rindas": [("Figūrai ir 4 malas un 4 virsotnes:  ……",
                          "četrstūris"),
                         ("Figūrai ir 3 virsotnes:  ……", "trijstūris"),
                         ("Figūra, ko veido nogriežņi vienā rindā:  ……",
                          "lauzta līnija")]},
         ]},
        {"sr": "Zīmē figūras pēc nosacījumiem un sadala tās daļās",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Zīmē un sadali", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē kvadrātu, kura mala ir 4 rūtiņas!", 1),
                       ("Sadali to divās vienādās daļās!", 1),
                       ("Uzzīmē trijstūri!", 1),
                       ("Novelc kvadrātam vienu simetrijas asi!", 1)],
              "atbildes": ["1) Uzzīmēts kvadrāts ar 4 rūtiņu malu.   (1 p.)",
                           "2) Novilkta līnija, kas dala kvadrātu divās "
                           "vienādās daļās.   (1 p.)",
                           "3) Uzzīmēts trijstūris.   (1 p.)",
                           "4) Novilkta simetrijas ass.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un sadali", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē taisnstūri, kura malas ir 3 un 5 rūtiņas!",
                        1),
                       ("Sadali to divās vienādās daļās!", 1),
                       ("Uzzīmē kvadrātu!", 1),
                       ("Novelc taisnstūrim vienu simetrijas asi!", 1)],
              "atbildes": ["1) Uzzīmēts taisnstūris ar 3 un 5 rūtiņu "
                           "malām.   (1 p.)",
                           "2) Novilkta līnija, kas dala to divās vienādās "
                           "daļās.   (1 p.)",
                           "3) Uzzīmēts kvadrāts.   (1 p.)",
                           "4) Novilkta simetrijas ass.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Zīmē un sadali", "vieta": 7.0,
              "ievads": "Zīmē rūtiņās ar lineālu!",
              "jaut": [("Uzzīmē kvadrātu, kura mala ir 6 rūtiņas!", 1),
                       ("Sadali to četrās vienādās daļās!", 1),
                       ("Uzzīmē četrstūri, kas nav kvadrāts!", 1),
                       ("Uzraksti, cik simetrijas asu ir kvadrātam!", 1)],
              "atbildes": ["1) Uzzīmēts kvadrāts ar 6 rūtiņu malu.   (1 p.)",
                           "2) Novilktas divas līnijas, kas dala kvadrātu "
                           "četrās vienādās daļās.   (1 p.)",
                           "3) Uzzīmēts četrstūris, kura malas nav vienādas.  "
                           " (1 p.)",
                           "4) Pierakstīts 4.   (1 p.)"]},
         ]},
        {"sr": "Pieraksta algoritmu figūras zīmēšanai",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Algoritms", "vieta": 5.5,
              "ievads": "Uzraksti soļus, kā rūtiņu lapā uzzīmēt kvadrātu, "
                        "kura mala ir 3 rūtiņas.",
              "jaut": [("Pieraksti 1. soli!", 1), ("Pieraksti 2. soli!", 1),
                       ("Pieraksti pēdējo soli!", 1)],
              "atbildes": ["1) Piemēram: novelc 3 rūtiņas garu malu.   "
                           "(1 p.)",
                           "2) Piemēram: no mala gala novelc 3 rūtiņas uz "
                           "leju.   (1 p.)",
                           "3) Piemēram: novelc pārējās divas malas, lai "
                           "figūra ir noslēgta.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Algoritms", "vieta": 5.5,
              "ievads": "Uzraksti soļus, kā rūtiņu lapā uzzīmēt taisnstūri, "
                        "kura malas ir 2 un 5 rūtiņas.",
              "jaut": [("Pieraksti 1. soli!", 1), ("Pieraksti 2. soli!", 1),
                       ("Pieraksti pēdējo soli!", 1)],
              "atbildes": ["1) Piemēram: novelc 5 rūtiņas garu malu.   "
                           "(1 p.)",
                           "2) Piemēram: no mala gala novelc 2 rūtiņas uz "
                           "leju.   (1 p.)",
                           "3) Piemēram: novelc pārējās malas, lai figūra ir "
                           "noslēgta.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Algoritms", "vieta": 5.5,
              "ievads": "Draugs izpildīja tavu algoritmu un ieguva "
                        "trijstūri, nevis kvadrātu.",
              "jaut": [("Uzraksti, kur algoritmā varēja būt kļūda!", 1),
                       ("Pieraksti pareizo soli!", 1),
                       ("Uzraksti, kā pārbaudīt labotu algoritmu!", 1)],
              "atbildes": ["1) Piemēram: bija norādītas tikai 3 malas.   "
                           "(1 p.)",
                           "2) Piemēram: novelc 4 vienāda garuma malas.   "
                           "(1 p.)",
                           "3) Atbilde: vēlreiz izpildīt soļus un salīdzināt "
                           "rezultātu.   (1 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
