# -*- coding: utf-8 -*-
"""Matemātikas darbu ģeneratora veidotājs - no satura uz vienu HTML lapu.

Katram programmas tematam ir divi darbi (rules_mat.txt):

    «fd»  formatīvais darbs      - viena lapa, 12 jautājumi ar atbildēm A-D;
    «pd»  summatīvais PD         - divas lapas, tests un uzdevumi ar darba
                                   vietu.

Abus uzbūvē šis modulis: pārbauda saturu un uzraksta lapu (SRP). Lapas
izskats ir mat_page.py, lapas saturs - fd_paper.py un mat_paper.py.

Saturs dzīvo mat_<klase>_<temats>.py failos (piemēram, mat_1_1.py), un tas ir
vienīgā vieta, kas jāraksta no jauna, pievienojot tematu; dzinējs paliek šis
(DRY). Augstumu mēra tie paši palīgi, ar ko mēra Word pārbaudes darbus
(pd_common.py, at_common.py), tāpēc uz papīra darbs ietilpst tur, kur solīts.

Lapa rāda vienu darbu, un poga «Ģenerēt» izlozē nākamo, tāpēc katrā
jautājumu grupā vajag vismaz dažus līdzvērtīgus jautājumus un katram
uzdevumam - vairākus variantus; cik dažādus darbus no tiem var salikt, saka
būvēšanas paziņojums.
"""

import os

import fd_common
import fd_stils
import mat_temati
import mat_varianti
import pd_common as C

REZERVE = 3        # cik jautājumu vismaz vienā grupā un variantu uzdevumā

VIRSRAKSTI = {
    "fd": "Formatīvais darbs",
    "pd": "Summatīvais pārbaudes darbs",
}

# Ievads ir vienāds visiem viena veida darbiem, tāpēc tas dzīvo te, nevis
# katrā satura failā (DRY); temats to var aizstāt ar savu.
IEVADI = {
    "fd": "Katram jautājumam ir viena pareizā atbilde. Apvelc pareizās "
          "atbildes burtu! Par pareizu atbildi — 1 punkts.",
    "pd": "Darba izpildes laiks — 40 minūtes. Kopā var iegūt 20 punktus. "
          "Aprēķinus pieraksti tam atvēlētajā vietā!",
}


# ----------------------------------------------------------------- palīgi
def ievads(saturs):
    """Darba ievads; ja temats savu nedod, der visiem kopīgais (DRY)."""
    return saturs.get("ievads") or IEVADI[saturs["veids"]]


def garakais(grupa):
    """Grupas jautājums, kas uz lapas aizņem visvairāk vietas."""
    return fd_common.garakais(grupa)


def smagakie(grupas):
    """No katras grupas garākais jautājums - vissmagākais iespējamais tests."""
    return [(fd_common.vienkarsi(t), [fd_common.vienkarsi(v) for v in vv], p)
            for t, vv, p in map(garakais, grupas)]


def smagakais_uzdevums(u):
    """Uzdevuma variants, kas aizņem visvairāk vietas."""
    return max(u["varianti"], key=C.h_uzdevums)


def kombinacijas(saturs):
    """Cik dažādus darbus no satura var izlozēt (neskaitot atbilžu kārtību)."""
    n = 1
    for g in (saturs["grupas"] if saturs["veids"] == "fd" else saturs["tests"]):
        n *= len(g["jautajumi"])
    for u in saturs.get("uzdevumi", []):
        n *= len(u["varianti"])
    return n


def kopa(pd):
    """Pārbaudes darba punktu summa: tests + uzdevumi."""
    return len(pd["tests"]) + sum(u["punkti"] for u in pd["uzdevumi"])


# -------------------------------------------------------------- pārbaude
def parbaudi_grupas(grupas, kur):
    """Jautājumu grupu uzbūve - tā ir vienāda abiem darba veidiem."""
    redzeti = set()
    for g in grupas:
        assert g.get("sr"), "%s: grupai trūkst «sr»" % kur
        assert len(g["jautajumi"]) >= REZERVE, \
            "%s: grupā «%s» ir tikai %d jautājumi — vajag vismaz %d, lai " \
            "izlozētie darbi atšķirtos" \
            % (kur, g["sr"][:40], len(g["jautajumi"]), REZERVE)
        for teksts, varianti, pareizais in g["jautajumi"]:
            assert len(varianti) == 4, \
                "%s: %s — vajag 4 atbilžu variantus" % (kur, teksts[:40])
            assert len(set(varianti)) == 4, \
                "%s: %s — atkārtojas atbilžu varianti" % (kur, teksts[:40])
            assert 0 <= pareizais < 4, \
                "%s: %s — nederīgs pareizās atbildes numurs" % (kur,
                                                                teksts[:40])
            assert teksts not in redzeti, \
                "%s: jautājums atkārtojas — %s" % (kur, teksts[:40])
            redzeti.add(teksts)


def parbaudi_fd(fd):
    """Formatīvais darbs: grupas, atbilžu tabula un viena lapa."""
    kur = apraksts(fd)
    grupas = fd["grupas"]
    assert grupas, "%s: nav neviena jautājumu grupas" % kur
    assert len(grupas) % fd_stils.AILES == 0, \
        "%s: grupu skaits (%d) nedalās ar %d — atbilžu tabula būs nepilna" \
        % (kur, len(grupas), fd_stils.AILES)
    parbaudi_grupas(grupas, kur)
    h = fd_common.augstums(dict(fd, ievads=ievads(fd)),
                           smagakie(grupas))
    assert h <= C.LAPAS_BUDZETS, \
        "%s: garākie jautājumi vienā lapā neietilpst — %.1f cm no %.1f cm" \
        % (kur, h, C.LAPAS_BUDZETS)
    return [h]


def augstumi_pd(pd):
    """Abu lapu augstums centimetros vissmagākajā variantā."""
    h_ievads = C.h_para(ievads(pd), 9.5, after=4)
    atgadne = 0.55 + len(pd["atgadne"]) * 0.42 + 0.45
    lapa = {1: C.H_GALVENE + h_ievads + 1.45 + atgadne
               + C.h_tests(smagakie(pd["tests"])),
            2: C.H_GALVENE + C.H_VERTEJUMS}
    for u in pd["uzdevumi"]:
        lapa[u["lapa"]] += C.h_uzdevums(smagakais_uzdevums(u))
    return [lapa[1], lapa[2]]


def parbaudi_pd(pd):
    """Pārbaudes darbs: tests, uzdevumi, punkti un divas lapas."""
    kur = apraksts(pd)
    assert len(pd["tests"]) == fd_stils.AILES, \
        "%s: testā vajag %d jautājumus — tik ir vienā atbilžu tabulas blokā" \
        % (kur, fd_stils.AILES)
    parbaudi_grupas(pd["tests"], kur)
    assert pd["uzdevumi"], "%s: nav neviena uzdevuma" % kur
    for i, u in enumerate(pd["uzdevumi"], start=2):
        assert u["lapa"] in (1, 2), \
            "%s: %d. uzdevumam «lapa» jābūt 1 vai 2" % (kur, i)
        assert u["punkti"] > 0, "%s: %d. uzdevumam nav punktu" % (kur, i)
        assert len(u["varianti"]) >= REZERVE, \
            "%s: %d. uzdevumam ir %d varianti — vajag vismaz %d" \
            % (kur, i, len(u["varianti"]), REZERVE)
        for v in u["varianti"]:
            assert v["tips"] in ("parveide", "aprekins", "jautajumi"), \
                "%s: %d. uzdevumā nezināms tips «%s»" % (kur, i, v["tips"])
            if v["tips"] == "parveide":
                assert len(v["rindas"]) == u["punkti"], \
                    "%s: %d. uzdevumā rindu skaits neatbilst punktiem" \
                    % (kur, i)
            elif v["tips"] == "jautajumi":
                assert sum(p for _, p in v["jaut"]) == u["punkti"], \
                    "%s: %d. uzdevumā jautājumu punkti nesakrīt ar %d p." \
                    % (kur, i, u["punkti"])
                assert len(v["atbildes"]) == len(v["jaut"]), \
                    "%s: %d. uzdevumam trūkst atbildes" % (kur, i)
            else:
                assert v.get("risinajums") or v.get("kriteriji"), \
                    "%s: %d. uzdevumam trūkst risinājuma" % (kur, i)
    h1, h2 = augstumi_pd(pd)
    for nr, h in ((1, h1), (2, h2)):
        assert h <= C.LAPAS_BUDZETS, \
            "%s: %d. lapa neietilpst — %.1f cm no %.1f cm" \
            % (kur, nr, h, C.LAPAS_BUDZETS)
    return [h1, h2]


PARBAUDES = {"fd": parbaudi_fd, "pd": parbaudi_pd}


# ---------------------------------------------------------------- saturs
def apraksts(saturs):
    """Īss darba apzīmējums kļūdu paziņojumiem."""
    return "%d. klases %s %s" % (saturs["klase"], saturs["temats"],
                                 VIRSRAKSTI[saturs["veids"]])


def fails(saturs):
    """Lejupielādētā Word faila nosaukums."""
    return "Matemātika %d. klase %s %s" % (
        saturs["klase"], saturs["temats"],
        dict(mat_temati.VEIDI)[saturs["veids"]])


def kopigie(saturs, punkti):
    """Lauki, kas abiem darba veidiem ir vienādi."""
    return {
        "veids": saturs["veids"],
        "virsraksts": VIRSRAKSTI[saturs["veids"]],
        "nr": saturs["nr"],
        "nosaukums": saturs["nosaukums"],
        "prieksmets": saturs["prieksmets"],
        # Matemātikas darbus lieto arī citās skolās, tāpēc galvenē skolas
        # nosaukuma nav - tikai priekšmets, klase un mācību gads.
        "skola": "",
        "kicker": saturs["kicker"],
        "laiks": saturs["laiks"],
        "apraksts": saturs["apraksts"],
        "ievads": ievads(saturs),
        "atgadne": list(saturs["atgadne"]),
        "fails": fails(saturs),
        # Matemātikā sasniedzamais rezultāts pieder tematam, nevis vienai
        # stundai, tāpēc atbilžu lapas tabulas trešā aile ir «Temats».
        "aile": ["Jaut.", "Pārbaudāmais sasniedzamais rezultāts", "Temats"],
        "kopa": punkti,
        "skala": [list(r) for r in C.skala(punkti)],
    }


def grupas_dati(grupas):
    return [{"sr": g["sr"], "stunda": g.get("stunda", ""),
             "jautajumi": [[t, list(v), p] for t, v, p in g["jautajumi"]]}
            for g in grupas]


def dati(saturs):
    """Saturs tādā veidā, kā to lasa lapa."""
    if saturs["veids"] == "fd":
        out = kopigie(saturs, len(saturs["grupas"]))
        out["grupas"] = grupas_dati(saturs["grupas"])
        return out
    out = kopigie(saturs, kopa(saturs))
    out["tests"] = grupas_dati(saturs["tests"])
    out["uzdevumi"] = [{"sr": u["sr"], "stunda": u.get("stunda", ""),
                        "punkti": u["punkti"], "lapa": u["lapa"],
                        "varianti": u["varianti"]}
                       for u in saturs["uzdevumi"]]
    return out


# ----------------------------------------------------------- rakstīšana
def mape(saturs):
    """Klases mape vietnē; ja tās vēl nav, to izveido."""
    ce = os.path.join(C.SAKNE, mat_temati.MAPE,
                      mat_temati.mape(saturs["klase"]))
    if not os.path.isdir(ce):
        os.makedirs(ce)
    return ce


def build(saturs):
    """Uzbūvē viena darba ģeneratora lapu un atgriež ceļu."""
    import mat_page                       # tikai būvējot, nevis pārbaudot
    augstumi = PARBAUDES[saturs["veids"]](saturs)
    path = os.path.join(mape(saturs),
                        "%s.html" % mat_temati.fails(saturs["temats"],
                                                     saturs["veids"]))
    with open(path, "w", encoding="utf-8") as f:
        f.write(mat_page.page(dati(saturs)))
    print("Izveidots: %s\n           %s, %s dažādi darbi; %s"
          % (os.path.relpath(path, C.SAKNE), kopsavilkums(saturs),
             "{:,}".format(kombinacijas(saturs)).replace(",", " "),
             " un ".join("%d. lapa %.1f cm" % (i + 1, h)
                         for i, h in enumerate(augstumi))))
    return path


def sausakais(saturs):
    """Cik jautājumu ir visnabadzīgākajā grupā (un variantu uzdevumā).

    Tieši šis skaitlis nosaka, cik ātri izlozētie darbi sāk atkārtoties, tāpēc
    to rāda būvējot: ja tas ir mazāks nekā mat_varianti.MERKIS, tematam vēl
    vajag jautājumus.
    """
    grupas = saturs["grupas"] if saturs["veids"] == "fd" else saturs["tests"]
    return min([len(g["jautajumi"]) for g in grupas]
               + [len(u["varianti"]) for u in saturs.get("uzdevumi", [])])


def kopsavilkums(saturs):
    """Cik jautājumu un punktu darbā - būvēšanas paziņojumam."""
    n = sausakais(saturs)
    truka = "" if n >= mat_varianti.MERKIS else " — mazākajā grupā tikai %d" % n
    if saturs["veids"] == "fd":
        g = len(saturs["grupas"])
        return "%d jautājumi (%d rezervē), %d punkti%s" % (
            g, sum(len(x["jautajumi"]) for x in saturs["grupas"]) - g, g,
            truka)
    return "tests %d jaut. + %d uzdevumi, kopā %d punkti%s" % (
        len(saturs["tests"]), len(saturs["uzdevumi"]), kopa(saturs), truka)
