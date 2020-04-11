'''
    fetch
    ----

    Fetch raw match IDs and match information and export to JSON.
'''

import os
import json

import api
import path
from matches import recent_match_ids

def match_ids_path():
    '''Get path to a given match ID.'''

    os.makedirs(path.data_dir(), exist_ok=True)
    return os.path.join(path.data_dir(), 'match_ids.json')

def match_ids(count=1500):
    '''Fetch and save raw match IDs to JSON.'''

    conditions = [
        # Fetch only matches from the last week.
        'public_matches.start_time >= (extract(epoch from now()) - 604800)',
        # Fetch only matches longer than 1 hour.
        'public_matches.duration >= 3600'
    ]
    match_ids = list(recent_match_ids(count, initial_conditions=conditions), persistent=True)
    with open(match_ids_path(), 'w') as f:
        json.dump(match_ids, f, indent=4)

def matches():
    '''Fetch and save raw matches to JSON.'''

    with open(match_ids_path(), 'r') as f:
        match_ids = json.load(f)

    matches_dir = os.path.join(path.data_dir(), 'matches')
    os.makedirs(matches_dir, exist_ok=True)
    for match_id in match_ids:
        full_path = os.path.join(matches_dir, f'{match_id}.json')
        if not os.path.exists(full_path):
            # Fetch and save the match ID if it does not previously exist.
            match =  api.match(match_id, persistant=True)
            with open(full_path, 'w') as f:
                json.dump(match, f, indent=4)