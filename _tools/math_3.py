# -*- coding: utf-8 -*-
"""3. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 3. klases sadaļa.
Daļas plānā rakstītas ar vārdiem (puse, trešdaļa), jo tabulas ailē daļsvītra
nav lasāma; stundās daļas raksta ar daļsvītru latviešu standartā.
"""

from math_plani import B, T

IEVADS = (
    "Trešais matemātikas gads. Pabeidz reizināšanas tabulu, sāk reizināt un "
    "dalīt divciparu skaitļus, rēķina 1000 apjomā un pirmo reizi satiek "
    "daļskaitļus - gan parastās daļas, gan decimāldaļas naudā. Ģeometrijā nāk "
    "klāt leņķis, laukums un tilpums, un gads ietver divus praktiskus darbus: "
    "telpas plānu ar mērogu un telpisku figūru izklājumus.")

TEMATI = [
    T("3.1.", "Kā reizina un dala ar 6, 7, 8, 9 un 10?",
      "Nostiprina reizināšanas tabulu līdz 10 un pārnes prasmi uz divciparu "
      "skaitļu reizināšanu un dalīšanu ar viencipara skaitli.",
      [B("Reizināšana ar 6 un 7", [
          ("Ko jau proti no reizināšanas tabulas?",
           "Atkārto reizināšanu un dalīšanu ar 2, 3, 4 un 5 un atzīmē, kuri "
           "reizinājumi vēl jāapgūst."),
          ("Kāpēc pietiek iemācīties pusi tabulas?",
           "Skaidro īpašību a · b = b · a un izmanto to, lai samazinātu "
           "iegaumējamo reizinājumu skaitu."),
          ("Kā modelēt reizinājumu ar 6?",
           "Modelē reizinājumus ar 6 ar rūtiņās sadalītu taisnstūri un "
           "pieraksta rezultātus."),
          ("Kā atcerēties reizinājumus ar 6?",
           "Izstrādā savu stratēģiju (reizina ar 5 un pieskaita vēl vienu "
           "daudzumu) un pārbauda to."),
          ("Kā izskatās reizināšana uz skaitļu taisnes?",
           "Attēlo reizināšanu uz skaitļu taisnes kā vienādus soļus."),
          ("Kas jauns ir reizinājumos ar 7?",
           "Modelē reizinājumus ar 7 un papildina reizināšanas tabulu."),
          ("Kā trenēties ar kartītēm?",
           "Papildina kartīšu komplektu un vingrinās pārī, atzīmējot "
           "iegaumētos reizinājumus."),
          ("Cik veikli jau rēķini?",
           "Veikli nosauc reizinājumus ar 6 un 7 un paskaidro savu "
           "atcerēšanās paņēmienu."),
      ]),
       B("Reizināšana ar 8, 9 un 10", [
           ("Kā reizināšana ar 8 saistās ar reizināšanu ar 4?",
            "Iegūst reizinājumus ar 8, dubultojot reizinājumus ar 4."),
           ("Kāds triks palīdz reizināt ar 9?",
            "Atklāj likumsakarību reizinājumos ar 9 un pārbauda to ar "
            "modeli."),
           ("Kas notiek, reizinot ar 10?",
            "Formulē likumsakarību par reizinājumu ar 10 un lieto to "
            "aprēķinos."),
           ("Kā izskatās pabeigta reizināšanas tabula?",
            "Pabeidz un pārskata visu reizināšanas tabulu; atrod tajā "
            "atkārtojumus."),
           ("Kuri skaitļi dalās ar 5 un kuri ar 10?",
            "Simta kvadrātā iekrāso skaitļus, kas dalās ar 5 vai 10, un "
            "apraksta pamanīto."),
           ("Kā skaitli uzrakstīt kā reizinājumu?",
            "Uzraksta doto skaitli kā divu skaitļu reizinājumu vairākos "
            "veidos."),
           ("Kā trenēties ar digitālu rīku?",
            "Izmanto lietotni reizināšanas tabulas trenēšanai un seko savam "
            "progresam."),
           ("Cik daudz tabulas zini no galvas?",
            "Formatīvi pārbauda visu reizināšanas tabulu un izvēlas "
            "trenējamo."),
       ]),
       B("Dalīšana tabulas apjomā", [
           ("Kā reizinājums palīdz atrast dalījumu?",
            "Nosaka dalījumu, domājot par atbilstošo reizinājumu, un pārbauda "
            "rezultātu."),
           ("Vienādās daļās vai pa vienādi?",
            "Skaidro abas dalīšanas nozīmes ar praktisku piemēru."),
           ("Ko dara ar 1 un 0?",
            "Secina un lieto sakarības 1 · a = a, a : 1 = a, 0 · a = 0; "
            "skaidro, kāpēc ar 0 dalīt nevar."),
           ("Cik vienādās daļās var sadalīt figūru?",
            "Dala rūtiņās sadalītu taisnstūri 2-10 vienādās daļās un nosaka "
            "vienas daļas lielumu."),
           ("Cik zīmuļus var nopirkt?",
            "Risina sadzīves uzdevumu ar dalīšanu, izmantojot naudas "
            "modeļus."),
           ("Kā pārbaudīt dalījumu?",
            "Pārbauda dalīšanu ar reizināšanu un skaidro savu pierakstu."),
           ("Kāds uzdevums der šai darbībai?",
            "Izdomā situāciju, kas atbilst dotai reizināšanas vai dalīšanas "
            "darbībai."),
           ("Cik veikli dali?",
            "Patstāvīgi dala tabulas apjomā un pārbauda rezultātus."),
       ]),
       B("Divciparu skaitļu reizināšana un dalīšana", [
           ("Kā reizināt 23 ar 2?",
            "Reizina divciparu skaitli ar viencipara skaitli, atsevišķi "
            "reizinot desmitus un vienus."),
           ("Kāpēc drīkst reizināt pa daļām?",
            "Ar modeli formulē īpašību (a + b) · c = a · c + b · c savos "
            "vārdos."),
           ("Kā dalīt 48 ar 4?",
            "Dala divciparu skaitli ar viencipara skaitli, izmantojot "
            "decimālā sastāva modeli."),
           ("Cik apmēram sanāks?",
            "Prognozē reizinājuma vai dalījuma aptuveno vērtību un pārbauda "
            "to."),
           ("Kā aug virkne, kas trīskāršojas?",
            "Veido virknes, kurās katrs nākamais skaitlis ir 2 vai 3 reizes "
            "lielāks vai mazāks."),
           ("Pērku divreiz vairāk - cik maksā?",
            "Formulē sakarību starp preču daudzumu un pirkuma summu, ja cena "
            "nemainās."),
           ("Kā atrisināt divu darbību uzdevumu?",
            "Risina divu darbību situāciju uzdevumu ar reizināšanu un "
            "dalīšanu, pierakstot izteiksmi."),
           ("Kāds uzdevums sanāk tev?",
            "Veido savu uzdevumu ar reizināšanu vai dalīšanu un izvērtē "
            "klasesbiedra uzdevumu."),
       ])],
      "Reizināšana un dalīšana līdz 10; divciparu skaitļi",
      "Reizina un dala reizināšanas tabulas apjomā; reizina un dala divciparu "
      "skaitli ar viencipara skaitli; risina viena un divu darbību uzdevumus.",
      "reizināšana ar pāreju citā desmitā; trīs skaitļu reizinājums."),

    T("3.2.", "Kā izmanto visas darbības?",
      "Pilnveido visas četras darbības 100 apjomā, darbību secību "
      "vairākdarbību izteiksmēs un taisnstūra perimetra formulu.",
      [B("Cik labi protu rēķināt?", [
          ("Ko es jau protu un ko vēl ne?",
           "Novērtē savas rēķināšanas prasmes ar piemēriem un formulē mērķi "
           "to pilnveidei."),
          ("Cik veikli rēķinu galvā?",
           "Veikli saskaita un atņem 20 apjomā un reizina tabulas apjomā."),
          ("Kā izveidot savu treniņu plānu?",
           "Sastāda rīcības plānu prasmju pilnveidei un vienojas par "
           "pārbaudes laiku."),
          ("Kurš paņēmiens man der?",
           "Salīdzina vairākus rēķināšanas paņēmienus un izvēlas sev "
           "piemērotāko."),
          ("Kā pārbaudīt savu darbu?",
           "Pārbauda rezultātus ar pretējo darbību un ar aptuveno vērtību."),
      ]),
       B("Izteiksmes un darbību secība", [
           ("Kura darbība ir pirmā?",
            "Nosaka darbību secību: vispirms iekavas, tad reizināšana un "
            "dalīšana, tad saskaitīšana un atņemšana."),
           ("Kā pieraksta risinājumu ar izteiksmi?",
            "Dotam tekstam veido risinājumu gan pa darbībām, gan kā vienu "
            "izteiksmi."),
           ("Kā aprēķināt izteiksmi ar iekavām?",
            "Aprēķina izteiksmes vērtību, kurā ir 2-4 darbības un iekavas."),
           ("Kā izskatās saistītais pieraksts?",
            "Veido saistīto pierakstu, izpildītās darbības vietā rakstot "
            "rezultātu."),
           ("Kur risinājumā ir kļūda?",
            "Pārbauda dotu risinājumu, atrod kļūdu un komentē tās cēloni."),
           ("Cik izteiksmes var izveidot no trim skaitļiem?",
            "Grupā veido pēc iespējas vairāk dažādu izteiksmju no dotiem "
            "skaitļiem, zīmēm un iekavām."),
           ("Vai visas izteiksmes ir atrastas?",
            "Spriež, vai izveidoti visi gadījumi, un atlasa tās izteiksmes, "
            "kurām var aprēķināt vērtību."),
           ("Kāds teksts der šai izteiksmei?",
            "Veido situācijas aprakstu, kas atbilst dotai vairākdarbību "
            "izteiksmei."),
       ]),
       B("Uzdevumi par naudu un dzīvi", [
           ("Kā samaksāt vajadzīgo summu?",
            "Ar naudas modeļiem atrod pēc iespējas vairāk veidu, kā samaksāt "
            "doto summu."),
           ("Ko var nopirkt par šo naudu?",
            "Izvēlas preces par doto summu un pieraksta atbilstošu "
            "izteiksmi."),
           ("Cik jāmaksā par klases pasākumu?",
            "Risina 2-3 darbību uzdevumu, veidojot shematisku zīmējumu un "
            "pierakstot risinājumu."),
           ("Vai atbilde atbilst situācijai?",
            "Pārliecinās, ka rezultāts ir ticams un atbilst reālajai "
            "situācijai."),
           ("Kā pastāstīt savu risinājumu?",
            "Uzskatāmi attēlo un pamato savu risinājumu klasesbiedriem."),
       ]),
       B("Taisnstūra perimetra formula", [
           ("Cik dažādi var aprēķināt perimetru?",
            "Aprēķina taisnstūra perimetru pa darbībām un kā vienu izteiksmi; "
            "salīdzina paņēmienus."),
           ("Kā pateikt formulu ar vārdiem?",
            "Formulē taisnstūra perimetra aprēķināšanu vārdiski."),
           ("Ko nozīmē burti formulā?",
            "Lasa un skaidro formulas pierakstu ar burtiem un atrod tam "
            "atbilstošo vārdisko formulējumu."),
           ("Cik taisnstūru ar vienādu perimetru?",
            "Zīmē rūtiņu tīklā visus taisnstūrus ar dotu perimetru un pamato, "
            "ka atrasti visi."),
           ("Kāds perimetrs rodas, figūras savietojot?",
            "Kombinē figūras un pieraksta izteiksmi jaunās figūras "
            "perimetram."),
       ])],
      "Četras darbības, izteiksmes un perimetrs",
      "Veic četras darbības 100 apjomā; aprēķina vairākdarbību izteiksmes "
      "vērtību, ievērojot darbību secību; aprēķina taisnstūra perimetru un "
      "risina 2-3 darbību uzdevumus.",
      "izteiksmes ar dubultajām iekavām; uzdevumi ar vairākiem risinājumiem."),

    T("3.3.", "Kā veido vietas plānu?",
      "Praktisks temats: mērījumi dabā, samazinājums un telpas plāns; ceļā uz "
      "to - skaitļi līdz 1000 un reizināšana ar 10 un 100.",
      [B("Kas ir plāns un kā to veido", [
          ("Ko var ieraudzīt evakuācijas plānā?",
           "Aplūko dažādus telpu plānus un stāsta, kā tie veidoti."),
          ("Ko nozīmē samazināt vienādu skaitu reižu?",
           "Skaidro, ka plānā visi lielumi samazināti vienādu skaitu reižu."),
          ("Kādas prasmes mums vēl trūkst?",
           "Kopā veido darbības plānu klases attēlošanai un nosaka, kādas "
           "prasmes vēl vajadzīgas."),
          ("Kā sadalīt darbu grupā?",
           "Vienojas grupā par pienākumiem un darba gaitu."),
      ]),
       B("Mērīšana un lielie skaitļi", [
           ("Kā izlasīt četrciparu skaitli?",
            "Lasa un raksta trīsciparu un četrciparu skaitļus; nosaka to "
            "decimālo sastāvu."),
           ("Kā skaitli pierakstīt kā summu?",
            "Pieraksta skaitli izvērstā formā (605 = 600 + 5 = 6 · 100 + 5)."),
           ("Kas notiek, reizinot ar 10 un 100?",
            "Reizina un dala ar 10 un 100; ar kalkulatoru pārbauda un "
            "formulē likumsakarību."),
           ("Cik tas ir centimetros?",
            "Izsaka metrus centimetros un centimetrus milimetros."),
           ("Cik precīzi jāmēra?",
            "Mēra telpas izmērus, noapaļo mērījumus līdz pilniem desmitiem "
            "centimetru."),
           ("Kā apkopot mērījumus?",
            "Veido tabulu mērījumiem, precīzi norādot mērāmo objektu un "
            "mērvienību."),
       ]),
       B("Telpas plāna izveide", [
           ("Kādu samazinājumu izvēlēties?",
            "Salīdzina, kā izmēri izskatās, samazinot 10 un 20 reizes, un "
            "izvēlas piemērotāko."),
           ("Cik liels objekts ir plānā?",
            "Aprēķina objektu izmērus plānā, izmantojot kalkulatoru."),
           ("Kā uzzīmēt telpas plānu?",
            "Izveido telpas plānu, attēlojot logus, durvis un galvenos "
            "objektus."),
           ("Vai plāns ir labs?",
            "Prezentē plānu, salīdzina to ar citu grupu plāniem un izvērtē "
            "pēc kritērijiem."),
       ])],
      "Mērogs, mērījumi un skaitļi līdz 1000",
      "Lasa un raksta skaitļus līdz 1000 un lielākus; reizina un dala ar 10 "
      "un 100; izsaka garumu mazākās vienībās; veido un lasa telpas plānu ar "
      "izvēlētu samazinājumu.",
      "samazinājums 25 vai 50 reizes; apkārtnes plāns ar vairākām telpām."),

    T("3.4.", "Ko nozīmē daļa no veselā?",
      "Veido sākotnējo izpratni par daļskaitļiem - parastajām daļām un "
      "decimāldaļām, ko satiek naudā un mērījumos.",
      [B("Veselais un daļa", [
          ("Kā sadalīt riņķi vienādās daļās?",
           "Saloka riņķi un taisnstūri 2, 4 un 8 vienādās daļās un nosauc "
           "iegūtās daļas."),
          ("Kā sadalīt sloksnīti trīs daļās?",
           "Saloka sloksnīti 3 un 6 vienādās daļās un pārbauda, vai daļas ir "
           "vienādas."),
          ("Kur uz lineāla ir desmitdaļas?",
           "Parāda, ka 1 cm ir sadalīts 10 vienādās daļās, un nosauc vienu "
           "daļu."),
          ("Cik liela ir viena daļa?",
           "Vērojot vienādās daļās sadalītu nogriezni, nosaka daļu skaitu un "
           "vienas daļas lielumu."),
          ("Cik daļu ir iekrāsotas?",
           "Iekrāso figūrā doto daļu skaitu un nosauc iekrāsoto daļu."),
          ("Kā daļu parāda pulkstenis?",
           "Ar pulksteņa modeli parāda pusi un ceturtdaļu no stundas."),
          ("Cik liels bija veselais?",
           "Papildina figūru līdz veselajam, ja redzama tikai tā daļa."),
          ("Cik dažādi var sadalīt taisnstūri?",
           "Dala vienādu taisnstūri vienādās daļās dažādos veidos un "
           "salīdzina rezultātus."),
      ]),
       B("Daļskaitļa pieraksts", [
           ("Kā pieraksta daļu?",
            "Lasa un pieraksta parasto daļu; nosauc skaitītāju un saucēju."),
           ("Ko rāda saucējs un ko skaitītājs?",
            "Skaidro, ka saucējs rāda dalījumu skaitu, bet skaitītājs - ņemto "
            "daļu skaitu."),
           ("Kā atcerēties, kurš ir kurš?",
            "Stāsta savu atcerēšanās stratēģiju un pārbauda to piemēros."),
           ("Kāda daļa ir iekrāsota un kāda - ne?",
            "Pieraksta daļskaitli figūras iekrāsotajai un neiekrāsotajai "
            "daļai."),
           ("Kur uz skaitļu taisnes ir puse?",
            "Atliek daļskaitli uz skaitļu taisnes un pamato tā vietu."),
           ("Kā saskaitīt daļas ar vienādu saucēju?",
            "Ar modeli saskaita un atņem parastās daļas ar vienādiem "
            "saucējiem."),
           ("Kāds ir tavs piemērs?",
            "Rada savu piemēru ar daļām un parāda to ar modeli."),
           ("Kāda daļa ir mazāka nekā viens?",
            "Skaidro, ka īsta daļa atrodas starp 0 un 1, un min piemērus."),
       ]),
       B("Daļskaitļu salīdzināšana", [
           ("Kura daļa ir lielāka?",
            "Salīdzina daļas ar vienādiem saucējiem un pamato ar modeli."),
           ("Puse vai trešdaļa?",
            "Salīdzina pamatdaļas ar dažādiem saucējiem un skaidro, kāpēc "
            "lielāks saucējs dod mazāku daļu."),
           ("Kā salīdzināt uz skaitļu taisnes?",
            "Izmanto skaitļu taisni daļu salīdzināšanai un pieraksta "
            "salīdzinājumu ar «<» vai «>»."),
           ("Vai puse vienmēr ir vienāda?",
            "Pēta, ka daļa ir atkarīga no veselā lieluma, un min piemērus."),
           ("Kad daļa ir vesels?",
            "Modelē gadījumus, kad daļa veido veselo (četras ceturtdaļas ir "
            "viens)."),
           ("Vai vienu skaitli var pierakstīt dažādi?",
            "Ar modeli parāda, ka puse ir tas pats, kas divas ceturtdaļas."),
           ("Cik daļu vajag līdz veselam?",
            "Nosaka, cik daļu pietrūkst līdz veselajam."),
           ("Kurš apgalvojums ir patiess?",
            "Izvērtē apgalvojumus par daļām un pamato ar modeli vai "
            "pretpiemēru."),
       ]),
       B("Decimāldaļas un daļa no skaita", [
           ("Kā desmitdaļu pieraksta ar komatu?",
            "Pieraksta daļu ar saucēju 10 kā decimāldaļu un lasa to "
            "divējādi."),
           ("Kā ar komatu pieraksta centus?",
            "Izsaka naudas summu centos kā eiro un otrādi; skaidro pierakstu "
            "0,01."),
           ("Kas ir simtdaļa?",
            "Lasa un pieraksta simtdaļas; saista tās ar daļu, kuras saucējs "
            "ir 100."),
           ("Kā saskaitīt centus?",
            "Ar naudas modeļiem saskaita vienkāršas decimāldaļas un skaidro "
            "līdzību ar veselo skaitļu saskaitīšanu."),
           ("Cik ir puse no divpadsmit?",
            "Nosaka daļu no skaita praktiskā situācijā un pieraksta "
            "spriedumu."),
           ("Kāda daļa no stundas ir 15 minūtes?",
            "Ar pulksteņa modeli nosaka daļu no stundas."),
           ("Kāda daļa no decimetra ir centimetrs?",
            "Ar lineālu nosaka daļu no garuma mērvienības."),
           ("Kur dzīvē noder daļas?",
            "Risina sadzīves uzdevumus, kuros jānosaka daļa no lieluma vai "
            "skaita."),
       ])],
      "Daļskaitļi un decimāldaļas",
      "Nosaka un pieraksta daļu no veselā; atliek daļu uz skaitļu taisnes; "
      "salīdzina daļas; lasa un pieraksta desmitdaļas un simtdaļas; nosaka "
      "daļu no skaita.",
      "daļu saskaitīšana ar dažādiem saucējiem modelī; jaukti skaitļi."),

    T("3.5.", "Kādi lielumi raksturo figūru?",
      "Pilnveido izpratni par malu garumiem, perimetru un laukumu; iepazīst "
      "leņķi un tilpumu.",
      [B("Leņķi un figūru īpašības", [
          ("Kas taisnstūrim ir īpašs?",
           "Raksturo taisnstūri un kvadrātu, nosaucot kopīgās un atšķirīgās "
           "īpašības."),
          ("Kāpēc figūra ar vienādām malām var izskatīties citādi?",
           "Salīdzina taisnstūri ar figūru, kurai tādas pašas malas, bet "
           "leņķi nav taisni."),
          ("Kas ir leņķis?",
           "Parāda leņķus daudzstūros un apkārtnē; lieto jēdzienu leņķis."),
          ("Šaurs, taisns vai plats?",
           "Pēc acumēra nosaka leņķa veidu un pārbauda to ar uzstūri."),
          ("Kā ar locīšanu iegūt taisnu leņķi?",
           "Lokot papīru, iegūst taisnus, šaurus un platus leņķus."),
          ("Kā uzzīmēt četrstūri ar diviem taisniem leņķiem?",
           "Zīmē vai veido daudzstūrus pēc dotām pazīmēm."),
          ("Kā uzzīmēt riņķi?",
           "Zīmē riņķi ar cirkuli; skaidro, ka riņķa lielumu nosaka rādiuss."),
      ]),
       B("Taisnstūra laukums", [
           ("Cik rūtiņu ietilpst figūrā?",
            "Nosaka figūras laukumu, skaitot vienādas rūtiņas."),
           ("Kā aprēķināt, nenoklājot visu?",
            "Saskata, ka laukumu var iegūt, rindas kvadrātu skaitu reizinot "
            "ar rindu skaitu."),
           ("Kā pateikt laukuma aprēķinu ar vārdiem?",
            "Formulē vārdisku taisnstūra laukuma aprēķināšanas sakarību."),
           ("Kurš laukums ir lielāks?",
            "Salīdzina laukumus, figūras uzliekot vienu uz otras vai "
            "aprēķinot."),
           ("Kā izmērīt lapas laukumu?",
            "Ar caurspīdīgu rūtiņu režģi nosaka neregulāras figūras aptuveno "
            "laukumu."),
           ("Vai dažādām figūrām var būt vienāds laukums?",
            "Zīmē dažādus taisnstūrus ar vienādu laukumu un pamato atbildi."),
           ("Kas notiek ar laukumu, mainot malas?",
            "Pēta, kā mainās laukums, mainot malu garumus, un formulē "
            "pamanīto."),
           ("Vai apgalvojums ir patiess?",
            "Veido pretpiemēru, lai apgāztu aplamu apgalvojumu par "
            "taisnstūriem."),
       ]),
       B("Tilpums", [
           ("Cik kubu ietilpst kastē?",
            "No vienādiem kubiem veido taisnstūru skaldni un nosaka tā "
            "tilpumu kubos."),
           ("Kurā traukā ietilpst vairāk?",
            "Salīdzina trauku tilpumus, izmantojot beramus produktus vai "
            "ūdeni."),
           ("Kā nolasīt mērtrauku?",
            "Nolasa mērtrauka skalu litros un mililitros."),
           ("Cik litru vajag?",
            "Veic vienkāršus aprēķinus ar tilpumu sadzīves situācijā."),
           ("Kas kopīgs diviem ķermeņiem?",
            "Salīdzina ķermeņus pēc tilpuma un formas; raksturo kopīgo un "
            "atšķirīgo."),
           ("Kā izmērīt neregulāru ķermeni?",
            "Izsaka un pārbauda idejas, kā salīdzināt tilpumu, ja kubi "
            "neder."),
       ])],
      "Leņķi, laukums un tilpums",
      "Nosaka leņķa veidu; aprēķina taisnstūra laukumu; zīmē figūras pēc "
      "nosacījumiem; nosaka taisnstūru skaldņa tilpumu kubos un nolasa "
      "mērtrauka skalu.",
      "figūras ar vienādu laukumu un dažādu perimetru; riņķa rādiuss un "
      "diametrs."),

    T("3.6.", "Kā saskaita un atņem trīsciparu skaitļus?",
      "Pārnes darbības 100 apjomā uz skaitļiem līdz 1000 un lieto tās "
      "reālās situācijās ar garumu, masu un tilpumu.",
      [B("Trīsciparu skaitļi", [
          ("Kā izlasīt un uzrakstīt lielu skaitli?",
           "Lasa un raksta skaitļus līdz 1000 ar cipariem un vārdiem."),
          ("Cik simtu, desmitu un vienu?",
           "Nosaka trīsciparu skaitļa decimālo sastāvu un pieraksta to "
           "izvērstā formā."),
          ("Kurš skaitlis ir lielāks?",
           "Salīdzina divus trīsciparu skaitļus un pieraksta ar «>» vai «<»."),
          ("Kā sakārtot skaitļus?",
           "Sakārto skaitļus augošā un dilstošā secībā un skaidro savu "
           "kārtību."),
          ("Kur skaitlis atrodas uz skaitļu taisnes?",
           "Attēlo skaitļus uz skaitļu taisnes ar dotu iedaļas vērtību."),
          ("Kurš skaitlis trūkst?",
           "Ievieto trūkstošos skaitļus virknē un pamato izvēli."),
          ("Cik ir desmit simtu?",
           "Skaidro, ka desmit simti veido tūkstoti, un modelē to."),
      ]),
       B("Saskaitīšana 1000 apjomā", [
           ("Kā saskaitīt simtus?",
            "Saskaita pilnus simtus un desmitus, saskatot analoģiju ar "
            "vieniem."),
           ("Kā saskaitīt trīsciparu skaitļus galvā?",
            "Saskaita trīsciparu skaitļus galvā, izmantojot decimālo "
            "sastāvu."),
           ("Kāpēc izdevīgi rakstīt vienu zem otra?",
            "Veido saskaitīšanas pierakstu stabiņā un skaidro katru soli."),
           ("Kad rodas jauns simts?",
            "Saskaita ar pāreju jaunā desmitā un simtā; modelē to."),
           ("Kādā secībā saskaitīt vairākus skaitļus?",
            "Saskaita 2-4 divciparu skaitļus, izvēloties izdevīgu secību."),
           ("Cik apmēram sanāks?",
            "Novērtē summas aptuveno vērtību un izmanto to pārbaudei."),
           ("Kā pārbaudīt savu darbu?",
            "Pārbauda summu ar pretējo darbību vai citu paņēmienu."),
       ]),
       B("Atņemšana 1000 apjomā", [
           ("Kā atņemt pilnus simtus?",
            "Atņem pilnus simtus un desmitus un skaidro savu paņēmienu."),
           ("Kad simts jāsadala desmitos?",
            "Atņem ar aizņēmumu, modelējot simta sadalīšanu desmitos."),
           ("Kā pieraksta atņemšanu stabiņā?",
            "Veido atņemšanas pierakstu stabiņā un aprēķina starpību."),
           ("Kā pārbaudīt starpību?",
            "Pārbauda atņemšanu ar saskaitīšanu."),
           ("Cik pietrūkst līdz 1000?",
            "Aprēķina, cik pietrūkst līdz pilnam simtam vai tūkstotim."),
           ("Kur ir kļūda?",
            "Atrod kļūdu dotā risinājumā un izskaidro tās cēloni."),
           ("Cik veikli rēķini?",
            "Patstāvīgi saskaita un atņem 1000 apjomā, pārbaudot atbildes."),
       ]),
       B("Lielumi, dati un situācijas", [
           ("Cik gara ir figūras apmale?",
            "Aprēķina dažādmalu figūru perimetrus, ja malas ir divciparu un "
            "trīsciparu skaitļi."),
           ("Cik smaga ir prece?",
            "Lieto gramus un kilogramus; saprot, ka 0,357 kg ir 357 g."),
           ("Milimetri, metri vai kilometri?",
            "Salīdzina garumus, kas izteikti mm, cm, m un km, un pārveido "
            "tos."),
           ("Cik tālu ir kilometrs?",
            "Novērtē attālumu, masu un tilpumu aptuveni un pārbauda "
            "novērtējumu."),
           ("Kā savākt un pierakstīt mērījumus?",
            "Plāno un veic mērījumus apkārtnē, apkopojot tos tabulā."),
           ("Ko stāsta diagramma?",
            "Lasa stabiņu un joslu diagrammu, kurā viena iedaļa atbilst 10 "
            "vai 100 objektiem."),
           ("Cik maksās klases pasākums?",
            "Grupā plāno pasākuma izmaksas, izmantojot datus no teksta un "
            "tabulas."),
       ])],
      "Saskaitīšana un atņemšana 1000 apjomā",
      "Lasa, raksta un salīdzina skaitļus līdz 1000; saskaita un atņem 1000 "
      "apjomā, arī rakstot stabiņā; rēķina ar garumu, masu un tilpumu; risina "
      "situāciju uzdevumus.",
      "aprēķini ar skaitļiem līdz 10 000; vairāku soļu izmaksu plāns."),

    T("3.7.", "Kā veido telpiskus modeļus?",
      "Attīsta ģeometrisko iztēli, praktiski darbojoties ar plaknes un "
      "telpiskām figūrām un to izklājumiem.",
      [B("Telpiskas figūras", [
          ("Kā sauc šo ķermeni?",
           "Atrod un nosauc taisnstūru skaldni, kubu, piramīdu, cilindru un "
           "konusu."),
          ("Cik skaldņu, šķautņu un virsotņu?",
           "Raksturo telpisku figūru, lietojot jēdzienus skaldne, šķautne, "
           "virsotne."),
          ("Cik gara ir visu šķautņu summa?",
           "Mēra šķautnes un pieraksta izteiksmi visu šķautņu garumu summai."),
          ("Kā uzbūvēt modeli no kociņiem?",
           "Veido taisnstūru skaldni un piramīdu no kociņiem, izvēloties "
           "vajadzīgos garumus."),
      ]),
       B("Izklājums", [
           ("Kas rodas, pārgriežot kastīti?",
            "No papīra modeļa iegūst izklājumu, pārgriežot to pa šķautnēm."),
           ("Vai no šī izklājuma sanāks kubs?",
            "Atlasa izklājumus, no kuriem var salocīt kubu vai piramīdu, un "
            "pārbauda praktiski."),
           ("Kāds taisnstūris vajadzīgs cilindram?",
            "Piemeklē taisnstūri cilindra sānu virsmai un izveido modeli."),
           ("Kāds konuss sanāks?",
            "No vienāda lieluma riņķiem veido dažādus konusus un salīdzina "
            "tos."),
       ]),
       B("Skati no dažādām pusēm", [
           ("Kā ķermenis izskatās no augšas?",
            "Zīmē vai fotografē telpiskas figūras skatus no dažādām pusēm."),
           ("Kā uzbūvēt figūru pēc skatiem?",
            "Veido figūru no kubiem, ja doti skati no augšas, priekšas un "
            "sāniem."),
           ("Kuras skaldnes būs blakus?",
            "Prognozē, kuras krāsainā izklājuma skaldnes saskarsies, un "
            "pārbauda pieņēmumu."),
       ])],
      "Telpiskas figūras un izklājumi",
      "Raksturo un salīdzina telpiskas figūras; no izklājuma veido modeli; "
      "zīmē un atpazīst figūras skatus no dažādām pusēm.",
      "prizmas izklājums; vairāki izklājumi vienai figūrai."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 3. klasē", [
        ("Cik droši zinu reizināšanas tabulu?",
         "Formatīvi pārbauda reizināšanas tabulu un dalīšanu; atzīmē, kas vēl "
         "jātrenē."),
        ("Cik veikli rēķinu 1000 apjomā?",
         "Pārbauda saskaitīšanu un atņemšanu 1000 apjomā un izteiksmju "
         "aprēķināšanu."),
        ("Ko es zinu par daļām?",
         "Atkārto daļas jēgu: parāda daļu modelī, salīdzina daļas un nosaka "
         "daļu no skaita."),
        ("Ko gribu iemācīties 4. klasē?",
         "Apkopo gadā apgūto un iepazīstas ar 4. klases tematiem."),
    ]),
]
