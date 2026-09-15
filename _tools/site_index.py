# -*- coding: utf-8 -*-
"""Sākumlapa, kursu stundu saraksti un PD ģeneratora saraksts.

Viena atbildība vienai funkcijai (SRP):

    natural_key   - kārtošanas kārtula (1. < 3. < 11., 3.2. < 3.10.)
    scan_course   - mapes -> dati (temati un to stundas)
    render_*      - dati -> HTML
    build_*       - HTML -> fails

Stils, lapas karkass un ceļu kodēšana ir pa vienam eksemplāram un tos lieto
visas lapas (DRY), tāpēc sākumlapa, kursu saraksti un matemātikas tematu
saraksts izskatās vienādi. Ko rādīt, zina reģistri: kursus - courses.py,
matemātikas klases un tematus - mat_temati.py.

Lietošana:
    python site_index.py            # sākumlapa + visi saraksti
"""

import glob
import html
import os
import re
import sys
from urllib.parse import quote

import mat_temati
import palette
from courses import (COURSES, LESSONS_LEAD, RIKI, SITE_LEAD, SITE_ROOT,
                     SITE_TITLE, ordered)


# -------------------------------------------------------------------- palīgi
def esc(s):
    return html.escape(s, quote=False)


def href(*parts):
    """Ceļš saitei - katru posmu kodē atsevišķi, lai "/" paliek "/"."""
    return "/".join(quote(p) for p in parts)


def natural_key(name):
    """"11." pēc "3.", un "3.10." pēc "3.2." - ciparus salīdzina kā skaitļus."""
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r"(\d+)", name)]


def split_number(name):
    """("3.10.", "Vielas daudzums") vai (None, viss nosaukums)."""
    m = re.match(r"^(\d+(?:[.\-]+\d+)*\.?)\s+(.*)$", name)
    return (m.group(1), m.group(2)) if m else (None, name)


def plural(n, one, many, none):
    """Latviešu skaitļa forma: 1 temats, 2 temati, 0 tematu, 21 temats."""
    if n == 0:
        return "%d %s" % (n, none)
    if n % 10 == 1 and n % 100 != 11:
        return "%d %s" % (n, one)
    return "%d %s" % (n, many)


# --------------------------------------------------------------------- stils
CSS = """
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
     font-family:var(--font);line-height:1.6}
a{color:inherit;text-decoration:none}
.wrap{max-width:60rem;margin:0 auto;padding:0 1rem 3.5rem}

header{margin:0 -1rem;padding:2.2rem 1rem 1.8rem;background:var(--grad);
       color:#fff;border-radius:0 0 1.5rem 1.5rem}
h1{margin:0;color:#fff;font-family:var(--font-h);font-weight:600;
   font-size:clamp(1.35rem,5vw,2.1rem)}
.lead{margin:.45rem 0 0;color:rgba(255,255,255,.85);max-width:44rem;
      font-size:clamp(.85rem,3.4vw,1rem)}

.bar{display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;
     padding:.8rem 0;position:sticky;top:0;z-index:10;
     background:var(--bg);border-bottom:1px solid var(--line)}
.back{color:var(--dim);padding:.3rem 0;font-size:clamp(.85rem,3.4vw,.95rem)}
.back:hover{color:var(--primary)}
.spacer{flex:1}
.toggle{background:var(--primary);color:#fff;border:0;border-radius:var(--r-pill);
        padding:.5rem 1rem;cursor:pointer;font:inherit;font-weight:500;
        font-size:clamp(.8rem,3.2vw,.9rem);transition:background .15s}
.toggle:hover{background:var(--violet)}

.cards{display:grid;gap:.9rem;margin:1.6rem 0;
       grid-template-columns:repeat(auto-fit,minmax(18rem,1fr))}
.card{display:block;background:var(--surface);border:1px solid transparent;
      border-radius:var(--r);padding:1.3rem 1.2rem;box-shadow:var(--sh);
      transition:transform .15s,box-shadow .15s,border-color .15s}
.card:hover{transform:translateY(-3px);box-shadow:var(--sh-lg);
            border-color:var(--violet)}
.card-t{display:block;color:var(--primary);font-family:var(--font-h);
        font-weight:600;font-size:clamp(1.1rem,4.5vw,1.45rem)}
.card-s{display:block;margin-top:.3rem;color:var(--dim);
        font-size:clamp(.82rem,3.3vw,.95rem)}
.card-m{display:block;margin-top:.9rem;color:var(--amber-ink);font-weight:500;
        font-size:clamp(.75rem,3vw,.85rem)}

.theme{border-bottom:1px solid var(--line)}
.theme summary{display:flex;align-items:baseline;gap:.6rem;cursor:pointer;
               padding:.85rem .2rem;list-style:none;font-family:var(--font-h);
               font-weight:600;font-size:clamp(.95rem,3.8vw,1.15rem)}
.theme summary::-webkit-details-marker{display:none}
.theme summary:hover{color:var(--primary)}
.theme summary .n{flex:none;min-width:2.2rem;color:var(--primary)}
.theme summary .t{flex:1}
.theme summary .c{flex:none;color:var(--cyan);font-size:.8em;font-weight:500}
.theme summary::after{content:"";flex:none;width:.5rem;height:.5rem;
    margin-left:.2rem;transform:rotate(45deg);transition:transform .15s;
    border-right:2px solid var(--dim);border-bottom:2px solid var(--dim)}
.theme[open] summary{color:var(--primary)}
.theme[open] summary::after{transform:rotate(225deg);border-color:var(--primary)}

ul{list-style:none;margin:0;padding:0 0 1rem;display:grid;gap:.5rem;
   grid-template-columns:repeat(auto-fill,minmax(15rem,1fr))}
li a{display:flex;gap:.5rem;padding:.7rem .8rem;background:var(--surface);
     border:1px solid var(--line);border-radius:.75rem;box-shadow:var(--sh);
     font-size:clamp(.85rem,3.5vw,1rem);
     transition:background .15s,border-color .15s,transform .15s}
li a:hover{background:var(--surface2);border-color:var(--violet);
           transform:translateY(-1px)}
li a .n{flex:none;color:var(--primary);font-weight:500}

li.rik a{background:var(--surface2);border-style:dashed;
         border-color:var(--violet);color:var(--primary);font-weight:500}
li.rik a:hover{background:#EDE9FE}
li.rik .ico{flex:none}

/* Tematu rinda PD ģeneratorā: nosaukums pa kreisi, divas pogas pa labi. */
ul.temati{grid-template-columns:1fr}
li.tema{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;
        padding:.6rem .8rem;background:var(--surface);
        border:1px solid var(--line);border-radius:.75rem;box-shadow:var(--sh)}
li.tema .n{flex:none;color:var(--primary);font-weight:500}
li.tema .t{flex:1 1 12rem;font-size:clamp(.85rem,3.5vw,1rem)}
li.tema .pogas{flex:none;display:flex;gap:.4rem;flex-wrap:wrap}
li.tema .pogas a,li.tema .pogas span{display:block;padding:.35rem .8rem;
        border-radius:var(--r-pill);font-size:clamp(.75rem,3vw,.85rem);
        font-weight:500;white-space:nowrap}
li.tema .pogas a.poga{background:var(--primary);color:#fff;transition:background .15s}
li.tema .pogas a.poga:hover{background:var(--violet)}
li.tema .pogas span{background:var(--bg);color:var(--dim);
        border:1px dashed var(--line)}

@media (max-width:768px){
  ul{grid-template-columns:1fr}
  li.tema .pogas{flex:1 1 100%;}
  li.tema .pogas a,li.tema .pogas span{flex:1 1 auto;text-align:center}
}
"""

JS = """
(function(){
  var b=document.getElementById("all");
  if(!b){return;}
  b.addEventListener("click",function(){
    var d=document.getElementsByTagName("details"),
        open=b.getAttribute("data-open")!=="1",i;
    for(i=0;i<d.length;i++){d[i].open=open;}
    b.setAttribute("data-open",open?"1":"0");
    b.textContent=open?"Sakļaut visu":"Izvērst visu";
  });
})();
"""

PAGE = """<!DOCTYPE html>
<html lang="lv">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
%(fonts)s<style>%(root)s%(css)s</style>
</head>
<body>
<div class="wrap">
%(body)s
</div>
<script>%(js)s</script>
</body>
</html>
"""


def page(title, body):
    """Viens karkass visām lapām."""
    return PAGE % {"title": esc(title), "css": CSS, "js": JS,
                   "body": body, "root": palette.root_css(),
                   "fonts": palette.FONT_LINK}


# ---------------------------------------------------------------- nolasīšana
def lesson_label(stem):
    """Faila nosaukums bez ģeneratora sufiksa "_tt"."""
    return re.sub(r"_tt$", "", stem)


def scan_course(root):
    """Mape -> [(temats, [(saite, stunda), ...], [(saite, rīks), ...]), ...].

    Apakšmapes bez .html neparādās - tur ir tikai skolas materiāli. Rīku
    lapas (sk. courses.RIKI) nav stundas, tāpēc tās iet savā sarakstā un
    stundu skaitītājā neparādās.
    """
    themes = []
    for d in sorted(os.listdir(root), key=natural_key):
        folder = os.path.join(root, d)
        if not os.path.isdir(folder):
            continue
        files = [f for f in glob.glob(os.path.join(folder, "*.html"))
                 if os.path.basename(f).lower() != "index.html"]
        if not files:
            continue
        lessons, riki = [], []
        for f in sorted(files, key=lambda p: natural_key(os.path.basename(p))):
            name = os.path.basename(f)
            label = lesson_label(os.path.splitext(name)[0])
            if label in RIKI:
                riki.append((href(d, name), RIKI[label]))
            else:
                lessons.append((href(d, name), label))
        themes.append((d, lessons, riki))
    return themes


def course_stats(root):
    """(tematu skaits, stundu skaits) - sākumlapas pogām."""
    themes = scan_course(root)
    return len(themes), sum(len(ls) for _, ls, _ in themes)


# ---------------------------------------------------------------- attēlošana
def render_number(text):
    return '<span class="n">%s</span>' % esc(text) if text else ""


def render_header(title, lead):
    """Lapas galva; tukšs «lead» nozīmē, ka paskaidrojuma rindas nav."""
    rindas = ["<h1>%s</h1>" % esc(title)]
    if lead:
        rindas.append('<p class="lead">%s</p>' % esc(lead))
    return "<header>\n%s\n</header>" % "\n".join(rindas)


def render_lesson(link, label):
    num, name = split_number(label)
    return ('  <li><a href="%s">%s<span>%s</span></a></li>'
            % (link, render_number(num), esc(name)))


def render_rik(link, label):
    """Rīka poga temata beigās - izskatās citādi, lai nejauktu ar stundu."""
    return ('  <li class="rik"><a href="%s"><span class="ico">&#9851;</span>'
            '<span>%s</span></a></li>' % (link, esc(label)))


def render_theme(title, lessons, riki=()):
    num, name = split_number(title)
    items = "\n".join([render_lesson(link, t) for link, t in lessons]
                      + [render_rik(link, t) for link, t in riki])
    return ('<details class="theme">\n'
            '<summary>%s<span class="t">%s</span>'
            '<span class="c">%d</span></summary>\n'
            '<ul>\n%s\n</ul>\n</details>'
            % (render_number(num), esc(name), len(lessons), items))


def render_course(course, themes):
    """Viena kursa saraksts: temati atveras uz pieskāriena."""
    bar = ('<div class="bar">\n'
           '<a class="back" href="../index.html">&#8592; Sākums</a>\n'
           '<span class="spacer"></span>\n'
           '<button class="toggle" id="all" data-open="0" type="button">'
           'Izvērst visu</button>\n</div>')
    return page("%s · %s" % (course["title"], course["kicker"]),
                "\n".join([render_header(course["title"], LESSONS_LEAD), bar]
                          + [render_theme(t, ls, rk)
                             for t, ls, rk in themes]))


# ------------------------------------------------- PD ģeneratora saraksts
def render_tema(mape, kods, nosaukums):
    """Viena temata rinda: nosaukums un divas pogas.

    Ja tematam vēl nav uzrakstīts saturs (mat_temati.SATURS), pogas vietā ir
    pelēks uzraksts - saraksts rāda visu programmu, ne tikai gatavo.
    """
    gatavs = mat_temati.gatavs(kods)
    pogas = []
    # Abi darba veidi ir vienlīdz svarīgi, tāpēc abām pogām ir viens izskats.
    for veids, uzraksts in mat_temati.VEIDI:
        if gatavs:
            saite = href(mape, "%s.html" % mat_temati.fails(kods, veids))
            pogas.append('<a class="poga" href="%s">%s</a>'
                         % (saite, esc(uzraksts)))
        else:
            pogas.append("<span>%s</span>" % esc(uzraksts))
    return ('  <li class="tema"><span class="n">%s</span>'
            '<span class="t">%s</span>'
            '<span class="pogas">%s</span></li>'
            % (esc(kods), esc(nosaukums), "".join(pogas)))


def render_klase(nr, mape, temati):
    """Viena klase: uz pieskāriena atveras tās tematu saraksts."""
    rindas = "\n".join(render_tema(mape, k, n) for k, n in temati)
    gatavi = sum(1 for k, _ in temati if mat_temati.gatavs(k))
    return ('<details class="theme">\n'
            '<summary><span class="n">%d.</span><span class="t">klase</span>'
            '<span class="c">%d/%d</span></summary>\n'
            '<ul class="temati">\n%s\n</ul>\n</details>'
            % (nr, gatavi, len(temati), rindas))


def render_pd_index():
    """PD ģeneratora saraksts: klases, to temati un abu darbu pogas."""
    bar = ('<div class="bar">\n'
           '<a class="back" href="../index.html">&#8592; Sākums</a>\n'
           '<span class="spacer"></span>\n'
           '<button class="toggle" id="all" data-open="0" type="button">'
           'Izvērst visu</button>\n</div>')
    klases = [render_klase(nr, mape, temati)
              for nr, mape, temati in mat_temati.klases()]
    return page("%s · %s" % (mat_temati.POGA, mat_temati.NOSAUKUMS),
                "\n".join([render_header(mat_temati.NOSAUKUMS,
                                         mat_temati.LEAD), bar] + klases))


def render_pd_card():
    """PD ģeneratora poga sākumlapā - blakus kursu pogām."""
    temati = sum(len(t) for _, _, t in mat_temati.klases())
    return ('<a class="card" href="%s">\n'
            '<span class="card-t">%s</span>\n'
            '<span class="card-s">%s</span>\n'
            '<span class="card-m">%s · %s</span>\n</a>'
            % (href(mat_temati.MAPE, "index.html"), esc(mat_temati.POGA),
               esc(mat_temati.KICKER),
               plural(len(mat_temati.klases()), "klase", "klases", "klašu"),
               plural(temati, "temats", "temati", "tematu")))


def render_card(course, n_themes, n_lessons):
    return ('<a class="card" href="%s">\n'
            '<span class="card-t">%s</span>\n'
            '<span class="card-s">%s</span>\n'
            '<span class="card-m">%s · %s</span>\n</a>'
            % (href(os.path.basename(course["root"]), "index.html"),
               esc(course["label"]), esc(course["kicker"]),
               plural(n_themes, "temats", "temati", "tematu"),
               plural(n_lessons, "stunda", "stundas", "stundu")))


def render_home(cards):
    return page(SITE_TITLE,
                "\n".join([render_header(SITE_TITLE, SITE_LEAD),
                           '<div class="cards">\n%s\n</div>'
                           % "\n".join(cards)]))


# --------------------------------------------------------------- rakstīšana
def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def build_course_index(slug):
    """Uzbūvē viena kursa index.html un atgriež ceļu."""
    course = COURSES[slug]
    return write(os.path.join(course["root"], "index.html"),
                 render_course(course, scan_course(course["root"])))


def build_pd_index():
    """Uzbūvē PD ģeneratora sarakstu ar visām klasēm un tematiem."""
    return write(os.path.join(SITE_ROOT, mat_temati.MAPE, "index.html"),
                 render_pd_index())


def build_home():
    """Uzbūvē sākumlapu ar pogu uz katru kursu un uz PD ģeneratoru."""
    cards = [render_card(c, *course_stats(c["root"])) for _, c in ordered()]
    return write(os.path.join(SITE_ROOT, "index.html"),
                 render_home(cards + [render_pd_card()]))


def build_site():
    """Visa vietne: kursu saraksti, PD ģeneratora saraksts un sākumlapa."""
    return ([build_course_index(slug) for slug, _ in ordered()]
            + [build_pd_index(), build_home()])


def slug_for_root(root):
    """Mapes ceļš -> kursa atslēga."""
    want = os.path.normcase(os.path.abspath(root))
    for slug, course in COURSES.items():
        if os.path.normcase(os.path.abspath(course["root"])) == want:
            return slug
    raise KeyError(root)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for p in build_site():
        print("Saraksts:   %s" % p)
