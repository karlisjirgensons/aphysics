# -*- coding: utf-8 -*-
"""7. klase, 96. stunda: «Kas ir īpašība un kas - pazīme?»

Īpašība: ja taisnes paralēlas, tad leņķi vienādi. Pazīme: ja leņķi vienādi,
tad taisnes paralēlas. Tās ir apgrieztas teorēmas: nosacījums un
secinājums samainīti. Stunda iemāca tās atšķirt un lietot pareizā vietā.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, paralelas, restis)

TEMA = "Kas ir īpašība un kas - pazīme?"

MERKIS = ("Paskaidrosim atšķirību starp īpašību un pazīmi un minēsim "
          "piemērus.")

SATURS = [
    Sakums("Paralēlas → leņķi vienādi. Leņķi vienādi → paralēlas?",
           zimejums=restis([["", "ja ...", "tad ..."],
                            ["īpašība", "a ∥ b", "∠1 = ∠5"],
                            ["pazīme", "∠1 = ∠5", "a ∥ b"]]),
           paraksts="Tie paši vārdi, samainītā secībā.",
           fakti=["Īpašība saka, kas ir patiess par zināmu figūru.",
                  "Pazīme saka, kā figūru atpazīt.",
                  "Paralēlām taisnēm abas ir patiesas."]),

    Doma("Īpašība izriet no figūras, pazīme - atpazīst to",
         "Īpašība ir teorēma «ja figūra ir X, tad tai ir Y». Pazīme ir "
         "teorēma «ja figūrai ir Y, tad tā ir X». Pazīmi lieto, lai "
         "pierādītu, ka figūra ir X.",
         soli=[
             "Jāaprēķina leņķis, zinot a ∥ b - lieto īpašību.",
             "Jāpierāda a ∥ b, zinot leņķus - lieto pazīmi.",
             "Pazīmes: kāpšļu vienādi, šķērsleņķi vienādi vai "
             "vienpusleņķu summa 180° - tad a ∥ b.",
         ],
         pieze="Ne katrai īpašībai apgrieztā ir patiesa: «ja kvadrāts, tad "
               "4 vienādas malas» - patiesa; «ja 4 vienādas malas, tad "
               "kvadrāts» - nē (rombs)."),

    Paraugs("Pierādi paralelitāti",
            uzd="Krustotājs c veido ∠3 = 64° un ∠5 = 64°. Vai a ∥ b?",
            soli=[
                ("∠3 un ∠5 - iekšējie šķērsleņķi", "Nosauc pāri."),
                ("∠3 = ∠5", "(dots)"),
                ("a ∥ b", "(pazīme: šķērsleņķi vienādi)"),
            ],
            atbilde="Jā, a ∥ b."),

    Zimejums("Nav paralēlas - leņķi atšķiras",
             paralelas(radit=(1, 5), paralelas=False,
                       uzraksti={1: "54°", 5: "60°"}),
             paskaidro="∠1 ≠ ∠5 - pēc pazīmes taisnes nav paralēlas."),

    Varianti("Īpašība vai pazīme?", [
        {"jaut": "«Ja a ∥ b, tad ∠4 + ∠5 = 180°.»",
         "opcijas": ["Īpašība", "Pazīme"], "pareizi": 0, "jaukt": False,
         "padoms": "Sākas ar a ∥ b."},
        {"jaut": "«Ja ∠2 = ∠6, tad a ∥ b.»",
         "opcijas": ["Īpašība", "Pazīme"], "pareizi": 1, "jaukt": False,
         "padoms": "Secina paralelitāti."},
        {"jaut": "«Ja trijstūrim divi leņķi vienādi, tas ir vienādsānu.»",
         "opcijas": ["Īpašība", "Pazīme"], "pareizi": 1, "jaukt": False,
         "padoms": "Atpazīst vienādsānu."},
        {"jaut": "«Vienādsānu trijstūrim leņķi pie pamata vienādi.»",
         "opcijas": ["Īpašība", "Pazīme"], "pareizi": 0, "jaukt": False,
         "padoms": "Zināms, ka vienādsānu."},
    ], pamats=4),

    Varianti("Vai a ∥ b?", [
        {"jaut": "∠4 = 110°, ∠5 = 70°.",
         "opcijas": ["Jā - vienpusleņķu summa 180°", "Nē", "Nevar zināt"],
         "pareizi": 0, "padoms": "110 + 70 = 180."},
        {"jaut": "∠1 = 80°, ∠5 = 82°.",
         "opcijas": ["Nē - kāpšļu leņķi atšķiras", "Jā", "Nevar zināt"],
         "pareizi": 0, "padoms": "Nav vienādi."},
        {"jaut": "∠3 = 50°, ∠6 = 130°.",
         "opcijas": ["Jā - vienpusleņķi 180°", "Nē", "Nevar zināt"],
         "pareizi": 0, "padoms": "∠3 un ∠6 - vienpusleņķi."},
    ]),

    Pasaule("Plaukts pie sienas",
            Varianti("", [
                {"jaut": "Divi plaukti pie sienas veido ar to 90° katrs. "
                         "Kāpēc tie ir paralēli?",
                 "opcijas": ["Pazīme: kāpšļu leņķi vienādi",
                             "Īpašība", "Tā izskatās", "Nav paralēli"],
                 "pareizi": 0, "padoms": "Leņķi → paralēlas."},
                {"jaut": "Plaukti ir paralēli un viens 90° pret sienu. Kāds "
                         "ir otrs?",
                 "opcijas": ["90° - īpašība", "Nevar zināt", "45°",
                             "180°"],
                 "pareizi": 0, "padoms": "Paralēlas → leņķi."},
                {"jaut": "Ar ko meistars pārbauda plauktus?",
                 "opcijas": ["Ar līmeņrādi vai stūreni - mēra leņķi",
                             "Ar lineālu - garumu", "Ar svariem",
                             "Uz aci"],
                 "pareizi": 0, "padoms": "Pazīme balstās uz leņķiem."},
            ]),
            pavediens="maja",
            konteksts="Meistars paralelitāti nekad nemēra «līdz bezgalībai» - "
                      "viņš mēra leņķi un lieto pazīmi.",
            kapec="Pazīme ir praktisks tests."),

    Kopsavilkums([
        "Atšķiru īpašību no pazīmes.",
        "Lietoju pazīmi, lai pierādītu a ∥ b.",
        "Lietoju īpašību, lai aprēķinātu leņķus.",
        "Zinu, ka apgrieztā teorēma ne vienmēr ir patiesa.",
    ]),

    Majas([
        "Uzraksti 2 īpašības un 2 pazīmes no ģeometrijas.",
        "Katrai īpašībai uzraksti apgriezto un pārbaudi, vai patiesa.",
        "Pārbaudi grāmatu plauktu paralelitāti ar stūreni.",
    ]),
]
