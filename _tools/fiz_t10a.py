# -*- coding: utf-8 -*-
"""10. temats "Līdzstrāva". A daļa: 10.1.-10.5. stunda.

10.5. ir dubultstunda (plānā "st2") - virknes un paralēlais slēgums.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "10. temats. Līdzstrāva"
KICKER = "FIZIKA I · 11. KLASE · 10. TEMATS: LĪDZSTRĀVA"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/10. Līdzstrāva"

STUNDAS = [

dict(
    nr="10.1", virsraksts="Strāva, shēma un drošība",
    jautajums="Kā droši saslēgt elektrisko ķēdi?",
    apaksraksts="I = q/t · Ampērmetrs virknē · Voltmetrs paralēli",
    merkis="Lasīt vienkāršu shēmu, atšķirt strāvas stiprumu no sprieguma "
           "un pareizi pieslēgt mēraparātus.",
    protu=["izskaidrot, kas ir elektriskā strāva;",
           "lietot I = q/t;",
           "lasīt un zīmēt vienkāršu shēmu;",
           "pareizi pieslēgt ampērmetru un voltmetru."],
    atkartojums="9. tematā lādiņi bija nekustīgi. Tagad tie kustas - un "
                "sakārtota lādiņu kustība ir elektriskā strāva.",
    uzdevumu_apraksts="Strāvas stiprums un shēmas lasīšana",
    teorija=[
        ("Elektriskā strāva", [
            ("formula", "STRĀVAS STIPRUMS",
             "I = q/t        q = It        [I] = ampērs (A)",
             "Strāvas stiprums rāda, cik liels lādiņš izplūst caur "
             "vadītāja šķērsgriezumu vienā sekundē. Viens ampērs ir "
             "viens kulons sekundē.", GOLD),
            ("kartitas", [
                ("KAS PLŪST", BLUE,
                 ["Metālā - brīvie elektroni.",
                  "Šķīdumā - joni.",
                  "Kustība sakārtota."]),
                ("VIRZIENS", GREEN,
                 ["Par virzienu pieņem",
                  "pozitīvo lādiņu kustību.",
                  "Elektroni iet pretēji."]),
                ("KAS VAJADZĪGS", GOLD,
                 ["Brīvie lādiņnesēji.",
                  "Spriegums (avots).",
                  "Noslēgta ķēde."]),
            ]),
        ]),
        ("Shēma un mēraparāti", [
            ("tabula",
             ["Elements", "Ko dara", "Kā pieslēdz"],
             [["Strāvas avots", "Uztur spriegumu", "Ķēdes sākumā"],
              ["Ampērmetrs", "Mēra strāvu I", "VIRKNĒ ar patērētāju"],
              ["Voltmetrs", "Mēra spriegumu U", "PARALĒLI patērētājam"],
              ["Reostats", "Maina pretestību", "Virknē ķēdē"]],
             [3.00, 3.60, 3.63]),
            ("panelis", "DROŠĪBAS NOTEIKUMI",
             ["Ampērmetru nekad neslēdz tieši pie avota poliem - tam ir "
              "ļoti maza pretestība, un rodas īsslēgums.",
              "Ķēdi saslēdz pirms sprieguma ieslēgšanas; skolotājs "
              "pārbauda shēmu pirms ieslēgšanas.",
              "Laboratorijā strādā tikai ar zemsprieguma avotiem (līdz "
              "24 V) un nepieskaras atsegtiem kontaktiem."], RED),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Lādiņš caur vadītāju",
             teksts="Caur spuldzi 2,0 minūtes plūst 0,50 A strāva.\n"
                    "Cik liels lādiņš izplūdis?",
             dots=["I = 0,50 A", "t = 2,0 min = 120 s"],
             jaaprekina=["q = ?"],
             formulas=["I = q/t", "q = It"],
             aprekins=["1)  t = 2,0 · 60 = 120 s",
                       "2)  q = 0,50 · 120",
                       "3)  q = 60 C"],
             atbilde="q = 60 C",
             piezime="Laiku vienmēr pārrēķina sekundēs - ampērs ir "
                     "kulons sekundē."),
        dict(nr=2, virsraksts="Strāvas stiprums",
             teksts="Caur vadītāju 30 sekundēs izplūst 9,0 C lādiņa.\n"
                    "Aprēķini strāvas stiprumu!",
             dots=["q = 9,0 C", "t = 30 s"],
             jaaprekina=["I = ?"],
             formulas=["I = q/t"],
             aprekins=["1)  I = 9,0 : 30",
                       "2)  I = 0,30 A"],
             atbilde="I = 0,30 A",
             piezime="Tipiska LED spuldzes strāva - desmitdaļas ampēra."),
        dict(nr=3, virsraksts="Elektronu skaits",
             teksts="Caur vadītāju plūst 0,32 A strāva 1,0 s.\n"
                    "Cik elektronu izplūst? (e = 1,6·10⁻¹⁹ C)",
             dots=["I = 0,32 A", "t = 1,0 s", "e = 1,6·10⁻¹⁹ C"],
             jaaprekina=["N = ?"],
             formulas=["q = It", "N = q/e"],
             aprekins=["1)  q = 0,32 · 1,0 = 0,32 C",
                       "2)  N = 0,32 : 1,6·10⁻¹⁹",
                       "3)  N = 2·10¹⁸ elektronu"],
             atbilde="N = 2·10¹⁸",
             piezime="Katrs elektrons kustas lēni, bet to ir tik daudz, "
                     "ka strāva ir ievērojama."),
        dict(nr=4, virsraksts="Mēraparātu pieslēgums",
             teksts="Ķēdē ar spuldzi jāizmēra strāva caur spuldzi un\n"
                    "spriegums uz tās. Kā pieslēdz katru mēraparātu\n"
                    "un kāpēc?",
             dots=["Ampērmetrs mēra I", "Voltmetrs mēra U"],
             jaaprekina=["Pieslēgums = ?"],
             formulas=["Ampērmetram maza pretestība",
                       "Voltmetram liela pretestība"],
             aprekins=["1)  Ampērmetrs virknē - visa strāva iet caur to",
                       "2)  Voltmetrs paralēli - mēra spriegumu uz spuldzes",
                       "3)  Otrādi saslēdzot, rastos īsslēgums"],
             atbilde="Ampērmetrs virknē, voltmetrs paralēli",
             piezime="Atceries pēc jēgas: strāvai jāiet CAURI "
                     "ampērmetram, spriegums ir STARP diviem punktiem."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Strāva ir sakārtota lādiņu kustība.",
            "I = q/t; strāvas stiprumu mēra ampēros.",
            "Strāvai vajadzīgi lādiņnesēji, spriegums un noslēgta ķēde.",
            "Ampērmetru slēdz virknē, voltmetru - paralēli.",
        ],
        majasdarbs=[
            "I = 0,80 A, t = 5,0 min. Aprēķini q.",
            "q = 24 C, t = 40 s. Aprēķini I.",
            "Uzzīmē shēmu ar avotu, spuldzi, slēdzi un abiem "
            "mēraparātiem.",
        ],
        pasvertejums=["Zinu, kas ir strāva",
                      "Protu lietot I = q/t",
                      "Protu lasīt shēmu",
                      "Zinu mēraparātu pieslēgumu"],
        nakama="Nākamā stunda: Oma likums un raksturlīkne."),
),

dict(
    nr="10.2", virsraksts="Oma likums un raksturlīkne",
    jautajums="Kā pretestība ietekmē strāvu?",
    apaksraksts="I = U/R · R = U/I · Raksturlīkne I(U)",
    merkis="Lietot Oma likumu un no I(U) grafika noteikt pretestību.",
    protu=["formulēt Oma likumu ķēdes posmam;",
           "lietot I = U/R un R = U/I;",
           "nolasīt raksturlīkni I(U);",
           "no grafika noteikt pretestību."],
    atkartojums="Iepriekšējā stundā noskaidrojām, ka strāvai vajadzīgs "
                "spriegums. Šodien atradīsim, cik liela strāva rodas pie "
                "dotā sprieguma.",
    uzdevumu_apraksts="Oma likums un grafiku lasīšana",
    teorija=[
        ("Oma likums", [
            ("formula", "OMA LIKUMS ĶĒDES POSMAM",
             "I = U/R        U = IR        R = U/I        [R] = omi (Ω)",
             "Strāvas stiprums posmā ir tieši proporcionāls spriegumam "
             "un apgriezti proporcionāls pretestībai. Pretestība rāda, "
             "cik ļoti vadītājs pretojas strāvai.", GOLD),
            ("kartitas", [
                ("LIELĀKS U", BLUE,
                 ["Spriegums divkāršojas -",
                  "strāva divkāršojas.",
                  "Tieši proporcionāli."]),
                ("LIELĀKA R", RED,
                 ["Pretestība divkāršojas -",
                  "strāva samazinās divreiz.",
                  "Apgriezti proporcionāli."]),
                ("R VĒRTĪBAS", GREEN,
                 ["Vads - daļa oma.",
                  "Spuldze - desmiti omu.",
                  "Cilvēks - tūkstoši omu."]),
            ]),
        ]),
        ("Raksturlīkne", [
            ("tabula",
             ["U (V)", "I (A)", "R = U/I", "Secinājums"],
             [["2,0", "0,10", "20 Ω", "Pretestība nemainās"],
              ["4,0", "0,20", "20 Ω", "Punkti uz taisnes"],
              ["6,0", "0,30", "20 Ω", "Vadītājs pakļaujas Oma likumam"],
              ["8,0", "0,40", "20 Ω", "Taisne iet caur nulli"]],
             [2.20, 2.20, 2.40, 5.43]),
            ("panelis", "KO RĀDA GRAFIKS",
             ["Ja I(U) grafiks ir taisne caur koordinātu sākumu, "
              "pretestība ir nemainīga un vadītājs pakļaujas Oma likumam.",
              "Stāvāka taisne nozīmē MAZĀKU pretestību: tā pati sprieguma "
              "izmaiņa dod lielāku strāvas pieaugumu.",
              "Kvēlspuldzei līkne izliecas, jo, sakarstot, kvēldiega "
              "pretestība pieaug."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Strāva ķēdē",
             teksts="Uz rezistora ar pretestību 50 Ω ir spriegums 12 V.\n"
                    "Aprēķini strāvas stiprumu!",
             dots=["R = 50 Ω", "U = 12 V"],
             jaaprekina=["I = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  I = 12 : 50",
                       "2)  I = 0,24 A"],
             atbilde="I = 0,24 A",
             piezime="Pārbaude: 0,24 · 50 = 12 V - atgriežamies pie "
                     "dotā."),
        dict(nr=2, virsraksts="Pretestība",
             teksts="Pie sprieguma 9,0 V caur rezistoru plūst 0,30 A.\n"
                    "Aprēķini pretestību!",
             dots=["U = 9,0 V", "I = 0,30 A"],
             jaaprekina=["R = ?"],
             formulas=["R = U/I"],
             aprekins=["1)  R = 9,0 : 0,30",
                       "2)  R = 30 Ω"],
             atbilde="R = 30 Ω",
             piezime="Tieši tā pretestību nosaka arī no grafika - dala "
                     "spriegumu ar strāvu."),
        dict(nr=3, virsraksts="Spriegums",
             teksts="Caur sildelementu ar pretestību 25 Ω plūst 8,0 A\n"
                    "strāva. Aprēķini spriegumu!",
             dots=["R = 25 Ω", "I = 8,0 A"],
             jaaprekina=["U = ?"],
             formulas=["I = U/R", "U = IR"],
             aprekins=["1)  U = 8,0 · 25",
                       "2)  U = 200 V"],
             atbilde="U = 200 V",
             piezime="Sildierīcēm ir maza pretestība un liela strāva - "
                     "tāpēc tām vajag biezākus vadus."),
        dict(nr=4, virsraksts="Pretestība no grafika",
             teksts="Raksturlīknē punktam atbilst U = 6,0 V un I = 0,30 A,\n"
                    "un taisne iet caur koordinātu sākumu.\n"
                    "Nosaki pretestību un strāvu pie 10 V!",
             dots=["U₁ = 6,0 V", "I₁ = 0,30 A", "U₂ = 10 V"],
             jaaprekina=["R = ?", "I₂ = ?"],
             formulas=["R = U/I", "I = U/R"],
             aprekins=["1)  R = 6,0 : 0,30 = 20 Ω",
                       "2)  I₂ = 10 : 20",
                       "3)  I₂ = 0,50 A"],
             atbilde="R = 20 Ω;  I₂ = 0,50 A",
             piezime="Ja taisne iet caur nulli, pietiek ar vienu punktu, "
                     "lai atrastu pretestību."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Oma likums posmam: I = U/R.",
            "No tā izriet U = IR un R = U/I.",
            "Taisne caur nulli I(U) grafikā nozīmē nemainīgu pretestību.",
            "Stāvāka taisne nozīmē mazāku pretestību.",
        ],
        majasdarbs=[
            "U = 24 V, R = 60 Ω. Aprēķini I.",
            "U = 4,5 V, I = 0,15 A. Aprēķini R.",
            "I = 2,0 A, R = 12 Ω. Aprēķini U.",
        ],
        pasvertejums=["Zinu Oma likumu",
                      "Protu izteikt visus trīs lielumus",
                      "Protu lasīt raksturlīkni",
                      "Protu noteikt R no grafika"],
        nakama="Nākamā stunda: uzdevumi par Oma likumu."),
),

dict(
    nr="10.3", virsraksts="Uzdevumi: Oma likums",
    jautajums="Kā pārbaudīt aprēķina ticamību?",
    apaksraksts="Viena un divu soļu uzdevumi · Mērvienības · Pārbaude",
    merkis="Risināt viena un divu soļu uzdevumus par strāvu, spriegumu un "
           "pretestību un pārbaudīt rezultāta ticamību.",
    protu=["izvēlēties pareizo formulas formu;",
           "risināt divu soļu uzdevumus;",
           "pārrēķināt mērvienības pirms aprēķina;",
           "novērtēt, vai atbilde ir saprātīga."],
    atkartojums="Oma likumu jau zinām. Šodien mācīsimies to lietot "
                "situācijās, kur meklēto lielumu nevar atrast vienā "
                "solī.",
    uzdevumu_apraksts="Divu soļu uzdevumi un pārbaude",
    teorija=[
        ("Kā risināt", [
            ("panelis", "ČETRI SOĻI KATRAM UZDEVUMAM",
             ["1. Pieraksti doto un pārrēķini SI vienībās: mA ampēros, "
              "kΩ omos, minūtes sekundēs.",
              "2. Nosaki, ko meklē, un izvēlies formulu, kurā ir tikai "
              "viens nezināmais.",
              "3. Ja tāda nav, atrodi starplielumu - tas ir divu soļu "
              "uzdevums.",
              "4. Pārbaudi atbildi: vai lielums ir saprātīgs un vai "
              "mērvienība ir pareiza."], NAVY),
            ("tabula",
             ["Mērvienība", "Pārrēķins", "Kur sastopas"],
             [["1 mA", "0,001 A", "LED, elektronika"],
              ["1 kΩ", "1000 Ω", "Rezistori shēmās"],
              ["1 MΩ", "10⁶ Ω", "Izolācijas pretestība"],
              ["1 mV", "0,001 V", "Sensoru signāli"]],
             [3.00, 3.20, 4.03]),
        ]),
        ("Ticamības pārbaude", [
            ("divi",
             ("SAPRĀTĪGI SKAITĻI", GREEN,
              ["Mājas ierīcēm I = 0,1-10 A.",
               "Spuldzēm R = 10-1000 Ω.",
               "Baterijām U = 1,5-12 V.",
               "Rozetē U = 230 V."]),
             ("AIZDOMĪGI SKAITĻI", RED,
              ["I = 5000 A mājas ķēdē.",
               "R = 0,001 Ω spuldzei.",
               "U = 10 000 V baterijai.",
               "Negatīva pretestība."])),
            ("panelis", "PĀRBAUDE AR ATGRIEZENISKO SOLI",
             ["Ievieto atrasto lielumu atpakaļ formulā un pārliecinies, "
              "vai iegūsti doto vērtību.",
              "Piemērs: ja I = 0,24 A un R = 50 Ω, tad U = 0,24 · 50 = "
              "12 V - tieši tas, kas bija dots.",
              "Šis solis pārbaudes darbā aizņem 20 sekundes un pasargā "
              "no rupjas kļūdas."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Miliampēri ampēros",
             teksts="Caur LED plūst 20 mA strāva, tā pretestība 150 Ω.\n"
                    "Aprēķini spriegumu uz LED!",
             dots=["I = 20 mA = 0,020 A", "R = 150 Ω"],
             jaaprekina=["U = ?"],
             formulas=["U = IR"],
             aprekins=["1)  I = 20 : 1000 = 0,020 A",
                       "2)  U = 0,020 · 150",
                       "3)  U = 3,0 V"],
             atbilde="U = 3,0 V",
             piezime="3 V ir tipisks LED spriegums - atbilde ir "
                     "saprātīga."),
        dict(nr=2, virsraksts="Divi soļi: lādiņš un pretestība",
             teksts="Caur rezistoru 60 s laikā izplūst 18 C lādiņa, un\n"
                    "spriegums uz tā ir 12 V. Aprēķini pretestību!",
             dots=["q = 18 C", "t = 60 s", "U = 12 V"],
             jaaprekina=["R = ?"],
             formulas=["I = q/t", "R = U/I"],
             aprekins=["1)  I = 18 : 60 = 0,30 A",
                       "2)  R = 12 : 0,30",
                       "3)  R = 40 Ω"],
             atbilde="R = 40 Ω",
             piezime="Pirmais solis deva strāvu, otrais - pretestību. "
                     "Bez starplieluma neiztikt."),
        dict(nr=3, virsraksts="Kiloomi shēmā",
             teksts="Rezistoram 2,2 kΩ pieliek spriegumu 11 V.\n"
                    "Aprēķini strāvu miliampēros!",
             dots=["R = 2,2 kΩ = 2200 Ω", "U = 11 V"],
             jaaprekina=["I = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  R = 2,2 · 1000 = 2200 Ω",
                       "2)  I = 11 : 2200 = 0,005 A",
                       "3)  I = 5,0 mA"],
             atbilde="I = 5,0 mA",
             piezime="Elektronikā atbildi parasti izsaka miliampēros - "
                     "skaitlis kļūst ērtāks."),
        dict(nr=4, virsraksts="Ticamības pārbaude",
             teksts="Skolēns ieguva, ka mājas spuldzei pie 230 V strāva\n"
                    "ir 46 A. Pārbaudi, vai tas ir ticami, ja spuldzes\n"
                    "pretestība ir 500 Ω!",
             dots=["U = 230 V", "R = 500 Ω", "Skolēna atbilde 46 A"],
             jaaprekina=["I = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  I = 230 : 500 = 0,46 A",
                       "2)  Skolēns kļūdījies 100 reizes",
                       "3)  46 A izsistu drošinātāju"],
             atbilde="I = 0,46 A - skolēna atbilde nav ticama",
             piezime="Mājas ķēdes drošinātājs ir 16 A - lielāka strāva "
                     "vienkārši nav iespējama."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Vispirms pārrēķina mērvienības, tikai tad rēķina.",
            "Divu soļu uzdevumā vispirms atrod starplielumu.",
            "Atbildi pārbauda, ievietojot to atpakaļ formulā.",
            "Saprātīguma pārbaude pasargā no rupjām kļūdām.",
        ],
        majasdarbs=[
            "I = 50 mA, R = 220 Ω. Aprēķini U.",
            "q = 30 C, t = 50 s, U = 9,0 V. Aprēķini R.",
            "U = 230 V, R = 46 Ω. Aprēķini I un novērtē ticamību.",
        ],
        pasvertejums=["Protu pārrēķināt vienības",
                      "Protu risināt divu soļu uzdevumus",
                      "Protu pārbaudīt atbildi",
                      "Protu novērtēt ticamību"],
        nakama="Nākamā stunda: vadītāja pretestība un R = ρl/S."),
),

dict(
    nr="10.4", virsraksts="Vadītāja pretestība",
    jautajums="No kā atkarīga vada pretestība?",
    apaksraksts="R = ρl/S · Īpatnējā pretestība · Materiāla izvēle",
    merkis="Lietot sakarību R = ρl/S un pamatot vadītāja materiāla izvēli.",
    protu=["nosaukt, no kā atkarīga vada pretestība;",
           "lietot R = ρl/S;",
           "izskaidrot īpatnējās pretestības jēgu;",
           "pamatot vara un alumīnija izvēli vados."],
    atkartojums="Iepriekš pretestību uzskatījām par doto skaitli. Šodien "
                "noskaidrosim, no kā tā rodas un kā to var aprēķināt "
                "pirms mērīšanas.",
    uzdevumu_apraksts="Vadītāja pretestības aprēķini",
    teorija=[
        ("Pretestības formula", [
            ("formula", "VADĪTĀJA PRETESTĪBA",
             "R = ρl/S        ρ - īpatnējā pretestība",
             "Pretestība ir tieši proporcionāla vadītāja garumam un "
             "apgriezti proporcionāla šķērsgriezuma laukumam. ρ ir "
             "materiāla īpašība; to mēra omos reiz kvadrātmilimetrs uz "
             "metru.", GOLD),
            ("kartitas", [
                ("GARUMS l", BLUE,
                 ["Garāks vads -",
                  "lielāka pretestība.",
                  "Tieši proporcionāli."]),
                ("LAUKUMS S", GREEN,
                 ["Biezāks vads -",
                  "mazāka pretestība.",
                  "Apgriezti proporcionāli."]),
                ("MATERIĀLS ρ", GOLD,
                 ["Varš vada vislabāk.",
                  "Nihroms - slikti.",
                  "Tāpēc to lieto sildelementos."]),
            ]),
        ]),
        ("Materiāli", [
            ("tabula",
             ["Materiāls", "ρ (Ω·mm²/m)", "Kur lieto"],
             [["Varš", "0,017", "Mājas instalācija, vadi"],
              ["Alumīnijs", "0,028", "Gaisa līnijas - viegls"],
              ["Tērauds", "0,10", "Nesošās konstrukcijas"],
              ["Nihroms", "1,1", "Sildelementi, reostati"]],
             [3.20, 3.00, 4.03]),
            ("panelis", "KĀPĒC TIEŠI VARŠ UN ALUMĪNIJS",
             ["Varam ir maza īpatnējā pretestība un tas labi lodējams - "
              "tāpēc to lieto mājas instalācijā.",
              "Alumīnijs vada nedaudz sliktāk, bet ir trīs reizes "
              "vieglāks - tāpēc to lieto augstsprieguma gaisa līnijās.",
              "Nihromam pretestība ir gandrīz 65 reizes lielāka nekā "
              "varam - tieši tāpēc tas sakarst un der sildītājiem."],
             NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vara vada pretestība",
             teksts="Vara vads ir 100 m garš, šķērsgriezuma laukums\n"
                    "2,0 mm². Aprēķini pretestību!\n"
                    "(ρ = 0,017 Ω·mm²/m)",
             dots=["l = 100 m", "S = 2,0 mm²", "ρ = 0,017"],
             jaaprekina=["R = ?"],
             formulas=["R = ρl/S"],
             aprekins=["1)  ρl = 0,017 · 100 = 1,7",
                       "2)  R = 1,7 : 2,0",
                       "3)  R = 0,85 Ω"],
             atbilde="R = 0,85 Ω",
             piezime="Simts metru vada pretestība ir mazāka par omu - "
                     "tāpēc vados spriegums gandrīz nezūd."),
        dict(nr=2, virsraksts="Biezāks vads",
             teksts="To pašu 100 m vara vadu nomaina pret vadu ar\n"
                    "laukumu 4,0 mm². Kā mainās pretestība?\n"
                    "(ρ = 0,017 Ω·mm²/m)",
             dots=["l = 100 m", "S = 4,0 mm²", "ρ = 0,017"],
             jaaprekina=["R = ?"],
             formulas=["R = ρl/S"],
             aprekins=["1)  R = 0,017 · 100 : 4,0",
                       "2)  R = 0,425 Ω",
                       "3)  Divreiz biezāks - divreiz mazāka R"],
             atbilde="R ≈ 0,43 Ω",
             piezime="Tāpēc lielas jaudas ierīcēm velk biezākus vadus - "
                     "lai tie nesasiltu."),
        dict(nr=3, virsraksts="Nihroma spirāle",
             teksts="Sildītāja nihroma spirāle ir 5,0 m gara ar laukumu\n"
                    "0,20 mm². Aprēķini pretestību! (ρ = 1,1 Ω·mm²/m)",
             dots=["l = 5,0 m", "S = 0,20 mm²", "ρ = 1,1"],
             jaaprekina=["R = ?"],
             formulas=["R = ρl/S"],
             aprekins=["1)  ρl = 1,1 · 5,0 = 5,5",
                       "2)  R = 5,5 : 0,20",
                       "3)  R = 27,5 Ω"],
             atbilde="R ≈ 27,5 Ω",
             piezime="Tāda pretestība pie 230 V dod apmēram 8 A - "
                     "tipisks sildītājs."),
        dict(nr=4, virsraksts="Meklē garumu",
             teksts="Cik garš jābūt nihroma vadam ar laukumu 0,50 mm²,\n"
                    "lai tā pretestība būtu 44 Ω? (ρ = 1,1 Ω·mm²/m)",
             dots=["R = 44 Ω", "S = 0,50 mm²", "ρ = 1,1"],
             jaaprekina=["l = ?"],
             formulas=["R = ρl/S", "l = RS/ρ"],
             aprekins=["1)  RS = 44 · 0,50 = 22",
                       "2)  l = 22 : 1,1",
                       "3)  l = 20 m"],
             atbilde="l = 20 m",
             piezime="Tieši tā ražotājs izvēlas spirāles garumu "
                     "vajadzīgajai jaudai."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "R = ρl/S - pretestība atkarīga no garuma, laukuma un "
            "materiāla.",
            "Garāks vads - lielāka pretestība; biezāks - mazāka.",
            "Īpatnējā pretestība ir materiāla īpašība.",
            "Varš un alumīnijs vada labi, nihroms - slikti.",
        ],
        majasdarbs=[
            "l = 50 m, S = 1,0 mm², varš. Aprēķini R.",
            "l = 2,0 m, S = 0,10 mm², nihroms. Aprēķini R.",
            "Paskaidro, kāpēc gaisa līnijās lieto alumīniju, nevis varu.",
        ],
        pasvertejums=["Zinu, no kā atkarīga R",
                      "Protu lietot R = ρl/S",
                      "Saprotu ρ jēgu",
                      "Protu pamatot materiāla izvēli"],
        nakama="Nākamā stunda (dubultstunda): virknes un paralēlais "
               "slēgums."),
),

dict(
    nr="10.5", virsraksts="Virknes un paralēlais slēgums",
    jautajums="Kāpēc mājas ierīces slēdz paralēli?",
    apaksraksts="Virknē R = R₁ + R₂ · Paralēli R = R₁R₂/(R₁ + R₂)",
    merkis="Salīdzināt strāvu un spriegumu abos slēgumos un risināt divu "
           "rezistoru uzdevumus.",
    protu=["nosaukt strāvas un sprieguma īpašības abos slēgumos;",
           "aprēķināt ekvivalento pretestību virknē;",
           "aprēķināt ekvivalento pretestību paralēli;",
           "pamatot, kāpēc mājās lieto paralēlo slēgumu."],
    atkartojums="Līdz šim ķēdē bija viens patērētājs. Reālās ķēdēs to ir "
                "vairāki - un ir tikai divi pamatveidi, kā tos savienot.",
    uzdevumu_apraksts="Divu rezistoru slēgumi",
    teorija=[
        ("Divi slēgumu veidi", [
            ("formula", "EKVIVALENTĀ PRETESTĪBA",
             "Virknē: R = R₁ + R₂        Paralēli: R = R₁R₂/(R₁ + R₂)",
             "Virknē pretestības saskaita. Paralēli kopējā pretestība ir "
             "mazāka par mazāko no abām; vairākiem rezistoriem lieto "
             "apgriezto vērtību summu.", GOLD),
            ("divi",
             ("VIRKNES SLĒGUMS", BLUE,
              ["Strāva visur VIENĀDA.",
               "Spriegumi SASKAITĀS.",
               "R = R₁ + R₂.",
               "Viens pārtrūkst - visa",
               "ķēde pārtrūkst."]),
             ("PARALĒLAIS SLĒGUMS", GREEN,
              ["Spriegums visur VIENĀDS.",
               "Strāvas SASKAITĀS.",
               "R mazāka par mazāko.",
               "Viens pārtrūkst - pārējie",
               "strādā tālāk."])),
        ]),
        ("Kur ko lieto", [
            ("tabula",
             ["Situācija", "Slēgums", "Kāpēc"],
             [["Mājas rozetes", "Paralēli", "Visām 230 V, darbojas atsevišķi"],
              ["Egles virtene", "Virknē", "Lēti, bet viena spuldze aptur visu"],
              ["Drošinātājs", "Virknē", "Pārtrauc visu ķēdi"],
              ["Slēdzis", "Virknē", "Atslēdz savu patērētāju"]],
             [3.20, 2.60, 4.43]),
            ("panelis", "KĀPĒC MĀJĀS PARALĒLI",
             ["Paralēlā slēgumā katrai ierīcei ir pilns 230 V spriegums, "
              "neatkarīgi no tā, cik ierīču ieslēgtas.",
              "Katru ierīci var ieslēgt un izslēgt atsevišķi, un vienas "
              "bojājums neaptur pārējās.",
              "Trūkums: jo vairāk ierīču, jo lielāka kopējā strāva - "
              "tāpēc ķēdi aizsargā drošinātājs."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Virknes slēgums",
             teksts="Divus rezistorus 30 Ω un 20 Ω saslēdz virknē un\n"
                    "pieliek 10 V. Aprēķini kopējo pretestību un strāvu!",
             dots=["R₁ = 30 Ω", "R₂ = 20 Ω", "U = 10 V"],
             jaaprekina=["R = ?", "I = ?"],
             formulas=["R = R₁ + R₂", "I = U/R"],
             aprekins=["1)  R = 30 + 20 = 50 Ω",
                       "2)  I = 10 : 50",
                       "3)  I = 0,20 A"],
             atbilde="R = 50 Ω;  I = 0,20 A",
             piezime="Virknē strāva ir vienāda abos rezistoros - 0,20 A."),
        dict(nr=2, virsraksts="Spriegumu sadalījums",
             teksts="Iepriekšējā ķēdē aprēķini spriegumu uz katra\n"
                    "rezistora un pārbaudi to summu!",
             dots=["R₁ = 30 Ω", "R₂ = 20 Ω", "I = 0,20 A"],
             jaaprekina=["U₁ = ?", "U₂ = ?"],
             formulas=["U = IR"],
             aprekins=["1)  U₁ = 0,20 · 30 = 6,0 V",
                       "2)  U₂ = 0,20 · 20 = 4,0 V",
                       "3)  Summa: 6,0 + 4,0 = 10 V"],
             atbilde="U₁ = 6,0 V;  U₂ = 4,0 V",
             piezime="Lielākā pretestība saņem lielāko spriegumu - tā "
                     "vienmēr ir pārbaude."),
        dict(nr=3, virsraksts="Paralēlais slēgums",
             teksts="Rezistorus 30 Ω un 20 Ω saslēdz paralēli un pieliek\n"
                    "12 V. Aprēķini kopējo pretestību!",
             dots=["R₁ = 30 Ω", "R₂ = 20 Ω", "U = 12 V"],
             jaaprekina=["R = ?"],
             formulas=["R = R₁R₂/(R₁ + R₂)"],
             aprekins=["1)  R₁R₂ = 30 · 20 = 600",
                       "2)  R₁ + R₂ = 50",
                       "3)  R = 600 : 50 = 12 Ω"],
             atbilde="R = 12 Ω",
             piezime="Pārbaude: 12 Ω ir mazāk par 20 Ω - paralēlā "
                     "slēgumā tā vienmēr ir."),
        dict(nr=4, virsraksts="Strāvu sadalījums",
             teksts="Iepriekšējā paralēlajā ķēdē aprēķini strāvu katrā\n"
                    "zarā un kopējo strāvu!",
             dots=["R₁ = 30 Ω", "R₂ = 20 Ω", "U = 12 V"],
             jaaprekina=["I₁ = ?", "I₂ = ?", "I = ?"],
             formulas=["I = U/R", "I = I₁ + I₂"],
             aprekins=["1)  I₁ = 12 : 30 = 0,40 A",
                       "2)  I₂ = 12 : 20 = 0,60 A",
                       "3)  I = 0,40 + 0,60 = 1,0 A"],
             atbilde="I₁ = 0,40 A;  I₂ = 0,60 A;  I = 1,0 A",
             piezime="Pārbaude ar kopējo pretestību: 12 : 12 = 1,0 A - "
                     "sakrīt."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Virknē strāva vienāda, spriegumi saskaitās, R = R₁ + R₂.",
            "Paralēli spriegums vienāds, strāvas saskaitās.",
            "Paralēlā slēgumā kopējā pretestība mazāka par mazāko.",
            "Mājas ierīces slēdz paralēli, lai tās darbotos neatkarīgi.",
        ],
        majasdarbs=[
            "R₁ = 40 Ω, R₂ = 60 Ω virknē, U = 20 V. Aprēķini R un I.",
            "Tie paši rezistori paralēli, U = 24 V. Aprēķini R un I.",
            "Paskaidro, kāpēc virknes virtenē viena spuldze aptur visas.",
        ],
        pasvertejums=["Zinu abu slēgumu īpašības",
                      "Protu rēķināt R virknē",
                      "Protu rēķināt R paralēli",
                      "Protu pamatot slēguma izvēli"],
        nakama="Nākamā stunda: LD2 sagatavošana."),
),

]
