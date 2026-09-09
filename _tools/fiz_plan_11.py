# -*- coding: utf-8 -*-
"""
Fizika I, 11. klase - tematu, PD un LD plāns (temati 6.-14.).

Struktūra un stundu skaits pārņemts no Fizika_1/theme_example.pdf; datumi
pārrēķināti pēc rules_fizika.txt kalendāra (trešdiena + piektdiena).
Vienīgā satura izmaiņa: 6. tematam pievienota viena uzdevumu stunda, lai
pirmais pārbaudes darbs iekristu 16.09.2026. Līdzstrāvas tematā viena
papildu stunda rezistoru un pretestības apguvei.

100 mācību stundas, 14 vērtējumi (9 PD, 4 LD, 1 PR), svaru summa 100 %.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fiz_plani as F                                    # noqa: E402
from fiz_plani import (new_doc, kalendars, temata_tabula,  # noqa: E402
                       noslegums, para, Plans, FIZIKA, GREY)

PIEZ = "Vērtē tikai iepriekš mācīto saturu."
PIEZ_LD = ("Laboratorijas darbs trešdienas dubultstundā; protokolu iesniedz "
           "e-klasē nedēļas laikā.")

# --------------------------------------------------- 6. temats (5 stundas)
T6 = [
    ("st", "Svārstības un rezonanse",
     "Kāpēc šūpoles var iešūpot arvien augstāk?",
     "Atpazīst amplitūdu, periodu un frekvenci; ar piemēru izskaidro "
     "rezonansi. Īsa diagnostika precizē pamatskolā apgūto."),
    ("st", "Mehāniskie viļņi un skaņa",
     "Kas pārvietojas vilnī?",
     "Atšķir šķērsviļņus un garenviļņus; saista skaņas augstumu ar "
     "frekvenci un skaļumu ar svārstību amplitūdu."),
    ("st", "Viļņu raksturlielumi",
     "Kā saistīti viļņa garums, frekvence un ātrums?",
     "Nolasa vienkāršu grafiku un lieto v = λf viena vai divu soļu "
     "uzdevumā; izskaidro rezultāta nozīmi."),
    ("st", "Uzdevumi par viļņiem",
     "Kā no grafika nolasīt periodu un amplitūdu?",
     "Nolasa svārstību un viļņa grafiku; aprēķina periodu, frekvenci un "
     "viļņa garumu; pārbauda mērvienības."),
    ("PD", "PD1", "Mehāniskās svārstības un viļņi",
     "Skaidro svārstības, rezonansi un viļņu piemērus; nolasa datus un "
     "lieto vienu piemērotu sakarību.", 6, PIEZ),
]

# --------------------------------------------------- 7. temats (7 stundas)
T7 = [
    ("st", "Daļiņu modelis un temperatūra",
     "Kā temperatūra saistīta ar daļiņu kustību?",
     "Skaidro vielas daļiņu modeli; pāriet starp Celsija un Kelvina "
     "skalām; iepazīst vielas daudzuma jēgu."),
    ("st", "Difūzija un izplešanās",
     "Kāpēc smarža izplatās un tiltiem vajag spraugas?",
     "Ar daļiņu modeli skaidro difūziju un termisko izplešanos; analizē "
     "ikdienas piemērus."),
    ("st", "Šķidrumu īpašības",
     "Kāpēc ūdens veido pilienus un paceļas kapilāros?",
     "Pēc neliela demonstrējuma skaidro virsmas spraigumu, slapināšanu un "
     "kapilaritāti."),
    ("st", "Gāzes spiediens un tilpums",
     "Kāpēc saspiestu gāzi kļūst grūtāk saspiest?",
     "Skaidro spiedienu ar daļiņu kustību; no dotas tabulas vai grafika "
     "raksturo spiediena un tilpuma saistību."),
    ("st", "Gāzes temperatūra un stāvoklis",
     "Kā mainās gāzes spiediens vai tilpums, to sildot?",
     "Salīdzina izoprocesus ar sadzīves piemēriem; atpazīst p, V un T "
     "sakarības un lieto doto vienkāršoto formulu."),
    ("st", "Modeļi un vienkārši aprēķini",
     "Ko gāzes modelis palīdz paredzēt?",
     "Pēc parauga lieto pV = nRT, ja n ir dots; izvērtē mērvienības un "
     "modeļa ierobežojumus."),
    ("PD", "PD2", "Atoma un vielas uzbūve",
     "Ar daļiņu modeli skaidro vielas īpašības; lasa gāzes procesa "
     "grafiku un veic vienkāršu aprēķinu.", 6, PIEZ),
]

# -------------------------------------------------- 8. temats (12 stundas)
T8 = [
    ("st", "Iekšējā enerģija un siltuma pārnese",
     "Kāpēc siltināšana samazina enerģijas zudumus?",
     "Atšķir temperatūru no enerģijas; salīdzina siltumvadīšanu, "
     "konvekciju un starojumu mājoklī."),
    ("st", "Siltuma daudzums",
     "No kā atkarīga ūdens uzsildīšanai vajadzīgā enerģija?",
     "Lieto Q = cmΔT vienkāršā situācijā un izskaidro katra lieluma "
     "nozīmi."),
    ("st", "Agregātstāvokļa maiņa",
     "Kāpēc kušanas laikā temperatūra var nemainīties?",
     "Nolasa sildīšanas grafiku; skaidro kušanu, iztvaikošanu un "
     "kondensāciju; pēc parauga lieto Q = λm vai Q = Lm."),
    ("st", "Siltuma bilance un pētījuma plāns",
     "Kā godīgi salīdzināt siltumizolāciju?",
     "Ar enerģijas nezūdamību pamato vienkāršu siltuma bilanci; formulē "
     "pētāmo jautājumu, izvēlas mainīgos un sagatavo datu tabulu."),
    ("LD", "LD1", "Siltuma māja",
     "Siltuma māja: siltumizolācijas pētīšana",
     "Grupā veic salīdzināmus temperatūras un laika mērījumus; "
     "sistemātiski reģistrē datus un dokumentē apstākļus.", 9,
     "Mērījumi trešdienas dubultstundā pirms rudens brīvlaika; protokolu "
     "iesniedz e-klasē."),
    ("st", "Mērījumu datu sakārtošana",
     "Kā mērījumi kļūst par pamatotu secinājumu?",
     "Izveido temperatūras-laika grafiku; salīdzina modeļus, identificē "
     "neprecizitātes un sagatavo prezentācijas struktūru."),
    ("PR", "PR1", "Siltuma māja",
     "Siltuma mājas rezultātu prezentācija",
     "Īsi izskaidro jautājumu, metodi, grafiku un secinājumus; "
     "individuāli atbild uz jautājumiem.", 4,
     "Īsas prezentācijas pirmajā stundā pēc rudens brīvlaika."),
    ("st", "Pirmais termodinamikas likums",
     "Kā siltums un darbs maina iekšējo enerģiju?",
     "Ar vienkāršu piemēru skaidro pirmo termodinamikas likumu; aprēķina "
     "gāzes darbu pie nemainīga spiediena."),
    ("st", "Siltuma dzinēji un energoefektivitāte",
     "Kāpēc visu siltumu nevar pārvērst lietderīgā darbā?",
     "Skaidro lietderības koeficientu un to aprēķina pēc dotajiem "
     "datiem; apspriež enerģijas taupīšanas risinājumus."),
    ("st", "Siltuma procesu nostiprināšana",
     "Kā pamatot energoefektīvu izvēli?",
     "Risina siltuma bilances uzdevumus; savieno siltuma pārnesi, "
     "siltuma daudzumu un enerģijas nezūdamību; labo biežākās kļūdas."),
    ("PD", "PD3", "Siltums un siltuma procesi",
     "Skaidro siltuma procesus, lasa grafikus un risina vienkāršus "
     "enerģijas uzdevumus; PD ir atsevišķs no projekta vērtējumiem.",
     7, PIEZ),
]

# --------------------------------------------------- 9. temats (7 stundas)
T9 = [
    ("st", "Lādiņš un elektrizācija",
     "Kāpēc apģērbs elektrizējas?",
     "Skaidro elektrizāciju un lādiņa nezūdamību; nošķir vadītājus no "
     "izolatoriem."),
    ("st", "Lādiņu mijiedarbība",
     "Kā attālums ietekmē elektrisko spēku?",
     "Nosaka pievilkšanos vai atgrūšanos; lieto Kulona likumu vienkāršam "
     "lādiņu pārim un skaidro attāluma ietekmi."),
    ("st", "Elektriskā lauka modelis",
     "Kā parādīt neredzama elektriskā lauka darbību?",
     "Lasa lauka līniju attēlu; nosaka spēka virzienu un lieto E = F/q "
     "vienkāršā piemērā."),
    ("st", "Spriegums un enerģija",
     "Ko nozīmē spriegums?",
     "Saista spriegumu ar enerģiju uz vienu lādiņa vienību; pēc parauga "
     "lieto U = A/q un E = U/d."),
    ("st", "Vadītāji un kondensatori",
     "Kur izmanto lādiņu pārdali un enerģijas uzkrāšanu?",
     "Skaidro ekranēšanu un kondensatora darbības ideju; pēc parauga "
     "izmanto C = q/U."),
    ("st", "Elektrostatika sadzīvē",
     "Kā izskaidrot zibeni un elektrostatisko aizsardzību?",
     "Izmanto lauka un lādiņa modeļus, lai pamatotu drošu rīcību; "
     "nostiprina pamataprēķinus."),
    ("PD", "PD4", "Elektriskie lādiņi un elektriskais lauks",
     "Skaidro elektrizāciju, lauku un spriegumu; analizē attēlu un veic "
     "vienkāršu aprēķinu.", 6, PIEZ),
]

# ------------------------------------------------- 10. temats (19 stundas)
T10 = [
    ("st", "Strāva, shēma un drošība",
     "Kā droši saslēgt elektrisko ķēdi?",
     "Lasa vienkāršu shēmu, atšķir strāvas stiprumu un spriegumu, "
     "izvēlas pareizu mēraparātu pieslēgumu."),
    ("st", "Oma likums un raksturlīkne",
     "Kā pretestība ietekmē strāvu?",
     "Lieto I = U/R; nolasa I(U) grafiku un nosaka pretestību."),
    ("st", "Uzdevumi: Oma likums",
     "Kā pārbaudīt aprēķina ticamību?",
     "Risina viena un divu soļu uzdevumus par strāvu, spriegumu un "
     "pretestību; pārbauda mērvienības."),
    ("st", "Vadītāja pretestība",
     "No kā atkarīga vada pretestība?",
     "Lieto R = ρl/S; skaidro īpatnējās pretestības jēgu un pamato "
     "vadītāja materiāla izvēli."),
    ("st2", "Virknes un paralēlais slēgums",
     "Kāpēc mājas ierīces slēdz paralēli?",
     "Salīdzina strāvu un spriegumu abos slēgumos; risina vienkāršu divu "
     "rezistoru uzdevumu."),
    ("st", "LD2 sagatavošana",
     "Ko un kā mērīsim elektriskajā ķēdē?",
     "Uzzīmē shēmu, nosaka lielumus un mēraparātu diapazonus; sagatavo "
     "datu tabulu."),
    ("LD", "LD2", "Laboratorijas darbs",
     "Oma likums un rezistoru slēgumi",
     "Droši saslēdz zemsprieguma ķēdi, mēra U un I; veido grafiku, "
     "salīdzina slēgumus un izvērtē rezultātu ticamību.", 8, PIEZ_LD),
    ("st", "Jauda un elektroenerģija",
     "Cik enerģijas patērē mājokļa ierīces?",
     "Lieto P = UI un E = Pt; pāriet starp enerģijas mērvienībām un pēc "
     "dotā tarifa aprēķina izmaksas."),
    ("st", "Reāls strāvas avots",
     "Kāpēc baterijas spriegums slodzē samazinās?",
     "Skaidro EDS un iekšējo pretestību; pēc parauga lieto pilnas ķēdes "
     "Oma likumu vienkāršai ķēdei."),
    ("st", "Vadītspēja dažādās vidēs",
     "Kas vada strāvu metālā, šķīdumā un pusvadītājā?",
     "Salīdzina lādiņnesējus un nosauc lietojumus; skaidro diodes "
     "darbības pamatideju."),
    ("st", "Elektrodrošība un aizsardzība",
     "Kā pasargā drošinātājs un zemējums?",
     "Skaidro pārslodzi un īsslēgumu; izvērtē drošu elektroierīču "
     "lietošanu."),
    ("st", "Ekvivalentā pretestība",
     "Kā sarežģītu shēmu sadalīt vienkāršos soļos?",
     "Pakāpeniski nosaka ekvivalento pretestību jauktā slēgumā; pamato "
     "katru pārveidošanas soli un pārbauda robežgadījumus."),
    ("st", "Sprieguma un strāvas sadalījums",
     "Kā paredzēt mēraparāta rādījumu pirms mērījuma?",
     "Izmanto Oma likumu un slēgumu īpašības, lai aprēķinātu un "
     "salīdzinātu spriegumus un strāvas; sasaista rezultātu ar shēmu."),
    ("st", "Elektroenerģijas patēriņa uzdevumi",
     "Kā no ierīču datiem aprēķināt patēriņu un izmaksas?",
     "Lieto P = UI un E = Pt vairāku ierīču sadzīves situācijā; "
     "salīdzina risinājumus un pamato energoefektīvāku izvēli."),
    ("st", "Datu un shēmu nostiprināšana",
     "Kā pamanīt kļūdu shēmā vai aprēķinā?",
     "Lasa mērījumu datus un shēmas; atrod kļūdaini izvēlētu sakarību, "
     "pārbauda vienības un risinājuma ticamību."),
    ("st", "Līdzstrāvas kopsavilkums",
     "Kā pamatot elektrības patēriņa samazināšanu?",
     "Izvēlas atbilstošu sakarību praktiskā situācijā; ar aprēķinu pamato "
     "vienu enerģijas taupīšanas risinājumu."),
    ("PD", "PD5", "Līdzstrāva",
     "Lasa shēmu un grafiku, lieto Oma likumu, aprēķina jaudu vai "
     "patēriņu un pamato drošu rīcību.", 8, PIEZ),
]

# ------------------------------------------------- 11. temats (13 stundas)
T11 = [
    ("st", "Magnēti un elektromagnēti",
     "Kā elektriskā strāva rada magnētisko lauku?",
     "Attēlo vienkāršu magnētisko lauku; pēc demonstrējuma skaidro "
     "elektromagnēta darbību."),
    ("st", "Elektromotors un spēks uz vadu",
     "Kāpēc elektromotors griežas?",
     "Ar modeli skaidro spēka iedarbību uz strāvas vadu; pēc parauga "
     "lieto F = BIl perpendikulārā laukā."),
    ("st", "Daļiņa magnētiskajā laukā",
     "Kāpēc lādētas daļiņas novirzās?",
     "Kvalitatīvi skaidro Lorenca spēku un kustības virziena maiņu; "
     "sasaista ar ziemeļblāzmas piemēru."),
    ("st", "Elektromagnētiskā indukcija",
     "Kā kustīgs magnēts var radīt strāvu?",
     "Pēc demonstrējuma skaidro magnētiskās plūsmas izmaiņas; nosaka, kas "
     "palielina inducēto spriegumu."),
    ("st", "Ģenerators un indukcijas lietojumi",
     "Kā elektrību iegūst elektrostacijā?",
     "Salīdzina motoru un ģeneratoru; skaidro enerģijas pārvērtības un "
     "indukcijas lietojumus."),
    ("st", "Maiņstrāva",
     "Ar ko maiņstrāva atšķiras no līdzstrāvas?",
     "Lasa vienkāršu maiņstrāvas grafiku; skaidro frekvenci un efektīvās "
     "vērtības jēgu."),
    ("st", "Transformators un LD3 plāns",
     "Kāpēc elektrības pārvadē maina spriegumu?",
     "Skaidro transformatora darbības nosacījumu; pēc parauga lieto "
     "vijumu un spriegumu attiecību, sagatavo mērījumus."),
    ("st", "Elektroenerģijas pārvade",
     "Kāpēc pārvadei izmanto augstu spriegumu?",
     "Ar vienkāršu modeli skaidro strāvas un siltuma zudumu saistību; "
     "analizē enerģijas pārvades ķēdi."),
    ("st", "Dati, enerģija un lietojumi",
     "Kā atšķirt motora, ģeneratora un transformatora darbību?",
     "Salīdzina ierīces un enerģijas plūsmu; labo grafiku un spriegumu "
     "attiecību uzdevumu kļūdas."),
    ("LD", "LD3", "Laboratorijas darbs",
     "Transformatora darbības pētīšana",
     "Ar drošu zemsprieguma maiņstrāvas avotu mēra spriegumus; salīdzina "
     "vijumu attiecības un pamato secinājumus.", 8, PIEZ_LD),
    ("st", "Elektromagnētisma nostiprināšana",
     "Kā izskaidrot elektromagnētisku ierīci?",
     "Ar shēmu un īsu tekstu izskaidro vienas ierīces darbību; izmanto "
     "apgūtās sakarības."),
    ("PD", "PD6", "Elektromagnētisms",
     "Skaidro magnētisma un indukcijas piemērus, lasa grafiku un lieto "
     "transformatora spriegumu attiecību.", 8, PIEZ),
]

# ------------------------------------------------- 12. temats (10 stundas)
T12 = [
    ("st", "EM viļņi un svārstību kontūrs",
     "Kā signāls pārvietojas bez vada?",
     "Skaidro mainīgu elektrisko un magnētisko lauku; atpazīst enerģijas "
     "maiņu svārstību kontūrā un lieto c = λf."),
    ("st", "EM spektrs un informācijas izvērtēšana",
     "Kas kopīgs radio, redzamajai gaismai un rentgenstarojumam?",
     "Sakārto spektra daļas, saista tās ar lietojumiem; atšķir jonizējošu "
     "un nejonizējošu starojumu."),
    ("st", "Interference un difrakcija",
     "Kāpēc viļņi pastiprina vai dzēš cits citu?",
     "Ar attēlu vai demonstrējumu skaidro superpozīciju, interferences un "
     "difrakcijas pazīmes."),
    ("st", "Difrakcijas režģis",
     "Kā režģis sadala gaismu?",
     "Skaidro režģa periodu un maksimumu kārtu; pēc parauga lieto "
     "d·sin α = kλ."),
    ("st", "LD4 sagatavošana",
     "Kā noteikt gaismas viļņa garumu?",
     "Nosaka mērāmos attālumus, izvēlas aprēķina shēmu un pārrunā lāzera "
     "drošību; sagatavo tabulu."),
    ("LD", "LD4", "Laboratorijas darbs",
     "Difrakcijas režģa pētīšana",
     "Mēra attālumus līdz ekrānam un maksimumiem; ar doto aprēķina shēmu "
     "nosaka viļņa garumu un izvērtē kļūdu avotus.", 7, PIEZ_LD),
    ("st", "Polarizācija un optiskie lietojumi",
     "Kā darbojas polarizācijas filtrs?",
     "Pēc demonstrējuma skaidro polarizācijas efektu; nosauc lietojumus "
     "brillēs un ekrānos."),
    ("st", "Datu analīze un nostiprināšana",
     "Vai izmērītais viļņa garums ir ticams?",
     "Pārbauda mērvienības un skaidro novirzes; risina uzdevumus par "
     "c = λf un d·sin α = kλ, pārbaudot kārtas skaitļa vērtības."),
    ("PD", "PD7", "Elektromagnētiskie viļņi un difrakcija",
     "Orientējas EM spektrā, skaidro difrakciju un analizē vienkāršus "
     "viļņu vai režģa datus.", 7, PIEZ),
]

# ------------------------------------------------- 13. temats (11 stundas)
T13 = [
    ("st", "Gaismas avoti un apgaismojums",
     "Kas nosaka labu darba vietas apgaismojumu?",
     "Atšķir gaismas avotu no apgaismota ķermeņa; skaidro attāluma "
     "ietekmi uz apgaismojumu un izvērtē darba vietu."),
    ("st", "Gaisma un krāsas",
     "Kāpēc priekšmetu krāsas dažādā apgaismojumā atšķiras?",
     "Skaidro gaismas krāsu, atstarošanu un absorbciju; saista ar mākslas, "
     "foto un skatuves piemēriem."),
    ("st", "Atstarošanās un spoguļi",
     "Kur rodas attēls spogulī?",
     "Zīmē staru gaitu plakanā spogulī; skaidro attēla īpašības."),
    ("st", "Gaismas laušana",
     "Kāpēc salmiņš ūdenī izskatās saliekts?",
     "Zīmē un skaidro staru gaitu uz divu vidu robežas; pēc parauga lieto "
     "laušanas likumu."),
    ("st", "Pilnīga iekšējā atstarošanās",
     "Kā optiskā šķiedra vada gaismu?",
     "Nosauc pilnīgas iekšējās atstarošanās nosacījumus un skaidro "
     "optiskās šķiedras lietojumu."),
    ("st", "Lēcas un attēli",
     "Kā lēca veido attēlu?",
     "Konstruē vienkāršu attēlu savācējlēcā; atšķir īstu un šķietamu "
     "attēlu, izmanto lēcas formulu pēc parauga."),
    ("st", "Acs, brilles un fotoaparāts",
     "Kā koriģē redzes defektus un fokusē attēlu?",
     "Ar vienkāršu modeli skaidro acs un fotoaparāta darbību; pamato "
     "savācēj- vai izkliedētājlēcas izvēli."),
    ("st", "Praktiskais darbs: attēls lēcā",
     "Kā iegūt asu attēlu uz ekrāna?",
     "Maina attālumus un iegūst asu attēlu; nosaka aptuvenu fokusa "
     "attālumu. Formatīvs darbs; mērījumus saglabā nākamajai stundai."),
    ("st", "Lēcas pētījuma datu analīze",
     "Vai staru shēma atbilst novērojumam?",
     "Pēc saglabātajiem mērījumiem aprēķina fokusa attālumu un "
     "palielinājumu; salīdzina ar staru shēmu un izvērtē kļūdas."),
    ("st", "Optikas nostiprināšana",
     "Kā izvēlēties pareizu staru shēmu?",
     "Lasa un labo staru zīmējumus; risina vienkāršu lēcas vai "
     "palielinājuma uzdevumu."),
    ("PD", "PD8", "Apgaismojums un attēli",
     "Skaidro atstarošanos un laušanu, konstruē vienkāršu attēlu un "
     "sasaista optiku ar redzi un attēlu iegūšanu.", 8, PIEZ),
]

# ------------------------------------------------- 14. temats (12 stundas)
T14 = [
    ("st", "Atoma modeļi un fotons",
     "Kāpēc atomu aprakstam vajadzīgi modeļi?",
     "Salīdzina vienkāršotus atoma modeļus; skaidro fotona un diskrētu "
     "enerģijas līmeņu ideju."),
    ("st", "Gaismas spektri",
     "Ko gaisma pastāsta par vielu un zvaigznēm?",
     "Atšķir nepārtrauktu un līniju spektru; pēc parauga lieto E = hf un "
     "skaidro spektru lietojumus."),
    ("st", "Kodols un izotopi",
     "Ar ko atšķiras viena elementa izotopi?",
     "Nosaka protonu un neitronu skaitu pēc apzīmējuma; skaidro izotopa "
     "jēdzienu."),
    ("st", "Radioaktivitāte un pussabrukšana",
     "Kāpēc radioaktīva parauga aktivitāte samazinās?",
     "Atšķir alfa, beta un gamma starojumu; nolasa sabrukšanas grafiku un "
     "aprēķina atlikumu pēc vesela pussabrukšanas periodu skaita."),
    ("st", "Dalīšanās un sintēze",
     "Kā iegūst kodolenerģiju un kā spīd Saule?",
     "Skaidro kodolu dalīšanās un sintēzes atšķirību; salīdzina "
     "ieguvumus, riskus un enerģijas izcelsmi."),
    ("st", "Starojuma lietojumi un drošība",
     "Kā izvērtēt apgalvojumu par starojuma risku?",
     "Nošķir apstarošanu un radioaktīvu piesārņojumu; pamato aizsardzību "
     "ar laiku, attālumu un ekranēšanu."),
    ("st", "Saules sistēma un novērojumi",
     "Ko varam novērot un ko secinām netieši?",
     "Orientējas Saules sistēmā; atšķir tiešu novērojumu, mērījumu un no "
     "modeļa izrietošu secinājumu."),
    ("st", "Zvaigznes un to evolūcija",
     "Kāpēc zvaigznes atšķiras un mainās?",
     "Skaidro zvaigžņu krāsas, temperatūras un evolūcijas pamatidejas; "
     "lasa vienkāršu attēlu vai datu kopu."),
    ("st", "Galaktikas un Visuma izplešanās",
     "Kādi novērojumi pamato Visuma modeļus?",
     "Raksturo Visuma struktūru; skaidro sarkanās nobīdes un izplešanās "
     "saistību, atšķir datus no interpretācijas."),
    ("st", "Kosmosa izpēte un informācijas avoti",
     "Kā izvērtēt zinātnisku ziņu par kosmosu?",
     "Atrod apgalvojuma avotu un pierādījumus; nošķir pamatotu "
     "secinājumu, nenoteiktību un spekulāciju."),
    ("st", "Atoma un Visuma kopsavilkums",
     "Kā savienot atoma un kosmosa pētījumus?",
     "Ar īsu skaidrojumu sasaista spektrus, enerģiju un astronomijas "
     "novērojumus; labo būtiskākās kļūdas."),
    ("PD", "PD9", "Atoms un Visums",
     "Skaidro atomu, kodolu un Visuma pamatidejas; lasa datus, vērtē "
     "apgalvojuma pamatojumu un veic vienkāršu aprēķinu.", 8, PIEZ),
]

# ------------------------------------------------------------------ noslēgums
NOSL = [
    ("st", "Eksāmena 1. daļa",
     "Kā ātri izvēlēties pareizo atbildi?",
     "Trenē eksāmena 1. daļas formātu: 24 izvēles jautājumi 40 minūtēs; "
     "analizē tipiskās izvēles kļūdas."),
    ("st", "Eksāmena 2. daļa: īsās atbildes",
     "Kā uzrakstīt atbildi bez risinājuma?",
     "Trenē īso atbilžu uzdevumus - mērvienības, grafika nolasīšana, "
     "jēdziena nosaukšana."),
    ("st", "Eksāmena 2. daļa: risinājumi",
     "Kā pierakstīt pilnu risinājumu?",
     "Pieraksta risinājumu latviešu standartā ar formulām, aprēķinu, "
     "mērvienībām un atbildi; vērtē pēc eksāmena kritērijiem."),
    ("st", "Gada noslēgums",
     "Kas jāatkārto pirms eksāmena?",
     "Apkopo divu gadu saturu vienā atgādnē; novērtē savu sniegumu un "
     "plāno atkārtošanu."),
]


def build(path):
    p = Plans()
    b6 = p.bloks(T6)
    b7 = p.bloks(T7)
    b8 = p.bloks(T8)
    b9 = p.bloks(T9)
    b10 = p.bloks(T10)
    b11 = p.bloks(T11)
    b12 = p.bloks(T12)
    b13 = p.bloks(T13)
    b14 = p.bloks(T14)
    bn = p.bloks(NOSL)
    p.parbaudi()

    doc = new_doc("11. klase", p.n,
                  "Fizika I pamatkurss, otrais mācību gads. Plāns aptver "
                  "programmas tematus no «Mehāniskās svārstības un viļņi» "
                  "līdz «Atoms un Visums». Mācību mērķis ir centralizētais "
                  "eksāmens fizikā optimālajā līmenī, tāpēc katrā tematā ir "
                  "uzdevumu risināšanas un datu analīzes stundas eksāmena "
                  "formātā, bet mācību gada beigās - atsevišķs gatavošanās "
                  "bloks.")

    kalendars(doc, p.vertejumi,
              "Pirmais pārbaudes darbs PD1 ir 16.09.2026. - otrajā mācību "
              "nedēļā. Siltuma mājas mērījumi notiek trešdienas "
              "dubultstundā pirms rudens brīvlaika, prezentācija - pirmajā "
              "stundā pēc brīvlaika, protokols e-klasē nedēļas laikā. "
              "Protokola iesniegšanai mācību stunda nav atvēlēta.")

    temata_tabula(doc, "6. temats. Mehāniskās svārstības un viļņi "
                       "(%d stundas)" % len(b6),
                  "Svārstību atkārtojums apvienots ar rezonansi; pievienota "
                  "viena uzdevumu stunda pirms pirmā pārbaudes darba.", b6,
                  "Svārstību vienādojuma detalizēta analīze.")
    temata_tabula(doc, "7. temats. Atoma un vielas uzbūve (%d stundas)"
                  % len(b7),
                  "Apvienota daļiņu modeļa un temperatūras apguve; mazāk "
                  "atkārtotu gāzu aprēķinu.", b7,
                  "Kombinēti daļiņu skaita un izoprocesu uzdevumi.")
    temata_tabula(doc, "8. temats. Siltums un siltuma procesi (%d stundas)"
                  % len(b8),
                  "Temata centrā ir Siltuma mājas pētījums: mērījumi (LD1, "
                  "9 %), prezentācija (PR1, 4 %) un atsevišķs temata "
                  "pārbaudes darbs (PD3, 7 %).", b8,
                  "Adiabātisku procesu aprēķini un vairāku procesu "
                  "kombinācijas.")
    temata_tabula(doc, "9. temats. Elektriskie lādiņi (%d stundas)" % len(b9),
                  "Lauka un sprieguma tēmas apgūst ar vienkāršiem "
                  "modeļiem; kondensatoram īss pārskats.", b9,
                  "Vairāku lādiņu vektoriāla superpozīcija un sarežģīti "
                  "kondensatoru uzdevumi.")
    temata_tabula(doc, "10. temats. Līdzstrāva (%d stundas)" % len(b10),
                  "Kursa apjomīgākais elektrības temats: Oma likums, "
                  "slēgumi, LD2 un elektroenerģijas patēriņš. Pievienotas "
                  "stundas shēmu analīzei un kļūdu korekcijai.", b10,
                  "Vairāku avotu ķēdes un reāla avota atsevišķs pētījums.")
    temata_tabula(doc, "11. temats. Elektromagnētisms (%d stundas)"
                  % len(b11),
                  "Uzsvērta ierīču darbība un enerģijas pārvērtības; daļiņu "
                  "kustību skaidro kvalitatīvi.", b11,
                  "Daļiņu trajektoriju aprēķini un pašindukcija.")
    temata_tabula(doc, "12. temats. Elektromagnētiskie viļņi (%d stundas)"
                  % len(b12),
                  "Svārstību kontūrs īsā pārskatā; apvienota interference "
                  "un difrakcija; saglabāts LD4.", b12,
                  "Svārstību kontūra izvērsti aprēķini un viļņu optikas "
                  "problēmuzdevumi.")
    temata_tabula(doc, "13. temats. Apgaismojums un attēli (%d stundas)"
                  % len(b13),
                  "Viens formatīvs lēcas praktiskais darbs; nav atsevišķa "
                  "lēcu sistēmu pētījuma.", b13,
                  "Vairāku lēcu sistēmas un izkliedētājlēcas aprēķini.")
    temata_tabula(doc, "14. temats. Visums un atoms (%d stundas)" % len(b14),
                  "Apvienoti atoma un kvantu ievada un radioaktivitātes "
                  "jautājumi; uzsvars uz datiem un skaidrojumiem.", b14,
                  "Izvērsti kvantu aprēķini un detalizēta kosmoloģija.")
    noslegums(doc, "Gatavošanās eksāmenam (%d stundas)" % len(bn),
              "Formatīvas stundas pēc pēdējā pārbaudes darba. Jauns "
              "summatīvs vērtējums nav paredzēts.", bn)

    para(doc, "Ja mācību gada gaitā izkrīt stundas, programmas dziļumu "
              "koriģē ar izvēles padziļinājumiem un uzdevumu apjomu; "
              "atsevišķas rezerves stundas nav paredzētas.",
         size=8.5, italic=True, color=GREY, before=8)
    doc.save(path)
    return p


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    out = os.path.join(FIZIKA,
                       "Fizika I 11. klase - tematu, PD un LD plans_tt.docx")
    p = build(out)
    print("11. klase: %d stundas, %d vertejumi -> %s"
          % (p.n, len(p.vertejumi), os.path.basename(out)))
    for m in p.mainas:
        print("  UZMANIBU: %s" % m)
    for kods, tema, svars, datums, _ in p.vertejumi:
        print("      %-5s %-48s %2d %%  %s" % (kods, tema[:48], svars, datums))
