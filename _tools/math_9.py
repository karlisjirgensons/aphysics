# -*- coding: utf-8 -*-
"""9. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 9. klases sadaļa.
Mācību gada mērķis ir valsts pārbaudes darbs matemātikā, tāpēc noslēguma
bloks ir gatavošanās eksāmenam (Math/mat_ex.pdf).
"""

from math_plani import B, T

IEVADS = (
    "Devītais matemātikas gads - pamatskolas noslēgums. Ģeometrijā nāk "
    "līdzība, trapece, trigonometriskās sakarības taisnleņķa trijstūrī un "
    "riņķa līnija ar ievilktiem un apvilktiem daudzstūriem. Algebrā - "
    "saīsinātās reizināšanas formulas, kvadrātvienādojums un kvadrātfunkcija, "
    "vienādojumu sistēmas un aritmētiskā progresija. Katrs temats ir arī "
    "eksāmena temats, tāpēc uzdevumi visu gadu tiek risināti eksāmena "
    "formātā, un gads noslēdzas ar mērķtiecīgu gatavošanos eksāmenam.")

TEMATI = [
    T("9.1.", "Kā definē un raksturo līdzīgus trijstūrus?",
      "Veido izpratni par proporcionāliem nogriežņiem, trijstūra viduslīniju "
      "un trijstūru līdzību un lieto tās aprēķinos.",
      [B("Proporcionāli nogriežņi un viduslīnija", [
          ("Kad nogriežņi ir proporcionāli?",
           "Nosaka, vai nogriežņi ir proporcionāli, un pieraksta attiecību."),
          ("Ko dara paralēlas taisnes leņķī?",
           "Nosaka proporcionālus nogriežņus, ja leņķa malas krusto paralēlas "
           "taisnes."),
          ("Kā sadalīt nogriezni vienādās daļās?",
           "Ar cirkuli un lineālu sadala nogriezni vienādās daļās, lietojot "
           "Talesa teorēmu."),
          ("Kas ir trijstūra viduslīnija?",
           "Definē trijstūra viduslīniju un zīmē to."),
          ("Kādas ir viduslīnijas īpašības?",
           "Formulē un pierāda trijstūra viduslīnijas īpašību."),
          ("Kā lietot viduslīniju aprēķinos?",
           "Aprēķina nezināmos lielumus, lietojot viduslīnijas īpašību."),
      ]),
       B("Līdzīgi trijstūri", [
          ("Ko nozīmē «līdzīgi»?",
           "Definē līdzīgus trijstūrus un nosauc atbilstošos elementus."),
          ("Kas ir līdzības koeficients?",
           "Nosaka līdzības koeficientu un skaidro, ko tas parāda."),
          ("Kāda ir līdzības pirmā pazīme?",
           "Formulē un lieto līdzības pazīmi pēc diviem leņķiem."),
          ("Kādas ir pārējās pazīmes?",
           "Formulē un lieto līdzības pazīmes pēc malām un leņķa."),
          ("Kā pamatot, ka trijstūri ir līdzīgi?",
           "Saskata līdzīgus trijstūrus zīmējumā un pamato līdzību ar "
           "pazīmi."),
          ("Kā mainās perimetrs un laukums?",
           "Nosaka līdzīgu trijstūru perimetru un laukumu attiecību."),
       ]),
       B("Līdzības lietojums", [
           ("Kā aprēķināt nezināmo malu?",
            "Aprēķina nezināmus nogriežņus, lietojot līdzīgu trijstūru malu "
            "proporcionalitāti."),
           ("Kā izmērīt koka augstumu?",
            "Risina praktisku uzdevumu par attālumu vai augstumu, lietojot "
            "līdzību."),
           ("Kur kļūdās pierādījums?",
            "Lasa dotu pierādījumu, atrod un skaidro kļūdu tajā."),
           ("Kā līdzība palīdz taisnleņķa trijstūrī?",
            "Lieto līdzību taisnleņķa trijstūrī ar augstumu pret hipotenūzu."),
           ("Kā plānot risinājumu?",
            "Veido skici un plāno risinājuma soļus uzdevumam ar līdzību."),
           ("Kā to risinātu eksāmenā?",
            "Risina eksāmena formāta uzdevumus par līdzību un noformē "
            "risinājumu."),
       ])],
      "Trijstūru līdzība",
      "Nosaka proporcionālus nogriežņus un lieto viduslīnijas īpašību; pamato "
      "trijstūru līdzību ar pazīmēm; lieto līdzības koeficientu, perimetru un "
      "laukumu attiecību nezināmo lielumu aprēķināšanai.",
      "līdzīgu figūru tilpumu attiecība; līdzība koordinātu plaknē."),

    T("9.2.", "Kas kopīgs četrstūriem, kuriem tieši divas malas ir paralēlas?",
      "Sistematizē zināšanas par četrstūriem, definējot trapeci un pētot tās "
      "īpašības, viduslīniju un laukumu.",
      [B("Trapece un tās veidi", [
          ("Kā definē trapeci?",
           "Definē trapeci un nosauc tās pamatus, sānu malas un augstumu."),
          ("Kādi ir trapeču veidi?",
           "Nošķir vienādsānu un taisnleņķa trapeci un raksturo to īpašības."),
          ("Kādi leņķi ir trapecē?",
           "Aprēķina trapeces leņķus, lietojot paralēlu taišņu leņķu "
           "sakarības."),
          ("Kā konstruēt trapeci?",
           "Ar cirkuli un lineālu konstruē trapeci pēc dotiem elementiem."),
          ("Kā pierādīt trapeces īpašību?",
           "Pierāda kādu no vienādsānu trapeces īpašībām vai pazīmēm."),
      ]),
       B("Trapeces viduslīnija", [
           ("Kas ir trapeces viduslīnija?",
            "Definē trapeces viduslīniju un zīmē to."),
           ("Kāda ir sakarība ar pamatiem?",
            "Formulē pieņēmumu par viduslīnijas garumu un pārbauda to ar "
            "mērījumiem."),
           ("Kā to pierādīt?",
            "Pierāda trapeces viduslīnijas īpašību, lietojot trijstūra "
            "viduslīniju."),
           ("Kā aprēķināt pamatu?",
            "Aprēķina trapeces pamatu vai viduslīniju, ja pārējie lielumi "
            "zināmi."),
           ("Kā sadalīt trapeci?",
            "Sadala trapeci trijstūros un taisnstūrī un izmanto to "
            "aprēķinos."),
       ]),
       B("Trapeces laukums", [
           ("Kā rodas trapeces laukuma formula?",
            "Iegūst trapeces laukuma formulu, izmantojot jau zināmo par "
            "laukumu."),
           ("Kā aprēķināt laukumu?",
            "Aprēķina trapeces laukumu un nezināmos lielumus, ja laukums "
            "zināms."),
           ("Kā Pitagora teorēma palīdz trapecē?",
            "Aprēķina trapeces augstumu vai sānu malu, lietojot Pitagora "
            "teorēmu."),
           ("Kā līdzība palīdz trapecē?",
            "Lieto trijstūru līdzību, lai aprēķinātu trapeces nezināmos "
            "lielumus."),
           ("Kā to risinātu eksāmenā?",
            "Risina eksāmena formāta uzdevumu par trapeci un noformē "
            "risinājumu."),
       ]),
       B("Trapece telpiskos ķermeņos", [
           ("Kā izskatās prizma ar trapeces pamatu?",
            "Zīmē taisnu prizmu, kuras pamats ir trapece, un raksturo to."),
           ("Kā aprēķināt virsmas laukumu?",
            "Aprēķina prizmas virsmas laukumu, izmantojot pamata laukumu un "
            "izklājumu."),
           ("Kā aprēķināt tilpumu?",
            "Aprēķina prizmas tilpumu ar trapeces pamatu."),
           ("Kur tādas formas sastopamas?",
            "Risina praktisku uzdevumu par konstrukciju ar trapeces formu."),
       ])],
      "Trapece un tās lielumi",
      "Definē un konstruē trapeci; lieto trapeces un tās viduslīnijas "
      "īpašības; aprēķina trapeces laukumu un nezināmos lielumus; aprēķina "
      "prizmas ar trapeces pamatu virsmas laukumu un tilpumu.",
      "trapeces diagonāļu īpašības; ap trapeci apvilkta riņķa līnija."),

    T("9.3.", "Kā aprēķinos izmanto taisnleņķa trijstūra divu malu attiecību?",
      "Veido izpratni par šaurā leņķa sinusu, kosinusu un tangensu un lieto "
      "tos aprēķinos.",
      [B("Sinuss, kosinuss un tangenss", [
          ("Kāpēc visi trijstūri ar vienādu leņķi ir līdzīgi?",
           "Secina, ka taisnleņķa trijstūri ar vienādu šauro leņķi ir "
           "līdzīgi, un pamato to."),
          ("Ko nozīmē malu attiecība?",
           "Skaidro, ka līdzīgos trijstūros atbilstošo malu attiecība "
           "nemainās."),
          ("Kas ir sinuss?",
           "Definē šaurā leņķa sinusu un pieraksta to zīmējumā."),
          ("Kas ir kosinuss un tangenss?",
           "Definē kosinusu un tangensu un nosaka tos konkrētā trijstūrī."),
          ("Kā noteikt vērtību?",
           "Lieto tabulu vai digitālos rīkus, lai noteiktu sinusa, kosinusa "
           "un tangensa vērtības."),
          ("Kā no vērtības atrast leņķi?",
           "Nosaka leņķa lielumu, ja zināma trigonometriskās sakarības "
           "vērtība."),
      ]),
       B("Īpašie leņķi", [
           ("Kāds ir 30° leņķa sinuss?",
            "Iegūst 30° un 60° leņķu vērtības no vienādmalu trijstūra "
            "īpašībām."),
           ("Kāds ir 45° leņķa sinuss?",
            "Iegūst 45° leņķa vērtības no vienādsānu taisnleņķa trijstūra."),
           ("Kā izveidot atgādni?",
            "Veido pārskatu par īpašo leņķu vērtībām un pārbauda to."),
           ("Kā katete saistās ar hipotenūzu?",
            "Lieto sakarību, ka katete pret 30° ir puse no hipotenūzas."),
           ("Kā pārbaudīt rezultātu?",
            "Pārbauda aprēķinu ar Pitagora teorēmu vai novērtējumu."),
       ]),
       B("Trigonometrija uzdevumos", [
           ("Kā aprēķināt nezināmo malu?",
            "Aprēķina taisnleņķa trijstūra malas, ja dots šaurais leņķis un "
            "viena mala."),
           ("Kā aprēķināt leņķi?",
            "Aprēķina šaurā leņķa lielumu, ja zināmas divas malas."),
           ("Kur figūrā ir taisnleņķa trijstūris?",
            "Saskata taisnleņķa trijstūrus citās figūrās un izmanto tos "
            "aprēķinos."),
           ("Cik stāvs ir nogāzes slīpums?",
            "Risina praktisku uzdevumu par slīpumu, augstumu vai attālumu."),
           ("Kā aprēķināt laukumu ar leņķi?",
            "Aprēķina figūras laukumu, izmantojot trigonometriskās "
            "sakarības."),
           ("Kā to risinātu eksāmenā?",
            "Plāno risinājuma soļus un risina eksāmena formāta uzdevumu."),
       ])],
      "Trigonometriskās sakarības taisnleņķa trijstūrī",
      "Definē un nosaka šaurā leņķa sinusu, kosinusu un tangensu; aprēķina "
      "taisnleņķa trijstūra nezināmās malas un leņķus; lieto īpašo leņķu "
      "vērtības un risina praktiskus uzdevumus.",
      "sinusu teorēma vienkāršos gadījumos; trigonometrija telpiskos "
      "ķermeņos."),

    T("9.4.", "Kā izmanto izteiksmju sadalīšanu reizinātājos?",
      "Pilnveido darbu ar algebriskām izteiksmēm: saīsinātās reizināšanas "
      "formulas un sadalīšana reizinātājos.",
      [B("Sadalīšana reizinātājos", [
          ("Kad izteiksme ir reizinājums?",
           "Nosaka, vai izteiksme ir sadalīta reizinātājos, pēc pēdējās "
           "darbības."),
          ("Kā iznest kopīgo reizinātāju?",
           "Sadala polinomu reizinātājos, iznesot kopīgo reizinātāju, un "
           "skaidro darbību."),
          ("Kā grupēt locekļus?",
           "Sadala polinomu reizinātājos ar grupēšanas paņēmienu."),
          ("Kāpēc sadalīšana noder?",
           "Skaidro, kā sadalīšana reizinātājos palīdz saīsināt daļu vai "
           "atrisināt vienādojumu."),
          ("Kā pārbaudīt sadalījumu?",
           "Pārbauda sadalījumu, atverot iekavas vai ievietojot skaitli."),
      ]),
       B("Saīsinātās reizināšanas formulas", [
           ("Kas notiek, kāpinot binomu?",
            "Iegūst binoma kvadrāta formulu, sareizinot binomu ar sevi."),
           ("Kā to parādīt ar laukumu?",
            "Skaidro binoma kvadrāta formulu, izmantojot kvadrāta laukumu."),
           ("Kāda ir starpības kvadrāta formula?",
            "Formulē un lieto starpības kvadrāta formulu."),
           ("Kas ir kvadrātu starpība?",
            "Formulē un lieto kvadrātu starpības formulu."),
           ("Kā atcerēties formulas?",
            "Veido sev atgādni par formulām un pārbauda tās ar piemēriem."),
           ("Kā formulas paātrina rēķinus?",
            "Lieto formulas skaitliskos aprēķinos un pamato to izdevīgumu."),
       ]),
       B("Formulu lietojums pārveidojumos", [
           ("Kā formulu lasīt abos virzienos?",
            "Lieto formulu gan izteiksmes atvēršanai, gan sadalīšanai "
            "reizinātājos."),
           ("Kā vienkāršot garāku izteiksmi?",
            "Vienkāršo izteiksmi, lietojot vairākas formulas un "
            "pārveidojumus."),
           ("Kā saīsināt algebrisku daļu?",
            "Saīsina algebrisku daļu, sadalot skaitītāju un saucēju "
            "reizinātājos."),
           ("Kā pierādīt apgalvojumu par skaitļiem?",
            "Pamato skaitļu dalāmību vai citu īpašību, izmantojot sadalīšanu "
            "reizinātājos."),
           ("Kur radusies kļūda?",
            "Atrod kļūdu dotā pārveidojumā un izskaidro tās cēloni."),
       ]),
       B("Nepilnie kvadrātvienādojumi", [
           ("Ko nozīmē, ka reizinājums ir nulle?",
            "Secina, ka reizinājums ir nulle tikai tad, ja kāds reizinātājs "
            "ir nulle."),
           ("Kā atrisināt vienādojumu ar iznestu reizinātāju?",
            "Atrisina nepilno kvadrātvienādojumu, sadalot izteiksmi "
            "reizinātājos."),
           ("Kā atrisināt vienādojumu ar kvadrātu starpību?",
            "Atrisina vienādojumu, lietojot kvadrātu starpības formulu."),
           ("Cik sakņu ir vienādojumam?",
            "Nosaka nepilnā kvadrātvienādojuma sakņu skaitu un pamato to."),
           ("Kā to risinātu eksāmenā?",
            "Risina eksāmena formāta uzdevumus par izteiksmju "
            "pārveidojumiem."),
       ])],
      "Saīsinātās reizināšanas formulas un sadalīšana reizinātājos",
      "Sadala polinomu reizinātājos, iznesot kopīgo reizinātāju, grupējot un "
      "lietojot saīsinātās reizināšanas formulas; vienkāršo izteiksmes un "
      "saīsina algebriskas daļas; atrisina nepilnos kvadrātvienādojumus.",
      "kuba summas un starpības formulas; daļveida izteiksmju pārveidojumi."),

    T("9.5.", "Kā skaidro un izmanto formulas darbā ar kvadrātvienādojumu, "
      "kvadrātfunkciju?",
      "Apgūst kvadrātvienādojuma risināšanu ar sakņu formulu un "
      "kvadrātfunkcijas grafika veidošanu; risina kvadrātnevienādības.",
      [B("Kvadrātvienādojums un tā saknes", [
          ("Kas ir kvadrātvienādojums?",
           "Nosaka, vai vienādojums ir kvadrātvienādojums, un nosauc tā "
           "koeficientus."),
          ("Kā atrisināt spriežot?",
           "Atrisina vienkāršu kvadrātvienādojumu, spriežot vai sadalot "
           "reizinātājos."),
          ("Ko rāda grafiks?",
           "Nosaka sakņu skaitu no atbilstošās funkcijas grafika."),
          ("Kas ir kvadrāttrinoms?",
           "Pieraksta kvadrāttrinomu kā binoma kvadrāta un skaitļa summu."),
          ("Kā pārveidot vienādojumu?",
           "Veic ekvivalentus pārveidojumus, lai iegūtu kvadrātvienādojumu "
           "standartformā."),
          ("Kā pārbaudīt sakni?",
           "Pārbauda saknes, ievietojot tās sākotnējā vienādojumā."),
      ]),
       B("Sakņu formula un diskriminants", [
           ("Kas ir diskriminants?",
            "Aprēķina diskriminantu un nosaka sakņu skaitu pēc tā vērtības."),
           ("Kā lietot sakņu formulu?",
            "Atrisina kvadrātvienādojumu ar sakņu formulu un noformē "
            "risinājumu."),
           ("Kad saknes ir iracionālas?",
            "Pieraksta saknes ar kvadrātsakni un nosaka to aptuveno vērtību."),
           ("Kā rīkoties ar daļām vienādojumā?",
            "Atrisina vienādojumu, kurā ir daļas vai iekavas, veicot "
            "pārveidojumus."),
           ("Kā atrisināt vienādojumu ar nezināmo saucējā?",
            "Atrisina vienādojumu ar nezināmo saucējā un pārbauda "
            "atrisinājuma pieļaujamību."),
           ("Kā to risinātu eksāmenā?",
            "Risina eksāmena formāta uzdevumus par kvadrātvienādojumiem."),
       ]),
       B("Kvadrātfunkcijas grafiks", [
           ("Kur atrodas parabolas virsotne?",
            "Aprēķina virsotnes koordinātas un pamato formulu."),
           ("Kas ir funkcijas nulles?",
            "Nosaka funkcijas nulles un saista tās ar vienādojuma saknēm."),
           ("Kā uzzīmēt grafiku?",
            "Zīmē kvadrātfunkcijas grafiku, izmantojot virsotni, nulles un "
            "simetriju."),
           ("Kāda ir funkcijas lielākā vērtība?",
            "Nosaka funkcijas lielāko vai mazāko vērtību un vērtību "
            "apgabalu."),
           ("Kā grafiks palīdz saprast uzdevumu?",
            "Lieto grafika skici, lai raksturotu situāciju vai pārbaudītu "
            "atrisinājumu."),
       ]),
       B("Kvadrātnevienādības un lietojums", [
           ("Kā atrisināt kvadrātnevienādību?",
            "Atrisina kvadrātnevienādību, izmantojot funkcijas grafika "
            "skici."),
           ("Kā pierakstīt atrisinājumu kopu?",
            "Pieraksta atrisinājumu kopu ar nevienādību un attēlo to uz "
            "skaitļu taisnes."),
           ("Kā atrisināt sistēmu?",
            "Atrisina sistēmu, kurā ir lineāra un kvadrātnevienādība."),
           ("Kā uzdevumu pierakstīt ar vienādojumu?",
            "Veido kvadrātvienādojumu situācijas uzdevumam un izvērtē "
            "atrisinājuma jēgu."),
           ("Kur meklēt lielāko vērtību?",
            "Risina praktisku uzdevumu par lielāko laukumu vai mazākajām "
            "izmaksām."),
       ])],
      "Kvadrātvienādojumi un kvadrātfunkcija",
      "Nosaka sakņu skaitu ar diskriminantu un atrisina kvadrātvienādojumu ar "
      "sakņu formulu; zīmē kvadrātfunkcijas grafiku un nosaka tā "
      "raksturlielumus; atrisina kvadrātnevienādības un situāciju uzdevumus.",
      "Vjeta teorēma; kvadrātfunkcijas pieraksts ar virsotnes formu."),

    T("9.6.", "Kā apraksta situācijas ar diviem nezināmiem lielumiem?",
      "Veido izpratni par vienādojumu ar diviem nezināmajiem un vienādojumu "
      "sistēmu, to grafisko un analītisko risināšanu.",
      [B("Vienādojums ar diviem nezināmajiem", [
          ("Kas ir vienādojuma atrisinājums?",
           "Nosaka skaitļu pārus, kas apmierina vienādojumu ar diviem "
           "nezināmajiem."),
          ("Kā atrisinājumus attēlot plaknē?",
           "Attēlo vienādojuma atrisinājumus koordinātu plaknē un raksturo "
           "iegūto līniju."),
          ("Kā no vienādojuma iegūt funkciju?",
           "Izsaka vienu nezināmo ar otru un pieraksta atbilstošo funkciju."),
          ("Kā atrast naturālos atrisinājumus?",
           "Lieto pilno pārlasi, lai atrastu vienādojuma naturālos "
           "atrisinājumus."),
          ("Kā situāciju pierakstīt ar diviem nezināmajiem?",
           "Veido vienādojumu ar diviem nezināmajiem praktiskai situācijai."),
      ]),
       B("Grafiskā risināšana", [
           ("Kas ir vienādojumu sistēma?",
            "Skaidro, ka sistēmas atrisinājums ir abu vienādojumu kopīgais "
            "atrisinājums."),
           ("Kā atrisināt grafiski?",
            "Atrisina lineāru vienādojumu sistēmu grafiski un nolasa "
            "krustpunktu."),
           ("Kad sistēmai nav atrisinājuma?",
            "Analizē gadījumus, kad taisnes ir paralēlas vai sakrīt."),
           ("Cik precīzs ir grafiskais atrisinājums?",
            "Izvērtē grafiskā atrisinājuma precizitāti un pārbauda to "
            "analītiski."),
           ("Kā digitālie rīki palīdz?",
            "Lieto digitālos rīkus sistēmas grafiskajai risināšanai."),
       ]),
       B("Analītiskie paņēmieni", [
           ("Kā risināt ar ievietošanas paņēmienu?",
            "Atrisina sistēmu, izsakot vienu nezināmo un ievietojot to otrā "
            "vienādojumā."),
           ("Kā risināt ar saskaitīšanas paņēmienu?",
            "Atrisina sistēmu, saskaitot vai atņemot vienādojumus."),
           ("Kurš paņēmiens ir ērtāks?",
            "Izvēlas piemērotāko paņēmienu konkrētai sistēmai un pamato "
            "izvēli."),
           ("Kā pārbaudīt atrisinājumu?",
            "Pārbauda atrisinājumu, ievietojot skaitļu pāri abos "
            "vienādojumos."),
           ("Kā atrisināt sarežģītāku sistēmu?",
            "Atrisina sistēmu, kurā vispirms nepieciešami pārveidojumi."),
       ]),
       B("Uzdevumu risināšana ar sistēmu", [
           ("Kā uzdevumu pārtulkot sistēmā?",
            "Veido vienādojumu sistēmu situācijas uzdevumam un skaidro "
            "nezināmos."),
           ("Kā risināt uzdevumu par kustību?",
            "Risina uzdevumu par kustību, veidojot sistēmu."),
           ("Kā risināt uzdevumu par maisījumiem?",
            "Risina uzdevumu par sastāvu vai izmaksām, veidojot sistēmu."),
           ("Vai atrisinājums der situācijai?",
            "Izvērtē atrisinājuma atbilstību reālajai situācijai."),
           ("Kā to risinātu eksāmenā?",
            "Risina eksāmena formāta uzdevumus ar vienādojumu sistēmām."),
       ])],
      "Vienādojumu sistēmas",
      "Nosaka vienādojuma ar diviem nezināmajiem atrisinājumus; atrisina "
      "lineāru sistēmu grafiski un analītiski; veido un atrisina sistēmu "
      "situāciju uzdevumiem un izvērtē atrisinājuma jēgu.",
      "sistēma ar kvadrātvienādojumu; sistēmas ar trim nezināmajiem."),

    T("9.7.", "Kā skaitļu virkni pieraksta ar formulu?",
      "Sistematizē izpratni par skaitļu virkni un apgūst aritmētisko "
      "progresiju un tās formulas.",
      [B("Skaitļu virknes", [
          ("Kas ir skaitļu virkne?",
           "Nosauc virknes locekļus un nosaka to kārtas numuru."),
          ("Kā virkni pieraksta ar formulu?",
           "Aprēķina virknes locekļus, ja dota vispārīgā locekļa formula."),
          ("Kā pieraksta rekurenti?",
           "Aprēķina locekļus, ja dots pirmais loceklis un veids, kā iegūt "
           "nākamo."),
          ("Kāpēc virkne ir funkcija?",
           "Skaidro virkni kā funkciju ar naturāliem argumentiem."),
          ("Kā virkni attēlot grafiski?",
           "Attēlo virkni koordinātu plaknē un raksturo tās uzvedību."),
          ("Kāda ir virknes likumsakarība?",
           "Saskata likumsakarību dotā virknē un pieraksta to ar formulu."),
      ]),
       B("Aritmētiskā progresija", [
           ("Kas ir aritmētiskā progresija?",
            "Definē aritmētisko progresiju un nosaka tās diferenci."),
           ("Kā atrast jebkuru locekli?",
            "Lieto vispārīgā locekļa formulu, lai aprēķinātu doto locekli."),
           ("Kā atrast diferenci un pirmo locekli?",
            "Aprēķina diferenci un pirmo locekli, ja zināmi divi locekļi."),
           ("Kāda ir vidējā locekļa īpašība?",
            "Lieto īpašību, ka katrs loceklis ir kaimiņu vidējais "
            "aritmētiskais."),
           ("Vai skaitlis pieder progresijai?",
            "Nosaka, vai dotais skaitlis ir progresijas loceklis, un pamato "
            "atbildi."),
           ("Kā progresiju attēlot grafiski?",
            "Attēlo aritmētisko progresiju grafiski un saista to ar lineāru "
            "funkciju."),
       ]),
       B("Progresijas summa un lietojums", [
           ("Kā saskaitīt pirmos locekļus?",
            "Iegūst un lieto pirmo n locekļu summas formulu."),
           ("Cik ir visu skaitļu summa no 1 līdz 100?",
            "Aprēķina summu, izmantojot progresijas īpašības, un skaidro "
            "paņēmienu."),
           ("Kā progresija apraksta uzkrājumu?",
            "Risina praktisku uzdevumu par regulāru pieaugumu vai "
            "samazinājumu."),
           ("Kā atrast locekļu skaitu?",
            "Aprēķina locekļu skaitu, ja zināma summa vai pēdējais loceklis."),
           ("Kur vēl sastopamas virknes?",
            "Min piemērus par virknēm dabā un tehnikā un raksturo tās."),
           ("Kā to risinātu eksāmenā?",
            "Risina eksāmena formāta uzdevumus par virknēm un progresiju."),
       ])],
      "Skaitļu virknes un aritmētiskā progresija",
      "Aprēķina virknes locekļus pēc formulas; nosaka aritmētiskās "
      "progresijas diferenci un jebkuru locekli; aprēķina pirmo n locekļu "
      "summu un risina praktiskus uzdevumus.",
      "ģeometriskā progresija; virknes ar rekurentu pierakstu."),

    T("9.8.", "Kā raksturo riņķa līnijas un daudzstūra savstarpējo "
      "novietojumu?",
      "Pēta riņķa līnijas un daudzstūra savstarpējo novietojumu: pieskare, "
      "ievilkti un apvilkti daudzstūri, regulāri daudzstūri.",
      [B("Ap trijstūri apvilkta riņķa līnija", [
          ("Kur atrodas punkts vienādā attālumā no trim punktiem?",
           "Nosaka punkta ģeometrisko vietu un saista to ar "
           "vidusperpendikuliem."),
          ("Kā konstruēt apvilktu riņķa līniju?",
           "Ar cirkuli un lineālu konstruē ap trijstūri apvilktu riņķa "
           "līniju."),
          ("Kur ir centrs taisnleņķa trijstūrim?",
           "Pēta un pamato apvilktās riņķa līnijas centra vietu dažāda veida "
           "trijstūriem."),
          ("Kāpēc trijstūris uz diametra ir taisnleņķa?",
           "Formulē un pierāda apgalvojumu par trijstūri, kas balstās uz "
           "diametra."),
          ("Kā lietot šīs sakarības?",
           "Aprēķina nezināmos lielumus, lietojot apvilktās riņķa līnijas "
           "īpašības."),
      ]),
       B("Leņķi un hordas riņķa līnijā", [
           ("Kas ir centra leņķis un loks?",
            "Nosauc riņķa līnijas elementus un saista centra leņķi ar loku."),
           ("Kas ir ievilktais leņķis?",
            "Definē ievilkto leņķi un formulē tā sakarību ar centra leņķi."),
           ("Kā to pierādīt?",
            "Iepazīst ievilktā leņķa īpašības pierādījumu un atstāsta to."),
           ("Kādi ir ievilktie leņķi uz viena loka?",
            "Lieto īpašību, ka ievilktie leņķi uz viena loka ir vienādi."),
           ("Kā aprēķināt leņķus riņķa līnijā?",
            "Aprēķina nezināmos leņķus, lietojot ievilktā leņķa īpašības."),
           ("Kādas īpašības ir hordai?",
            "Lieto sakarību starp hordu, tās attālumu līdz centram un "
            "rādiusu."),
       ]),
       B("Pieskare un ievilkta riņķa līnija", [
           ("Cik kopīgu punktu var būt taisnei un riņķa līnijai?",
            "Nosaka taisnes un riņķa līnijas savstarpējo novietojumu."),
           ("Kas ir pieskare?",
            "Definē riņķa līnijas pieskari un formulē tās pazīmi un īpašību."),
           ("Kādas ir pieskaru nogriežņu īpašības?",
            "Pierāda, ka no viena punkta vilktie pieskaru nogriežņi ir "
            "vienādi."),
           ("Kā konstruēt ievilktu riņķa līniju?",
            "Konstruē trijstūrī ievilktu riņķa līniju un pamato centra "
            "vietu."),
           ("Kur tas noder dzīvē?",
            "Risina praktisku uzdevumu, kurā izmantotas pieskares vai "
            "ievilktas riņķa līnijas sakarības."),
       ]),
       B("Ievilkti un apvilkti daudzstūri", [
           ("Ap kuriem četrstūriem var apvilkt riņķa līniju?",
            "Pēta un pamato, ap kuriem četrstūriem var apvilkt riņķa līniju."),
           ("Kuros četrstūros var ievilkt riņķa līniju?",
            "Pēta un pamato, kuros četrstūros var ievilkt riņķa līniju."),
           ("Kas ir regulārs daudzstūris?",
            "Definē regulāru daudzstūri un aprēķina tā leņķa lielumu."),
           ("Kādas sakarības ir regulāram daudzstūrim?",
            "Lieto sakarības starp regulāra daudzstūra malu un riņķa līniju "
            "rādiusiem."),
           ("Kā uzzīmēt parketu?",
            "Plāno un veido parketa zīmējumu no regulāriem daudzstūriem un "
            "pamato izvēli."),
       ])],
      "Riņķa līnija, pieskare un daudzstūri",
      "Konstruē ievilktas un apvilktas riņķa līnijas; lieto ievilktā leņķa, "
      "hordas un pieskares īpašības; aprēķina regulāra daudzstūra lielumus un "
      "risina uzdevumus par riņķa līniju un daudzstūri.",
      "riņķa loka garums un sektora laukums; daudzstūru parketi."),
]

NOSLEGUMS = [
    B("Eksāmena saturs un formāts", [
        ("Kas ir eksāmenā?",
         "Iepazīstas ar eksāmena struktūru, laiku, vērtēšanu un atļautajiem "
         "palīglīdzekļiem."),
        ("Kā noformē risinājumu?",
         "Atkārto risinājuma noformēšanas prasības un biežākās punktu "
         "zaudēšanas vietas."),
        ("Kas man vēl jāatkārto?",
         "Veic diagnosticējošu pārbaudi un izveido savu atkārtojamo tematu "
         "sarakstu."),
        ("Kā plānot atkārtošanu?",
         "Sastāda personīgu gatavošanās plānu līdz eksāmenam."),
    ]),
    B("Treniņš eksāmena formātā", [
        ("Cik veikli risinu skaitļu un izteiksmju uzdevumus?",
         "Risina eksāmena formāta uzdevumus par skaitļiem, procentiem un "
         "izteiksmēm."),
        ("Kā risinu vienādojumus un funkcijas?",
         "Risina eksāmena formāta uzdevumus par vienādojumiem, sistēmām un "
         "funkciju grafikiem."),
        ("Kā risinu ģeometrijas uzdevumus?",
         "Risina eksāmena formāta ģeometrijas uzdevumus un noformē "
         "pamatojumu."),
        ("Ko darīt ar laiku eksāmenā?",
         "Risina pilnu darbu laika kontrolē un analizē savas kļūdas."),
    ]),
]
