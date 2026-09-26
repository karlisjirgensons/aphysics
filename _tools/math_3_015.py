# -*- coding: utf-8 -*-
"""3. klase, 15. stunda: «Kā trenēties ar digitālu rīku?»

Digitālais treniņš ir šīs pašas lapas uzdevumu bloks - skolēns to izmēģina
uzreiz un tad iemācās nolasīt savu rezultātu: cik izdarīja, cik ātri un ko
tas nozīmē. Bez šī otrā soļa treniņš ir spēle, nevis mācīšanās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Kā trenēties ar digitālu rīku?"

MERKIS = ("Iemācīsimies trenēt reizināšanas tabulu ar lietotni un sekot "
          "savam progresam.")

SATURS = [
    Sakums("Kā pateikt, vai treniņš tiešām palīdz?",
           zimejums=kolonnas([("pirmdien", 12), ("trešdien", 18),
                              ("piektdien", 25)], " pareizi"),
           paraksts="Trīs treniņi nedēļā - un rezultāts ir redzams.",
           fakti=["Rīks pats pasaka, cik atbilžu bija pareizas.",
                  "Progress ir redzams tikai tad, ja rezultātu pieraksta."]),

    Doma("Treniņš bez pieraksta ir tikai spēle",
         "Pieraksti katru reizi divus skaitļus - cik uzdevumu un cik pareizi - "
         "un salīdzini tos ar iepriekšējo reizi.",
         soli=[
             "Izvēlies, kuru rindu šodien trenēsi.",
             "Izdari vienu piegājienu līdz galam, neskatoties tabulā.",
             "Pieraksti, cik bija pareizi.",
             "Atzīmē tos reizinājumus, kuros kļūdījies.",
             "Nākamajā reizē sāc tieši ar tiem.",
         ],
         pieze="Vissvarīgākais skaitlis nav punkti, bet *kļūdu saraksts*: tas "
               "pasaka, ko darīt rīt."),

    Paraugs("Vai šodien sanāca labāk?",
            uzd="Pirmdien bija 12 pareizas atbildes no 20, piektdien - 17 no "
                "20. Par cik rezultāts uzlabojās?",
            soli=[
                ("17 − 12 = 5",
                 "Starpība parāda, par cik atbilžu vairāk."),
                ("20 − 17 = 3",
                 "Tik daudz vēl jātrenē."),
                ("Rezultāts uzlabojās par 5 atbildēm",
                 "Trīs uzdevumi paliek nākamajai reizei."),
            ],
            atbilde="par 5 atbildēm; vēl 3 jātrenē"),

    Ievadi("Treniņa piegājiens", [
        {"jaut": "8 · 9 = ?", "atb": ["72"], "padoms": "80 − 8."},
        {"jaut": "7 · 6 = ?", "atb": ["42"], "padoms": "35 + 7."},
        {"jaut": "9 · 4 = ?", "atb": ["36"], "padoms": "40 − 4."},
        {"jaut": "6 · 8 = ?", "atb": ["48"], "padoms": "24 + 24."},
        {"jaut": "7 · 9 = ?", "atb": ["63"], "padoms": "70 − 7."},
        {"jaut": "8 · 6 = ?", "atb": ["48"], "padoms": "Tas pats, kas 6 · 8."},
        {"jaut": "9 · 9 = ?", "atb": ["81"], "padoms": "90 − 9."},
        {"jaut": "7 · 8 = ?", "atb": ["56"], "padoms": "49 + 7."},
    ], pamats=4,
        ievads="Izdari visus astoņus un pieraksti, cik bija pareizi no "
               "pirmā mēģinājuma."),

    Petijums("Savs treniņu dienasgrāmatas ieraksts",
             vajag="burtnīca un zīmulis",
             soli=[
                 "Uzraksti datumu un to rindu, ko trenēji.",
                 "Pieraksti, cik uzdevumu izdarīji un cik bija pareizi.",
                 "Pieraksti tos reizinājumus, kuros kļūdījies.",
                 "Pēc nedēļas salīdzini pirmo un pēdējo ierakstu.",
             ],
             secinajums="Ja pareizo atbilžu skaits aug un kļūdu saraksts "
                        "sarūk, treniņš strādā."),

    Zimejums("Kļūdu saraksts sarūk",
             kolonnas([("1. ned.", 8), ("2. ned.", 5), ("3. ned.", 2)],
                      " kļūdas"),
             paskaidro="Tieši šis stabiņš ir īstais progresa mērs - nevis "
                       "punkti, ko rīks parāda.",
             ievads="Tā izskatās trīs nedēļu treniņš."),

    Varianti("Kā izmantot rīku gudri?", [
        {"jaut": "Ko darīt vispirms pēc treniņa?",
         "opcijas": ["Pierakstīt kļūdas", "Sākt jaunu piegājienu",
                     "Aizvērt lietotni", "Palielināt ātrumu"],
         "pareizi": 0, "padoms": "Kļūdas pasaka, ko trenēt rīt."},
        {"jaut": "Kurš rezultāts ir labāks: 15 no 20 vai 18 no 30?",
         "opcijas": ["15 no 20", "18 no 30", "Abi vienādi",
                     "To nevar pateikt"],
         "pareizi": 0, "padoms": "15 no 20 ir trīs ceturtdaļas, 18 no 30 - "
                                 "mazāk nekā divas trešdaļas."},
        {"jaut": "Vai drīkst treniņa laikā skatīties tabulā?",
         "opcijas": ["Nē, tad atmiņa netrenējas", "Jā, vienmēr",
                     "Jā, ja steidzies", "Tikai pirmajā uzdevumā"],
         "pareizi": 0, "padoms": "Vispirms jāmēģina atcerēties."},
        {"jaut": "Cik bieži labāk trenēties?",
         "opcijas": ["Īsi katru dienu", "Vienu reizi nedēļā ilgi",
                     "Reizi mēnesī", "Tikai pirms pārbaudes darba"],
         "pareizi": 0, "padoms": "Atmiņai palīdz biežums."},
    ], pamats=4),

    Pasaule("Cik datu saglabā treniņu lietotne?",
            Ievadi("", [
                {"jaut": "Lietotne saglabā 8 rezultātus dienā. Cik "
                         "rezultātu tā saglabās 7 dienās?",
                 "atb": ["56"], "padoms": "7 · 8."},
                {"jaut": "Cik rezultātu būs 9 dienās?",
                 "atb": ["72"], "padoms": "9 · 8."},
                {"jaut": "Lietotnē ir 48 rezultāti, katru dienu pa 8. Cik "
                         "dienas trenējies?",
                 "atb": ["6"], "padoms": "48 : 8."},
                {"jaut": "Vienā rezultātā ir 10 uzdevumi. Cik uzdevumu ir "
                         "48 rezultātos?",
                 "atb": ["480"], "padoms": "48 · 10."},
            ]),
            pavediens="dati",
            konteksts="Katrs treniņš lietotnē ir dati - skaitļi, kurus var "
                      "salikt tabulā un salīdzināt.",
            kapec="Dati ļauj redzēt progresu, ko ar aci nepamanītu."),

    Kopsavilkums([
        "Trenēju reizināšanas tabulu ar digitālu rīku.",
        "Pierakstu savu rezultātu un kļūdu sarakstu.",
        "Salīdzinu rezultātus dažādās dienās.",
        "Nākamo treniņu sāku ar to, kas iepriekš nepadevās.",
    ]),

    Majas([
        "Izdari vienu treniņa piegājienu un pieraksti rezultātu.",
        "Atzīmē trīs reizinājumus, kas nepadevās, un atkārto tos rīt.",
        "Pēc nedēļas salīdzini pirmo un pēdējo rezultātu.",
    ]),
]
