# -*- coding: utf-8 -*-
"""4. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 4. klases sadaļa.
"""

from math_plani import B, T

IEVADS = (
    "Ceturtais matemātikas gads. Skaitļu apjoms pieaug līdz desmit "
    "tūkstošiem, un visas četras darbības sasniedz daudzciparu skaitļus. "
    "Ģeometrijā parādās transportieris un leņķa lielums grādos, laukums ar "
    "mērvienībām un formulu. Daļskaitļus salīdzina, saskaita un atņem, un "
    "gada beigās kustība un iepirkšanās izrādās viens un tas pats "
    "matemātiskais apraksts.")

TEMATI = [
    T("4.1.", "Kā saskaita un atņem daudzciparu skaitļus?",
      "Salīdzina, saskaita un atņem daudzciparu skaitļus, lai iegūtu, "
      "attēlotu un analizētu datus un risinātu sadzīves situācijas.",
      [B("Pirmais tūkstotis - atkārtojums", [
          ("Ko es protu no 3. klases?",
           "Nosaka trīsciparu skaitļa sastāvu un komentē savu sniegumu "
           "diagnosticējošajā darbā."),
          ("Kā salīdzināt, nerēķinot precīzi?",
           "Salīdzina summas un starpības spriežot, neaprēķinot precīzās "
           "vērtības."),
          ("Kā izvēlēties skaitļu taisnes soli?",
           "Veido skaitļu taisni ar piemērotu soli un atliek uz tās skaitļus "
           "līdz 1000."),
          ("Kā rēķinu galvā un kā rakstos?",
           "Saskaita un atņem līdz 1000 galvā un rakstos, stāstot savu "
           "risinājumu."),
          ("Kur noder mērvienības?",
           "Risina uzdevumus ar naudas, garuma, masas, tilpuma un laika "
           "mērvienībām."),
      ]),
       B("Četrciparu skaitļi", [
           ("Kā izlasīt un uzrakstīt četrciparu skaitli?",
            "Lasa un raksta skaitļus līdz 10 000 ar cipariem un vārdiem."),
           ("Kas ir skaitļu šķira?",
            "Nosauc šķiras - vieni, desmiti, simti, tūkstoši - un nosaka "
            "skaitļa decimālo sastāvu."),
           ("Kā skaitli uzrakstīt kā summu?",
            "Pieraksta četrciparu skaitli kā tūkstošu, simtu, desmitu un "
            "vienu summu."),
           ("Kurš skaitlis lielāks?",
            "Salīdzina četrciparu skaitļus, izmantojot decimālo sastāvu, un "
            "pieraksta ar «>» vai «<»."),
           ("Kur skaitlis stāv uz skaitļu taisnes?",
            "Izveido skaitļu taisni ar izvēlētu vienību un atliek uz tās "
            "četrciparu skaitļus."),
           ("Precīzi vai aptuveni?",
            "Argumentē, vai konkrētu lielumu sadzīvē raksturo ar precīzu vai "
            "aptuvenu vērtību."),
       ]),
       B("Saskaitīšana un atņemšana 10 000 apjomā", [
           ("Kā saskaitīt galvā?",
            "Saskaita un atņem četrciparu skaitļus galvā vienkāršos "
            "gadījumos, izmantojot decimālo sastāvu."),
           ("Kā saskaitīt rakstos?",
            "Saskaita un atņem četrciparu skaitļus rakstos, komentējot "
            "darbības izpildi."),
           ("Kad jāsadala tūkstotis?",
            "Atņem ar pāreju citā šķirā un skaidro, kā tūkstoti sadala "
            "simtos."),
           ("Cik apmēram sanāks?",
            "Nosaka summas un starpības aptuveno vērtību un lieto to "
            "pārbaudei."),
           ("Kurš darbības loceklis pazudis?",
            "Aprēķina darbības nezināmo locekli, lietojot jēdzienus summa un "
            "starpība."),
           ("Kāda ir darbību secība?",
            "Aprēķina izteiksmes vērtību ar līdz četrām darbībām un iekavām."),
       ]),
       B("Dati, diagrammas un situācijas", [
           ("Ko stāsta infogramma?",
            "Nolasa datus no infogrammām un dažādi organizētām stabiņu "
            "diagrammām."),
           ("Kā attēlot savus datus?",
            "Attēlo skaitliskus datus stabiņu diagrammā un pamato izvēlēto "
            "mērogu."),
           ("Kādus jautājumus var uzdot?",
            "Formulē secinājumus un jautājumus par tabulā vai diagrammā doto "
            "informāciju."),
           ("Kā izplānot ceļojumu?",
            "Ar 3-4 darbību izteiksmēm plāno un salīdzina ceļojuma vai "
            "pasākuma izmaksas."),
           ("Kāds uzdevums der šim zīmējumam?",
            "Veido uzdevuma tekstu shematiskam zīmējumam, lietojot «par tik "
            "vairāk», «kopā», «atlika»."),
       ])],
      "Daudzciparu skaitļi, saskaitīšana un atņemšana",
      "Lasa, raksta un salīdzina skaitļus līdz 10 000; saskaita un atņem "
      "10 000 apjomā; nosaka aptuveno vērtību; lasa un veido stabiņu "
      "diagrammu; risina līdz 3 darbību situāciju uzdevumus.",
      "skaitļi virs 10 000; vienādības ar nezināmo abās pusēs."),

    T("4.2.", "Kā daudzciparu skaitļus reizina un dala ar viencipara "
      "skaitli?",
      "Mācās reizināt un dalīt divciparu un trīsciparu skaitli ar viencipara "
      "skaitli, izmantojot decimālo sastāvu un darbību īpašības.",
      [B("Divciparu skaitļa reizināšana", [
          ("Kā modelēt 23 · 3?",
           "Modelē divciparu skaitļa reizinājumu ar monētām vai rūtiņām "
           "taisnstūrī."),
          ("Kā reizināt bez pārejas citā šķirā?",
           "Reizina divciparu skaitli ar viencipara skaitli galvā, pierakstot "
           "starprezultātus."),
          ("Kas mainās, ja rodas jauns desmits?",
           "Reizina ar pāreju citā šķirā un stāsta, kā rīkojās."),
          ("Kāpēc drīkst reizināt pa daļām?",
           "Lieto un skaidro īpašību (a + b) · c = a · c + b · c."),
          ("Kurš pieraksts man ērtāks?",
           "Salīdzina reizināšanas pierakstus - rindā, ar starprezultātiem un "
           "stabiņā."),
          ("Kā izdevīgāk reizināt trīs skaitļus?",
           "Nosaka 3-4 skaitļu reizinājumu, izvēloties izdevīgu secību un "
           "pārveidojumu."),
      ]),
       B("Dalīšana ar viencipara skaitli un atlikums", [
           ("Kā modelēt dalīšanu?",
            "Modelē divciparu skaitļa dalījumu ar viencipara skaitli un "
            "attēlo to shematiski."),
           ("Kā dalīt bez pārejas citā šķirā?",
            "Dala pilnus desmitus un divciparu skaitli bez pārejas; pārbauda "
            "ar reizināšanu."),
           ("Kā dalīt, ja jāsadala desmits?",
            "Dala ar pāreju citā šķirā (85 : 5) un skaidro savu paņēmienu."),
           ("Ko darīt, ja nesanāk gludi?",
            "Dala ar atlikumu; nosauc un pieraksta dalījumu un atlikumu."),
           ("Kā pārbaudīt dalīšanu ar atlikumu?",
            "Pārbauda rezultātu ar vienādību: dalāmais ir dalītāja un "
            "dalījuma reizinājums plus atlikums."),
           ("Ko atlikums nozīmē dzīvē?",
            "Risina praktisku uzdevumu ar atlikumu un skaidro, ko izsaka "
            "dalījums un ko - atlikums."),
           ("Kuri skaitļi dalās ar 2, 3, 5 un 9?",
            "Aplūko piemērus un formulē dalāmības pazīmes; pamato savus "
            "spriedumus."),
       ]),
       B("Trīsciparu skaitļa reizināšana", [
           ("Kā reizināt katru šķiru atsevišķi?",
            "Reizina trīsciparu skaitli ar viencipara skaitli, lietojot "
            "decimālo sastāvu."),
           ("Kā reizināt veikli?",
            "Lieto ērtus pārveidojumus (199 · 5 = (200 − 1) · 5; "
            "120 · 5 = 12 · 10 · 5)."),
           ("Kā reizina rakstos?",
            "Reizina rakstos trīsciparu skaitli ar viencipara skaitli, "
            "komentējot vienus, desmitus un simtus."),
           ("Cik apmēram būs reizinājums?",
            "Nosaka reizinājuma aptuveno vērtību pirms aprēķina un pārbauda "
            "pieņēmumu."),
           ("Vai izdosies arī ar četrciparu skaitli?",
            "Patstāvīgi reizina četrciparu skaitli ar viencipara skaitli un "
            "pārbauda rezultātu."),
       ]),
       B("Trīsciparu skaitļa dalīšana un lietojums", [
           ("Kā dalīt trīsciparu skaitli?",
            "Dala trīsciparu skaitli ar viencipara skaitli, izsakot dalāmo kā "
            "summu vai dalot pakāpeniski."),
           ("Kā dala rakstos?",
            "Dala rakstos un skaidro pieraksta veidošanu."),
           ("Cik apmēram būs dalījums?",
            "Nosaka dalījuma aptuveno vērtību un pārbauda to, arī ar "
            "digitāliem rīkiem."),
           ("Cik maksā deviņi bloki?",
            "Risina uzdevumu par proporcionāliem lielumiem, veidojot "
            "shematisku zīmējumu."),
           ("Tik reižu vairāk vai par tik vairāk?",
            "Attēlo shematiski situācijas ar «tik reižu vairāk» un risina "
            "tās."),
           ("Kura izteiksme lielāka?",
            "Salīdzina divu darbību izteiksmes spriežot, neaprēķinot precīzās "
            "vērtības."),
       ])],
      "Reizināšana un dalīšana ar viencipara skaitli",
      "Reizina un dala divciparu un trīsciparu skaitli ar viencipara skaitli; "
      "dala ar atlikumu; nosaka aptuveno vērtību; risina līdz 3 darbību "
      "uzdevumus ar «tik reižu vairāk».",
      "dalāmības pazīmes ar 4 un 6; reizināšana ar piecciparu skaitļiem."),

    T("4.3.", "Kā mēra leņķi?",
      "Iepazīst jēdzienus paralēls un perpendikulārs, leņķa lielumu grādos un "
      "mācās zīmēt leņķus un daudzstūrus ar transportieri.",
      [B("Paralēlas un perpendikulāras līnijas", [
          ("Kā izvietotas rūtiņu lapas līnijas?",
           "Raksturo paralēlas un perpendikulāras līnijas; min piemērus "
           "apkārtnē."),
          ("Kā uzzīmēt paralēlas līnijas baltā lapā?",
           "Ar diviem lineāliem zīmē paralēlas taisnas līnijas un pārbauda "
           "rezultātu."),
          ("Kā pārbaudīt, vai malas ir perpendikulāras?",
           "Ar uzstūri pārbauda, vai daudzstūra malas ir perpendikulāras."),
          ("Kādas malas ir taisnstūrim?",
           "Skaidro, ka taisnstūra pretējās malas ir paralēlas, bet blakus "
           "malas - perpendikulāras."),
          ("Kur paralēlas līnijas ir telpiskos ķermeņos?",
           "Saskata paralēlas šķautnes taisnstūra paralēlskaldnī un raksturo "
           "to."),
      ]),
       B("Leņķis un tā mērīšana", [
           ("Kas ir stars un kas - leņķis?",
            "Apraksta staru un leņķi savos vārdos; salīdzina savu aprakstu ar "
            "citu aprakstiem."),
           ("Kā apzīmē leņķi?",
            "Nosauc un pieraksta leņķus ar pieņemtajiem apzīmējumiem; nosaka "
            "leņķa virsotni un malas."),
           ("Kā mainās leņķa lielums?",
            "Ar leņķa modeli parāda leņķa palielināšanu un samazināšanu; "
            "saskata nekustīgo un kustīgo malu."),
           ("Cik grādu ir taisnam leņķim?",
            "Zina, ka taisns leņķis ir 90°, un spriež par šaura un plata "
            "leņķa lielumu."),
           ("Kā mēra ar transportieri?",
            "Ar transportieri izmēra leņķa lielumu un pieraksta rezultātu."),
           ("Kas kopīgs garuma un leņķa mērīšanai?",
            "Salīdzina nogriežņa garuma un leņķa lieluma mērīšanu; raksturo "
            "kopīgo un atšķirīgo."),
           ("Vai malu pagarināšana maina leņķi?",
            "Secina, ka leņķa lielums nemainās, pagarinot tā malas, un pamato "
            "to."),
           ("Cik leņķu ir zīmējumā?",
            "Saskata visus leņķus figūrā ar trim vai četriem stariem un "
            "pārliecinās, ka apskatīti visi."),
       ]),
       B("Figūru zīmēšana pēc leņķiem", [
           ("Kā uzzīmēt 40° leņķi?",
            "Zīmē dota lieluma leņķi ar transportieri un pieraksta tā "
            "lielumu."),
           ("Kā papildināt zīmējumu?",
            "Papildina zīmējumu ar dota lieluma leņķi un spriež, cik veidos "
            "to var izdarīt."),
           ("Kā pagriezt staru par leņķi?",
            "Pagriež staru ap punktu par doto leņķi un veido zīmējumu."),
           ("Kā pagriezt taisnstūri par 90°?",
            "Pagriež taisnstūri rūtiņu lapā ap virsotni un attēlo abas "
            "figūras."),
           ("Kā uzzīmēt trijstūri pēc nosacījumiem?",
            "Zīmē trijstūri, ja dots leņķa lielums un divu malu garumi."),
           ("Kāds četrstūris sanāks?",
            "Zīmē daudzstūri, ievērojot nosacījumus par malu novietojumu un "
            "leņķu veidiem."),
           ("Vai apgalvojums par leņķiem ir patiess?",
            "Nosaka apgalvojuma par leņķiem patiesumu un pamato savu "
            "spriedumu."),
       ])],
      "Leņķi, paralēlas un perpendikulāras malas",
      "Zīmē un mēra leņķus ar transportieri; nosaka leņķa veidu; zīmē "
      "paralēlas un perpendikulāras līnijas; zīmē daudzstūrus pēc "
      "nosacījumiem par malām un leņķiem.",
      "leņķu summa trijstūrī; pagriezieni par dažādiem leņķiem."),

    T("4.4.", "Kā daudzciparu skaitļus reizina un dala ar divciparu skaitli?",
      "Reizina un dala daudzciparu skaitļus ar divciparu skaitli, saistot "
      "jauno ar jau zināmo.",
      [B("Reizināšana ar 10, 100 un pilniem desmitiem", [
          ("Kas notiek, reizinot ar 10?",
           "Modelē un skaidro reizinājumu ar 10, 100 un 1000, izmantojot "
           "šķiru modeļus."),
          ("Kā reizināt ar pilniem desmitiem?",
           "Reizina divciparu skaitli ar pilniem desmitiem, izsakot tos kā "
           "reizinājumu ar 10."),
          ("Kā reizināt skaitļus ar nullēm galā?",
           "Secina, kā sareizināt skaitļus, kas beidzas ar vienu vai vairākām "
           "nullēm."),
          ("Cik ir desmittūkstotis?",
           "Lieto jēdzienu desmittūkstotis un lasa lielus skaitļus."),
          ("Cik apmēram sanāks?",
           "Nosaka reizinājuma aptuveno vērtību, reizinot tuvākos pilnos "
           "desmitus."),
      ]),
       B("Divu divciparu skaitļu reizināšana", [
           ("Kā sadalīt reizinājumu pa daļām?",
            "Reizina divus divciparu skaitļus pakāpeniski, izsakot skaitli kā "
            "summu."),
           ("Kāpēc sanāk četri saskaitāmie?",
            "Modelē reizinājumu ģeometriski un secina, ka tas veidojas no "
            "četriem reizinājumiem."),
           ("Kā reizina rakstos?",
            "Reizina divus divciparu skaitļus rakstos un skaidro katru soli."),
           ("Kurš paņēmiens man ērtāks?",
            "Izvēlas piemērotāko paņēmienu un pierakstu; pamato izvēli."),
           ("Kā reizināt trīsciparu skaitli?",
            "Reizina trīsciparu skaitli ar divciparu skaitli rakstos un "
            "komentē, kas mainās."),
           ("Kuri cipari trūkst?",
            "Nosaka trūkstošos ciparus reizinājumā rakstos, spriežot no "
            "beigām."),
       ]),
       B("Dalīšana ar divciparu skaitli", [
           ("Kā dalīt galvā?",
            "Dala galvā divciparu un trīsciparu skaitļus ar divciparu skaitli "
            "un pārbauda ar reizināšanu."),
           ("Kā dalāmo izteikt kā summu?",
            "Dala trīsciparu skaitli, izsakot dalāmo kā summu "
            "(575 : 25 = (500 + 75) : 25)."),
           ("Kā dalīt pakāpeniski?",
            "Dala trīsciparu skaitli ar divciparu skaitli pakāpeniski un "
            "veido sev piemērotu pierakstu."),
           ("Kā dala rakstos?",
            "Dala rakstos un komentē katru soli."),
           ("Cik apmēram būs dalījums?",
            "Nosaka dalījuma aptuveno vērtību un pārbauda to ar kalkulatoru."),
           ("Kad noder kalkulators?",
            "Lieto kalkulatoru daudzciparu skaitļu reizināšanai un dalīšanai; "
            "pārbauda dalījumu ar reizināšanu."),
       ]),
       B("Prasmju lietošana problēmās", [
           ("Cik reižu viens lielums ietilpst otrā?",
            "Nosaka, cik reižu viena lieluma vērtība ietilpst otrā, un "
            "skaidro atlikuma nozīmi."),
           ("Kā zīmējums palīdz saprast uzdevumu?",
            "Veido shematisku zīmējumu situācijām ar «tik reižu vairāk», "
            "«kopā», «atlika»."),
           ("Kāda ir darbību secība?",
            "Aprēķina izteiksmes vērtību ar divām vai trim darbībām un "
            "iekavām."),
           ("Cik maksās klases brauciens?",
            "Plāno pasākuma vai ceļojuma budžetu, veidojot izteiksmes un "
            "veicot aprēķinus."),
           ("Vai uzdevumam ir viena atbilde?",
            "Risina atvērtu problēmu ar vairākiem iespējamiem risinājumiem un "
            "pamato savu izvēli."),
       ])],
      "Reizināšana un dalīšana ar divciparu skaitli",
      "Reizina un dala daudzciparu skaitli ar divciparu skaitli; nosaka "
      "aptuveno vērtību; lieto kalkulatoru pārbaudei; risina praktiskas "
      "problēmas ar līdz 3 darbībām.",
      "reizināšana ar trīsciparu skaitli; budžeta plānošana ar tabulu."),

    T("4.5.", "Kā salīdzina, saskaita un atņem daļskaitļus?",
      "Padziļina izpratni par daļām kā skaitļiem: to vieta uz skaitļu "
      "taisnes, salīdzināšana, saskaitīšana un atņemšana ar vienādiem "
      "saucējiem.",
      [B("Daļas uz skaitļu taisnes", [
          ("Kā izlasīt un uzrakstīt daļu?",
           "Lasa un pieraksta daļas pēc dzirdētā; uzraksta daļu pēc "
           "nosacījumiem."),
          ("Kur uz skaitļu taisnes ir daļa?",
           "Atliek daļu uz dotas skaitļu taisnes un pamato tās vietu."),
          ("Kā rīkoties, ja taisne nav gatava?",
           "Papildina vai veido skaitļu taisni, lai atliktu doto daļu."),
          ("Kad daļa ir vienāda ar vienu?",
           "Skaidro, ka daļa, kurai skaitītājs un saucējs vienādi, ir viens, "
           "un min piemērus."),
          ("Kas ir īsta un kas - neīsta daļa?",
           "Nošķir īstu un neīstu daļu un parāda tās uz skaitļu taisnes."),
          ("Kā neīstu daļu izteikt ar veselo?",
           "Izsaka neīstu daļu kā vesela skaitļa un īstas daļas summu."),
      ]),
       B("Daļu salīdzināšana", [
           ("Kura daļa lielāka, ja saucēji vienādi?",
            "Salīdzina daļas ar vienādiem saucējiem un veido paskaidrojošu "
            "spriedumu."),
           ("Kāpēc lielāks saucējs dod mazāku daļu?",
            "Salīdzina pamatdaļas, izmantojot piemērus no dzīves un modeļus."),
           ("Kura daļa lielāka, ja skaitītāji vienādi?",
            "Salīdzina daļas ar vienādiem skaitītājiem un pamato spriedumu."),
           ("Vairāk vai mazāk nekā puse?",
            "Grupē daļas ar vienu saucēju, salīdzinot tās ar pusi."),
           ("Kā salīdzināt daļas ar dažādiem saucējiem?",
            "Vienkāršos gadījumos salīdzina daļas ar dažādiem saucējiem, "
            "veidojot zīmējumu vai divas skaitļu taisnes."),
           ("Kāda daļa ir starp šīm divām?",
            "Uzraksta un atliek uz skaitļu taisnes daļas, kas lielākas vai "
            "mazākas nekā dotā."),
       ]),
       B("Daļu saskaitīšana un atņemšana", [
           ("Ko nozīmē saskaitīt daļas?",
            "Modelē daļu saskaitīšanu ar sloksnītēm, zīmējumu vai uz skaitļu "
            "taisnes."),
           ("Kā pieraksta summu un starpību?",
            "Saskaita un atņem daļas ar vienādiem saucējiem, veidojot pareizu "
            "pierakstu."),
           ("Cik pietrūkst līdz veselam?",
            "Nosaka dotās daļas papildinājumu līdz vienam."),
           ("Cik dažādi var pierakstīt vienu daļu?",
            "Uzraksta doto daļu vai skaitli 1 kā summu vai starpību dažādos "
            "veidos."),
           ("Kur risinājumā kļūda?",
            "Analizē dotu daļu saskaitīšanas risinājumu, pamato tā aplamību "
            "un iesaka labojumu."),
           ("Kurš skaitlis trūkst?",
            "Nosaka nezināmo lielumu darbībā ar daļām un skaidro, kā ieguva "
            "rezultātu."),
           ("Kā aug daļu virkne?",
            "Turpina skaitļu virkni, ko veido daļas, un formulē "
            "likumsakarību."),
       ]),
       B("Daļa kā reizinājums", [
           ("Kā daļu izteikt ar pamatdaļām?",
            "Izsaka daļu kā pamatdaļu summu un pieraksta to īsāk."),
           ("Kā daļu uzrakstīt kā reizinājumu?",
            "Pieraksta daļu kā skaitītāja un pamatdaļas reizinājumu."),
           ("Kas sanāk, reizinot veselu skaitli ar daļu?",
            "Modelē uz skaitļu taisnes vesela skaitļa un daļas reizinājumu un "
            "secina rezultātu."),
           ("Vai rezultāts ir īsta vai neīsta daļa?",
            "Nosaka, vai reizinājums ir īsta vai neīsta daļa, un pamato "
            "atbildi."),
           ("Kāds skaitlis der vienādībā?",
            "Nosaka nezināmo vienādībā vai nevienādībā ar daļām, modelējot "
            "situāciju."),
       ])],
      "Daļskaitļi: salīdzināšana, saskaitīšana un atņemšana",
      "Atliek daļas uz skaitļu taisnes; salīdzina daļas; saskaita un atņem "
      "daļas ar vienādiem saucējiem; reizina veselu skaitli ar daļu; "
      "pieraksta daļu dažādos veidos.",
      "daļu saskaitīšana ar dažādiem saucējiem; jaukta skaitļa pieraksts."),

    T("4.6.", "Ko nozīmē daļa no veselā?",
      "Padziļina izpratni par veselo un daļu; mācās aprēķināt daļas un veselā "
      "skaitlisko vērtību praktiskos kontekstos.",
      [B("Kas ir veselais", [
          ("Kas šajā situācijā ir veselais?",
           "Skaidro, kas dotajā situācijā ir veselais, un raksturo to "
           "skaitliski."),
          ("Ko var uzzināt no teikuma par daļu?",
           "Analizē sadzīves teikumu ar daļu un formulē, ko no tā var "
           "uzzināt."),
          ("Kā apkopot daļas un to vērtības?",
           "Veido tabulu, kurā attēlota daļa un tās skaitliskā vērtība."),
          ("Kāda daļa no stundas?",
           "Nosaka pamatdaļu no stundas, izmantojot pulksteņa modeli."),
          ("Kāda daļa no 10 centimetriem?",
           "Ar lineālu nosaka dažādu daļu vērtību no 10 cm un apkopo "
           "rezultātus."),
          ("Kāda daļa no figūras laukuma?",
           "Nosaka daļu no rūtiņās dotas figūras laukuma, arī tad, ja figūru "
           "nevar sadalīt vienādās daļās acīmredzami."),
      ]),
       B("Daļa no skaita un naudas", [
           ("Kā aprēķināt daļu no naudas?",
            "Nosaka pamatdaļu no naudas daudzuma, vispirms ar monētu "
            "modeļiem."),
           ("Ko darīt, ja modeli izveidot nevar?",
            "Aprēķina daļu no lielas summas, spriežot un pierakstot "
            "risinājumu."),
           ("Kā aprēķināt daļu no skaita?",
            "Nosaka pamatdaļu no elementu skaita un pēc tam - atlikušās daļas "
            "vērtību."),
           ("Kā zīmējums palīdz?",
            "Veido shematisku zīmējumu daļas noteikšanai un stāsta, kā tas "
            "palīdz."),
           ("Kā aprēķina citi?",
            "Lasa un komentē dažādus risinājumus daļas vērtības "
            "aprēķināšanai."),
           ("Kāda daļa no kilometra?",
            "Pārveido pamatdaļu no lieluma mazākās mērvienībās (puse "
            "kilograma, ceturtdaļa kilometra)."),
           ("Cik daudz laika veltu mācībām?",
            "Veic praktisku pētījumu par diennakts sadalījumu un apkopo datus "
            "ar daļām."),
       ]),
       B("Veselais, ja zināma daļa", [
           ("Cik bija sākumā?",
            "Nosaka veselo, ja zināma pamatdaļas vērtība."),
           ("Kā pieraksta spriedumu?",
            "Veido pierakstu, kas atbilst domāšanas gaitai, nosakot veselo un "
            "daļu."),
           ("Kāds ir skaitlis, ja zināma tā ceturtdaļa?",
            "Nosaka skaitli, ja zināma pamatdaļas vērtība, ar diviem "
            "paņēmieniem."),
           ("Cik nobrauca trešajā dienā?",
            "Risina uzdevumu, kurā apvienota daļas vērtības aprēķināšana un "
            "daļu saskaitīšana."),
           ("Kāds uzdevums sanāk tev?",
            "Sastāda savu uzdevumu par daļas vērtību, apmainās ar "
            "klasesbiedru un risina."),
           ("Kā izskatās figūru virkne ar daļām?",
            "Saskata likumsakarību figūru virknē ar daļām un pieraksta to kā "
            "skaitļu virkni."),
       ])],
      "Daļas un veselā skaitliskā vērtība",
      "Nosaka, kas situācijā ir veselais; aprēķina pamatdaļas un daļas "
      "vērtību; nosaka veselo, ja zināma daļa; risina situāciju uzdevumus ar "
      "daļām.",
      "daļa no daļas; uzdevumi ar divām dažādām daļām."),

    T("4.7.", "Kā nosaka dažādu figūru laukumu?",
      "Padziļina izpratni par laukumu: mērvienības, taisnstūra laukuma "
      "formula un kombinētu figūru laukums.",
      [B("Laukuma īpašības un vienlielas figūras", [
          ("Kuras figūras ir vienlielas?",
           "Atrod rūtiņu lapā figūras ar vienādu laukumu un pamato atbildi."),
          ("Kā izveidot citu figūru ar to pašu laukumu?",
           "Sadala figūru daļās un savieto citādi, iegūstot vienlielu "
           "figūru."),
          ("Cik dažādi var sadalīt figūru?",
           "Dala figūru vienlielās daļās vairākos veidos un salīdzina "
           "risinājumus."),
          ("Kā uzzīmēt trijstūri ar tādu pašu laukumu?",
           "Zīmē trijstūri, kura laukums vienāds ar dotā taisnstūra laukumu, "
           "un skaidro rīcību."),
          ("Vai apgalvojums ir patiess?",
           "Ar pretpiemēru pamato, ka apgalvojums par laukumu un perimetru "
           "nav patiess."),
      ]),
       B("Laukuma mērvienības", [
           ("Cik liels ir kvadrātcentimetrs?",
            "Praktiski veido 1 cm² un 1 dm² modeļus un skaidro sakarību starp "
            "tiem."),
           ("Kā lielāku vienību izteikt mazākā?",
            "Izsaka lielākas laukuma mērvienības mazākās un otrādi."),
           ("Cik liels ir kvadrātmetrs?",
            "Novērtē telpas virsmu laukumu kvadrātmetros un pārbauda "
            "novērtējumu."),
           ("Kur lieto hektāru?",
            "Novērtē apkārtnes objektu laukumu hektāros un min piemērus."),
           ("Cik liels ir šis galds?",
            "Aptuveni novērtē taisnstūrveida virsmas laukumu un pārbauda "
            "aprēķinu."),
       ]),
       B("Laukuma formula un kombinētas figūras", [
           ("Kā pieraksta laukuma formulu?",
            "Formulē un lieto taisnstūra laukuma formulu S = a · b."),
           ("Kā atrast nezināmo malu?",
            "Aprēķina taisnstūra malas garumu, ja zināms laukums un otra "
            "mala."),
           ("Kā sadalīt figūru taisnstūros?",
            "Aprēķina kombinētas figūras laukumu kā divu taisnstūru laukumu "
            "summu."),
           ("Kad der starpība?",
            "Aprēķina figūras laukumu kā divu taisnstūru laukumu starpību."),
           ("Kas notiek, ja malas palielina divas reizes?",
            "Pēta un secina, kā mainās laukums, mainot malu garumus vienādu "
            "skaitu reižu."),
           ("Cik liels ir skolas pagalms?",
            "Plāno mērījumus un aprēķina reāla vides objekta laukumu."),
       ])],
      "Laukums un tā aprēķināšana",
      "Lieto laukuma mērvienības; aprēķina taisnstūra laukumu un nezināmo "
      "malu; aprēķina kombinētas figūras laukumu; zīmē figūras ar dotu "
      "laukumu.",
      "trijstūra laukums rūtiņās; laukuma izmaiņas, mainot vienu malu."),

    T("4.8.", "Kas kopīgs iepirkšanās un kustības matemātiskajā aprakstā?",
      "Veido izpratni par savstarpēji atkarīgiem lielumiem: skaits, cena, "
      "samaksa un ceļš, laiks, ātrums.",
      [B("Skaits, cena, samaksa", [
          ("Ko var uzzināt no iepirkuma apraksta?",
           "Raksturo situāciju saviem vārdiem un formulē, ko no tās var "
           "uzzināt."),
          ("Kā aprēķināt samaksu?",
           "Lieto reizināšanu un dalīšanu, lai noteiktu samaksu, cenu vai "
           "skaitu."),
          ("Cik maksās deviņi, ja zināms par četriem?",
           "Aprēķina samaksu citam preču skaitam, veidojot shematisku "
           "zīmējumu."),
          ("Cik varēs nopirkt par šo naudu?",
           "Aprēķina iegādājamo preču skaitu, ja zināma cita summa un "
           "skaits."),
          ("Kā mainās samaksa, mainoties skaitam?",
           "Formulē sakarību: ja preču ir divas reizes vairāk, samaksa ir "
           "divas reizes lielāka."),
      ]),
       B("Ceļš, laiks, ātrums", [
           ("Ko nozīmē 60 kilometri stundā?",
            "Skaidro ātruma jēgu un lasa ātruma mērvienības km/h un m/s."),
           ("Cik ātri skrienam mēs?",
            "Grupā mēra distanci un laiku, aprēķina ātrumu un salīdzina "
            "rezultātus."),
           ("Kā aprēķināt ceļu vai laiku?",
            "Aprēķina nezināmo lielumu, ja zināmi divi no trim: ceļš, laiks, "
            "ātrums."),
           ("Kurš pārvietojas ātrāk?",
            "Salīdzina ātrumus, arī tad, ja tie doti dažādās mērvienībās."),
           ("Kā zīmējums palīdz saprast kustību?",
            "Veido shematisku zīmējumu situācijai par kustību un atrisina "
            "uzdevumu."),
       ]),
       B("Kopīgais sakarībās", [
           ("Kā sakarību pierakstīt ar burtiem?",
            "Veido un lieto formulas, piemēram, s = t · v, un skaidro burtu "
            "nozīmi."),
           ("Kas kopīgs iepirkšanās un kustības aprakstam?",
            "Salīdzina divas situācijas un formulē kopīgo sakarībās starp "
            "lielumiem."),
           ("Kā veidojas saliktā mērvienība?",
            "Skaidro, kā veidojas saliktas mērvienības, arī praktiskas, "
            "piemēram, degvielas patēriņš."),
       ])],
      "Savstarpēji atkarīgi lielumi",
      "Aprēķina nezināmo lielumu situācijās par iepirkšanos un kustību; "
      "salīdzina ātrumus; lieto vienkāršas formulas un skaidro salikto "
      "mērvienību nozīmi.",
      "vidējais ātrums vairākos posmos; grafiku lasīšana par kustību."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 4. klasē", [
        ("Cik veikli rēķinu ar daudzciparu skaitļiem?",
         "Formatīvi pārbauda četras darbības ar daudzciparu skaitļiem un "
         "atzīmē trenējamo."),
        ("Ko es zinu par daļām?",
         "Atkārto daļu salīdzināšanu, saskaitīšanu un daļas vērtības "
         "aprēķināšanu."),
        ("Kā risinu praktisku uzdevumu?",
         "Risina praktisku uzdevumu par laukumu, kustību vai iepirkšanos un "
         "skaidro risinājumu."),
        ("Ko gribu iemācīties 5. klasē?",
         "Apkopo gadā apgūto un iepazīstas ar 5. klases tematiem."),
    ]),
]
