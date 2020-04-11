'''
    neutral_probabilities
    ---------------------

    Calculate the probabilities of various neutral items.
'''

import collections
import json
import os
import path

import item

def classify_neutral_tier(neutral_item):
    '''Classify neutral item tier.'''

    if item.is_tier1_neutral(neutral_item):
        return '1'
    elif item.is_tier2_neutral(neutral_item):
        return '2'
    elif item.is_tier3_neutral(neutral_item):
        return '3'
    elif item.is_tier4_neutral(neutral_item):
        return '4'
    elif item.is_tier5_neutral(neutral_item):
        return '5'
    raise ValueError(f'Invalid item, got {neutral_item}')

def classify_neutral_items(items):
    '''Extract and classify all neutral items in the items slot.'''

    result = {}
    if 'neutral_item' in items:
        # Has an active neutral item.
        neutral_item = items['neutral_item']
        result['active'] = {'item': neutral_item, 'tier': classify_neutral_tier(neutral_item)}

    result['inactive'] = inactive = []
    for slot in items['backpack']:
        if item.is_neutral(slot):
            inactive.append({'item': slot, 'tier': classify_neutral_tier(slot)})

    return result

def calculate_active(neutral_items):
    '''Calculate neutral item probabilities for only active items.'''

    # Extract all the item names.
    active = []
    for neutral_item in neutral_items:
        if 'active' in neutral_item:
            active.append(neutral_item['active']['item'])

    # Create a counter for all the probabilities.
    counts = dict(collections.Counter(active))
    length = len(neutral_items)
    return {k: v / length for k, v in counts.items()}

def calculate_inactive(neutral_items):
    '''Calculate neutral item probabilities for only inactive items.'''

    # Extract all the inactive items.
    inactive = []
    for neutral_item in neutral_items:
        inactive.extend([i['item'] for i in neutral_item['inactive']])

    # Create a counter for all the probabilities.
    counts = dict(collections.Counter(inactive))
    length = len(neutral_items)
    return {k: v / length for k, v in counts.items()}

def calculate_total(neutral_items):
    '''Calculate neutral item probabilities for active or inactive items.'''

    total = []
    for neutral_item in neutral_items:
        total.extend([i['item'] for i in neutral_item['inactive']])
        if 'active' in neutral_item:
            total.append(neutral_item['active']['item'])

    # Create a counter for all the probabilities.
    counts = dict(collections.Counter(total))
    length = len(neutral_items)
    return {k: v / length for k, v in counts.items()}

def calculate(matches):
    '''Calculate neutral item probabilities for active, inactive, and toial item counts.'''

    # Extract all the items for all players over all matches.
    neutral_items = []
    for match in matches:
        for player in match['players']:
            neutral_items.append(classify_neutral_items(item.extract_items(player)))

    probabilities = {
        'active': calculate_active(neutral_items),
        'inactive': calculate_inactive(neutral_items),
        'total': calculate_total(neutral_items)
    }
    with open(os.path.join(path.data_dir(), 'neutral_probabilities.json'), 'w') as f:
        json.dump(probabilities, f, indent=4)

def calculate_trident_recipe_with_component(matches):
    '''Determine the chance that a player with a trident recipe has a trident component'''

    # Extract all the items for all players over all matches.
    has_component = []
    for match in matches:
        for player in match['players']:
            items = item.extract_items(player)
            if items.get('neutral_item') == 'recipe_trident' or 'recipe_trident' in items['backpack']:
                # Only continue if we have a trident recipe in here.
                flat_items = items['items'] + items['backpack']
                has_component.append(
                    'sange' in flat_items
                    or 'yasha' in flat_items
                    or 'kaya' in flat_items
                )

    return sum(has_component) / len(has_component)