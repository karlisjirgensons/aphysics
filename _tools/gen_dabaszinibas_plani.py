# -*- coding: utf-8 -*-
"""
Ģenerē Dabaszinību (fizikas daļas) tematu un pārbaudes darbu plānus
10., 11. un 12. klasei - atsevišķs fails katrai klasei.

Paraugs: example_theme_plan_and_test_plan.pdf
Atšķirības pēc uzdevuma:
  - vērtējumi TIKAI pārbaudes darbi (PD); nav LD, PR vai citu darbu veidu;
  - vērtēšanas kalendārā NAV svara (%) ailes.

Saturs veidots pēc dabaszinibas_programma.pdf tematiem:
  10. klase - temati 10.1.-10.5.;  11. klase - 10.6.-10.10.;
  12. klase - 10.11.-10.16.   Māca tikai fizikas daļu (rules_dabaszinibas.txt).
"""

import datetime as dt
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SKOLA = "Ādažu vidusskola"
GADS = "2026./2027."
NAVY = RGBColor(0x1F, 0x38, 0x64)
GREY = RGBColor(0x60, 0x60, 0x60)

# ------------------------------------------------------------ mācību kalendārs
BRIVLAIKI = [(dt.date(2026, 10, 19), dt.date(2026, 10, 23)),
             (dt.date(2026, 12, 23), dt.date(2027, 1, 4)),
             (dt.date(2027, 3, 15), dt.date(2027, 3, 19))]
SVETKI = [dt.date(2026, 11, 18),      # Latvijas Republikas proklamēšanas diena
          dt.date(2027, 3, 26),      # Lielā Piektdiena (Lieldienas 28.03.2027.)
          dt.date(2027, 5, 4)]       # Neatkarības atjaunošanas diena


def stundu_datumi(sakums=dt.date(2026, 9, 1), beigas=dt.date(2027, 5, 31)):
    """Fizikas stundas notiek TIKAI piektdienās - viena stunda nedēļā."""
    out, cur = [], sakums
    while cur <= beigas:
        if (cur.weekday() == 4
                and not any(a <= cur <= b for a, b in BRIVLAIKI)
                and cur not in SVETKI):
            out.append(cur)
        cur += dt.timedelta(days=1)
    return out


DATUMI = stundu_datumi()


def d(x):
    return x.strftime("%d.%m.%Y")


# =========================================================== dokumenta veidnes
def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def cell_text(cell, text, size=8.5, bold=False, color=None, align=None):
    cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    if align:
        p.alignment = align
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.name = "Calibri"
    if color:
        r.font.color.rgb = color


def para(doc, text, size=9, bold=False, color=None, before=0, after=3,
         italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = "Calibri"
    if color:
        r.font.color.rgb = color
    return p


def new_doc(klase, stundu_skaits):
    doc = Document()
    s = doc.sections[0]
    s.orientation = WD_ORIENT.LANDSCAPE
    s.page_width, s.page_height = Cm(29.7), Cm(21.0)
    s.left_margin = s.right_margin = Cm(1.2)
    s.top_margin = s.bottom_margin = Cm(1.0)

    st = doc.styles["Normal"]
    st.font.name = "Calibri"
    st.font.size = Pt(9)

    para(doc, "Dabaszinības (fizikas daļa)  |  %s  |  %s  |  %s  |  "
               "1 fizikas stunda nedēļā  |  %d mācību stunda"
         % (SKOLA, klase, GADS, stundu_skaits),
         size=9, bold=True, color=NAVY, after=1)
    para(doc, "Mācību priekšmets dabaszinības ietver fiziku, bioloģiju un "
              "ķīmiju. Šis plāns aptver TIKAI fizikas daļu — vienu stundu "
              "nedēļā. Visi vērtējumi ir pārbaudes darbi (PD).",
         size=8.5, color=GREY, after=8)
    return doc


def kalendars(doc, pd_saraksts):
    para(doc, "Darba organizācija un vērtēšanas kalendārs", size=13,
         bold=True, color=NAVY, after=3)
    para(doc, "Mācību gada sākums 01.09.2026., noslēgums 31.05.2027. "
              "Brīvlaiki: 19.–23.10.2026., 23.12.2026.–04.01.2027., "
              "15.–19.03.2027. Datumi ir provizoriski un aprēķināti, "
              "jo fizikas stundas un pārbaudes darbi notiek TIKAI "
              "piektdienās. 26.03.2027. ir Lielā Piektdiena — stundu nav.",
         size=8.5, color=GREY, after=6)

    t = doc.add_table(rows=1, cols=4)
    t.style = "Table Grid"
    hdr = ["Darbs", "Tēma / vērtēšanas objekts", "Datums", "Piezīme"]
    for i, h in enumerate(hdr):
        shade(t.rows[0].cells[i], "1F3864")
        cell_text(t.rows[0].cells[i], h, size=9, bold=True,
                  color=RGBColor(0xFF, 0xFF, 0xFF))
    for kods, tema, datums, piez in pd_saraksts:
        row = t.add_row().cells
        cell_text(row[0], kods, bold=True, color=NAVY)
        cell_text(row[1], tema)
        cell_text(row[2], datums)
        cell_text(row[3], piez, size=8, color=GREY)
    for w, c in zip([2.0, 10.5, 3.0, 11.5], range(4)):
        for row in t.rows:
            row.cells[c].width = Cm(w)

    para(doc, "Kopā %d vērtējumi — visi pārbaudes darbi (PD). "
              "Laboratorijas darbi un citi vērtējumu veidi šajā plānā nav "
              "paredzēti. PD vērtē tikai stundās faktiski apgūto saturu; "
              "neapgūtus izvēles padziļinājumus darbā neiekļauj."
         % len(pd_saraksts), size=8.5, before=6, after=10)


def temata_tabula(doc, virsraksts, komentars, rindas, padzilinajumi=None):
    para(doc, virsraksts, size=12, bold=True, color=NAVY, before=8, after=2)
    if komentars:
        para(doc, komentars, size=8.5, italic=True, color=GREY, after=4)

    t = doc.add_table(rows=1, cols=6)
    t.style = "Table Grid"
    hdr = ["N.p.k.", "Apakštemats", "Stundas tēma / jautājums",
           "Stundas sasniedzamais rezultāts", "Provizoriskais datums", "St."]
    for i, h in enumerate(hdr):
        shade(t.rows[0].cells[i], "1F3864")
        cell_text(t.rows[0].cells[i], h, size=8.5, bold=True,
                  color=RGBColor(0xFF, 0xFF, 0xFF))
    for nr, apak, tema, sr, datums, pd in rindas:
        row = t.add_row().cells
        cell_text(row[0], str(nr), align=WD_ALIGN_PARAGRAPH.CENTER)
        cell_text(row[1], apak, bold=pd)
        cell_text(row[2], tema, bold=pd, color=NAVY if pd else None)
        cell_text(row[3], sr)
        cell_text(row[4], datums, align=WD_ALIGN_PARAGRAPH.CENTER)
        cell_text(row[5], "1", align=WD_ALIGN_PARAGRAPH.CENTER)
        if pd:
            for c in row:
                shade(c, "FFF4D6")
    widths = [1.3, 4.0, 6.0, 11.0, 3.0, 1.0]
    for c, w in enumerate(widths):
        for row in t.rows:
            row.cells[c].width = Cm(w)

    if padzilinajumi:
        para(doc, "Izvēles padziļinājumi, ja atliek laiks: " + padzilinajumi,
             size=8.5, italic=True, color=GREY, before=3, after=6)


def nav_fizikas(doc, virsraksts, kas):
    para(doc, virsraksts, size=12, bold=True, color=GREY, before=8, after=2)
    para(doc, "Šajā tematā fizikas daļas nav — saturu apgūst %s. "
              "Fizikas stundas šajā laikā turpina iepriekšējo vai nākamo "
              "fizikas tematu." % kas,
         size=8.5, italic=True, color=GREY, after=6)


# ============================================================ satura veidošana
class Plans:
    """Pieškir stundu numurus un datumus secīgi visai klasei."""

    def __init__(self):
        self.n = 0
        self.pd = []

    def bloks(self, stundas):
        """stundas: (apakštemats, tēma, SR) vai ('PD', kods, tēma, SR, piez)"""
        out = []
        for s in stundas:
            self.n += 1
            datums = d(DATUMI[self.n - 1])
            if s[0] == "PD":
                _, kods, tema, sr, piez = s
                out.append((self.n, "Summatīvā vērtēšana",
                            "%s: %s" % (kods, tema), sr, datums, True))
                self.pd.append((kods, tema, datums, piez))
            else:
                out.append((self.n, s[0], s[1], s[2], datums, False))
        return out


PIEZ = "Vērtē tikai iepriekš mācīto saturu."

# ------------------------------------------------------------------ 10. KLASE
K10_T1 = [
    ("Matērija: viela un lauks",
     "Kas ir matērija un kādās formās tā pastāv?",
     "Skaidro matēriju, lietojot jēdzienus “viela” un “lauks”; klasificē "
     "objektus mikro-, makro- un megapasaulē pēc izmēra."),
    ("Pasaules organizācijas līmeņi",
     "Kā saistīts atoms ar Galaktiku?",
     "Sakārto objektus pēc izmēra no atoma līdz Visumam; pamato līmeņu "
     "savstarpējo saistību ar piemēriem."),
    ("Fizikālie lielumi un SI",
     "Kāpēc visā pasaulē mēra vienādi?",
     "Lieto fizikālo lielumu apzīmējumus, SI pamatvienības, priedēkļus un "
     "standartformu; pārvērš mērvienības un pārbauda rezultāta ticamību."),
    ("Mikropasaules pētīšana",
     "Ko un ar ko var saskatīt mikropasaulē?",
     "Salīdzina optiskā, elektronu un atomspēku mikroskopa palielinājumu un "
     "izšķirtspēju; izvēlas objektam piemērotu ierīci."),
    ("Mērierīces un mērījumu precizitāte",
     "Vai digitāls mērījums vienmēr ir precīzāks?",
     "Salīdzina analogās un digitālās mērierīces un sensorus; novērtē "
     "mērījuma kļūdu un pieraksta rezultātu ar atbilstošu precizitāti."),
    ("Megapasaules pētīšana",
     "Kā izmēra attālumu līdz zvaigznei?",
     "Raksturo teleskopu un kosmisko zondu iespējas; rēķina ar astronomisko "
     "vienību, gaismas gadu un parseku."),
    ("Pētījuma plānošana un dati",
     "Kā veikt godīgu pētījumu?",
     "Formulē pētāmo jautājumu, nosaka atkarīgo, neatkarīgo un nemainīgos "
     "lielumus; attēlo datus grafikā un formulē secinājumu."),
    ("PD", "PD1", "Pasaule ap mums un tās pētīšana",
     "Skaidro matēriju, klasificē objektus pēc mēroga, pārvērš mērvienības "
     "un pamato mērierīces izvēli.", PIEZ),
]

K10_T3 = [
    ("Atoma uzbūve", "No kā sastāv atoms?",
     "Raksturo kodolu un elektronapvalku; nosaka protonu, neitronu un "
     "elektronu skaitu, izmantojot ķīmisko elementu periodisko tabulu."),
    ("Izotopi un relatīvā atommasa", "Ar ko atšķiras viena elementa atomi?",
     "Salīdzina izotopu kodola sastāvu; aprēķina ķīmiskā elementa relatīvo "
     "atommasu pēc izotopu sastāva."),
    ("Elektronu enerģijas līmeņi",
     "Kāpēc atoms izstaro noteiktas krāsas gaismu?",
     "Skaidro diskrētus enerģijas līmeņus; saista elektrona pāreju starp "
     "līmeņiem ar spektra līniju."),
    ("Atoma modeļu attīstība", "Kāpēc atoma modelis laika gaitā mainījies?",
     "Salīdzina vienkāršotus atoma modeļus; pamato, kā jauns eksperiments "
     "maina zinātnisku modeli."),
    ("Kodolreakcijas", "Kā rodas jauns ķīmiskais elements?",
     "Atšķir kodolu dalīšanos no kodolsintēzes; pieraksta un papildina "
     "vienkāršu kodolreakcijas vienādojumu."),
    ("Radioaktivitāte", "Kāpēc daži atomi sabrūk paši no sevis?",
     "Salīdzina alfa, bēta un gamma starojumu pēc dabas, caurspiešanās "
     "spējas un bīstamības; atšķir dabisko un mākslīgo radioaktivitāti."),
    ("Pussabrukšanas periods", "Cik ilgi viela paliek radioaktīva?",
     "Nolasa sabrukšanas grafiku; aprēķina atlikušo vielas daudzumu pēc "
     "vesela pussabrukšanas periodu skaita."),
    ("Jonizējošais starojums un fons", "Cik daudz starojuma saņemam ikdienā?",
     "Nosauc dabiskos un mākslīgos jonizējošā starojuma avotus; salīdzina "
     "saņemtās devas ar dabisko radioaktīvo fonu."),
    ("Radiācijas drošība", "Kā pasargāties no jonizējošā starojuma?",
     "Pamato aizsardzību ar laiku, attālumu un ekranēšanu; nošķir "
     "apstarošanu no radioaktīva piesārņojuma."),
    ("Radioaktivitātes lietojumi", "Kur izmanto radioaktīvos izotopus?",
     "Ar piemēriem pamato izotopu lietojumu medicīnā, datēšanā un "
     "enerģētikā; izvērtē ieguvumus un riskus."),
    ("Vielas daudzums un daļiņu skaits", "Cik daļiņu ir vienā gramā vielas?",
     "Lieto n = m/M = N/NA; aprēķina daļiņu skaitu, vielas daudzumu un masu."),
    ("Kristāliskas un amorfas vielas", "Kāpēc stikls nav kristāls?",
     "Atšķir kristālisku un amorfu uzbūvi; nosaka kristālrežģa veidu pēc "
     "vielas fizikālajām īpašībām."),
    ("Uzbūve un fizikālās īpašības", "Kā uzbūve nosaka vielas īpašības?",
     "Prognozē kušanas temperatūru, cietību, siltum- un elektrovadītspēju "
     "pēc kristālrežģa veida; labo biežākās kļūdas aprēķinos."),
    ("PD", "PD2", "Atoma uzbūve, radioaktivitāte un vielas uzbūve",
     "Skaidro atoma un kodola uzbūvi, izotopus un starojuma veidus; lasa "
     "sabrukšanas grafiku un veic vienkāršu aprēķinu.", PIEZ),
]

K10_T5 = [
    ("Materiālu fizikālās īpašības", "Pēc kā izvēlas materiālu?",
     "Salīdzina materiālus pēc blīvuma, cietības un kušanas temperatūras; "
     "lieto ρ = m/V un pārbauda mērvienības."),
    ("Mehāniskais spriegums", "Kāpēc trosei ir slodzes robeža?",
     "Lieto σ = F/S; salīdzina materiālu stiprību un pamato drošības rezervi."),
    ("Elastība un plastiskums", "Kāpēc atspere atgriežas, bet plastilīns nē?",
     "Atšķir elastīgu un plastisku deformāciju; skaidro elastības spēku ar "
     "vielas uzbūvi."),
    ("Siltumvadītspēja", "Kāpēc metāls šķiet aukstāks par koku?",
     "Salīdzina materiālu siltumvadītspēju; pamato siltumizolācijas "
     "materiāla izvēli mājoklim."),
    ("Elektrovadītspēja", "Kas vada elektrisko strāvu un kas ne?",
     "Nošķir vadītājus, dielektriķus un pusvadītājus; saista vadītspēju ar "
     "vielas uzbūvi un saites veidu."),
    ("Materiālu grupas", "Ar ko metāli atšķiras no polimēriem?",
     "Salīdzina metālus, keramiku, polimērus un kompozītus pēc uzbūves, "
     "īpašībām un lietojuma."),
    ("Moderni materiāli", "Kādus materiālus rada mūsdienās?",
     "Raksturo kompozītmateriālu un nanomateriālu īpašības; pamato jaunu "
     "materiālu izstrādes nepieciešamību Latvijā."),
    ("Materiāla izvēle ar aprēķinu", "Kā pamatot izvēli ar skaitļiem?",
     "Ar aprēķiniem pamato materiāla izvēli dotai situācijai; pārbauda "
     "mērvienības un rezultāta ticamību."),
    ("Nostiprināšana", "Kā no uzbūves paredzēt pielietojumu?",
     "Sasaista materiāla uzbūvi, īpašības un lietojumu; labo tipiskās "
     "kļūdas un gatavojas pārbaudes darbam."),
    ("PD", "PD3", "Materiālu veidi un fizikālās īpašības",
     "Prognozē materiāla īpašības pēc uzbūves, veic aprēķinu ar σ = F/S vai "
     "ρ = m/V un pamato materiāla izvēli.", PIEZ),
]

K10_NOSL = [
    ("Fizika ap mums", "Kur gada laikā apgūtais noder ikdienā?",
     "Sasaista mērogu, mērvienības, atoma uzbūvi un materiālu īpašības ar "
     "sadzīves piemēriem."),
    ("Gada refleksija", "Ko esmu iemācījies un kas jāpilnveido?",
     "Izvērtē savu sniegumu, atpazīst biežākās kļūdas un plāno nākamā gada "
     "mācīšanos."),
]

# ------------------------------------------------------------------ 11. KLASE
K11_T7A = [
    ("Vektori un skalāri", "Ar ko ātrums atšķiras no ceļa?",
     "Atšķir vektoriālus un skalārus lielumus; saskaita vektorus "
     "ģeometriski un nosaka summas virzienu."),
    ("Ceļš, pārvietojums, trajektorija", "Cik tālu un cik daudz?",
     "Aprēķina un salīdzina ceļu un pārvietojumu kustībai pa dažādām "
     "trajektorijām."),
    ("Vienmērīga kustība", "Kā aprakstīt vienmērīgu kustību?",
     "Lieto v = s/t un x = x₀ + vt; veido un nolasa kustības grafikus."),
    ("Kustības grafiki", "Ko stāsta grafika slīpums?",
     "Nolasa x(t) un v(t) grafikus; nosaka ātrumu pēc grafika slīpuma un "
     "ceļu pēc laukuma."),
    ("Paātrinājums", "Kā mainās ātrums?",
     "Lieto a = Δv/Δt un v = v₀ + at; nosaka paātrinājumu no datiem, "
     "tabulas vai grafika."),
    ("Kustības vienādojums", "Kur ķermenis būs pēc piecām sekundēm?",
     "Lieto x = x₀ + v₀t + at²/2; prognozē koordinātu un ātrumu dotā laika "
     "momentā."),
    ("Brīvā krišana", "Vai smagāks ķermenis krīt ātrāk?",
     "Skaidro brīvo krišanu ar g = 9,81 m/s²; aprēķina krišanas laiku un "
     "ātrumu."),
    ("Kustības drošība", "Cik garš ir bremzēšanas ceļš?",
     "Aprēķina reakcijas un bremzēšanas ceļu; izvērtē faktorus, kas "
     "palielina reakcijas laiku."),
    ("PD", "PD1", "Kustības apraksts (kinemātika)",
     "Lieto kustības sakarības un vienādojumus, lasa un veido kustības "
     "grafikus, aprēķina bremzēšanas ceļu.", PIEZ),
]

K11_T7B = [
    ("Inerce un Ņūtona I likums", "Kāpēc pasažieri paliecas uz priekšu?",
     "Skaidro inerci un masu kā inerces mēru; ar piemēriem pamato pirmo "
     "Ņūtona likumu."),
    ("Ņūtona II likums", "Kā spēks maina kustību?",
     "Lieto a = F/m; risina uzdevumus par spēka, masas un paātrinājuma "
     "saistību."),
    ("Ņūtona III likums un reaktīvā kustība", "Kāpēc raķete lido?",
     "Skaidro spēku pārus; ar impulsa p = mυ nezūdamību pamato reaktīvo "
     "kustību."),
    ("Gravitācijas spēks", "Kas notur planētas orbītā?",
     "Lieto F = Gm₁m₂/R² un F = mg; salīdzina ķermeņa svaru uz dažādām "
     "planētām."),
    ("Elastības un berzes spēks", "Kāpēc kāpnes neslīd?",
     "Lieto Fe = −kΔx; salīdzina berzes veidus un pamato to nozīmi tehnikā."),
    ("Spiediens", "Kāpēc slēpes nesagrimst sniegā?",
     "Lieto p = F/S; pamato virsmas laukuma nozīmi sadzīves un tehnikas "
     "piemēros."),
    ("Spēka moments", "Kā ietaupīt spēku?",
     "Lieto M = Fl; nosaka sviras līdzsvara nosacījumu un veic aprēķinu."),
    ("Vienkāršie mehānismi", "Vai mehānisms dod enerģijas ieguvumu?",
     "Salīdzina sviru, bloku un slīpo plakni; pamato, ka mehānisms ietaupa "
     "spēku, nevis darbu."),
    ("Spēku shēmas un nostiprināšana", "Kā attēlot uz ķermeni darbojošos spēkus?",
     "Zīmē spēku shēmu; risina kombinētu uzdevumu par spēku un "
     "paātrinājumu, labo tipiskās kļūdas."),
    ("PD", "PD2", "Spēki un ķermeņu mijiedarbība (dinamika)",
     "Zīmē spēku shēmu, lieto Ņūtona likumus, spiediena un spēka momenta "
     "sakarības.", PIEZ),
]

K11_T8 = [
    ("Blīvums un maisījumi", "Kāpēc eļļa peld virs ūdens?",
     "Lieto ρ = m/V; salīdzina vielu blīvumus un skaidro šķidrumu "
     "slāņošanos."),
    ("Spiediens šķidrumā", "Kāpēc dziļumā spiež stiprāk?",
     "Skaidro hidrostatisko spiedienu; aprēķina spiedienu dotā dziļumā."),
    ("Paskāla likums", "Kā darbojas hidrauliskā prese?",
     "Skaidro spiediena pārnesi šķidrumā; aprēķina spēka ieguvumu "
     "hidrauliskā sistēmā."),
    ("Arhimēda spēks", "Kāpēc kuģis peld?",
     "Nosaka cēlējspēku; pamato peldēšanas, grimšanas un lidināšanās "
     "nosacījumus."),
    ("Virsmas spraigums un kapilaritāte", "Kāpēc ūdens veido pilienus?",
     "Skaidro virsmas spraigumu, slapināšanu un kapilaritāti ar piemēriem "
     "dabā un tehnikā."),
    ("Šķidrumu plūsma", "Kāpēc šaurā vietā ūdens plūst ātrāk?",
     "Skaidro plūsmas nepārtrauktību; salīdzina lamināru un turbulentu "
     "plūsmu."),
    ("Uzdevumi par šķidrumiem", "Kā apvienot blīvumu, spiedienu un cēlējspēku?",
     "Risina kombinētu uzdevumu; pārbauda mērvienības un rezultāta "
     "ticamību."),
]

K11_T9 = [
    ("Troksnis un skaņa", "Kad skaņa kļūst bīstama?",
     "Raksturo skaņas skaļumu decibelos; izvērtē trokšņa ietekmi uz "
     "veselību un aizsardzības iespējas."),
    ("Apgaismojums un redze", "Kas nosaka labu darba vietas apgaismojumu?",
     "Skaidro apgaismojuma atkarību no attāluma; izvērtē konkrētas darba "
     "vietas apgaismojumu."),
    ("Ultravioletais starojums", "Kāpēc vajadzīgs saules aizsargkrēms?",
     "Salīdzina UV starojuma ietekmi uz ādu un acīm; pamato aizsardzības "
     "līdzekļu izvēli."),
    ("Elektromagnētiskais starojums vidē", "Vai mobilais tālrunis ir bīstams?",
     "Nošķir jonizējošu un nejonizējošu starojumu; izvērtē informācijas "
     "avota ticamību un apgalvojuma pierādījumus."),
]

K11_NOSL_PD = [
    ("Nostiprināšana", "Kā fizika skaidro vidi ap mums?",
     "Sasaista blīvumu, spiedienu, cēlējspēku un vides fizikālos faktorus; "
     "gatavojas pārbaudes darbam."),
    ("PD", "PD3", "Šķidrumi un vides fizikālie faktori",
     "Lieto blīvuma, spiediena un cēlējspēka sakarības; izvērtē vides "
     "fizikālo faktoru ietekmi uz cilvēku.", PIEZ),
]

K11_NOSL = [
    ("Kustība, spēki un vide", "Kā gada laikā apgūtais saistās kopā?",
     "Izvēlas atbilstošu sakarību praktiskā situācijā un pamato risinājumu "
     "ar aprēķinu."),
    ("Gada refleksija", "Ko esmu iemācījies un kas jāpilnveido?",
     "Izvērtē savu sniegumu, atpazīst biežākās kļūdas un plāno nākamā gada "
     "mācīšanos."),
]

# ------------------------------------------------------------------ 12. KLASE
K12_T11 = [
    ("Debess sfēra un zvaigznāji", "Kāpēc zvaigznes pārvietojas pa debesīm?",
     "Lieto grozāmo zvaigžņu karti; skaidro diennakts un gada kustību, "
     "ekliptiku un zvaigžņlielumu."),
    ("Zemes kustības un gadalaiki", "Kāpēc ir gadalaiki?",
     "Saista Zemes rotāciju un riņķošanu ap Sauli ar diennakti, kalendāru "
     "un Saules staru slīpumu."),
    ("Saules sistēma", "Kas ir Saules sistēmā?",
     "Grupē Saules sistēmas objektus; salīdzina fizikālos apstākļus uz "
     "planētām un to pavadoņiem."),
    ("Gravitācija un kosmiskie ātrumi", "Kas notur pavadoni orbītā?",
     "Lieto F = Gm₁m₂/R²; salīdzina pirmo, otro un trešo kosmisko ātrumu "
     "un to nozīmi."),
    ("Attālumi Visumā", "Kā izmērīt attālumu līdz zvaigznei?",
     "Rēķina ar astronomisko vienību, gaismas gadu un parseku; pamato "
     "mērvienības izvēli objektam."),
    ("Zvaigznes un to raksturlielumi", "Kāpēc zvaigznes ir dažādās krāsās?",
     "Saista zvaigznes krāsu ar virsmas temperatūru; nosaka Saules "
     "raksturlielumus Hercšprunga–Rasela diagrammā."),
    ("Galaktikas un Visuma struktūra", "Kā ir uzbūvēts Visums?",
     "Sakārto Visuma struktūrelementus pēc izmēra; salīdzina galaktiku "
     "tipus pēc to izskata."),
    ("Visuma pētniecība", "Kā pēta to, kurp nevar aizlidot?",
     "Salīdzina optiskos un radioteleskopus un kosmiskās zondes; raksturo "
     "Irbenes radioteleskopa nozīmi; pamato, kāpēc izpētīta ir tikai daļa "
     "no Visuma."),
    ("Citplanētas un dzīvība Visumā", "Vai Visumā ir dzīvība?",
     "Nosauc dzīvībai nepieciešamos faktorus; izvērtē apgalvojumu par "
     "citplanētām un tā pierādījumus."),
    ("PD", "PD1", "Visuma uzbūve un pētniecība",
     "Orientējas Visuma struktūrā, rēķina ar astronomiskiem attālumiem un "
     "izvērtē Visuma pētīšanas metodes.", PIEZ),
]

K12_T13 = [
    ("Svārstības", "Kas ir periods, frekvence un amplitūda?",
     "Lieto f = 1/T; raksturo svārstību amplitūdu, periodu un frekvenci ar "
     "piemēriem dabā un tehnikā."),
    ("Mehāniskie viļņi", "Kas pārvietojas vilnī?",
     "Atšķir garenviļņus un šķērsviļņus; lieto λ = υT un skaidro, ka vilnī "
     "pārvietojas enerģija, nevis viela."),
    ("Skaņa", "No kā atkarīgs skaņas augstums un skaļums?",
     "Saista frekvenci ar skaņas augstumu un amplitūdu ar skaļumu; "
     "aprēķina skaņas viļņa garumu dotā vidē."),
    ("Atbalss, eholokācija, ultraskaņa un infraskaņa",
     "Kā ar skaņu izmērīt attālumu un ieraudzīt neredzamo?",
     "Aprēķina attālumu pēc atbalss vai atstarotā ultraskaņas signāla laika; "
     "skaidro ultrasonogrāfijas, eholokācijas un seismoloģiskā monitoringa "
     "pamatideju."),
    ("Elektromagnētiskie viļņi", "Kā signāls ceļo bez vada?",
     "Skaidro elektromagnētiskā viļņa rašanos; lieto λ = c/f, kur "
     "c = 3,00·10⁸ m/s."),
    ("Elektromagnētisko viļņu skala", "Kas kopīgs radioviļņiem un rentgenam?",
     "Sakārto elektromagnētisko viļņu skalu pēc frekvences; nošķir "
     "jonizējošu un nejonizējošu starojumu."),
    ("Viļņu īpašības", "Kāpēc viļņi liecas ap šķērsli?",
     "Salīdzina atstarošanos, laušanu, interferenci un difrakciju "
     "garenviļņiem un šķērsviļņiem."),
    ("Viļņi tehnoloģijās un veselībā",
     "Kur viļņi noder un kuri viļņi ir bīstami?",
     "Raksturo elektromagnētisko viļņu lietojumus (GPS, lāzers, "
     "mikroviļņi); salīdzina ultravioletā, rentgena un gamma starojuma "
     "ietekmi un pamato aizsardzības pasākumus."),
    ("PD", "PD2", "Viļņi dabā un tehnikā",
     "Lieto viļņu sakarības, orientējas elektromagnētisko viļņu skalā un "
     "izvērtē viļņu lietojumus un riskus.", PIEZ),
]

K12_T15 = [
    ("Darbs, enerģija, jauda", "Kas fizikā ir darbs?",
     "Lieto darba un jaudas sakarības; aprēķina ierīces veikto darbu un "
     "jaudu, pārbauda mērvienības."),
    ("Kinētiskā un potenciālā enerģija", "Kur enerģija “uzkrājas”?",
     "Lieto Ek = mυ²/2 un Ep = mgh; salīdzina enerģijas veidus konkrētā "
     "situācijā."),
    ("Enerģijas nezūdamība", "Kur enerģija pazūd?",
     "Ar enerģijas nezūdamības likumu skaidro pārvērtību virknes; analizē "
     "enerģijas zudumus ierīcē."),
    ("Lietderības koeficients", "Cik efektīva ir ierīce?",
     "Lieto η = Al/Ap; salīdzina ierīču efektivitāti un pamato izvēli ar "
     "aprēķinu."),
    ("Kurināmais un siltums", "Cik enerģijas dod malka un gāze?",
     "Aprēķina degšanā iegūto siltuma daudzumu; salīdzina kurināmā veidu "
     "priekšrocības un trūkumus apkurē."),
    ("Elektroenerģija mājsaimniecībā", "Cik maksā elektrība?",
     "Lieto P = IU; aprēķina patērēto elektroenerģiju un izmaksas pēc dotā "
     "tarifa; salīdzina energoefektivitātes klases."),
    ("Elektrodrošība", "Kā pasargā drošinātājs un zemējums?",
     "Skaidro pārslodzi un īsslēgumu; pamato rīcības soļus elektrotraumas "
     "gadījumā."),
    ("Ģenerators, elektrodzinējs, transformators",
     "Kā elektrība nonāk no elektrostacijas mājā?",
     "Skaidro ierīču darbību; lieto k = N₁/N₂ = U₁/U₂ un pamato augsta "
     "sprieguma izmantošanu pārvadē."),
    ("PD", "PD3", "Enerģija dabā un tehnikā",
     "Lieto enerģijas, jaudas un lietderības sakarības, aprēķina "
     "elektroenerģijas patēriņu un pamato ilgtspējīgu izvēli.", PIEZ),
]

K12_EKS = [
    ("Ilgtspējīga enerģijas ieguve", "Kā ražot elektrību ilgtspējīgi?",
     "Salīdzina elektrostaciju veidus Latvijā; izvērtē atjaunojamo un "
     "neatjaunojamo enerģijas avotu ietekmi uz vidi. (10.14. temats)"),
    ("Mijiedarbības mikro-, makro- un megapasaulē",
     "Kuri spēki valda katrā pasaulē?",
     "Salīdzina gravitācijas, elektromagnētisko un kodolmijiedarbību "
     "dominanci dažādos mērogos. (10.16. temats)"),
    ("Gatavošanās eksāmenam: aprēķini un datu buklets",
     "Kā ātri atrast un pareizi lietot vajadzīgo formulu?",
     "Izvēlas datu bukletā atbilstošu formulu, pārveido mērvienības un "
     "noformē risinājumu: Dots — Jāaprēķina — Formulas — Aprēķins — Atbilde."),
]

# ================================================================== BŪVĒŠANA
IZV10_1 = ("Mērījumu kļūdu izvērsta apstrāde; patstāvīgs novērojums ar "
           "teleskopu vai binokli.")
IZV10_3 = ("Kodolreakciju vienādojumu izvērsti uzdevumi; pussabrukšanas "
           "aprēķini ar nepilniem periodiem.")
IZV10_5 = ("Kompozītmateriāla izgatavošana un tā īpašību pētīšana; "
           "materiālu pārstrādes enerģijas patēriņa salīdzinājums.")
IZV11_7 = ("Kustība pa slīpu plakni; vektoriāla spēku summēšana; "
           "izvērsti impulsa nezūdamības uzdevumi.")
IZV11_8 = ("Bernulli likuma kvalitatīvi piemēri; ūdenstilpes fizikāli "
           "ķīmiskās kvalitātes pētījums.")
IZV12_11 = ("Zvaigžņu spektru analīze; novērojumi observatorijā vai ar "
            "virtuālo planetāriju Stellarium.")
IZV12_13 = ("Difrakcijas režģa aprēķini; svārstību kontūra izvērsts "
            "apskats.")
IZV12_15 = ("Termodinamikas pirmā likuma piemēri; siltumsūkņa un biomasas "
            "kā alternatīvu avotu izvērtējums.")


def build_10(path):
    p = Plans()
    t1 = p.bloks(K10_T1)
    t3 = p.bloks(K10_T3)
    t5 = p.bloks(K10_T5)
    nos = p.bloks(K10_NOSL)

    doc = new_doc("10. klase", p.n)
    kalendars(doc, p.pd)
    temata_tabula(doc, "10.1. Pasaule ap mums un tās pētīšana (%d stundas)"
                  % len(t1),
                  "Fizikas daļa: matērija, mērogs, fizikālie lielumi un "
                  "mērierīces. Pamats visiem turpmākajiem aprēķiniem.",
                  t1, IZV10_1)
    nav_fizikas(doc, "10.2. Neredzamā dzīvā pasaule",
                "bioloģijas skolotājs")
    temata_tabula(doc, "10.3. Atoma uzbūve, vielas uzbūve, vielas stāvokļi "
                  "(%d stundas)" % len(t3),
                  "Fizikas daļa: atoma un kodola uzbūve, izotopi, "
                  "radioaktivitāte, vielas daļiņveida uzbūve un kristālrežģi. "
                  "Ķīmiskās saites un REN apgūst ķīmijas stundās.",
                  t3, IZV10_3)
    nav_fizikas(doc, "10.4. Organiskās vielas, to īpašības",
                "ķīmijas skolotājs")
    temata_tabula(doc, "10.5. Materiālu veidi un īpašības (%d stundas)"
                  % len(t5),
                  "Fizikas daļa: materiālu fizikālās īpašības un to saistība "
                  "ar uzbūvi. Korozija un oksidēšanās–reducēšanās procesi — "
                  "ķīmijas stundās.",
                  t5, IZV10_5)
    temata_tabula(doc, "Gada noslēguma nostiprināšana (%d stundas)" % len(nos),
                  "Formatīvas stundas. Jauns summatīvs darbs nav paredzēts.",
                  nos)
    doc.save(path)
    return p


def build_11(path):
    p = Plans()
    t7a = p.bloks(K11_T7A)
    t7b = p.bloks(K11_T7B)
    t8 = p.bloks(K11_T8)
    t9 = p.bloks(K11_T9)
    npd = p.bloks(K11_NOSL_PD)
    nos = p.bloks(K11_NOSL)

    doc = new_doc("11. klase", p.n)
    kalendars(doc, p.pd)
    nav_fizikas(doc, "10.6. Ķīmisko procesu norise", "ķīmijas skolotājs")
    temata_tabula(doc, "10.7. Cietu ķermeņu kustība un mijiedarbība "
                  "(%d stundas)" % (len(t7a) + len(t7b)),
                  "Gada apjomīgākais fizikas temats. Dalīts divās daļās: "
                  "kustības apraksts (PD1) un spēki (PD2).",
                  t7a + t7b, IZV11_7)
    temata_tabula(doc, "10.8. Šķidrumi dabā un tehnikā (%d stundas)"
                  % len(t8),
                  "Fizikas daļa: blīvums, spiediens, cēlējspēks un šķidrumu "
                  "īpašības. Dispersās sistēmas un šķīdumu ķīmija — ķīmijas "
                  "stundās.",
                  t8, IZV11_8)
    temata_tabula(doc, "10.9. Vides faktoru ietekme uz cilvēka organismu "
                  "(%d stundas)" % (len(t9) + len(npd)),
                  "Fizikas daļa: vides fizikālie faktori — troksnis, "
                  "apgaismojums un starojums. Uzturs, fermenti un imunitāte — "
                  "bioloģijas un ķīmijas stundās.",
                  t9 + npd)
    nav_fizikas(doc, "10.10. Organismi un vide", "bioloģijas skolotājs")
    temata_tabula(doc, "Gada noslēguma nostiprināšana (%d stundas)" % len(nos),
                  "Formatīvas stundas. Jauns summatīvs darbs nav paredzēts.",
                  nos)
    doc.save(path)
    return p


def build_12(path):
    p = Plans()
    t11 = p.bloks(K12_T11)
    t13 = p.bloks(K12_T13)
    t15 = p.bloks(K12_T15)
    eks = p.bloks(K12_EKS)

    doc = new_doc("12. klase", p.n)
    para(doc, "Mācību mērķis — sagatavot skolēnu centralizētajam eksāmenam "
              "dabaszinībās (ap 10.05.2027.). Pēdējais pārbaudes darbs "
              "plānots 15.04.2027., pēc tā seko tikai formatīvas "
              "atkārtošanas stundas.",
         size=9, bold=True, color=NAVY, after=8)
    kalendars(doc, p.pd)
    temata_tabula(doc, "10.11. Visuma uzbūve un pētniecība (%d stundas)"
                  % len(t11),
                  "Pilnībā fizikas/astronomijas temats.", t11, IZV12_11)
    nav_fizikas(doc, "10.12. Iedzimtība un ģenētika", "bioloģijas skolotājs")
    temata_tabula(doc, "10.13. Viļņi dabā un tehnikā (%d stundas)"
                  % len(t13),
                  "Pilnībā fizikas temats. Cieši saistīts ar eksāmena "
                  "uzdevumiem par viļņiem un starojumu.", t13, IZV12_13)
    temata_tabula(doc, "10.14. un 10.15. Enerģija dabā un tehnikā; vides "
                  "tehnoloģijas (%d stundas)" % len(t15),
                  "Fizikas daļa: darbs, enerģija, jauda, elektroenerģija un "
                  "tās pārvade. Zaļā ķīmija un biorafinēšana — ķīmijas "
                  "stundās.", t15, IZV12_15)
    temata_tabula(doc, "Gatavošanās eksāmenam un 10.16. temats (%d stundas)"
                  % len(eks),
                  "Formatīvas stundas pēc pēdējā PD. Jauns summatīvs darbs "
                  "nav paredzēts.", eks)
    doc.save(path)
    return p


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    base = "C:/aphysics/Dabaszinibas"
    faili = [
        ("10. klase", os.path.join(base, "Dabaszinības 10. klase - tematu un PD plāns.docx"), build_10),
        ("11. klase", os.path.join(base, "Dabaszinības 11. klase - tematu un PD plāns.docx"), build_11),
        ("12. klase", os.path.join(base, "Dabaszinības 12. klase - tematu un PD plāns.docx"), build_12),
    ]
    for nosaukums, path, fn in faili:
        p = fn(path)
        print("%s: %d stundas, %d PD  ->  %s"
              % (nosaukums, p.n, len(p.pd), os.path.basename(path)))
        for kods, tema, datums, _ in p.pd:
            print("      %-5s %-46s %s" % (kods, tema, datums))
