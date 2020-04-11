'''
    item
    ----

    Utilities to process DOTA2 items.
'''

import operator

# Item identifiers, from OpenDota.
ITEMS = {
    1: 'blink',
    2: 'blades_of_attack',
    3: 'broadsword',
    4: 'chainmail',
    5: 'claymore',
    6: 'helm_of_iron_will',
    7: 'javelin',
    8: 'mithril_hammer',
    9: 'platemail',
    10: 'quarterstaff',
    11: 'quelling_blade',
    12: 'ring_of_protection',
    13: 'gauntlets',
    14: 'slippers',
    15: 'mantle',
    16: 'branches',
    17: 'belt_of_strength',
    18: 'boots_of_elves',
    19: 'robe',
    20: 'circlet',
    21: 'ogre_axe',
    22: 'blade_of_alacrity',
    23: 'staff_of_wizardry',
    24: 'ultimate_orb',
    25: 'gloves',
    26: 'lifesteal',
    27: 'ring_of_regen',
    28: 'sobi_mask',
    29: 'boots',
    30: 'gem',
    31: 'cloak',
    32: 'talisman_of_evasion',
    33: 'cheese',
    34: 'magic_stick',
    35: 'recipe_magic_wand',
    36: 'magic_wand',
    37: 'ghost',
    38: 'clarity',
    39: 'flask',
    40: 'dust',
    41: 'bottle',
    42: 'ward_observer',
    43: 'ward_sentry',
    44: 'tango',
    45: 'courier',
    46: 'tpscroll',
    47: 'recipe_travel_boots',
    48: 'travel_boots',
    49: 'recipe_phase_boots',
    50: 'phase_boots',
    51: 'demon_edge',
    52: 'eagle',
    53: 'reaver',
    54: 'relic',
    55: 'hyperstone',
    56: 'ring_of_health',
    57: 'void_stone',
    58: 'mystic_staff',
    59: 'energy_booster',
    60: 'point_booster',
    61: 'vitality_booster',
    62: 'recipe_power_treads',
    63: 'power_treads',
    64: 'recipe_hand_of_midas',
    65: 'hand_of_midas',
    66: 'recipe_oblivion_staff',
    67: 'oblivion_staff',
    68: 'recipe_pers',
    69: 'pers',
    70: 'recipe_poor_mans_shield',
    71: 'poor_mans_shield',
    72: 'recipe_bracer',
    73: 'bracer',
    74: 'recipe_wraith_band',
    75: 'wraith_band',
    76: 'recipe_null_talisman',
    77: 'null_talisman',
    78: 'recipe_mekansm',
    79: 'mekansm',
    80: 'recipe_vladmir',
    81: 'vladmir',
    85: 'recipe_buckler',
    86: 'buckler',
    87: 'recipe_ring_of_basilius',
    88: 'ring_of_basilius',
    89: 'recipe_pipe',
    90: 'pipe',
    91: 'recipe_urn_of_shadows',
    92: 'urn_of_shadows',
    93: 'recipe_headdress',
    94: 'headdress',
    95: 'recipe_sheepstick',
    96: 'sheepstick',
    97: 'recipe_orchid',
    98: 'orchid',
    99: 'recipe_cyclone',
    100: 'cyclone',
    101: 'recipe_force_staff',
    102: 'force_staff',
    103: 'recipe_dagon',
    104: 'dagon',
    105: 'recipe_necronomicon',
    106: 'necronomicon',
    107: 'recipe_ultimate_scepter',
    108: 'ultimate_scepter',
    109: 'recipe_refresher',
    110: 'refresher',
    111: 'recipe_assault',
    112: 'assault',
    113: 'recipe_heart',
    114: 'heart',
    115: 'recipe_black_king_bar',
    116: 'black_king_bar',
    117: 'aegis',
    118: 'recipe_shivas_guard',
    119: 'shivas_guard',
    120: 'recipe_bloodstone',
    121: 'bloodstone',
    122: 'recipe_sphere',
    123: 'sphere',
    124: 'recipe_vanguard',
    125: 'vanguard',
    126: 'recipe_blade_mail',
    127: 'blade_mail',
    128: 'recipe_soul_booster',
    129: 'soul_booster',
    130: 'recipe_hood_of_defiance',
    131: 'hood_of_defiance',
    132: 'recipe_rapier',
    133: 'rapier',
    134: 'recipe_monkey_king_bar',
    135: 'monkey_king_bar',
    136: 'recipe_radiance',
    137: 'radiance',
    138: 'recipe_butterfly',
    139: 'butterfly',
    140: 'recipe_greater_crit',
    141: 'greater_crit',
    142: 'recipe_basher',
    143: 'basher',
    144: 'recipe_bfury',
    145: 'bfury',
    146: 'recipe_manta',
    147: 'manta',
    148: 'recipe_lesser_crit',
    149: 'lesser_crit',
    150: 'recipe_armlet',
    151: 'armlet',
    152: 'invis_sword',
    153: 'recipe_sange_and_yasha',
    154: 'sange_and_yasha',
    155: 'recipe_satanic',
    156: 'satanic',
    157: 'recipe_mjollnir',
    158: 'mjollnir',
    159: 'recipe_skadi',
    160: 'skadi',
    161: 'recipe_sange',
    162: 'sange',
    163: 'recipe_helm_of_the_dominator',
    164: 'helm_of_the_dominator',
    165: 'recipe_maelstrom',
    166: 'maelstrom',
    167: 'recipe_desolator',
    168: 'desolator',
    169: 'recipe_yasha',
    170: 'yasha',
    171: 'recipe_mask_of_madness',
    172: 'mask_of_madness',
    173: 'recipe_diffusal_blade',
    174: 'diffusal_blade',
    175: 'recipe_ethereal_blade',
    176: 'ethereal_blade',
    177: 'recipe_soul_ring',
    178: 'soul_ring',
    179: 'recipe_arcane_boots',
    180: 'arcane_boots',
    181: 'orb_of_venom',
    182: 'stout_shield',
    183: 'recipe_invis_sword',
    184: 'recipe_ancient_janggo',
    185: 'ancient_janggo',
    186: 'recipe_medallion_of_courage',
    187: 'medallion_of_courage',
    188: 'smoke_of_deceit',
    189: 'recipe_veil_of_discord',
    190: 'veil_of_discord',
    191: 'recipe_necronomicon_2',
    192: 'recipe_necronomicon_3',
    193: 'necronomicon_2',
    194: 'necronomicon_3',
    196: 'diffusal_blade_2',
    197: 'recipe_dagon_2',
    198: 'recipe_dagon_3',
    199: 'recipe_dagon_4',
    200: 'recipe_dagon_5',
    201: 'dagon_2',
    202: 'dagon_3',
    203: 'dagon_4',
    204: 'dagon_5',
    205: 'recipe_rod_of_atos',
    206: 'rod_of_atos',
    207: 'recipe_abyssal_blade',
    208: 'abyssal_blade',
    209: 'recipe_heavens_halberd',
    210: 'heavens_halberd',
    211: 'recipe_ring_of_aquila',
    212: 'ring_of_aquila',
    213: 'recipe_tranquil_boots',
    214: 'tranquil_boots',
    215: 'shadow_amulet',
    216: 'enchanted_mango',
    217: 'recipe_ward_dispenser',
    218: 'ward_dispenser',
    219: 'recipe_travel_boots_2',
    220: 'travel_boots_2',
    221: 'recipe_lotus_orb',
    222: 'recipe_meteor_hammer',
    223: 'meteor_hammer',
    224: 'recipe_nullifier',
    225: 'nullifier',
    226: 'lotus_orb',
    227: 'recipe_solar_crest',
    228: 'recipe_octarine_core',
    229: 'solar_crest',
    230: 'recipe_guardian_greaves',
    231: 'guardian_greaves',
    232: 'aether_lens',
    233: 'recipe_aether_lens',
    234: 'recipe_dragon_lance',
    235: 'octarine_core',
    236: 'dragon_lance',
    237: 'faerie_fire',
    238: 'recipe_iron_talon',
    239: 'iron_talon',
    240: 'blight_stone',
    241: 'tango_single',
    242: 'crimson_guard',
    243: 'recipe_crimson_guard',
    244: 'wind_lace',
    245: 'recipe_bloodthorn',
    246: 'recipe_moon_shard',
    247: 'moon_shard',
    248: 'recipe_silver_edge',
    249: 'silver_edge',
    250: 'bloodthorn',
    251: 'recipe_echo_sabre',
    252: 'echo_sabre',
    253: 'recipe_glimmer_cape',
    254: 'glimmer_cape',
    255: 'recipe_aeon_disk',
    256: 'aeon_disk',
    257: 'tome_of_knowledge',
    258: 'recipe_kaya',
    259: 'kaya',
    260: 'refresher_shard',
    261: 'crown',
    262: 'recipe_hurricane_pike',
    263: 'hurricane_pike',
    265: 'infused_raindrop',
    266: 'recipe_spirit_vessel',
    267: 'spirit_vessel',
    268: 'recipe_holy_locket',
    269: 'holy_locket',
    270: 'recipe_ultimate_scepter_2',
    271: 'ultimate_scepter_2',
    272: 'recipe_kaya_and_sange',
    273: 'kaya_and_sange',
    274: 'recipe_yasha_and_kaya',
    275: 'recipe_trident',
    276: 'combo_breaker',
    277: 'yasha_and_kaya',
    279: 'ring_of_tarrasque',
    286: 'flying_courier',
    287: 'keen_optic',
    288: 'grove_bow',
    289: 'quickening_charm',
    290: 'philosophers_stone',
    291: 'force_boots',
    292: 'desolator_2',
    293: 'phoenix_ash',
    294: 'seer_stone',
    295: 'greater_mango',
    297: 'vampire_fangs',
    298: 'craggy_coat',
    299: 'greater_faerie_fire',
    300: 'timeless_relic',
    301: 'mirror_shield',
    302: 'elixer',
    303: 'recipe_ironwood_tree',
    304: 'ironwood_tree',
    305: 'royal_jelly',
    306: 'pupils_gift',
    307: 'tome_of_aghanim',
    308: 'repair_kit',
    309: 'mind_breaker',
    310: 'third_eye',
    311: 'spell_prism',
    312: 'horizon',
    313: 'fusion_rune',
    317: 'recipe_fallen_sky',
    325: 'princes_knife',
    326: 'spider_legs',
    327: 'helm_of_the_undying',
    328: 'mango_tree',
    329: 'recipe_vambrace',
    330: 'witless_shako',
    331: 'vambrace',
    334: 'imp_claw',
    335: 'flicker',
    336: 'spy_gadget',
    349: 'arcane_ring',
    354: 'ocean_heart',
    355: 'broom_handle',
    356: 'trusty_shovel',
    357: 'nether_shawl',
    358: 'dragon_scale',
    359: 'essence_ring',
    360: 'clumsy_net',
    361: 'enchanted_quiver',
    362: 'ninja_gear',
    363: 'illusionsts_cape',
    364: 'havoc_hammer',
    365: 'panic_button',
    366: 'apex',
    367: 'ballista',
    368: 'woodland_striders',
    369: 'trident',
    370: 'demonicon',
    371: 'fallen_sky',
    372: 'pirate_hat',
    373: 'dimensional_doorway',
    374: 'ex_machina',
    375: 'faded_broach',
    376: 'paladin_sword',
    377: 'minotaur_horn',
    378: 'orb_of_destruction',
    379: 'the_leveller',
    381: 'titan_sliver',
    1021: 'river_painter',
    1022: 'river_painter2',
    1023: 'river_painter3',
    1024: 'river_painter4',
    1025: 'river_painter5',
    1026: 'river_painter6',
    1027: 'river_painter7',
    1028: 'mutation_tombstone',
    1029: 'super_blink',
    1030: 'pocket_tower',
    1032: 'pocket_roshan'
}

# Names of all tier 1 neutral items.
TIER1_NEUTRAL_NAMES = {
    'arcane_ring',
    'broom_handle',
    'faded_broach',
    'iron_talon',
    'ironwood_tree',
    'keen_optic',
    'mango_tree',
    'ocean_heart',
    'poor_mans_shield',
    'royal_jelly',
    'trusty_shovel'
}

# Names of all tier 2 neutral items.
TIER2_NEUTRAL_NAMES = {
    'clumsy_net',
    'dragon_scale',
    'essence_ring',
    'grove_bow',
    'imp_claw',
    'nether_shawl',
    'philosophers_stone',
    'pupils_gift',
    'ring_of_aquila',
    'vambrace',
    'vampire_fangs'
}

# Names of all tier 3 neutral items.
TIER3_NEUTRAL_NAMES = {
    'craggy_coat',
    'enchanted_quiver',
    'greater_faerie_fire',
    'mind_breaker',
    'orb_of_destruction',
    'paladin_sword',
    'quickening_charm',
    'repair_kit',
    'spider_legs',
    'spy_gadget',   # Telescope
    'titan_sliver'
}

# Names of all tier 4 neutral items.
TIER4_NEUTRAL_NAMES = {
    'flicker',
    'havoc_hammer',
    'illusionsts_cape',
    'panic_button', # Magic Lamp
    'minotaur_horn',
    'ninja_gear',
    'princes_knife',
    'spell_prism',
    'the_leveller',
    'timeless_relic',
    'witless_shako'
}

# Names of all tier 5 neutral items.
TIER5_NEUTRAL_NAMES = {
    'apex',
    'ballista',
    'woodland_striders',
    'recipe_trident',
    'trident',
    'demonicon',    # Book of the Dead
    'fallen_sky',
    'pirate_hat',
    'ex_machina',
    'the_leveller',
    'seer_stone',
    'mirror_shield',
    'desolator_2',  # Stygian Desolator
    'force_boots'
}

# Names of all neutral items.
NEUTRAL_NAMES = (
    TIER1_NEUTRAL_NAMES
    | TIER2_NEUTRAL_NAMES
    | TIER3_NEUTRAL_NAMES
    | TIER4_NEUTRAL_NAMES
    | TIER5_NEUTRAL_NAMES
)

def normalize_item(item):
    '''Normalize item to item name.'''

    if isinstance(item, int):
        return ITEMS[item]
    return item

# Key names of item slots.
ITEM_SLOTS = operator.itemgetter(
    'item_0',
    'item_1',
    'item_2',
    'item_3',
    'item_4',
    'item_5'
)

# Key names of backpack slots.
BACKPACK_SLOTS = operator.itemgetter(
    'backpack_0',
    'backpack_1',
    'backpack_2',
    'backpack_3'
)

# Key names of the neutral item slot.
NEUTRAL_SLOT = operator.itemgetter(
    'item_neutral'
)

def item_filter(item_id):
    '''Filter to remove invalid item IDs.'''
    return item_id is not None and item_id != 0

def extract_items(player):
    '''Process the item, backpack, and neutral slot identifiers to names.'''

    result = {}

    # Process the items.
    item_ids = [i for i in ITEM_SLOTS(player) if item_filter(i)]
    result['items'] = [ITEMS[i] for i in item_ids]

    # Process the backpack.
    backpack_ids = [i for i in BACKPACK_SLOTS(player) if item_filter(i)]
    result['backpack'] = [ITEMS[i] for i in backpack_ids]

    # Process the neutral item.
    if item_filter(NEUTRAL_SLOT(player)):
        result['neutral_item'] = ITEMS[NEUTRAL_SLOT(player)]

    return result

def is_neutral(item):
    '''Determine if item is a neutral item.'''
    return normalize_item(item) in NEUTRAL_NAMES

def is_recipe(item):
    '''Determine if the item is a recipe.'''
    return 'recipe' in normalize_item(item)

def is_tier1_neutral(item):
    '''Determine if item is a tier 1 neutral item.'''
    return normalize_item(item) in TIER1_NEUTRAL_NAMES

def is_tier2_neutral(item):
    '''Determine if item is a tier 2 neutral item.'''
    return normalize_item(item) in TIER2_NEUTRAL_NAMES

def is_tier3_neutral(item):
    '''Determine if item is a tier 3 neutral item.'''
    return normalize_item(item) in TIER3_NEUTRAL_NAMES

def is_tier4_neutral(item):
    '''Determine if item is a tier 4 neutral item.'''
    return normalize_item(item) in TIER4_NEUTRAL_NAMES

def is_tier5_neutral(item):
    '''Determine if item is a tier 5 neutral item.'''
    return normalize_item(item) in TIER5_NEUTRAL_NAMES