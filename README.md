# Fizika un dabaszinības

Stundu prezentācijas telefonam un datoram: **Dabaszinības** (fizikas daļa,
10.-12. klase) un **Fizika I** (10.-11. klase, 3 stundas nedēļā).

Sākumlapa ir [`index.html`](index.html) — divas pogas, katra ved uz sava
priekšmeta tematu sarakstu, kur stundas atveras uz pieskāriena.

## Mapes

| Mape | Kas tur ir |
|---|---|
| `Dabaszinibas/`, `Fizika_1/` | temati apakšmapēs, katrā stundas `.html` |
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
```

Katra prezentācija ir viens patstāvīgs HTML fails: uz datora precīzs platais
slaids, uz telefona tas pats saturs vienā slejā. Poga **Pilnekrāns** rāda
slaidus pa vienam uz visa ekrāna (Esc — ārā, bultiņas — uz priekšu un atpakaļ).

## Uzbūve

Atbildības ir sadalītas pa moduļiem, lai vienu lietu nevajadzētu labot divās
vietās:

| Modulis | Atbild par |
|---|---|
| `_tools/courses.py` | kursu saraksts: mapes, nosaukumi, secība |
| `_tools/palette.py` | krāsas, fonti, formas; arī veco slaidu krāsu pārnešana |
| `_tools/site_index.py` | sākumlapa un tematu saraksti |
| `_tools/html_deck.py` | `.pptx` → responsīva HTML prezentācija |
| `_tools/mathfmt*.py` | formulas: vertikālas daļas, kvadrātsaknes, vektori |
| `_tools/zimejumi.py` | vektoru zīmējumi slaidos (bultas, apzīmējumi) |

Krāsu shēma (indigo–violets–ciāns) ir viena visai vietnei un dzīvo tikai
`palette.py`; to nomainot un pārbūvējot, mainās visas lapas.

Prasības saturam un noformējumam ir aprakstītas `rules_lessons.txt`.
