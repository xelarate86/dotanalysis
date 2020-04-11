'''
    path
    ----

    Directory paths for the project.
'''

import os.path

def project_dir():
    '''Get path the project directory.'''
    return os.path.dirname(os.path.realpath(__file__))

def data_dir():
    '''Get path the data directory.'''
    return os.path.join(project_dir(), 'json')