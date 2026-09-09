# -*- coding: utf-8 -*-
"""10. temats "Līdzstrāva". C daļa: 10.11.-10.15. stunda.

10.15. ir pēdējā mācību stunda pirms PD5.
"""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401
from fiz_t10a import TEMATS, KICKER, KURSS, MAPE              # noqa: F401

STUNDAS = [

dict(
    nr="10.11", virsraksts="Ekvivalentā pretestība",
    jautajums="Kā sarežģītu shēmu sadalīt vienkāršos soļos?",
    apaksraksts="Jaukts slēgums · Soli pa solim · Robežgadījumu pārbaude",
    merkis="Pakāpeniski noteikt ekvivalento pretestību jauktā slēgumā un "
           "pamatot katru pārveidošanas soli.",
    protu=["atpazīt, kuri rezistori slēgti virknē un kuri paralēli;",
           "pakāpeniski vienkāršot shēmu;",
           "aprēķināt ekvivalento pretestību;",
           "pārbaudīt rezultātu ar robežgadījumiem."],
    atkartojums="10.5. stundā apguvām abus pamatslēgumus. Reālās shēmās "
                "tie ir sajaukti - bet katru shēmu var sadalīt "
                "vienkāršos gabalos.",
    uzdevumu_apraksts="Jauktu slēgumu vienkāršošana",
    teorija=[
        ("Kā vienkāršot shēmu", [
            ("panelis", "TRĪS SOĻI",
             ["1. Atrodi rezistorus, kas noteikti slēgti PARALĒLI (abi "
              "gali savienoti ar tiem pašiem punktiem), un aizstāj tos ar "
              "vienu.",
              "2. Tagad atlikušie parasti ir virknē - saskaiti tos.",
              "3. Atkārto, līdz paliek viena pretestība; katrā solī "
              "pieraksti, ko tieši aizstāji."], NAVY),
            ("formula", "ABAS PAMATFORMULAS",
             "Virknē: R = R₁ + R₂        Paralēli: R = R₁R₂/(R₁ + R₂)",
             "Vienādām paralēlām pretestībām rezultāts ir vienkāršs: "
             "divas vienādas dod pusi, trīs vienādas - trešdaļu no "
             "vienas pretestības.", GOLD),
        ]),
        ("Pārbaude", [
            ("tabula",
             ["Pārbaude", "Kas jāsanāk", "Ja nesanāk"],
             [["Paralēlais posms", "Mazāk par mazāko", "Kļūda formulā"],
              ["Virknes posms", "Vairāk par lielāko", "Saskaitīts nepareizi"],
              ["Divas vienādas paralēli", "Tieši puse", "Ātrā pārbaude"],
              ["Kopējā R", "Starp mazāko un summu", "Pārskati soļus"]],
             [3.60, 3.40, 3.23]),
            ("panelis", "ROBEŽGADĪJUMI",
             ["Ja viens paralēlais rezistors ir daudz mazāks par otru, "
              "kopējā pretestība ir gandrīz vienāda ar mazāko - lielākais "
              "gandrīz nevada strāvu.",
              "Ja rezistors ir īsslēgts ar vadu, tā pretestība shēmā "
              "kļūst nulle un to var izsvītrot.",
              "Šīs pārbaudes ļauj pamanīt kļūdu, pat neveicot pilnu "
              "aprēķinu."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Divas vienādas paralēli",
             teksts="Divus 60 Ω rezistorus slēdz paralēli.\n"
                    "Aprēķini ekvivalento pretestību!",
             dots=["R₁ = 60 Ω", "R₂ = 60 Ω"],
             jaaprekina=["R = ?"],
             formulas=["R = R₁R₂/(R₁ + R₂)"],
             aprekins=["1)  R₁R₂ = 3600",
                       "2)  R₁ + R₂ = 120",
                       "3)  R = 3600 : 120 = 30 Ω"],
             atbilde="R = 30 Ω",
             piezime="Divas vienādas paralēli vienmēr dod pusi - to var "
                     "pateikt bez aprēķina."),
        dict(nr=2, virsraksts="Jaukts slēgums",
             teksts="Rezistori 20 Ω un 30 Ω slēgti paralēli, un tiem\n"
                    "virknē pievienots 8,0 Ω rezistors.\n"
                    "Aprēķini kopējo pretestību!",
             dots=["R₁ = 20 Ω", "R₂ = 30 Ω", "R₃ = 8,0 Ω"],
             jaaprekina=["R = ?"],
             formulas=["R₁₂ = R₁R₂/(R₁ + R₂)", "R = R₁₂ + R₃"],
             aprekins=["1)  R₁R₂ = 600;  R₁ + R₂ = 50",
                       "2)  R₁₂ = 600 : 50 = 12 Ω",
                       "3)  R = 12 + 8,0 = 20 Ω"],
             atbilde="R = 20 Ω",
             piezime="Vispirms paralēlais posms, tikai tad virknes - "
                     "otrādi sanāktu nepareizi."),
        dict(nr=3, virsraksts="Strāva jauktā ķēdē",
             teksts="Iepriekšējo ķēdi pieslēdz 24 V spriegumam.\n"
                    "Aprēķini kopējo strāvu un spriegumu uz paralēlā\n"
                    "posma!",
             dots=["R = 20 Ω", "U = 24 V", "R₁₂ = 12 Ω"],
             jaaprekina=["I = ?", "U₁₂ = ?"],
             formulas=["I = U/R", "U = IR"],
             aprekins=["1)  I = 24 : 20 = 1,2 A",
                       "2)  U₁₂ = 1,2 · 12 = 14,4 V",
                       "3)  Uz 8 Ω: 1,2 · 8,0 = 9,6 V"],
             atbilde="I = 1,2 A;  U₁₂ = 14,4 V",
             piezime="Pārbaude: 14,4 + 9,6 = 24 V - visa sprieguma "
                     "summa sakrīt."),
        dict(nr=4, virsraksts="Robežgadījums",
             teksts="Paralēli slēgti rezistori 5,0 Ω un 500 Ω.\n"
                    "Aprēķini kopējo pretestību un paskaidro rezultātu!",
             dots=["R₁ = 5,0 Ω", "R₂ = 500 Ω"],
             jaaprekina=["R = ?"],
             formulas=["R = R₁R₂/(R₁ + R₂)"],
             aprekins=["1)  R₁R₂ = 2500;  R₁ + R₂ = 505",
                       "2)  R = 2500 : 505 ≈ 4,95 Ω",
                       "3)  Gandrīz vienāds ar mazāko"],
             atbilde="R ≈ 4,95 Ω",
             piezime="Lielā pretestība gandrīz nevada strāvu - visa "
                     "strāva iet pa mazākās pretestības ceļu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Jauktu shēmu vienkāršo pa soļiem - vispirms paralēlie posmi.",
            "Virknē pretestības saskaita, paralēli lieto reizinājuma "
            "formulu.",
            "Divas vienādas paralēli dod pusi.",
            "Robežgadījumi ļauj ātri pārbaudīt rezultātu.",
        ],
        majasdarbs=[
            "R₁ = 40 Ω un R₂ = 40 Ω paralēli. Aprēķini R.",
            "R₁ = 10 Ω, R₂ = 15 Ω paralēli, virknē R₃ = 4,0 Ω. Aprēķini R.",
            "R₁ = 2,0 Ω, R₂ = 200 Ω paralēli. Aprēķini R un paskaidro.",
        ],
        pasvertejums=["Protu atpazīt slēgumu veidus",
                      "Protu vienkāršot pa soļiem",
                      "Protu rēķināt ekvivalento R",
                      "Protu pārbaudīt rezultātu"],
        nakama="Nākamā stunda: sprieguma un strāvas sadalījums."),
),

dict(
    nr="10.12", virsraksts="Sprieguma un strāvas sadalījums",
    jautajums="Kā paredzēt mēraparāta rādījumu pirms mērījuma?",
    apaksraksts="Virknē U sadalās · Paralēli I sadalās · Paredzēt un "
                "pārbaudīt",
    merkis="Aprēķināt spriegumus un strāvas shēmas posmos un sasaistīt "
           "rezultātu ar shēmu.",
    protu=["noteikt, kur shēmā spriegums sadalās;",
           "noteikt, kur sadalās strāva;",
           "paredzēt mēraparāta rādījumu;",
           "pārbaudīt rezultātu ar summu."],
    atkartojums="Iepriekšējā stundā atradām kopējo pretestību. Tagad "
                "iesim otrā virzienā - no kopējiem lielumiem atpakaļ uz "
                "katru shēmas posmu.",
    uzdevumu_apraksts="Rādījumu paredzēšana",
    teorija=[
        ("Kā sadalās lielumi", [
            ("divi",
             ("VIRKNĒ", BLUE,
              ["I visur VIENĀDA.",
               "U sadalās proporcionāli R.",
               "Lielāka R - lielāks U.",
               "U₁ + U₂ = U.",
               "Tā darbojas sprieguma",
               "dalītājs."]),
             ("PARALĒLI", GREEN,
              ["U visur VIENĀDS.",
               "I sadalās apgriezti R.",
               "Mazāka R - lielāka I.",
               "I₁ + I₂ = I.",
               "Tā strādā mājas",
               "instalācija."])),
            ("panelis", "SPRIEGUMA DALĪTĀJS",
             ["Divos virknē slēgtos rezistoros spriegumi attiecas tāpat "
              "kā pretestības: uz divreiz lielākas pretestības ir "
              "divreiz lielāks spriegums.",
              "Šo principu izmanto skaļuma regulatoros, sensoru shēmās un "
              "mērierīcēs.",
              "Pārbaude vienmēr ir viena: visu spriegumu summai jābūt "
              "vienādai ar avota spriegumu."], NAVY),
        ]),
        ("Ko rādīs mēraparāts", [
            ("tabula",
             ["Kur pieslēgts", "Ko rāda", "Kā pārbaudīt"],
             [["Ampērmetrs virknē", "Visas ķēdes strāvu", "I = U/R"],
              ["Ampērmetrs zarā", "Tikai tā zara strāvu", "I₁ + I₂ = I"],
              ["Voltmetrs uz R₁", "Spriegumu uz R₁", "U = IR₁"],
              ["Voltmetrs uz avota", "Avota spriegumu", "U₁ + U₂ = U"]],
             [3.60, 3.40, 3.23]),
            ("panelis", "PAREDZI, TAD MĒRI",
             ["Pirms ieslēgšanas vienmēr aprēķini gaidāmo rādījumu - tā "
              "uzreiz pamanīsi shēmas kļūdu.",
              "Ja rādījums atšķiras vairāk nekā par dažiem procentiem, "
              "meklē kļūdu shēmā, nevis pieņem, ka «tā jau ir».",
              "Šī prasme ir tieši tā, ko vērtē PD5 un laboratorijas "
              "darbā."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Sprieguma dalītājs",
             teksts="Virknē slēgti 100 Ω un 200 Ω, pieslēgti 12 V.\n"
                    "Aprēķini spriegumu uz katra rezistora!",
             dots=["R₁ = 100 Ω", "R₂ = 200 Ω", "U = 12 V"],
             jaaprekina=["U₁ = ?", "U₂ = ?"],
             formulas=["R = R₁ + R₂", "I = U/R", "U = IR"],
             aprekins=["1)  R = 300 Ω;  I = 12 : 300 = 0,040 A",
                       "2)  U₁ = 0,040 · 100 = 4,0 V",
                       "3)  U₂ = 0,040 · 200 = 8,0 V"],
             atbilde="U₁ = 4,0 V;  U₂ = 8,0 V",
             piezime="Pretestības attiecas 1 : 2, un tieši tāpat "
                     "attiecas spriegumi."),
        dict(nr=2, virsraksts="Strāvu sadalījums",
             teksts="Paralēli slēgti 12 Ω un 24 Ω, spriegums 24 V.\n"
                    "Aprēķini strāvu katrā zarā un kopējo strāvu!",
             dots=["R₁ = 12 Ω", "R₂ = 24 Ω", "U = 24 V"],
             jaaprekina=["I₁ = ?", "I₂ = ?", "I = ?"],
             formulas=["I = U/R", "I = I₁ + I₂"],
             aprekins=["1)  I₁ = 24 : 12 = 2,0 A",
                       "2)  I₂ = 24 : 24 = 1,0 A",
                       "3)  I = 2,0 + 1,0 = 3,0 A"],
             atbilde="I₁ = 2,0 A;  I₂ = 1,0 A;  I = 3,0 A",
             piezime="Mazākajā pretestībā ir lielākā strāva - tieši "
                     "otrādi nekā spriegumam virknē."),
        dict(nr=3, virsraksts="Ampērmetra rādījums",
             teksts="Jauktā ķēdē kopējā strāva ir 1,2 A, un paralēlajā\n"
                    "posmā ir 20 Ω un 30 Ω. Ko rādīs ampērmetrs, kas\n"
                    "pieslēgts 20 Ω zarā? (U(posmā) = 14,4 V)",
             dots=["U₁₂ = 14,4 V", "R₁ = 20 Ω", "I = 1,2 A"],
             jaaprekina=["I₁ = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  I₁ = 14,4 : 20 = 0,72 A",
                       "2)  I₂ = 14,4 : 30 = 0,48 A",
                       "3)  Pārbaude: 0,72 + 0,48 = 1,2 A"],
             atbilde="I₁ = 0,72 A",
             piezime="Summas pārbaude apstiprina, ka abi zari aprēķināti "
                     "pareizi."),
        dict(nr=4, virsraksts="Voltmetra rādījums",
             teksts="Virknē slēgti 47 Ω un 100 Ω, avots 9,0 V.\n"
                    "Ko rādīs voltmetrs, pieslēgts paralēli 100 Ω\n"
                    "rezistoram?",
             dots=["R₁ = 47 Ω", "R₂ = 100 Ω", "U = 9,0 V"],
             jaaprekina=["U₂ = ?"],
             formulas=["R = R₁ + R₂", "I = U/R", "U₂ = IR₂"],
             aprekins=["1)  R = 147 Ω;  I = 9,0 : 147 ≈ 0,061 A",
                       "2)  U₂ = 0,061 · 100 ≈ 6,1 V",
                       "3)  Pārbaude: U₁ ≈ 2,9 V;  2,9 + 6,1 = 9,0 V"],
             atbilde="U₂ ≈ 6,1 V",
             piezime="Lielākā pretestība saņem lielāko sprieguma daļu - "
                     "tā ir ātrā ticamības pārbaude."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Virknē sadalās spriegums, paralēli - strāva.",
            "Virknē lielākā pretestība saņem lielāko spriegumu.",
            "Paralēli mazākajā pretestībā plūst lielākā strāva.",
            "Pārbaude: spriegumu vai strāvu summai jāsakrīt ar kopējo.",
        ],
        majasdarbs=[
            "Virknē 50 Ω un 150 Ω pie 20 V. Aprēķini U₁ un U₂.",
            "Paralēli 10 Ω un 40 Ω pie 12 V. Aprēķini I₁, I₂ un I.",
            "Uzzīmē shēmu un atzīmē, kur pieslēgtu abus mēraparātus.",
        ],
        pasvertejums=["Zinu, kā sadalās U un I",
                      "Protu rēķināt posmu spriegumus",
                      "Protu rēķināt zaru strāvas",
                      "Protu paredzēt rādījumu"],
        nakama="Nākamā stunda: elektroenerģijas patēriņa uzdevumi."),
),

dict(
    nr="10.13", virsraksts="Elektroenerģijas patēriņa uzdevumi",
    jautajums="Kā no ierīču datiem aprēķināt patēriņu un izmaksas?",
    apaksraksts="P = UI · E = Pt · kWh un tarifs · Salīdzināšana",
    merkis="Lietot P = UI un E = Pt vairāku ierīču situācijā un pamatot "
           "energoefektīvāku izvēli.",
    protu=["nolasīt ierīces datus no plāksnītes;",
           "aprēķināt vairāku ierīču patēriņu;",
           "aprēķināt izmaksas pēc tarifa;",
           "salīdzināt divus risinājumus ar skaitļiem."],
    atkartojums="10.7. stundā apguvām jaudu un kilovatstundas. Šodien to "
                "lietosim reālās sadzīves situācijās, kur ierīču ir "
                "vairākas.",
    uzdevumu_apraksts="Mājsaimniecības patēriņa aprēķini",
    teorija=[
        ("Kā rēķina patēriņu", [
            ("panelis", "SOĻI KATRAI IERĪCEI",
             ["1. Nolasi jaudu vatos un pārrēķini kilovatos: 2000 W = "
              "2,0 kW.",
              "2. Nosaki darbības laiku stundās - tieši šis solis biežāk "
              "izraisa kļūdas.",
              "3. E = P · t dod kilovatstundas; vairākām ierīcēm "
              "rezultātus saskaita.",
              "4. Izmaksas = kopējais patēriņš reiz tarifs."], NAVY),
            ("tabula",
             ["Ierīce", "Jauda", "Laiks dienā", "E dienā"],
             [["LED apgaismojums", "0,05 kW", "5 h", "0,25 kWh"],
              ["Ledusskapis", "0,10 kW", "24 h", "2,40 kWh"],
              ["Tējkanna", "2,00 kW", "0,25 h", "0,50 kWh"],
              ["Dators", "0,15 kW", "4 h", "0,60 kWh"]],
             [3.40, 2.60, 2.80, 3.43]),
        ]),
        ("Kā salīdzināt risinājumus", [
            ("divi",
             ("KVĒLSPULDZE", RED,
              ["Jauda 60 W.",
               "5 h dienā - 0,30 kWh.",
               "Gadā ≈ 110 kWh.",
               "Kalpo apmēram 1000 h."]),
             ("LED SPULDZE", GREEN,
              ["Jauda 8 W pie tāda paša",
               "gaismas daudzuma.",
               "5 h dienā - 0,04 kWh.",
               "Gadā ≈ 15 kWh.",
               "Kalpo 25 000 h."])),
            ("panelis", "ATMAKSĀŠANĀS",
             ["Ietaupījums gadā = patēriņa starpība reiz tarifs.",
              "Atmaksāšanās laiks = ierīces cena dalīta ar ietaupījumu "
              "gadā.",
              "Pamatojumā vienmēr jābūt skaitlim: «LED atmaksājas "
              "septiņos mēnešos» ir arguments, «LED ir labāks» - nav."],
             GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Vienas ierīces patēriņš",
             teksts="Ledusskapja vidējā jauda ir 100 W, tas strādā\n"
                    "visu diennakti. Cik kilovatstundu tas patērē\n"
                    "mēnesī (30 dienās)?",
             dots=["P = 100 W = 0,10 kW", "t = 24 h", "30 dienas"],
             jaaprekina=["E = ?"],
             formulas=["E = Pt"],
             aprekins=["1)  Dienā: 0,10 · 24 = 2,4 kWh",
                       "2)  Mēnesī: 2,4 · 30",
                       "3)  E = 72 kWh"],
             atbilde="E = 72 kWh",
             piezime="Ledusskapis patērē daudz nevis lielās jaudas, bet "
                     "nepārtrauktā darba dēļ."),
        dict(nr=2, virsraksts="Vairākas ierīces",
             teksts="Dienā: apgaismojums 0,25 kWh, ledusskapis 2,4 kWh,\n"
                    "tējkanna 0,50 kWh, dators 0,60 kWh.\n"
                    "Aprēķini patēriņu un izmaksas mēnesī (0,20 EUR/kWh)!",
             dots=["Kopā dienā: 0,25 + 2,4 + 0,5 + 0,6",
                   "30 dienas", "Tarifs 0,20 EUR/kWh"],
             jaaprekina=["E = ?", "Cena = ?"],
             formulas=["E = ΣE(dienā) · 30", "Cena = E · tarifs"],
             aprekins=["1)  Dienā: 3,75 kWh",
                       "2)  Mēnesī: 3,75 · 30 = 112,5 kWh",
                       "3)  Cena = 112,5 · 0,20 = 22,50 EUR"],
             atbilde="E = 112,5 kWh;  22,50 EUR",
             piezime="Vispirms saskaita dienas patēriņu, tikai tad "
                     "reizina - tā ir mazāk kļūdu."),
        dict(nr=3, virsraksts="Spuldžu salīdzinājums",
             teksts="Kvēlspuldze 60 W un LED 8 W deg 5 h dienā.\n"
                    "Cik kilovatstundu un eiro gadā ietaupa LED?\n"
                    "(365 dienas; 0,20 EUR/kWh)",
             dots=["P₁ = 0,060 kW", "P₂ = 0,008 kW", "t = 5 h",
                   "365 dienas"],
             jaaprekina=["ΔE = ?", "Ietaupījums = ?"],
             formulas=["E = Pt", "ΔE = E₁ − E₂"],
             aprekins=["1)  E₁ = 0,060 · 5 · 365 = 109,5 kWh",
                       "2)  E₂ = 0,008 · 5 · 365 = 14,6 kWh",
                       "3)  ΔE = 94,9 kWh ≈ 19 EUR gadā"],
             atbilde="ΔE ≈ 95 kWh;  ≈ 19 EUR gadā",
             piezime="Vienai spuldzei - 19 eiro; desmit spuldzēm mājā "
                     "jau 190 eiro gadā."),
        dict(nr=4, virsraksts="Atmaksāšanās laiks",
             teksts="LED spuldze maksā 6,00 EUR un gadā ietaupa\n"
                    "19,00 EUR. Pēc cik mēnešiem tā atmaksājas?",
             dots=["Cena = 6,00 EUR", "Ietaupījums = 19,00 EUR gadā"],
             jaaprekina=["Laiks = ?"],
             formulas=["t = cena/ietaupījums gadā"],
             aprekins=["1)  6,00 : 19,00 ≈ 0,32 gada",
                       "2)  0,32 · 12 ≈ 3,8 mēneši",
                       "3)  Atmaksājas mazāk nekā 4 mēnešos"],
             atbilde="Apmēram 4 mēneši",
             piezime="Atmaksāšanās laiks ir tieši tas skaitlis, ar ko "
                     "pamato izvēli."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "E = Pt; jaudu izsaka kilovatos, laiku stundās.",
            "Vairākām ierīcēm patēriņus saskaita.",
            "Izmaksas = kilovatstundas reiz tarifs.",
            "Izvēli pamato ar ietaupījumu un atmaksāšanās laiku.",
        ],
        majasdarbs=[
            "Boileris 2,0 kW strādā 3 h dienā. Aprēķini E mēnesī.",
            "Aprēķini savas mājas mēneša patēriņu piecām ierīcēm.",
            "Atrodi vienu ierīci, kuru nomainot, ietaupījums būtu "
            "lielākais.",
        ],
        pasvertejums=["Protu nolasīt ierīces datus",
                      "Protu rēķināt patēriņu",
                      "Protu rēķināt izmaksas",
                      "Protu pamatot izvēli"],
        nakama="Nākamā stunda: datu un shēmu nostiprināšana."),
),

dict(
    nr="10.14", virsraksts="Datu un shēmu nostiprināšana",
    jautajums="Kā pamanīt kļūdu shēmā vai aprēķinā?",
    apaksraksts="Datu lasīšana · Shēmas pārbaude · Vienību kontrole",
    merkis="Lasīt mērījumu datus un shēmas, atrast kļūdaini izvēlētu "
           "sakarību un pārbaudīt risinājuma ticamību.",
    protu=["pārbaudīt, vai dati atbilst Oma likumam;",
           "atrast kļūdu shēmā;",
           "atrast kļūdu aprēķinā;",
           "pārbaudīt mērvienības un ticamību."],
    atkartojums="Visas temata sakarības jau apgūtas. Šodien mācīsimies "
                "tās izmantot pretējā virzienā - lai pamanītu, kad kaut "
                "kas nav pareizi.",
    uzdevumu_apraksts="Kļūdu meklēšana datos un shēmās",
    teorija=[
        ("Kā pārbaudīt datus", [
            ("tabula",
             ["U (V)", "I (A)", "R = U/I", "Vērtējums"],
             [["2,0", "0,10", "20 Ω", "Atbilst"],
              ["4,0", "0,20", "20 Ω", "Atbilst"],
              ["6,0", "0,45", "13 Ω", "Aizdomīgs punkts"],
              ["8,0", "0,40", "20 Ω", "Atbilst"]],
             [2.20, 2.20, 2.40, 5.43]),
            ("panelis", "KO DARĪT AR IZLECOŠU PUNKTU",
             ["Vispirms pārrēķini - visbiežāk tā ir pierakstīšanas "
              "kļūda, nevis fizikas efekts.",
              "Ja iespējams, mērījumu atkārto; ja ne, punktu atzīmē kā "
              "aizdomīgu un tam neuzticas.",
              "Nekad neizmet datus tikai tāpēc, ka tie neiederas - to "
              "vienmēr pamato un pieraksta protokolā."], RED),
        ]),
        ("Biežākās kļūdas", [
            ("divi",
             ("SHĒMĀ", RED,
              ["Ampērmetrs paralēli.",
               "Voltmetrs virknē.",
               "Aizmirsts slēdzis.",
               "Sajaukts virknes un",
               "paralēlais slēgums."]),
             ("APRĒĶINĀ", GOLD,
              ["mA neatstāj ampēros.",
               "kΩ nepārrēķina omos.",
               "Minūtes nepārvērš sekundēs.",
               "Paralēlajā slēgumā",
               "pretestības saskaitītas."])),
            ("panelis", "TRĪS ĀTRĀS PĀRBAUDES",
             ["Vai paralēlā slēguma kopējā pretestība ir mazāka par "
              "mazāko? Ja nav - kļūda.",
              "Vai visu spriegumu summa virknē ir vienāda ar avota "
              "spriegumu? Ja nav - kļūda.",
              "Vai atbildes mērvienība ir tā, ko prasa uzdevums? Ja nav - "
              "kļūda."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kurš punkts kļūdains",
             teksts="Mērījumi: (2,0 V; 0,10 A), (4,0 V; 0,20 A),\n"
                    "(6,0 V; 0,45 A), (8,0 V; 0,40 A).\n"
                    "Atrodi kļūdaino punktu un pamato!",
             dots=["Četri mērījumu punkti", "Rezistors nemainīgs"],
             jaaprekina=["Kurš punkts kļūdains?"],
             formulas=["R = U/I", "R jābūt nemainīgai"],
             aprekins=["1)  R = 20 Ω;  20 Ω;  13,3 Ω;  20 Ω",
                       "2)  Trešais punkts izlec",
                       "3)  Pareizi būtu I = 6,0 : 20 = 0,30 A"],
             atbilde="Kļūdains trešais punkts (6,0 V; 0,45 A)",
             piezime="Pretestības aprēķins katram punktam ir ātrākais "
                     "veids, kā atrast izlecošo mērījumu."),
        dict(nr=2, virsraksts="Kļūda paralēlajā slēgumā",
             teksts="Skolēns rakstīja: 20 Ω un 30 Ω paralēli dod 50 Ω.\n"
                    "Paskaidro kļūdu un aprēķini pareizi!",
             dots=["R₁ = 20 Ω", "R₂ = 30 Ω",
                   "Skolēna atbilde 50 Ω"],
             jaaprekina=["R = ?"],
             formulas=["Paralēli: R = R₁R₂/(R₁ + R₂)"],
             aprekins=["1)  Skolēns lietojis virknes formulu",
                       "2)  R = 600 : 50 = 12 Ω",
                       "3)  12 Ω < 20 Ω - pārbaude izpildās"],
             atbilde="R = 12 Ω",
             piezime="Paralēlajā slēgumā rezultāts nekad nevar būt "
                     "lielāks par mazāko pretestību."),
        dict(nr=3, virsraksts="Vienību kļūda",
             teksts="Skolēns rēķināja: I = 12 V : 2,2 kΩ = 5,5 A.\n"
                    "Atrodi kļūdu un aprēķini pareizi!",
             dots=["U = 12 V", "R = 2,2 kΩ = 2200 Ω"],
             jaaprekina=["I = ?"],
             formulas=["I = U/R"],
             aprekins=["1)  Kiloomi nav pārrēķināti omos",
                       "2)  I = 12 : 2200 ≈ 0,0055 A",
                       "3)  I ≈ 5,5 mA, nevis 5,5 A"],
             atbilde="I ≈ 5,5 mA",
             piezime="Skaitlis bija pareizs, kļūdaina bija tikai "
                     "mērvienība - tūkstoškārtīga kļūda."),
        dict(nr=4, virsraksts="Shēmas kļūda",
             teksts="Shēmā ampērmetrs pieslēgts paralēli spuldzei, bet\n"
                    "voltmetrs - virknē. Kas notiks, ieslēdzot ķēdi?",
             dots=["Ampērmetrs paralēli", "Voltmetrs virknē"],
             jaaprekina=["Kas notiks?"],
             formulas=["Ampērmetram maza pretestība",
                       "Voltmetram liela pretestība"],
             aprekins=["1)  Ampērmetrs īsslēdz spuldzi - spuldze nedeg",
                       "2)  Caur ampērmetru plūst ļoti liela strāva",
                       "3)  Voltmetrs virknē gandrīz aptur strāvu"],
             atbilde="Īsslēgums un neuzticami rādījumi",
             piezime="Tāpēc shēmu pirms ieslēgšanas vienmēr pārbauda "
                     "skolotājs."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Katram datu punktam var pārbaudīt R = U/I.",
            "Paralēlā slēguma R vienmēr ir mazāka par mazāko.",
            "Mērvienību kļūda ir biežākā kļūda aprēķinos.",
            "Nepareizi pieslēgts mēraparāts sabojā visu mērījumu.",
        ],
        majasdarbs=[
            "Pārbaudi datus: (3,0 V; 0,15 A), (6,0 V; 0,30 A), "
            "(9,0 V; 0,40 A).",
            "R₁ = 10 Ω un R₂ = 40 Ω paralēli - aprēķini un pārbaudi.",
            "Atrodi kļūdu: U = 5,0 V, R = 470 Ω, I = 10,6 A.",
        ],
        pasvertejums=["Protu pārbaudīt datus",
                      "Protu atrast kļūdu shēmā",
                      "Protu atrast kļūdu aprēķinā",
                      "Protu pārbaudīt vienības"],
        nakama="Nākamā stunda: līdzstrāvas kopsavilkums pirms PD5."),
),

dict(
    nr="10.15", virsraksts="Līdzstrāvas kopsavilkums",
    jautajums="Kā pamatot elektrības patēriņa samazināšanu?",
    apaksraksts="Visas temata sakarības · Praktiska situācija · "
                "Gatavošanās PD5",
    merkis="Izvēlēties atbilstošu sakarību praktiskā situācijā un ar "
           "aprēķinu pamatot enerģijas taupīšanas risinājumu.",
    protu=["izvēlēties pareizo sakarību no temata;",
           "risināt kombinētu uzdevumu;",
           "ar aprēķinu pamatot taupīšanas risinājumu;",
           "sagatavoties PD5."],
    atkartojums="Šī ir temata pēdējā mācību stunda. PD5 vērtēs shēmas "
                "lasīšanu, Oma likumu, jaudu, patēriņu un drošu rīcību.",
    uzdevumu_apraksts="Kombinēti uzdevumi pirms PD5",
    teorija=[
        ("Temata formulu karte", [
            ("tabula",
             ["Kad lietot", "Formula", "Ko pārbaudīt"],
             [["Lādiņš un laiks", "I = q/t", "Laiks sekundēs"],
              ["Posma aprēķins", "I = U/R", "Omi un volti"],
              ["Vada pretestība", "R = ρl/S", "Laukums kvadrātmilimetros"],
              ["Slēgumi", "R = R₁ + R₂ vai R₁R₂/(R₁ + R₂)", "Kurš slēgums"],
              ["Jauda un patēriņš", "P = UI;  E = Pt", "Kilovati un stundas"]],
             [3.20, 4.20, 3.23]),
            ("panelis", "PD5 UZBŪVE",
             ["Shēmas lasīšana: atpazīt slēgumu un mēraparātu "
              "pieslēgumu.",
              "Grafika lasīšana: no I(U) noteikt pretestību.",
              "Aprēķins: Oma likums, ekvivalentā pretestība vai jauda.",
              "Pamatojums: drošas rīcības vai taupīšanas izvēle ar "
              "skaitli."], NAVY),
        ]),
        ("Kā pamatot izvēli", [
            ("divi",
             ("VĀJŠ PAMATOJUMS", RED,
              ["«LED ir labāks.»",
               "«Tā ir ekonomiskāk.»",
               "«Visi tā dara.»",
               "Nav neviena skaitļa."]),
             ("STIPRS PAMATOJUMS", GREEN,
              ["«LED patērē 95 kWh mazāk",
               "gadā, tas ir 19 eiro;",
               "spuldze maksā 6 eiro,",
               "tātad atmaksājas",
               "4 mēnešos.»"])),
            ("panelis", "PĒDĒJAIS PADOMS PIRMS PD5",
             ["Uzraksti formulu lapu pats - rakstīšana palīdz atcerēties "
              "labāk nekā lasīšana.",
              "Izrēķini vismaz vienu uzdevumu no katra veida: Oma likums, "
              "slēgumi, jauda, patēriņš.",
              "Pārbaudes darbā vispirms izpildi tos uzdevumus, kurus "
              "proti - pārējiem paliks vairāk laika."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kombinēts uzdevums",
             teksts="Sildītāja pretestība ir 46 Ω, spriegums 230 V.\n"
                    "Aprēķini strāvu, jaudu un patēriņu 2 stundās!",
             dots=["R = 46 Ω", "U = 230 V", "t = 2 h"],
             jaaprekina=["I = ?", "P = ?", "E = ?"],
             formulas=["I = U/R", "P = UI", "E = Pt"],
             aprekins=["1)  I = 230 : 46 = 5,0 A",
                       "2)  P = 230 · 5,0 = 1150 W = 1,15 kW",
                       "3)  E = 1,15 · 2 = 2,3 kWh"],
             atbilde="I = 5,0 A;  P = 1150 W;  E = 2,3 kWh",
             piezime="Trīs soļi pēc kārtas - tieši tāds būs PD5 "
                     "galvenais aprēķina uzdevums."),
        dict(nr=2, virsraksts="Slēgums un jauda",
             teksts="Divas spuldzes ar pretestību 100 Ω katra saslēgtas\n"
                    "paralēli pie 12 V. Aprēķini kopējo pretestību,\n"
                    "strāvu un jaudu!",
             dots=["R₁ = R₂ = 100 Ω", "U = 12 V"],
             jaaprekina=["R = ?", "I = ?", "P = ?"],
             formulas=["R = R₁R₂/(R₁ + R₂)", "I = U/R", "P = UI"],
             aprekins=["1)  R = 10 000 : 200 = 50 Ω",
                       "2)  I = 12 : 50 = 0,24 A",
                       "3)  P = 12 · 0,24 = 2,88 W"],
             atbilde="R = 50 Ω;  I = 0,24 A;  P ≈ 2,9 W",
             piezime="Divas vienādas paralēli - puse pretestības un "
                     "divkārša jauda."),
        dict(nr=3, virsraksts="Vads un zudumi",
             teksts="Vara vads 50 m garš, laukums 1,5 mm², caur to plūst\n"
                    "10 A. Aprēķini vada pretestību un tajā zaudēto\n"
                    "jaudu! (ρ = 0,017 Ω·mm²/m)",
             dots=["l = 50 m", "S = 1,5 mm²", "I = 10 A", "ρ = 0,017"],
             jaaprekina=["R = ?", "P = ?"],
             formulas=["R = ρl/S", "P = I²R"],
             aprekins=["1)  R = 0,017 · 50 : 1,5 ≈ 0,57 Ω",
                       "2)  I² = 100",
                       "3)  P = 100 · 0,57 = 57 W"],
             atbilde="R ≈ 0,57 Ω;  P ≈ 57 W",
             piezime="57 vati aizsilda vadu - tāpēc lielām strāvām vajag "
                     "biezākus vadus."),
        dict(nr=4, virsraksts="Pamato ar skaitli",
             teksts="Mājā desmit 60 W kvēlspuldzes deg 4 h dienā.\n"
                    "Aprēķini gada patēriņu un cik ietaupītu, nomainot\n"
                    "tās pret 8 W LED! (365 dienas; 0,20 EUR/kWh)",
             dots=["10 spuldzes", "P₁ = 0,060 kW", "P₂ = 0,008 kW",
                   "t = 4 h dienā"],
             jaaprekina=["E₁ = ?", "Ietaupījums = ?"],
             formulas=["E = Pt · n", "Cena = E · tarifs"],
             aprekins=["1)  E₁ = 0,060 · 4 · 365 · 10 = 876 kWh",
                       "2)  E₂ = 0,008 · 4 · 365 · 10 ≈ 117 kWh",
                       "3)  ΔE ≈ 759 kWh ≈ 152 EUR gadā"],
             atbilde="Ietaupījums ≈ 759 kWh ≈ 152 EUR gadā",
             piezime="Šis skaitlis arī ir pamatojums - tieši to prasa "
                     "PD5 pēdējais uzdevums."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Temata sakarības: I = q/t, I = U/R, R = ρl/S, slēgumi, "
            "P = UI, E = Pt.",
            "Kombinētu uzdevumu risina pa soļiem.",
            "Vados zaudētā jauda P = I²R.",
            "Taupīšanas izvēli pamato ar kilovatstundām un eiro.",
        ],
        majasdarbs=[
            "Atkārto 10.1.-10.14. stundas kopsavilkumus.",
            "R = 100 Ω, U = 230 V. Aprēķini I, P un E 3 stundās.",
            "Sagatavo formulu lapu PD5.",
        ],
        pasvertejums=["Protu izvēlēties sakarību",
                      "Protu risināt kombinētus uzdevumus",
                      "Protu pamatot ar skaitli",
                      "Esmu gatavs PD5"],
        nakama="Nākamā stunda: PD5 - līdzstrāva."),
),

]
