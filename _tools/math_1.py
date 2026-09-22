# -*- coding: utf-8 -*-
"""1. klases matemātikas stundu plāns.

Temati, to secība un ieteicamais stundu skaits - oficiālā programmas parauga
(Math/mat_p.pdf) 1. klases sadaļa. Stundu skaits pielāgots mācību gadam, kurā
matemātika ir katru mācību dienu.

Katra stunda ir viens jautājums, uz kuru stundā atbild, un viens sasniedzamais
rezultāts, ko skolēns pēc stundas prot. Vienā mikrotematā ir 3-10 stundas.
"""

from math_plani import B, T

IEVADS = (
    "Pirmais matemātikas gads. Temati aptver skaitīšanu un skaitļa sastāvu "
    "līdz 10, skaitļus līdz 100, saskaitīšanu un atņemšanu 20 un 100 apjomā, "
    "garuma mērīšanu, laiku, naudu un figūras. Visā gadā skaitļi nāk no "
    "reālām situācijām - klases, veikala, pagalma un pulksteņa -, un katru "
    "jaunu domu skolēns vispirms parāda ar priekšmetiem vai zīmējumu un tikai "
    "tad pieraksta ar cipariem.")

TEMATI = [
    T("1.1.", "Kā izstāsta un parāda: cik, kur, kāds?",
      "Atkārto un precizē pirmsskolā apgūto par skaitļiem un figūrām; mācās "
      "aprakstīt novēroto un paskaidrot savas darbības.",
      [B("Skaits un skaitīšana līdz 10", [
          ("Cik logu ir mūsu klasē?",
           "Nosaka objektu skaitu līdz 10 un attēlo to ar modeli - paņem tik "
           "ripiņu, cik ir logu, krēslu, somu."),
          ("Kā uzraksta skaitli, ko redzi?",
           "Raksta ciparus no 0 līdz 9 rūtiņu lapā; pieraksta redzēto "
           "objektu skaitu ar ciparu."),
          ("Vai vari pateikt, cik ir, neskaitot?",
           "Uztver 4-6 objektu izkārtojumu kā kopumu, nepārskaitot katru; "
           "pārbauda, saskaitot."),
          ("Kur satiec skaitli 7?",
           "Min piemērus, kur skaitli lieto dzīvē (7 nedēļas dienas); skaita "
           "līdz 10 un atpakaļ, sākot no jebkura skaitļa."),
          ("Kur ir vairāk - pie loga vai pie durvīm?",
           "Salīdzina divu grupu skaitu, sagrupējot pa pāriem vai saskaitot; "
           "lieto vārdus vairāk, mazāk, tikpat."),
      ]),
       B("Priekšmetu un skaitļu virknes", [
           ("Kāds būs nākamais?",
            "Turpina ritmisku objektu virkni un pastāsta, pēc kā izdomāja "
            "nākamo elementu."),
           ("Kā izveidot savu rakstu?",
            "Veido ritmisku virkni no krāsainām figūrām un parāda grupu, kas "
            "atkārtojas."),
           ("Kurš pēc kārtas?",
            "Lieto pamata un kārtas skaitļa vārdus, stāstot par virkni: "
            "pirmais, otrais, trešais."),
           ("Kura diena bija vakar?",
            "Nosauc nedēļas dienas pēc kārtas; nosaka, kura diena bija vakar, "
            "būs rīt vai pēc divām dienām."),
       ]),
       B("Figūras ap mums", [
           ("Kā figūra dabū savu vārdu?",
            "Nosauc trijstūri, četrstūri un piecstūri pēc malu un virsotņu "
            "skaita."),
           ("Vai vari uzzīmēt taisnu līniju?",
            "Novelk taisnu līniju ar lineālu un ar brīvu roku pa rūtiņām; "
            "zīmē trijstūrus un četrstūrus."),
           ("Ko var salikt no trim figūrām?",
            "Veido jaunas figūras, savietojot ar malām dotās figūras "
            "(Tangrama vai kartona komplekts)."),
           ("Kā pateikt tā, lai otrs uzzīmē to pašu?",
            "Pārī apraksta figūru tā, lai otrs to atpazīst vai izveido; "
            "salīdzina, vai rezultāts sakrīt ar domāto."),
       ]),
       B("Kur kas atrodas - virzieni un soļi", [
           ("Kā pateikt, kur kas atrodas?",
            "Apraksta objektu novietojumu ar vārdiem pa labi, pa kreisi, "
            "virs, zem, starp; sakārto savu darbavietu pēc norādēm."),
           ("Kā ar bultiņām pastāstīt ceļu?",
            "Attēlo pārvietošanos pa rūtiņu laukumu ar bultiņām un izpilda "
            "dotu 3-5 soļu ceļu."),
           ("Vai uz mērķi ir tikai viens ceļš?",
            "Salīdzina divus pārvietošanās variantus un skaidro, kas mainās, "
            "ja soļus sakārto citādi."),
       ])],
      "Skaits, figūras un virzieni",
      "Nosaka objektu skaitu līdz 10 un salīdzina divas grupas; raksta "
      "ciparus; atpazīst un zīmē daudzstūrus; turpina virkni un izpilda "
      "pārvietošanās soļus pa rūtiņu laukumu.",
      "skaitīšana pa pāriem; virknes, kurās atkārtojas trīs elementi."),

    T("1.2.", "Cik kopā, cik palika?",
      "Veido izpratni par skaitļa sastāvu un par saskaitīšanas un atņemšanas "
      "jēgu; visu vispirms parāda ar modeli un tikai tad pieraksta.",
      [B("Skaitļa sastāvs līdz 10", [
          ("Cik dažādi var izbirt piecas ripiņas?",
           "Modelē skaitļa sastāvu ar divpusēji krāsainām ripiņām un "
           "pieraksta iznākumus divu aiļu tabulā."),
          ("Kā sadalīt klucīšu virteni divās rokās?",
           "Sadala saspraustus klucīšus divās daļās un nosauc, cik ir katrā "
           "rokā, ja kopā ir zināms skaits."),
          ("Cik stāvu ir skaitļa mājiņai?",
           "Veido skaitļa mājiņu ar visiem sadalījumiem un spriež, cik stāvu "
           "tajā var izveidot."),
          ("Ko nozīmē 0?",
           "Skaidro, ka 0 nozīmē «necik»; parāda gadījumu, kur viena daļa ir "
           "0, un pieraksta to."),
          ("Kā skaitļa sastāvu uzrakstīt ar zīmēm?",
           "Pieraksta skaitļa sastāvu kā vienādību (8 = 3 + 5) un izlasa to."),
          ("Cik pietrūkst līdz 10?",
           "Attēlo skaitli 2 × 5 rūtiņu taisnstūrī un pasaka, cik pietrūkst "
           "līdz 10 un cik ir vairāk nekā 5."),
          ("Vai esam atraduši visus gadījumus?",
           "Sakārto sadalījumus pēc kārtas un skaidro, kā zināt, ka neviens "
           "nav aizmirsts."),
          ("Kurš skaitlis slēpjas?",
           "Pēc daļēji aizpildītas mājiņas nosaka trūkstošo skaitli un "
           "pārbauda ar modeli."),
      ]),
       B("Tabula, kurā redz visu", [
           ("Kā pierakstīt tā, lai pats saproti?",
            "Izveido divu aiļu tabulu, pārlokot lapu, un ieraksta tajā "
            "iegūtos datus."),
           ("Kas notiek, ja tas pats iznāk otrreiz?",
            "Ieraksta datus tabulā iegūšanas secībā un atzīmē atkārtotos "
            "gadījumus."),
           ("Kā pastāstīt citam, ko izdarīji?",
            "Stāsta pēc savas tabulas, kā rīkojies, lai pierakstītu visus "
            "iespējamos veidus."),
       ]),
       B("Saskaitīšana un atņemšana 10 apjomā", [
           ("Ko nozīmē «+» un «−»?",
            "Pieraksta situāciju ar saskaitīšanu vai atņemšanu un skaidro, ko "
            "katra zīme nozīmē."),
           ("Vai svarīgi, kurš skaitlis ir pirmais?",
            "Pārliecinās ar modeli, ka, saskaitāmos mainot vietām, summa "
            "nemainās."),
           ("Skaitīt klāt vai atcerēties?",
            "Salīdzina saskaitīšanas paņēmienus - saliek kopā un izskaita, "
            "skaita uz priekšu, izmanto skaitļa sastāvu."),
           ("Kā no viena piemēra dabūt četrus?",
            "No skaitļa sastāva pieraksta divas summas un divas starpības "
            "(3 + 2 = 5, 2 + 3 = 5, 5 − 2 = 3, 5 − 3 = 2)."),
           ("Ko dara ar lineālu, ja neesi zīmētājs?",
            "Modelē summu un starpību uz lineāla kā uz skaitļu taisnes."),
           ("Kuras summas jau zini no galvas?",
            "Atlasa summas un starpības 10 apjomā, ko zina no galvas, un "
            "izspēlē pārī pārējās."),
           ("Cik ātri vari?",
            "Aprēķina summas un starpības 10 apjomā, skaidrojot, kā rezultāts "
            "iegūts."),
           ("Cik palika somā?",
            "Risina vienkāršu situāciju par «pienāk» un «aiziet», pierakstot "
            "to ar atbilstošu darbību."),
       ]),
       B("Patiess vai aplams pieraksts", [
           ("Vai pieraksts ir patiess?",
            "Skaidro, kāpēc dota vienādība ir patiesa vai aplama, "
            "nepieciešamības gadījumā modelējot to."),
           ("Kā aplamu vienādību salabot?",
            "Izdomā vairākus veidus, kā aplamu vienādību pārveidot par "
            "patiesu, un salīdzina idejas."),
           ("Vai aiz «=» vienmēr ir atbilde?",
            "Lasa un veido pierakstus, kuros abās pusēs ir izteiksme "
            "(3 + 2 = 4 + 1)."),
           ("Kāds stāsts der šim pierakstam?",
            "Nosauc piemēru no dzīves, kas atbilst dotai izteiksmei ar "
            "saskaitīšanu vai atņemšanu 10 apjomā."),
       ])],
      "Skaitļa sastāvs, saskaitīšana un atņemšana 10 apjomā",
      "Modelē un pieraksta skaitļa sastāvu; saskaita un atņem 10 apjomā; "
      "sadzīves situāciju pieraksta ar atbilstošu darbību; nosaka, vai "
      "vienādība ir patiesa.",
      "skaitļa sastāvs kā trīs saskaitāmo summa."),

    T("1.3.", "Kā mēra garumus un kā iegūst simetrisku figūru?",
      "Sāk apgūt mērīšanu ar lineālu - prasmi, ko vēlāk pārnes uz citiem "
      "lielumiem; praktiski darbojoties, iepazīst simetriju.",
      [B("Nogrieznis un mērīšana ar lineālu", [
          ("Cik zīmuļu garš ir galds?",
           "Mēra ar izvēlētu nosacītu vienību un spriež, kas ir laba "
           "mērvienība."),
          ("Kāpēc cilvēki vienojās par centimetru?",
           "Skaidro, ka mērīt nozīmē salīdzināt ar vienību; pareizi pieliek "
           "lineālu mērāmajam objektam."),
          ("Cik centimetru?",
           "Mēra reālu objektu garumu veselos centimetros un pieraksta "
           "rezultātu (8 cm)."),
          ("Vai vari uzzīmēt tieši 7 cm?",
           "Zīmē dota garuma nogriezni un lauztu līniju ar lineālu."),
          ("Cik gara ir lauzta līnija?",
           "Saskaita mērījumos iegūtos garumus 10 apjomā, veidojot pierakstu "
           "2 cm + 3 cm = 5 cm."),
          ("Cik tev šķiet - un cik ir?",
           "Izsaka pieņēmumu par garumu pēc acumēra un pārbauda to, izmērot; "
           "raksturo mērījumu ar «apmēram», «gandrīz»."),
      ]),
       B("Simetriskas figūras", [
           ("Kā pārbaudīt, vai figūra ir taisnstūris?",
            "Pārbauda taisnos leņķus ar papīra lapas stūri un zīmē taisnstūri "
            "rūtiņu lapā."),
           ("Kuras malas ir vienādas?",
            "Saskata un ar locīšanu pamato, ka taisnstūra un kvadrāta "
            "pretējās malas ir vienāda garuma."),
           ("Kā pārlocīt uz pusēm?",
            "Lokot sadala kvadrātu un riņķi divās un četrās vienādās daļās."),
           ("Vai figūra ir simetriska?",
            "Ar locīšanu pārbauda, vai figūra ir simetriska, un parāda "
            "locījuma līniju."),
           ("Kā izgriezt simetrisku rotājumu?",
            "Veido simetrisku figūru lokot un izgriežot; pārbauda rezultātu "
            "ar locīšanu."),
       ])],
      "Garuma mērīšana un simetrija",
      "Mēra ar lineālu veselos centimetros un zīmē dota garuma nogriezni; "
      "saskaita un atņem garumus; nosaka, vai figūra ir simetriska.",
      "mērīšana ar precizitāti līdz pusei centimetra."),

    T("1.4.", "Kā pieraksta un salīdzina skaitļus, kuri ir lielāki nekā 10?",
      "Veido skaitļu izjūtu līdz 100: desmiti un vieni, skaitļu taisne, simta "
      "kvadrāts un skaitļu salīdzināšana.",
      [B("Desmiti un vieni", [
          ("Kā saskaitīt daudz priekšmetu, nesajaucoties?",
           "Grupē objektus pa 10 un pasaka, cik ir pilnu desmitu un cik vēl "
           "vienu."),
          ("Kāpēc 10 ir īpašs skaitlis?",
           "Skaidro, ka viens desmits ir desmit vieni; modelē desmitu ar "
           "sloksnīti vai klucīšiem."),
          ("Kā sauc skaitļus otrajā desmitā?",
           "Lasa un pieraksta skaitļus no 11 līdz 19; nosaka, cik pietrūkst "
           "līdz 20."),
          ("Cik ir desmitu un cik vienu?",
           "Nosaka divciparu skaitļa sastāvu (46 - 4 desmiti un 6 vieni) un "
           "modelē to."),
          ("Kā uzrakstīt to, ko dzirdi?",
           "Ar cipariem pieraksta nosauktus skaitļus līdz 100 un lasa "
           "uzrakstītus skaitļus."),
          ("Cik dažādus skaitļus var izveidot?",
           "No dotiem cipariem veido visus iespējamos divciparu skaitļus."),
          ("Kur dzīvē redzam simtu?",
           "Skaidro, ka simts ir 10 desmiti un 100 vieni; min piemērus "
           "(centi, lapas, soļi)."),
          ("Kā izskatās simta kvadrāts?",
           "Aizpilda simta kvadrātu un stāsta, kā atrast konkrēta skaitļa "
           "vietu."),
      ]),
       B("Skaitļu salīdzināšana", [
           ("Kurš skaitlis ir lielāks?",
            "Salīdzina divciparu skaitļus, vispirms salīdzinot desmitus, tad "
            "vienus."),
           ("Ko nozīmē zīmes «<» un «>»?",
            "Lieto simbolus «<» un «>» un lasa pierakstu no abām pusēm."),
           ("Kur skaitlis stāv uz skaitļu taisnes?",
            "Atliek skaitļus uz skaitļu taisnes un pamato, kāpēc viens ir "
            "lielāks nekā otrs."),
           ("Kuri skaitļi ir starp?",
            "Nosauc skaitļus, kas atrodas starp diviem dotiem skaitļiem, "
            "izmantojot simta kvadrātu."),
           ("Kā sakārtot pēc lieluma?",
            "Sakārto dotus skaitļus augošā un dilstošā secībā un pastāsta "
            "savu rīcības kārtību."),
           ("Ko var nopirkt par vienu eiro?",
            "Salīdzina cenas centos un novērtē, kuras preces var iegādāties "
            "par vienu eiro."),
           ("Cik apmēram ir?",
            "Novērtē objektu skaitu aptuveni un pārbauda, saskaitot."),
       ]),
       B("Skaitļu virknes", [
           ("Kā skaitīt pa 2, 5 un 10?",
            "Skaita uz priekšu un atpakaļ pa 2, pa 5 un pa 10, izmantojot "
            "simta kvadrātu vai lineālu."),
           ("Pēc kāda likuma virkne aug?",
            "Turpina skaitļu virkni un vārdiski raksturo likumsakarību "
            "(1; 3; 5; 7; ...)."),
           ("Kurš skaitlis pazuda?",
            "Ieraksta trūkstošos skaitļus virknē un paskaidro savu izvēli."),
           ("Vai virkni var turpināt citādi?",
            "Parāda, ka vienu virkni dažkārt var turpināt vairākos veidos, un "
            "pamato katru variantu."),
       ]),
       B("Garums: cm, dm un m", [
           ("Cik centimetru ir decimetrā?",
            "Pieraksta un lasa mērvienības cm, dm, m; pāriet no decimetriem "
            "uz centimetriem."),
           ("Kā izmērīt, ja objekts garāks par lineālu?",
            "Mēra garākus objektus un izsaka rezultātu decimetros un "
            "centimetros (14 cm = 1 dm + 4 cm)."),
           ("Cik garš ir metrs?",
            "Salīdzina metru ar savu augumu un klases priekšmetiem; nosaka "
            "iespējamo garumu un pārbauda, izmērot."),
           ("Cik rāda pulkstenis?",
            "Nolasa un parāda pilnas stundas analogajā pulkstenī; izmanto "
            "kalendāru datuma atrašanai."),
       ])],
      "Skaitļi līdz 100",
      "Lasa, pieraksta un salīdzina skaitļus līdz 100; nosaka desmitus un "
      "vienus; turpina skaitļu virkni; lieto mērvienības cm, dm un m.",
      "skaitļu virknes ar diviem likumiem; skaitļu kvadrāta fragmenti."),

    T("1.5.", "Kā saskaita un atņem skaitļus, kuri lielāki nekā 10?",
      "Apgūst un izvēlas paņēmienus saskaitīšanai un atņemšanai 20 apjomā - "
      "pamatu visām turpmākajām darbībām ar skaitļiem.",
      [B("Pieskaitīšana bez desmita pāriešanas", [
          ("Kas kopīgs 6 + 3 un 16 + 3?",
           "Pie divciparu skaitļa pieskaita viencipara skaitli, saskatot "
           "analoģiju ar pirmo desmitu."),
          ("Cik ātri zini summas 10 apjomā?",
           "Veikli saskaita un atņem 10 apjomā; stāsta savu atcerēšanās "
           "paņēmienu."),
          ("Kas notiek, ja pieskaita vairāk?",
           "Pēta konkrētos piemēros, kā mainās rezultāts, ja maina "
           "pieskaitāmo skaitli."),
          ("Vai summa mainās, mainot vietām?",
           "Secina no piemēriem, ka saskaitāmos var mainīt vietām, un lieto "
           "to aprēķinos."),
          ("Kā pierakstīt savu rēķinu?",
           "Veido darbības pierakstu un skaidro katru soli."),
          ("Cik kopā maksā divas preces?",
           "Risina sadzīves situāciju ar saskaitīšanu 20 apjomā."),
          ("Kā pārbaudīt, vai sanāca pareizi?",
           "Pārbauda saskaitīšanas rezultātu ar citu paņēmienu vai pretējo "
           "darbību."),
      ]),
       B("Saskaitīšana ar desmita pāriešanu", [
           ("Kad rodas jauns desmits?",
            "Modelē ar klucīšiem, kā, saskaitot viencipara skaitļus, veidojas "
            "pilns desmits."),
           ("Cik trūkst līdz 10?",
            "Nosaka, cik pietrūkst līdz pilnam desmitam, un izmanto to "
            "saskaitīšanā (8 + 5 = 8 + 2 + 3)."),
           ("Kā sadalīt otro saskaitāmo?",
            "Saskaita ar desmita pāriešanu, sadalot otro saskaitāmo divās "
            "daļās, un pieraksta soļus."),
           ("Cik dažādi var izveidot 15?",
            "Veido doto otrā desmita skaitli kā divu saskaitāmo summu visos "
            "iespējamos veidos."),
           ("Vai būs vairāk nekā 10?",
            "Bez precīza aprēķina nosaka, vai summa būs lielāka nekā 10 vai "
            "15, un pārbauda."),
           ("Kādā secībā saskaitīt trīs skaitļus?",
            "Izvēlas izdevīgāko saskaitīšanas secību, saskaitot trīs skaitļus "
            "20 apjomā."),
           ("Cik gara ir šī lauztā līnija?",
            "Zīmē lauztu līniju pēc nosacījumiem un aprēķina tās garumu "
            "(10-20 cm)."),
           ("Vai vari izdomāt uzdevumu draugam?",
            "Izdomā saskaitīšanas uzdevumu pēc dota nosacījuma un pārbauda "
            "klasesbiedra risinājumu."),
       ]),
       B("Atņemšana 20 apjomā", [
           ("Kas kopīgs 8 − 3 un 18 − 3?",
            "No divciparu skaitļa atņem viencipara skaitli, saskatot "
            "analoģiju ar pirmo desmitu."),
           ("Kā atņemt divciparu skaitli?",
            "Aprēķina 18 − 13 veidā, izmantojot skaitļa sastāvu."),
           ("Kā «izjaukt» desmitu?",
            "Modelē atņemšanu ar desmita sadalīšanu un skaidro soļus."),
           ("Ko nozīmē atņemt?",
            "Skaidro atņemšanu kā nezināmā saskaitāmā meklēšanu (9 − 6 - "
            "kas kopā ar 6 dod 9)."),
           ("Kā pārbaudīt starpību?",
            "Pārbauda atņemšanas rezultātu ar saskaitīšanu."),
           ("Kurš skaitlis pazudis vienādībā?",
            "Nosaka nezināmo skaitli vienādībā ar zīmēm «+», «−» un «=»."),
           ("Kas mainās, ja atņem vairāk?",
            "Veido piemērus, atņemot no viena skaitļa dažādus skaitļus, un "
            "spriež par izmaiņām."),
           ("Kāda summa uzkrīt biežāk?",
            "Ar metamajiem kauliņiem ģenerē piemērus, pieraksta rezultātus un "
            "nosaka, kuras summas atkārtojas biežāk."),
       ]),
       B("Izvēlos paņēmienu un pārbaudu", [
           ("Kuru paņēmienu izvēlēties?",
            "Saskaita un atņem 20 apjomā, izvēloties paņēmienu, un skaidro, "
            "kāpēc tas šim piemēram ir ērts."),
           ("Kā pastāstīt savu domu gaitu?",
            "Skaidro risinājumu pa soļiem un pamato, kā zina, ka rezultāts ir "
            "pareizs."),
           ("Kāds stāsts der šai izteiksmei?",
            "Nosauc piemēru no dzīves, kas atbilst dotai izteiksmei 20 "
            "apjomā."),
           ("Kur paslēpusies kļūda?",
            "Atrod kļūdu dotā risinājumā un izskaidro, kā to izlabot."),
           ("Cik veikli jau proti?",
            "Patstāvīgi risina jauktus piemērus 20 apjomā un pats pārbauda "
            "atbildes."),
       ])],
      "Saskaitīšana un atņemšana 20 apjomā",
      "Saskaita un atņem 20 apjomā, arī ar desmita pāriešanu; nosaka nezināmo "
      "vienādībā; aprēķina lauztas līnijas garumu; skaidro savu paņēmienu.",
      "trīs skaitļu saskaitīšana ar izvēlētu secību; uzdevumi ar nezināmo "
      "pirmajā pozīcijā."),

    T("1.6.", "Ko nozīmē «par tik vairāk», «par tik mazāk»?",
      "Saista sadzīves situācijas ar matemātisku darbību: situāciju vispirms "
      "izspēlē un uzzīmē, tad pieraksta un aprēķina.",
      [B("Par cik vairāk, par cik mazāk", [
          ("Par cik viena sloksnīte garāka nekā otra?",
           "Ar sloksnītēm un lineālu nosaka, par cik viens skaitlis ir "
           "lielāks nekā otrs."),
          ("Kā vienu un to pašu pateikt divējādi?",
           "Skaidro: ja viens ir par 3 lielāks nekā otrs, tad otrs ir par 3 "
           "mazāks nekā pirmais."),
          ("Kurš skaitlis ir par 4 lielāks?",
           "Aprēķina skaitli, kas ir par doto lielāks vai mazāks, ja otrs ir "
           "zināms."),
          ("Ko nozīmē «tikpat un vēl»?",
           "Modelē izteikumu «tikpat un vēl 2» un pieraksta to ar darbību."),
          ("Kā uzzīmēt divus nogriežņus?",
           "Zīmē divus nogriežņus, lai viens būtu par doto skaitli garāks "
           "nekā otrs."),
          ("Palielināt vai pamazināt?",
           "Izvēlas pareizo darbību situācijai, kurā lielumu palielina vai "
           "pamazina par doto skaitli."),
          ("Kā sakārtot pēc lieluma?",
           "Sakārto skaitļus augošā un dilstošā secībā un pamato kārtību."),
      ]),
       B("Uzdevums, ko vispirms uzzīmē", [
           ("Kā uzdevumu pārvērst zīmējumā?",
            "Attēlo shematiskā zīmējumā situāciju, kurā salīdzināti divi "
            "lielumi."),
           ("Kur uzdevumā slēpjas nezināmais?",
            "Pieraksta situāciju ar vienādību, nezināmā vietā liekot «?»."),
           ("Cik bija sākumā?",
            "Risina uzdevumu, kurā nezināmais ir sākuma lielums («pienāca "
            "klāt», «aizgāja prom»)."),
           ("Cik kopā un cik katram?",
            "Risina uzdevumu par «cik kopā», «cik vienam», «cik otram» ar "
            "nezināmo jebkurā pozīcijā."),
           ("Kāds jautājums der šim stāstam?",
            "Veido matemātisku jautājumu par tekstā doto situāciju un "
            "atbild uz to."),
           ("Kāds stāsts der šim zīmējumam?",
            "Izdomā situāciju, kas atbilst dotam shematiskam zīmējumam."),
           ("Vai atbilde ir ticama?",
            "Pārbauda atbildi pēc situācijas jēgas un paskaidro, kāpēc tā ir "
            "ticama."),
       ]),
       B("Dati tabulā un diagrammā", [
           ("Ko var uzzināt no tabulas?",
            "Nolasa datus no vienkāršas tabulas un atbild uz jautājumiem par "
            "tiem."),
           ("Kurš stabiņš ir augstākais?",
            "Lasa vienkāršu stabiņu diagrammu un salīdzina lielumus."),
           ("Par cik viens stabiņš augstāks?",
            "Nosaka pēc diagrammas, par cik viens lielums ir lielāks nekā "
            "otrs."),
           ("Kādus jautājumus var uzdot?",
            "Veido savus jautājumus par datiem tabulā vai diagrammā."),
           ("Kā savākt datus par klasi?",
            "Savāc klases datus (mājdzīvnieki, brokastis) un pieraksta tos "
            "tabulā."),
           ("Vai pieraksts ir patiess bez rēķināšanas?",
            "Salīdzina summu vai starpību ar skaitli, lietojot «<», «>», «=», "
            "neveicot precīzus aprēķinus."),
       ])],
      "Salīdzināšana un sadzīves uzdevumi 20 apjomā",
      "Nosaka, par cik viens skaitlis ir lielāks vai mazāks; attēlo situāciju "
      "shematiskā zīmējumā; risina uzdevumus ar nezināmo jebkurā pozīcijā; "
      "lasa datus tabulā un diagrammā.",
      "uzdevumi ar diviem soļiem; dati no divām tabulām."),

    T("1.7.", "Kur sastopamies ar lieliem skaitļiem?",
      "Skaitļi un darbības sadzīvē: nauda, laiks, garums, masa un tilpums; "
      "saskaitīšana un atņemšana 100 apjomā.",
      [B("Nauda - eiro un centi", [
          ("Cik maksā?",
           "Nolasa preces cenu centos un eiro; salīdzina cenas."),
          ("Kā samaksāt tieši?",
           "Ar naudas modeļiem saliek doto summu un apskata vairākus veidus, "
           "kā to samaksāt."),
          ("Cik jāizdod atpakaļ?",
           "Izspēlē iepirkšanos, nosakot pirkuma summu un izdodamo naudu."),
          ("Ko iekļaut iepirkumu sarakstā?",
           "Veido iepirkumu sarakstu ar daudzumu un cenu; ieraksta datus "
           "tabulā."),
          ("Vai pietiks naudas?",
           "Novērtē, vai dotā summa pietiek pirkumam, un pamato atbildi."),
          ("Kura summa ir lielāka?",
           "Salīdzina naudas vērtības eiro un centos, pierakstot «<», «>» vai "
           "«=»."),
      ]),
       B("Laiks un pulkstenis", [
           ("Kā uzbūvēt savu pulksteni?",
            "Pēc dotām norādēm izveido pulksteņa modeli un parāda ar to "
            "pilnas stundas."),
           ("Cik ir pusseptiņi?",
            "Nolasa un parāda pilnas stundas un pusstundas analogajā "
            "pulkstenī."),
           ("Kā skaitīt pa 5 minūtēm?",
            "Nosaka laiku ar 5 minūšu intervālu, saistot to ar skaitīšanu pa "
            "5."),
           ("Cik rādīs pēc 15 minūtēm?",
            "Nosaka pulksteņa laiku pēc noteikta laika sprīža."),
           ("Cik ilgi?",
            "Aprēķina notikuma ilgumu pilnās stundās un minūtēs; lieto "
            "jēdzienus stunda un minūte."),
           ("Kā izskatās mana diena?",
            "Izmanto laika norāžu tabulu vai sarakstu savas dienas plānam."),
       ]),
       B("Garums, masa un tilpums", [
           ("Kā izveidot savu metramēru?",
            "Izveido metramēru ar decimetru iedaļām un izmēra objektus "
            "klasē."),
           ("Metros, decimetros vai centimetros?",
            "Izsaka viena objekta garumu vairākās mērvienībās un salīdzina "
            "pierakstus."),
           ("Kas ir puse no metra?",
            "Praktiski, pārlokot mērlenti, nosaka pusi no metra un pusi no "
            "decimetra."),
           ("Cik smags un cik daudz?",
            "Lieto kilogramu un litru, nosakot preču masu un tilpumu "
            "situācijās no veikala."),
           ("Kā pierakstīt mērījumus?",
            "Veido vienkāršu tabulu mērījumiem un aprēķiniem; pieraksta "
            "rezultātu ar mērvienību."),
       ]),
       B("Saskaitīšana un atņemšana 100 apjomā", [
           ("Kā saskaitīt pilnus desmitus?",
            "Saskaita un atņem pilnus desmitus 100 apjomā, saskatot analoģiju "
            "ar vieniem."),
           ("Kā pieskaitīt desmitus divciparu skaitlim?",
            "Divciparu skaitlim pieskaita un atņem pilnus desmitus; nosauc "
            "par 10 lielāku vai mazāku skaitli."),
           ("Kā pieskaitīt vienus?",
            "Divciparu skaitlim pieskaita un atņem viencipara skaitli, "
            "izmantojot simta kvadrātu."),
           ("Cik apmēram sanāks?",
            "Nosaka aptuveno rezultātu un pēc tam pārbauda to ar aprēķinu."),
           ("Kurš skaitlis trūkst?",
            "Nosaka vienādībā nezināmo lielumu ar paņēmienu «mēģinu un "
            "pārbaudu»."),
           ("Kā izteiksmē ielikt savu iepirkumu?",
            "Veido savu izteiksmi par reālu situāciju ar nosauktiem skaitļiem "
            "un aprēķina rezultātu."),
       ])],
      "Nauda, laiks, mērvienības un skaitļi līdz 100",
      "Rēķina ar eiro un centiem; nosaka laiku ar 5 minūšu precizitāti; mēra "
      "un pieraksta garumu, masu un tilpumu; saskaita un atņem 100 apjomā.",
      "laiks ar minūtes precizitāti digitālajā pulkstenī; vairāku pirkumu "
      "kopsummas."),

    T("1.8.", "Kā apraksta un veido figūras?",
      "Novēro, veido un raksturo plaknes un telpiskas figūras; mācās pateikt, "
      "kas figūrai ir būtisks un kas - nav.",
      [B("Figūru dalīšana daļās", [
          ("Kas figūrai ir svarīgs?",
           "Nosaka figūras būtiskās īpašības (malu skaits) un nebūtiskās "
           "(krāsa, lielums)."),
          ("Kā uzzīmēt pēc nosacījumiem?",
           "Zīmē figūru pēc dotiem nosacījumiem (sešstūris; daudzstūris ar "
           "divām vienādām malām)."),
          ("Kā pierakstīt zīmēšanas soļus?",
           "Sadala soļos kvadrāta zīmēšanu rūtiņu lapā un pieraksta "
           "algoritmu."),
          ("Vai cita pieraksts strādā?",
           "Izpilda cita skolēna uzrakstīto algoritmu un, ja vajag, izlabo "
           "to."),
          ("Kā sadalīt vienādās daļās?",
           "Sadala taisnstūri un riņķi divās un četrās vienādās daļās; "
           "salīdzina dažādus risinājumus."),
          ("Kādas figūras rodas?",
           "Sadala daudzstūri ar taisnu līniju un nosauc, kādas figūras "
           "izveidojas."),
      ]),
       B("Simetrija ap mums", [
           ("Vai figūras ir vienādas?",
            "Pārliecinās par divu figūru vienādību, tās savietojot, un zīmē "
            "rūtiņu lapā figūru, kas vienāda ar doto."),
           ("Cik locījuma līniju ir kvadrātam?",
            "Atrod figūrai visas simetrijas līnijas un parāda, ka to var būt "
            "vairākas."),
           ("Kur dabā ir simetrija?",
            "Atrod attēlus ar simetriskiem dabas objektiem un pamato savu "
            "izvēli."),
           ("Kā uzzīmēt otru pusi?",
            "Zīmē rūtiņu lapā vienkāršu simetrisku figūru pēc dotās puses."),
           ("Kādu rotājumu izveidosi?",
            "Veido simetrisku rotājumu vai apsveikuma kartīti izvēlētā "
            "tehnikā."),
       ]),
       B("Telpiskas figūras", [
           ("Cik kociņu vajag kubam?",
            "Nosaka kuba modeļa izveidei nepieciešamo kociņu un savienojumu "
            "skaitu; lieto vārdus virsotne un šķautne."),
           ("Cik dažādas figūras no četriem kubiem?",
            "Veido no vienāda kubu skaita dažādas telpiskas figūras un spriež "
            "par to skaitu."),
           ("Vai no visām pusēm izskatās vienādi?",
            "Apraksta telpisku figūru no dažādām pusēm; saskata, ka skats var "
            "atšķirties."),
           ("Kā uzbūvēt ēkas modeli?",
            "Plāno un veido telpisku modeli, iepriekš nosakot vajadzīgo kubu "
            "skaitu."),
           ("Cik kubu būs nākamajā?",
            "Veido telpisku figūru virkni un aprēķina kubu skaitu nākamajā "
            "figūrā."),
       ])],
      "Plaknes un telpiskas figūras",
      "Apraksta un grupē figūras pēc īpašībām; sadala figūru vienādās daļās; "
      "zīmē simetrisku figūru; veido un raksturo telpiskus modeļus.",
      "figūru dalīšanas pētījums grupās; kubu figūru skati no trim pusēm."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 1. klasē", [
        ("Kur gada laikā noderēja matemātika?",
         "Apkopo gadā apgūto: skaitīšana, saskaitīšana un atņemšana, "
         "mērīšana, figūras; min piemērus no savas dzīves."),
        ("Cik veikli rēķinu 20 apjomā?",
         "Formatīvi pārbauda saskaitīšanas un atņemšanas veiklību 20 apjomā "
         "un atzīmē, kas vēl jātrenē."),
        ("Kā risinu uzdevumu ar zīmējumu?",
         "Risina sadzīves uzdevumu, vispirms to uzzīmējot, un skaidro "
         "risinājumu klasesbiedram."),
        ("Ko gribu iemācīties 2. klasē?",
         "Formulē, kas padodas viegli un kas vēl jāatkārto; iepazīstas ar to, "
         "kas gaida 2. klasē."),
    ]),
]
