# -*- coding: utf-8 -*-
"""14. temats "Atoms un Visums". A daļa: 14.1.-14.4. stunda."""

from fiz_common import NAVY, BLUE, GOLD, GREY, RED, GREEN     # noqa: F401

TEMATS = "14. temats. Atoms un Visums"
KICKER = "FIZIKA I · 11. KLASE · 14. TEMATS: ATOMS UN VISUMS"
KURSS = "FIZIKA I · 11. KLASE"
MAPE = "C:/aphysics/Fizika_1/14. Visums un atoms"

STUNDAS = [

dict(
    nr="14.1", virsraksts="Atoma modeļi un fotons",
    jautajums="Kāpēc atomu aprakstam vajadzīgi modeļi?",
    apaksraksts="Atoma modeļi · Fotons · Diskrēti enerģijas līmeņi",
    merkis="Salīdzināt vienkāršotus atoma modeļus un skaidrot fotona un "
           "diskrētu enerģijas līmeņu ideju.",
    protu=["nosaukt galvenos atoma modeļus;",
           "izskaidrot, kāpēc modeļus nomaina;",
           "izskaidrot, kas ir fotons;",
           "izskaidrot diskrētu enerģijas līmeņu ideju."],
    atkartojums="7. tematā vielas uzbūvi aprakstījām ar daļiņu modeli. "
                "Šodien ieskatīsimies pašā atomā - un redzēsim, ka arī "
                "tur fizika strādā ar modeļiem.",
    uzdevumu_apraksts="Modeļi, fotoni un enerģijas līmeņi",
    teorija=[
        ("Atoma modeļi", [
            ("tabula",
             ["Modelis", "Galvenā ideja", "Kāpēc nomainīts"],
             [["Dalton", "Atoms - nedalāma lodīte", "Atklāja elektronu"],
              ["Tomsons", "Elektroni vienmērīgā masā",
               "Rezerforda izmēģinājums"],
              ["Rezerfords", "Kodols un elektroni ap to",
               "Neizskaidro spektrus"],
              ["Bors", "Elektroni noteiktās orbītās",
               "Der tikai ūdeņradim"]],
             [2.90, 4.00, 3.33]),
            ("panelis", "KĀPĒC MODEĻI MAINĀS",
             ["Katrs modelis izskaidro noteiktu novērojumu loku; kad "
              "parādās jauns eksperiments, modeli papildina vai nomaina.",
              "Vecais modelis nekļūst «nepareizs» - tas paliek derīgs "
              "savā jomā, tāpat kā Ņūtona mehānika joprojām der "
              "ikdienas ātrumiem.",
              "Tieši tāpēc fizikā modeli vienmēr raksturo arī ar tā "
              "robežām."], NAVY),
        ]),
        ("Fotons un enerģijas līmeņi", [
            ("formula", "FOTONA ENERĢIJA",
             "E = hf        E = hc/λ        h = 6,63·10⁻³⁴ J·s",
             "Gaisma tiek izstarota un absorbēta porcijās - fotonos. "
             "Fotona enerģija ir atkarīga tikai no frekvences: jo "
             "augstāka frekvence, jo enerģiskāks fotons.", GOLD),
            ("divi",
             ("DISKRĒTI LĪMEŅI", BLUE,
              ["Elektronam atomā ir tikai",
               "noteiktas enerģijas.",
               "Starpvērtību nav.",
               "Kā kāpnes, nevis rampa."]),
             ("PĀREJA STARP LĪMEŅIEM", GREEN,
              ["Krītot uz zemāku līmeni,",
               "izstaro fotonu.",
               "Fotona enerģija = līmeņu",
               "starpība.",
               "Tāpēc spektrā ir līnijas."])),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Fotona enerģija",
             teksts="Aprēķini zaļās gaismas fotona enerģiju!\n"
                    "(f = 6,0·10¹⁴ Hz; h = 6,63·10⁻³⁴ J·s)",
             dots=["f = 6,0·10¹⁴ Hz", "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["E = ?"],
             formulas=["E = hf"],
             aprekins=["1)  E = 6,63·10⁻³⁴ · 6,0·10¹⁴",
                       "2)  E ≈ 3,98·10⁻¹⁹ J",
                       "3)  E ≈ 4,0·10⁻¹⁹ J"],
             atbilde="E ≈ 4,0·10⁻¹⁹ J",
             piezime="Elektronvoltos tas ir apmēram 2,5 eV - tipiska "
                     "redzamās gaismas fotona enerģija."),
        dict(nr=2, virsraksts="Enerģija no viļņa garuma",
             teksts="Aprēķini fotona enerģiju, ja λ = 500 nm!\n"
                    "(h = 6,63·10⁻³⁴ J·s; c = 3,0·10⁸ m/s)",
             dots=["λ = 5,0·10⁻⁷ m", "h = 6,63·10⁻³⁴ J·s",
                   "c = 3,0·10⁸ m/s"],
             jaaprekina=["E = ?"],
             formulas=["E = hc/λ"],
             aprekins=["1)  hc = 6,63·10⁻³⁴ · 3,0·10⁸ ≈ 1,99·10⁻²⁵",
                       "2)  E = 1,99·10⁻²⁵ : 5,0·10⁻⁷",
                       "3)  E ≈ 4,0·10⁻¹⁹ J"],
             atbilde="E ≈ 4,0·10⁻¹⁹ J",
             piezime="Tas pats rezultāts kā iepriekšējā uzdevumā - "
                     "500 nm atbilst 6·10¹⁴ hercu."),
        dict(nr=3, virsraksts="Kurš fotons enerģiskāks",
             teksts="Salīdzini rentgena (f = 10¹⁸ Hz) un radioviļņa\n"
                    "(f = 10⁸ Hz) fotonu enerģijas!\n"
                    "Cik reižu tās atšķiras?",
             dots=["f₁ = 10¹⁸ Hz", "f₂ = 10⁸ Hz"],
             jaaprekina=["Attiecība = ?"],
             formulas=["E = hf", "E₁/E₂ = f₁/f₂"],
             aprekins=["1)  E ~ f",
                       "2)  Attiecība = 10¹⁸ : 10⁸",
                       "3)  Atšķiras 10¹⁰ reižu"],
             atbilde="Rentgena fotons ir 10¹⁰ reižu enerģiskāks",
             piezime="Tieši tāpēc rentgens jonizē vielu, bet radioviļņi "
                     "- ne."),
        dict(nr=4, virsraksts="Pāreja starp līmeņiem",
             teksts="Elektrons pāriet no līmeņa ar enerģiju\n"
                    "−3,4·10⁻¹⁹ J uz līmeni −8,4·10⁻¹⁹ J.\n"
                    "Aprēķini izstarotā fotona enerģiju!",
             dots=["E₁ = −3,4·10⁻¹⁹ J", "E₂ = −8,4·10⁻¹⁹ J"],
             jaaprekina=["E(fotona) = ?"],
             formulas=["E(fotona) = E₁ − E₂"],
             aprekins=["1)  E = −3,4·10⁻¹⁹ − (−8,4·10⁻¹⁹)",
                       "2)  E = 5,0·10⁻¹⁹ J",
                       "3)  Enerģija izstarota kā viens fotons"],
             atbilde="E = 5,0·10⁻¹⁹ J",
             piezime="Tieši šī līmeņu starpība nosaka spektra līnijas "
                     "krāsu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Atoma modeļi mainījās līdz ar jauniem eksperimentiem.",
            "Modelis vienmēr der tikai noteiktā jomā.",
            "Gaisma tiek izstarota porcijās - fotonos; E = hf.",
            "Elektroniem atomā ir tikai noteiktas enerģijas vērtības.",
        ],
        majasdarbs=[
            "f = 4,3·10¹⁴ Hz. Aprēķini fotona enerģiju.",
            "λ = 400 nm. Aprēķini fotona enerģiju.",
            "Uzraksti, kāpēc Bora modelis nomainīja Rezerforda modeli.",
        ],
        pasvertejums=["Zinu galvenos atoma modeļus",
                      "Saprotu, kāpēc modeļi mainās",
                      "Zinu, kas ir fotons",
                      "Protu lietot E = hf"],
        nakama="Nākamā stunda: gaismas spektri."),
),

dict(
    nr="14.2", virsraksts="Gaismas spektri",
    jautajums="Ko gaisma pastāsta par vielu un zvaigznēm?",
    apaksraksts="Nepārtraukts un līniju spektrs · E = hf · Spektru "
                "lietojumi",
    merkis="Atšķirt nepārtrauktu un līniju spektru un skaidrot spektru "
           "lietojumus.",
    protu=["atšķirt spektru veidus;",
           "izskaidrot, kā rodas līniju spektrs;",
           "lietot E = hf spektra līnijai;",
           "nosaukt, ko spektri pastāsta par zvaigznēm."],
    atkartojums="Iepriekšējā stundā noskaidrojām, ka elektronam ir "
                "diskrēti enerģijas līmeņi. Tieši tie izskaidro, kāpēc "
                "katrai vielai ir savs spektrs.",
    uzdevumu_apraksts="Spektri un fotonu enerģijas",
    teorija=[
        ("Spektru veidi", [
            ("kartitas", [
                ("NEPĀRTRAUKTS", GOLD,
                 ["Visas krāsas bez",
                  "pārtraukumiem.",
                  "Izstaro karsti cieti",
                  "ķermeņi un šķidrumi.",
                  "Piemērs: kvēldiegs."]),
                ("LĪNIJU", BLUE,
                 ["Atsevišķas spilgtas",
                  "līnijas.",
                  "Izstaro retinātas gāzes.",
                  "Katrai vielai savas.",
                  "Piemērs: neona lampa."]),
                ("ABSORBCIJAS", GREEN,
                 ["Tumšas līnijas uz",
                  "nepārtraukta fona.",
                  "Gāze absorbē savas",
                  "līnijas.",
                  "Piemērs: Saules spektrs."]),
            ]),
            ("panelis", "KĀPĒC KATRAI VIELAI SAVS SPEKTRS",
             ["Katram elementam ir sava enerģijas līmeņu sistēma, tāpēc "
              "arī līmeņu starpības - un fotonu enerģijas - ir "
              "unikālas.",
              "Spektrs kalpo kā vielas «pirkstu nospiedums»: pēc līnijām "
              "var noteikt, kāda viela izstaro vai absorbē gaismu.",
              "Tieši absorbcijas līnijas Saules spektrā atklāja hēliju - "
              "vispirms uz Saules, tikai pēc tam uz Zemes."], NAVY),
        ]),
        ("Ko spektri pastāsta", [
            ("tabula",
             ["Novērojums", "Ko no tā secina", "Kur izmanto"],
             [["Kuras līnijas ir", "Vielas sastāvs", "Zvaigžņu ķīmija"],
              ["Līniju spilgtums", "Vielas daudzums", "Analīze rūpniecībā"],
              ["Nepārtrauktā fona krāsa", "Virsmas temperatūra",
               "Zvaigžņu klasifikācija"],
              ["Līniju nobīde", "Kustība pret novērotāju",
               "Galaktiku ātrumi"]],
             [3.40, 3.20, 3.63]),
            ("panelis", "SPEKTROSKOPIJA PRAKSĒ",
             ["Zvaigznes sastāvu nosaka, salīdzinot tās spektra līnijas "
              "ar laboratorijā izmērītajām.",
              "Tas ir vienīgais veids, kā uzzināt, no kā sastāv objekti, "
              "kurus nekad nevarēsim aizsniegt.",
              "To pašu metodi lieto rūpniecībā - metālu sastāva "
              "kontrolei un pārtikas analīzei."], GOLD),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Līnijas fotona enerģija",
             teksts="Nātrija spektra dzeltenā līnija ir λ = 589 nm.\n"
                    "Aprēķini fotona enerģiju!\n"
                    "(h = 6,63·10⁻³⁴ J·s; c = 3,0·10⁸ m/s)",
             dots=["λ = 5,89·10⁻⁷ m", "h = 6,63·10⁻³⁴ J·s",
                   "c = 3,0·10⁸ m/s"],
             jaaprekina=["E = ?"],
             formulas=["E = hc/λ"],
             aprekins=["1)  hc ≈ 1,99·10⁻²⁵",
                       "2)  E = 1,99·10⁻²⁵ : 5,89·10⁻⁷",
                       "3)  E ≈ 3,4·10⁻¹⁹ J"],
             atbilde="E ≈ 3,4·10⁻¹⁹ J",
             piezime="Šo līniju var redzēt, ievietojot liesmā mazliet "
                     "galda sāls."),
        dict(nr=2, virsraksts="Frekvence no enerģijas",
             teksts="Spektra līnijas fotona enerģija ir 3,0·10⁻¹⁹ J.\n"
                    "Aprēķini frekvenci! (h = 6,63·10⁻³⁴ J·s)",
             dots=["E = 3,0·10⁻¹⁹ J", "h = 6,63·10⁻³⁴ J·s"],
             jaaprekina=["f = ?"],
             formulas=["E = hf", "f = E/h"],
             aprekins=["1)  f = 3,0·10⁻¹⁹ : 6,63·10⁻³⁴",
                       "2)  f ≈ 4,5·10¹⁴ Hz",
                       "3)  Tas ir sarkanās gaismas diapazons"],
             atbilde="f ≈ 4,5·10¹⁴ Hz",
             piezime="Pārbaude: redzamajai gaismai frekvence ir "
                     "4-7·10¹⁴ Hz - iekļaujas."),
        dict(nr=3, virsraksts="Kurš spektrs",
             teksts="Nosaki spektra veidu: a) kvēlspuldze; b) neona\n"
                    "reklāma; c) Saules gaisma ar tumšām līnijām!",
             dots=["a) karsts kvēldiegs", "b) retināta gāze",
                   "c) gaisma caur atmosfēru"],
             jaaprekina=["Spektra veids = ?"],
             formulas=["Cietvielas - nepārtraukts",
                       "Gāzes - līniju",
                       "Gaisma caur gāzi - absorbcijas"],
             aprekins=["1)  a) nepārtraukts spektrs",
                       "2)  b) līniju spektrs",
                       "3)  c) absorbcijas spektrs"],
             atbilde="a) nepārtraukts; b) līniju; c) absorbcijas",
             piezime="Spektra veids uzreiz pasaka, kādā stāvoklī ir "
                     "izstarojošā viela."),
        dict(nr=4, virsraksts="Vielas noteikšana",
             teksts="Zvaigznes spektrā ir līnijas ar tādiem pašiem viļņu\n"
                    "garumiem kā ūdeņradim laboratorijā.\n"
                    "Ko no tā var secināt un ko nevar?",
             dots=["Līnijas sakrīt ar ūdeņraža līnijām"],
             jaaprekina=["Ko secina?"],
             formulas=["Katrai vielai savas līnijas"],
             aprekins=["1)  Zvaigznes atmosfērā ir ūdeņradis",
                       "2)  Par citu elementu daudzumu tas neko nesaka",
                       "3)  Par zvaigznes vecumu tas tieši neliecina"],
             atbilde="Var secināt tikai ūdeņraža klātbūtni",
             piezime="Svarīga prasme: nošķirt to, ko dati rāda, no tā, "
                     "ko mēs pieņemam."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Nepārtrauktu spektru dod karstas cietvielas, līniju - gāzes.",
            "Absorbcijas spektrā ir tumšas līnijas uz nepārtraukta fona.",
            "Katrai vielai ir savs spektrs - tās «pirkstu nospiedums».",
            "Fotona enerģija E = hf jeb E = hc/λ.",
        ],
        majasdarbs=[
            "λ = 656 nm (ūdeņraža līnija). Aprēķini fotona enerģiju.",
            "E = 4,5·10⁻¹⁹ J. Aprēķini frekvenci.",
            "Nosauc, ko var uzzināt par zvaigzni no tās spektra.",
        ],
        pasvertejums=["Atšķiru spektru veidus",
                      "Zinu, kāpēc līnijas ir unikālas",
                      "Protu rēķināt fotona enerģiju",
                      "Zinu spektru lietojumus"],
        nakama="Nākamā stunda: kodols un izotopi."),
),

dict(
    nr="14.3", virsraksts="Kodols un izotopi",
    jautajums="Ar ko atšķiras viena elementa izotopi?",
    apaksraksts="A = Z + N · Apzīmējums · Izotopu lietojumi",
    merkis="Noteikt protonu un neitronu skaitu pēc apzīmējuma un skaidrot "
           "izotopa jēdzienu.",
    protu=["nosaukt kodola sastāvdaļas;",
           "lasīt kodola apzīmējumu;",
           "aprēķināt neitronu skaitu;",
           "izskaidrot, kas ir izotopi."],
    atkartojums="Iepriekšējās stundās skatījāmies uz elektroniem. Tagad "
                "ieskatīsimies kodolā - tur slēpjas gan elementa "
                "identitāte, gan kodolenerģija.",
    uzdevumu_apraksts="Kodola sastāvs un izotopi",
    teorija=[
        ("Kodola uzbūve", [
            ("formula", "MASAS UN KĀRTAS SKAITLIS",
             "A = Z + N        Z - protoni,  N - neitroni",
             "Z ir kārtas skaitlis - protonu skaits, kas nosaka "
             "elementu. A ir masas skaitlis - protonu un neitronu "
             "kopskaits. Neitrālā atomā elektronu skaits ir vienāds ar "
             "Z.", GOLD),
            ("kartitas", [
                ("PROTONS", RED,
                 ["Lādiņš pozitīvs.",
                  "Nosaka elementu.",
                  "Z - kārtas skaitlis."]),
                ("NEITRONS", GREY,
                 ["Lādiņa nav.",
                  "Nosaka izotopu.",
                  "N = A − Z."]),
                ("ELEKTRONS", BLUE,
                 ["Lādiņš negatīvs.",
                  "Ap kodolu.",
                  "Neitrālā atomā N(e) = Z."]),
            ]),
        ]),
        ("Izotopi", [
            ("tabula",
             ["Izotops", "Z", "N", "Kur sastopams"],
             [["Ūdeņradis-1", "1", "0", "Parastais ūdens"],
              ["Ūdeņradis-2", "1", "1", "Smagais ūdens"],
              ["Ogleklis-12", "6", "6", "Parastā viela"],
              ["Ogleklis-14", "6", "8", "Vecuma noteikšanai"]],
             [3.60, 1.80, 1.80, 5.03]),
            ("panelis", "KAS IR IZOTOPI",
             ["Izotopi ir viena elementa atomi ar vienādu protonu, bet "
              "dažādu neitronu skaitu.",
              "Ķīmiskās īpašības tiem ir gandrīz vienādas, jo tās nosaka "
              "elektroni; atšķiras masa un kodola stabilitāte.",
              "Nestabilie izotopi ir radioaktīvi - tieši tos izmanto "
              "medicīnā un vecuma noteikšanā."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Kodola sastāvs",
             teksts="Urāna kodolam A = 235, Z = 92.\n"
                    "Cik tajā ir protonu un neitronu?",
             dots=["A = 235", "Z = 92"],
             jaaprekina=["N = ?"],
             formulas=["A = Z + N", "N = A − Z"],
             aprekins=["1)  Protoni: Z = 92",
                       "2)  N = 235 − 92",
                       "3)  N = 143 neitroni"],
             atbilde="92 protoni, 143 neitroni",
             piezime="Tas ir urāns-235 - vienīgais dabā sastopamais "
                     "izotops, kas der kodolreaktoram."),
        dict(nr=2, virsraksts="Divi izotopi",
             teksts="Urānam-238 Z = 92. Salīdzini tā kodolu ar\n"
                    "urānu-235: kas sakrīt un kas atšķiras?",
             dots=["A₁ = 235", "A₂ = 238", "Z = 92"],
             jaaprekina=["N₁ = ?", "N₂ = ?"],
             formulas=["N = A − Z"],
             aprekins=["1)  N₁ = 235 − 92 = 143",
                       "2)  N₂ = 238 − 92 = 146",
                       "3)  Protonu skaits vienāds, neitronu atšķiras par 3"],
             atbilde="N₁ = 143;  N₂ = 146",
             piezime="Vienāds Z nozīmē vienu elementu; atšķirīgs N - "
                     "dažādus izotopus."),
        dict(nr=3, virsraksts="Elektronu skaits",
             teksts="Neitrālam nātrija atomam Z = 11, A = 23.\n"
                    "Nosaki protonu, neitronu un elektronu skaitu!",
             dots=["Z = 11", "A = 23", "Atoms neitrāls"],
             jaaprekina=["Daļiņu skaits = ?"],
             formulas=["N = A − Z", "Neitrālā atomā elektronu skaits = Z"],
             aprekins=["1)  Protoni: 11",
                       "2)  Neitroni: 23 − 11 = 12",
                       "3)  Elektroni: 11"],
             atbilde="11 protoni, 12 neitroni, 11 elektroni",
             piezime="Ja elektronu skaits atšķirtos no Z, tas būtu jons, "
                     "nevis neitrāls atoms."),
        dict(nr=4, virsraksts="Ogleklis-14",
             teksts="Oglekļa izotopam A = 14, Z = 6.\n"
                    "Cik neitronu tajā ir un ar ko tas atšķiras no\n"
                    "parastā oglekļa-12?",
             dots=["A = 14", "Z = 6", "Ogleklis-12: N = 6"],
             jaaprekina=["N = ?"],
             formulas=["N = A − Z"],
             aprekins=["1)  N = 14 − 6 = 8",
                       "2)  Ogleklim-12 ir 6 neitroni",
                       "3)  Atšķirība - divi neitroni"],
             atbilde="N = 8; par diviem neitroniem vairāk",
             piezime="Tieši šie divi papildu neitroni padara kodolu "
                     "nestabilu - un ļauj noteikt atradumu vecumu."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Kodolā ir protoni un neitroni; A = Z + N.",
            "Protonu skaits Z nosaka elementu.",
            "Izotopiem Z ir vienāds, bet N atšķiras.",
            "Nestabilie izotopi ir radioaktīvi.",
        ],
        majasdarbs=[
            "A = 40, Z = 19. Aprēķini N.",
            "A = 60, Z = 27. Nosaki protonu, neitronu un elektronu "
            "skaitu.",
            "Paskaidro, kāpēc izotopiem ir vienādas ķīmiskās īpašības.",
        ],
        pasvertejums=["Zinu kodola sastāvdaļas",
                      "Protu lasīt apzīmējumu",
                      "Protu aprēķināt neitronu skaitu",
                      "Saprotu izotopa jēdzienu"],
        nakama="Nākamā stunda: radioaktivitāte un pussabrukšana."),
),

dict(
    nr="14.4", virsraksts="Radioaktivitāte un pussabrukšana",
    jautajums="Kāpēc radioaktīva parauga aktivitāte samazinās?",
    apaksraksts="Alfa, beta un gamma · N = N₀/2ⁿ · Sabrukšanas grafiks",
    merkis="Atšķirt starojuma veidus, nolasīt sabrukšanas grafiku un "
           "aprēķināt atlikumu pēc vesela pussabrukšanas periodu skaita.",
    protu=["atšķirt alfa, beta un gamma starojumu;",
           "izskaidrot pussabrukšanas periodu;",
           "aprēķināt atlikumu pēc n periodiem;",
           "nolasīt sabrukšanas grafiku."],
    atkartojums="Iepriekšējā stundā noskaidrojām, ka daži izotopi ir "
                "nestabili. Šodien redzēsim, kā tie sabrūk un kā to "
                "apraksta ar skaitļiem.",
    uzdevumu_apraksts="Pussabrukšanas aprēķini",
    teorija=[
        ("Trīs starojuma veidi", [
            ("tabula",
             ["Starojums", "Kas tas ir", "Ko aptur"],
             [["Alfa (α)", "Hēlija kodols", "Papīra lapa, āda"],
              ["Beta (β)", "Elektrons", "Alumīnija plāksne"],
              ["Gamma (γ)", "EM starojums", "Biezs svins vai betons"],
              ["Neitronu", "Neitroni", "Ūdens, betons"]],
             [2.90, 3.60, 3.73]),
            ("formula", "PUSSABRUKŠANA",
             "N = N₀/2ⁿ        n = t/T",
             "T ir pussabrukšanas periods - laiks, kurā sabrūk puse "
             "kodolu. n ir periodu skaits. Process ir nejaušs katram "
             "kodolam, bet lielam skaitam - stingri likumsakarīgs.",
             GOLD),
        ]),
        ("Sabrukšanas gaita", [
            ("tabula",
             ["Periodu skaits n", "Atlikums", "Daļa procentos"],
             [["0", "N₀", "100 %"],
              ["1", "N₀/2", "50 %"],
              ["2", "N₀/4", "25 %"],
              ["3", "N₀/8", "12,5 %"]],
             [3.40, 3.00, 3.83]),
            ("panelis", "KO GRAFIKS RĀDA",
             ["Sabrukšanas grafiks nekad nesasniedz nulli - katrā "
              "periodā paliek puse no iepriekšējā daudzuma.",
              "Pussabrukšanas periods ir vielas īpašība: jodam-131 tas "
              "ir 8 dienas, oglekļim-14 - 5730 gadi, urānam-238 - "
              "4,5 miljardi gadu.",
              "Tieši tāpēc oglekli-14 lieto arheoloģisku atradumu "
              "datēšanai, bet jodu-131 - medicīnā."], NAVY),
        ]),
    ],
    uzdevumi=[
        dict(nr=1, virsraksts="Atlikums pēc trim periodiem",
             teksts="Paraugā sākumā ir 8,0·10²⁰ kodolu.\n"
                    "Cik to paliks pēc trim pussabrukšanas periodiem?",
             dots=["N₀ = 8,0·10²⁰", "n = 3"],
             jaaprekina=["N = ?"],
             formulas=["N = N₀/2ⁿ"],
             aprekins=["1)  2³ = 8",
                       "2)  N = 8,0·10²⁰ : 8",
                       "3)  N = 1,0·10²⁰"],
             atbilde="N = 1,0·10²⁰ kodolu",
             piezime="Palikusi astotā daļa - 12,5 % no sākotnējā "
                     "daudzuma."),
        dict(nr=2, virsraksts="Cik periodu pagājis",
             teksts="Joda-131 pussabrukšanas periods ir 8 dienas.\n"
                    "Cik periodu pagājis 24 dienās un cik vielas paliks?",
             dots=["T = 8 dienas", "t = 24 dienas"],
             jaaprekina=["n = ?", "Daļa = ?"],
             formulas=["n = t/T", "N = N₀/2ⁿ"],
             aprekins=["1)  n = 24 : 8 = 3",
                       "2)  2³ = 8",
                       "3)  Paliek astotā daļa jeb 12,5 %"],
             atbilde="n = 3;  paliek 12,5 %",
             piezime="Tāpēc pēc joda terapijas pacients ir izolēts tikai "
                     "dažas dienas."),
        dict(nr=3, virsraksts="Oglekļa datēšana",
             teksts="Atradumā palikusi ceturtā daļa oglekļa-14.\n"
                    "Cik vecs ir atradums? (T = 5730 gadi)",
             dots=["Daļa = 1/4", "T = 5730 gadi"],
             jaaprekina=["t = ?"],
             formulas=["N = N₀/2ⁿ", "t = n · T"],
             aprekins=["1)  Ceturtā daļa nozīmē n = 2",
                       "2)  t = 2 · 5730",
                       "3)  t = 11 460 gadi"],
             atbilde="t ≈ 11 500 gadi",
             piezime="Metode der aptuveni līdz 50 000 gadiem - pēc tam "
                     "oglekļa-14 paliek par maz."),
        dict(nr=4, virsraksts="Kurš starojums",
             teksts="Nosaki starojuma veidu: a) aptur papīra lapa;\n"
                    "b) iziet cauri alumīnijam, bet ne svinam;\n"
                    "c) aptur alumīnija plāksne.",
             dots=["a) aptur papīrs", "b) vajag svinu",
                   "c) aptur alumīnijs"],
             jaaprekina=["Starojuma veids = ?"],
             formulas=["Alfa - vismazākā caurspiešanās spēja",
                       "Gamma - vislielākā"],
             aprekins=["1)  a) alfa starojums",
                       "2)  b) gamma starojums",
                       "3)  c) beta starojums"],
             atbilde="a) alfa; b) gamma; c) beta",
             piezime="Caurspiešanās spēja aug secībā alfa - beta - "
                     "gamma; tieši pretēji ir ar jonizācijas spēju."),
    ],
    kopsavilkums=dict(
        iemacijamies=[
            "Alfa aptur papīrs, beta - alumīnijs, gamma - svins.",
            "Pussabrukšanas periodā sabrūk puse kodolu.",
            "N = N₀/2ⁿ, kur n = t/T.",
            "Pussabrukšanas periods ir vielas īpašība.",
        ],
        majasdarbs=[
            "N₀ = 6,4·10¹⁸, n = 4. Aprēķini N.",
            "T = 5 gadi, t = 20 gadi. Cik daļas paliks?",
            "Paskaidro, kāpēc sabrukšanas grafiks nesasniedz nulli.",
        ],
        pasvertejums=["Atšķiru starojuma veidus",
                      "Saprotu pussabrukšanas periodu",
                      "Protu rēķināt atlikumu",
                      "Protu lasīt grafiku"],
        nakama="Nākamā stunda: kodolu dalīšanās un sintēze."),
),

]
