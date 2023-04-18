# Question Bank as a list of dictionaries with the questions, options, weights
questions = [
            {
                "question": "How does your skin feel after cleansing?",
                "options": [
                    "Tight/dry",
                    "Comfortable/clean",
                    "Oily",
                    "Dry in some areas, oily in others",
                    "Easily irritated/red"
                ],
                "weights": [
                    {"dry": 2},
                    {"normal": 2},
                    {"oily": 2},
                    {"combination": 2},
                    {"sensitive": 2}
                ]
            },
            {
                "question": "How often do you experience breakouts?",
                "options": [
                    "Never/rarely",
                    "Occasionally",
                    "Frequently",
                    "Only in specific areas",
                    "Easily triggered by products/other environmental factors"
                ],
                "weights": [
                    {"normal": 2},
                    {"dry": 1, "combination": 1},
                    {"oily": 2},
                    {"combination": 2},
                    {"sensitive": 2}
                ]
            },
            {
                "question": "How would you describe your pores?",
                "options": [
                    "Small/barely visible",
                    "Medium-sized/mostly visible",
                    "Large/clearly visible",
                    "A mix of small/large pores",
                    "Easily clogged/irritated"
                ],
                "weights": [
                    {"dry": 2, "sensitive": 1},
                    {"normal": 2},
                    {"oily": 2},
                    {"combination": 2},
                    {"sensitive": 2}
                ]
            },
            {
                "question": "How does your skin react to the sun?",
                "options": [
                    "Burns easily/rarely tans",
                    "Burns sometimes/can also tan",
                    "Tans easily/minimal burning",
                    "A mix of burning/tanning",
                    "Easily irritated/develops rashes"
                ],
                "weights": [
                    {"dry": 1, "sensitive": 2},
                    {"normal": 2},
                    {"oily": 1},
                    {"combination": 2},
                    {"sensitive": 2}
                ]
            },
            {
                "question": "How does your skin feel during the day?",
                "options": [
                    "Dry/in need of moisturizing",
                    "Comfortable without the need for additional products",
                    "Greasy/shiny",
                    "A mix of dry/oily areas",
                    "Tight/itchy/easily irritated"
                ],
                "weights": [
                    {"dry": 2},
                    {"normal": 2},
                    {"oily": 2},
                    {"combination": 2},
                    {"sensitive": 2}
                ]
            },
            {
                "question": "How does your skin feel after applying makeup?",
                "options": [
                    "Flaky / dry",
                    "Smooth / comfortable",
                    "Shiny / oily",
                    "Dry in some areas / oily in others",
                    "Easily irritated / prone to redness"
                ],
                "weights": [
                    {"dry": 2},
                    {"normal": 2},
                    {"oily": 2},
                    {"combination": 2},
                    {"sensitive": 2}
                ]
            }
        ]

