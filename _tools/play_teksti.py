# -*- coding: utf-8 -*-
"""Dienas izaicinājuma (play/) teikumi abās valodās - viena vieta (SRP).

Lapas (play_vietne.py) un JS (play_spele, play_rezultats, play_dalisana,
play_forma) ņem teikumus no šejienes, tāpēc tulkojums nedzīvo vairākās
vietās (DRY). {x} vietas aizpilda JS (PT.f) vai Python (teksts).
"""

import json

import valoda

TEKSTI = {
    "en": {
        "virsraksts": "Daily challenge",
        "rez_virsraksts": "Challenge result",
        "sakt": "Start daily challenge",
        "sakt_meta": "3 tasks · 20 seconds each · new every day",
        "vecaks": "I'm a parent (18 years or older)",
        "agri": "Get early access",
        "agri_kapec": ("We're building Calcubo: short daily math games that "
                       "show how your child is doing. Leave your email and "
                       "you'll be among the first to get access when it "
                       "opens."),
        "agri_vecakiem": "Are you a parent? Get early access",
        "epasts": "Your email",
        "pieteikties": "Get early access",
        "piekrisana": ("By signing up you confirm you are 18+ and agree to "
                       "receive emails about Calcubo. Unsubscribe anytime."),
        "paldies": "Thank you! We'll email you when early access opens.",
        "slikts_epasts": "Please check the email address.",
        "nesanaca": "Couldn't send. Please try again.",
        "uzdevums": "Task {n} of 3",
        "izlaist": "Skip",
        "laiks_beidzas": "Time's up!",
        "pareizi": "Correct!",
        "nepareizi": "Not quite",
        "izlaists": "Skipped",
        "precizitate": "Accuracy",
        "atrums": "Speed",
        "no_3": "{c} of 3 tasks",
        "pret_labako": "of a top player's pace",
        "atruma_skaidrojums": ("Top players solve a task in about {top} s. "
                               "Time per correct answer: {tavs} s."),
        "kopa_laiks": "Total time: {s} s",
        "pareiza_atbilde": "Answer: {a}",
        "slava_3": "Perfect score!",
        "slava_2": "Great job!",
        "slava_1": "Good start!",
        "slava_0": "Tomorrow is your day!",
        "slava_atri": "⚡ As fast as the top players!",
        "slava_veikli": "⚡ Super quick!",
        "dalities": "Send to my parent",
        "pieaugusais": "I'm 18 or older",
        "kopet": "Copy link",
        "nokopets": "Link copied!",
        "zina": ("I solved {c} of 3 tasks in today's Calcubo math challenge! "
                 "See my result:"),
        "zina_virsraksts": "My Calcubo daily challenge result",
        "izmeginat": "Try today's challenge",
        "slikta_saite": "This result link is broken.",
        # uzdevumu teikumi
        "aprekini": "Calculate",
        "atver_iekavas": "Open the brackets",
        "atrisini": "Solve",
        "no": "{p}% of {n}",
        "palielina": "{n} increased by {p}%",
        "cik_procenti": "{a} is what % of {b}?",
        "dala_no": "{d} of {n}",
        "laukums": "Rectangle {a} cm × {b} cm. Area?",
        "perimetrs": "Rectangle {a} cm × {b} cm. Perimeter?",
        "lenkis": "Triangle angles: {a}° and {b}°. Third angle?",
        "procentos": "Write as a percentage",
        "reiz": "×",
    },
    "lv": {
        "virsraksts": "Dienas izaicinājums",
        "rez_virsraksts": "Izaicinājuma rezultāts",
        "sakt": "Sākt dienas izaicinājumu",
        "sakt_meta": "3 uzdevumi · 20 sekundes katram · katru dienu jauni",
        "vecaks": "Esmu vecāks (18 gadus vecs vai vecāks)",
        "agri": "Saņem agrāko piekļuvi",
        "agri_kapec": ("Mēs veidojam Calcubo: īsas ikdienas matemātikas "
                       "spēles, kas parāda, kā bērnam veicas. Atstāj e-pastu, "
                       "un tu būsi starp pirmajiem, kas saņems piekļuvi."),
        "agri_vecakiem": "Esi vecāks? Saņem agrāko piekļuvi",
        "epasts": "Tavs e-pasts",
        "pieteikties": "Saņemt agrāko piekļuvi",
        "piekrisana": ("Piesakoties tu apliecini, ka tev ir 18+ gadi, un "
                       "piekrīti saņemt e-pastus par Calcubo. Atteikties var "
                       "jebkurā brīdī."),
        "paldies": "Paldies! Uzrakstīsim, kad agrā piekļuve būs atvērta.",
        "slikts_epasts": "Lūdzu, pārbaudi e-pasta adresi.",
        "nesanaca": "Neizdevās nosūtīt. Lūdzu, mēģini vēlreiz.",
        "uzdevums": "{n}. uzdevums no 3",
        "izlaist": "Izlaist",
        "laiks_beidzas": "Laiks beidzās!",
        "pareizi": "Pareizi!",
        "nepareizi": "Ne gluži",
        "izlaists": "Izlaists",
        "precizitate": "Precizitāte",
        "atrums": "Ātrums",
        "no_3": "{c} no 3 uzdevumiem",
        "pret_labako": "no labākā spēlētāja tempa",
        "atruma_skaidrojums": ("Labākie spēlētāji uzdevumu atrisina ~{top} s. "
                               "Laiks vienai pareizai atbildei: {tavs} s."),
        "kopa_laiks": "Kopējais laiks: {s} s",
        "pareiza_atbilde": "Atbilde: {a}",
        "slava_3": "Perfekts rezultāts!",
        "slava_2": "Lieliski!",
        "slava_1": "Labs sākums!",
        "slava_0": "Rīt būs tava diena!",
        "slava_atri": "⚡ Tikpat ātri kā labākie spēlētāji!",
        "slava_veikli": "⚡ Zibensātri!",
        "dalities": "Nosūtīt vecākiem",
        "pieaugusais": "Man ir 18+ gadi",
        "kopet": "Kopēt saiti",
        "nokopets": "Saite nokopēta!",
        "zina": ("Šodienas Calcubo matemātikas izaicinājumā atrisināju {c} "
                 "no 3 uzdevumiem! Mans rezultāts:"),
        "zina_virsraksts": "Mans Calcubo dienas izaicinājuma rezultāts",
        "izmeginat": "Izmēģināt šodienas izaicinājumu",
        "slikta_saite": "Šī rezultāta saite ir bojāta.",
        "aprekini": "Aprēķini",
        "atver_iekavas": "Atver iekavas",
        "atrisini": "Atrisini",
        "no": "{p}% no {n}",
        "palielina": "{n}, palielināts par {p}%",
        "cik_procenti": "Cik % no {b} ir {a}?",
        "dala_no": "{d} no {n}",
        "laukums": "Taisnstūris {a} cm × {b} cm. Laukums?",
        "perimetrs": "Taisnstūris {a} cm × {b} cm. Perimetrs?",
        "lenkis": "Trijstūra leņķi: {a}° un {b}°. Trešais leņķis?",
        "procentos": "Izsaki procentos",
        "reiz": "·",
    },
}


def teksts(atslega, **vietas):
    """Teikums tagadējā valodā (valoda.tagad()) ar aizpildītām {vietām}."""
    s = TEKSTI[valoda.tagad()][atslega]
    for k, v in vietas.items():
        s = s.replace("{%s}" % k, str(v))
    return s


# PT.T - tagadējās valodas teikumi; PT.f aizpilda {vietas}.
JS = """
var PT={T:/*TEKSTI*/,
  f:function(s,v){return s.replace(/\\{(\\w+)\\}/g,function(m,k){
    return k in v?v[k]:m;});}};
"""


def js():
    """PT objekts ar tagadējās valodas teikumiem (tikai tiem - lapa ir vienā
    valodā)."""
    return JS.replace("/*TEKSTI*/", json.dumps(TEKSTI[valoda.tagad()],
                                                ensure_ascii=False))
