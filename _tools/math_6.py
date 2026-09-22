# -*- coding: utf-8 -*-
"""6. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 6. klases sadaļa.
Programmas ieteicamais laiks šai klasei kopā pārsniedz mācību gada stundu
skaitu, tāpēc katram tematam atvēlētās stundas ir samērotas ar gada garumu;
saturs saglabāts pilnībā, saīsinātas ir vingrināšanās stundas.
"""

from math_plani import B, T

IEVADS = (
    "Sestais matemātikas gads. Parādās attiecība, mērogs un proporcionāli "
    "lielumi, tiek pabeigtas darbības ar parastajām daļām un decimāldaļām, un "
    "skaitļu pasaule paplašinās ar negatīvajiem skaitļiem un visu koordinātu "
    "plakni. Procenti nāk no atlaidēm, produktu sastāva un statistikas, bet "
    "telpiskie ķermeņi - no iepakojuma, kas jāizveido ar pēc iespējas mazāku "
    "materiāla patēriņu. Gads noslēdzas ar rēķināšanu, kurā satiekas visu "
    "veidu skaitļi.")

TEMATI = [
    T("6.1.", "Kā kopumu sadala noteiktā attiecībā?",
      "Veido izpratni par lielumu attiecību, tieši un apgriezti "
      "proporcionāliem lielumiem un mērogu.",
      [B("Skaitļu attiecība", [
          ("Ko nozīmē «divi pret trīs»?",
           "Lasa autentisku tekstu ar attiecību un skaidro to saviem "
           "vārdiem."),
          ("Kā attiecību uzzīmēt?",
           "Attēlo divu lielumu attiecību shematiskā zīmējumā un izvēlas sev "
           "piemērotāko veidu."),
          ("Kā attiecību pieraksta?",
           "Pieraksta attiecību ar vārdu «pret», ar daļsvītru un ar dalīšanas "
           "zīmi."),
          ("Kādi lielumi veido attiecību 1 pret 10?",
           "Min piemērus lielumiem, kas veido doto attiecību, un pamato tos."),
          ("Kāda ir šo objektu attiecība?",
           "Aptuveni nosaka apkārtnes objektu garumu vai laukumu attiecību un "
           "pārbauda to ar mērījumiem."),
      ]),
       B("Kopuma sadalīšana attiecībā", [
           ("Ko var uzzināt no pieraksta 1 : 3 : 4?",
            "Nosaka kopīgo vienību skaitu no attiecības pieraksta."),
           ("Kā pagatavot maisījumu?",
            "Skaidro, kā izveidot maisījumu dotā attiecībā ar divām vai trim "
            "sastāvdaļām."),
           ("Kā sadalīt nogriezni?",
            "Sadala nogriezni divās vai trīs daļās dotā attiecībā."),
           ("Kā sadalīt figūru?",
            "Rūtiņu lapā sadala figūru daļās, ja dota daļu laukumu "
            "attiecība."),
           ("Cik katram pienākas?",
            "Sadala kopumu dotā attiecībā sadzīves situācijā ar nezināmo "
            "jebkurā pozīcijā."),
       ]),
       B("Proporcionāli lielumi un mērogs", [
           ("Kad otrs lielums aug tikpat reižu?",
            "Atšķir situācijas ar tieši proporcionāliem lielumiem no pārējām "
            "un min piemērus."),
           ("Kā pārrēķināt recepti?",
            "Aprēķina sastāvdaļu daudzumu citam produkta daudzumam."),
           ("Ko stāsta tabula un grafiks?",
            "Apkopo datus par tieši proporcionāliem lielumiem tabulā un "
            "attēlo tos grafiski."),
           ("Kā nolasīt nezināmo no grafika?",
            "Nolasa lielumu vērtības no proporcionālu lielumu grafiskā "
            "attēla."),
           ("Ko nozīmē mērogs 1 : 500?",
            "Aprēķina attālumu dabā, ja dots mērogs un attālums kartē, un "
            "otrādi."),
           ("Kā uzzīmēt plānu mērogā?",
            "Grupā veic mērījumus un uzzīmē telpas vai dobes plānu norādītajā "
            "mērogā."),
       ])],
      "Attiecība, proporcionāli lielumi un mērogs",
      "Nosaka lielumu attiecību un sadala kopumu dotā attiecībā; aprēķina "
      "nezināmo lielumu tieši un apgriezti proporcionālu lielumu situācijās; "
      "lieto mērogu.",
      "apgriezti proporcionālu lielumu grafiks; attiecība trīs lielumiem."),

    T("6.2.", "Kā reizina un dala parastās daļas?",
      "Apgūst parasto daļu un jauktu skaitļu reizināšanu un dalīšanu, "
      "izmantojot modeļus, darbību īpašības un daļas pamatīpašību.",
      [B("Reizināšana un dalīšana ar veselu skaitli", [
          ("Ko nozīmē reizināt daļu ar veselu skaitli?",
           "Modelē vesela skaitļa un daļas reizinājumu uz skaitļu taisnes un "
           "pieraksta rezultātu."),
          ("Kā daļu sadalīt vienādās daļās?",
           "Dala daļu ar veselu skaitli, spriežot un izmantojot daļas "
           "pamatīpašību."),
          ("Kad daļu izdevīgi paplašināt?",
           "Skaidro, kāpēc, dalot daļu ar veselu skaitli, dažkārt to "
           "paplašina."),
          ("Cik reižu daļa ietilpst veselajā?",
           "Dala veselu skaitli ar pamatdaļu un vārdiski raksturo rezultātu."),
          ("Kā pārbaudīt rezultātu?",
           "Pārbauda dalījumu ar reizināšanu un skaidro savu pierakstu."),
      ]),
       B("Divu daļu reizināšana", [
           ("Kā reizinājumu parādīt kvadrātā?",
            "Attēlo divu īstu daļu reizinājumu kvadrātā ar malu 1 un skaidro, "
            "ko izsaka katrs skaitlis."),
           ("Kā reizināt bez zīmējuma?",
            "Sareizina divas parastās daļas un veido darbības pierakstu."),
           ("Kad reizinājumu var saīsināt?",
            "Saskata iespēju saīsināt pirms reizināšanas un skaidro savu "
            "rīcību."),
           ("Kāpēc reizinot var iegūt mazāku skaitli?",
            "Skaidro, kāpēc reizinājums ar īstu daļu ir mazāks nekā "
            "sākotnējais skaitlis."),
           ("Daļa no skaitļa vai reizinājums?",
            "Salīdzina daļas no vesela skaitļa aprēķinu ar reizinājumu un "
            "formulē secinājumu."),
       ]),
       B("Dalīšana ar daļu", [
           ("Kā dalījumu parādīt uz skaitļu taisnes?",
            "Attēlo divu daļu dalījumu uz skaitļu taisnes un pārbauda "
            "rezultātu ar reizināšanu."),
           ("Kas ir apgrieztais skaitlis?",
            "Nosaka un pieraksta skaitlim apgriezto skaitli; secina, ka to "
            "reizinājums ir 1."),
           ("Kāpēc dalīšanu var aizstāt ar reizināšanu?",
            "Formulē algoritmu dalīšanai ar parasto daļu un pamato to."),
           ("Kā izskatās pieraksts?",
            "Dala daļu ar daļu, veidojot skaidru pierakstu."),
           ("Kāpēc dalot var iegūt lielāku skaitli?",
            "Skaidro, kad dalīšanas rezultāts ir lielāks nekā dalāmais."),
       ]),
       B("Jaukti skaitļi un lietojums", [
           ("Kā reizināt jauktus skaitļus?",
            "Sareizina jauktus skaitļus, pārveidojot tos par neīstām daļām."),
           ("Kā dalīt ar jauktu skaitli?",
            "Dala ar jauktu skaitli un pārbauda rezultātu."),
           ("Cik apmēram sanāks?",
            "Novērtē daļu vai jauktu skaitļu reizinājuma un dalījuma aptuveno "
            "vērtību."),
           ("Kā kāpināt daļu?",
            "Kāpina parasto daļu un jauktu skaitli, lietojot reizināšanu."),
           ("Kur tas noder dzīvē?",
            "Risina situāciju uzdevumu, kura risinājumā jāreizina vai jādala "
            "daļas."),
       ])],
      "Parasto daļu un jauktu skaitļu reizināšana un dalīšana",
      "Reizina un dala parastās daļas un jauktus skaitļus; nosaka apgriezto "
      "skaitli; novērtē rezultāta aptuveno vērtību; risina situāciju "
      "uzdevumus ar daļām.",
      "daļu kāpināšana ar lielākiem kāpinātājiem; trīs daļu reizinājums."),

    T("6.3.", "Kā izpratne par komata lietojumu palīdz, ja reizina un dala "
      "decimāldaļas?",
      "Apgūst decimāldaļu reizināšanu un dalīšanu, izmantojot veselo skaitļu "
      "paņēmienus un skaitļa decimālo sastāvu.",
      [B("Decimāldaļu reizināšana", [
          ("Kā reizinājumu parādīt simta kvadrātā?",
           "Attēlo divu decimāldaļu reizinājumu simta kvadrātā un pieraksta "
           "to."),
          ("Kā reizināt galvā?",
           "Aprēķina galvā vesela skaitļa un decimāldaļas reizinājumu, "
           "skaidrojot savu paņēmienu."),
          ("Cik ciparu būs aiz komata?",
           "Secina reizinājuma ciparu skaitu aiz komata pēc reizinātājiem."),
          ("Kā reizina rakstos?",
           "Reizina decimāldaļas rakstos un formulē algoritmu."),
          ("Kura izteiksme ir lielāka?",
           "Salīdzina izteiksmes ar decimāldaļu reizinājumiem, novērtējot "
           "aptuvenās vērtības."),
      ]),
       B("Reizināšana un dalīšana ar 10 un ar 0,1", [
           ("Kas notiek, reizinot ar 10, 100 un 1000?",
            "Pēta un formulē algoritmu reizināšanai ar 10, 100 un 1000."),
           ("Kas notiek, reizinot ar 0,1?",
            "Formulē algoritmu reizināšanai ar 0,1, 0,01 un 0,001."),
           ("Kā izskatās dalīšana ar 10?",
            "Formulē algoritmu dalīšanai ar 10, 100 un 1000 un pārbauda to ar "
            "kalkulatoru."),
           ("Kāpēc dalot ar 0,1 skaitlis aug?",
            "Skaidro dalīšanu ar 0,1, 0,01 un 0,001 un saista to ar "
            "reizināšanu."),
           ("Kā algoritmi saistīti savā starpā?",
            "Raksturo saistību starp četriem algoritmiem un lieto tos "
            "aprēķinos."),
       ]),
       B("Decimāldaļu dalīšana", [
           ("Kā dalīt decimāldaļu ar veselu skaitli?",
            "Dala decimāldaļu ar veselu skaitli un pārbauda rezultātu ar "
            "reizināšanu."),
           ("Kāds dalījums sanāk, dalot 42 : 7 un 4,2 : 7?",
            "Salīdzina dalāmā decimālo sastāvu un saista to ar rezultātu."),
           ("Kā dalīt ar decimāldaļu?",
            "Dala ar decimāldaļu, palielinot dalāmo un dalītāju vienādu "
            "skaitu reižu; pamato to ar daļas pamatīpašību."),
           ("Kur liek komatu?",
            "Dala rakstos un skaidro, kad rezultātā aiz veselajiem liek "
            "komatu."),
           ("Cik apmēram būs dalījums?",
            "Novērtē dalījuma aptuveno vērtību un salīdzina dalījumus bez "
            "precīziem aprēķiniem."),
       ]),
       B("Parastās daļas un decimāldaļas kopā", [
           ("Kā parasto daļu pārvērst decimāldaļā?",
            "Izsaka parasto daļu kā decimāldaļu, dalot skaitītāju ar saucēju "
            "vai lietojot pamatīpašību."),
           ("Kurš pieraksts ir ērtāks?",
            "Izvēlas daļskaitļu pieraksta veidu konkrētam aprēķinam un pamato "
            "izvēli."),
           ("Kā rēķināt jauktā izteiksmē?",
            "Saskaita, atņem, reizina un dala daļskaitļus, kas pierakstīti "
            "abos veidos."),
           ("Cik dažādus rezultātus var iegūt?",
            "Starp dotiem skaitļiem ievieto darbību zīmes, lai iegūtu dažādus "
            "rezultātus."),
           ("Kur radusies kļūda?",
            "Izvērtē cita risinājuma pareizību un raksturo iespējamos kļūdas "
            "cēloņus."),
       ])],
      "Decimāldaļu reizināšana un dalīšana",
      "Reizina un dala decimāldaļas, arī ar 10, 100, 0,1 un 0,01; novērtē "
      "rezultāta aptuveno vērtību; pāriet no parastās daļas uz decimāldaļu un "
      "rēķina jauktās izteiksmēs.",
      "periodiskas decimāldaļas; aprēķini ar kalkulatoru un to pārbaude."),

    T("6.4.", "Kā attēlo un raksturo telpiskus ķermeņus?",
      "Sistematizē izpratni par telpisku ķermeņu attēlošanu, virsmas laukumu "
      "un tilpumu.",
      [B("Telpisku ķermeņu īpašības", [
          ("Cik dažādus ķermeņus var izveidot?",
           "No dotā kubu skaita veido dažādus ķermeņus un raksturo tos."),
          ("Kā ķermeni aprakstīt precīzi?",
           "Raksturo daudzskaldni, lietojot jēdzienus skaldne, šķautne, "
           "virsotne."),
          ("Kā ķermenis izskatās no dažādām pusēm?",
           "Zīmē un raksturo telpiska ķermeņa skatus dažādās plaknēs."),
          ("Kā uzbūvēt cilindru?",
           "Plāno un praktiski veido cilindra modeli pēc dotiem izmēriem."),
          ("Kas kopīgs piramīdai un konusam?",
           "Salīdzina daudzskaldni, piramīdu, cilindru un konusu pēc to "
           "elementiem."),
      ]),
       B("Virsmas laukums un izklājums", [
           ("Kā izskatās kastes izklājums?",
            "Zīmē taisnstūra paralēlskaldņa izklājumu pēc dotiem izmēriem."),
           ("Kā aprēķināt virsmas laukumu?",
            "Aprēķina taisnstūra paralēlskaldņa virsmas laukumu un skaidro "
            "savu izteiksmi."),
           ("Cik liela ir kubu figūras virsma?",
            "Aprēķina virsmas laukumu ķermenim, kas sastāv no vienādiem "
            "kubiem."),
           ("Cik daudz papīra vajag dāvanai?",
            "Lieto virsmas laukuma aprēķinu praktiskā situācijā ar mērvienību "
            "vienādošanu."),
           ("Kā pārveidot laukuma mērvienības?",
            "Izsaka lielākas laukuma mērvienības mazākās un otrādi."),
       ]),
       B("Tilpums", [
           ("Cik kubu ietilpst ķermenī?",
            "Nosaka ķermeņa tilpumu kā vienības kubu skaitu un veido "
            "izteiksmi."),
           ("Kā rodas tilpuma formula?",
            "Iegūst taisnstūra paralēlskaldņa tilpuma formulu, modelējot ar "
            "vienības kubiem."),
           ("Cik kubikcentimetru ir kubikdecimetrā?",
            "Praktiski veido 1 dm³ modeli un nosaka sakarību starp tilpuma "
            "mērvienībām."),
           ("Kāpēc litrs ir kubikdecimetrs?",
            "Skaidro sakarību 1 l = 1 dm³ un lieto to aprēķinos."),
           ("Cik liels ir šis trauks?",
            "Novērtē tilpuma aptuveno vērtību un salīdzina to ar precīzo."),
           ("Kā rēķināt saliktam ķermenim?",
            "Aprēķina tilpumu ķermenim, ko var sadalīt taisnstūra "
            "paralēlskaldņos."),
       ]),
       B("Sakarības starp lielumiem", [
           ("Kā izveidot izdevīgāko iepakojumu?",
            "Veido kastīti ar iespējami lielāku tilpumu un mazāku materiāla "
            "patēriņu."),
           ("Kas notiek, ja šķautni palielina divas reizes?",
            "Pēta un skaidro, kā mainās kuba virsmas laukums un tilpums, "
            "mainot šķautni."),
           ("Kā mainās tilpums, mainot vienu izmēru?",
            "Spriež par tilpuma izmaiņām, mainot vienu vai vairākus izmērus."),
           ("Kāda likumsakarība ir ķermeņu virknē?",
            "Pēta sakarības starp daudzskaldņu lielumiem virknē un formulē "
            "likumsakarību."),
       ])],
      "Telpiski ķermeņi, virsmas laukums un tilpums",
      "Raksturo telpiskus ķermeņus un to skatus; zīmē izklājumu; aprēķina "
      "taisnstūra paralēlskaldņa virsmas laukumu un tilpumu; pārveido laukuma "
      "un tilpuma mērvienības.",
      "prizmas un cilindra tilpums; iepakojuma optimizācijas uzdevums."),

    T("6.5.", "Kā sadzīves situācijās izmanto procentus?",
      "Nosaka vienu skaitli kā otra skaitļa procentus un lieto procentus "
      "autentisku problēmu risināšanā.",
      [B("Skaitlis kā otra skaitļa procenti", [
          ("Kā procentus saistīt ar daļu?",
           "Skaidro, ka «a kā b procenti» nozīmē to pašu, ko «a kā b daļa»."),
          ("Kā aprēķināt, cik procenti?",
           "Aprēķina vienu skaitli kā otra skaitļa procentus un pieraksta "
           "rezultātu."),
          ("Kuras vienādības jāzina no galvas?",
           "Lieto vienādības 50 % = puse, 25 % = ceturtdaļa, 20 % = piektdaļa "
           "aprēķinos."),
          ("Kā zīmējums palīdz?",
           "Veido shematisku zīmējumu, lai attēlotu vienu skaitli kā otra "
           "procentus."),
          ("Kādas sakarības var izlasīt?",
           "Formulē dažādas sakarības starp lielumiem, ja zināma viena "
           "(ja 2 pret 8 ir 25 %, tad 25 % no 8 ir 2)."),
      ]),
       B("Procenti dzīvē", [
           ("Cik liela ir atlaide?",
            "Aprēķina procentus no skaitļa un jauno cenu pēc atlaides."),
           ("Cik maksāja sākumā?",
            "Aprēķina veselo, ja zināma procentu skaitliskā vērtība."),
           ("Ko stāsta produkta sastāvs?",
            "Ar procentiem raksturo pārtikas sastāvu un salīdzina to ar "
            "ieteikumiem."),
           ("Kā izplānot telpas iekārtošanu?",
            "Plāno dārza vai sporta laukuma iekārtošanu, lietojot attiecību "
            "un procentus."),
           ("Ko rāda skolas sporta dati?",
            "Apkopo datus, apstrādā tos un formulē secinājumus, lietojot "
            "procentus un daļas."),
           ("Cik liela ir vielas masas daļa?",
            "Lieto procentus uzdevumā ar dabaszinātņu saturu."),
       ]),
       B("Procentu problēmas", [
           ("Kā pierakstīt problēmas risinājumu?",
            "Pieraksta situācijas risinājumu ar izteiksmi vai vienādību, kas "
            "satur nezināmo."),
           ("Procenti vai reizes?",
            "Risina uzdevumu, kurā apvienoti procenti un sakarības «tik reižu "
            "vairāk»."),
           ("Vai rezultāts ir ticams?",
            "Pārbauda iegūtā rezultāta atbilstību reālajam kontekstam."),
           ("Kā izlasīt sarežģītu tekstu?",
            "Nolasa informāciju no autentiska teksta ar procentiem un daļām "
            "un raksturo to lietojumu."),
           ("Kāds uzdevums sanāk tev?",
            "Veido savu procentu uzdevumu par sev nozīmīgu situāciju un "
            "risina klasesbiedra uzdevumu."),
       ])],
      "Procenti praktiskās situācijās",
      "Nosaka vienu skaitli kā otra skaitļa procentus; aprēķina procentus no "
      "skaitļa un veselo, ja zināmi procenti; risina praktiskas problēmas, "
      "kurās procenti apvienoti ar attiecību un salīdzinājumiem.",
      "procentu izmaiņas vairākos soļos; salikto procentu ideja."),

    T("6.6.", "Kāpēc nepieciešami skaitļi, kuri ir mazāki nekā nulle?",
      "Veido izpratni par pozitīviem un negatīviem skaitļiem, to novietojumu "
      "uz skaitļu taisnes un par visu koordinātu plakni.",
      [B("Negatīvi skaitļi un skaitļu taisne", [
          ("Kur dzīvē satiekam skaitļus zem nulles?",
           "Min piemērus lielumiem, ko raksturo negatīvi skaitļi, un skaidro "
           "to nozīmi."),
          ("Kas ir pretējais skaitlis?",
           "Nosaka un pieraksta skaitlim pretējo skaitli, arī pierakstā ar "
           "divām zīmēm."),
          ("Kā izskatās pilna skaitļu taisne?",
           "Atliek uz skaitļu taisnes negatīvus veselus skaitļus, daļas un "
           "decimāldaļas."),
          ("Kas ir skaitļa modulis?",
           "Skaidro moduli kā attālumu līdz nullei un nosaka pretēju skaitļu "
           "moduļus."),
          ("Kurš skaitlis ir lielāks?",
           "Salīdzina pozitīvus un negatīvus skaitļus un sakārto tos augošā "
           "secībā."),
          ("Kā skaitīt no negatīva skaitļa?",
           "Skaita uz priekšu un atpakaļ no negatīva skaitļa ar soli 1, 2, 5 "
           "un 10."),
          ("Kāds vispārīgs apgalvojums ir patiess?",
           "Formulē vispārīgus spriedumus par skaitļu salīdzināšanu un pamato "
           "tos."),
      ]),
       B("Sakarības starp negatīviem skaitļiem", [
           ("Kurš skaitlis ir tieši vidū?",
            "Nosaka skaitli, kas uz skaitļu taisnes atrodas vidū starp diviem "
            "dotajiem."),
           ("Kādi skaitļi ir starp?",
            "Nosauc vairākus skaitļus starp diviem dotajiem negatīviem "
            "skaitļiem."),
           ("Cik tālu viens no otra?",
            "Nosaka attālumu starp diviem skaitļiem uz skaitļu taisnes."),
           ("Kā izveidot virkni ar vienādu soli?",
            "Veido negatīvu skaitļu virkni ar dotu attālumu starp blakus "
            "skaitļiem."),
           ("Kāda likumsakarība ir virknē?",
            "Turpina virkni un skaidro saskatīto likumsakarību."),
           ("Kuri skaitļi atbilst nosacījumiem?",
            "Nosaka skaitļu kopu pēc nosacījumiem par moduli un novietojumu."),
       ]),
       B("Koordinātu plakne", [
           ("Kas kopīgs visiem šiem grafikiem?",
            "Aplūko dažādu jomu grafikus un nosaka, kas tiem kopīgs."),
           ("Kā iekārto koordinātu plakni?",
            "Iekārto koordinātu plakni, nosauc asis un izvēlas vienības."),
           ("Kā attēlot temperatūras izmaiņas?",
            "Attēlo tabulā dotos temperatūras datus koordinātu plaknē un "
            "skaidro grafiku."),
           ("Ko var secināt starp mērījumiem?",
            "Formulē secinājumus par lieluma izmaiņām starp diviem "
            "mērījumiem."),
           ("Kā izpētīt ledus kušanu?",
            "Plāno mājas eksperimentu, apkopo datus tabulā un attēlo tos "
            "grafiski."),
           ("Kā raksturot grafiku ar vārdiem?",
            "Raksturo grafisko attēlu, lietojot «paaugstinās par», «zem "
            "nulles», «par tik lielāks»."),
       ]),
       B("Figūras koordinātu plaknē", [
           ("Kā pieraksta punkta koordinātas?",
            "Nolasa un pieraksta koordinātu plaknē atliktu punktu "
            "koordinātas."),
           ("Kā uzzīmēt daudzstūri pēc koordinātām?",
            "Atliek punktus un zīmē nogriezni vai daudzstūri pēc virsotņu "
            "koordinātām."),
           ("Kāda figūra sanāks?",
            "Veido figūru pēc dotiem nosacījumiem un raksturo tās īpašības."),
           ("Kas notiek, figūru pārvietojot?",
            "Zīmē figūru, kas iegūta, pārvietojot doto par vienībām pa asīm, "
            "un raksturo koordinātu sakarības."),
           ("Kā uzzīmēt simetrisku figūru pret asi?",
            "Zīmē dotai figūrai simetrisku figūru pret koordinātu asi."),
           ("Kā pagriezt figūru par 180°?",
            "Zīmē figūru, kas simetriska dotajai pret punktu, un skaidro "
            "rīcību."),
       ])],
      "Pozitīvi un negatīvi skaitļi; koordinātu plakne",
      "Nosaka pretējo skaitli un moduli; atliek un salīdzina pozitīvus un "
      "negatīvus skaitļus; nosaka attālumu starp skaitļiem; lieto koordinātu "
      "plakni un zīmē simetriskas figūras.",
      "attālums no punkta līdz taisnei; figūru pagriešana par 90°."),

    T("6.7.", "Ko nozīmē skaitlim pieskaitīt negatīvu skaitli, no skaitļa "
      "atņemt negatīvu skaitli?",
      "Modelē un skaidro saskaitīšanu un atņemšanu ar negatīviem skaitļiem un "
      "formulē algoritmus racionālu skaitļu saskaitīšanai un atņemšanai.",
      [B("Veselu skaitļu saskaitīšana", [
          ("Kā mainās temperatūra?",
           "Interpretē vienkāršas veselu skaitļu summas ar temperatūras vai "
           "naudas piemēriem."),
          ("Ko nozīmē zīme skaitļa priekšā?",
           "Lasa un pieraksta izteiksmes, skaidrojot zīmju divējādo nozīmi."),
          ("Kā saskaitīšanu parādīt ar bultiņām?",
           "Modelē saskaitīšanu uz skaitļu taisnes ar vērstiem nogriežņiem."),
          ("Kāpēc pretējo skaitļu summa ir nulle?",
           "Formulē secinājumu par pretējo skaitļu summu un lieto to "
           "aprēķinos."),
          ("Kāda būs summas zīme?",
           "Formulē apgalvojumus par summas zīmi un nosaka to pirms "
           "aprēķina."),
          ("Kā saskaitīt vairākus skaitļus?",
           "Saskaita trīs vai četrus veselus skaitļus, izmantojot saskaitāmo "
           "maiņu vietām."),
      ]),
       B("Veselu skaitļu atņemšana", [
           ("Vai no mazāka var atņemt lielāku?",
            "Modelē uz skaitļu taisnes atņemšanu, kur mazinātājs ir lielāks "
            "nekā mazināmais."),
           ("Kas notiek, atņemot negatīvu skaitli?",
            "Aprēķina starpību virknē un komentē saskatīto sakarību."),
           ("Kāpēc atņemšanu var aizstāt?",
            "Pieraksta atņemšanu kā pretējā skaitļa pieskaitīšanu un skaidro, "
            "kad tas palīdz."),
           ("Kā izlasīt garu izteiksmi?",
            "Lasa izteiksmi ar 3-4 darbībām, apraksta veicamās darbības un "
            "aprēķina vērtību."),
           ("Kurš skaitlis trūkst?",
            "Nosaka nezināmo darbības locekli un pieraksta aprēķinu."),
           ("Cik dažādus rezultātus var iegūt?",
            "Starp dotiem skaitļiem ievieto zīmes, lai iegūtu dažādus "
            "rezultātus."),
       ]),
       B("Izteiksmes un likumsakarības", [
           ("Kā pierakstīt izteiksmi citādi?",
            "Pieraksta vienu izteiksmi vairākos veidos, nemainot tās "
            "vērtību."),
           ("Kā saskaitīt ļoti daudz saskaitāmo?",
            "Aprēķina summu, kas veidota pēc likumsakarības, sadalot problēmu "
            "daļās."),
           ("Kāda izteiksme atbilst aprakstam?",
            "Veido izteiksmi pēc vispārīga apraksta par saskaitāmo zīmēm un "
            "summu."),
           ("Kā atrisināt nevienādību?",
            "Nosaka nezināmo nevienādībā ar negatīviem skaitļiem, izmantojot "
            "skaitļu taisni."),
           ("Kur radusies kļūda?",
            "Izvērtē cita risinājumu un raksturo kļūdas cēloni."),
       ]),
       B("Daļskaitļi un lietojums", [
           ("Kā saskaitīt negatīvas daļas?",
            "Saskaita un atņem pozitīvus un negatīvus daļskaitļus, kas doti "
            "kā parastās daļas."),
           ("Kā rēķināt ar negatīvām decimāldaļām?",
            "Saskaita un atņem pozitīvas un negatīvas decimāldaļas un skaidro "
            "darbības."),
           ("Kā plānot savu risinājumu?",
            "Pirms aprēķina strukturēti stāsta, ko darīs vispirms un kā "
            "veidos pierakstu."),
           ("Par cik mainījās temperatūra?",
            "Lieto saskaitīšanu un atņemšanu situācijās ar citu mācību jomu "
            "kontekstu."),
           ("Cik droši jau protu?",
            "Patstāvīgi aprēķina izteiksmju vērtības ar pozitīviem un "
            "negatīviem skaitļiem."),
       ])],
      "Saskaitīšana un atņemšana ar pozitīviem un negatīviem skaitļiem",
      "Saskaita un atņem pozitīvus un negatīvus skaitļus, arī daļskaitļus; "
      "pieraksta atņemšanu kā pretējā skaitļa pieskaitīšanu; aprēķina "
      "izteiksmes vērtību ar līdz 4 darbībām un iekavām.",
      "summas pēc likumsakarības; nevienādības ar diviem nosacījumiem."),

    T("6.8.", "Kā plāno darbību izpildi ar visu veidu skaitļiem?",
      "Apgūst pozitīvu un negatīvu skaitļu reizināšanu un dalīšanu un "
      "sistematizē rēķināšanu ar visu veidu skaitļiem.",
      [B("Reizināšana un dalīšana ar negatīviem skaitļiem", [
          ("Kāpēc reizinājums sanāk negatīvs?",
           "Izsaka negatīva skaitļa reizinājumu ar veselu skaitli kā summu un "
           "secina par zīmi."),
          ("Kāda zīme būs rezultātam?",
           "Formulē likumu par reizinājuma un dalījuma zīmi un lieto to pirms "
           "aprēķina."),
          ("Kā reizina un dala veselus skaitļus?",
           "Reizina un dala dažādu zīmju veselus skaitļus, skaidrojot abus "
           "soļus."),
          ("Kāda zīme ir garai izteiksmei?",
           "Nosaka rezultāta zīmi izteiksmei ar daudzām reizināšanas un "
           "dalīšanas zīmēm."),
          ("Kā kāpināt negatīvu skaitli?",
           "Nosaka pakāpes vērtību, ja bāze ir negatīvs skaitlis, un formulē "
           "vispārinājumu."),
          ("Kā reizina un dala daļskaitļus?",
           "Reizina un dala pozitīvus un negatīvus daļskaitļus un pārbauda "
           "cits cita darbus."),
      ]),
       B("Racionālie skaitļi", [
           ("Kādi skaitļi mums ir?",
            "Veido strukturētu apkopojumu par skaitļu kopām un to savstarpējo "
            "saistību."),
           ("Kas ir racionāls skaitlis?",
            "Skaidro, ka racionālu skaitli var pierakstīt kā daļu, un nosaka "
            "skaitļu piederību kopai."),
           ("Cik dažādi var pierakstīt vienu skaitli?",
            "Pieraksta doto skaitli pēc iespējas dažādos veidos un skaidro, "
            "kad tas noder."),
           ("Kā sagrupēt skaitļus?",
            "Šķiro un grupē racionālus skaitļus pēc noteiktas pazīmes."),
           ("Kuri apgalvojumi ir patiesi?",
            "Formulē konkrētu piemēru dotam vispārīgam apgalvojumam par "
            "skaitļu īpašībām."),
       ]),
       B("Aprēķinu plānošana", [
           ("Kā izplānot garu aprēķinu?",
            "Pirms aprēķina pastāsta par pieraksta veidu, darbību secību un "
            "izvēlētajiem paņēmieniem."),
           ("Kad pāriet uz viena veida daļskaitļiem?",
            "Izvēlas, vai rēķināt ar parastajām daļām vai decimāldaļām, un "
            "pamato izvēli."),
           ("Kāda ir darbību secība?",
            "Aprēķina racionālu skaitļu izteiksmes vērtību ar līdz četrām "
            "darbībām un iekavām."),
           ("Kad izmantot kalkulatoru?",
            "Izvērtē, kuras darbības veikt galvā un kurām lietot digitālos "
            "rīkus."),
           ("Kur risinājumā ir kļūda?",
            "Lasa citu risinājumus, izvērtē to pareizību un raksturo kļūdu "
            "cēloņus."),
       ]),
       B("Situāciju uzdevumi", [
           ("Kā uzdevumu pierakstīt matemātiski?",
            "Veido izteiksmi vai vienādību ar nezināmo situācijas aprakstam."),
           ("Kā rēķini palīdz plānot budžetu?",
            "Risina praktisku uzdevumu par ienākumiem un izdevumiem, lietojot "
            "racionālus skaitļus."),
           ("Kā apvienot procentus un daļas?",
            "Risina uzdevumu, kurā apvienoti procenti, daļas un darbības ar "
            "racionāliem skaitļiem."),
           ("Vai atbilde ir ticama?",
            "Pārbauda rezultāta atbilstību situācijai un skaidro savu "
            "spriedumu."),
           ("Cik droši jau rēķinu?",
            "Patstāvīgi risina jauktus uzdevumus ar visu veidu skaitļiem."),
       ])],
      "Reizināšana, dalīšana un darbības ar racionāliem skaitļiem",
      "Reizina, dala un kāpina racionālus skaitļus; nosaka rezultāta zīmi; "
      "aprēķina izteiksmes vērtību ar līdz 4 darbībām; plāno un skaidro savu "
      "aprēķinu gaitu.",
      "pakāpes ar negatīvu bāzi un lielāku kāpinātāju; aprēķinu "
      "optimizācija."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 6. klasē", [
        ("Cik droši rēķinu ar racionāliem skaitļiem?",
         "Formatīvi pārbauda darbības ar daļām, decimāldaļām un negatīviem "
         "skaitļiem."),
        ("Ko protu ar procentiem un attiecību?",
         "Atkārto procentu aprēķinus un kopuma sadalīšanu attiecībā."),
        ("Kā lietoju koordinātu plakni?",
         "Atkārto punktu koordinātas, grafikus un simetriskas figūras."),
        ("Ko gaida 7. klasē?",
         "Apkopo gadā apgūto un iepazīstas ar 7. klases tematiem - "
         "funkcijām, vienādojumiem un ģeometriju."),
    ]),
]
