# -*- coding: utf-8 -*-
"""«Cik labi zini bērna matemātiku» (smart/) teikumi abās valodās (SRP).

Uzdevumi ir smart_uzdevumi, jautājuma soļa teikumi - aptaujas_solis,
e-pasta formas teikumi - play_teksti (DRY). {n} - klase, {c} - pareizo
skaits, {a} - atbilde; tos aizpilda JS (PT.f).
"""

import json

import valoda

TEKSTI = {
    "en": {
        "virsraksts": "Your child's math",
        "ievads_v": "How well do you know your child's math?",
        "ievads": ("Pick your child's grade and solve 5 tasks they meet at "
                   "school. No timer, no pressure - just curiosity."),
        "klase_v": "Your child's grade",
        "klase": "Grade {n}",
        "meta": "5 questions · about 2 minutes",
        "pareizi_no": "{c} of 5 correct",
        "atbilde": "Answer: {a}",
        "tava": "Your answer: {a}",
        "augsts_v": "You really know your child's math!",
        "augsts": ("Grade {n} math holds no secrets from you. Your child is "
                   "lucky - when homework gets tricky, help is right at "
                   "home."),
        "videjs_v": "You know more than you think",
        "videjs": ("A couple of tasks were tricky - that's completely "
                   "normal. School math has changed since we learned it, "
                   "and you still did well."),
        "zems_v": "School math has changed - and that's okay",
        "zems": ("Many parents feel exactly this. Topics and methods are "
                 "different from when we were at school. You don't need to "
                 "know everything to help your child - being there matters "
                 "most."),
        "cta_v": "We're here for you and your child",
        "cta": ("We're building Calcubo to help parents like you: short "
                "daily math practice made for grade {n}, with clear "
                "explanations, so you can help without stress. Leave your "
                "email and we'll let you know when it's ready."),
        "cita_klase": "Try another grade",
    },
    "lv": {
        "virsraksts": "Bērna matemātika",
        "ievads_v": "Cik labi tu zini sava bērna matemātiku?",
        "ievads": ("Izvēlies bērna klasi un atrisini 5 uzdevumus, ar kuriem "
                   "bērns sastopas skolā. Bez taimera un bez spiediena - "
                   "tikai ziņkāre."),
        "klase_v": "Bērna klase",
        "klase": "{n}. klase",
        "meta": "5 jautājumi · apmēram 2 minūtes",
        "pareizi_no": "{c} no 5 pareizi",
        "atbilde": "Atbilde: {a}",
        "tava": "Tava atbilde: {a}",
        "augsts_v": "Tu tiešām pārzini bērna matemātiku!",
        "augsts": ("{n}. klases matemātika tev nav noslēpums. Bērnam "
                   "paveicies - kad mājasdarbs sagādā grūtības, palīdzība "
                   "ir turpat mājās."),
        "videjs_v": "Tu zini vairāk, nekā tev šķiet",
        "videjs": ("Pāris uzdevumi bija viltīgi - tas ir pilnīgi normāli. "
                   "Skolas matemātika ir mainījusies kopš mūsu skolas "
                   "laikiem, un tev tik un tā veicās labi."),
        "zems_v": "Skolas matemātika ir mainījusies - un tas ir labi",
        "zems": ("Tieši tā jūtas daudzi vecāki. Tēmas un metodes ir citas "
                 "nekā mūsu skolas laikā. Lai palīdzētu bērnam, nav jāzina "
                 "viss - vissvarīgākais ir būt blakus."),
        "cta_v": "Mēs esam šeit - tev un tavam bērnam",
        "cta": ("Mēs veidojam Calcubo, lai palīdzētu tādiem vecākiem kā tu: "
                "īsi ikdienas matemātikas uzdevumi tieši {n}. klasei ar "
                "skaidriem paskaidrojumiem, lai tu vari palīdzēt bez "
                "stresa. Atstāj e-pastu, un mēs tev pastāstīsim, kad tas "
                "būs gatavs."),
        "cita_klase": "Izmēģināt citu klasi",
    },
}


def teksts(atslega, **vietas):
    """Teikums tagadējā valodā ar aizpildītām {vietām}."""
    s = TEKSTI[valoda.tagad()][atslega]
    for k, v in vietas.items():
        s = s.replace("{%s}" % k, str(v))
    return s


def js():
    """ST - tagadējās valodas teikumi (lapa ir vienā valodā)."""
    return "var ST=%s;" % json.dumps(TEKSTI[valoda.tagad()],
                                     ensure_ascii=False)
