# -*- coding: utf-8 -*-
"""8. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 8. klases sadaļa.
Daļveida izteiksmes plāna tekstā rakstītas ar vārdiem vai ar dalīšanas zīmi;
stundās daļas raksta vertikāli, kā to prasa latviešu standarts.
"""

from math_plani import B, T

IEVADS = (
    "Astotais matemātikas gads. Skaitļu pasaule kļūst pilnīga: pakāpes ar "
    "veselu kāpinātāju, skaitļa normālforma, iracionāli skaitļi un "
    "kvadrātsakne. Algebrā parādās monomi un polinomi, funkcijās - parabola "
    "un hiperbola, bet ģeometrijā - trijstūra un riņķa laukums, četrstūru "
    "īpašības, prizma, cilindrs un Pitagora teorēma. Gads sākas ar "
    "statistiku, kas nepieciešama, lai saprastu datus ziņās.")

TEMATI = [
    T("8.1.", "Kā matemātiski raksturo un analizē datus?",
      "Apgūst vienkāršākos statistiskos rādītājus un pilnveido datu ieguves, "
      "apstrādes un attēlošanas prasmes.",
      [B("Datu ieguve un sakārtošana", [
          ("Kā iegūt ticamus datus?",
           "Plāno datu ieguvi un raksturo, kā datu avots ietekmē "
           "secinājumus."),
          ("Kāpēc dati vispirms jāsakārto?",
           "Sakārto datu kopu augošā secībā un skaidro, kāpēc tas vajadzīgs."),
          ("Kā datus apstrādāt ar digitāliem rīkiem?",
           "Lieto izklājlapu datu sakārtošanai, apkopošanai un attēlošanai."),
          ("Kura diagramma der šiem datiem?",
           "Izvēlas piemērotu diagrammas veidu un pamato izvēli."),
          ("Kas ir absolūtais un relatīvais biežums?",
           "Nosaka absolūto un relatīvo biežumu un attēlo tos tabulā."),
      ]),
       B("Statistiskie rādītāji", [
           ("Kas ir aritmētiskais vidējais?",
            "Aprēķina aritmētisko vidējo un skaidro, ko tas raksturo."),
           ("Kas ir mediāna?",
            "Nosaka sakārtotas datu kopas mediānu un skaidro tās jēgu."),
           ("Kas ir moda un amplitūda?",
            "Nosaka datu kopas modu un amplitūdu un raksturo, ko tās parāda."),
           ("Kad vidējais maldina?",
            "Salīdzina aritmētisko vidējo un mediānu datu kopā ar novirzēm."),
           ("Kā salīdzināt divas datu kopas?",
            "Salīdzina divas objektu kopas, lietojot vairākus statistiskos "
            "rādītājus."),
       ]),
       B("Pētījums un secinājumi", [
           ("Kā formulēt pētījuma jautājumu?",
            "Plāno pētījuma mērķi un gaitu un formulē pētāmo jautājumu."),
           ("Kā savākt un apstrādāt datus?",
            "Iegūst datus, apstrādā tos un attēlo uzskatāmi."),
           ("Ko dati patiesībā rāda?",
            "Analizē datus ar statistiskajiem rādītājiem un formulē "
            "secinājumus."),
           ("Vai ziņās parādītie dati ir godīgi?",
            "Izvērtē diagrammu un statistikas lietojumu plašsaziņas "
            "līdzekļos."),
           ("Kā prezentēt rezultātus?",
            "Prezentē pētījuma rezultātus un atbild uz klasesbiedru "
            "jautājumiem."),
       ])],
      "Datu apstrāde un statistiskie rādītāji",
      "Sakārto un attēlo datus; nosaka amplitūdu, modu, mediānu un "
      "aritmētisko vidējo; analizē datus un salīdzina divas datu kopas; "
      "formulē pamatotus secinājumus.",
      "izkliedes jēdziens; datu attēlojumu kritiska analīze."),

    T("8.2.", "Kā skaidro un lieto pakāpi ar veselu kāpinātāju?",
      "Sistematizē izpratni par pakāpi, apgūst pakāpju īpašības un skaitļa "
      "normālformu.",
      [B("Pakāpes jēdziens un īpašības", [
          ("Kad izteiksme ir pakāpe?",
           "Nosaka, vai izteiksme ir pakāpe, pēc pēdējās darbības tās "
           "pierakstā."),
          ("Kā reizina pakāpes ar vienādām bāzēm?",
           "Pēta un formulē pakāpju reizināšanas īpašību, pierakstot pakāpi "
           "kā reizinājumu."),
          ("Kā dala pakāpes?",
           "Formulē un lieto pakāpju dalīšanas īpašību."),
          ("Kā kāpina pakāpi?",
           "Formulē un lieto pakāpes kāpināšanas īpašību."),
          ("Kā kāpina reizinājumu un daļu?",
           "Kāpina reizinājumu un daļu; pieraksta rezultātu vienkāršotā "
           "veidā."),
          ("Kā lietot īpašības kopā?",
           "Vienkāršo izteiksmi, lietojot vairākas pakāpju īpašības pēc "
           "kārtas."),
      ]),
       B("Pakāpe ar nulles un negatīvu kāpinātāju", [
           ("Kāda ir pakāpes vērtība ar kāpinātāju 0?",
            "Pēta virkni un formulē pieņēmumu par pakāpi ar kāpinātāju 0."),
           ("Ko nozīmē negatīvs kāpinātājs?",
            "Skaidro pakāpi ar negatīvu kāpinātāju kā apgriezto skaitli."),
           ("Kā pāriet uz pozitīvu kāpinātāju?",
            "Pārveido pakāpi ar negatīvu kāpinātāju par pakāpi ar pozitīvu "
            "kāpinātāju."),
           ("Vai īpašības der arī negatīviem kāpinātājiem?",
            "Lieto pakāpju īpašības izteiksmēs ar veselu kāpinātāju."),
           ("Kāds skaitlis sanāk?",
            "Aprēķina pakāpes skaitlisko vērtību, ja kāpinātājs ir vesels "
            "skaitlis."),
       ]),
       B("Pārveidojumi ar pakāpēm", [
           ("Kā skaitli pierakstīt kā pakāpi?",
            "Pieraksta skaitli vai reizinājumu kā pakāpi, ja tas iespējams."),
           ("Kā salīdzināt pakāpes?",
            "Salīdzina pakāpes, izmantojot vienādas bāzes vai vienādus "
            "kāpinātājus."),
           ("Kāda zīme ir pakāpei?",
            "Nosaka pakāpes zīmi, ja bāze ir negatīvs skaitlis."),
           ("Kā vienkāršot garu izteiksmi?",
            "Vienkāršo izteiksmi ar vairākām pakāpēm un pārbauda rezultātu."),
           ("Kāda likumsakarība ir pakāpju virknē?",
            "Pēta likumsakarības pakāpju pēdējos ciparos un formulē "
            "vispārinājumu."),
       ]),
       B("Skaitļa normālforma", [
           ("Kas ir skaitļa normālforma?",
            "Pieraksta skaitli normālformā un lasa to."),
           ("Kā no normālformas iegūt parasto pierakstu?",
            "Pārveido normālformā pierakstītu skaitli parastajā pierakstā."),
           ("Kā rēķināt ar normālformu?",
            "Reizina un dala normālformā pierakstītus skaitļus."),
           ("Kur lieto normālformu?",
            "Meklē informāciju par normālformas lietojumu zinātnē un tehnikā "
            "un raksturo to."),
       ])],
      "Pakāpes ar veselu kāpinātāju un normālforma",
      "Aprēķina pakāpes vērtību; lieto pakāpju īpašības izteiksmju "
      "pārveidojumos; pārveido pakāpi ar negatīvu kāpinātāju; pieraksta "
      "skaitli normālformā un rēķina ar to.",
      "pakāpju salīdzināšana bez aprēķina; ļoti lielu un mazu lielumu "
      "aprēķini."),

    T("8.3.", "Kā rīkojas, ja skaitli nevar pierakstīt kā daļu?",
      "Pilnveido izpratni par precīzo vērtību un tuvinājumu; iepazīst "
      "iracionālus skaitļus un aritmētisko kvadrātsakni.",
      [B("Tuvinājumi un mērījuma kļūda", [
          ("Kāpēc mērījums nav precīzs?",
           "Skaidro, ka mērījumos iegūst tuvinājumus, un nosaka "
           "mērinstrumenta iedaļas vērtību."),
          ("Kā pierakstīt mērījuma rezultātu?",
           "Pieraksta mērījuma rezultātu, ievērojot mērījuma kļūdu."),
          ("Cik ciparu atstāt?",
           "Noapaļo skaitli ar norādīto precizitāti un pamato izvēli."),
          ("Kad vajag precīzo vērtību?",
           "Izvērtē, kad situācijā nepieciešama precīza un kad - aptuvena "
           "vērtība."),
          ("Kā kļūda ietekmē rezultātu?",
           "Spriež, kā mērījuma kļūda ietekmē aprēķina rezultātu."),
          ("Kā pārbaudīt starprezultātus?",
           "Seko aprēķinu gaitai un pārbauda starprezultātus ar novērtējumu."),
      ]),
       B("Racionāli un iracionāli skaitļi", [
           ("Kad daļu var pierakstīt kā decimāldaļu?",
            "Pārveido parasto daļu par galīgu vai periodisku decimāldaļu."),
           ("Kas ir periodiska decimāldaļa?",
            "Lasa un pieraksta periodisku decimāldaļu un saista to ar parasto "
            "daļu."),
           ("Kādi skaitļi ir racionāli?",
            "Skaidro, ka racionālu skaitli var pierakstīt kā daļu, un nosaka "
            "skaitļu piederību kopai."),
           ("Kas ir skaitlis pī?",
            "Skaidro, ka riņķa līnijas garuma un diametra dalījums ir "
            "skaitlis pī, un lieto tā tuvinājumu."),
           ("Kādi skaitļi nav racionāli?",
            "Min iracionālu skaitļu piemērus un pamato, ka tos nevar "
            "pierakstīt kā daļu."),
           ("Kā izskatās reālo skaitļu kopa?",
            "Veido pārskatu par skaitļu kopām un to savstarpējo saistību."),
       ]),
       B("Aritmētiskā kvadrātsakne", [
           ("Ko nozīmē vilkt kvadrātsakni?",
            "Skaidro aritmētiskās kvadrātsaknes definīciju un min piemērus."),
           ("Kurus skaitļus var izvilkt precīzi?",
            "Nosaka kvadrātsaknes precīzo vērtību, ja zemsaknes izteiksme ir "
            "pilns kvadrāts."),
           ("Kāda ir aptuvenā vērtība?",
            "Nosaka kvadrātsaknes aptuveno vērtību, izmantojot kvadrātu "
            "tabulu vai kalkulatoru."),
           ("Kur uz skaitļu taisnes atrodas šī sakne?",
            "Atliek uz skaitļu taisnes iracionālu skaitli ar norādīto "
            "precizitāti."),
           ("Kad kvadrātsakne neeksistē?",
            "Skaidro, kāpēc negatīvam skaitlim aritmētiskās kvadrātsaknes "
            "nav."),
           ("Kā atrisināt vienādojumu ar kvadrātu?",
            "Atrisina vienādojumu, kurā nezināmais ir kvadrātā, un pamato "
            "abas saknes."),
           ("Kā salīdzināt saknes?",
            "Salīdzina dažādā veidā pierakstītus reālus skaitļus un sakārto "
            "tos."),
       ]),
       B("Darbības ar kvadrātsaknēm", [
           ("Kā izvilkt sakni no reizinājuma?",
            "Lieto reizinājuma saknes īpašību izteiksmju pārveidojumos."),
           ("Kā izvilkt sakni no daļas?",
            "Lieto dalījuma saknes īpašību un pieraksta rezultātu "
            "vienkāršotā veidā."),
           ("Kā iznest reizinātāju pirms saknes?",
            "Iznes reizinātāju pirms saknes un ienes to zem saknes."),
           ("Kā saskaitīt līdzīgas saknes?",
            "Saskaita un atņem līdzīgas kvadrātsaknes un pamato darbību."),
           ("Kā reizina izteiksmes ar saknēm?",
            "Reizina izteiksmes, kas satur kvadrātsaknes, un vienkāršo "
            "rezultātu."),
           ("Kā pierakstīt algoritmu?",
            "Formulē un pieraksta algoritmu darbību izpildei ar "
            "kvadrātsaknēm."),
       ])],
      "Reāli skaitļi un kvadrātsakne",
      "Pieraksta mērījumu ar kļūdu un noapaļo ar doto precizitāti; nošķir "
      "racionālus un iracionālus skaitļus; nosaka kvadrātsaknes precīzo un "
      "aptuveno vērtību; lieto kvadrātsakņu īpašības pārveidojumos.",
      "saknes ar kāpinātāju; iracionāla skaitļa tuvināšana ar intervāliem."),

    T("8.4.", "Kā aprēķina laukumu jebkuram trijstūrim, riņķim?",
      "Paplašina zināšanas par laukumu; iepazīst prizmu un cilindru un to "
      "virsmas laukumu un tilpumu.",
      [B("Trijstūra laukums", [
          ("Kā no taisnstūra iegūt trijstūra laukumu?",
           "Iegūst trijstūra laukuma formulu, izmantojot taisnstūra laukumu."),
          ("Kurš augstums der?",
           "Zīmē trijstūra augstumus un skaidro, ka laukumu var aprēķināt ar "
           "katru malu un tās augstumu."),
          ("Kā aprēķināt taisnleņķa trijstūra laukumu?",
           "Aprēķina taisnleņķa trijstūra laukumu, lietojot katetes."),
          ("Kā atrast nezināmo augstumu?",
           "Aprēķina trijstūra malu vai augstumu, ja zināms laukums."),
          ("Kā sadalīt sarežģītu figūru?",
           "Sadala figūru trijstūros un taisnstūros un aprēķina tās laukumu."),
          ("Kā izteiksme apraksta laukumu?",
           "Pieraksta figūras laukumu ar algebrisku izteiksmi un vienkāršo "
           "to."),
      ]),
       B("Riņķa laukums", [
           ("Kā rodas riņķa laukuma formula?",
            "Skaidro riņķa laukuma formulu, izmantojot riņķa sadalīšanu "
            "sektoros."),
           ("Precīzi vai aptuveni?",
            "Aprēķina riņķa laukumu precīzi ar skaitli pī un aptuveni ar tā "
            "tuvinājumu."),
           ("Kā atrast rādiusu?",
            "Aprēķina rādiusu vai diametru, ja zināms laukums vai riņķa "
            "līnijas garums."),
           ("Cik liels ir riņķa gredzens?",
            "Aprēķina kombinētas figūras laukumu, kurā ietilpst riņķis."),
           ("Cik liels ir sektors?",
            "Aprēķina riņķa daļas laukumu, izmantojot centra leņķi."),
       ]),
       B("Prizma un cilindrs", [
           ("Kā telpisku ķermeni attēlo plaknē?",
            "Skaidro, kas saglabājas, attēlojot telpisku ķermeni plaknē, un "
            "zīmē prizmu."),
           ("Kas raksturo taisnu prizmu?",
            "Raksturo taisnas prizmas pamatus un sānu skaldnes un zīmē tās "
            "izklājumu."),
           ("Kā zīmē cilindru?",
            "Zīmē cilindru, arī ar digitāliem rīkiem, un raksturo tā "
            "elementus."),
           ("Kāds ķermenis tas ir?",
            "Nosaka iespējamo telpisko ķermeni pēc dažiem tā skatiem."),
           ("Kā izskatās izklājums?",
            "Zīmē prizmas un cilindra virsmas izklājumu pēc dotiem izmēriem."),
       ]),
       B("Virsmas laukums un tilpums", [
           ("Kā aprēķina prizmas virsmas laukumu?",
            "Aprēķina taisnas prizmas virsmas laukumu, izmantojot izklājumu."),
           ("Kā aprēķina cilindra virsmas laukumu?",
            "Aprēķina cilindra virsmas laukumu un skaidro katru saskaitāmo."),
           ("Kā aprēķina tilpumu?",
            "Aprēķina prizmas un cilindra tilpumu, lietojot pamata laukumu un "
            "augstumu."),
           ("Cik daudz ietilpst traukā?",
            "Risina praktisku uzdevumu par tilpumu ar mērvienību "
            "pārveidojumiem."),
       ])],
      "Trijstūra un riņķa laukums; prizma un cilindrs",
      "Aprēķina trijstūra un riņķa laukumu un nezināmos lielumus; sadala "
      "figūru daļās laukuma aprēķināšanai; zīmē prizmu un cilindru un "
      "aprēķina to virsmas laukumu un tilpumu.",
      "sektora laukums; ķermeņi, kas salikti no prizmām un cilindriem."),

    T("8.5.", "Kas kopīgs četrstūriem, kuru pretējās malas ir pa pāriem "
      "paralēlas?",
      "Sistematizē zināšanas par četrstūriem; pēta paralelograma, romba, "
      "taisnstūra un kvadrāta īpašības un pazīmes.",
      [B("Taišņu paralelitātes pazīmes", [
          ("Kad divas taisnes ir paralēlas?",
           "Formulē un lieto taišņu paralelitātes pazīmes."),
          ("Kā pierādīt paralelitāti?",
           "Pierāda divu taišņu paralelitāti, izmantojot leņķu sakarības."),
          ("Kā konstruēt paralēlu taisni?",
           "Ar cirkuli un lineālu konstruē taisni, kas paralēla dotajai."),
          ("Kas ir attālums starp paralēlām taisnēm?",
           "Definē attālumu starp paralēlām taisnēm un mēra to."),
          ("Kā perpendikulitāte dod paralelitāti?",
           "Pamato, ka divas taisnes, kas perpendikulāras trešajai, ir "
           "paralēlas."),
      ]),
       B("Četrstūri un to leņķi", [
           ("Kāda ir četrstūra leņķu summa?",
            "Iegūst četrstūra leņķu summu, izmantojot trijstūra leņķu summu."),
           ("Kā aprēķināt nezināmo leņķi?",
            "Aprēķina četrstūra nezināmos leņķus un pamato risinājumu."),
           ("Kas ir izliekts un ieliekts četrstūris?",
            "Nošķir izliektus un ieliektus četrstūrus un raksturo to "
            "diagonāles."),
           ("Kā klasificēt četrstūrus?",
            "Klasificē četrstūrus pēc paralēlo malu pāru skaita un pēc paša "
            "izvēlētām pazīmēm."),
           ("Kāda ir daudzstūra leņķu summa?",
            "Vispārina leņķu summas aprēķinu daudzstūrim ar n malām."),
       ]),
       B("Paralelograms un tā īpašības", [
           ("Kā definē paralelogramu?",
            "Definē paralelogramu un atpazīst to starp četrstūriem."),
           ("Kādas ir paralelograma īpašības?",
            "Formulē un pierāda paralelograma īpašības par malām un leņķiem."),
           ("Ko dara diagonāles?",
            "Pierāda, ka paralelograma diagonāles krustpunktā dalās uz "
            "pusēm."),
           ("Kad četrstūris ir paralelograms?",
            "Lieto paralelograma pazīmes, lai pamatotu, ka četrstūris ir "
            "paralelograms."),
           ("Kā aprēķināt paralelograma lielumus?",
            "Aprēķina paralelograma malas, leņķus un perimetru."),
           ("Kā aprēķina paralelograma laukumu?",
            "Iegūst un lieto paralelograma laukuma formulu."),
       ]),
       B("Rombs, taisnstūris un kvadrāts", [
           ("Ar ko rombs atšķiras no paralelograma?",
            "Definē rombu un formulē tā papildu īpašības."),
           ("Kā aprēķina romba laukumu?",
            "Lieto romba laukuma formulu ar diagonālēm un ar malu un "
            "augstumu."),
           ("Kādas ir taisnstūra īpašības?",
            "Formulē un pierāda taisnstūra īpašības par diagonālēm."),
           ("Kas kvadrātam ir īpašs?",
            "Raksturo kvadrātu kā rombu un taisnstūri vienlaikus."),
           ("Vai īpašība ir arī pazīme?",
            "Izvērtē, kuras īpašības ir arī pazīmes, un pamato ar "
            "pretpiemēru."),
           ("Kā risināt uzdevumu ar četrstūri?",
            "Risina aprēķinu un pierādījuma uzdevumu, lietojot četrstūru "
            "īpašības."),
       ])],
      "Paralelograms un tā veidi",
      "Lieto taišņu paralelitātes pazīmes un četrstūra leņķu summu; pierāda "
      "un lieto paralelograma, romba, taisnstūra un kvadrāta īpašības un "
      "pazīmes; aprēķina to lielumus un laukumus.",
      "trapeces īpašības; četrstūri koordinātu plaknē."),

    T("8.6.", "Kā skaidro un izpilda darbības ar izteiksmēm?",
      "Pilnveido izpratni par izteiksmēm ar mainīgo: monomi, polinomi un "
      "darbības ar tiem.",
      [B("Monomi", [
          ("Kas ir monoms?",
           "Nosaka, vai izteiksme ir monoms, un nosauc tā koeficientu."),
          ("Kas ir monoma normālforma?",
           "Pārveido monomu normālformā un nosaka tā pakāpi."),
          ("Kā reizina monomus?",
           "Reizina monomus, lietojot pakāpju īpašības."),
          ("Kā kāpina monomu?",
           "Kāpina monomu un pieraksta rezultātu normālformā."),
          ("Kā dala monomus?",
           "Dala monomus un skaidro, kad dalījums ir monoms."),
      ]),
       B("Polinomi un to saskaitīšana", [
           ("Kas ir polinoms?",
            "Nosauc polinoma locekļus; nošķir binomu un trinomu."),
           ("Kā polinomu pieraksta normālformā?",
            "Pārveido polinomu normālformā un nosaka tā pakāpi."),
           ("Kā saskaita polinomus?",
            "Saskaita un atņem polinomus, savelkot līdzīgos locekļus."),
           ("Kā atver iekavas ar mīnusu?",
            "Atver iekavas, pirms kurām ir mīnusa zīme, un pamato zīmju "
            "maiņu."),
           ("Kā aprēķināt polinoma vērtību?",
            "Aprēķina polinoma vērtību dotai mainīgā vērtībai un pārbauda "
            "pārveidojumu."),
       ]),
       B("Polinomu reizināšana", [
           ("Kā reizina polinomu ar monomu?",
            "Reizina polinomu ar monomu un pieraksta rezultātu normālformā."),
           ("Kā reizina divus polinomus?",
            "Reizina divus polinomus un skaidro darbības kārtību."),
           ("Kā to parādīt ģeometriski?",
            "Modelē divu binomu reizinājumu ar taisnstūra laukumu."),
           ("Kā iznest kopīgo reizinātāju?",
            "Sadala polinomu reizinātājos, iznesot kopīgo reizinātāju."),
           ("Kā sagrupēt locekļus?",
            "Sadala polinomu reizinātājos ar grupēšanas paņēmienu."),
       ]),
       B("Izteiksmju lietojums", [
           ("Kā izteiksme apraksta figūru?",
            "Pieraksta ar izteiksmi figūras perimetru, laukumu vai tilpumu un "
            "vienkāršo to."),
           ("Kā pierādīt apgalvojumu par skaitļiem?",
            "Ar algebrisku izteiksmi pamato apgalvojumu par skaitļu "
            "īpašībām."),
           ("Kā vienkāršot garu izteiksmi?",
            "Vienkāršo izteiksmi, lietojot vairākus pārveidojumus pēc "
            "kārtas."),
           ("Kur radusies kļūda?",
            "Atrod kļūdu dotā pārveidojumā un izskaidro tās cēloni."),
           ("Kā izteiksme palīdz atrisināt vienādojumu?",
            "Pārveido izteiksmi, lai atrisinātu vienādojumu vai aprēķinātu "
            "vērtību."),
       ])],
      "Monomi un polinomi",
      "Pārveido monomus un polinomus normālformā; saskaita, atņem un reizina "
      "polinomus; sadala polinomu reizinātājos; lieto izteiksmes figūru "
      "lielumu un skaitļu īpašību aprakstīšanai.",
      "saīsinātās reizināšanas formulas; polinoma dalīšana ar monomu."),

    T("8.7.", "Kā dažādas funkcijas izmanto matemātiskai modelēšanai?",
      "Paplašina izpratni par funkcijām: kvadrātfunkcija, parabola, hiperbola "
      "un grafiku lietojums vienādojumu risināšanā.",
      [B("Kvadrātfunkcija un parabola", [
          ("Kā izskatās funkcijas ar kvadrātu grafiks?",
           "Zīmē funkcijas y = x² grafiku pēc punktiem un raksturo to."),
          ("Kāpēc parabola ir simetriska?",
           "Skaidro grafika simetriju pret y asi, izmantojot funkcijas "
           "formulu."),
          ("Ko maina koeficients pie kvadrāta?",
           "Pēta, kā koeficients maina parabolas platumu un virzienu."),
          ("Kā izskatās virsotne?",
           "Nosaka no grafika parabolas virsotni un funkcijas lielāko vai "
           "mazāko vērtību."),
          ("Kad funkcija aug un kad dilst?",
           "Nosaka no grafika intervālus, kuros funkcija ir augoša vai "
           "dilstoša."),
          ("Kur dzīvē redzam parabolu?",
           "Min piemērus par parabolas formu dabā un tehnikā un raksturo "
           "tos."),
      ]),
       B("Parabolas pārbīde", [
           ("Kas notiek, pieskaitot skaitli?",
            "Pēta funkcijas y = ax² + c grafiku un tā novietojumu."),
           ("Kā zīmēt grafiku pēc punktiem?",
            "Zīmē grafiku, izvēloties piemērotus argumentus un vienības."),
           ("Kur grafiks krusto asis?",
            "Nosaka grafika krustpunktus ar asīm un skaidro to nozīmi."),
           ("Kāds ir funkcijas vērtību apgabals?",
            "Nosaka no grafika funkcijas vērtību apgabalu."),
           ("Kā digitālie rīki palīdz pētīt?",
            "Ar digitāliem rīkiem pēta grafika izmaiņas, mainot "
            "koeficientus."),
       ]),
       B("Apgriezti proporcionāla sakarība", [
           ("Kā izskatās hiperbola?",
            "Zīmē funkcijas grafiku, kas apraksta apgriezti proporcionālus "
            "lielumus."),
           ("Kāpēc grafiks nekrusto asis?",
            "Skaidro, kāpēc mainīgais nevar būt nulle, un raksturo grafika "
            "tuvošanos asīm."),
           ("Kādas ir funkcijas īpašības?",
            "Nosaka no grafika vērtību apgabalu un intervālus, kuros funkcija "
            "dilst."),
           ("Kā sakarība apraksta dzīvi?",
            "Lieto apgriezti proporcionālu sakarību uzdevumā par ātrumu, "
            "laiku vai darba ražīgumu."),
           ("Kura funkcija der šiem datiem?",
            "Izvēlas piemērotu funkciju kā situācijas matemātisko modeli un "
            "pamato izvēli."),
       ]),
       B("Grafiki, vienādojumi un nevienādības", [
           ("Kā no grafika nolasīt vienādojuma saknes?",
            "Nosaka no funkcijas grafika dota vienādojuma saknes."),
           ("Kā no grafika nolasīt nevienādības atrisinājumu?",
            "Nosaka no grafika nevienādības atrisinājumu kopu."),
           ("Kā atrisināt vienādojumu ar kvadrātu?",
            "Atrisina vienādojumu, kas pārveidojams formā x² = t, un pamato "
            "sakņu skaitu."),
           ("Kā atrisināt vienādojumu ar daļu?",
            "Atrisina vienādojumu, kurā nezināmais ir saucējā, un pārbauda "
            "atrisinājumu."),
           ("Kā divi grafiki palīdz salīdzināt?",
            "Salīdzina divas sakarības pēc to grafikiem un formulē "
            "secinājumus."),
       ])],
      "Kvadrātfunkcija, hiperbola un to lietojums",
      "Zīmē un raksturo kvadrātfunkcijas un apgriezti proporcionālas "
      "sakarības grafikus; nosaka virsotni, vērtību apgabalu un monotonitāti; "
      "lieto grafikus vienādojumu un nevienādību risināšanā.",
      "grafiku pārbīde pa abām asīm; funkcijas kā modeļi citās mācību jomās."),

    T("8.8.", "Kā nosaka taisnleņķa trijstūra nezināmās malas garumu?",
      "Pilnveido spriešanas un pierādīšanas prasmes; apgūst Pitagora teorēmu "
      "un tās lietojumu.",
      [B("Taisnleņķa trijstūris", [
          ("Kā sauc taisnleņķa trijstūra malas?",
           "Nosauc katetes un hipotenūzu un saista tās ar leņķiem."),
          ("Kādas ir taisnleņķa trijstūra īpašības?",
           "Lieto leņķu summu taisnleņķa trijstūrī un vienādsānu trijstūra "
           "īpašības."),
          ("Kā konstruēt taisnleņķa trijstūri?",
           "Ar cirkuli un lineālu konstruē taisnleņķa trijstūri pēc dotiem "
           "elementiem."),
          ("Kur taisnleņķa trijstūris slēpjas figūrā?",
           "Saskata taisnleņķa trijstūrus citās figūrās un izmanto tos "
           "aprēķinos."),
          ("Kāds ir katetes pretleņķis?",
           "Lieto sakarību starp 30° leņķi un katetes garumu."),
      ]),
       B("Pitagora teorēma", [
           ("Kā atklāt sakarību starp malām?",
            "Pēta laukumus uz taisnleņķa trijstūra malām un formulē "
            "pieņēmumu."),
           ("Kā pierāda Pitagora teorēmu?",
            "Iepazīst un atstāsta vienu Pitagora teorēmas pierādījumu."),
           ("Kā aprēķināt hipotenūzu?",
            "Aprēķina hipotenūzas garumu, ja zināmas katetes."),
           ("Kā aprēķināt kateti?",
            "Aprēķina katetes garumu, ja zināma hipotenūza un otra katete."),
           ("Kad atbilde ir iracionāla?",
            "Pieraksta rezultātu ar kvadrātsakni un nosaka tā aptuveno "
            "vērtību."),
           ("Vai trijstūris ir taisnleņķa?",
            "Lieto apgriezto teorēmu, lai noteiktu, vai trijstūris ir "
            "taisnleņķa."),
       ]),
       B("Pitagora teorēmas lietojums", [
           ("Cik gara ir diagonāle?",
            "Aprēķina taisnstūra un kvadrāta diagonāli."),
           ("Kā aprēķināt vienādsānu trijstūra augstumu?",
            "Aprēķina vienādsānu un vienādmalu trijstūra augstumu un "
            "laukumu."),
           ("Cik garš ir attālums koordinātu plaknē?",
            "Aprēķina attālumu starp diviem punktiem koordinātu plaknē."),
           ("Cik augstas ir kāpnes?",
            "Risina praktisku uzdevumu par attālumiem un augstumiem."),
           ("Kā izmantot teorēmu telpiskā ķermenī?",
            "Aprēķina taisnstūra paralēlskaldņa diagonāli vai prizmas "
            "elementus."),
           ("Kā plānot risinājumu?",
            "Veido skici, plāno risinājuma soļus un pamato katru aprēķinu."),
       ])],
      "Pitagora teorēma",
      "Lieto taisnleņķa trijstūra īpašības; aprēķina malas garumu ar Pitagora "
      "teorēmu; nosaka, vai trijstūris ir taisnleņķa; lieto teorēmu figūru un "
      "praktisku uzdevumu risināšanā.",
      "Pitagora trijnieki; attālums telpā."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 8. klasē", [
        ("Cik droši rīkojos ar pakāpēm un saknēm?",
         "Formatīvi pārbauda darbības ar pakāpēm, normālformu un "
         "kvadrātsaknēm."),
        ("Ko protu ar polinomiem?",
         "Atkārto polinomu reizināšanu un sadalīšanu reizinātājos."),
        ("Ko protu ģeometrijā?",
         "Atkārto laukumu formulas, četrstūru īpašības un Pitagora teorēmu."),
        ("Ko gaida 9. klasē un eksāmenā?",
         "Apkopo gadā apgūto un iepazīstas ar 9. klases tematiem un eksāmena "
         "prasībām."),
    ]),
]
