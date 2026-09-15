# -*- coding: utf-8 -*-
"""Matemātikas tematu reģistrs 1.-9. klasei - viena vieta, kas ir vietnē.

Temati un to secība nāk no oficiālās programmas (PD_generate/mat_p.pdf,
4. pielikums «Tematu pārskats 1.-9. klasei matemātikā»), tāpēc darbu saraksts
atbilst tam, ko skolotājs māca, un nav izdomāts no jauna (rules_mat.txt).

Šo lasa gan gen_mat.py (ko būvēt), gan site_index.py (ko rādīt sarakstā),
tāpēc nosaukumi un mapes ir vienā eksemplārā (DRY).

Lauki:
    MAPE     - kursa sakne vietnē
    KLASES   - katrai klasei mape un tematu saraksts (kods, nosaukums)
    SATURS   - temata kods -> satura modulis (mat_*.py); ja koda te nav,
               temats sarakstā ir redzams, bet pogas vēl nav aktīvas
"""

import glob
import os
import re

MAPE = "PD_generate"
NOSAUKUMS = "Matemātika 1.-9. klasei"
KICKER = "matemātika · 1.-9. klase"
POGA = "PD ģenerēšana"          # uzraksts uz sākumlapas pogas
LEAD = ("Izvēlies klasi un tematu. Katram tematam ir divi darbi: īss "
        "formatīvais darbs vienā lapā un summatīvais pārbaudes darbs divās "
        "lapās.")

# Darbu veidi. Atslēga ir arī faila nosaukuma daļa, tāpēc to lieto gan
# ģenerators, gan tematu saraksts (DRY).
VEIDI = [
    ("fd", "Formatīvais darbs"),
    ("pd", "Summatīvais PD"),
]

KLASES = [
    (1, "1. klase", [
        ("1.1.", "Kā izstāsta un parāda: cik, kur, kāds?"),
        ("1.2.", "Cik kopā, cik palika?"),
        ("1.3.", "Kā mēra garumus un kā iegūst simetrisku figūru?"),
        ("1.4.", "Kā pieraksta un salīdzina skaitļus, kuri ir lielāki nekā 10?"),
        ("1.5.", "Kā saskaita un atņem skaitļus, kuri lielāki nekā 10?"),
        ("1.6.", "Ko nozīmē «par tik vairāk», «par tik mazāk»?"),
        ("1.7.", "Kur sastopamies ar lieliem skaitļiem?"),
        ("1.8.", "Kā apraksta un veido figūras?"),
    ]),
    (2, "2. klase", [
        ("2.1.", "Kā grupē objektus?"),
        ("2.2.", "Kā nosaka dažādus garumus?"),
        ("2.3.", "Kā saskaita un atņem divciparu skaitļus?"),
        ("2.4.", "Kā laika rēķini palīdz plānot?"),
        ("2.5.", "Kā rodas izteiksme?"),
        ("2.6.", "Kā veido un raksturo figūras?"),
        ("2.7.", "Ko nozīmē reizināt un dalīt ar 2?"),
        ("2.8.", "Kā reizina un dala ar 3, 4 un 5?"),
    ]),
    (3, "3. klase", [
        ("3.1.", "Kā reizina un dala ar 6, 7, 8, 9 un 10?"),
        ("3.2.", "Kā izmanto visas darbības?"),
        ("3.3.", "Kā veido vietas plānu?"),
        ("3.4.", "Ko nozīmē daļa no veselā?"),
        ("3.5.", "Kādi lielumi raksturo figūru?"),
        ("3.6.", "Kā saskaita un atņem trīsciparu skaitļus?"),
        ("3.7.", "Kā veido telpiskus modeļus?"),
    ]),
    (4, "4. klase", [
        ("4.1.", "Kā saskaita un atņem daudzciparu skaitļus?"),
        ("4.2.", "Kā daudzciparu skaitļus reizina un dala ar viencipara "
                 "skaitli?"),
        ("4.3.", "Kā mēra leņķi?"),
        ("4.4.", "Kā daudzciparu skaitļus reizina un dala ar divciparu "
                 "skaitli?"),
        ("4.5.", "Kā salīdzina, saskaita un atņem daļskaitļus?"),
        ("4.6.", "Ko nozīmē daļa no veselā?"),
        ("4.7.", "Kā nosaka dažādu figūru laukumu?"),
        ("4.8.", "Kas kopīgs iepirkšanās un kustības matemātiskajā "
                 "aprakstā?"),
    ]),
    (5, "5. klase", [
        ("5.1.", "Kā dažādi pieraksta naturālos skaitļus?"),
        ("5.2.", "Kā lieto skaitļa sadalīšanu reizinātājos?"),
        ("5.3.", "Kā skaidro un lieto daļas pamatīpašību?"),
        ("5.4.", "Kā vienu skaitli izsaka kā otra skaitļa daļu?"),
        ("5.5.", "Kā saskaita un atņem jauktus skaitļus?"),
        ("5.6.", "Kā nosaka figūru nezināmos lielumus?"),
        ("5.7.", "Kā lieto decimāldaļas un procentus?"),
        ("5.8.", "Kā vizuāli attēlo sakarību starp lielumiem?"),
    ]),
    (6, "6. klase", [
        ("6.1.", "Kā kopumu sadala noteiktā attiecībā?"),
        ("6.2.", "Kā reizina un dala parastās daļas?"),
        ("6.3.", "Kā izpratne par komata lietojumu palīdz, ja reizina un "
                 "dala decimāldaļas?"),
        ("6.4.", "Kā attēlo un raksturo telpiskus ķermeņus?"),
        ("6.5.", "Kā sadzīves situācijās izmanto procentus?"),
        ("6.6.", "Kāpēc nepieciešami skaitļi, kuri ir mazāki nekā nulle?"),
        ("6.7.", "Ko nozīmē skaitlim pieskaitīt negatīvu skaitli, no skaitļa "
                 "atņemt negatīvu skaitli?"),
        ("6.8.", "Kā plāno darbību izpildi ar visu veidu skaitļiem?"),
    ]),
    (7, "7. klase", [
        ("7.1.", "Kā nosaka kopas visus elementus, aprēķina notikuma "
                 "varbūtību?"),
        ("7.2.", "Kā definē ģeometriskas figūras?"),
        ("7.3.", "Kā raksturo sakarību starp mainīgiem lielumiem?"),
        ("7.4.", "Kā pieraksta un pēta funkcijas, kuru grafiks ir taisne?"),
        ("7.5.", "Kā raksturo trijstūri, izmantojot tā elementus?"),
        ("7.6.", "Kādas ir sakarības starp lielumiem trijstūrī?"),
        ("7.7.", "Ko nozīmē pārveidot izteiksmi ar mainīgo lielumu?"),
        ("7.8.", "Kādi ir paņēmieni nezināmā noteikšanai?"),
        ("7.9.", "Kā salīdzina izteiksmes, kurās ir mainīgais lielums?"),
    ]),
    (8, "8. klase", [
        ("8.1.", "Kā matemātiski raksturo un analizē datus?"),
        ("8.2.", "Kā skaidro un lieto pakāpi ar veselu kāpinātāju?"),
        ("8.3.", "Kā rīkojas, ja skaitli nevar pierakstīt kā daļu?"),
        ("8.4.", "Kā aprēķina laukumu jebkuram trijstūrim, riņķim?"),
        ("8.5.", "Kas kopīgs četrstūriem, kuru pretējās malas ir pa pāriem "
                 "paralēlas?"),
        ("8.6.", "Kā skaidro un izpilda darbības ar izteiksmēm?"),
        ("8.7.", "Kā dažādas funkcijas izmanto matemātiskai modelēšanai?"),
        ("8.8.", "Kā nosaka taisnleņķa trijstūra nezināmās malas garumu?"),
    ]),
    (9, "9. klase", [
        ("9.1.", "Kā definē un raksturo līdzīgus trijstūrus?"),
        ("9.2.", "Kas kopīgs četrstūriem, kuriem tieši divas malas ir "
                 "paralēlas?"),
        ("9.3.", "Kā aprēķinos izmanto taisnleņķa trijstūra divu malu "
                 "attiecību?"),
        ("9.4.", "Kā izmanto izteiksmju sadalīšanu reizinātājos?"),
        ("9.5.", "Kā skaidro un izmanto formulas darbā ar "
                 "kvadrātvienādojumu, kvadrātfunkciju?"),
        ("9.6.", "Kā apraksta situācijas ar diviem nezināmiem lielumiem?"),
        ("9.7.", "Kā skaitļu virkni pieraksta ar formulu?"),
        ("9.8.", "Kā raksturo riņķa līnijas un daudzstūra savstarpējo "
                 "novietojumu?"),
    ]),
]

# Temata kods -> satura modulis. Sarakstu neuztur ar roku: par tematu ar
# saturu skaitās katrs fails mat_<klase>_<temats>.py, tāpēc jaunu tematu
# pievieno, tikai uzrakstot vienu failu (DRY).
def _atrastie():
    mape = os.path.dirname(os.path.abspath(__file__))
    out = {}
    for ce in glob.glob(os.path.join(mape, "mat_*_*.py")):
        vards = os.path.splitext(os.path.basename(ce))[0]
        m = re.match(r"^mat_(\d+)_(\d+)$", vards)
        if m:
            out["%s.%s." % m.groups()] = vards
    return out


SATURS = _atrastie()


def klases():
    """Klases sākumlapas secībā."""
    return KLASES


def mape(nr):
    """Klases numurs -> mapes nosaukums vietnē."""
    for k, folder, _ in KLASES:
        if k == nr:
            return folder
    raise KeyError(nr)


def temati(nr):
    """Vienas klases temati."""
    for k, _, ts in KLASES:
        if k == nr:
            return ts
    raise KeyError(nr)


def fails(kods, veids):
    """Temata koda un darba veida faila nosaukums (bez .html)."""
    return "%s %s" % (kods, dict(VEIDI)[veids])


def gatavs(kods):
    """Vai tematam jau ir uzrakstīts saturs."""
    return kods in SATURS
