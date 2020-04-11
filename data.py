#!/usr/bin/env python
'''
    data
    ----

    Load saved data.
'''

import os
import json
import path

def load_matches():
    '''Load all matches from file.'''

    matches_dir = os.path.join(path.data_dir(), 'matches')
    os.makedirs(matches_dir, exist_ok=True)

    matches = []
    for basename in os.listdir(matches_dir):
        full_path = os.path.join(matches_dir, basename)
        with open(full_path) as f:
            matches.append(json.load(f))

    return matches