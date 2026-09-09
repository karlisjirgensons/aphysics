# -*- coding: utf-8 -*-
"""
Fizika I, 10. klase - tematu, PD un LD plāns (temati 1.-5.).

Saturs pēc skola2030_fizika1.pdf tematiem:
  progr. 1. Vektori un kustība + 2. Vienmērīga kustība -> mape «1. Ievads
  pētniecībā. Vienmērīga un nevienmērīga kustība»
  progr. 4. Vienmērīgi paātrināta kustība   -> mape «2. ...»
  progr. 5. Mijiedarbība un spēks           -> mape «3. ...»
  progr. 6. Gravitācijas lauks un kustība   -> mape «4. ...»
  progr. 7. Enerģija un darbs               -> mape «5. ...»

100 mācību stundas, 11 vērtējumi (6 PD, 4 LD, 1 PR), svaru summa 100 %.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fiz_plani as F                                    # noqa: E402
from fiz_plani import (new_doc, kalendars, temata_tabula,  # noqa: E402
                       noslegums, para, Plans, FIZIKA, NAVY, GREY)

PIEZ = "Vērtē tikai iepriekš mācīto saturu."
PIEZ_LD = ("Laboratorijas darbs trešdienas dubultstundā; protokolu iesniedz "
           "e-klasē nedēļas laikā.")

# ------------------------------------------------------------------ 1. TEMATS
T1 = [
    ("st", "Fizika kā zinātne",
     "Kāpēc fiziķi mēra, nevis min?",
     "Nosauc fizikas pētīšanas metodes; lieto fizikālo lielumu apzīmējumus, "
     "SI pamatvienības, priedēkļus un standartformu; pārbauda rezultāta "
     "ticamību pēc mērvienībām."),
    ("st", "Skalāri un vektori",
     "Ar ko ātrums atšķiras no ceļa?",
     "Nošķir skalārus lielumus no vektoriālajiem; attēlo vektoru ar vērstu "
     "nogriezni un nosaka tā moduli izvēlētā mērogā."),
    ("st", "Darbības ar vektoriem",
     "Kā saskaita divus spēkus?",
     "Saskaita un atņem vektorus ģeometriski (trijstūra un paralelograma "
     "metode); reizina vektoru ar skaitli un pamato rezultāta virzienu."),
    ("st", "Vektora projekcijas",
     "Kā vektoru pierakstīt ar skaitļiem?",
     "Nosaka vektora projekcijas uz koordinātu asīm; aprēķina moduli pēc "
     "projekcijām un pāriet no ģeometriskās formas uz koordinātu formu."),
    ("PD", "PD1", "Vektori un fizikālie lielumi",
     "Pārvērš mērvienības, nošķir skalārus no vektoriem, saskaita vektorus "
     "un nosaka to projekcijas.", 6, PIEZ),

    ("st", "Mehāniskā kustība",
     "Kustas vai stāv - salīdzinot ar ko?",
     "Skaidro relatīvo kustību; izvēlas atskaites ķermeni un atskaites "
     "sistēmu; nosaka materiālā punkta modeļa lietojamību."),
    ("st", "Ceļš un pārvietojums",
     "Kāpēc ceļš un pārvietojums nav viens un tas pats?",
     "Atšķir ceļu no pārvietojuma; nosaka abus lielumus vienkāršā "
     "trajektorijā un pamato, kad tie sakrīt."),
    ("st", "Vienmērīga taisnvirziena kustība",
     "Ko nozīmē 20 metri sekundē?",
     "Lieto v = s/t; pārvērš m/s un km/h; risina viena un divu soļu "
     "uzdevumus par vienmērīgu kustību."),
    ("st", "Kustības vienādojums un grafiki",
     "Ko par kustību pastāsta grafiks?",
     "Pieraksta x = x₀ + vt; zīmē un nolasa x(t) un v(t) grafikus; nosaka "
     "ātrumu pēc grafika slīpuma."),
    ("st", "Grafiku lasīšana",
     "Kur satiksies divi ķermeņi?",
     "No diviem kustības vienādojumiem vai grafikiem nosaka satikšanās "
     "laiku un vietu; pārbauda atbildes fizikālo jēgu."),
    ("st", "Vidējais ātrums",
     "Kāds ir ātrums, ja tas mainās?",
     "Aprēķina vidējo ātrumu pa visu ceļu; skaidro, kāpēc vidējais ātrums "
     "nav ātrumu vidējais aritmētiskais."),
    ("st", "Mērierīces un mērījumu kļūdas",
     "Cik precīzs ir mērījums?",
     "Nosaka mērierīces iedaļas vērtību un absolūto kļūdu; pieraksta "
     "rezultātu formā a ± Δa un aprēķina relatīvo kļūdu."),
    ("st", "Pētījuma plānošana",
     "Kā pētījumu padarīt godīgu?",
     "Formulē pētāmo jautājumu un hipotēzi; nosaka atkarīgo, neatkarīgo un "
     "nemainīgos lielumus; sagatavo datu tabulu un ievēro drošību."),
    ("LD", "LD1", "Pētnieciskais darbs",
     "Lodītes vidējais ātrums uz slīpas renītes",
     "Grupā veic atkārtotus laika un ceļa mērījumus pie dažādiem renītes "
     "slīpumiem; sistemātiski reģistrē datus un novērtē mērījumu kļūdu.",
     9, PIEZ_LD),
    ("st", "Datu apstrāde un grafiks",
     "Kā no mērījumiem iegūst secinājumu?",
     "Aprēķina vidējās vērtības, veido v(α) grafiku, izvērtē datu izkliedi "
     "un formulē secinājumu, kas atbild uz pētāmo jautājumu."),
    ("PR", "PR1", "Pētnieciskais darbs",
     "Pētījuma rezultātu prezentācija",
     "Īsi izskaidro pētāmo jautājumu, metodi, grafiku un secinājumu; "
     "individuāli atbild uz jautājumiem par kļūdu avotiem.", 5,
     "Īsas grupu prezentācijas; vērtē saturu un pamatojumu."),
    ("st", "Relatīvā kustība",
     "Cik ātri iet cilvēks kustīgā vilcienā?",
     "Lieto ātrumu saskaitīšanas likumu vienā un pretējos virzienos; "
     "risina uzdevumus par laivu upē un gaisa kuģi vējā."),
    ("st", "Kustības uzdevumi",
     "Kā risināt uzdevumu par diviem ķermeņiem?",
     "Izvēlas atskaites sistēmu un pieraksta abu ķermeņu vienādojumus; "
     "atrisina vienādojumu sistēmu un pārbauda mērvienības."),
    ("st", "Grafiku un vienādojumu nostiprināšana",
     "Kā no grafika uzrakstīt vienādojumu?",
     "Pāriet no grafika uz vienādojumu un atpakaļ; atrod kļūdu dotā "
     "risinājumā un to izlabo."),
    ("st", "Kļūdas pētījumā",
     "Cik ticams ir mūsu rezultāts?",
     "Aprēķina vidējo vērtību un absolūto kļūdu; salīdzina relatīvās kļūdas "
     "un nosauc galvenos kļūdu avotus."),
    ("st", "Temata nostiprināšana",
     "Kā izvēlēties pareizo sakarību?",
     "Sakārto temata jēdzienus un sakarības; risina jauktus uzdevumus un "
     "labo biežākās kļūdas pirms pārbaudes darba."),
    ("PD", "PD2", "Vienmērīga un nevienmērīga kustība",
     "Lasa kustības grafikus, lieto v = s/t un kustības vienādojumu, "
     "aprēķina vidējo ātrumu un novērtē mērījuma kļūdu.", 10, PIEZ),
    ("st", "Kļūdu analīze",
     "Ko no pārbaudes darba mācāmies?",
     "Analizē sava darba kļūdas, izlabo risinājumus un formulē, kas "
     "jāatkārto pirms nākamā temata."),
]

# ------------------------------------------------------------------ 2. TEMATS
T2 = [
    ("st", "Paātrinājums",
     "Ko nozīmē 'no 0 līdz 100 sešās sekundēs'?",
     "Skaidro paātrinājumu kā ātruma izmaiņu laika vienībā; lieto "
     "a = (v − v₀)/t un nosaka paātrinājuma virzienu."),
    ("st", "Ātruma vienādojums un grafiks",
     "Kā mainās ātrums, ja paātrinājums ir nemainīgs?",
     "Pieraksta v = v₀ + at; zīmē un nolasa v(t) grafiku; nosaka "
     "paātrinājumu pēc grafika slīpuma."),
    ("st", "Pārvietojums paātrinātā kustībā",
     "Kāpēc laukums zem grafika ir ceļš?",
     "Aprēķina pārvietojumu kā laukumu zem v(t) grafika; lieto "
     "s = v₀t + at²/2 un s = (v² − v₀²)/(2a)."),
    ("st", "Kustības vienādojums",
     "Kur ķermenis atradīsies pēc 5 sekundēm?",
     "Pieraksta x = x₀ + v₀t + at²/2; nosaka koordinātu, ātrumu un laiku "
     "dotā kustībā."),
    ("st", "Uzdevumi par paātrinātu kustību",
     "Cik garš ir bremzēšanas ceļš?",
     "Risina uzdevumus par paātrināšanos un bremzēšanu; pamato "
     "paātrinājuma zīmi un pārbauda rezultāta ticamību."),
    ("st", "Brīvā krišana",
     "Vai smagāks ķermenis krīt ātrāk?",
     "Skaidro brīvo krišanu kā vienmērīgi paātrinātu kustību ar g; risina "
     "uzdevumus par krišanas laiku, augstumu un ātrumu."),
    ("st", "Vertikāli mests ķermenis",
     "Cik augstu uzlido bumba?",
     "Aprēķina pacelšanās augstumu un lidojuma laiku vertikāli augšup "
     "mestam ķermenim; skaidro ātrumu augstākajā punktā."),
    ("st", "Uzdevumi: krišana un mešana",
     "Cik ilgi ķermenis atrodas gaisā?",
     "Risina kombinētus uzdevumus par brīvo krišanu un vertikālu mešanu; "
     "salīdzina uzlidošanas un krišanas laiku."),
    ("LD", "LD2", "Laboratorijas darbs",
     "Brīvās krišanas paātrinājuma noteikšana",
     "Ar matemātisko svārstu vai krītošu ķermeni nosaka g; veic "
     "atkārtotus mērījumus, aprēķina vidējo vērtību un relatīvo kļūdu, "
     "salīdzina ar tabulas vērtību.", 9, PIEZ_LD),
    ("st", "Horizontāli mests ķermenis",
     "Kāpēc lodes trajektorija ir parabola?",
     "Sadala kustību horizontālā un vertikālā komponentē; aprēķina "
     "lidojuma laiku, tālumu un ātrumu krišanas brīdī."),
    ("st", "Kustība pa riņķa līniju",
     "Ar ko riņķa kustība atšķiras no taisnvirziena?",
     "Lieto periodu, frekvenci un lineāro ātrumu v = 2πR/T; pāriet starp "
     "leņķisko un lineāro ātrumu."),
    ("st", "Centrtieces paātrinājums",
     "Kāpēc kustība pa riņķi ir paātrināta?",
     "Skaidro centrtieces paātrinājuma virzienu; lieto a = v²/R un "
     "a = 4π²R/T²."),
    ("st", "Uzdevumi par riņķa kustību",
     "Cik ātri jāgriežas karuselim?",
     "Risina uzdevumus par periodu, frekvenci un centrtieces "
     "paātrinājumu; salīdzina dažādu punktu ātrumus uz rotējoša ķermeņa."),
    ("st", "Temata nostiprināšana",
     "Kuru vienādojumu izvēlēties?",
     "Salīdzina vienmērīgas un vienmērīgi paātrinātas kustības "
     "vienādojumus; risina jauktus uzdevumus un labo biežākās kļūdas."),
    ("PD", "PD3", "Vienmērīgi paātrināta kustība",
     "Lieto kustības vienādojumus, lasa v(t) grafikus, risina brīvās "
     "krišanas un riņķa kustības uzdevumus.", 10, PIEZ),
    ("st", "Kļūdu analīze un treniņš",
     "Kā izvairīties no tipiskajām kļūdām?",
     "Analizē pārbaudes darba kļūdas; trenē grafiku lasīšanu un "
     "mērvienību pārbaudi eksāmena formātā."),
]

# ------------------------------------------------------------------ 3. TEMATS
T3 = [
    ("st", "Mijiedarbība un spēks",
     "Kāpēc mainās ķermeņu ātrums?",
     "Skaidro spēku kā mijiedarbības mēru; attēlo spēkus zīmējumā, "
     "nosaka to virzienu un pielikšanas punktu."),
    ("st", "Ņūtona pirmais likums",
     "Kas notiek, ja spēku nav?",
     "Formulē inerciālas atskaites sistēmas jēdzienu; skaidro inerci ar "
     "ikdienas piemēriem."),
    ("st", "Ņūtona otrais likums",
     "Cik liels paātrinājums rodas no dotā spēka?",
     "Lieto F = ma; nosaka kopspēku un paātrinājumu; pārbauda mērvienības "
     "un rezultāta ticamību."),
    ("st", "Ņūtona trešais likums",
     "Vai zirgs velk ratus vai rati zirgu?",
     "Nosaka darbības un pretdarbības spēku pāri; skaidro, kāpēc šie spēki "
     "neizlīdzsvaro viens otru."),
    ("st", "Spēku shēmas un kopspēks",
     "Kā uzzīmēt visus spēkus?",
     "Zīmē pilnu spēku shēmu; nosaka kopspēku ģeometriski un ar "
     "projekcijām uz asīm."),
    ("st", "Smaguma spēks un svars",
     "Ar ko svars atšķiras no smaguma spēka?",
     "Nošķir smaguma spēku no ķermeņa svara; aprēķina svaru liftā, kas "
     "kustas ar paātrinājumu."),
    ("st", "Balsta reakcija",
     "Kāpēc grīda 'spiež pretī'?",
     "Nosaka balsta reakcijas spēku horizontālā un slīpā virsmā; skaidro "
     "bezsvara stāvokli."),
    ("st", "Elastības spēks. Huka likums",
     "No kā atkarīgs atsperes spēks?",
     "Lieto F = kx; skaidro stinguma koeficienta fizikālo jēgu un "
     "elastības robežu."),
    ("st", "LD3 sagatavošana",
     "Ko un kā mērīsim atsperei?",
     "Uzzīmē mērīšanas shēmu, izvēlas mēraparātus un diapazonus; "
     "sagatavo datu tabulu un pārrunā drošību."),
    ("LD", "LD3", "Laboratorijas darbs",
     "Atsperes stinguma koeficienta noteikšana",
     "Mēra atsperes pagarinājumu pie dažādām slodzēm; veido F(x) grafiku, "
     "nosaka k pēc grafika slīpuma un izvērtē kļūdu avotus.", 9, PIEZ_LD),
    ("st", "Berzes spēks",
     "Kāpēc kastes grūti pabīdīt?",
     "Atšķir miera, slīdes un rites berzi; lieto Fb = μN un skaidro berzes "
     "koeficienta jēgu."),
    ("st", "Uzdevumi par berzi",
     "Cik liels spēks jāpieliek, lai kaste kustētos?",
     "Risina uzdevumus par kustību ar berzi uz horizontālas virsmas; "
     "pieraksta Ņūtona otro likumu projekcijās."),
    ("st", "Slīpā plakne",
     "Kā spēku sadala uz slīpas virsmas?",
     "Sadala smaguma spēku komponentēs; aprēķina paātrinājumu uz slīpās "
     "plaknes ar berzi un bez tās."),
    ("st", "Uzdevumi: slīpā plakne",
     "Kad ķermenis sāk slīdēt?",
     "Nosaka slīdēšanas nosacījumu un berzes koeficientu pēc slīpuma "
     "leņķa; pārbauda robežgadījumus."),
    ("st", "Ķermeņu sistēmas",
     "Kā rēķina ar diviem saistītiem ķermeņiem?",
     "Pieraksta Ņūtona otro likumu katram sistēmas ķermenim; nosaka "
     "sastiepuma spēku auklā un risina uzdevumu par diviem ķermeņiem pār "
     "bloku."),
    ("st", "Spiediens cietās vielās",
     "Kāpēc naglai ir smails gals?",
     "Lieto p = F/S; salīdzina spiedienu dažādos laukumos un pamato "
     "praktiskus risinājumus."),
    ("st", "Spiediens šķidrumos",
     "Kāpēc dziļumā spiediens ir lielāks?",
     "Lieto p = ρgh un Paskāla likumu; skaidro hidrauliskās preses "
     "darbību."),
    ("st", "Arhimēda spēks",
     "Kāpēc kuģis peld?",
     "Lieto FA = ρgV; nosaka peldēšanas, grimšanas un nirstošas "
     "peldēšanas nosacījumus."),
    ("st", "Uzdevumi: hidrostatika",
     "Cik daudz ledus ir zem ūdens?",
     "Risina kombinētus uzdevumus par spiedienu un cēlējspēku; salīdzina "
     "blīvumus un pamato secinājumu."),
    ("st", "Deformācijas un spriegums",
     "Kad trose pārtrūks?",
     "Atšķir elastīgu un plastisku deformāciju; lieto σ = F/S un pamato "
     "drošības rezervi."),
    ("st", "Spēka moments",
     "Kā ar mazu spēku pacelt smagu kravu?",
     "Lieto M = Fd; formulē momentu līdzsvara nosacījumu un to pielieto "
     "svirai."),
    ("st", "Temata nostiprināšana",
     "Kā no situācijas nonākt līdz vienādojumam?",
     "Zīmē spēku shēmu, izvēlas asis un pieraksta vienādojumus; labo "
     "biežākās kļūdas pirms pārbaudes darba."),
    ("PD", "PD4", "Mijiedarbība un spēks",
     "Zīmē spēku shēmu, lieto Ņūtona likumus, Huka likumu un berzes "
     "sakarību; risina uzdevumus par spiedienu un cēlējspēku.", 12, PIEZ),
    ("st", "Kļūdu analīze",
     "Kuras spēku shēmas bija kļūdainas?",
     "Analizē pārbaudes darba kļūdas; izlabo spēku shēmas un pieraksta "
     "pareizos risinājumus."),
]

# ------------------------------------------------------------------ 4. TEMATS
T4 = [
    ("st", "Vispasaules gravitācijas likums",
     "Kas notur Mēnesi orbītā?",
     "Formulē un lieto F = Gm₁m₂/r²; skaidro attāluma ietekmi uz "
     "gravitācijas spēku."),
    ("st", "Gravitācijas lauks",
     "Kā aprakstīt neredzamu lauku?",
     "Lieto lauka intensitāti g = F/m; salīdzina lauka intensitāti dažādos "
     "attālumos un uz dažādām planētām."),
    ("st", "Brīvās krišanas paātrinājums",
     "Cik smagi būtu uz Marsa?",
     "Aprēķina g = GM/R² dažādām planētām; salīdzina rezultātus un "
     "izvērtē to ticamību."),
    ("st", "Uzdevumi par gravitāciju",
     "Cik reižu mainās spēks, mainot attālumu?",
     "Risina proporcionalitātes uzdevumus par gravitācijas spēku; pamato "
     "atbildi ar apgriezti kvadrātisko sakarību."),
    ("st", "Kustība gravitācijas laukā",
     "Kāpēc pavadonis nekrīt zemē?",
     "Skaidro riņķveida kustību kā brīvu krišanu; saista centrtieces "
     "paātrinājumu ar gravitācijas lauka intensitāti."),
    ("st", "Pirmais kosmiskais ātrums",
     "Cik ātri jālido, lai paliktu orbītā?",
     "Izvada un lieto v = √(GM/R); aprēķina pirmo kosmisko ātrumu Zemei "
     "un citām planētām."),
    ("st", "Mākslīgie pavadoņi",
     "Kāpēc daži pavadoņi 'karājas' virs viena punkta?",
     "Aprēķina orbītas rādiusu un periodu; skaidro ģeostacionāras orbītas "
     "nosacījumus un lietojumus."),
    ("st", "Keplera likumi",
     "Kā planētas kustas ap Sauli?",
     "Formulē Keplera likumus; lieto trešo likumu T²/a³ = const orbītas "
     "perioda vai rādiusa aprēķinam."),
    ("st", "Uzdevumi: pavadoņi un orbītas",
     "Cik ilgs ir pavadoņa apriņķojums?",
     "Risina kombinētus uzdevumus par orbītas rādiusu, ātrumu un periodu; "
     "pārbauda mērvienības un lielumu kārtu."),
    ("st", "Svars un pārslodze",
     "Kāpēc kosmonauti 'peld'?",
     "Aprēķina svaru, kustoties ar paātrinājumu; skaidro pārslodzi un "
     "bezsvara stāvokli orbītā."),
    ("st", "Gravitācijas potenciālā enerģija",
     "Cik enerģijas vajag, lai paceltu kravu?",
     "Lieto Ep = mgh tuvu Zemei; skaidro, kad šī tuvinājuma vairs nepietiek."),
    ("st", "Uzdevumi: enerģija gravitācijas laukā",
     "Cik enerģijas vajag palaišanai orbītā?",
     "Risina uzdevumus par darbu pret gravitācijas spēku; salīdzina "
     "enerģijas apjomus ar ikdienas piemēriem."),
    ("st", "Datu un grafiku analīze",
     "Ko par planētu pastāsta tās orbīta?",
     "No dotiem orbītu datiem nosaka planētas vai zvaigznes masu; izvērtē "
     "datu ticamību un mērvienības."),
    ("st", "Temata nostiprināšana",
     "Kuru sakarību izvēlēties gravitācijas uzdevumā?",
     "Sakārto temata sakarības; risina jauktus uzdevumus un labo "
     "biežākās kļūdas."),
    ("PD", "PD5", "Gravitācijas lauks un kustība",
     "Lieto vispasaules gravitācijas likumu, aprēķina lauka intensitāti, "
     "kosmisko ātrumu un orbītas raksturlielumus.", 10, PIEZ),
    ("st", "Kļūdu analīze",
     "Kur pazuda mērvienības?",
     "Analizē pārbaudes darba kļūdas; trenē lielumu kārtas novērtēšanu un "
     "standartformu."),
]

# ------------------------------------------------------------------ 5. TEMATS
T5 = [
    ("st", "Mehāniskais darbs",
     "Kad spēks veic darbu?",
     "Lieto A = Fs·cosα; nosaka darba zīmi un skaidro, kad darbs ir nulle."),
    ("st", "Jauda un lietderības koeficients",
     "Kāpēc jaudīgāks dzinējs ir ātrāks?",
     "Lieto P = A/t un P = Fv; aprēķina lietderības koeficientu un "
     "izvērtē enerģijas zudumus."),
    ("st", "Uzdevumi: darbs un jauda",
     "Cik jaudīgs ir cilvēks, skrienot pa kāpnēm?",
     "Risina praktiskus uzdevumus par darbu, jaudu un lietderību; "
     "pārbauda mērvienības un rezultāta ticamību."),
    ("st", "Kinētiskā enerģija",
     "Kāpēc ātrums ir bīstamāks par masu?",
     "Lieto Ek = mv²/2; saista kinētiskās enerģijas izmaiņu ar padarīto "
     "darbu."),
    ("st", "Potenciālā enerģija",
     "Kur 'glabājas' pacelta ķermeņa enerģija?",
     "Lieto Ep = mgh un atsperes enerģiju Ep = kx²/2; izvēlas nulles "
     "līmeni un pamato izvēli."),
    ("st", "Enerģijas nezūdamība un LD4 plāns",
     "Kur pazūd enerģija?",
     "Formulē mehāniskās enerģijas nezūdamības likumu; sagatavo mērīšanas "
     "plānu un datu tabulu laboratorijas darbam."),
    ("LD", "LD4", "Laboratorijas darbs",
     "Mehāniskās enerģijas nezūdamības pārbaude",
     "Mēra ķermeņa augstumu un ātrumu vai svārsta novirzi; salīdzina "
     "potenciālo un kinētisko enerģiju, novērtē zudumus un kļūdas.",
     9, PIEZ_LD),
    ("st", "LD4 datu analīze",
     "Vai enerģija tiešām saglabājās?",
     "Aprēķina enerģijas attiecību, veido grafiku un skaidro novirzes ar "
     "berzi un mērījumu kļūdām."),
    ("st", "Impulss",
     "Kāpēc smagu ķermeni grūti apturēt?",
     "Lieto p = mv un spēka impulsu Ft = Δp; skaidro trieciena laika "
     "nozīmi drošībā."),
    ("st", "Impulsa nezūdamība",
     "Kas notiek sadursmē?",
     "Formulē un lieto impulsa nezūdamības likumu slēgtai sistēmai; "
     "risina uzdevumus par sadursmēm vienā taisnē."),
    ("st", "Elastīgs un neelastīgs trieciens",
     "Kad enerģija pazūd, bet impulss nē?",
     "Salīdzina elastīgu un neelastīgu triecienu; pamato, kura sakarība "
     "der katrā gadījumā."),
    ("st", "Enerģija un impulss kopā",
     "Kad lietot enerģiju, kad impulsu?",
     "Izvēlas piemērotu nezūdamības likumu situācijai; risina kombinētus "
     "uzdevumus un pamato izvēli."),
    ("st", "Temata nostiprināšana",
     "Kā pamatot enerģijas pārvērtību ķēdi?",
     "Apraksta enerģijas pārvērtības reālā ierīcē; risina jauktus "
     "uzdevumus un labo biežākās kļūdas."),
    ("PD", "PD6", "Enerģija, darbs un impulss",
     "Lieto darba, jaudas un lietderības sakarības, enerģijas un impulsa "
     "nezūdamības likumus; pamato izvēlēto risinājuma ceļu.", 11, PIEZ),
    ("st", "Kļūdu analīze",
     "Ko paņemam līdzi uz 11. klasi?",
     "Analizē pārbaudes darba kļūdas; apkopo mehānikas sakarības vienā "
     "atgādnē."),
]

# ------------------------------------------------------------------- noslēgums
NOSL = [
    ("st", "Mehānika ap mums",
     "Kur mehānika parādās ikdienā?",
     "Ar apgūtajām sakarībām skaidro transporta drošību, sportu un "
     "celtniecības risinājumus."),
    ("st", "Gada noslēgums",
     "Ko protam, sākot 11. klasi?",
     "Apkopo gada laikā apgūtās sakarībās un prasmes; novērtē savu "
     "sniegumu un plāno, kas jāatkārto."),
]


def build(path):
    p = Plans()
    b1 = p.bloks(T1)
    b2 = p.bloks(T2)
    b3 = p.bloks(T3)
    b4 = p.bloks(T4)
    b5 = p.bloks(T5)
    bn = p.bloks(NOSL)
    p.parbaudi()

    doc = new_doc("10. klase", p.n,
                  "Fizika I pamatkurss, pirmais mācību gads. Plāns aptver "
                  "programmas tematus «Vektori un kustība», «Vienmērīga "
                  "kustība», «Vienmērīgi paātrināta kustība», "
                  "«Mijiedarbība un spēks», «Gravitācijas lauks un kustība» "
                  "un «Enerģija un darbs». Mācību mērķis ir centralizētais "
                  "eksāmens fizikā optimālajā līmenī 11. klases beigās, "
                  "tāpēc katrā tematā ir uzdevumu risināšanas un kļūdu "
                  "analīzes stundas eksāmena formātā.")

    kalendars(doc, p.vertejumi,
              "Pirmais pārbaudes darbs PD1 ir 16.09.2026. - otrajā mācību "
              "nedēļā. Laboratorijas darbi vienmēr notiek trešdienas "
              "dubultstundā; protokolu iesniedz e-klasē nedēļas laikā, "
              "atsevišķa mācību stunda tam nav atvēlēta.")

    temata_tabula(doc, "1. temats. Ievads pētniecībā. Vienmērīga un "
                       "nevienmērīga kustība (%d stundas)" % len(b1),
                  "Apvienoti programmas temati «Vektori un kustība» un "
                  "«Vienmērīga kustība». Temats noslēdzas ar kļūdu "
                  "aprēķināšanu pētījumā.", b1,
                  "Vektoru koordinātu forma telpā; kustība ar mainīgu "
                  "ātrumu un integrāļa jēdziens.")
    temata_tabula(doc, "2. temats. Vienmērīgi paātrināta kustība "
                       "(%d stundas)" % len(b2),
                  "Kinemātikas pamattemats: vienādojumi, grafiki, brīvā "
                  "krišana un kustība pa riņķa līniju.", b2,
                  "Slīpi mests ķermenis un trajektorijas vienādojums.")
    temata_tabula(doc, "3. temats. Mijiedarbība un spēks (%d stundas)"
                  % len(b3),
                  "Kursa apjomīgākais temats. Ietver Ņūtona likumus, "
                  "spēku veidus, statiku un hidrostatiku.", b3,
                  "Sarežģītas ķermeņu sistēmas ar vairākiem blokiem; "
                  "berze uz slīpas plaknes ar mainīgu leņķi.")
    temata_tabula(doc, "4. temats. Gravitācijas lauks un kustība "
                       "(%d stundas)" % len(b4),
                  "Gravitācija kā lauks; kustība orbītā un Keplera "
                  "likumi.", b4,
                  "Otrais kosmiskais ātrums un enerģija atklātā orbītā.")
    temata_tabula(doc, "5. temats. Enerģija un darbs (%d stundas)" % len(b5),
                  "Darbs, enerģija, jauda un abi nezūdamības likumi - "
                  "biežāk pārbaudītais saturs eksāmenā.", b5,
                  "Trieciens divās dimensijās; enerģijas zudumi reālās "
                  "sistēmās.")
    noslegums(doc, "Gada noslēguma nostiprināšana (%d stundas)" % len(bn),
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
                       "Fizika I 10. klase - tematu, PD un LD plans_tt.docx")
    p = build(out)
    print("10. klase: %d stundas, %d vertejumi -> %s"
          % (p.n, len(p.vertejumi), os.path.basename(out)))
    for m in p.mainas:
        print("  UZMANIBU: %s" % m)
    for kods, tema, svars, datums, _ in p.vertejumi:
        print("      %-5s %-48s %2d %%  %s" % (kods, tema[:48], svars, datums))
