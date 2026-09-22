# -*- coding: utf-8 -*-
"""Pārbaudes darba stundas lapa - uzbūvēta no plāna, nevis rakstīta ar roku.

Katrs temats noslēdzas ar vienu pārbaudes darbu (rules_matematika.txt). Ko tur
vērtē, jau ir pateikts plānā: temata pārbaudes darba sasniedzamais rezultāts,
mikrotemati un to stundas. Tāpēc šo lapu neraksta atsevišķi katram tematam -
to saliek no tā paša plāna, no kā aug stundu saraksts (DRY), un deviņām
klasēm sanāk septiņdesmit divas lapas bez viena satura faila.

Lapa nav pats darbs - tā ir pēdējā atkārtošanās pirms tā: ko vērtēs, ko
atkārtot un ar ko sākt, ja laika atlicis maz.

Uzdevumus darbam ģenerē atsevišķa vietnes sadaļa (PD_generate/), tāpēc šeit
uzdevumu nav.
"""

from math_saturs import Doma, Kopsavilkums, Majas, Sakums


def _mikrotemati(temats):
    """«Mikrotemats (6 stundas)» - ar ko katrs temata gabals nodarbojās."""
    return ["%s - %d. līdz %d. stunda"
            % (b.nosaukums, b.stundas[0].nr, b.stundas[-1].nr)
            for b in temats.bloki]


def _atkarto(temats):
    """Jautājumi, ar kuriem pārbaudīt sevi: viens par katru mikrotematu."""
    return ["%s: vai vari izstāstīt, ko šeit mācījāmies, un parādīt vienu "
            "piemēru?" % b.nosaukums for b in temats.bloki]


class _Saturs(object):
    """Tāds pats saturs, kādu dod stundas fails: TEMA, MERKIS un SATURS."""

    PARBAUDES_DARBS = True           # dzīves uzdevumu te negaida

    def __init__(self, stunda):
        temats = stunda.temats
        self.TEMA = stunda.tema
        self.MERKIS = ("Šodien parādīsi, ko esi iemācījies tematā «%s»."
                       % temats.nosaukums)
        self.SATURS = [
            Sakums("Šodien ir temata «%s» pārbaudes darbs"
                   % temats.nosaukums,
                   fakti=["Darbs aizņem visu stundu.",
                          "Vērtē tikai stundās apgūto - nekā jauna nebūs.",
                          "Svars gada vērtējumā: %d %%." % temats.svars]),
            Doma("Ko vērtēs?", temats.pd_sr,
                 soli=_mikrotemati(temats),
                 pieze="Ja kāds no šiem punktiem vēl neskaidrs, sāc "
                       "atkārtot ar to."),
            Kopsavilkums(_atkarto(temats),
                         virsraksts="Pārbaudi sevi pirms darba"),
            Majas([
                "Pārskati savas pierakstu burtnīcas lapas par šo tematu.",
                "Izrēķini vēlreiz vienu uzdevumu, kas stundā nepadevās.",
                "Sagatavo, kas darbā vajadzīgs: pildspalva, zīmulis, lineāls.",
            ], virsraksts="Kā sagatavoties",
                ievads="Vislabāk palīdz nevis lasīšana, bet viens pašam "
                       "izrēķināts uzdevums."),
        ]


def saturs(stunda):
    """Pārbaudes darba stundas saturs vai None, ja tā nav PD stunda."""
    if not stunda.pd or not stunda.temats:
        return None
    return _Saturs(stunda)
