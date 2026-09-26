# -*- coding: utf-8 -*-
"""Stundu pavedieni - viens dzīves temats, kas iet cauri vairākām stundām.

Ja katrā stundā reālās dzīves uzdevums ir par ko citu, tas paliek atsevišķs
piemērs un aizmirstas. Ja turpretī viena mikrotemata stundas rēķina par vienu
un to pašu lietu - par datoru atmiņu, par ceļojumu vai par veikalu -, tad
katra nākamā stunda paskaidro iepriekšējo, un skolēns redz, ka matemātika ir
par vienu pasauli, nevis par sadalītiem uzdevumiem.

Pavediena nosaukums ir uzrakstīts te vienu reizi (DRY), un stunda uz to
atsaucas ar atslēgu:

    Pasaule("Cik ilgi krājas 1 GB?", pavediens="dati", kartas=[...])

Jaunu pavedienu pievieno ar vienu rindu šajā sarakstā. Atslēga, kas nav
sarakstā, ir kļūda - tā pamana pārrakstīšanās.
"""

# atslēga: (nosaukums, ar ko tas nodarbojas)
PAVEDIENI = {
    "dati": ("Dators un dati",
             "cik vietas aizņem faili, attēli un video"),
    "kosmoss": ("Kosmoss un attālumi",
                "planētas, gaismas ātrums un lieli attālumi"),
    "veikals": ("Veikals un nauda",
                "cenas, atlaides, čeki un budžets"),
    "sports": ("Sports un rezultāti",
               "laiki, distances, rezultātu tabulas"),
    "daba": ("Daba un dzīvnieki",
             "augšana, sugu skaits, attālumi dabā"),
    "celojums": ("Ceļojums",
                 "attālumi, ātrums, laiks un degviela"),
    "skola": ("Mūsu skola",
              "skolēnu skaits, stundas, ēdnīca un telpas"),
    "maja": ("Māja un remonts",
             "laukumi, materiāli, rēķini un patēriņš"),
    "tehnika": ("Tehnika un izgudrojumi",
                "raķetes, roboti, dzinēji un to izmēri"),
    "virtuve": ("Virtuve un receptes",
                "sastāvdaļas, proporcijas un porciju skaits"),
    "planeta": ("Planēta un klimats",
                "temperatūra, ledus, ūdens un gaiss"),
    "speles": ("Spēles un nejaušība",
               "kauliņi, kārtis, loterijas un izredzes"),
    "kodi": ("Kodi un drošība",
             "PIN kodi, paroles, šifri un pārbaudes"),
}


def ir(atslega):
    return atslega in PAVEDIENI


def nosaukums(atslega):
    """Pavediena nosaukums; nezināma atslēga ir kļūda, nevis tukšums."""
    if atslega not in PAVEDIENI:
        raise KeyError("nav pavediena «%s»; ir: %s"
                       % (atslega, ", ".join(sorted(PAVEDIENI))))
    return PAVEDIENI[atslega][0]


def apraksts(atslega):
    return PAVEDIENI[atslega][1]
