# -*- coding: utf-8 -*-
"""7. klase, 26. stunda: «Kā pārbaudīt vienādību?»

Vienādību var pārbaudīt praktiski: pārzīmē vienu figūru uz caurspīdīga
papīra un uzliec otrai, vai arī saloki papīru. Stunda saista šos
paņēmienus ar definīciju un iemāca pierakstīt, kas tika pārbaudīts.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, figura)

TEMA = "Kā pārbaudīt vienādību?"

MERKIS = ("Pārbaudīsim figūru vienādību ar caurspīdīgu papīru un "
          "locīšanu un pamatosim rezultātu.")

SATURS = [
    Sakums("Pauspapīrs - arhitekta vecais triks",
           zimejums=figura([(0, 0), (3, 0), (4, 2), (1, 3)],
                           platums=5, augstums=4),
           paraksts="Pārzīmē uz caurspīdīga papīra un uzliec otrai figūrai.",
           fakti=["Pirms datoriem rasējumus kopēja uz pauspapīra.",
                  "Ja kopija pilnībā sakrīt ar figūru - tās ir vienādas."]),

    Doma("Pārnes vai saloki - un salīdzini",
         "Figūru vienādību praktiski pārbauda, pārnesot vienu figūru uz "
         "otru (ar caurspīdīgu papīru) vai salokot papīru tā, lai viena "
         "figūra nonāktu uz otras.",
         soli=[
             "Pārzīmē vienu figūru uz caurspīdīga papīra.",
             "Bīdi, pagriez vai apgriez papīru otrādi.",
             "Ja kopija pilnībā sakrīt ar otru figūru - tās ir vienādas.",
             "Ja figūras ir simetriskas pret līniju - saloki pa to.",
         ],
         pieze="Praktiska pārbaude ir mērījums, un tai ir precizitāte. "
               "Ģeometrijā vienādību pierāda ar spriedumiem - to mācīsimies "
               "vēlāk ar trijstūriem."),

    Petijums("Pārbaudi ar pauspapīru",
             ["Uz rūtiņu lapas uzzīmē četrstūri un vēl vienu - tādu pašu, "
              "bet pagrieztu.",
              "Pārzīmē pirmo uz caurspīdīga papīra (vai cepampapīra).",
              "Uzliec kopiju otrajam četrstūrim: kā tas jāpagriež?",
              "Uzzīmē trešo četrstūri, kas atšķiras tikai par 1 rūtiņu. "
              "Vai kopija sakrīt?"],
             vajag="rūtiņu lapa, caurspīdīgs papīrs, zīmulis",
             secinajums="Pat 1 rūtiņas atšķirība ir redzama uzreiz - figūras "
                        "vairs nav vienādas."),

    Paraugs("Locīšanas pārbaude",
            uzd="Taisnstūra ABCD lapu saloka pa diagonāli AC. Vai "
                "trijstūri ABC un CDA ir vienādi?",
            soli=[
                ("Locot pa AC, B nenonāk uz D",
                 "Lapa nav kvadrāts - stūri neaizsniedz viens otru."),
                ("Bet △ABC pagriežot par 180° ap AC viduspunktu, tas "
                 "sakrīt ar △CDA",
                 "Pārnešana ar pagriešanu."),
                ("△ABC = △CDA", "A → C, B → D, C → A."),
            ],
            atbilde="Jā, vienādi - pārbauda ar pagriešanu, ne locīšanu."),

    Varianti("Kurš paņēmiens der?", [
        {"jaut": "Jāpārbauda, vai divi tauriņa spārni ir vienādi.",
         "opcijas": ["Salocīt pa ķermeņa līniju", "Nosvērt spārnus",
                     "Saskaitīt krāsas", "Izmērīt tikai garumu"],
         "pareizi": 0,
         "padoms": "Spārni ir simetriski."},
        {"jaut": "Jāpārbauda, vai divas flīzes grīdā ir vienādas.",
         "opcijas": ["Uzlikt vienu virsū otrai", "Salīdzināt krāsu",
                     "Salīdzināt laukumu vien", "Saskaitīt stūrus"],
         "pareizi": 0,
         "padoms": "Uzliek - sakrīt."},
        {"jaut": "Pēc locīšanas figūras sakrīt gandrīz, bet ne pilnīgi. Ko "
                 "tas nozīmē?",
         "opcijas": ["Tās nav vienādas vai zīmējums nav precīzs",
                     "Tās ir vienādas",
                     "Locīšana nekad nestrādā",
                     "Jāloka vēlreiz, līdz sakrīt"],
         "pareizi": 0,
         "padoms": "Praktiskai pārbaudei ir precizitāte."},
    ]),

    Zimejums("Simetrisks četrstūris - pārbauda ar locīšanu",
             figura([(0, 2), (3, 0), (6, 2), (3, 5)], platums=7, augstums=6),
             paskaidro="Salokot pa vertikālo diagonāli, kreisā puse sakrīt ar "
                       "labo."),

    Pasaule("Kvalitātes pārbaude ar kameru",
            Varianti("", [
                {"jaut": "Rūpnīcas kamera salīdzina katru detaļu ar "
                         "paraugu. Ko tā dara ģeometriski?",
                 "opcijas": ["Uzliek detaļas attēlu paraugam un meklē "
                             "nesakritības",
                             "Saskaita detaļas", "Nosver detaļu",
                             "Mēra temperatūru"],
                 "pareizi": 0,
                 "padoms": "Tas pats pauspapīrs, tikai digitāls."},
                {"jaut": "Detaļa ir pagriezta par 90°. Vai kamera to "
                         "noraidīs?",
                 "opcijas": ["Nē - pirms salīdzināšanas to pagriež",
                             "Jā - pagriezta figūra nav vienāda",
                             "Jā, vienmēr", "Tikai naktī"],
                 "pareizi": 0,
                 "padoms": "Pagriešana nemaina vienādību."},
                {"jaut": "Kamera redz detaļu, kas ir par 2 mm garāka. "
                         "Ko tā secina?",
                 "opcijas": ["Detaļa nav vienāda ar paraugu",
                             "Detaļa ir vienāda", "Detaļa ir pagriezta",
                             "Kamera ir salūzusi"],
                 "pareizi": 0,
                 "padoms": "Atbilstošās malas nav vienādas."},
            ]),
            pavediens="tehnika",
            konteksts="Mašīnredze rūpnīcās pārbauda vienādību tūkstošiem "
                      "reižu minūtē.",
            kapec="Vienādības definīcija ir algoritms datoram."),

    Kopsavilkums([
        "Pārbaudu vienādību ar caurspīdīgu papīru.",
        "Pārbaudu simetriskas figūras ar locīšanu.",
        "Zinu, ka praktiskai pārbaudei ir precizitāte.",
        "Pierakstu, kuras virsotnes sakrita.",
    ]),

    Majas([
        "Izgriez divus vienādus trijstūrus un pārbaudi ar uzlikšanu.",
        "Atrodi mājās figūru, ko var pārbaudīt ar locīšanu.",
        "Izdomā figūru pāri ar vienādu perimetru, kas nav vienādas.",
    ]),
]
