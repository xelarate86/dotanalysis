'''
    api
    ---

    Utilities to query the OpenDOTA API.
'''

import requests
import sys
import time

# CONSTANTS
# ---------

# Domain name for OpenDota.
HOST = 'https://api.opendota.com'
# Time to sleep for free tier requests to avoid rate limits.
FREE_TIER_RATE_LIMIT = 1
# Time to sleep for premium tier requests to avoid rate limits.
PREMIUM_TIER_RATE_LIMIT = 1 / 20
# OpenDota API key (optional). Can be None or the API key as a string.
API_KEY = None
# Timeout for an API request.
TIMEOUT = 5
# Maximum number of retries for read timeout errors.
MAX_RETRIES = 20

# HELPERS
# -------

def api_key():
    '''Format API key to the parameters.'''

    if API_KEY is not None:
        return {'api_key': API_KEY}
    return {}

def sleep(params=None):
    '''Sleep to avoid incurring rate limits.'''

    if params is None or params.get('api_key') is None:
        time.sleep(FREE_TIER_RATE_LIMIT)
    else:
        time.sleep(PREMIUM_TIER_RATE_LIMIT)

def single_get(url, params=None, timeout=TIMEOUT):
    '''Single get request.'''

    sleep(params)
    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()

    return response.json()

def persistent_get(url, params=None, timeout=TIMEOUT, retries=0, max_retries=MAX_RETRIES):
    '''Persistent get request, whcih repeatedly retries if various connection errors occur.'''

    try:
        return single_get(url, params=params, timeout=timeout)
    except (requests.exceptions.BaseHTTPError, requests.exceptions.RequestException) as error:
        print(f'{error.__class__.__name__} error in request for URL "{url}"', file=sys.stderr)
        if retries < max_retries:
            return persistent_get(url, params=params, timeout=timeout, retries=retries+1)
        else:
            raise

def get(url, params=None, timeout=TIMEOUT, persistent=False):
    '''Make GET request to the OpenDOTA API, including rate limits.'''

    if persistent:
        return persistent_get(url, params=params, timeout=timeout)
    return single_get(url, params=params, timeout=timeout)

# RESOURCES
# ---------

# Methods to simplify calls to the OpenDota resources.

def explorer(sql, persistent=False):
    '''Make a request to the OpenDOTA explorer resource.'''

    # Get our client URL and parameters.
    url = f'{HOST}/api/explorer'
    params = api_key()
    params['sql'] = sql

    # Make request and process result.
    data = get(url, params=params, persistent=persistent)
    if data['err'] is not None:
        raise RuntimeError(f'Unexpected error, got {data["err"]}')

    return data['rows']

def match(match_id, persistent=False):
    '''Make a request to the OpenDOTA matches resource.'''

    url = f'{HOST}/api/matches/{match_id}'
    params = api_key()

    return get(url, params=params, persistent=persistent)