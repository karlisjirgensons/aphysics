# PD un nodarbības

Pārbaudes darbu ģenerators un stundu prezentācijas telefonam un datoram:
**Matemātikas stundas** (1.-9. klase, katru mācību dienu),
**Dabaszinības** (fizikas daļa, 10.-12. klase), **Fizika I** (10.-11. klase,
3 stundas nedēļā) un **PD ģenerēšana** (matemātika 1.-9. klasei).

Sākumlapa ir [`index.html`](index.html) — trīs pogas: divas ved uz priekšmeta
tematu sarakstu, kur stundas atveras uz pieskāriena, trešā — uz matemātikas
pārbaudes darbu ģeneratoru.

## Mapes

| Mape | Kas tur ir |
|---|---|
| `Dabaszinibas/`, `Fizika_1/` | temati apakšmapēs, katrā stundas `.html` |
| `Math/` | matemātikas stundas: klase -> temati -> stundas; klašu plāni `math_N.docx` |
| `PD_generate/` | matemātikas darbu ģenerators: klases, temati, programma |
| `_tools/` | ģeneratori: no `.pptx` uz HTML, saraksti, palete |

Prezentāciju avoti (`.pptx`), skolas materiāli (`.pdf`, `.docx`) un video
repozitorijā nav — tie ir par lieliem GitHub un daļa ir citu autoru
materiāli. Stundu saturs ir pašos `_tools/*.py` skriptos, tāpēc prezentācijas
var uzģenerēt no jauna.

## Uzbūvēšana

```bash
python _tools/html_deck.py               # visas dabaszinību prezentācijas
python _tools/html_deck.py fizika        # visas fizikas prezentācijas
python _tools/site_index.py              # tikai sākumlapa un saraksti
python _tools/gen_fiz_plani.py           # fizikas tematu, PD un LD plāni
python _tools/gen_fd.py                  # formatīvo darbu ģeneratori
python _tools/gen_mat.py                 # matemātikas PD ģeneratori
python _tools/gen_math.py                # matemātikas stundu plāni un lapas
```

Katra prezentācija ir viens patstāvīgs HTML fails: uz datora precīzs platais
slaids, uz telefona tas pats saturs vienā slejā. Telefonā slaidus šķir ar
pirkstu — tie stāv horizontālā lentē un piesienas pie ekrāna malas, un
augšējā josla rāda, kurš slaids ir redzams. Poga **Pilnekrāns** rāda slaidus
pa vienam uz visa ekrāna (Esc — ārā, bultiņas — uz priekšu un atpakaļ).

## Formatīvais darbs

Temata stundu saraksta beigās ir poga **Ģenerēt formatīvo darbu**. Tā atver
lapu, kas pati izlozē īsu 12 jautājumu testu (~15 minūtes): darbu var apskatīt
ekrānā, ieslēgt atbildes, izdrukāt vai lejupielādēt kā Word failu — atsevišķi
skolēna darba lapu un atbilžu lapu skolotājam. Viss notiek pārlūkā, tāpēc
vietne paliek statiska.

Saturs ir sadalīts jautājumu grupās: viena grupa = viens sasniedzamais
rezultāts, un tajā ir vairāki līdzvērtīgi jautājumi. No katras grupas lapa
paņem vienu, tāpēc darba uzbūve nemainās, bet lapas atšķiras (12 grupas ar
trim jautājumiem dod vairāk nekā 500 000 dažādu darbu). Katram darbam ir
četru zīmju variants kods — ar to pašu kodu vienmēr sanāk tā pati lapa.

Jaunu jautājumu pievieno, ierakstot to grupā `_tools/fd_*.py` failā; jaunu
tematu — uzrakstot vēl vienu `fd_*.py` un pierakstot tā kodu `gen_fd.py`
sarakstā. Būvējot tiek pārbaudīts, vai arī pats garākais iespējamais darbs
ietilpst vienā A4 lapā.

## Matemātikas pārbaudes darbi

Sākumlapas poga **PD ģenerēšana** atver [`PD_generate/index.html`](PD_generate/index.html):
deviņas klases, katrā tās temati pa vienam rindā, un katram tematam divas
pogas — **Formatīvais darbs** (viena lapa, 12 jautājumi ar atbildēm A-D) un
**Summatīvais PD** (divas lapas: tests un uzdevumi ar darba vietu). Temati,
to secība un nosaukumi ir no oficiālās programmas `PD_generate/mat_p.pdf`
(4. pielikums), tāpēc sarakstā ir visa programma; pogas ir aktīvas tiem
tematiem, kuriem saturs jau ir uzrakstīts.

Lapa rāda vienu darbu; poga **Ģenerēt** izlozē nākamo. Variantam nav kārtas
numura — to apzīmē piecu zīmju kods (piemēram, T32MC), tāpēc pēc koda nevar
noprast, kurš darbs kuram skolēnam dots. Ar to pašu kodu vienmēr sanāk tā
pati lapa, tāpēc drukāt var tieši to, ko rāda ekrāns; kods ir arī lapas
adresē aiz `#`. No 12 grupām ar trim jautājumiem sanāk vairāk nekā 500 000
dažādu formatīvo darbu.

Jaunu tematu pievieno ar vienu failu: `_tools/mat_<klase>_<temats>.py` ar
`FD` un `PD` saturu — `mat_temati.py` to atrod pats. Būvējot tiek pārbaudīts, vai formatīvais darbs ietilpst vienā A4
lapā un pārbaudes darbs — divās, vai punkti sakrīt un vai katrā grupā pietiek
jautājumu trim variantiem.

Lai izlozētie darbi patiešām atšķirtos, vienā grupā vajag daudz līdzvērtīgu
jautājumu (mērķis — 15). Rēķinu jautājumus neraksta ar roku pa vienam: vienu
veidni un skaitļu sarakstu pavairo `_tools/mat_varianti.py`, tāpēc no trim
rindām koda sanāk piecpadsmit jautājumi. Būvēšanas paziņojums pasaka, cik
jautājumu ir visnabadzīgākajā grupā — ja mazāk nekā 15, tematam vēl vajag
jautājumus.

## Matemātikas stundas

Sākumlapas poga **Matemātikas stundas** atver [`Math/index.html`](Math/index.html):
deviņas klases, katrā tās temati programmas secībā, un tematā — stundas,
sagrupētas pa mikrotematiem. Stunda kļūst par pogu tikai tad, kad tās lapa ir
uzrakstīta; pārējās paliek pelēkas, tāpēc sarakstā vienmēr redzams viss gada
plāns. Gada plāns ir arī `Math/math_N.docx`.

Stunda ir viens patstāvīgs HTML fails, veidots vispirms telefonam: viena
sleja, liels teksts un lielas pogas, platākam ekrānam — tikai vairāk vietas
malās. Stunda sākas ar to, kur šo vajag dzīvē, tad nāk galvenā doma, spēles,
kurās to izmēģina uzreiz, kopsavilkums un darbiņš mājās. Skolotāja rinda ar
sasniedzamo rezultātu un datumu ir salokāma — skolēnam tā nav priekšā.

Uz platā ekrāna poga **Pilnekrāns** rāda to pašu stundu kā prezentāciju:
virsraksts un katrs bloks pa vienam uz visa ekrāna. Šķir ar pirkstu, ar
bultiņām, ar pogām ‹ › vai ar atstarpi; Esc iziet ārā — tāpat kā fizikas
prezentācijās.

Uzdevumos pirmās kārtas izdara visi, un beigās poga **Vēl divi uzdevumi**
izsniedz nākamo pāri tiem, kas tiek galā ātrāk. Cik kārtas ir obligātās,
pasaka `pamats`, un stundas garums no tā nemainās.

Jaunu stundu pievieno ar vienu failu: `_tools/math_<klase>_<numurs>.py` ar
`TEMA` (tā pati, kas plānā), `MERKIS` un `SATURS` — bloku sarakstu, ko
importē no `math_saturs.py`. Numerācija ir tā pati, kas gada plānā, un būvējot
tiek pārbaudīts, vai stundas tēma sakrīt ar plānu. Pēc tam `python
_tools/gen_math.py <klase>` uzraksta lapu un pārbūvē sarakstus.

Katra temata pēdējā stunda ir pārbaudes darbs. Tā lapu neviens neraksta — to
saliek `math_pd.py` no paša plāna (ko vērtēs, ko atkārtot), tāpēc deviņām
klasēm tās ir septiņdesmit divas bez viena satura faila.

Divas lietas stundas uzbūvē ir obligātas, un tās pārbauda būvētājs, nevis
autors — tāpēc tās der visām klasēm un tematiem vienādi:

* **stunda sākas ar `Sakums`** — viens jautājums, attēls un līdz trim īsiem
  faktiem. Rindkopu ievada nav: skolēns to nelasa, un garā tekstā visvieglāk
  iezogas kļūda. Fakta garumu un skaitu ierobežo pati klase, tāpēc par garš
  ievads vienkārši neuzbūvējas;
* **stundā ir vismaz viens `Pasaule` uzdevums** — tas pats rēķins par īstu
  lietu. `Pasaule` pati neko nerēķina: tā apņem jebkuru uzdevuma bloku
  (`Ievadi`, `Varianti` vai 1. klases `Izvele`), tāpēc viens ietvars der no
  pirmās līdz devītajai klasei.

Katrs `Pasaule` uzdevums pieder **pavedienam** — vienam dzīves tematam, kas
iet cauri vairākām stundām (`math_pavedieni.py`): 5.1. temata pirmajās
stundās tas ir kosmoss, nākamajās — dators un dati. Tā stundas cita citu
turpina, nevis stāv atsevišķi, un pavediena nosaukums ir uzrakstīts vienā
vietā.

Attēlus zīmē pati lapa (`math_zimejumi.py`): skaitļu taisne, laika ass, Venna
diagramma, stabiņu salīdzinājums un bitu slēdži. Tie mērogojas līdz ar tekstu
un der gan stundas sākumā, gan atsevišķā blokā.

Matemātiku stundas tekstā raksta ar to pašu marķējumu, ko darba lapās
(`PD_generate/rules_pd.txt`): `{3|4}` ir vertikāla daļa, `√(a + b)` — sakne,
`*7*` — izcelts gabals. HTML birkas saturā rakstīt nedrīkst; tās nonāktu lapā
kā teksts. Mērvienības (`12 m/s`) paliek rindā, kā prasa latviešu standarts.

Uzrakstīto pārbauda ar vienu komandu:

```bash
python _tools/check_stunda.py 5          # visas 5. klases stundas
```

Tā atver katru lapu īstā pārlūkā 390 px platumā un izspēlē katru uzdevumu:
vai saturs neizplūst ārpus ekrāna, vai lapas JavaScript nostrādā, vai katru
uzdevumu var izpildīt līdz galam, vai nepareiza atbilde tiek noraidīta un vai
ekrānā nav palicis neizšķirts marķējums. Atbilde ir saraksts, nevis bilde.

Attēli stundās ir zīmēti ar SVG līnijām (`math_ikonas.py`), nevis ņemti no
emocijzīmju fonta, un līdzās katram attēlam ir tā vārda trīs formas, tāpēc
lapa pati uzraksta «1 logs», «2 logi», «0 logu».

## Uzbūve

Atbildības ir sadalītas pa moduļiem, lai vienu lietu nevajadzētu labot divās
vietās:

| Modulis | Atbild par |
|---|---|
| `_tools/courses.py` | kursu saraksts: mapes, nosaukumi, secība |
| `_tools/palette.py` | krāsas, fonti, formas; arī veco slaidu krāsu pārnešana |
| `_tools/site_index.py` | sākumlapa un tematu saraksti |
| `_tools/html_deck.py` | `.pptx` → responsīva HTML prezentācija |
| `_tools/deck_page.py` | prezentācijas lapas čaula: CSS, vadība, veidne |
| `_tools/mathfmt*.py` | formulas: vertikālas daļas, kvadrātsaknes, vektori |
| `_tools/zimejumi.py` | vektoru zīmējumi slaidos (bultas, apzīmējumi) |
| `_tools/fd_common.py` | formatīvā darba saturs → ģeneratora lapa, pārbaudes |
| `_tools/fd_page.py` | ģeneratora lapas čaula: CSS, izloze, druka |
| `_tools/fd_paper.py` | darba lapas modelis un abi attēlotāji (ekrāns, Word) |
| `_tools/fd_docx.py` | .docx rakstītājs pārlūkā (ZIP + OOXML, bez servera) |
| `_tools/fd_stils.py` | darba lapas noformējums: fonts, krāsas, izmēri |
| `_tools/izloze.py` | varianta izloze pārlūkā: kods, sēkla, atbilžu kārtība |
| `_tools/mat_temati.py` | matemātikas klases un temati pēc programmas |
| `_tools/mat_varianti.py` | veidnes: no viena parauga daudz līdzvērtīgu jautājumu |
| `_tools/mat_common.py` | matemātikas darba saturs → ģeneratora lapa, pārbaudes |
| `_tools/mat_page.py` | trīs variantu lapas čaula: CSS, vadība, druka |
| `_tools/math_plani.py` | matemātikas gada plāni: stundu numuri, datumi, PD svari |
| `_tools/math_vietne.py` | matemātikas klašu un tematu saraksti |
| `_tools/math_stundas.py` | stundu lapas: kuras ir uzrakstītas un kur tās liek |
| `_tools/math_lapa.py` | stundas lapas čaula: augšējā josla, galva, bloku vieta |
| `_tools/math_bloki.py` | stundas bloki: stāsts, doma, spēles, kopsavilkums |
| `_tools/math_pilnekrans.py` | stundas pilnekrāna skats: viena daļa uz visa ekrāna |
| `_tools/math_ikonas.py` | zīmētie attēli stundām un vārdu formas |
| `_tools/math_saturs.py` | viena vieta, ko stundas failam importēt |
| `_tools/math_uzdevumi.py` | uzdevumi ar atbildi: paraugs, ievade, varianti |
| `_tools/math_zimejumi.py` | skaitļu taisne, laika ass, Venna diagramma, stabiņi, biti |
| `_tools/math_pavedieni.py` | dzīves temati, kas iet cauri vairākām stundām |
| `_tools/math_pd.py` | pārbaudes darba stunda, salikta no plāna |
| `_tools/mathhtml.py` | daļas, saknes un indeksi HTML — arī prezentācijām |
| `_tools/check_stunda.py` | stundu lapu pārbaude pārlūkā, viena komanda |
| `_tools/mat_paper.py` | pārbaudes darba divas lapas (uzdevumi, darba vieta) |
| `_tools/fiz_plani.py` | plānu veidnes un mācību grafiki (kad ir stundas) |
| `_tools/gen_fiz_plani.py` | plāni katram stundu sarakstam (Ādaži, Carnikava) |

Krāsu shēma (indigo–violets–ciāns) ir viena visai vietnei un dzīvo tikai
`palette.py`; to nomainot un pārbūvējot, mainās visas lapas.

Prasības saturam un noformējumam ir aprakstītas `rules_lessons.txt`, bet
matemātikas darbiem — `PD_generate/rules_mat.txt` un
`PD_generate/rules_pd.txt`.
