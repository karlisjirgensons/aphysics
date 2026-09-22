# -*- coding: utf-8 -*-
"""2. klases matemātikas stundu plāns.

Temati un secība - programmas parauga (Math/mat_p.pdf) 2. klases sadaļa.
"""

from math_plani import B, T

IEVADS = (
    "Otrais matemātikas gads. Skaitļu apjoms ir 100, un tajā mācās brīvi "
    "saskaitīt un atņemt; parādās izteiksme ar divām darbībām, iekavas, "
    "perimetrs un laukums, kā arī pirmie reizinājumi - ar 2, 3, 4 un 5. "
    "Mērīšana, laika rēķini un nauda nāk no reālām situācijām: veikala, "
    "sporta laukuma un autobusa saraksta.")

TEMATI = [
    T("2.1.", "Kā grupē objektus?",
      "Pilnveido prasmi novērot īpašības, grupēt objektus pēc kopīgas pazīmes "
      "un uzskatāmi parādīt grupēšanas rezultātu.",
      [B("Ko nozīmē grupēt", [
          ("Kas šim priekšmetam ir īpašs?",
           "Nosauc objekta īpašības un nošķir būtiskās no nebūtiskajām."),
          ("Kas visiem ir kopīgs?",
           "Objektu kopai nosauc kopīgu pazīmi un pārbauda konkrēta objekta "
           "piederību grupai."),
          ("Kurš neiederas?",
           "Atrod kopā neiederīgo objektu un paskaidro savu izvēli."),
          ("Kā grupēšanu parādīt ar zīmējumu?",
           "Attēlo grupēšanu Venna diagrammā vai tabulā un nosauc katras "
           "grupas pazīmi."),
      ]),
       B("Skaitļu un figūru grupēšana", [
           ("Kuri skaitļi der šai grupai?",
            "Atlasa skaitļus pēc pazīmes: beidzas ar 5, ir viencipara, ir "
            "mazāki nekā 20."),
           ("Kā skaitļus sadalīt divās grupās?",
            "Ievieto skaitļus Venna diagrammā un izdomā sadalījumu divās "
            "grupās, kas nepārklājas."),
           ("Pēc kā var sagrupēt figūras?",
            "Grupē plaknes un telpiskas figūras pēc dotas un pašizvēlētas "
            "pazīmes."),
           ("Vai vari atšifrēt cita grupējumu?",
            "Nosaka klasesbiedra izvēlēto grupēšanas pazīmi un raksturo katru "
            "grupu."),
           ("Ko par klasi stāsta mūsu dati?",
            "Veic nelielu aptauju, sagrupē datus un attēlo tos uzskatāmi."),
       ])],
      "Objektu, skaitļu un figūru grupēšana",
      "Nosauc kopīgās un atšķirīgās īpašības; nosaka grupas pazīmi; attēlo "
      "grupēšanu Venna diagrammā vai tabulā un lasa tajā doto informāciju.",
      "grupēšana pēc divām pazīmēm vienlaikus."),

    T("2.2.", "Kā nosaka dažādus garumus?",
      "Pilnveido mērīšanu daudzveidīgās situācijās: mērinstruments, "
      "mērvienība, precizitāte un rezultāta pieraksts.",
      [B("Mērinstrumenti un mērvienības", [
          ("Ar ko mērīsi stadionu un ar ko - grāmatu?",
           "Izvēlas garumam piemērotu mērinstrumentu un pamato izvēli."),
          ("Kas ir milimetrs?",
           "Mēra ar lineālu centimetros un milimetros; pieraksta rezultātu ar "
           "mērvienību."),
          ("Kāpēc iznāk dažādi skaitļi?",
           "Skaidro, ka, jo mazāka mērvienība, jo vairāk reižu tā ietilpst "
           "lielumā; salīdzina mērījumus dažādās vienībās."),
          ("Kā izgatavot savu mērlenti?",
           "Izgatavo mērlenti ar m, dm un cm iedaļām un pārbauda to."),
          ("Kā mērīja senāk?",
           "Atrod informāciju par senajām mērvienībām un salīdzina tās ar "
           "metru."),
      ]),
       B("Dažādu objektu mērīšana", [
           ("Cik tas ir centimetros un cik milimetros?",
            "Mēra vienu un to pašu garumu divās mērvienībās un pieraksta abus "
            "rezultātus."),
           ("Kā izmērīt to, kas nav taisns?",
            "Netieši mēra līklīnijas garumu ar auklu un pēc tam ar lineālu."),
           ("Cik apmēram?",
            "Nosaka garumu pēc acumēra, pēc tam pārbauda, mērot līdz "
            "tuvākajai veselajai vienībai."),
           ("Kā pierakstīt visus mērījumus?",
            "Izveido tabulu mērījumiem un ieraksta tajā grupas datus."),
           ("Cik tālu aizlēci?",
            "Mēra un pieraksta tāllēkšanas rezultātus; salīdzina, par cik "
            "viens rezultāts lielāks nekā otrs."),
       ]),
       B("Dota garuma objekti un aprēķini", [
           ("Kā uzzīmēt 6 cm 5 mm?",
            "Zīmē dota garuma nogriezni, ja garums dots cm un mm."),
           ("Kur ir puse un kur ceturtdaļa?",
            "Ar sloksnīti atzīmē nogriežņa pusi un ceturtdaļu, salokot to."),
           ("Cik kopā un par cik garāks?",
            "Saskaita un atņem garumus vienās mērvienībās; nosaka, par cik "
            "viens objekts ir garāks."),
           ("Kā uzbūvēt modeli pēc reāliem izmēriem?",
            "Grupā izgatavo objekta modeli pēc dotiem izmēriem un pārbauda "
            "izmērus."),
       ])],
      "Garuma mērīšana un aprēķini",
      "Mēra garumu mm, cm, dm un m; zīmē dota garuma nogriezni; izsaka "
      "lielāku mērvienību mazākā; veic aprēķinus ar garumiem un apkopo "
      "mērījumus tabulā.",
      "attālumu mērīšana dabā ar soļiem; mērījumu precizitātes "
      "salīdzināšana."),

    T("2.3.", "Kā saskaita un atņem divciparu skaitļus?",
      "Pilnveido saskaitīšanu un atņemšanu 100 apjomā ar sev saprotamiem "
      "paņēmieniem un pārbauda rezultāta ticamību.",
      [B("Atkārtojam 20 apjomu", [
          ("Cik veikli rēķini 20 apjomā?",
           "Saskaita un atņem 20 apjomā, skaidrojot izmantoto paņēmienu."),
          ("Kā skaitli pierakstīt kā summu?",
           "Pieraksta skaitli līdz 20 kā divu un vairāku skaitļu summu, arī "
           "kā vienādu skaitļu summu."),
          ("Kā rēķināt uz skaitļu taisnes?",
           "Saskaita un atņem, izmantojot skaitļu taisni un lineālu."),
          ("Rindā vai stabiņā?",
           "Pieraksta darbību un rezultātu gan rindā, gan stabiņā."),
          ("Vai atbilde ir ticama?",
           "Pārbauda rezultātu ar pretējo darbību un novērtē tā ticamību."),
          ("Kā atcerēties summas?",
           "Stāsta savu atcerēšanās paņēmienu un trenē summas un starpības 20 "
           "apjomā."),
      ]),
       B("Divciparu skaitļu saskaitīšana", [
           ("Kā saskaitīt pa desmitiem?",
            "Saskaita, skaitot pa 10 un pa 5 (47 = 10 + 10 + 10 + 10 + 5 + 1 "
            "+ 1); izmanto to naudas rēķinos."),
           ("Desmiti ar desmitiem, vieni ar vieniem?",
            "Modelē divciparu skaitļu saskaitīšanu ar desmitu sloksnītēm un "
            "secina par darbības kārtību."),
           ("Kad rodas jauns desmits?",
            "Saskaita divciparu skaitļus ar pāreju jaunā desmitā un skaidro, "
            "kas notiek ar vieniem."),
           ("Kā pierakstīt stabiņā?",
            "Veido saskaitīšanas pierakstu stabiņā un skaidro katru soli."),
           ("Cik apmēram sanāks?",
            "Prognozē summas aptuveno lielumu un izmanto to atbildes "
            "pārbaudei."),
           ("Kā pārbaudīt savu rezultātu?",
            "Pārbauda summu, salīdzinot ar klasesbiedra rezultātu vai risinot "
            "citādi."),
           ("Kurš paņēmiens tev ērtākais?",
            "Izvēlas piemērotāko paņēmienu konkrētam piemēram un pamato "
            "izvēli."),
           ("Cik veikli jau proti?",
            "Patstāvīgi saskaita divciparu skaitļus un pārbauda atbildes."),
       ]),
       B("Atņemšana 100 apjomā", [
           ("Kā atņemt bez desmita sadalīšanas?",
            "Atņem divciparu skaitli, kad vienus var atņemt no vieniem."),
           ("Kad desmits jāsasmalcina?",
            "Modelē atņemšanu, kurā viens desmits jāsadala, un skaidro "
            "soļus."),
           ("Kā pierakstīt stabiņā?",
            "Veido atņemšanas pierakstu stabiņā un aprēķina starpību."),
           ("Kā pārbaudīt starpību?",
            "Pārbauda atņemšanu ar saskaitīšanu."),
           ("Cik pietrūkst līdz 100?",
            "Aprēķina, cik pietrūkst līdz pilnam simtam vai desmitam."),
           ("Kurš skaitlis paslēpts?",
            "Nosaka nezināmo darbības locekli vienādībā 100 apjomā."),
           ("Kur radusies kļūda?",
            "Atrod kļūdu dotā risinājumā un izlabo to."),
           ("Cik veikli atņem?",
            "Patstāvīgi atņem divciparu skaitļus un pārbauda rezultātu."),
       ]),
       B("Situācijas, nauda un dati", [
           ("Kā uzdevumu pārvērst zīmējumā?",
            "Veido shematisku zīmējumu situācijai ar saskaitīšanu vai "
            "atņemšanu 100 apjomā."),
           ("Cik soļu ir šajā uzdevumā?",
            "Risina divu soļu situāciju uzdevumu un pieraksta katru darbību."),
           ("Ko stāsta tabula un diagramma?",
            "Nolasa datus no tabulas un stabiņu diagrammas un izmanto tos "
            "aprēķinos."),
           ("Cik centu ir 0,05 € un 0,50 €?",
            "Lasa un salīdzina naudas summas, kas pierakstītas ar komatu."),
           ("Kā samaksāt ar monētām?",
            "Ar monētu modeļiem saliek doto summu vairākos veidos."),
           ("Kur lētāk?",
            "Veic nelielu pētījumu par cenu atšķirībām un pamato secinājumu."),
       ])],
      "Saskaitīšana un atņemšana 100 apjomā",
      "Saskaita un atņem divciparu skaitļus, arī ar pāreju jaunā desmitā; "
      "risina divu soļu situāciju uzdevumus; pārbauda rezultāta pareizību un "
      "ticamību.",
      "aprēķini ar trim divciparu skaitļiem; naudas summas ar centiem."),

    T("2.4.", "Kā laika rēķini palīdz plānot?",
      "Mācās noteikt notikuma ilgumu, lasīt laika norādes un izmantot tās "
      "savas dienas un nedēļas plānošanā.",
      [B("Pulkstenis un kalendārs", [
          ("Cik ir pulkstenis - līdz minūtei?",
           "Nolasa un pieraksta laiku no analogā un digitālā pulksteņa ar "
           "precizitāti līdz minūtei."),
          ("Kas ir 13 dienā un kas - 1 naktī?",
           "Nolasa laiku 24 stundu intervālā un saista to ar dienas gaitu."),
          ("Cik ilgi tu skrien 100 metrus?",
           "Ar hronometru mēra reāla notikuma ilgumu un pieraksta rezultātu "
           "minūtēs un sekundēs."),
          ("Cik var paveikt vienā minūtē?",
           "Veic mērījumus par paveikto vienā minūtē, ieraksta tos tabulā un "
           "salīdzina."),
          ("Kā atcerēties mēnešus?",
           "Nosauc mēnešus pēc kārtas, atrod informāciju kalendārā, nosaka "
           "dienu skaitu mēnesī."),
      ]),
       B("Laika rēķini", [
           ("Cik ilgi notikums turpinājās?",
            "Aprēķina notikuma ilgumu, ja zināms sākuma un beigu laiks."),
           ("Cikos jāsāk?",
            "Aprēķina sākuma vai beigu laiku, ja zināms ilgums."),
           ("Cik minūšu ir stundā un pusstundā?",
            "Sadala stundu minūtēs un veic vienkāršus aprēķinus ar laika "
            "mērvienībām."),
           ("Vai paspēsi uz autobusu?",
            "Lasa kustības sarakstu un aprēķina, cik laika atliek."),
           ("Cik ilgi es esmu ceļā?",
            "Savāc klases datus par ceļā pavadīto laiku un apkopo tos "
            "tabulā."),
       ]),
       B("Plāns un diagramma", [
           ("Kā uzzīmēt stabiņu diagrammu?",
            "Veido vienkāršu stabiņu diagrammu par saviem datiem un stāsta, "
            "ko svarīgi ievērot."),
           ("Ko diagramma pasaka par izmaiņām?",
            "Lasa diagrammu, kas rāda izmaiņas laikā, un pārkārto datus "
            "tabulā."),
           ("Kā izskatās mana nedēļa?",
            "Veido tabulu ar savu nedēļas plānu un stāsta par to, lietojot "
            "laika vienības."),
           ("Kā saplānot pasākumu?",
            "Sastāda vienkāršu pasākuma laika plānu un pārbauda, vai laiks "
            "pietiek."),
       ])],
      "Laiks, pulkstenis un plānošana",
      "Nolasa laiku līdz minūtei; aprēķina notikuma ilgumu, sākuma un beigu "
      "laiku; lasa laika norādes tabulās un sarakstos; veido stabiņu "
      "diagrammu.",
      "laika rēķini pāri pusnaktij; laika zonas."),

    T("2.5.", "Kā rodas izteiksme?",
      "Veido izpratni, ka situāciju var pierakstīt pa soļiem, ar vairāku "
      "darbību izteiksmi, ar vienādību vai nevienādību.",
      [B("Izteiksmju veidošana", [
          ("Ko aprēķināt vispirms?",
           "Situāciju ar vairākiem teikumiem raksturo ar atsevišķām darbībām "
           "un skaidro to secību."),
          ("Kā divas darbības salikt vienā pierakstā?",
           "Pieraksta divas secīgas darbības kā vienu skaitlisku izteiksmi."),
          ("Kāpēc vajadzīgas iekavas?",
           "Lieto iekavas, ja no skaitļa jāatņem divu skaitļu summa."),
          ("Vai vienu situāciju var pierakstīt dažādi?",
           "Aplūko vairākas izteiksmes, ar kurām pieraksta vienu un to pašu "
           "situāciju."),
          ("Kura izteiksme der šim risinājumam?",
           "Katrai izteiksmei atrod atbilstošu pierakstu pa soļiem un "
           "otrādi."),
          ("Kāds stāsts der izteiksmei?",
           "Veido tekstu, kas atbilst dotai divu darbību izteiksmei."),
          ("Kā uzrakstīt savu uzdevumu?",
           "Izdomā situāciju un pieraksta to ar divu darbību izteiksmi."),
      ]),
       B("Izteiksmes vērtība", [
           ("Kā pieraksta aprēķinu?",
            "Vēro un skaidro izteiksmes vērtības aprēķināšanas pierakstu."),
           ("Ko rēķina vispirms?",
            "Nosaka darbību secību un aprēķina divu darbību izteiksmes "
            "vērtību."),
           ("Kā pierakstīt starprezultātus?",
            "Pieraksta starprezultātus atsevišķi vai saistītajā pierakstā."),
           ("Cik dažādas izteiksmes var izveidot?",
            "No trim dotiem skaitļiem un zīmēm «+» un «−» veido visas "
            "iespējamās izteiksmes."),
           ("Vai iekavas maina rezultātu?",
            "Salīdzina 20 − (5 + 7) un 20 − 5 + 7 un skaidro atšķirību."),
           ("Kura izteiksme ir lielāka?",
            "Salīdzina divu izteiksmju vērtības, spriežot un neveicot "
            "precīzus aprēķinus."),
           ("Kā pārbaudīt otra darbu?",
            "Pārī apmainās ar izteiksmēm, aprēķina un skaidro savu darbību "
            "secību."),
       ]),
       B("Vienādības un nevienādības", [
           ("Vai pieraksts ir patiess?",
            "Nosaka, vai vienādība vai nevienādība ir patiesa, izmantojot "
            "dažādus paņēmienus."),
           ("Kā pierakstīt nogriežņu salīdzinājumu?",
            "Pieraksta ar vienādību un nevienādību situācijas, kurās doti "
            "nogriežņu garumi."),
           ("Kā izlasīt pierakstu ar vārdiem?",
            "Lasa vienādību un nevienādību ar vārdiem: tikpat garš, īsāks "
            "nekā."),
           ("Kur uzdevumā slēpjas nezināmais?",
            "Pieraksta situāciju kā vienādību, nezināmo aizstājot ar "
            "simbolu."),
           ("Kurš skaitlis der?",
            "Nosaka nezināmo darbības locekli ar paņēmienu «mēģinu un "
            "pārbaudu» un pamato izvēli."),
           ("Kādi skaitļi der nevienādībā?",
            "Nosauc vairākus skaitļus, ar kuriem nevienādība ir patiesa."),
           ("Kā salīdzināt summu ar skaitli?",
            "Salīdzina summu vai starpību ar skaitli, lietojot «<», «>», «=», "
            "neveicot precīzus aprēķinus."),
       ]),
       B("Algoritmi ar nosacījumu", [
           ("Kā izpildīt soļus pēc pieraksta?",
            "Lasa un izpilda dotu algoritmu ar vairākiem soļiem."),
           ("Kas notiek, ja nosacījums izpildās?",
            "Lasa un izpilda sazarotu algoritmu, kurā solis atkarīgs no "
            "nosacījuma."),
           ("Kā pierakstīt savu algoritmu?",
            "Pieraksta savu algoritmu uzdevuma izpildei un pārbauda to ar "
            "klasesbiedru."),
           ("Kur algoritms kļūdās?",
            "Atrod kļūdu dotā algoritmā un izlabo to."),
           ("Kā algoritms palīdz rēķināt?",
            "Izmanto algoritmu skaitļu salīdzināšanai vai izteiksmes vērtības "
            "aprēķināšanai."),
           ("Cik soļu vajag mērķim?",
            "Salīdzina divus algoritmus pēc soļu skaita un izvēlas īsāko."),
       ])],
      "Izteiksmes, vienādības un nevienādības",
      "Veido un aprēķina divu darbību izteiksmes, arī ar iekavām; nosaka, vai "
      "vienādība vai nevienādība ir patiesa; atrod nezināmo darbības locekli; "
      "izpilda sazarotu algoritmu.",
      "izteiksmes ar trim darbībām; nevienādības ar diviem risinājumiem."),

    T("2.6.", "Kā veido un raksturo figūras?",
      "Nostiprina izpratni par figūru daudzveidību un iepazīst divus figūru "
      "lielumus - perimetru un laukumu.",
      [B("Daudzstūru veidi", [
          ("Kā nosaukt figūru precīzi?",
           "Lieto jēdzienus mala, virsotne, šķautne; nosauc daudzstūrus un "
           "telpiskās figūras."),
          ("Kas ir taisnstūru skaldnis un kas - piramīda?",
           "Atpazīst un raksturo kubu, taisnstūru skaldni un piramīdu."),
          ("Kā uzzīmēt figūru datorā?",
           "Veido figūru zīmējumus ar zīmēšanas rīkiem un saglabā rezultātu."),
          ("Vai figūras ir vienādas?",
           "Pārbauda figūru vienādību, tās savietojot, un zīmē vienādu figūru "
           "rūtiņu lapā."),
          ("Kā uzzīmēt pēc pieraksta?",
           "Rūtiņu lapā veido lauztu līniju pēc dota algoritma ar "
           "atkārtojumu."),
          ("Kā pierakstīt savu rakstu?",
           "Pieraksta ciklisku algoritmu savas figūru virknes veidošanai."),
      ]),
       B("Figūru veidošana un pārveidošana", [
           ("Kādas figūras rodas, tās savietojot?",
            "Veido jaunas figūras no dotajām, savietojot tās, un nosauc "
            "rezultātu."),
           ("Kas ir kopīgā daļa?",
            "Pēta figūru pārklāšanos ar caurspīdīgiem modeļiem un apraksta "
            "kopīgo daļu."),
           ("Kā sadalīt taisnstūri vienādos kvadrātos?",
            "Sadala taisnstūri rūtiņu tīklā vienāda lieluma daļās vairākos "
            "veidos."),
           ("Cik dažādi var dalīt uz pusēm?",
            "Dala figūru divās vienādās daļās dažādos veidos un salīdzina "
            "risinājumus."),
           ("Vai visi gadījumi ir apskatīti?",
            "Aplūko visus iespējamos gadījumus, ja to skaits nepārsniedz 12, "
            "un pieraksta tos pārskatāmi."),
           ("Ko noderīgu var izgatavot?",
            "Grupā izgatavo noderīgu lietu no daudzstūriem un apraksta "
            "izmantotās figūras."),
       ]),
       B("Perimetrs un laukums", [
           ("Cik gara ir figūras apmale?",
            "Mēra daudzstūra malas un aprēķina perimetru; pieraksta to ar "
            "izteiksmi."),
           ("Kāpēc taisnstūrim nav jāmēra visas malas?",
            "Skaidro, kurus mērījumus pietiek veikt taisnstūra un kvadrāta "
            "perimetram."),
           ("Cik metru žoga vajag?",
            "Risina situāciju uzdevumu par perimetru, lietojot mērvienības."),
           ("Cik rūtiņu ietilpst figūrā?",
            "Nosaka taisnstūra laukumu rūtiņās, noklājot to ar vienādiem "
            "kvadrātiem."),
           ("Vai diviem taisnstūriem var būt viens perimetrs?",
            "Zīmē taisnstūrus ar dotu perimetru vai laukumu un salīdzina "
            "tos."),
           ("Cik liels ir lapas laukums?",
            "Ar caurspīdīgu rūtiņu tīklu nosaka aptuvenu neregulāras figūras "
            "laukumu."),
       ])],
      "Figūras, perimetrs un laukums",
      "Atpazīst un zīmē daudzstūrus; veido jaunas figūras no dotajām; mēra un "
      "aprēķina perimetru; nosaka laukumu rūtiņās.",
      "figūras ar vienādu laukumu, bet dažādu perimetru."),

    T("2.7.", "Ko nozīmē reizināt un dalīt ar 2?",
      "Veido izpratni par reizināšanas un dalīšanas jēgu, sākot ar "
      "dubultošanu un dalīšanu uz pusēm.",
      [B("Dubultošana un puse", [
          ("Kurus skaitļus var salikt no diviem vienādiem?",
           "Pieraksta skaitļus no 2 līdz 20 kā divu skaitļu summu un izceļ "
           "vienādu skaitļu summas."),
          ("Ko nozīmē «divreiz vairāk»?",
           "Modelē doto daudzumu un divreiz lielāku daudzumu ar priekšmetiem "
           "vai sloksnītēm."),
          ("Kur dabā ir pāri?",
           "Atrod objektus, ko veido pāri, un pieraksta kopējo skaitu."),
          ("Kā sadalīt uz pusēm?",
           "Dala doto daudzumu divās vienādās daļās un pa 2, un pastāsta "
           "atšķirību."),
          ("Vai vienmēr var samaksāt ar divām vienādām monētām?",
           "Pēta, kuras summas var samaksāt ar divām vienādām monētām, un "
           "apskata visus gadījumus."),
          ("Kā uzzīmēt divreiz garāku?",
           "Zīmē nogriezni un taisnstūri, kas divreiz garāks vai lielāks nekā "
           "dotais."),
      ]),
       B("Reizināšana un dalīšana ar 2", [
           ("Kā pieraksta reizināšanu?",
            "Lasa un pieraksta reizināšanu ar zīmi «·»; skaidro, ko tā "
            "nozīmē."),
           ("Kā pieraksta dalīšanu?",
            "Lasa un pieraksta dalīšanu ar zīmi «:»; skaidro abas dalīšanas "
            "nozīmes."),
           ("Kā uzbūvēt reizināšanas ar 2 tabulu?",
            "Izveido reizinājumu ar 2 tabulu un izmanto to aprēķinos."),
           ("Kā reizināšana palīdz dalīt?",
            "Skaidro sakarību starp reizināšanu un dalīšanu (2 · 5 = 10 un "
            "10 : 2 = 5)."),
           ("Kā iegaumēt reizinājumus?",
            "Veido kartītes un vingrinās pārī, lai iegaumētu reizinājumus un "
            "dalījumus ar 2."),
           ("Kur dzīvē reizina ar 2?",
            "Izdomā piemērus no dzīves, kur jāreizina vai jādala ar 2."),
       ]),
       B("Pāra skaitļi un salīdzinājums", [
           ("Kuri skaitļi dalās ar 2?",
            "Nosauc pāra un nepāra skaitļus un raksturo to vietu simta "
            "kvadrātā."),
           ("Kas notiek, skaitot pa 2?",
            "Skaita pa 2 uz priekšu un atpakaļ, sākot no jebkura skaitļa, un "
            "veido virkni."),
           ("Kas rodas, saskaitot divus pāra skaitļus?",
            "Pēta un formulē likumsakarību par pāra un nepāra skaitļu summu."),
           ("Kā izskatās virkne, kas dubultojas?",
            "Veido virkni, kurā katrs nākamais skaitlis ir divreiz lielāks, "
            "un apraksta to."),
           ("Par 2 lielāks vai 2 reizes lielāks?",
            "Nošķir «par 2 lielāks» no «2 reizes lielāks» shematiskā "
            "zīmējumā."),
           ("Cik gara ir otra sloksnīte?",
            "Risina situāciju uzdevumu, kurā viens lielums ir 2 reizes "
            "lielāks vai mazāks nekā otrs."),
       ])],
      "Reizināšana un dalīšana ar 2",
      "Reizina viencipara skaitļus ar 2 un dala pāra skaitļus ar 2; skaidro "
      "darbību jēgu ar modeli; lieto jēdzienus «2 reizes vairāk» un «puse»; "
      "atšķir pāra un nepāra skaitļus.",
      "virknes, kurās skaitlis dubultojas vairākas reizes."),

    T("2.8.", "Kā reizina un dala ar 3, 4 un 5?",
      "Pilnveido izpratni par reizināšanu un dalīšanu; iegaumē viencipara "
      "skaitļu reizinājumus ar 2, 3, 4 un 5.",
      [B("Reizināšana ar 3", [
          ("Kurus skaitļus var salikt no trim vienādiem?",
           "Meklē skaitļus, ko var uzrakstīt kā trīs vienādu skaitļu summu."),
          ("Ko nozīmē reizināt ar 3?",
           "Modelē ar priekšmetiem doto daudzumu un 3 reizes lielāku "
           "daudzumu; pieraksta reizinājumu."),
          ("Kā skaitīt pa 3?",
           "Skaita pa 3 uz priekšu, pieraksta virkni un izmanto skaitļu "
           "taisni."),
          ("Cik rūtiņu ir taisnstūrī?",
           "Nosaka rūtiņu skaitu taisnstūrī, skaitot pa rindām vai kolonnām, "
           "un pieraksta reizinājumu."),
          ("Vai 3 · 4 un 4 · 3 ir vienādi?",
           "Ar taisnstūra modeli skaidro, kāpēc reizinātāju secība nemaina "
           "rezultātu."),
          ("Kā izveidot reizināšanas ar 3 tabulu?",
           "Izveido reizināšanas ar 3 tabulu un pārbauda to ar modeli."),
          ("Kā aprēķināt vairāku vienādu pirkumu summu?",
           "Pieraksta vienādu saskaitāmo summu kā reizinājumu un aprēķina "
           "rezultātu."),
          ("Cik veikli zini reizinājumus ar 3?",
           "Trenējas ar kartītēm un atzīmē, kurus reizinājumus jau zina no "
           "galvas."),
      ]),
       B("Reizināšana ar 4 un 5", [
           ("Ko nozīmē reizināt ar 4?",
            "Modelē reizināšanu ar 4 kā divkāršu dubultošanu un pieraksta "
            "rezultātu."),
           ("Kur dabā ir pa 4?",
            "Atrod objektus ar 4 vienādiem elementiem un aprēķina to "
            "kopskaitu."),
           ("Kā skaitīt pa 5?",
            "Skaita pa 5 uz priekšu un izmanto to reizinājumu iegūšanai."),
           ("Kāpēc reizinājumi ar 5 ir viegli?",
            "Formulē likumsakarību par reizinājumu ar 5 pēdējo ciparu."),
           ("Kā apvienot visas tabulas?",
            "Sakārto reizinājumus ar 2, 3, 4 un 5 vienā pārskatāmā tabulā."),
           ("Cik kopā maksā pieci vienādi pirkumi?",
            "Risina sadzīves uzdevumu, kurā jāreizina ar 4 vai 5."),
           ("Cik gara ir visu šķautņu summa?",
            "Ar saskaitīšanu un reizināšanu nosaka figūras malu vai šķautņu "
            "garumu summu."),
           ("Kurus reizinājumus vēl jāiemācās?",
            "Pārbauda sevi ar kartītēm un izvēlas, ko trenēt mērķtiecīgi."),
       ]),
       B("Dalīšana ar 3, 4 un 5", [
           ("Kā sadalīt konfektes taisnīgi?",
            "Praktiski dala daudzumu 3, 4 vai 5 vienādās daļās un pieraksta "
            "dalījumu."),
           ("Cik bērniem pietiks?",
            "Dala daļās pa 3, 4 vai 5 un nosaka daļu skaitu."),
           ("Kā reizinājums palīdz dalīt?",
            "Nosaka dalījumu, domājot, ar cik jāreizina dalītājs "
            "(16 : 2 = ? jo 2 · 8 = 16)."),
           ("Kas ir trešdaļa, ceturtdaļa, piektdaļa?",
            "Sadala figūru rūtiņu lapā vienādās daļās un nosauc katru daļu."),
           ("Kā pārbaudīt dalīšanu?",
            "Pārbauda dalījumu ar reizināšanu."),
           ("Vai vienmēr dalās bez atlikuma?",
            "Nosaka, kurus skaitļus līdz 50 var izdalīt ar 3, 4 vai 5 bez "
            "atlikuma."),
           ("Kā samaksāt ar vienādām monētām?",
            "Pieraksta, kādas summas var samaksāt ar 3, 4 vai 5 vienādām "
            "monētām."),
           ("Cik veikli dali?",
            "Patstāvīgi dala skaitļus līdz 50 ar 2, 3, 4 un 5 un pārbauda "
            "rezultātu."),
       ]),
       B("Divu darbību uzdevumi un salīdzinājums", [
           ("Reizes vai vienības?",
            "Nošķir «par tik lielāks» no «tik reižu lielāks», attēlojot abus "
            "shematiskā zīmējumā."),
           ("Kāda darbība jāizpilda vispirms?",
            "Nosaka darbību secību izteiksmē, kurā ir reizināšana un "
            "saskaitīšana."),
           ("Kā pierakstīt divu darbību risinājumu?",
            "Veido divu darbību izteiksmi situāciju uzdevumam un aprēķina tās "
            "vērtību."),
           ("Cik kopā abiem?",
            "Risina uzdevumu, kurā viens lielums ir vairākas reizes lielāks "
            "un jāatrod kopsumma."),
           ("Ko stāsta diagramma?",
            "Lasa un zīmē stabiņu diagrammu par lielumiem, kas atšķiras "
            "vairākas reizes."),
           ("Cik kubu ir ķermenī?",
            "No kubiem būvē ķermeni un aprēķina kubu skaitu, izmantojot "
            "reizināšanu."),
           ("Kā uzrakstīt uzdevumu izteiksmei?",
            "Izdomā situāciju, kas atbilst dotai izteiksmei ar reizināšanu "
            "vai dalīšanu."),
           ("Cik daudz jau protu?",
            "Patstāvīgi risina jauktus uzdevumus ar visām četrām darbībām."),
       ])],
      "Reizināšana un dalīšana ar 2, 3, 4 un 5",
      "Reizina viencipara skaitļus ar 2, 3, 4 un 5; dala skaitļus līdz 50 bez "
      "atlikuma; risina uzdevumus par «tik reižu vairāk»; aprēķina divu "
      "darbību izteiksmes vērtību.",
      "reizināšana ar 6 un 10; trīs skaitļu reizinājums."),
]

NOSLEGUMS = [
    B("Ko esmu iemācījies 2. klasē", [
        ("Cik veikli rēķinu 100 apjomā?",
         "Formatīvi pārbauda saskaitīšanu un atņemšanu 100 apjomā un atzīmē, "
         "kas vēl jātrenē."),
        ("Kurus reizinājumus zinu no galvas?",
         "Pārbauda reizinājumus ar 2, 3, 4 un 5 un izvēlas trenējamos."),
        ("Kā risinu uzdevumu ar diviem soļiem?",
         "Risina divu soļu uzdevumu, pieraksta to ar izteiksmi un skaidro "
         "risinājumu."),
        ("Ko gribu iemācīties 3. klasē?",
         "Apkopo gadā apgūto un iepazīstas ar 3. klases tematiem."),
    ]),
]
