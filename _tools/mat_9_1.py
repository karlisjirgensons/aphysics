# -*- coding: utf-8 -*-
"""Matemātika, 9. klase. 9.1. Kā definē un raksturo līdzīgus trijstūrus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 9. klase, 9.1. temats): Talesa teorēma,
trijstūra viduslīnija, proporcionāli nogriežņi, līdzīgi trijstūri, līdzības
koeficients, līdzības pazīmes, līdzīgu trijstūru perimetru un laukumu
attiecība, līdzības lietojums (ēna, mērogs, nepieejams attālums).
"""

PRIEKSMETS = "Matemātika  |  9. klase"
TEMATS = "9.1."
NOSAUKUMS = "Kā definē un raksturo līdzīgus trijstūrus?"

ATGADNE = [
    "Trijstūra viduslīnija savieno divu malu viduspunktus; tā ir paralēla "
    "trešajai malai un divreiz īsāka:   m = {a|2}",
    "Līdzīgiem trijstūriem atbilstošie leņķi ir vienādi, bet atbilstošās "
    "malas — proporcionālas;   k = {a₁|a}   ir līdzības koeficients.",
    "Perimetru attiecība   P₁ : P = k      ·      laukumu attiecība   "
    "S₁ : S = k²",
]

FD = {
    "veids": "fd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 9.1. temata beigās. Pārbauda "
                "proporcionālus nogriežņus, Talesa teorēmu, trijstūra "
                "viduslīniju, līdzīgu trijstūru definīciju un pazīmes, "
                "līdzības koeficientu un perimetru, laukumu attiecību.",
    "ievads": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
              "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kas ir proporcionāli nogriežņi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad divi nogriežņu pāri ir proporcionāli?",
              ["ja garumu attiecības ir vienādas", "ja garumi ir vienādi",
               "ja tie ir paralēli", "ja tie ir perpendikulāri"], 0),
             ("Cik nogriežņu vismaz vajag, lai spriestu par "
              "proporcionalitāti?", ["2", "3", "4", "5"], 2),
             ("Vai proporcija 3 : 6 = 5 : 10 ir patiesa?",
              ["jā, abas attiecības ir 0,5", "nē", "tikai centimetros",
               "to nevar noteikt"], 0),
         ]},
        {"sr": "Lieto Talesa teorēmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Leņķa malas krusto paralēlas taisnes. Kādi nogriežņi "
              "rodas?",
              ["proporcionāli", "vienādi", "perpendikulāri",
               "nesaistīti"], 0),
             ("Kā nogriezni sadala 3 vienādās daļās?",
              ["lieto Talesa teorēmu", "mēra ar skalu", "zīmē riņķi",
               "tas nav iespējams"], 0),
             ("Ko izmanto, lai nogriezni sadalītu attiecībā 2 : 3?",
              ["Talesa teorēmu", "Pitagora teorēmu", "trijstūra laukumu",
               "leņķu summu"], 0),
         ]},
        {"sr": "Zina trijstūra viduslīnijas definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir trijstūra viduslīnija?",
              ["divu malu viduspunktu savienojums", "mediāna", "augstums",
               "bisektrise"], 0),
             ("Cik viduslīniju ir trijstūrim?", ["1", "2", "3", "4"], 2),
             ("Kā viduslīnija novietota pret trešo malu?",
              ["paralēli", "perpendikulāri", "šķērsām", "sakrīt ar to"], 0),
         ]},
        {"sr": "Lieto viduslīnijas īpašību aprēķinos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Trijstūra mala ir 18 cm. Cik gara ir tai atbilstošā "
              "viduslīnija?", ["9 cm", "6 cm", "18 cm", "36 cm"], 0),
             ("Viduslīnija ir 7 cm. Cik gara ir tai paralēlā mala?",
              ["14 cm", "3,5 cm", "7 cm", "21 cm"], 0),
             ("Ar kuru formulu aprēķina viduslīniju m, ja mala ir a?",
              ["m = {a|2}", "m = 2a", "m = a", "m = {2|a}"], 0),
         ]},
        {"sr": "Zina līdzīgu trijstūru definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādi trijstūri ir līdzīgi?",
              ["leņķi vienādi, malas proporcionālas", "visas malas vienādas",
               "ir taisns leņķis", "ir kopīga mala"], 0),
             ("Ar kuru zīmi pieraksta trijstūru līdzību?",
              ["∼", "=", "⊥", "∥"], 0),
             ("Vai visi kvadrāti savā starpā ir līdzīgi?",
              ["jā", "nē", "tikai vienāda izmēra kvadrāti",
               "to nevar noteikt"], 0),
         ]},
        {"sr": "Nosaka līdzības koeficientu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir līdzības koeficients?",
              ["atbilstošo malu dalījums", "malu summa", "leņķu dalījums",
               "laukumu starpība"], 0),
             ("Atbilstošās malas ir 6 cm un 3 cm. Cik liels ir "
              "k = 6 : 3?", ["2", "0,5", "3", "18"], 0),
             ("Ko nozīmē līdzības koeficients k = 1?",
              ["trijstūri ir vienādi", "tie nav līdzīgi",
               "viens ir divreiz lielāks", "leņķi nav vienādi"], 0),
         ]},
        {"sr": "Zina trijstūru līdzības pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko pietiek trijstūru līdzības pamatošanai?",
              ["ar divu leņķu vienādību", "ar divu malu vienādību",
               "ar kopīgu malu", "ar vienādiem perimetriem"], 0),
             ("Diviem taisnleņķa trijstūriem šaurais leņķis ir 40°. Vai "
              "tie ir līdzīgi?",
              ["jā", "nē", "tikai ar vienādām malām", "nevar noteikt"], 0),
             ("Kura pazīme der, ja divas malas proporcionālas un leņķi "
              "starp tām vienādi?",
              ["mala–leņķis–mala", "leņķis–leņķis", "mala–mala–mala",
               "tādas nav"], 0),
         ]},
        {"sr": "Saskata atbilstošos elementus",
         "stunda": TEMATS,
         "jautajumi": [
             ("△ABC ∼ △MNK. Kurš leņķis ir vienāds ar leņķi A?",
              ["leņķis M", "leņķis N", "leņķis K", "neviens"], 0),
             ("△ABC ∼ △MNK. Kura mala atbilst malai AB?",
              ["MN", "NK", "MK", "AC"], 0),
             ("Ko var teikt par līdzīgu trijstūru leņķiem?",
              ["atbilstošie ir vienādi", "visi ir 60°", "tie ir "
               "proporcionāli", "tie nav saistīti"], 0),
         ]},
        {"sr": "Aprēķina nezināmo malas garumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("△ABC ∼ △A₁B₁C₁, k = 3 un AB = 4 cm. Cik gara ir A₁B₁?",
              ["12 cm", "1,3 cm", "7 cm", "3 cm"], 0),
             ("Malām 5 cm un 15 cm atbilst mala 4 cm. Cik gara ir tai "
              "atbilstošā mala?", ["12 cm", "8 cm", "20 cm", "6 cm"], 0),
             ("Kā pārbauda, vai malas garums ir ticams?",
              ["lielākā trijstūra malai jābūt garākai", "jābūt veselam "
               "skaitlim", "jābūt mazākai nekā 1", "nav jāpārbauda"], 0),
         ]},
        {"sr": "Lieto perimetru attiecību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Līdzības koeficients ir k = 2. Kāda ir perimetru attiecība?",
              ["2", "4", "1", "0,5"], 0),
             ("Mazākā perimetrs ir 12 cm un k = 3. Cik liels ir lielākā "
              "perimetrs?", ["36 cm", "4 cm", "15 cm", "108 cm"], 0),
             ("No kā atkarīga līdzīgu trijstūru augstumu attiecība?",
              ["no līdzības koeficienta", "no laukuma",
               "no leņķu summas", "ne no kā"], 0),
         ]},
        {"sr": "Lieto laukumu attiecību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Līdzības koeficients ir k = 3. Kāda ir laukumu attiecība?",
              ["9", "3", "6", "1,5"], 0),
             ("Mazākā laukums ir 5 cm² un k = 2. Cik liels ir lielākā "
              "laukums?", ["20 cm²", "10 cm²", "7 cm²", "2,5 cm²"], 0),
             ("Laukumu attiecība ir 16. Cik liels ir līdzības koeficients?",
              ["4", "16", "8", "2"], 0),
         ]},
        {"sr": "Lieto līdzību praktiskās situācijās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā ar ēnu nosaka koka augstumu?",
              ["salīdzina koka un mieta ēnas", "mēra ar lineālu",
               "izmanto leņķu summu", "nosver koku"], 0),
             ("Kartes mērogs ir 1 : 25 000. Ko tas nozīmē?",
              ["1 cm kartē ir 250 m dabā", "1 cm kartē ir 25 m",
               "1 m kartē ir 25 km", "karte ir 25 000 cm gara"], 0),
             ("Miets 2 m met 3 m ēnu, koks met 12 m ēnu. Cik augsts ir "
              "koks?", ["8 m", "18 m", "6 m", "24 m"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 9,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 25 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 9.1. temata noslēgumā. "
                "Pārbauda trijstūra viduslīnijas īpašību, līdzīgu trijstūru "
                "definīciju un pazīmes, līdzības koeficientu, perimetru un "
                "laukumu attiecību un līdzības lietojumu aprēķinos.",
    "ievads": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 25 "
              "punktus. Risinājumu pieraksti tam atvēlētajā vietā; "
              "atļauts kalkulators.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina viduslīnijas īpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Trijstūra mala ir 22 cm. Cik gara ir tai atbilstošā "
              "viduslīnija?", ["11 cm", "44 cm", "22 cm", "7 cm"], 0),
             ("Viduslīnija ir 8 cm. Cik gara ir tai paralēlā mala?",
              ["16 cm", "4 cm", "8 cm", "24 cm"], 0),
             ("Kā viduslīnija novietota pret trešo malu?",
              ["paralēli tai", "perpendikulāri tai", "šķērsām",
               "sakrīt ar to"], 0),
         ]},
        {"sr": "Zina proporcionālus nogriežņus un Talesa teorēmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Leņķa malas krusto paralēlas taisnes. Kādi ir iegūtie "
              "nogriežņi?",
              ["proporcionāli", "vienāda garuma", "perpendikulāri",
               "nesaistīti"], 0),
             ("Kad nogriežņu pāri ir proporcionāli?",
              ["ja to garumu attiecības ir vienādas",
               "ja to garumu summas ir vienādas",
               "ja tie ir vienāda garuma", "ja tie ir paralēli"], 0),
             ("Ko lieto, lai nogriezni sadalītu 5 vienādās daļās?",
              ["Talesa teorēmu", "Pitagora teorēmu", "laukuma formulu",
               "leņķu summu"], 0),
         ]},
        {"sr": "Zina līdzīgu trijstūru definīciju un koeficientu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādi trijstūri ir līdzīgi?",
              ["kuru leņķi ir vienādi un malas proporcionālas",
               "kuru malas ir vienāda garuma", "kuriem ir taisns leņķis",
               "kuriem ir vienāds perimetrs"], 0),
             ("Atbilstošās malas ir 10 cm un 4 cm. Cik liels ir "
              "k = 10 : 4?", ["2,5", "0,4", "6", "40"], 0),
             ("Ko nozīmē k = 1?",
              ["trijstūri ir vienādi", "trijstūri nav līdzīgi",
               "viens ir divreiz lielāks", "malas nav proporcionālas"], 0),
         ]},
        {"sr": "Lieto līdzības pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko pietiek trijstūru līdzības pamatošanai?",
              ["ar divu leņķu vienādību", "ar vienas malas vienādību",
               "ar vienādiem perimetriem", "ar kopīgu virsotni"], 0),
             ("Trijstūrī novilkts nogrieznis paralēli malai. Kas veidojas?",
              ["dotajam līdzīgs trijstūris", "vienādsānu trijstūris",
               "taisnleņķa trijstūris", "vienādmalu trijstūris"], 0),
             ("Trijstūriem leņķi ir 40° un 60°; otram — 60° un 80°. Vai tie "
              "ir līdzīgi?",
              ["jā, sakrīt visi trīs leņķi", "nē", "tikai tad, ja malas "
               "vienādas", "to nevar noteikt"], 0),
         ]},
        {"sr": "Lieto perimetru un laukumu attiecību",
         "stunda": TEMATS,
         "jautajumi": [
             ("k = 4. Kāda ir perimetru attiecība?", ["4", "16", "8", "2"],
              0),
             ("k = 5. Kāda ir laukumu attiecība?", ["25", "5", "10", "2,5"],
              0),
             ("Laukumu attiecība ir 36. Cik liels ir k?",
              ["6", "36", "18", "12"], 0),
         ]},
        {"sr": "Lieto līdzību praktiskā situācijā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Miets 1 m met 2 m garu ēnu; koks met 10 m garu ēnu. Cik "
              "augsts ir koks?", ["5 m", "20 m", "10 m", "2 m"], 0),
             ("Mērogs 1 : 1000. Cik garš dabā ir nogrieznis 3 cm kartē?",
              ["30 m", "3 m", "300 m", "3 km"], 0),
             ("Kāpēc koka augstumu var noteikt pēc ēnas?",
              ["saules stari veido līdzīgus trijstūrus",
               "ēna vienmēr ir vienāda ar augstumu",
               "ēnas garums nav svarīgs", "koks ir taisnleņķa trijstūris"],
              0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina lielumus pēc viduslīnijas un līdzības koeficienta",
         "stunda": TEMATS, "punkti": 5, "lapa": 1,
         "varianti": [
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Trijstūra mala ir 24 cm; viduslīnija ir …… cm",
                          "12"),
                         ("Viduslīnija ir 9 cm; tai paralēlā mala ir …… cm",
                          "18"),
                         ("△ABC ∼ △MNK, k = 2, AB = 7 cm; MN = …… cm",
                          "14"),
                         ("k = 4; perimetru attiecība ir ……", "4"),
                         ("k = 4; laukumu attiecība ir ……", "16")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Trijstūra mala ir 30 cm; viduslīnija ir …… cm",
                          "15"),
                         ("Viduslīnija ir 6,5 cm; tai paralēlā mala ir …… "
                          "cm", "13"),
                         ("△ABC ∼ △MNK, k = 3, AB = 5 cm; MN = …… cm",
                          "15"),
                         ("k = 5; perimetru attiecība ir ……", "5"),
                         ("k = 5; laukumu attiecība ir ……", "25")]},
             {"tips": "parveide", "virs": "Ieraksti trūkstošo vērtību",
              "note": "Ieraksti atbildi! Par katru pareizu atbildi — "
                      "1 punkts.",
              "rindas": [("Trijstūra mala ir 17 cm; viduslīnija ir …… cm",
                          "8,5"),
                         ("Viduslīnija ir 11 cm; tai paralēlā mala ir …… "
                          "cm", "22"),
                         ("△ABC ∼ △MNK, k = 0,5, AB = 8 cm; MN = …… cm",
                          "4"),
                         ("Laukumu attiecība ir 9; k = ……", "3"),
                         ("k = 6; laukumu attiecība ir ……", "36")]},
         ]},
        {"sr": "Aprēķina nezināmos lielumus, izmantojot trijstūru līdzību",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Līdzīgu trijstūru lielumi",
              "vieta": 5.8,
              "teksts": "Trijstūrī ABC novilkta viduslīnija MN, kas ir "
                        "paralēla malai AC. Trijstūra ABC perimetrs ir "
                        "48 cm. Aprēķini trijstūra MBN perimetru! Pamato, "
                        "kāpēc trijstūri ir līdzīgi.",
              "kriteriji": [
                  "Pamatots △MBN ∼ △ABC (viduslīnija ∥ AC, vienādi leņķi). "
                  "(1 p.)",
                  "Noteikts līdzības koeficients k = 0,5.   (1 p.)",
                  "Lietota perimetru attiecība P₁ : P = k.   (1 p.)",
                  "Aprēķins P(MBN) = 48 · 0,5.   (1 p.)",
                  "Atbilde: 24 cm.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Līdzīgu trijstūru lielumi",
              "vieta": 5.8,
              "teksts": "Trijstūrī ABC novilkts nogrieznis MN ∥ AC, kur "
                        "M ∈ AB un N ∈ BC. Dots: BM = 4 cm, MA = 8 cm, "
                        "MN = 5 cm. Aprēķini malas AC garumu!",
              "kriteriji": [
                  "Pamatots △BMN ∼ △BAC (MN ∥ AC, vienādi leņķi).   (1 p.)",
                  "Noteikts BA = 4 + 8 = 12 cm.   (1 p.)",
                  "Noteikts k = 12 : 4 = 3.   (1 p.)",
                  "Aprēķins AC = 3 · 5.   (1 p.)",
                  "Atbilde: AC = 15 cm.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Līdzīgu trijstūru lielumi",
              "vieta": 5.8,
              "teksts": "Divi trijstūri ir līdzīgi. Mazākā trijstūra malas "
                        "ir 6 cm, 8 cm un 10 cm, bet lielākā trijstūra "
                        "garākā mala ir 25 cm. Aprēķini lielākā trijstūra "
                        "perimetru un abu trijstūru laukumu attiecību!",
              "kriteriji": [
                  "Noteikts k = 25 : 10 = 2,5.   (1 p.)",
                  "Aprēķināts mazākā perimetrs 6 + 8 + 10 = 24 cm.   (1 p.)",
                  "Lietota perimetru attiecība P₁ = 24 · 2,5.   (1 p.)",
                  "Atbilde: P₁ = 60 cm.   (1 p.)",
                  "Laukumu attiecība k² = 6,25.   (1 p.)"]},
         ]},
        {"sr": "Risina praktiska satura uzdevumu par līdzību",
         "stunda": TEMATS, "punkti": 5, "lapa": 2,
         "varianti": [
             {"tips": "aprekins", "virs": "Līdzība praksē", "vieta": 5.0,
              "teksts": "Koks met 9 m garu ēnu. Tajā pašā laikā 1,5 m "
                        "augsts miets met 1,8 m garu ēnu. Cik augsts ir "
                        "koks?",
              "kriteriji": [
                  "Saskatīti divi līdzīgi taisnleņķa trijstūri.   (1 p.)",
                  "Pieraksta proporcija {h|9} = {1,5|1,8}.   (1 p.)",
                  "Izteikts h = {1,5 · 9|1,8}.   (1 p.)",
                  "Aprēķins h = 7,5.   (1 p.)",
                  "Atbilde: koks ir 7,5 m augsts.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Līdzība praksē", "vieta": 5.0,
              "teksts": "Cilvēks, kura augums ir 1,7 m, met 2,55 m garu "
                        "ēnu. Blakus esošs stabs tajā pašā laikā met 6 m "
                        "garu ēnu. Cik augsts ir stabs?",
              "kriteriji": [
                  "Saskatīti divi līdzīgi taisnleņķa trijstūri.   (1 p.)",
                  "Pieraksta proporcija {h|6} = {1,7|2,55}.   (1 p.)",
                  "Izteikts h = {1,7 · 6|2,55}.   (1 p.)",
                  "Aprēķins h = 4.   (1 p.)",
                  "Atbilde: stabs ir 4 m augsts.   (1 p.)"]},
             {"tips": "aprekins", "virs": "Līdzība praksē", "vieta": 5.0,
              "teksts": "Kartes mērogs ir 1 : 50 000. Divu ciemu attālums "
                        "kartē ir 7,4 cm. Cik liels šis attālums ir dabā? "
                        "Atbildi izsaki kilometros.",
              "kriteriji": [
                  "Saprasts, ka mērogs ir līdzības koeficients.   (1 p.)",
                  "Pieraksts 7,4 · 50 000.   (1 p.)",
                  "Aprēķins 370 000 cm.   (1 p.)",
                  "Pārvērsts 370 000 cm = 3,7 km.   (1 p.)",
                  "Atbilde: 3,7 km.   (1 p.)"]},
         ]},
        {"sr": "Spriež un pamato secinājumu par līdzīgiem trijstūriem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": [
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Trijstūrī ABC ∠A = 50° un ∠B = 70°. Trijstūrī MNK "
                        "∠M = 50° un ∠K = 60°.",
              "jaut": [("Aprēķini ∠C!", 1), ("Aprēķini ∠N!", 1),
                       ("Vai trijstūri ir līdzīgi? Pamato atbildi!", 2)],
              "atbildes": ["1) ∠C = 180° − 50° − 70° = 60°.   (1 p.)",
                           "2) ∠N = 180° − 50° − 60° = 70°.   (1 p.)",
                           "3) Abiem trijstūriem leņķi ir 50°, 60° un 70°, "
                           "tāpēc tie ir līdzīgi pēc divu leņķu vienādības. "
                           "  (2 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "△ABC ∼ △A₁B₁C₁ ar līdzības koeficientu k = 3. "
                        "Trijstūra ABC malas ir 4 cm, 6 cm un 7 cm.",
              "jaut": [("Uzraksti trijstūra A₁B₁C₁ malu garumus!", 2),
                       ("Aprēķini abu trijstūru perimetrus!", 1),
                       ("Cik reižu lielāks ir trijstūra A₁B₁C₁ laukums?",
                        1)],
              "atbildes": ["1) 12 cm, 18 cm un 21 cm.   (2 p.)",
                           "2) P = 17 cm un P₁ = 51 cm.   (1 p.)",
                           "3) k² = 9 reizes.   (1 p.)"]},
             {"tips": "jautajumi", "virs": "Spriedums un pamatojums",
              "vieta": 4.4,
              "ievads": "Taisnleņķa trijstūrī ABC (∠C = 90°) pret "
                        "hipotenūzu AB novilkts augstums CD.",
              "jaut": [("Nosauc trijstūri, kas ir līdzīgs trijstūrim ACD!",
                        1),
                       ("Ar kuru pazīmi līdzību pamato?", 1),
                       ("AD = 4 cm un DB = 9 cm. Aprēķini CD!", 2)],
              "atbildes": ["1) △ACD ∼ △ABC (arī △ACD ∼ △CBD).   (1 p.)",
                           "2) Pēc divu leņķu vienādības — taisnais leņķis "
                           "un kopīgais šaurais leņķis.   (1 p.)",
                           "3) CD = √(4 · 9) = 6 cm.   (2 p.)"]},
         ]},
    ],
}

DARBI = {"fd": FD, "pd": PD}
