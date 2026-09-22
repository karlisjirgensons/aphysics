# -*- coding: utf-8 -*-
"""7. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 7. klases sadaļa.
"""

from math_plani import B, T

IEVADS = (
    "Septītais matemātikas gads - pirmais pamatskolas noslēguma posmā. "
    "Sākas algebra: izteiksmes ar mainīgo, lineāri vienādojumi, nevienādības "
    "un lineāra funkcija ar grafiku. Ģeometrijā mācās definēt, pierādīt un "
    "konstruēt: trijstūru vienādības pazīmes, leņķu sakarības pie paralēlām "
    "taisnēm un trijstūra leņķu summa. Gads sākas ar kopām, pilno pārlasi un "
    "varbūtību, kas noder gan spēlēs, gan drošības kodos.")

TEMATI = [
    T("7.1.", "Kā nosaka kopas visus elementus, aprēķina notikuma varbūtību?",
      "Sistematizē izpratni par kopu un izlasi, mācās pilno pārlasi un "
      "notikuma varbūtību.",
      [B("Kopas un darbības ar tām", [
          ("Kas ir kopa?",
           "Skaidro jēdzienu kopa un ilustrē to ar piemēriem no dzīves un "
           "matemātikas."),
          ("Kā kopu var aprakstīt?",
           "Definē kopu, uzskaitot elementus vai norādot tos raksturojošu "
           "īpašību."),
          ("Kas ir apakškopa?",
           "Veido un raksturo dotas kopas apakškopas, piemēram, četrstūru "
           "klasifikācijā."),
          ("Kas ir kopu apvienojums un šķēlums?",
           "Nosaka divu galīgu kopu apvienojumu un šķēlumu un attēlo tos "
           "vizuāli."),
          ("Cik cilvēku ir kopā?",
           "Risina sadzīves uzdevumu, lietojot kopu apvienojumu un šķēlumu, "
           "un pamato rezultātu."),
          ("Vai esam uzskaitījuši visas apakškopas?",
           "Strukturēti pieraksta visas dotas kopas apakškopas un pamato, ka "
           "citu nav."),
      ]),
       B("Pilnā pārlase un izlases", [
           ("Kā informāciju parādīt pārskatāmi?",
            "Attēlo informāciju tabulā, grafā vai Venna diagrammā un "
            "salīdzina attēlojuma veidus."),
           ("Kas ir pilnā pārlase?",
            "Uzskaita visus gadījumus un pārliecinās, ka neviens nav "
            "izlaists."),
           ("Ar ko izlase atšķiras no apakškopas?",
            "Skaidro atšķirību starp kopu un izlasi un ilustrē to ar "
            "piemēriem."),
           ("Vai secībai ir nozīme?",
            "Argumentē, vai konkrētajā situācijā izlases elementu secībai ir "
            "nozīme."),
           ("Cik dažādus kodus var izveidot?",
            "Aprēķina iespēju skaitu, lietojot reizināšanas likumu, un pamato "
            "spriedumu."),
           ("Cik nogriežņu var novilkt?",
            "Nosaka objektu skaitu ģeometriskā situācijā, izmantojot pilno "
            "pārlasi vai spriedumus."),
       ]),
       B("Varbūtība", [
           ("Ko nozīmē «liela varbūtība»?",
            "Min piemērus par varbūtības jēdziena lietojumu sadzīvē un "
            "plašsaziņas līdzekļos."),
           ("Kā varbūtību noteikt ar eksperimentu?",
            "Eksperimentāli un ar simulāciju nosaka notikuma biežumu un "
            "salīdzina to ar prognozi."),
           ("Kā varbūtību aprēķina teorētiski?",
            "Aprēķina notikuma varbūtību un pieraksta to kā daļu vai "
            "procentus."),
           ("Kāda ir droša un neiespējama notikuma varbūtība?",
            "Nosaka droša un neiespējama notikuma varbūtību un pamato "
            "atbildi."),
           ("Vai loterijā ir izdevīgi spēlēt?",
            "Analizē spēles vai loterijas piemēru un izvērtē notikuma "
            "varbūtību."),
       ])],
      "Kopas, izlases un varbūtība",
      "Nosaka kopas elementus, apakškopas, apvienojumu un šķēlumu; lieto "
      "pilno pārlasi un reizināšanas likumu objektu skaita noteikšanai; "
      "aprēķina notikuma varbūtību.",
      "kombinācijas ar atkārtojumiem; varbūtības salīdzināšana divās spēlēs."),

    T("7.2.", "Kā definē ģeometriskas figūras?",
      "Veido izpratni par definēšanu un pierādīšanu, sistematizē zināšanas "
      "par figūrām un divu taišņu novietojumu plaknē.",
      [B("Ģeometrisku figūru definēšana", [
          ("Kas ir ģeometriska figūra?",
           "Skaidro, ka figūra ir punktu kopa, un ilustrē to ar piemēriem."),
          ("Kāpēc punktu nevar definēt?",
           "Raksturo punktu, taisni un plakni ar reāliem modeļiem un skaidro, "
           "kāpēc tos nedefinē."),
          ("Kā definē staru un nogriezni?",
           "Veido definīcijas pazīstamām figūrām, izmantojot jau definētās."),
          ("Vai šī definīcija ir laba?",
           "Izvērtē citu veidotas definīcijas un ar pretpiemēru parāda to "
           "neatbilstību."),
          ("Kur atrodas visi šie punkti?",
           "Nosaka punktu ar noteiktu īpašību novietojumu plaknē un formulē "
           "apgalvojumu."),
          ("Kā pieraksta ar simboliem?",
           "Lieto apzīmējumus punktu, taišņu, staru un nogriežņu novietojuma "
           "pierakstam."),
      ]),
       B("Vienādas figūras", [
           ("Kad divas figūras ir vienādas?",
            "Nosaka vienādas figūras un pamato vienādību ar modeli vai "
            "definīciju."),
           ("Kā pārbaudīt vienādību?",
            "Pārbauda figūru vienādību ar caurspīdīga papīra attēlojumu vai "
            "locīšanu."),
           ("Kā uzzīmēt vienādu figūru?",
            "Zīmē rūtiņu lapā figūru, kas vienāda ar doto, pēc dotiem "
            "nosacījumiem."),
           ("Vai figūru var sadalīt vienādās daļās?",
            "Spriež un pamato, vai doto figūru var sadalīt noteiktā skaitā "
            "vienādu daļu."),
           ("Kā lasīt zīmējumu?",
            "Nosaka un pieraksta pēc iespējas vairāk figūru dotā zīmējumā."),
       ]),
       B("Nogriežņa garums un pierādījums", [
           ("Kā aprēķina nogriežņa garumu?",
            "Aprēķina nogriežņa garumu kā citu nogriežņu garumu summu vai "
            "starpību."),
           ("Kas ir viduspunkts?",
            "Definē nogriežņa viduspunktu un lieto tā īpašību aprēķinos."),
           ("Kā izskatās strukturēts risinājums?",
            "Veido strukturētu risinājuma pierakstu un izvērtē citu "
            "pierakstus."),
           ("Kas ir teorēma un pierādījums?",
            "No situācijas apraksta nosaka, kas dots un kas jāpierāda."),
           ("Kā uzbūvēt divu soļu pamatojumu?",
            "Veido pamatojumu, kas satur divus saistītus spriedumus par "
            "nogriežņu vienādību."),
       ]),
       B("Divu taišņu novietojums plaknē", [
           ("Cik kopīgu punktu var būt divām taisnēm?",
            "Secina par divu taišņu savstarpējo novietojumu plaknē."),
           ("Kas ir blakusleņķi un krustleņķi?",
            "Definē blakusleņķus un krustleņķus un atrod tos zīmējumā."),
           ("Kā pierādīt krustleņķu īpašību?",
            "Pierāda krustleņķu īpašību, izmantojot blakusleņķu īpašību, un "
            "veido pierakstu."),
           ("Kā aprēķināt nezināmo leņķi?",
            "Aprēķina leņķu lielumus, lietojot blakusleņķu un krustleņķu "
            "īpašības."),
       ])],
      "Definīcijas, vienādas figūras un leņķi",
      "Veido un izvērtē figūru definīcijas; pamato figūru vienādību; aprēķina "
      "nogriežņu garumus un leņķu lielumus, lietojot blakusleņķu un "
      "krustleņķu īpašības; veido divu soļu pamatojumu.",
      "punktu ģeometriskā vieta; pierādījumi ar trim spriedumiem."),

    T("7.3.", "Kā raksturo sakarību starp mainīgiem lielumiem?",
      "Veido izpratni par neatkarīgo un atkarīgo mainīgo un par sakarības "
      "pierakstu ar formulu.",
      [B("Mainīgie lielumi un formula", [
          ("Kas situācijā mainās un kas ne?",
           "Nosaka situācijā mainīgos un nemainīgos lielumus un raksturo "
           "tos."),
          ("Kurš mainīgais no kura atkarīgs?",
           "Nosaka neatkarīgo un atkarīgo mainīgo un skaidro jēdzienu "
           "nozīmi."),
          ("Kā sakarību pierakstīt ar formulu?",
           "Pieraksta sakarību ar formulu, izvēloties burtus lielumu "
           "apzīmēšanai."),
          ("Kādas vērtības mainīgajam ir iespējamas?",
           "Nosaka, kuri skaitļi var būt mainīgā vērtības konkrētajā "
           "situācijā."),
      ]),
       B("Tieši proporcionāli lielumi", [
           ("Kā izskatās tarifa tabula un grafiks?",
            "Apkopo lielumu vērtības tabulā un attēlo tās grafiski; raksturo "
            "abu veidu priekšrocības."),
           ("Punkti vai nepārtraukta līnija?",
            "Argumentē, vai sakarības grafiks ir līnija vai atsevišķi "
            "punkti."),
           ("Kā mainās ceļš vienmērīgā kustībā?",
            "Attēlo grafiski un pieraksta ar formulu sakarību starp laiku un "
            "ceļu."),
           ("Kurš brauc ātrāk?",
            "Salīdzina divu objektu ātrumus pēc to grafikiem un pamato "
            "secinājumu."),
       ]),
       B("Apgriezti proporcionāli un citas sakarības", [
           ("Kā izskatās apgriezti proporcionāla sakarība?",
            "Apkopo tabulā taisnstūra malu garumus ar dotu laukumu un attēlo "
            "sakarību grafiski."),
           ("Ko stāsta grafika tuvošanās asīm?",
            "Nolasa informāciju no grafika un skaidro lielumu iespējamās "
            "vērtības."),
           ("Vai starp lielumiem vispār ir sakarība?",
            "Izvērtē, vai divus lielumus raksturojošos datus saista sakarība, "
            "ko var aprakstīt matemātiski."),
       ])],
      "Sakarības starp mainīgiem lielumiem",
      "Nosaka mainīgo vērtības, ja sakarība dota ar tabulu, grafiku vai "
      "formulu; raksturo sakarību vārdiski; attēlo sakarību grafiski un "
      "pieraksta ar formulu.",
      "sakarības ar trim mainīgajiem; mērvienību pārveidojumi formulās."),

    T("7.4.", "Kā pieraksta un pēta funkcijas, kuru grafiks ir taisne?",
      "Veido izpratni par funkciju un lineāru funkciju, tās grafiku un "
      "īpašībām; lieto to kā reālu procesu modeli.",
      [B("Funkcija un ar to saistītie jēdzieni", [
          ("Kad sakarība ir funkcija?",
           "Lieto funkcijas definīciju, lai noteiktu, vai dotā sakarība ir "
           "funkcija."),
          ("Kas ir arguments un funkcijas vērtība?",
           "Lieto jēdzienus arguments un funkcijas vērtība, nolasot "
           "informāciju no grafika."),
          ("Kā izskatās funkcijas grafiks?",
           "Veido skaitļu pārus un atzīmē tos koordinātu plaknē, iegūstot "
           "funkcijas grafiku."),
          ("Kuras sakarības nav funkcijas?",
           "Min piemērus sakarībām, kas nav funkcijas, un pamato izvēli."),
          ("Kādas vērtības funkcija pieņem?",
           "Nosaka funkcijas definīcijas kopu un vērtību kopu vienkāršos "
           "gadījumos."),
      ]),
       B("Lineāras funkcijas attēlojumi", [
           ("Kā no algoritma iegūt formulu?",
            "Pieraksta ar formulu funkciju, kas aprakstīta algoritma veidā."),
           ("Kāpēc grafiks ir taisne?",
            "Formulē vispārinājumu par grafiku, ja argumentu reizina un "
            "pieskaita skaitli."),
           ("Cik punktu vajag taisnei?",
            "Zīmē lineāras funkcijas grafiku pēc formulas, izvēloties punktu "
            "skaitu, un pamato izvēli."),
           ("Kā izskatās y = 2 grafiks?",
            "Zīmē grafikus funkcijām ar nemainīgu vērtību un formulē "
            "vispārinājumu."),
           ("Kā izvēlēties vienības uz asīm?",
            "Nosaka piemērotus vienību nogriežņus, lai attēlotu funkciju ar "
            "lieliem koeficientiem."),
       ]),
       B("Lineāras funkcijas īpašības", [
           ("Ko var nolasīt no grafika?",
            "Nolasa no grafika funkcijas vērtību, argumentu un krustpunktus "
            "ar asīm."),
           ("Kad funkcija ir pozitīva un kad negatīva?",
            "Nosaka argumenta vērtības, kurām funkcija ir pozitīva vai "
            "negatīva."),
           ("Funkcija aug vai dilst?",
            "Nosaka, vai funkcija ir augoša vai dilstoša, un saista to ar "
            "koeficientu k."),
           ("Ko nozīmē koeficienti k un b?",
            "Pēta ar digitāliem rīkiem grafika novietojumu atkarībā no k un b "
            "vērtībām."),
           ("Kā uzzīmēt grafiku pēc nosacījumiem?",
            "Zīmē grafiku lineārai funkcijai, kas atbilst diviem "
            "nosacījumiem."),
       ]),
       B("Lineāra funkcija kā modelis", [
           ("Kurš tarifs ir izdevīgāks?",
            "Salīdzina divus maksājumu tarifus, lietojot grafikus un "
            "formulas."),
           ("Kā izpētīt sveces degšanu?",
            "Iegūst datus par reālu procesu, attēlo tos grafiski un raksturo "
            "modeli."),
           ("Kāpēc grafiks nav ideāla taisne?",
            "Izsaka pieņēmumus par mērījumu novirzēm un procesa robežām."),
       ])],
      "Lineāra funkcija un tās grafiks",
      "Zīmē lineāras funkcijas grafiku pēc formulas; nolasa no grafika "
      "funkcijas vērtības, krustpunktus un zīmes; nosaka, vai funkcija ir "
      "augoša vai dilstoša; lieto lineāru funkciju kā situācijas modeli.",
      "divu funkciju grafiku krustpunkts; abscisu nolasīšana no grafika."),

    T("7.5.", "Kā raksturo trijstūri, izmantojot tā elementus?",
      "Veido izpratni par trijstūra eksistenci, veidiem un elementiem; "
      "pilnveido konstruēšanas un pierādīšanas prasmes.",
      [B("Trijstūra eksistence un elementi", [
          ("Vai no šiem nogriežņiem var izveidot trijstūri?",
           "Lieto trijstūra nevienādību, lai noteiktu trijstūra eksistenci."),
          ("Cik garš var būt trešais nogrieznis?",
           "Nosaka trešās malas iespējamo garumu, ja divas malas zināmas; "
           "izmanto skici."),
          ("Kurš maršruts ir īsāks?",
           "Lieto trijstūra nevienādību reālā kontekstā un pamato "
           "secinājumu."),
          ("Kā trijstūrī sauc katru elementu?",
           "Lieto jēdzienus mala, leņķis, pretmala, piemala, pretleņķis, "
           "pieleņķi."),
          ("Kā konstruēt vienādu leņķi?",
           "Ar cirkuli un lineālu konstruē leņķi, kas vienāds ar doto."),
      ]),
       B("Vienādi trijstūri", [
           ("Kā ar locīšanu iegūt vienādus trijstūrus?",
            "Ar locīšanu iegūst vienādus trijstūrus un pamato to vienādību."),
           ("Cik elementu jāzina, lai trijstūri būtu vienādi?",
            "Zīmē trijstūrus pēc diviem dotiem elementiem un secina, ka ar "
            "tiem nepietiek."),
           ("Kāda ir pazīme mlm?",
            "Formulē un lieto pirmo trijstūru vienādības pazīmi."),
           ("Kāda ir pazīme mmm?",
            "Ar cirkuli un lineālu konstruē trijstūri pēc trim malām un "
            "formulē pazīmi."),
           ("Kāda ir pazīme lml?",
            "Konstruē trijstūri pēc malas un tās pieleņķiem un formulē "
            "pazīmi."),
       ]),
       B("Vienādības pazīmju lietošana", [
           ("Kā pierādīt divu trijstūru vienādību?",
            "Pierāda trijstūru vienādību pēc dota zīmējuma un veido "
            "strukturētu pierakstu."),
           ("Kā no trijstūriem secināt par malām?",
            "No trijstūru vienādības secina par to elementu vienādību."),
           ("Kā zīmēt pašam?",
            "Veido zīmējumu pēc teksta un pierāda elementu vienādību."),
           ("Kā plānot garāku pierādījumu?",
            "Plāno pierādījuma gaitu, lietojot spriešanu no beigām."),
           ("Kad trijstūri pārklājas?",
            "Pierāda vienādību situācijā, kurā trijstūri zīmējumā pārklājas."),
       ]),
       B("Vienādsānu trijstūris un tā līnijas", [
           ("Kas ir vienādsānu un vienādmalu trijstūris?",
            "Definē un klasificē trijstūrus pēc malu garumiem."),
           ("Kādas īpašības ir vienādsānu trijstūrim?",
            "Lieto vienādsānu trijstūra īpašības figūru lielumu "
            "aprēķināšanai."),
           ("Kas ir bisektrise, mediāna un augstums?",
            "Definē trijstūra bisektrisi, mediānu un augstumu un zīmē tās."),
           ("Kā konstruēt leņķa bisektrisi?",
            "Ar cirkuli un lineālu konstruē leņķa bisektrisi un pamato "
            "darbības."),
           ("Kā izmērīt attālumu no punkta līdz taisnei?",
            "Konstruē perpendikulu no punkta pret taisni un skaidro attāluma "
            "jēdzienu."),
       ])],
      "Trijstūris, tā elementi un vienādības pazīmes",
      "Lieto trijstūra nevienādību; konstruē trijstūrus ar cirkuli un "
      "lineālu; pierāda figūru īpašības ar trijstūru vienādības pazīmēm; "
      "lieto vienādsānu trijstūra īpašības un trijstūra līniju definīcijas.",
      "vidusperpendikuls un tā īpašība; pierādījumi ar trim spriedumiem."),

    T("7.6.", "Kādas ir sakarības starp lielumiem trijstūrī?",
      "Veido izpratni par īpašību un pazīmi; apgūst leņķu sakarības pie "
      "paralēlām taisnēm un trijstūra leņķu summu.",
      [B("Paralēlas taisnes un leņķi", [
          ("Kā pārbaudīt, vai taisnes ir paralēlas?",
           "Konstruē paralēlas taisnes un pārbauda paralelitāti."),
          ("Kādi leņķi veidojas pie paralēlām taisnēm?",
           "Nosauc kāpšļu leņķus, iekšējos šķērsleņķus un iekšējos "
           "vienpusleņķus."),
          ("Kādas ir šo leņķu īpašības?",
           "Formulē un pierāda iekšējo šķērsleņķu un vienpusleņķu īpašības."),
          ("Kā aprēķināt nezināmo leņķi?",
           "Aprēķina leņķu lielumus, lietojot paralēlu taišņu leņķu "
           "īpašības."),
          ("Kas ir īpašība un kas - pazīme?",
           "Skaidro atšķirību starp īpašību un pazīmi un min piemērus."),
      ]),
       B("Trijstūra leņķu summa", [
           ("Cik ir trijstūra leņķu summa?",
            "Praktiski un ar spriedumu iegūst, ka trijstūra leņķu summa ir "
            "180°."),
           ("Kā pierāda leņķu summas teorēmu?",
            "Pierāda trijstūra leņķu summas teorēmu, izmantojot paralēlas "
            "taisnes."),
           ("Kā aprēķināt trijstūra leņķus?",
            "Aprēķina nezināmos leņķus trijstūrī, veidojot risinājuma "
            "pierakstu."),
           ("Kādi ir trijstūru veidi pēc leņķiem?",
            "Klasificē trijstūrus pēc leņķiem un pamato klasifikāciju."),
           ("Kādi leņķi ir vienādsānu trijstūrī?",
            "Lieto leņķu summu un vienādsānu trijstūra īpašības kopā."),
       ]),
       B("Malas, leņķi un ārējais leņķis", [
           ("Kurš leņķis ir lielākais?",
            "Formulē un lieto sakarību: pret garāko malu atrodas lielākais "
            "leņķis."),
           ("Kā no leņķiem spriest par malām?",
            "Salīdzina trijstūra malas, ja doti tā leņķu lielumi."),
           ("Kas ir trijstūra ārējais leņķis?",
            "Definē ārējo leņķi un formulē sakarību ar diviem iekšējiem "
            "leņķiem."),
           ("Kā aprēķināt ar ārējo leņķi?",
            "Aprēķina nezināmos lielumus, lietojot ārējā leņķa īpašību."),
           ("Vai apgalvojums ir patiess?",
            "Izvērtē apgalvojumus par vienādsānu un vienādmalu trijstūri un "
            "pamato atbildi."),
       ]),
       B("Taisnleņķa trijstūris un pierādījumi", [
           ("Kādas ir taisnleņķa trijstūra īpašības?",
            "Nosauc katetes un hipotenūzu un lieto leņķu summu taisnleņķa "
            "trijstūrī."),
           ("Kā konstruēt trijstūri pēc dotiem lielumiem?",
            "Ar cirkuli un lineālu konstruē trijstūrus atbilstoši dotiem "
            "elementiem."),
           ("Kā uzbūvēt pierādījumu?",
            "Pierāda figūras īpašību, lietojot leņķu sakarības un trijstūru "
            "vienādību."),
           ("Kā izmantot skici?",
            "Veido skici sarežģītākai situācijai un plāno risinājuma soļus."),
           ("Kur ģeometrija noder dzīvē?",
            "Lieto leņķu sakarības praktiskā situācijā (jumta slīpums, "
            "maršruts, konstrukcija)."),
       ])],
      "Leņķu sakarības un trijstūra leņķu summa",
      "Lieto leņķu īpašības pie paralēlām taisnēm; aprēķina nezināmos leņķus, "
      "izmantojot trijstūra leņķu summu un ārējā leņķa īpašību; salīdzina "
      "trijstūra malas un leņķus; pierāda figūru īpašības.",
      "trijstūra nevienādības pierādījums; daudzstūra leņķu summa."),

    T("7.7.", "Ko nozīmē pārveidot izteiksmi ar mainīgo lielumu?",
      "Sistematizē izpratni par algebriskām izteiksmēm un to identiskiem "
      "pārveidojumiem.",
      [B("Izteiksmes ar mainīgo", [
          ("Kā situāciju pierakstīt ar burtiem?",
           "Apraksta situāciju ar algebrisku izteiksmi, apzīmējot nezināmos "
           "lielumus ar burtiem."),
          ("Ko nozīmē 4a?",
           "Skaidro reizinājuma pierakstu ar mainīgo un modelē to "
           "ģeometriski."),
          ("Kā aprēķināt izteiksmes vērtību?",
           "Aprēķina algebriskas izteiksmes vērtību dotai mainīgā vērtībai."),
          ("Kā pierakstīt attiecību ar burtiem?",
           "Apraksta ar izteiksmi lielumus, kas doti kā divu vai trīs skaitļu "
           "attiecība."),
          ("Kā pierakstīt procentu izmaiņas?",
           "Pieraksta ar izteiksmi lieluma palielinājumu vai samazinājumu "
           "procentos."),
      ]),
       B("Identiski pārveidojumi", [
           ("Kad divas izteiksmes ir vienādas?",
            "Skaidro, kas ir identiski vienādas izteiksmes, un pamato tās ar "
            "piemēriem."),
           ("Kā savilkt līdzīgos saskaitāmos?",
            "Savelk līdzīgos saskaitāmos un raksturo izmantoto darbību "
            "īpašību."),
           ("Kā atvērt iekavas?",
            "Atver iekavas, lietojot reizināšanas sadalāmības īpašību."),
           ("Kas notiek ar zīmēm pirms iekavām?",
            "Atver iekavas, pirms kurām ir mīnusa zīme, un pamato zīmju "
            "maiņu."),
           ("Kā pārveidot garāku izteiksmi?",
            "Vienkāršo izteiksmi vairākos soļos un pieraksta katru soli."),
           ("Kur radusies kļūda?",
            "Atrod kļūdu dotā pārveidojumā un izskaidro tās cēloni."),
       ]),
       B("Sadalīšana reizinātājos un lietojums", [
           ("Kā iznest kopīgo reizinātāju?",
            "Sadala izteiksmi reizinātājos, iznesot kopīgo reizinātāju pirms "
            "iekavām."),
           ("Kā pārbaudīt pārveidojumu?",
            "Pārbauda pārveidojuma pareizību, ievietojot mainīgā skaitlisku "
            "vērtību."),
           ("Kā izteiksme palīdz aprēķināt perimetru?",
            "Pieraksta ar izteiksmi figūras perimetru vai laukumu un "
            "vienkāršo to."),
           ("Kā izteiksme apraksta dzīves situāciju?",
            "Veido un vienkāršo izteiksmi praktiskai situācijai ar cenām vai "
            "attālumiem."),
           ("Vai apgalvojums par izteiksmēm ir patiess?",
            "Pamato, ka izteiksmes ir identiski vienādas, vai atspēko to ar "
            "pretpiemēru."),
       ])],
      "Algebriskas izteiksmes un to pārveidojumi",
      "Veido un aprēķina algebriskas izteiksmes; savelk līdzīgos saskaitāmos; "
      "atver iekavas; sadala izteiksmi reizinātājos; pamato, ka izteiksmes ir "
      "identiski vienādas.",
      "izteiksmes ar diviem mainīgajiem; pierādījumi par skaitļu īpašībām."),

    T("7.8.", "Kādi ir paņēmieni nezināmā noteikšanai?",
      "Veido izpratni par lineāru vienādojumu un proporciju un lieto tos "
      "situāciju uzdevumu risināšanā.",
      [B("Vienādojums un tā sakne", [
          ("Kas ir vienādojums?",
           "Skaidro, kas ir vienādojums un tā sakne, un pārbauda, vai "
           "skaitlis ir sakne."),
          ("Ko nozīmē atrisināt vienādojumu?",
           "Skaidro, ka jāatrod visas saknes un jāpamato, ka citu nav."),
          ("Kad vienādojumi ir ekvivalenti?",
           "Nosaka, vai divi vienādojumi ir ekvivalenti, un pamato atbildi."),
          ("Kā vienādojumu atrisināt spriežot?",
           "Atrisina vienkāršu vienādojumu, spriežot par sakarībām starp "
           "lielumiem."),
          ("Kā atrisināt grafiski?",
           "Atrisina vienādojumu grafiski, abas puses attēlojot kā "
           "funkcijas."),
      ]),
       B("Lineāra vienādojuma risināšana", [
           ("Kā pārveidot vienādojumu ekvivalenti?",
            "Lieto vienādojuma abām pusēm vienādas darbības un pamato "
            "pārveidojumu."),
           ("Kā pārnest saskaitāmo uz otru pusi?",
            "Atrisina lineāru vienādojumu, pārnesot saskaitāmos un savelkot "
            "līdzīgos."),
           ("Kā rīkoties ar iekavām un daļām?",
            "Atrisina vienādojumu, kurā ir iekavas vai daļskaitļi."),
           ("Cik sakņu var būt?",
            "Analizē gadījumus, kad vienādojumam nav sakņu vai ir bezgalīgi "
            "daudz sakņu."),
           ("Kā pārbaudīt sakni?",
            "Pārbauda atrisinājumu, ievietojot to sākotnējā vienādojumā."),
       ]),
       B("Proporcija", [
           ("Kas ir proporcija?",
            "Skaidro proporciju kā divu attiecību vienādību un lasa tās "
            "pierakstu."),
           ("Kā aprēķināt nezināmo locekli?",
            "Aprēķina proporcijas nezināmo locekli un pārbauda rezultātu."),
           ("Kur proporcija noder?",
            "Lieto proporciju uzdevumos par mērogu, recepti un cenām."),
           ("Kā izteikt vienu lielumu ar otru?",
            "Izsaka vienu lielumu ar otru no proporcijas un skaidro "
            "pierakstu."),
           ("Vai proporcija šeit der?",
            "Izvērtē, vai situācijā lielumi ir proporcionāli, un pamato "
            "izvēli."),
       ]),
       B("Uzdevumu risināšana ar vienādojumu", [
           ("Kā uzdevumu pārtulkot vienādojumā?",
            "Veido vienādojumu situācijas aprakstam, apzīmējot nezināmo ar "
            "burtu."),
           ("Kādi ir modelēšanas soļi?",
            "Nosauc un lieto matemātiskās modelēšanas soļus problēmas "
            "risināšanā."),
           ("Vai atrisinājums der situācijai?",
            "Nosaka matemātiskā atrisinājuma atbilstību reālajai situācijai."),
           ("Kā vienādojums apraksta figūru?",
            "Ar lineāru vienādojumu apraksta sakarības starp figūras "
            "lielumiem un atrisina to."),
           ("Kāds uzdevums sanāk tev?",
            "Veido savu uzdevumu dotam vienādojumam un risina klasesbiedra "
            "uzdevumu."),
       ])],
      "Lineāri vienādojumi un proporcija",
      "Atrisina lineāru vienādojumu ar ekvivalentiem pārveidojumiem; aprēķina "
      "proporcijas nezināmo locekli; risina situāciju uzdevumus, veidojot "
      "vienādojumu, un izvērtē atrisinājuma atbilstību.",
      "vienādojumi ar moduli; grafiskā risināšana ar digitāliem rīkiem."),

    T("7.9.", "Kā salīdzina izteiksmes, kurās ir mainīgais lielums?",
      "Veido izpratni par nevienādību, tās atrisinājumu kopu un lineāru "
      "nevienādību risināšanu.",
      [B("Nevienādības un to īpašības", [
          ("Kā salīdzināt izteiksmes ar mainīgo?",
           "Salīdzina izteiksmes (x un x + 3; 2x un 3x), spriežot un "
           "pamatojot spriedumu."),
          ("Kad nevienādība ir patiesa?",
           "Nosaka, vai nevienādība ir patiesa visām vai tikai dažām nezināmā "
           "vērtībām."),
          ("Kas ir atrisinājumu kopa?",
           "Skaidro, ka atrisināt nevienādību nozīmē atrast visus "
           "atrisinājumus."),
          ("Kādas ir nevienādību īpašības?",
           "Formulē un pamato skaitlisku nevienādību īpašības, izmantojot "
           "skaitļu taisni."),
          ("Kas notiek, reizinot ar negatīvu skaitli?",
           "Pamato, kāpēc, reizinot nevienādību ar negatīvu skaitli, zīme "
           "mainās."),
          ("Kas ir skaitļu intervāls?",
           "Attēlo intervālu uz skaitļu taisnes un pieraksta to ar "
           "nevienādību."),
      ]),
       B("Lineāras nevienādības risināšana", [
           ("Kā atrisināt nevienādību ekvivalenti pārveidojot?",
            "Atrisina lineāru nevienādību un pieraksta atrisinājumu kopu."),
           ("Kā atrisinājumu attēlot uz taisnes?",
            "Pārveido intervāla attēlojumu no viena veida citā."),
           ("Kā atrisināt grafiski?",
            "Atrisina nevienādību grafiski, abas puses attēlojot kā funkciju "
            "grafikus."),
           ("Kas ir divkārša nevienādība?",
            "Pieraksta divkāršu nevienādību kā nevienādību sistēmu."),
           ("Kā atrisināt sistēmu?",
            "Atrisina lineāru nevienādību sistēmu, nosakot atrisinājumu kopu "
            "šķēlumu."),
           ("Kā pārbaudīt atrisinājumu?",
            "Pārbauda atrisinājumu, izvēloties skaitli no iegūtā intervāla."),
       ]),
       B("Nevienādības dzīvē", [
           ("Kā situāciju pierakstīt ar nevienādību?",
            "Apraksta praktisku situāciju ar nevienādību un skaidro nezināmā "
            "nozīmi."),
           ("Cik preču var nopirkt par šo summu?",
            "Risina uzdevumu, kurā atbilde ir nezināmā vērtību kopa."),
           ("Vai atrisinājums ir reāls?",
            "Izvērtē, kuras atrisinājumu kopas vērtības ir jēgpilnas dotajā "
            "situācijā."),
           ("Kā apvienot vienādojumu un nevienādību?",
            "Risina problēmu, kurā vajadzīgs gan vienādojums, gan "
            "nevienādība."),
           ("Cik droši jau protu?",
            "Patstāvīgi risina jauktus uzdevumus ar vienādojumiem un "
            "nevienādībām."),
       ])],
      "Nevienādības un to atrisināšana",
      "Atrisina lineāru nevienādību un nevienādību sistēmu; attēlo "
      "atrisinājumu kopu uz skaitļu taisnes; apraksta situāciju ar "
      "nevienādību un izvērtē atrisinājuma jēgu.",
      "nevienādības ar parametru; atrisinājumu kopu apvienojums."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 7. klasē", [
        ("Cik droši rīkojos ar izteiksmēm?",
         "Formatīvi pārbauda algebrisko izteiksmju pārveidojumus un "
         "vienādojumu risināšanu."),
        ("Ko protu ģeometrijā?",
         "Atkārto trijstūru vienādības pazīmes, leņķu sakarības un "
         "pierādījuma pierakstu."),
        ("Kā lasu un zīmēju funkcijas grafiku?",
         "Atkārto lineāras funkcijas grafiku un tā īpašības."),
        ("Ko gaida 8. klasē?",
         "Apkopo gadā apgūto un iepazīstas ar 8. klases tematiem."),
    ]),
]
