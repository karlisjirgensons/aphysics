# -*- coding: utf-8 -*-
"""Vecāku aptaujas (parent/) teikumi abās valodās - viena vieta (SRP).

E-pasta formas teikumi (poga, piekrišana, «Paldies!») nav šeit: forma ir tā
pati, kas dienas izaicinājumā (play_forma), un tās teikumi dzīvo
play_teksti (DRY). {x} vietas aizpilda JS (PT.f) vai Python (teksts).
"""

import json

import valoda

TEKSTI = {
    "en": {
        "virsraksts": "For parents",
        "ievads_v": "The small moments that shape a child",
        "ievads": ("5 quick questions about everyday time with your child. "
                   "Answer honestly - nobody is judging. It takes about a "
                   "minute."),
        "sakt": "Start",
        "sakt_meta": "5 questions · about 1 minute",
        # jautājumi
        "q_lasit": ("How often do you read with your child - or how often "
                    "did you, when they were younger?"),
        "q_spelet": ("How often do you play together - board games, ball, "
                     "building, or just fooling around?"),
        "q_macities": ("How often do you sit down with them to help with "
                       "homework or learning?"),
        "q_runat": ("How often do you really talk about their day - what "
                    "made them happy or worried?"),
        "q_est": ("How often do you eat together as a family, with no "
                  "screens at the table?"),
        # ieradumu īsie vārdi rezultātā
        "i_lasit": "Reading together",
        "i_spelet": "Playing together",
        "i_macities": "Learning together",
        "i_runat": "Talking about the day",
        "i_est": "Family meals",
        # atbildes - viena skala visiem jautājumiem
        "b0": "Almost every day",
        "b1": "A few times a week",
        "b2": "A few times a month",
        "b3": "Rarely",
        # rezultāts
        "tu": "You",
        "tipisks": "Typical parent*",
        "vairums": "Most parents: {a}",
        "virs_v": "Your child is lucky to have you",
        "virs": ("You give more everyday time than most parents in large "
                 "family studies. Children don't remember every lesson - "
                 "they remember who sat next to them. Keep going."),
        "lidz_v": "You're doing more than you think",
        "lidz": ("Your answers are close to what most parents say in large "
                 "family studies. Every story, game and chat adds up - and "
                 "you're already doing it."),
        "zem_v": "Every parent knows this feeling",
        "zem": ("Life gets busy, and being here already shows how much you "
                "care. Small moments matter most: ten minutes with a book "
                "or a game today is a wonderful start."),
        "cta_v": "We understand - and we want to help",
        "cta": ("We're building Calcubo for families like yours: short "
                "daily math moments to share with your child, so learning "
                "together feels easy, not like one more chore. Leave your "
                "email and we'll write to you when it's ready."),
        "avoti": ("* Typical answers are based on large family surveys, "
                  "such as the OECD PISA parent questionnaire and the "
                  "Scholastic Kids & Family Reading Report."),
    },
    "lv": {
        "virsraksts": "Vecākiem",
        "ievads_v": "Mazie brīži, kas veido bērnu",
        "ievads": ("5 īsi jautājumi par ikdienas laiku ar bērnu. Atbildi "
                   "godīgi - neviens tevi nevērtē. Tas aizņems apmēram "
                   "minūti."),
        "sakt": "Sākt",
        "sakt_meta": "5 jautājumi · apmēram 1 minūte",
        "q_lasit": ("Cik bieži tu lasi kopā ar bērnu - vai cik bieži lasīji, "
                    "kad bērns bija mazāks?"),
        "q_spelet": ("Cik bieži jūs spēlējaties kopā - galda spēles, bumba, "
                     "būvēšana vai vienkārši ākstīšanās?"),
        "q_macities": ("Cik bieži tu apsēdies blakus, lai palīdzētu ar "
                       "mājasdarbiem vai mācībām?"),
        "q_runat": ("Cik bieži jūs patiešām parunājat par bērna dienu - kas "
                    "iepriecināja vai satrauca?"),
        "q_est": ("Cik bieži jūs ēdat kopā kā ģimene, bez ekrāniem pie "
                  "galda?"),
        "i_lasit": "Lasīšana kopā",
        "i_spelet": "Spēlēšanās kopā",
        "i_macities": "Mācīšanās kopā",
        "i_runat": "Sarunas par dienu",
        "i_est": "Ģimenes maltītes",
        "b0": "Gandrīz katru dienu",
        "b1": "Dažas reizes nedēļā",
        "b2": "Dažas reizes mēnesī",
        "b3": "Reti",
        "tu": "Tu",
        "tipisks": "Tipisks vecāks*",
        "vairums": "Vairums vecāku: {a}",
        "virs_v": "Tavam bērnam ar tevi ļoti paveicies",
        "virs": ("Tu bērnam dod vairāk ikdienas laika nekā vairums vecāku "
                 "lielos ģimeņu pētījumos. Bērni neatceras katru stundu - "
                 "viņi atceras, kurš sēdēja blakus. Turpini tāpat."),
        "lidz_v": "Tu dari vairāk, nekā tev šķiet",
        "lidz": ("Tavas atbildes ir tuvu tam, ko lielos ģimeņu pētījumos "
                 "atbild vairums vecāku. Katra grāmata, spēle un saruna "
                 "krājas - un tu to jau dari."),
        "zem_v": "Šo sajūtu pazīst katrs vecāks",
        "zem": ("Dzīve mēdz būt steidzīga, un tas, ka esi šeit, jau parāda, "
                "cik ļoti tev rūp. Vissvarīgākie ir mazie brīži: desmit "
                "minūtes ar grāmatu vai spēli šodien ir lielisks sākums."),
        "cta_v": "Mēs tevi saprotam - un gribam palīdzēt",
        "cta": ("Calcubo top tieši tādām ģimenēm kā jūsējā: īsi ikdienas "
                "matemātikas brīži, ko piedzīvot kopā ar bērnu, lai kopā "
                "mācīties būtu viegli, nevis vēl viens pienākums. Atstāj "
                "e-pastu, un mēs uzrakstīsim, kad tas būs gatavs."),
        "avoti": ("* Tipiskās atbildes balstās lielos ģimeņu pētījumos, "
                  "piemēram, OECD PISA vecāku aptaujā un Scholastic "
                  "«Kids & Family Reading Report»."),
    },
}


def teksts(atslega):
    """Teikums tagadējā valodā (valoda.tagad())."""
    return TEKSTI[valoda.tagad()][atslega]


def js():
    """VT - tagadējās valodas teikumi (lapa ir vienā valodā)."""
    return "var VT=%s;" % json.dumps(TEKSTI[valoda.tagad()],
                                     ensure_ascii=False)
