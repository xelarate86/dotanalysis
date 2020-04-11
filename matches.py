'''
    matches
    -------

    Extract a certain number of matches based on certain criteria.
'''

from api import explorer
from query import query

# Number of results per query. Should be decently low, to avoid throttled requests.
MAX_LIMIT = 300

def recent_match_ids(count, initial_conditions=None, persistent=False):
    '''Generate up to `count` recent match IDs as a generator from the explorer API.'''

    # Generate our initial query, and make first request for N items.
    columns = ['public_matches.match_id']
    table = 'public_matches'
    order = 'public_matches.match_id DESC'
    limit = min(MAX_LIMIT, count)
    sql_query = query(
        columns,
        table,
        conditions=initial_conditions,
        order=order,
        limit=limit
    )
    rows = explorer(sql_query, persistent=persistent)
    count -= len(rows)
    yield from [i['match_id'] for i in rows]

    # Make iterative requests until we fetch `count` items.
    # If we ever return less than `limit` items, we know that we've
    # made our last query, exhausted the data.
    subsequent_conditions = ([] or initial_conditions) + ['public_matches.match_id < {match_id}']
    while limit == len(rows) and count > 0:
        limit = min(MAX_LIMIT, count)
        match_id = rows[-1]['match_id']
        sql_query = query(
            columns,
            table,
            conditions=subsequent_conditions,
            order=order,
            limit=limit
        ).format(match_id=match_id)
        rows = explorer(sql_query, persistent=persistent)
        count -= len(rows)
        yield from [i['match_id'] for i in rows]