# -*- coding: utf-8 -*-
"""9. klase, 53. stunda: «Kur figūrā ir taisnleņķa trijstūris?»

Trigonometrija strādā arī figūrās, kas pašas nav taisnleņķa: augstums
vienādsānu trijstūrī, rombā diagonāles, taisnstūrī diagonāle, trapecē
augstums. Prasme ir ieraudzīt taisnleņķa trijstūri.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Paraugs, Pasaule, Sakums, Slidnis, Varianti,
                         geometrija, trapece)

TEMA = "Kur figūrā ir taisnleņķa trijstūris?"

MERKIS = ("Saskatīsim taisnleņķa trijstūrus citās figūrās un izmantosim tos "
          "aprēķinos.")

_VIENADSANU = geometrija([("A", 0, 0), ("B", 8, 0), ("C", 4, 3),
                          ("D", 4, 0)],
                         nogriezni=["AB", "BC", "CA"], izcelti=["CD"],
                         taisni=["ADC"], iekrasot=[("ADC", 1)],
                         lenki=[("DAC", "α")])
_ROMBS = geometrija([("A", 0, 0), ("B", 4, -2.5), ("C", 8, 0),
                     ("D", 4, 2.5), ("O", 4, 0, -60)],
                    nogriezni=["AB", "BC", "CD", "DA"], izcelti=["AC", "BD"],
                    taisni=["AOD"], iekrasot=[("AOD", 1)])
_TAISNSTURIS = geometrija([("A", 0, 0), ("B", 8, 0), ("C", 8, 4.5),
                           ("D", 0, 4.5)],
                          nogriezni=["AB", "BC", "CD", "DA"],
                          izcelti=["AC"], iekrasot=[("ABC", 1)],
                          lenki=[("BAC", "α")])
_TRAPECE = geometrija(trapece(10, 4, 4, pedas=True)[:5],
                      nogriezni=TRAPECES_MALAS + ["DH"], taisni=["DHB"],
                      iekrasot=[("AHD", 1)], lenki=[("HAD", "α")])

SATURS = [
    Sakums("Taisnleņķa trijstūri slēpjas visur",
           zimejums=_ROMBS,
           paraksts="Rombā diagonāles ir perpendikulāras - 4 taisnleņķa "
                    "trijstūri.",
           fakti=["Vienādsānu trijstūris: augstums uz pamatu.",
                  "Rombs: diagonāles krustojas taisnā leņķī.",
                  "Taisnstūris: diagonāle; trapece: augstums."]),

    Slidnis("Atrodi taisnleņķa trijstūri", [
        {"v": "Vienādsānu", "teksts": "Augstums CD dala pamatu uz pusēm",
         "zim": _VIENADSANU},
        {"v": "Rombs", "teksts": "AO un DO - pusdiagonāles, AD - mala",
         "zim": _ROMBS},
        {"v": "Taisnstūris", "teksts": "Diagonāle AC - hipotenūza",
         "zim": _TAISNSTURIS},
        {"v": "Trapece", "teksts": "Augstums DH un AH = {a − b|2}",
         "zim": _TRAPECE},
    ]),

    Doma("Plāns",
         "Atrodi taisnleņķa trijstūri ar vienu zināmu malu un zināmu leņķi "
         "(vai divām malām) - tad sin, cos vai tg.",
         soli=[
             "Novelc augstumu vai diagonāli, ja vajag.",
             "Iekrāso trijstūri, kurā strādāsi.",
             "Pārnes zināmos lielumus uz tā malām (pusdiagonāle, pusbāze).",
             "Aprēķini un pārnes rezultātu atpakaļ uz figūru.",
         ]),

    Paraugs("Vienādsānu trijstūris",
            uzd="Vienādsānu trijstūra pamats 16 cm, pamata leņķis 35°. "
                "Atrodi augstumu.",
            soli=[
                ("AD = 16 : 2 = 8", "Augstums dala pamatu uz pusēm."),
                ("tg 35° = {CD|8}", "Trijstūris ADC."),
                ("CD = 8 · 0,700 ≈ 5,6 cm", "tg 35° ≈ 0,700."),
            ],
            atbilde="≈ 5,6 cm"),

    Ievadi("Aprēķini (līdz desmitdaļām)", [
        {"jaut": "Taisnstūris 12 × 5. Diagonāles leņķis ar garāko malu "
                 "(līdz grādiem)?", "atb": ["23"],
         "padoms": "tg α = 5 : 12."},
        {"jaut": "Romba diagonāles 6 un 8. Mala?", "atb": ["5"],
         "padoms": "Pusdiagonāles 3 un 4."},
        {"jaut": "Romba mala 10, asais leņķis 60°. Īsākā diagonāle?",
         "atb": ["10"], "padoms": "Vienādmalu trijstūris."},
        {"jaut": "Vienādsānu trapece: sānu mala 6, α = 60°. Augstums "
                 "(līdz desmitdaļām)?", "atb": ["5,2"],
         "padoms": "6 · sin 60° ≈ 5,196."},
        {"jaut": "Vienādsānu trijstūris: sānu mala 10, virsotnes leņķis 40°. "
                 "Pamats (līdz desmitdaļām)? sin 20° ≈ 0,342",
         "atb": ["6,8"], "padoms": "2 · 10 · sin 20°."},
    ], pamats=3),

    Varianti("Kurš trijstūris?", [
        {"jaut": "Lai atrastu romba diagonāli no malas un leņķa, lieto "
                 "trijstūri...",
         "opcijas": ["ar hipotenūzu - romba malu", "ar hipotenūzu - "
                     "diagonāli", "visu rombu", "neviens neder"],
         "pareizi": 0, "padoms": "AOD: AD ir hipotenūza."},
        {"jaut": "Vienādsānu trijstūrī augstums pret pamatu...",
         "opcijas": ["dala pamatu un virsotnes leņķi uz pusēm",
                     "ir vienāds ar sānu malu", "ir paralēls pamatam",
                     "neeksistē"],
         "pareizi": 0, "padoms": "Simetrijas ass."},
    ]),

    Pasaule("Telts",
            Ievadi("", [
                {"jaut": "Telts priekšpuse - vienādsānu trijstūris: pamats "
                         "2,4 m, sāni 45° slīpi. Augstums (m)?",
                 "atb": ["1,2"], "padoms": "tg 45° = 1; 1,2 · 1."},
                {"jaut": "Sānu malas garums (m, līdz desmitdaļām)?",
                 "atb": ["1,7"], "padoms": "1,2 · √2 ≈ 1,697."},
            ]),
            pavediens="celojums",
            konteksts="Pārgājiena telts priekšpuse ir vienādsānu trijstūris.",
            kapec="Augstums dala telti divos taisnleņķa trijstūros.",
            zimejums=_VIENADSANU),

    Kopsavilkums([
        "Saskatu taisnleņķa trijstūrus figūrās.",
        "Pārnesu lielumus uz tiem (pusbāze, pusdiagonāle).",
        "Aprēķinu figūras lielumus ar trigonometriju.",
    ]),

    Majas([
        "Taisnstūra diagonāle 20 cm veido 30° ar malu. Atrodi malas.",
        "Romba mala 8, asais leņķis 50°. Atrodi diagonāles.",
        "Uzzīmē 3 figūras un iekrāso tajās taisnleņķa trijstūrus.",
    ]),
]
