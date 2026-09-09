# -*- coding: utf-8 -*-
"""Vietnes krāsu palete un tipogrāfija - viena vieta visam projektam.

Stils pārņemts no matematika projekta ("Calcubo"): indigo, violets un ciāns
gradientā, dzintara akcents, gaišs fons, apaļi stūri un mīkstas ēnas.

Šis modulis atbild tikai par vērtībām (SRP). Kas ar tām tiek uzzīmēts, ir
site_index.py (sākumlapa un stundu saraksti) un html_deck.py (prezentācijas)
ziņā - abi lieto vienus un tos pašus mainīgos, tāpēc krāsu maiņa šeit maina
visu vietni uzreiz (DRY).
"""

# Vērtības - CSS mainīgo nosaukums bez "--" priekšā.
TOKENS = {
    # virsmas
    "bg":        "#F7F8FC",
    "surface":   "#FFFFFF",
    "surface2":  "#F5F3FF",
    "line":      "#E5E7EB",
    # teksts
    "fg":        "#374151",
    "dim":       "#6B7280",
    # zīmola krāsas
    "primary":   "#4F46E5",
    "violet":    "#7C3AED",
    "cyan":      "#06B6D4",
    "amber":     "#F59E0B",
    # dzintars uz balta ir par gaišu tekstam - tekstam šis tumšākais tonis
    "amber-ink": "#B45309",
    # gradients galvenēm
    "grad": ("linear-gradient(135deg,#4F46E5 0%,#7C3AED 50%,#06B6D4 100%)"),
    # forma
    "r-sm":      ".5rem",
    "r":         "1rem",
    "r-pill":    "50rem",
    "sh":        "0 1px 3px rgba(0,0,0,.10),0 1px 2px rgba(0,0,0,.06)",
    "sh-md":     "0 4px 6px -1px rgba(0,0,0,.10),0 2px 4px -1px rgba(0,0,0,.06)",
    "sh-lg":     "0 10px 15px -3px rgba(79,70,229,.18)",
    # fonti - ja tīkla nav, paliek vietējie aiz komata
    "font":      '"Inter",Calibri,"Segoe UI",system-ui,sans-serif',
    "font-h":    '"Poppins","Inter",Calibri,"Segoe UI",system-ui,sans-serif',
}

# Fontus ņem no Google Fonts; bez interneta lapa strādā ar rezerves fontiem.
FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" '
             'crossorigin>\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2'
             '?family=Inter:wght@400;500;600&family=Poppins:wght@500;600'
             '&display=swap">\n')


def root_css():
    """Visi mainīgie vienā :root blokā - to ievieto katras lapas stilā."""
    return ":root{%s}" % ";".join("--%s:%s" % kv for kv in TOKENS.items())


# ------------------------------------------------- slaidu krāsu pārnešana
# Pamatteksts slaidā. Vienā vietā, jo to lieto arī kā noklusējumu, ar ko
# salīdzina, vai krāsu vispār vajag rakstīt HTML.
TEXT_DEFAULT = TOKENS["fg"]

# Prezentāciju .pptx failos ir sava vecā palete (tumši zils, zelts, pelēks).
# Šeit katrai vecajai krāsai pateikts, kas tai atbilst Calcubo paletē. Kas
# sarakstā nav, paliek kā ir - tā jauni toņi netiek negaidīti pārkrāsoti.
SLIDE_MAP = {
    "#1F3864": TOKENS["primary"],    # tumši zils virsraksts -> indigo
    "#2E75B6": TOKENS["violet"],     # vidēji zils akcents -> violets
    "#172B4D": "#312E81",            # tumšā josla -> dziļš indigo
    "#B38600": TOKENS["amber-ink"],  # zelts -> dzintars
    "#1A1A1A": TOKENS["fg"],         # melns teksts -> pamatteksts
    # Slaida palīgteksts ir mazāks nekā saskarnes teksts, tāpēc tumšāks
    # pelēks nekā --dim: uz gaišām kartītēm tas citādi kļūst pārāk blāvs.
    "#606060": "#4B5563",            # pelēks palīgteksts
    "#D0D0D0": TOKENS["line"],       # gaišs rāmis
    "#F5F5F5": TOKENS["bg"],         # pelēks panelis
    "#EAF2FB": TOKENS["surface2"],   # gaiši zils panelis -> violets tonis
    "#FFF6DF": "#FEF3C7",            # gaiši dzeltens panelis
    "#BDD7EE": "#C7D2FE",            # gaiši zils uz tumša fona
    "#9DC3E6": "#A5B4FC",
    "#B41E1E": "#B91C1C",            # brīdinājuma sarkanais (teksta tonis)
    "#FDEEEE": "#FEF2F2",
    "#1E6B3A": "#047857",            # zaļais
}

# Dažas krāsas kā laukuma fons prasa tumšāku toni nekā kā teksts, citādi
# titullapa kļūst par spilgtu plankumu.
FILL_MAP = {
    "#1F3864": "#3730A3",
    "#1A1A1A": "#312E81",
}


# Uz tumša laukuma (titullapa, šķirlapa) tumšs teksts pazustu, tāpēc katrai
# teksta krāsai ir arī gaišais dvīnis. Balts un jau gaišie toņi paliek.
ON_DARK = {
    TOKENS["fg"]:        "#EEF2FF",
    "#4B5563":           "#C7D2FE",
    TOKENS["primary"]:   "#A5B4FC",
    TOKENS["violet"]:    "#C4B5FD",
    TOKENS["amber-ink"]: "#FCD34D",
    "#B91C1C":           "#FCA5A5",
    "#047857":           "#6EE7B7",
}


def slide_color(value, role="text"):
    """Vecā slaida krāsa -> paletes krāsa. None un nezināmas krāsas paliek."""
    if not value:
        return value
    key = value.upper()
    if role == "fill" and key in FILL_MAP:
        return FILL_MAP[key]
    return SLIDE_MAP.get(key, value)


def on_dark(value):
    """Teksta krāsas gaišais variants - lietojams uz tumša laukuma."""
    return ON_DARK.get((value or "").upper(), value)
