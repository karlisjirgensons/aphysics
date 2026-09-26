# -*- coding: utf-8 -*-
"""9. klase, 168. stunda: «Kā plānot atkārtošanu?»

No 167. stundas saraksta sastāda plānu: pieejamais laiks, laika dalījums
proporcionāli vājumam, atkārtošana ar starplaikiem (vienu tematu
atkārto vairākas reizes, nevis vienā vakarā) un pēdējā nedēļā - pilns darbs
laika kontrolē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā plānot atkārtošanu?"

MERKIS = "Sastādīsim personīgu gatavošanās plānu līdz eksāmenam."

_NEDELA = restis([["P", "O", "T", "C", "Pk"],
                  ["Funk.", "—", "Ģeom.", "—", "Funk."],
                  ["40'", "", "40'", "", "20'"]])

SATURS = [
    Sakums("Viens garš vakars vai daudzi īsi?",
           zimejums=_NEDELA,
           paraksts="Piemērs: funkcijas atkārto divreiz nedēļā ar starplaiku.",
           fakti=["Īsi, regulāri atkārtojumi paliek atmiņā ilgāk.",
                  "Vairāk laika vājākajiem tematiem.",
                  "Pēdējā nedēļā - pilns darbs laika kontrolē."]),

    Doma("Plāna soļi",
         "Labs plāns atbild uz trim jautājumiem: cik laika man ir, ko "
         "atkārtot un kad.",
         soli=[
             "Saskaiti pieejamās nedēļas un minūtes.",
             "Sadali laiku: vājākajām jomām vairāk.",
             "Katru tematu ieplāno vismaz divreiz ar starplaiku.",
             "Atstāj laiku 2-3 pilniem darbiem un kļūdu analīzei.",
         ]),

    Ievadi("Cik laika man ir?", [
        {"jaut": "6 nedēļas, 4 dienas nedēļā pa 40 min. Cik stundu kopā?",
         "atb": ["16"], "padoms": "6 · 4 · 40 = 960 min."},
        {"jaut": "No 16 h trīs pilni darbi pa 3 h. Cik stundu paliek "
                 "tematiem?", "atb": ["7"], "padoms": "16 − 9."},
        {"jaut": "Ģeometrijai jādod 40 % no 7 h. Cik minūšu?", "atb": ["168"],
         "padoms": "0,4 · 420."},
    ]),

    Varianti("Kurš plāns labāks?", [
        {"jaut": "Temats, kurā rezultāts 90 %...",
         "opcijas": ["atkārto īsi, beigās", "atkārto pirmo un visilgāk"],
         "jaukt": False, "pareizi": 0, "padoms": "Laiks vājākajiem."},
        {"jaut": "Trigonometriju atkārtot...",
         "opcijas": ["divreiz ar nedēļas starplaiku",
                     "vienreiz 3 stundas pēc kārtas"],
         "jaukt": False, "pareizi": 0, "padoms": "Starplaiki palīdz atcerēties."},
        {"jaut": "Pēc pilna darba...",
         "opcijas": ["izanalizē katru kļūdu", "uzreiz ņem nākamo darbu"],
         "jaukt": False, "pareizi": 0, "padoms": "Kļūdas ir plāna ieeja."},
    ]),

    Petijums("Mans plāns", [
        "Uzraksti eksāmena datumu un saskaiti nedēļas līdz tam.",
        "Izvēlies dienas un minūtes nedēļā, ko tiešām vari atvēlēt.",
        "Ievelc tabulā 3 vājākās jomas no 167. stundas - katru divreiz.",
        "Pēdējās 2 nedēļās ieplāno pilnus darbus.",
        "Pie katras nedēļas atstāj rūtiņu «izdarīts».",
    ], vajag="kalendārs, 167. stundas saraksts",
       secinajums="Plāns ir labs, ja tas ir reāls - labāk 20 min katru "
                  "dienu nekā 3 h, kas nenotiek."),

    Pasaule("Laiks pa jomām",
            Ievadi("", [
                {"jaut": "Tev ir 600 min. Jomām dod laiku attiecībā "
                         "funkcijas : ģeometrija : pārējais = 3 : 2 : 1. "
                         "Cik min funkcijām?", "atb": ["300"],
                 "padoms": "600 : 6 · 3."},
                {"jaut": "Cik min ģeometrijai?", "atb": ["200"],
                 "padoms": "600 : 6 · 2."},
            ]),
            pavediens="skola",
            konteksts="Diagnosticējošā darbā funkcijās bija 40 %, ģeometrijā "
                      "55 %, pārējā - virs 75 %.",
            kapec="Proporcionāla dalīšana - tas pats rēķins, ko lieto "
                  "receptēs un budžetā."),

    Kopsavilkums([
        "Saskaitu pieejamo laiku.",
        "Sadalu laiku proporcionāli vājumam.",
        "Ieplānoju atkārtošanu ar starplaikiem un pilnus darbus.",
    ]),

    Majas([
        "Pabeidz plānu un pieliec to redzamā vietā.",
        "Izpildi pirmās nedēļas pirmo atkārtojumu.",
        "Pēc nedēļas atzīmē, kas izdevās, un pielāgo plānu.",
    ]),
]
