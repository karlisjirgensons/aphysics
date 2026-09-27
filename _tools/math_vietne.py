# -*- coding: utf-8 -*-
"""Matemātikas sadaļas lapas: klases -> temati -> stundas.

Trīs līmeņi (rules_matematika.txt):
    Math/index.html              - deviņas klases;
    Math/<N>. klase/index.html   - klases temati; temats atveras uz
                                   pieskāriena, un zem tā ir stundu pogas,
                                   sagrupētas pa mikrotematiem.

Lapu karkass, stils un ceļu kodēšana nāk no site_index.py, tāpēc matemātikas
lapas izskatās tāpat kā pārējā vietne (DRY). Ko rādīt, zina plānu reģistrs
math_plani.py - stundu saraksts nav ierakstīts otrreiz (SRP).

Stunda kļūst par pogu tikai tad, kad tās HTML fails ir uzrakstīts; pārējās
redzamas kā pelēks uzraksts, lai sarakstā būtu viss gada plāns.
"""

import os

import analytics
import math_plani
import palette
import site_index
import valoda
from site_index import esc, href, plural

MAPE = "Math"
NOSAUKUMS = "Matemātika 1.-9. klasei"
KICKER = "matemātika · 1.-9. klase"

CSS = site_index.CSS + """
/* ---------- matemātikas stundu saraksts ---------- */
.mt{display:flex;align-items:baseline;gap:.5rem;flex-wrap:wrap;
    margin:.9rem 0 .5rem;font-family:var(--font-h);font-weight:600;
    color:var(--violet);font-size:clamp(.85rem,3.4vw,.98rem)}
.mt .cnt{color:var(--dim);font-weight:400;font-size:.85em}
li.gaida span.t{color:var(--dim)}
li.gaida .box{display:flex;gap:.5rem;padding:.7rem .8rem;background:var(--bg);
     border:1px dashed var(--line);border-radius:.75rem;
     font-size:clamp(.85rem,3.5vw,1rem)}
li.gaida .n{flex:none;color:var(--dim);font-weight:500}
li.pd a,li.pd .box{background:#FFF4D6;border-color:var(--amber);
     color:var(--amber-ink);font-weight:500}
li.pd .n{color:var(--amber-ink)}
.tinfo{margin:.2rem 0 .6rem;color:var(--dim);
       font-size:clamp(.8rem,3.2vw,.9rem)}
"""


def page(title, body):
    """Viens karkass visām matemātikas lapām."""
    return site_index.PAGE % {"title": esc(title), "css": CSS,
                              "js": site_index.JS, "body": body,
                              "root": palette.root_css(),
                              "fonts": palette.FONT_LINK,
                              "lang": valoda.tagad(),
                              "analytics": analytics.head()}


# ------------------------------------------------------------------- stundas
def stundas_cels(klase, stunda):
    """Stundas HTML fails attiecībā pret klases mapi."""
    return os.path.join(math_plani.stundas_mape(stunda),
                        math_plani.stundas_fails(stunda))


def gatava(klase, stunda):
    """Vai stundas lapa jau ir uzrakstīta."""
    return os.path.isfile(os.path.join(klases_mape(klase),
                                       stundas_cels(klase, stunda)))


def render_stunda(klase, stunda):
    klases = ["pd"] if stunda.pd else []
    iekss = ('<span class="n">%d.</span><span class="t">%s</span>'
             % (stunda.nr, esc(stunda.tema)))
    if gatava(klase, stunda):
        cels = href(*stundas_cels(klase, stunda).split(os.sep))
        return ('  <li%s><a href="%s">%s</a></li>'
                % (_cl(klases), cels, iekss))
    return ('  <li%s><span class="box">%s</span></li>'
            % (_cl(klases + ["gaida"]), iekss))


def _cl(klases):
    return ' class="%s"' % " ".join(klases) if klases else ""


def render_bloks(klase, bloks):
    stundas = "\n".join(render_stunda(klase, s) for s in bloks.stundas)
    return ('<h3 class="mt">%s<span class="cnt">%s</span></h3>\n'
            '<ul>\n%s\n</ul>' % (esc(bloks.nosaukums),
                                 valoda.skaits(len(bloks),
                                               ("stunda", "stundas", "stundu"),
                                               ("test", "tests")), stundas))


def render_temats(klase, temats):
    """Temata mikrotemati un to stundas.

    Noslēguma pārbaudes darbu te nerāda: tas paliek plānā un vērtēšanas
    kalendārā, bet nav lapa, ko skolēns atver. Tāpēc arī stundu skaits
    virsrakstā ir tikai mācību stundas, nevis len(temats), kurā PD ietilpst.
    """
    bloki = [render_bloks(klase, b) for b in temats.bloki]
    skaits = sum(len(b) for b in temats.bloki)
    return ('<details class="theme">\n'
            '<summary><span class="n">%s</span><span class="t">%s</span>'
            '<span class="c">%d</span></summary>\n'
            '<p class="tinfo">%s</p>\n%s\n</details>'
            % (esc(temats.kods), esc(temats.nosaukums), skaits,
               esc(temats.apraksts), "\n".join(bloki)))


def render_noslegums(klase):
    if not klase.noslegums:
        return ""
    bloki = "\n".join(render_bloks(klase, b) for b in klase.noslegums)
    stundas = sum(len(b) for b in klase.noslegums)
    return ('<details class="theme">\n'
            '<summary><span class="n">&#9873;</span>'
            '<span class="t">Mācību gada noslēgums</span>'
            '<span class="c">%d</span></summary>\n%s\n</details>'
            % (stundas, bloki))


# --------------------------------------------------------------------- lapas
def render_klase(klase, atpakal=("../index.html", "Klases"),
                 virsraksts=None, galva=None, valodas=""):
    """Klases (vai IQ) tematu lapa; «atpakal» - (saite, uzraksts).

    «virsraksts» - cilnes nosaukums, «galva» - lapas virsraksts; pēc
    noklusējuma abus saliek no klases nosaukuma. «valodas» - valodu
    pārslēgs galvā (site_index.render_valodas).
    """
    virsraksts = virsraksts or "%s · matemātika" % klase.nosaukums
    temati = [render_temats(klase, t) for t in klase.temati]
    return page(virsraksts,
                "\n".join([site_index.render_header(galva or klase.nosaukums,
                                                    valodas),
                           site_index.render_bar(*atpakal)]
                          + temati + [render_noslegums(klase)]))


def render_klases_karte(klase):
    return ('<a class="card" href="%s">\n'
            '<span class="card-t">%s</span>\n'
            '<span class="card-s">%s · %s</span>\n</a>'
            % (href("%s" % klase.nosaukums, "index.html"),
               esc(klase.nosaukums),
               plural(len(klase.temati), "temats", "temati", "tematu"),
               plural(klase.stundu_skaits, "stunda", "stundas", "stundu")))


def render_index(klases):
    kartes = "\n".join(render_klases_karte(k) for k in klases)
    return page(NOSAUKUMS,
                "\n".join([site_index.render_header(NOSAUKUMS),
                           site_index.render_bar("../index.html",
                                                 izverst=False),
                           '<div class="cards">\n%s\n</div>' % kartes]))


# ---------------------------------------------------------------- rakstīšana
def sakne():
    return os.path.join(math_plani.SAKNE, MAPE)


def klases_mape(klase):
    """Mape, kurā stāv klases lapas. Klase, kas dzīvo citur (IQ testi -
    arī en/IQ), to pasaka pati ar atribūtu «mape»."""
    return (getattr(klase, "mape", None)
            or os.path.join(sakne(), klase.nosaukums))


def build_klase(klase):
    mape = klases_mape(klase)
    if not os.path.isdir(mape):
        os.makedirs(mape)
    return site_index.write(os.path.join(mape, "index.html"),
                            render_klase(klase))


def build_index(klases):
    return site_index.write(os.path.join(sakne(), "index.html"),
                            render_index(klases))


def build_vietne():
    """Matemātikas sadaļa: klašu lapas un klašu saraksts."""
    klases = math_plani.klases()
    return [build_klase(k) for k in klases] + [build_index(klases)]


def render_card():
    """Matemātikas poga sākumlapā - blakus pārējiem kursiem."""
    klases = math_plani.klases()
    stundas = sum(k.stundu_skaits for k in klases)
    return site_index.render_karte(
        href(MAPE, "index.html"), "Matemātika", KICKER,
        "%s · %s" % (plural(len(klases), "klase", "klases", "klašu"),
                     plural(stundas, "stunda", "stundas", "stundu")))
