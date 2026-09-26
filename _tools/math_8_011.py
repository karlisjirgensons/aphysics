# -*- coding: utf-8 -*-
"""8. klase, 11. stunda: «Kā formulēt pētījuma jautājumu?»

Pētījuma bloka sākums. Labs jautājums ir tāds, uz ko var atbildēt ar
skaitļiem: skaidrs, ko mēra, kam jautā un ar ko salīdzina. Stundā skolēns
pārveido izplūdušus jautājumus par izmērāmiem un sāk savu pētījumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā formulēt pētījuma jautājumu?"

MERKIS = ("Plānosim pētījuma mērķi un gaitu un formulēsim jautājumu, uz ko "
          "var atbildēt ar datiem.")

SATURS = [
    Sakums("«Vai jaunieši guļ par maz?»",
           zimejums=restis([["izplūdis", "izmērāms"],
                            ["par maz?", "cik h naktī?"],
                            ["jaunieši", "8. klases skolēni"],
                            ["guļ", "darba dienās"]]),
           paraksts="Tas pats jautājums - pēc tam, kad izlemts, ko mērīt.",
           fakti=["Ārsti iesaka 13-18 gadu vecumā 8-10 h miega.",
                  "«Par maz» kļūst par skaitli, ko var salīdzināt.",
                  "Izmērāmam jautājumam var savākt datus."]),

    Doma("Pētījuma plāns piecos soļos",
         "Pētījums sākas ar jautājumu, uz kuru var atbildēt ar skaitļiem. "
         "Pārējos soļus izlemj, pirms savāc pirmo datu vērtību.",
         soli=[
             "Jautājums: ko tieši mērīsi un par ko?",
             "Kopa un izlase: kam jautāsi vai ko mērīsi?",
             "Metode: aptauja, mērījums vai novērojums?",
             "Rādītāji: kurus aprēķināsi (vidējais, mediāna, biežums)?",
             "Salīdzinājums: ar ko salīdzināsi (norma, cita grupa)?",
         ],
         pieze="Pieraksti plānu, pirms sāc - citādi beigās dati neatbild "
               "uz jautājumu."),

    Varianti("Kurš jautājums ir izmērāms?", [
        {"jaut": "Izvēlies labāko pētījuma jautājumu.",
         "opcijas": ["Cik minūšu dienā 8. klases skolēni lieto TikTok?",
                     "Vai TikTok ir slikts?",
                     "Kāpēc visi lieto TikTok?",
                     "Vai sociālie tīkli ir interesanti?"],
         "pareizi": 0, "padoms": "Atbilde ir skaitlis."},
        {"jaut": "Kurš jautājums salīdzina divas grupas?",
         "opcijas": ["Vai zēni un meitenes guļ vienādi ilgi?",
                     "Cik ilgi guļ skolēni?",
                     "Vai miegs ir svarīgs?",
                     "Kas ir miegs?"],
         "pareizi": 0, "padoms": "Divas grupas, viens lielums."},
        {"jaut": "Pētījums par skolas somas svaru. Kura metode der?",
         "opcijas": ["Nosvērt somas ar svariem", "Pajautāt, vai soma smaga",
                     "Paskatīties uz somām", "Izlasīt internetā"],
         "pareizi": 0, "padoms": "Mērījums ir precīzāks par viedokli."},
    ]),

    Ievadi("Plāno izlasi un laiku", [
        {"jaut": "Skolā 8 klases pa 25 skolēniem. Izlasē ņem 20 %. Cik "
                 "skolēnu?",
         "atb": ["40"], "padoms": "20 % no 200."},
        {"jaut": "Aptaujā katrs pavada 3 min. Cik minūšu aptaujai vajag "
                 "kopā?",
         "atb": ["120"], "padoms": "40 · 3."},
        {"jaut": "Ieteicamā norma - somas svars ne vairāk par 10 % no "
                 "ķermeņa svara. Cik kg drīkst svērt 52 kg skolēna soma?",
         "atb": ["5,2", "5.2"], "padoms": "10 % no 52."},
    ]),

    Petijums("Sāc savu pētījumu",
             vajag="burtnīca vai izklājlapa",
             soli=[
                 "Izvēlies tēmu: miegs, ekrāna laiks, somas svars, ceļš uz "
                 "skolu vai sava.",
                 "Uzraksti izmērāmu jautājumu ar skaitli atbildē.",
                 "Nosaki kopu un izlasi (vismaz 20 vērtību).",
                 "Izvēlies metodi un uzraksti vienu aptaujas jautājumu.",
                 "Pieraksti, ar ko salīdzināsi rezultātu.",
             ],
             secinajums="Šo plānu turpināsi nākamajās stundās: savāksi datus, "
                        "aprēķināsi rādītājus un prezentēsi rezultātu."),

    Pasaule("Miega pētījuma plāns",
            Ievadi("", [
                {"jaut": "Norma 8-10 h. Skolēns guļ no 23:30 līdz 6:45. Cik "
                         "stundu? (decimāldaļā)",
                 "atb": ["7,25", "7.25"], "padoms": "7 h 15 min."},
                {"jaut": "Cik minūšu līdz normas apakšējai robežai trūkst?",
                 "atb": ["45"], "padoms": "8 h − 7 h 15 min."},
                {"jaut": "Izlasē 30 skolēni, 18 guļ mazāk par 8 h. Cik "
                         "procentu?",
                 "atb": ["60", "60 %", "60%"], "padoms": "18 : 30."},
            ]),
            pavediens="skola",
            konteksts="Pētījumi rāda, ka pusaudžu miegs darba dienās bieži ir "
                      "īsāks par ieteikto - to var pārbaudīt savā skolā.",
            kapec="Izmērāms jautājums dod skaitli, ko salīdzināt ar normu."),

    Kopsavilkums([
        "Pārveidoju izplūdušu jautājumu par izmērāmu.",
        "Izvēlos kopu, izlasi un metodi.",
        "Plānoju, ar kuriem rādītājiem un ar ko salīdzināšu.",
    ]),

    Majas([
        "Pabeidz sava pētījuma plānu (5 soļi).",
        "Parādi aptaujas jautājumu vienam cilvēkam - vai viņš to saprot?",
        "Uzlabo jautājumu, ja atbilde nav skaitlis.",
    ]),
]
