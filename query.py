'''
    query
    -----

    Construct simple SQL queries.
'''

def query(columns, table, conditions=None, order=None, limit=None):
    '''
    Create a simple SQL query from the following parameters:

    1). Columns. Columns to select to return data from.
    2). Table. SQL table to query. May include JOIN statements.
    3). Conditions (optional). Match criteria.
    4). Sort order (optional). Sorting for returned data.
    5). Limit (optional). Maximum number of items to return.

    Note: This is not safe to SQL injection, all strings should be **trusted**
    by the user. Since we are querying a read-only database, this risk
    is minimal.
    '''

    query = f'SELECT {", ".join(columns)}\nFROM {table}'
    if conditions is not None:
        query += f'\nWHERE {" AND ".join(conditions)}'
    if order is not None:
        query += f'\nORDER BY {order}'
    if limit is not None:
        query += f'\nLIMIT {limit}'

    return query