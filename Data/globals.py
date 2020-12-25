INITIALIZATION = True
ADDING_CARGO = False

SAVEFILE_PATH = ''
SAVE_FILE = {}
CACHED_SAVEFILE = {}
ERRORS = []

VERSION = 'v0.4.1'

PORTS = {
    '9f50ee22-a594-4c42-939c-022cbe2fb677': {
        'Name': 'The Reach',
        'Id': {
            '8576ef12-9e4d-4f30-8116-db5eb80f9543': {
                'DisplayName': 'New Winchester',
                'InternalName': 'New Winchester'
            },
            '86641b94-c0de-48d5-b1c5-7fcdd70d3882': {
                'DisplayName': 'Hybras',
                'InternalName': 'Hybras'
            },
            '8fcc687f-1e9b-444a-a758-c402d0608733': {
                'DisplayName': 'Polmear and Plenty\'s Inconceivable Circus',
                'InternalName': 'The Inconceivable Circus'
            },
            '89aff93f-4b2e-4e03-bb41-d6054a84c5ee': {
                'DisplayName': 'Port Avon',
                'InternalName': 'Port Avon'
            },
            '660ff730-50ea-4190-8210-a232c6e7b087': {
                'DisplayName': 'Traitor\'s Wood',
                'InternalName': 'Traitor\'s Wood'
            },
            'a3e0d4ac-b595-42b6-8b10-349478fc7874': {
                'DisplayName': 'Leadbeater & Stainrod\'s Nature Reserve',
                'InternalName': 'Leadbeater & Stainrod Reserve'
            },
            '7f7247f1-34b4-4f57-95d8-d482105edcb2': {
                'DisplayName': 'Titania',
                'InternalName': 'Titania'
            },
            '21004c53-ad6e-43e4-8df4-0230da3e87e6': {
                'DisplayName': 'Magdalene\'s',
                'InternalName': 'Magdalene\'s',
            },
            '6c1c3a55-b424-4bec-a969-31023ace58e7': {
                'DisplayName': 'Port Prosper',
                'InternalName': 'Prosper'
            },
            'f3ca7b9d-a6ba-4d2a-bbd1-b12d4ec25036': {
                'DisplayName': 'Carillon',
                'InternalName': 'Carillon'
            },
            'c22807a9-7c42-41b5-823a-cc02f15c3f63': {
                'DisplayName': 'Lustrum',
                'InternalName': 'Lustrum'
            }
        }
    },
    '7e3ccf00-f0a8-47c1-b444-33e2f84a82b1': {
        'Name': 'Eleutheria',
        'Id': {
            'bb49fdab-1ebe-45d9-97cb-9ab39db8d2a8': {
                'DisplayName': 'Pan',
                'InternalName': 'Pan'
            },
            '06401842-00d7-463c-8d6b-6fdd41b2edae': {
                'DisplayName': 'Piranesi',
                'InternalName': 'Piranesi'
            },
            'dad2e4cc-5983-41db-8e20-d07104e92666': {
                'DisplayName': 'Eagle\'s Empyrean',
                'InternalName': 'Eagle\'s Empyrean'
            },
            'b14c0b6b-839c-4311-bfd5-518edeea28ad': {
                'DisplayName': 'House of Rods and Chains',
                'InternalName': 'House of Rods and Chains'
            },
            '418df4ef-902a-4ae9-9673-31e2978ce7b7': {
                'DisplayName': 'Langley Hall',
                'InternalName': 'Langley Hall'
            },
            '44773c30-e3dd-4ce4-a8bd-fec7b55bb463': {
                'DisplayName': 'Caduceus',
                'InternalName': 'Caduceus'
            },
            '9e91ea8e-3f0f-4a25-a400-2f451d91da81': {
                'DisplayName': 'Achlys',
                'InternalName': 'Achlys'
            },
            '83901830-f638-46e2-a130-b198d0552c84': {
                'DisplayName': 'Winter\'s Reside',
                'InternalName': 'Winter\'s Reside'
            },
            '495ca56d-e543-417b-a431-8e3ce0a4f8cc': {
                'DisplayName': 'The Brazen Brigade',
                'InternalName': 'The Brazen Brigade'
            },
            '72c7faeb-59a4-4726-9ebd-2b76b94c749b': {
                'DisplayName': 'The Gentlemen',
                'InternalName': 'The Gentlemen'
            },
            '3b960cb2-0335-4e16-935b-0e8000c0628a': {
                'DisplayName': 'Heart-Catcher Gardens',
                'InternalName': 'Heart-Catcher Gardens'
            }
        }
    },
    '25d750b5-bb46-409c-8a94-5676bad0df17': {
        'Name': 'The Blue Kingdom',
        'Id': {
            '8a6a2b39-691a-4373-a2d6-d0ef8f9853c7': {
                'DisplayName': 'The Forge of Souls',
                'InternalName': 'The Forge of Souls'
            },
            'f6d9ca88-cece-47ea-a973-264a37df87d7': {
                'DisplayName': 'Sky Barnet',
                'InternalName': 'Sky Barnet'
            },
            'c74be88b-b3dc-48e8-8659-ace9a2ca719a': {
                'DisplayName': 'The House of Days',
                'InternalName': 'House of Days'
            },
            '692cba21-55a3-4b38-b493-ba8849d0d123': {
                'DisplayName': 'The Shadow of the Sun',
                'InternalName': 'The Shadow of the Sun'
            },
            '97191169-a980-43eb-b965-d23c80cb0f85': {
                'DisplayName': 'Death\'s Door',
                'InternalName': 'Death\'s Door'
            },
            'd1c6e57c-ee23-45e6-b94a-e6ecf8d78f6d': {
                'DisplayName': 'Wellmouth',
                'InternalName': 'Wellmouth'
            },
            '27259fac-64b1-4385-ae4c-f84235504dee': {
                'DisplayName': 'The Stone-Faced Court',
                'InternalName': 'The White Well'
            }
        }
    },
    '3ea179aa-2a9c-47c5-9dc3-20fee32fc228': {
        'Name': 'Albion',
        'Id': {
            'fc40ea42-ec67-4e47-9ec0-8a8c1b41af7a': {
                'DisplayName': 'London',
                'InternalName': 'London'
            },
            'b301a570-2040-44e9-b679-aca62bac89f7': {
                'DisplayName': 'The Floating Parliament',
                'InternalName': 'Floating Parliament'
            },
            '86643f84-680c-415a-bf00-d4dceb891189': {
                'DisplayName': 'The Brabazon Workworld',
                'InternalName': 'Brabazon Workworld'
            },
            '731c7b0d-d06d-4681-a3b3-d265eaea8d82': {
                'DisplayName': 'The Royal Society',
                'InternalName': 'Royal Society'
            },
            'bfc72a01-6af5-4c74-9354-74848b97c35d': {
                'DisplayName': 'The Clockwork Sun',
                'InternalName': 'Clockwork Sun'
            },
            'dd23161a-eafa-4b19-be78-bb27d5c340d2': {
                'DisplayName': 'Perdurance',
                'InternalName': 'Perdurance'
            },
            '1b331350-d950-4c06-94e0-38dd736859d7': {
                'DisplayName': 'Avid Horizon',
                'InternalName': 'Avid Horizon'
            },
            '358df020-9a27-47c3-8a80-6f1c836898df': {
                'DisplayName': 'The Most Serene Mausoleum',
                'InternalName': 'Mausoleum'
            },
            '359b836b-864d-4587-8527-e2d2c360fdeb': {
                'DisplayName': 'Worlebury-juxta-Mare',
                'InternalName': 'Worlebury-juxta-Mare'
            },
            '3ea179aa-2a9c-47c5-9dc3-20fee32fc228': {
                'DisplayName': 'Wit & Vinegar Lumber Co.',
                'InternalName': 'Wit & Vinegar Lumber Co.'
            },
            '289aa8ac-754d-4610-9639-cc888c3f6eac': {
                'DisplayName': 'The Ministries',
                'InternalName': 'Ministries',
            }
        }
    }
}

PORT_REPORT_IDS = {
    'The Reach': [132173, 132174, 132175, 132176, 132177, 132179, 132194, 132195, 132326, 132314],
    'Albion': [133500, 133501, 133502, 133503, 133504, 133506, 133507, 135434],
    'Eleutheria': [135149, 133505, 135474, 135477, 135946, 137442],
    'The Blue Kingdom': [138083, 138084, 138085, 139090]
}

CARGO_IDS = {
    '131665': 'Barrel of Unseasoned Hours',
    '131662': 'Bronzewood',
    '131661': 'Caddy of Dried Tea',
    '131659': 'Caged Catch',
    '131663': 'Carefully-Packed Crate of Munitions',
    '131740': 'Cask of Navaratine Gemstones',
    '131666': 'Crate of Nostalgic Crockery',
    '135269': 'Curator\'s Egg',
    '132096': 'Fuel',
    '131664': 'Gourd of Chorister Nectar',
    '131657': 'Jumble of Undistinguished Souls',
    '131667': 'Ministry-Approved Literature',
    '131660': 'Pane of Stained Glass',
    '131669': 'Roll of Thirsty Bombazine',
    '131668': 'Sack of Verdant Seeds',
    '131658': 'Selection of Immaculate Souls',
    '132186': 'Supplies',
    '138994': 'Hogshead of Starshine',
    '138995': 'Trunk of Illicit Literature',
    '138996': 'Firkin of Red Honey',
    '135538': 'Adamant-Reinforced Windshield',
    '137235': 'Additional Cargo Bay',
    '137244': 'Adjustable Infirmary',
    '135534': 'Amniotic Crew Containment/Anti-Breach System',
    '133855': 'Bronzewood Shielding',
    '133853': 'Cabinet of Curiosities',
    '137211': 'Caminus Yards \'Blackjape\'',
    '133107': 'Caminus Yards \'Brassraven\'',
    '137210': 'Caminus Yards \'Grimalkin\'',
    '137213': 'Caminus Yards \'Saintfire\'',
    '135539': '\'Cantankerous\' Boring-Rig',
    '135544': 'Carmilla',
    '139180': 'Concealed Cavities',
    '135708': 'Contentable Cabins',
    '133854': 'Cosy Cabins',
    '137205': 'Cotterell & Hathersage \'Beulah\'',
    '133108': 'Cotterell & Hathersage \'Emanation\'',
    '137214': 'Cotterell & Hathersage \'Golgonooza\'',
    '133106': 'Cotterell & Hathersage \'Jerusalem\'',
    '137212': 'Cotterell & Hathersage \'Vala\'',
    '137236': 'Cramped Quarters',
    '134834': 'Crown & Misery Pneumatic Mining Array',
    '135082': '\'Durendal\' Pressure-Canning System',
    '135711': 'Fitted Cupboards',
    '137239': 'Gleaming Galley',
    '135542': '\'Heathcliffe\' Durable Plating',
    '139181': 'Hidden Hold',
    '137242': 'Interior Support Pillars',
    '137240': 'Lamellared Sky-Steel Plating',
    '135540': 'Mechanical Turk',
    '135537': '\'Mighty Pen\' Defensive Library System',
    '135532': '\'Montressor\' Chamber',
    '135080': 'Murgatroyd\'s \'Stain-Away\' Canning Station',
    '135710': 'Pergamon-Category Shielding',
    '135543': '\'Pluto\' Miniature Law-Furnace',
    '139069': 'Portsmouth House \'Albertine Candle\'',
    '139070': 'Portsmouth House \'Her Renewed Majesty\'s Jubilee\'',
    '135541': '\'Prosperina\' Superior Mining and Smelting Array',
    '137196': 'Reclaimed Marauder Mangonel',
    '137245': 'Rose & Adamant Plating',
    '135533': 'Rosetti Cabins',
    '137237': 'Sensible Plumbing',
    '135535': '\'Signora Zenobia\' Prestige Scythe',
    '135545': 'The \'Osiris\' Patented Divider',
    '135705': 'The \'Speciometer\' Assaying Device',
    '137197': 'The \'Uninvited\'',
    '137247': 'The Watchers in Azure',
    '137198': '\'The Tears of Astolat\'',
    '137199': '\'The Wrath of Heaven\'',
    '136995': 'Ravelling Jack',
    '135712': 'Wit & Winegar Sawing Device',
    '139072': 'Wit & Winegar \'Sneeze Lurker\'',
    '137238': 'Wit & Winegar Winch & Pulley',
    '139073': 'Wit & Winegar \'Zounderkite\'',
    '136735': 'Cyclopean Owl',
    '133856': 'Diffident Bat',
    '136736': 'Intrepid Cavy',
    '136733': 'Star-Smitten Bat',
    '136734': 'The Ratronaut'
}

POSSIBLE_CARGO = {}
