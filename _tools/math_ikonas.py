# -*- coding: utf-8 -*-
"""Zīmētie attēli matemātikas stundu lapām.

Attēli ir zīmēti ar SVG līnijām, nevis ņemti no emocijzīmju fonta: uz katras
ierīces tie izskatās vienādi, tie ir vienā krāsā ar tekstu un tos var
palielināt, cik vajag (tāpat kā saknes zīmi prezentācijās - sk. mathfmt.py).

Līdzās katram attēlam ir arī tā vārda trīs formas, jo latviski skaits maina
vārdu: 1 logs, 2 logi, 0 logu. Tāpēc stundas saturam pietiek nosaukt attēlu -
pareizo vārdu lapa atrod pati (DRY).

Šis modulis atbild tikai par zīmējumiem un vārdiem (SRP). Kur tos liek, zina
math_bloki.py; to pašu sarakstu lapas JavaScript daļa saņem ar js().
"""

import json

_SVG = '<svg viewBox="0 0 64 64" aria-hidden="true">%s</svg>'

# Zīmējuma daļas: "l" - līnija, "p" - aizpildīts laukums (sk. math_lapa.CSS).
_FORMAS = {
    "logs": '<rect class="l" x="10" y="8" width="44" height="48" rx="4"/>'
            '<path class="l" d="M32 8v48M10 32h44"/>',
    "durvis": '<rect class="l" x="16" y="6" width="32" height="52" rx="3"/>'
              '<circle class="p" cx="40" cy="34" r="3"/>',
    "kresls": '<path class="l" d="M22 10v46M22 16h12M22 36h26'
              'M46 36v20"/>',
    "galds": '<path class="l" d="M8 26h48M16 26v28M48 26v28"/>',
    "soma": '<rect class="l" x="10" y="24" width="44" height="32" rx="7"/>'
            '<path class="l" d="M22 24a10 10 0 0 1 20 0M18 42h28"/>',
    "zimulis": '<path class="l" d="M14 50l3-11L39 17l8 8-22 22z"/>'
               '<path class="l" d="M36 20l8 8"/>',
    "gramata": '<path class="l" d="M32 20v32M32 20c-6-4-14-4-22-2v32c8-2 16-2'
               ' 22 2 6-4 14-4 22-2V18c-8-2-16-2-22 2z"/>',
    "abols": '<circle class="l" cx="32" cy="38" r="17"/>'
             '<path class="l" d="M32 21v-7"/>'
             '<ellipse class="l" cx="41" cy="15" rx="7" ry="4"'
             ' transform="rotate(-25 41 15)"/>',
    "bumba": '<circle class="l" cx="32" cy="32" r="18"/>'
             '<path class="l" d="M14 32h36M32 14c7 6 7 30 0 36M32 14'
             'c-7 6-7 30 0 36"/>',
    "puke": '<circle class="l" cx="32" cy="16" r="8"/>'
            '<circle class="l" cx="46" cy="26" r="8"/>'
            '<circle class="l" cx="41" cy="42" r="8"/>'
            '<circle class="l" cx="23" cy="42" r="8"/>'
            '<circle class="l" cx="18" cy="26" r="8"/>'
            '<circle class="p" cx="32" cy="29" r="6"/>'
            '<path class="l" d="M32 50v10"/>',
    "karote": '<ellipse class="l" cx="32" cy="20" rx="9" ry="12"/>'
              '<path class="l" d="M32 32v26"/>',
    "ripina": '<circle class="p" cx="32" cy="32" r="16"/>',
    "klucis": '<rect class="l" x="10" y="26" width="44" height="28" rx="3"/>'
              '<rect class="l" x="16" y="15" width="11" height="11" rx="2"/>'
              '<rect class="l" x="37" y="15" width="11" height="11" rx="2"/>',
    "zvaigzne": '<path class="p" d="M32.0 11.0L37.9 26.9L54.8 27.6L41.5 38.1L46.1 54.4L32.0 45.0L17.9 54.4L22.5 38.1L9.2 27.6L26.1 26.9z"/>',
    "aplis": '<circle class="p" cx="32" cy="32" r="20"/>',
    "trijsturis": '<path class="p" d="M32 10L55 52H9z"/>',
    "kvadrats": '<rect class="p" x="12" y="12" width="40" height="40" rx="2"/>',
    "sirds": '<path class="p" d="M32 54C10 39 7 26 13 18c5-7 15-7 19 2'
             ' 4-9 14-9 19-2 6 8 3 21-19 36z"/>',
    "masina": '<path class="l" d="M7 42V31l9-11h22l11 11h8v11z"/>'
              '<circle class="l" cx="19" cy="45" r="6"/>'
              '<circle class="l" cx="45" cy="45" r="6"/>',
    "zivs": '<path class="l" d="M8 32c10-14 30-14 38 0-8 14-28 14-38 0z"/>'
            '<path class="l" d="M46 32l11-9v18z"/>'
            '<circle class="p" cx="19" cy="29" r="2.6"/>',
    "putns": '<path class="l" d="M8 34c8-10 16-10 24 0 8-10 16-10 24 0"/>',
}

# Vārda formas: (viens, vairāki, «cik?» - ģenitīvs).
VARDI = {
    "logs": ("logs", "logi", "logu"),
    "durvis": ("durvis", "durvis", "durvju"),
    "kresls": ("krēsls", "krēsli", "krēslu"),
    "galds": ("galds", "galdi", "galdu"),
    "soma": ("soma", "somas", "somu"),
    "zimulis": ("zīmulis", "zīmuļi", "zīmuļu"),
    "gramata": ("grāmata", "grāmatas", "grāmatu"),
    "abols": ("ābols", "āboli", "ābolu"),
    "bumba": ("bumba", "bumbas", "bumbu"),
    "puke": ("puķe", "puķes", "puķu"),
    "karote": ("karote", "karotes", "karošu"),
    "ripina": ("ripiņa", "ripiņas", "ripiņu"),
    "klucis": ("klucītis", "klucīši", "klucīšu"),
    "zvaigzne": ("zvaigzne", "zvaigznes", "zvaigžņu"),
    "aplis": ("aplis", "apļi", "apļu"),
    "trijsturis": ("trijstūris", "trijstūri", "trijstūru"),
    "kvadrats": ("kvadrāts", "kvadrāti", "kvadrātu"),
    "sirds": ("sirds", "sirdis", "siržu"),
    "masina": ("mašīna", "mašīnas", "mašīnu"),
    "zivs": ("zivs", "zivis", "zivju"),
    "putns": ("putns", "putni", "putnu"),
}

IKONAS = dict((v, _SVG % f) for v, f in _FORMAS.items())


def ir(vards):
    """Vai tāds zīmējums ir - saturu pārbauda jau būvējot."""
    return vards in IKONAS


def svg(vards):
    """Zīmējums kā HTML gabals; nezināms vārds ir kļūda, nevis tukšums."""
    if vards not in IKONAS:
        raise KeyError("nav zīmējuma «%s»; ir: %s"
                       % (vards, ", ".join(sorted(IKONAS))))
    return IKONAS[vards]


def ikona(vards):
    """Zīmējums, gatavs likšanai teksta rindā."""
    return '<span class="ik">%s</span>' % svg(vards)


def js():
    """Tie paši zīmējumi un vārdi lapas JavaScript daļai."""
    return ("window.MATH_IKONAS=%s;window.MATH_VARDI=%s;"
            % (json.dumps(IKONAS, ensure_ascii=False),
               json.dumps(VARDI, ensure_ascii=False)))
