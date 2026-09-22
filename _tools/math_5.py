# -*- coding: utf-8 -*-
"""5. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 5. klases sadaļa.
"""

from math_plani import B, T

IEVADS = (
    "Piektais matemātikas gads. Naturālie skaitļi sniedzas līdz miljardam, "
    "parādās kāpināšana, pirmskaitļi un skaitļa sadalīšana reizinātājos. "
    "Daļskaitļus tagad saskaita un atņem arī ar dažādiem saucējiem, "
    "decimāldaļas un procenti nāk no cenām, atlaidēm un statistikas, bet "
    "gada beigās sakarības starp lielumiem pirmo reizi tiek zīmētas "
    "koordinātu plaknē.")

TEMATI = [
    T("5.1.", "Kā dažādi pieraksta naturālos skaitļus?",
      "Sistematizē zināšanas par naturālajiem skaitļiem, to pieraksta veidiem "
      "un noapaļošanu; lieto saskaitīšanu un atņemšanu jaunās situācijās.",
      [B("Naturālie skaitļi līdz miljardam", [
          ("Cik tālu sniedzas skaitļi?",
           "Lasa un pieraksta naturālus skaitļus līdz miljardam; skaidro, ko "
           "izsaka katrs cipars."),
          ("Kā skaitli uzrakstīt kā šķiru summu?",
           "Pieraksta skaitli kā šķiru summu un nosauc tā kaimiņus."),
          ("Kādi skaitļi der nosacījumiem?",
           "Uzraksta skaitļu kopu pēc viena vai diviem nosacījumiem un "
           "raksturo to."),
          ("Kas kopīgs divām skaitļu kopām?",
           "Salīdzina divas skaitļu kopas, izmantojot Venna diagrammu."),
          ("Kur skaitlis stāv uz skaitļu taisnes?",
           "Atliek skaitļus uz skaitļu taisnes, izvēloties vienību un sākuma "
           "punktu."),
          ("Kā izskatās laika ass?",
           "Atliek uz laika ass sev nozīmīgus gadskaitļus un nolasa no tās "
           "informāciju."),
      ]),
       B("Citas skaitļu pieraksta sistēmas", [
           ("Kā skaitli uzrakstīt ar diviem simboliem?",
            "Iepazīst bināro pierakstu un mēģina uzrakstīt nākamos skaitļus."),
           ("Kā lasa romiešu ciparus?",
            "Lasa un pieraksta skaitļus ar romiešu cipariem."),
           ("Kad ciparus saskaita un kad atņem?",
            "Lieto romiešu ciparu pieraksta likumus un pārbauda savu "
            "pierakstu."),
           ("Kas atšķir decimālo sistēmu no romiešu?",
            "Salīdzina decimālo, bināro un romiešu pierakstu un formulē "
            "atšķirības."),
           ("Kā lasīt svešu šifru?",
            "Jaunā pieraksta sistēmā (piemēram, ēģiptiešu) veido spriedumus "
            "par skaitļu īpašībām."),
       ]),
       B("Skaitļu noapaļošana", [
           ("Kad precīzs skaitlis nav vajadzīgs?",
            "Izvērtē, vai situācijā vajadzīga precīza vai aptuvena vērtība."),
           ("Kā pārstāstīt tekstu ar lieliem skaitļiem?",
            "Atstāsta autentisku tekstu, lietojot skaitļu aptuvenās "
            "vērtības."),
           ("Kā noapaļo līdz simtiem un tūkstošiem?",
            "Noapaļo naturālus skaitļus līdz noteiktai šķirai un skaidro "
            "kārtulu."),
           ("Kā noapaļošanu pierakstīt kā algoritmu?",
            "Pieraksta noapaļošanu kā sazarotu algoritmu un pārbauda to."),
           ("Kuri skaitļi noapaļojas līdz šim?",
            "Nosauc skaitļus, kurus noapaļojot iegūst doto skaitli, un norāda "
            "šķiru."),
       ]),
       B("Saskaitīšana un atņemšana jaunās situācijās", [
           ("Kā saskatīt sakarību summā?",
            "Saskata sakarības starp saskaitāmajiem un aprēķina vairāku "
            "saskaitāmo summu racionāli."),
           ("Kā aizpildīt maģisko kvadrātu?",
            "Papildina skaitļu sakārtojumus (maģisko kvadrātu, skaitļu "
            "trijstūri) pēc dotiem nosacījumiem."),
           ("Kādi ir abi skaitļi?",
            "Veido shematisku zīmējumu situācijai, kurā zināma divu skaitļu "
            "summa un starpība."),
           ("Ko var un ko nevar aprēķināt?",
            "Lasa situācijas aprakstu bez jautājuma un spriež, ko var "
            "aprēķināt."),
           ("Kā pierakstīt nezināmo ar burtu?",
            "Nosaka nezināmo skaitli vienādībā, apzīmējot to ar burtu, un "
            "pieraksta atbildi."),
           ("Kā mainās summa un starpība?",
            "Formulē vispārinājumus par summas un starpības izmaiņām, mainot "
            "darbību locekļus."),
       ])],
      "Naturālie skaitļi, noapaļošana, saskaitīšana un atņemšana",
      "Lasa un pieraksta naturālus skaitļus līdz miljardam, arī ar romiešu "
      "cipariem; noapaļo līdz noteiktai šķirai; racionāli aprēķina summas; "
      "nosaka nezināmo vienādībā.",
      "binārais pieraksts; skaitļu sakārtojumi ar diviem nosacījumiem."),

    T("5.2.", "Kā lieto skaitļa sadalīšanu reizinātājos?",
      "Lieto darbību īpašības un sadalīšanu reizinātājos; iepazīst "
      "pirmskaitļus, dalītājus, dalāmos un kāpināšanu.",
      [B("Darbību īpašības aprēķinos", [
          ("Kurš paņēmiens ir racionālāks?",
           "Salīdzina dažādus reizināšanas un dalīšanas paņēmienus un izvēlas "
           "sev piemērotāko."),
          ("Vai vienādība ir patiesa?",
           "Nosaka vienādību patiesumu (36 : 4 · 9 un 36 : (4 · 9)) un "
           "formulē vispārinājumu."),
          ("Kā izteiksmi padarīt vienkāršāku?",
           "Aprēķina izteiksmes vērtību, lietojot sadalāmības īpašību "
           "b · a + c · a = (b + c) · a."),
          ("Vai dalīšanai ir tāda pati īpašība?",
           "Lieto īpašību b : a + c : a = (b + c) : a un skaidro tās "
           "lietojumu."),
          ("Kā pierakstīt nezināmo reizinājumā?",
           "Aprēķina nezināmo skaitli reizinājuma vai dalījuma vienādībā, "
           "apzīmējot to ar burtu."),
          ("Kura izteiksme ir lielāka?",
           "Salīdzina izteiksmju vērtības spriežot, neaprēķinot tās precīzi."),
      ]),
       B("Sadalīšana reizinātājos", [
           ("Cik dažādi var sadalīt šokolādi?",
            "Skaidro objekta sadalīšanu vienādās daļās un pieraksta to ar "
            "reizinājumu."),
           ("Cik veidos skaitli var uzrakstīt kā reizinājumu?",
            "Izsaka doto skaitli kā divu, trīs vai vairāku skaitļu "
            "reizinājumu."),
           ("Kas ir pirmskaitlis?",
            "Nošķir pirmskaitļus un saliktus skaitļus; skaidro, kāpēc 1 nav "
            "neviens no tiem."),
           ("Kā atrast pirmskaitļus?",
            "Meklē un pieraksta pirmskaitļus, izmantojot dalāmības pārbaudi "
            "vai kalkulatoru."),
           ("Kā sadalīt pirmreizinātājos?",
            "Sadala skaitli pirmreizinātājos un pieraksta rezultātu."),
           ("Ko par skaitli pasaka tā reizinātāji?",
            "Formulē skaitļa īpašības pēc tā sadalījuma pirmreizinātājos."),
       ]),
       B("Dalītāji un dalāmie", [
           ("Kā atrast visus dalītājus?",
            "Nosaka visus skaitļa dalītājus, izmantojot sadalījumu "
            "pirmreizinātājos."),
           ("Kā izveidot skaitli, kas dalās?",
            "Veido skaitļus, kas dalās ar doto skaitli, un skaidro savu "
            "paņēmienu."),
           ("Kas ir kopīgais dalāmais?",
            "Nosaka divu un trīs skaitļu kopīgos dalāmos."),
           ("Kā atrast mazāko kopīgo dalāmo?",
            "Nosaka mazāko kopīgo dalāmo ar diviem paņēmieniem un salīdzina "
            "tos."),
           ("Kad autobusi atkal satiksies?",
            "Lieto mazāko kopīgo dalāmo sadzīves uzdevumā par ciklisku "
            "darbību sakritību."),
           ("Kā sagrupēt skaitļus Venna diagrammā?",
            "Grupē skaitļus pēc dalāmības pazīmēm un attēlo tos Venna "
            "diagrammā."),
       ]),
       B("Kāpināšana", [
           ("Kā saīsināt vienādu reizinātāju reizinājumu?",
            "Pieraksta vienādu reizinātāju reizinājumu kā pakāpi un izlasa "
            "to."),
           ("Kas ir bāze un kas - kāpinātājs?",
            "Nosauc pakāpes elementus un veido izteiksmes pēc apraksta."),
           ("Kāpēc reizinājumu sauc par kvadrātu?",
            "Skaidro, kāpēc divu vienādu skaitļu reizinājumu sauc par skaitļa "
            "kvadrātu."),
           ("Kur kāpināšana stāv darbību secībā?",
            "Nosaka darbību secību izteiksmē, kas satur kāpināšanu un "
            "iekavas."),
           ("Kā aprēķināt garu izteiksmi?",
            "Aprēķina izteiksmes vērtību ar līdz četrām darbībām un pārbauda "
            "to ar kalkulatoru."),
           ("Kā mainās reizinājums, mainot reizinātāju?",
            "Raksturo, kā mainās reizinājums un dalījums, mainot kādu "
            "darbības locekli."),
       ])],
      "Reizinātāji, dalītāji, pirmskaitļi un kāpināšana",
      "Sadala skaitli reizinātājos un pirmreizinātājos; nosaka dalītājus, "
      "dalāmos un mazāko kopīgo dalāmo; kāpina naturālus skaitļus; lieto "
      "darbību īpašības aprēķinos.",
      "lielākais kopīgais dalītājs; dalāmības pazīmes ar 7 un 11."),

    T("5.3.", "Kā skaidro un lieto daļas pamatīpašību?",
      "Veido izpratni par daļas pamatīpašību un lieto to daļu salīdzināšanai, "
      "saskaitīšanai un atņemšanai.",
      [B("Daļas pamatīpašība", [
          ("Vai divas dažādi pierakstītas daļas var būt vienādas?",
           "Ar modeli un zīmējumu parāda, ka dažādi pierakstītām daļām var "
           "būt vienāda vērtība."),
          ("Kā to pierakstīt kā vienādību?",
           "Pieraksta secinājumu par vienādām daļām kā vienādību un skaidro "
           "to."),
          ("Kas notiek, ja skaitītāju un saucēju reizina?",
           "Formulē daļas pamatīpašību un pamato to ar modeli."),
          ("Kā izskatās divas skaitļu taisnes?",
           "Atliek daļas ar dažādiem saucējiem uz divām skaitļu taisnēm un "
           "formulē secinājumu."),
          ("Kā daļas atlikt uz vienas taisnes?",
           "Plāno, kā uz vienas skaitļu taisnes atlikt daļas ar dažādiem "
           "saucējiem."),
          ("Kā daļu pierakstīt citādi bez modeļa?",
           "Formulē ieteikumus, kā daļu pierakstīt ar citu saucēju, "
           "nelietojot modeli."),
      ]),
       B("Saīsināšana un paplašināšana", [
           ("Ko nozīmē paplašināt daļu?",
            "Paplašina daļu, ievērojot nosacījumu par skaitītāju vai "
            "saucēju."),
           ("Ko nozīmē saīsināt daļu?",
            "Saīsina daļu un pārbauda, vai iegūta nesaīsināma daļa."),
           ("Pa soļiem vai uzreiz?",
            "Saīsina daļas ar divciparu un trīsciparu skaitļiem, izvēloties "
            "sev piemērotu paņēmienu."),
           ("Kā izskatās pareizs pieraksts?",
            "Veido pierakstu, kurā redzams reizinājums vai dalījums gan "
            "skaitītājam, gan saucējam."),
           ("Kad starprezultātu nesaīsina?",
            "Spriež, kad izdevīgi starprezultātu atstāt nesaīsinātu, un "
            "pamato savu izvēli."),
       ]),
       B("Daļu salīdzināšana", [
           ("Kā salīdzināt daļas ar dažādiem saucējiem?",
            "Salīdzina divas daļas, vienādojot saucējus, un skaidro "
            "darbības."),
           ("Vairāk vai mazāk nekā puse?",
            "Galvā salīdzina daļas ar pusi un skaidro savu spriedumu."),
           ("Kura daļa ir tuvāk vieniniekam?",
            "Nosaka, kura no divām daļām atrodas tuvāk skaitlim 1, un pamato "
            "atbildi."),
           ("Kā sakārtot vairākas daļas?",
            "Sakārto trīs vai četras daļas augošā vai dilstošā secībā."),
           ("Kāda daļa ir starp divām dotajām?",
            "Nosauc daļu, kas uz skaitļu taisnes atrodas starp divām "
            "dotajām."),
       ]),
       B("Saskaitīšana un atņemšana ar dažādiem saucējiem", [
           ("Kas ir kopsaucējs?",
            "Nosaka divu daļu kopsaucēju un skaidro savu izvēli."),
           ("Kā saskaitīt daļas ar dažādiem saucējiem?",
            "Saskaita daļas ar dažādiem saucējiem, veidojot pierakstu, kurā "
            "redzama pamatīpašība."),
           ("Kā atņemt daļas?",
            "Atņem daļas ar dažādiem saucējiem un, ja vajag, saīsina "
            "rezultātu."),
           ("Kā papildināt līdz vienam?",
            "Atņem daļu no viena un papildina daļu līdz vienam, skaidrojot ar "
            "zīmējumu."),
           ("Kur šeit var kļūdīties?",
            "Analizē tipiskas kļūdas daļu saskaitīšanā un formulē, kā no tām "
            "izvairīties."),
           ("Ko nozīmē dalīt daļu?",
            "Modelē pamatdaļas dalīšanu ar veselu skaitli un vesela skaitļa "
            "dalīšanu ar pamatdaļu."),
       ])],
      "Daļas pamatīpašība un darbības ar daļām",
      "Saīsina un paplašina daļas; salīdzina daļas ar dažādiem saucējiem; "
      "saskaita un atņem daļas ar dažādiem saucējiem; modelē daļas dalīšanu "
      "ar veselu skaitli.",
      "daļu virknes ar mainīgu soli; daļas dalīšana ar daļu modelī."),

    T("5.4.", "Kā vienu skaitli izsaka kā otra skaitļa daļu?",
      "Padziļina daļu lietojumu reālos kontekstos; daļu izmanto "
      "salīdzināšanai un notikuma iespējamības raksturošanai.",
      [B("Daļas un veselā skaitliskā vērtība", [
          ("Kas ir daļa un kas - tās vērtība?",
           "Nošķir lielumus, kas raksturo daļu, no tiem, kas raksturo daļas "
           "skaitlisko vērtību."),
          ("Cik ir trīs ceturtdaļas kilograma?",
           "Nosaka daļu no garuma, masas un laika vienībām un pieraksta "
           "rezultātu."),
          ("Kā pierakstīt aprēķinu?",
           "Aprēķina daļas skaitlisko vērtību, pierakstot to pa darbībām un "
           "ar izteiksmi."),
          ("Cik bija sākumā?",
           "Aprēķina veselo, ja zināma tā daļas vērtība, izmantojot paņēmienu "
           "«spriežu no beigām»."),
          ("Kā uzzīmēt visu nogriezni?",
           "Uzzīmē visu nogriezni, ja dota tā noteikta daļa."),
          ("Kā attēlot trīs sastāvdaļas?",
           "Veido shematisku zīmējumu situācijai, kurā ar daļām raksturotas "
           "vairākas sastāvdaļas."),
      ]),
       B("Viens skaitlis kā otra skaitļa daļa", [
           ("Ko stāsta produkta sastāvs?",
            "Lasa autentisku tekstu ar masas datiem un skaidro, ko no tā var "
            "uzzināt."),
           ("Kā salīdzināt divas ģimenes izdevumus?",
            "Salīdzina situācijas, kurās veselie ir dažādi, izsakot vienu "
            "lielumu kā otra daļu."),
           ("Kā pieraksta «a pret b»?",
            "Pieraksta, ka viens skaitlis ir otra daļa, dažādos veidos."),
           ("Cik precīzi metieni?",
            "Izsaka vienu lielumu kā otra daļu sporta datos un formulē "
            "secinājumu."),
           ("Kā zīmējums palīdz?",
            "Veido shematisku zīmējumu, lai attēlotu vienu skaitli kā otra "
            "skaitļa daļu."),
           ("Kā atrisināt uzdevumu ar daļām?",
            "Risina situāciju uzdevumu, lietojot prasmi izteikt vienu skaitli "
            "kā otra daļu."),
       ]),
       B("Daļa kā dalījums un iespējamība", [
           ("Kā daļu pierakstīt kā dalījumu?",
            "Ilustrē ar piemēriem, ka dalījumu var pierakstīt kā daļu un "
            "otrādi."),
           ("Kad dalījums ir mazāks nekā viens?",
            "Skaidro, kādās situācijās dalīšanas rezultāts ir mazāks, vienāds "
            "vai lielāks nekā 1."),
           ("Kad daļa ir vesels skaitlis?",
            "Nosaka daļas vērtību, kas izsakāma kā vesels skaitlis, un "
            "pieraksta veselu skaitli kā daļu."),
           ("Cik bieži uzkrīt ģerbonis?",
            "Modelē vienādi iespējamus notikumus, apkopo datus un raksturo "
            "biežumu ar daļu."),
           ("Kā daļa raksturo iespējamību?",
            "Skaitliski raksturo notikuma iespējamību, lietojot daļu, un "
            "formulē secinājumu."),
           ("Kur vēl noder daļu rēķini?",
            "Atlasa un veido sadzīves piemērus, kuros daļu rēķinus lieto "
            "līdzīgi."),
       ])],
      "Daļa no veselā un viens skaitlis kā otra daļa",
      "Aprēķina daļas vērtību un veselo; izsaka vienu skaitli kā otra skaitļa "
      "daļu; pieraksta daļu kā dalījumu; ar daļu raksturo notikuma "
      "iespējamību.",
      "iespējamības salīdzināšana divās situācijās; daļas no daļas rēķini."),

    T("5.5.", "Kā saskaita un atņem jauktus skaitļus?",
      "Apgūst jauktu skaitļu pierakstu, salīdzināšanu, saskaitīšanu un "
      "atņemšanu un lieto tos praktiskos kontekstos.",
      [B("Jaukti skaitļi", [
          ("Kas ir jaukts skaitlis?",
           "Skaidro jauktu skaitli kā vesela skaitļa un īstas daļas summu."),
          ("Kā neīstu daļu pārvērst jauktā skaitlī?",
           "Pārveido neīstu daļu par jauktu skaitli, izmantojot dalīšanu ar "
           "atlikumu."),
          ("Kā jauktu skaitli pārvērst neīstā daļā?",
           "Pārveido jauktu skaitli par neīstu daļu un pārbauda rezultātu."),
          ("Kur uz skaitļu taisnes ir jaukts skaitlis?",
           "Atliek jauktus skaitļus uz skaitļu taisnes, arī veidojot to "
           "pats."),
          ("Kurš jauktais skaitlis lielāks?",
           "Salīdzina jauktus skaitļus un pamato salīdzinājumu."),
          ("Kā aug jauktu skaitļu virkne?",
           "Veido jauktu skaitļu virkni pēc dota nosacījuma un turpina to."),
      ]),
       B("Darbības ar vienādiem saucējiem", [
           ("Kā saskaitīt jauktus skaitļus?",
            "Saskaita jauktus skaitļus ar vienādiem saucējiem un rezultātu, "
            "ja vajag, saīsina."),
           ("Kā atņemt no vesela skaitļa?",
            "Galvā atņem daļu no viena vai cita vesela skaitļa."),
           ("Ko darīt, ja daļa ir par mazu?",
            "Atņem jauktus skaitļus, pārveidojot mazināmā veselo par daļu, un "
            "skaidro pierakstu."),
           ("Cik apmēram būs starpība?",
            "Novērtē starpības aptuveno vērtību pirms aprēķina un pamato "
            "spriedumu."),
           ("Kurš skaitlis trūkst vienādībā?",
            "Nosaka nezināmo vienādībā ar jauktiem skaitļiem un veido "
            "pierakstu."),
       ]),
       B("Darbības ar dažādiem saucējiem", [
           ("Kā plānot darbību izpildi?",
            "Pirms aprēķina apraksta, ko un kādā secībā darīs ar jauktiem "
            "skaitļiem."),
           ("Kā saskaitīt, ja saucēji atšķiras?",
            "Saskaita jauktus skaitļus ar dažādiem saucējiem, veidojot "
            "skaidru pierakstu."),
           ("Kurš atņemšanas paņēmiens ērtāks?",
            "Atņem jauktus skaitļus ar dažādiem saucējiem, izvēloties "
            "piemērotu paņēmienu."),
           ("Kā izmantot jauktus skaitļus dzīvē?",
            "Risina situāciju uzdevumu ar jauktiem skaitļiem un mērvienībām "
            "(līdz 3 darbībām)."),
           ("Kā aizpildīt skaitļu trijstūri?",
            "Papildina skaitļu sakārtojumu ar daļām un jauktiem skaitļiem pēc "
            "dotiem nosacījumiem."),
       ])],
      "Jaukti skaitļi",
      "Pārveido neīstu daļu par jauktu skaitli un otrādi; salīdzina jauktus "
      "skaitļus; saskaita un atņem tos ar vienādiem un dažādiem saucējiem; "
      "risina uzdevumus ar jauktiem skaitļiem.",
      "izteiksmes ar trim darbībām un iekavām; virknes ar jauktiem "
      "skaitļiem."),

    T("5.6.", "Kā nosaka figūru nezināmos lielumus?",
      "Pilnveido figūru zīmēšanu un raksturošanu; nosaka nezināmus leņķus, "
      "riņķa līnijas garumu un kombinētu figūru laukumus.",
      [B("Leņķis kā citu leņķu summa", [
          ("Kāds leņķis ir lielāks nekā plats?",
           "Raksturo izstieptu, pilnu un atvērtu leņķi un to lielumu grādos."),
          ("Kā sadalīt izstieptu leņķi?",
           "Ar staru sadala izstieptu leņķi un aprēķina otra leņķa lielumu."),
          ("Kādas sakarības veido vairāki stari?",
           "Formulē sakarības starp leņķiem, ko veido trīs vai četri stari ar "
           "kopīgu sākumpunktu."),
          ("Kā pierakstīt leņķa aprēķinu?",
           "Pieraksta leņķa lieluma aprēķināšanu, lietojot pieņemtos "
           "apzīmējumus."),
          ("Kāda daļa no pilna leņķa?",
           "Nosaka daļu no izstiepta un pilna leņķa un formulē sakarības."),
          ("Vai apgalvojums par leņķiem ir patiess?",
           "Nosaka apgalvojuma par leņķu lielumiem patiesumu un pamato to."),
      ]),
       B("Riņķa līnija un tās garums", [
           ("Kas nosaka riņķa līniju?",
            "Skaidro, ka riņķa līniju nosaka rādiuss; zīmē riņķa līniju ar "
            "dotu rādiusu vai diametru."),
           ("Kā izmērīt riņķa līnijas garumu?",
            "Praktiski nosaka riņķa līnijas garumu un pieraksta mērījumus "
            "tabulā."),
           ("Cik reižu rādiuss ietilpst riņķa līnijā?",
            "Formulē sakarību starp rādiusu un riņķa līnijas garumu."),
           ("Cik garš loks vajadzīgs grozam?",
            "Lieto sakarību praktiskā uzdevumā, atrodot vajadzīgos datus."),
           ("Kā ar cirkuli atlikt vienādus nogriežņus?",
            "Ar cirkuli konstruē nogriezni, kas vienāds ar doto vai vairākas "
            "reizes garāks."),
           ("Kādu rakstu var uzzīmēt ar cirkuli?",
            "Veido simetrisku zīmējumu, lietojot riņķa līnijas ar kopīgu "
            "centru un riņķa dalīšanu."),
       ]),
       B("Daudzstūru īpašības", [
           ("Kāds daudzstūris atbilst nosacījumiem?",
            "Zīmē daudzstūri pēc diviem vai trim nosacījumiem par malām un "
            "leņķiem."),
           ("Vai diagonāles vienmēr krustojas?",
            "Pēta, vai nogriežņi, kas savieno četrstūra pretējās virsotnes, "
            "vienmēr krustojas."),
           ("Kāds leņķis var būt lielāks nekā izstiepts?",
            "Raksturo ieliekta četrstūra īpašības un tā leņķus."),
           ("Kā raksturot cita uzzīmēto figūru?",
            "Pārī raksturo klasesbiedra uzzīmēta daudzstūra īpašības."),
           ("Vai apgalvojums par figūrām ir patiess?",
            "Nosaka un pamato apgalvojumu par daudzstūru lielumiem "
            "patiesumu."),
       ]),
       B("Kombinētu figūru laukums", [
           ("Kā rēķināt, ja malas dotas dažādās vienībās?",
            "Aprēķina taisnstūra laukumu, pārveidojot malu garumus vienādās "
            "mērvienībās."),
           ("Kā sadalīt kombinētu figūru?",
            "Sadala kombinētu figūru taisnstūros un taisnleņķa trijstūros."),
           ("Kā atrast nezināmo malu?",
            "Aprēķina kombinētas figūras nezināmo malu garumus, saskaitot vai "
            "atņemot zināmos."),
           ("Cik liels ir figūras laukums?",
            "Aprēķina kombinētas figūras laukumu un skaidro savu plānu."),
           ("Kā uzzīmēt figūru ar dotu laukumu?",
            "Zīmē rūtiņu lapā daudzstūri ar dotu laukumu un dotām malu "
            "īpašībām."),
       ])],
      "Leņķi, riņķa līnija un figūru laukumi",
      "Nosaka un aprēķina leņķu lielumus; zīmē riņķa līniju un aprēķina tās "
      "garumu; zīmē daudzstūrus pēc nosacījumiem; aprēķina kombinētas figūras "
      "laukumu.",
      "riņķa laukums; figūru pārveidošana ar griešanu un savietošanu."),

    T("5.7.", "Kā lieto decimāldaļas un procentus?",
      "Paplašina prasmes darbā ar decimāldaļām, ievieš procentus un sektoru "
      "diagrammu; aprēķina aritmētisko vidējo.",
      [B("Decimāldaļas un to salīdzināšana", [
          ("Kā parasto daļu pieraksta ar komatu?",
           "Pieraksta daļu ar saucēju 10, 100 vai 1000 kā decimāldaļu un "
           "otrādi."),
          ("Kāds ir decimāldaļas decimālais sastāvs?",
           "Skaidro decimāldaļas sastāvu un pieraksta to kā summu "
           "(3,12 = 3 + 0,1 + 0,02)."),
          ("Ko nozīmē paplašināt decimāldaļu?",
           "Skaidro decimāldaļas paplašināšanu un lieto to salīdzināšanai."),
          ("Kā parasto daļu pārvērst decimāldaļā?",
           "Lieto daļas pamatīpašību, lai daļu ar saucēju 2, 4, 5, 20, 25 vai "
           "50 pierakstītu kā decimāldaļu."),
          ("Kur uz skaitļu taisnes ir 0,7?",
           "Attēlo decimāldaļas uz skaitļu taisnes, izvēloties soli un sākuma "
           "punktu."),
          ("Kurš skaitlis ir lielāks?",
           "Salīdzina decimāldaļas līdz tūkstošdaļām un skaidro, kā sprieda."),
      ]),
       B("Decimāldaļu saskaitīšana un atņemšana", [
           ("Kā saskaitīt galvā?",
            "Saskaita divas decimāldaļas galvā ar vienu ciparu aiz komata un "
            "skaidro domu gaitu."),
           ("Kā saskaitīt rakstos?",
            "Saskaita decimāldaļas, rakstot vienas šķiras ciparus vienu zem "
            "otra."),
           ("Kā atņemt, ja ciparu skaits atšķiras?",
            "Aprēķina starpību, lietojot decimāldaļas paplašināšanu "
            "(3,6 − 1,57)."),
           ("Cik apmēram sanāks?",
            "Novērtē rezultāta aptuveno vērtību, salīdzinot ar veselu "
            "skaitli."),
           ("Kā pārbaudīt atņemšanu?",
            "Pārbauda starpību ar saskaitīšanu un komentē iespējamās kļūdas."),
           ("Kur dzīvē rēķina ar decimāldaļām?",
            "Lieto decimāldaļu saskaitīšanu un atņemšanu izdevumu un "
            "perimetra aprēķinos."),
       ]),
       B("Procenti", [
           ("Ko nozīmē procents?",
            "Skaidro, ka procents ir viena simtdaļa, un modelē procentus "
            "simta kvadrātā."),
           ("Kā procentus pierakstīt kā daļu?",
            "Pieraksta procentus kā parasto daļu un kā decimāldaļu."),
           ("Kā decimāldaļu izteikt procentos?",
            "Pieraksta decimāldaļu līdz simtdaļām kā procentus."),
           ("Puse vai 50 %?",
            "Salīdzina biežāk lietotās daļas un procentus un lieto tos "
            "sinonīmiski."),
           ("Kā aprēķināt procentus no skaitļa?",
            "Aprēķina procentus no veselā, veidojot shematisku zīmējumu."),
           ("Cik bija sākumā, ja zināmi procenti?",
            "Aprēķina veselo, ja zināma procentu skaitliskā vērtība."),
           ("Vai procentus var salīdzināt?",
            "Spriež par procentu salīdzināšanu, ja veselie ir dažādi "
            "lielumi."),
       ]),
       B("Sektoru diagramma un aritmētiskais vidējais", [
           ("Kā izskatās 25 % riņķī?",
            "Uzskicē riņķi ar sadalījumu 25 %, 50 % un 75 % un skaidro "
            "spriedumu."),
           ("Cik grādu ir sektoram?",
            "Aprēķina sektoru leņķu lielumus, izmantojot zināšanas par "
            "leņķiem."),
           ("Kā uzzīmēt sektoru diagrammu?",
            "Zīmē sektoru diagrammu ar transportieri un ar digitāliem "
            "rīkiem."),
           ("Ko diagramma stāsta un ko ne?",
            "Nolasa informāciju no sektoru diagrammas un formulē secinājumus; "
            "atrod kļūdas attēlojumos."),
           ("Kad aritmētiskais vidējais maldina?",
            "Aprēķina aritmētisko vidējo un argumentē, kad tas raksturo datus "
            "atbilstoši."),
       ])],
      "Decimāldaļas, procenti un datu attēlošana",
      "Pieraksta un salīdzina decimāldaļas; saskaita un atņem tās; pieraksta "
      "procentus kā daļu; aprēķina procentus no veselā un veselo; veido un "
      "lasa sektoru diagrammu; aprēķina aritmētisko vidējo.",
      "procentu izmaiņas; datu apkopošana ar digitāliem rīkiem."),

    T("5.8.", "Kā vizuāli attēlo sakarību starp lielumiem?",
      "Veido izpratni par sakarības grafisko attēlu koordinātu plaknē un "
      "mācās no tā nolasīt un secināt.",
      [B("Koordinātu plakne", [
          ("Kā atliek punktu koordinātu plaknē?",
           "Atliek un nolasa punktus koordinātu plaknē, ievērojot izvēlēto "
           "vienību."),
          ("Kā izvēlēties vienību uz ass?",
           "Izvēlas asu vienības atbilstoši lielumu skaitliskajām vērtībām."),
          ("Punkti vai līnija?",
           "Argumentē, kad sakarības attēls ir atsevišķi punkti un kad - "
           "līnija."),
          ("Kā no grafika nolasīt samaksu?",
           "Nolasa no grafiskā attēla visu iespējamo informāciju par diviem "
           "lielumiem."),
      ]),
       B("Kustības un pirkuma grafiks", [
           ("Kā attēlot vienmērīgu kustību?",
            "Grafiski attēlo tabulā doto sakarību starp laiku un veikto "
            "ceļu."),
           ("Ko stāsta grafika slīpums?",
            "Salīdzina divas kustības vienā koordinātu plaknē un secina, kurš "
            "pārvietojas ātrāk."),
           ("Kā salīdzināt divas cenas?",
            "Salīdzina divus pirkuma notikumus pēc to grafiskā attēla."),
           ("Ātrāk rēķināt vai nolasīt?",
            "Izvērtē, kad nezināmo lielumu ātrāk noteikt no grafika un kad - "
            "aprēķinot."),
       ]),
       B("Sakarības mums apkārt", [
           ("Ko stāsta temperatūras grafiks?",
            "Raksturo nepazīstamu sakarību pēc tās grafiskā attēla un formulē "
            "secinājumus."),
           ("Kādus jautājumus var uzdot?",
            "Formulē jautājumus par lielumiem un sakarībām, izmantojot "
            "grafisko attēlu."),
           ("Kā attēlot savus datus?",
            "Iegūst datus par diviem lielumiem un attēlo tos koordinātu "
            "plaknē."),
           ("Kas notiek starp diviem punktiem?",
            "Spriež, kā mainās lielums starp diviem attēlotajiem punktiem, un "
            "pamato savu pieņēmumu."),
       ])],
      "Sakarības grafiskais attēls",
      "Atliek punktus koordinātu plaknē; grafiski attēlo sakarību starp "
      "diviem lielumiem; nolasa no grafika precīzas un aptuvenas vērtības un "
      "formulē secinājumus.",
      "divu sakarību salīdzināšana; grafiks ar mainīgu ātrumu."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 5. klasē", [
        ("Cik droši rēķinu ar daļām?",
         "Formatīvi pārbauda darbības ar parastajām daļām un jauktiem "
         "skaitļiem."),
        ("Ko es protu ar decimāldaļām un procentiem?",
         "Atkārto decimāldaļu salīdzināšanu un procentu aprēķināšanu no "
         "skaitļa."),
        ("Kā lasu diagrammas un grafikus?",
         "Nolasa datus no sektoru diagrammas un sakarības grafika un formulē "
         "secinājumus."),
        ("Ko gribu iemācīties 6. klasē?",
         "Apkopo gadā apgūto un iepazīstas ar 6. klases tematiem."),
    ]),
]
