import requests
from exceptions import APIResponseError

class Pypertrail(object):
    def __init__(self, api_token):
        self.headers = {
            'X-Papertrail-Token': api_token,
            'User-Agent': 'https://github.com/JonathanCooper/pypertrail'
        }

    def search_events(self, search_string, **kwargs):
        param_names = ['group_id', 'system_id', 'min_id', 'min_time', 'max_id',
            'max_time']
        params = {'q': search_string}
        max_of_ones = [('group_id', 'system_id'),
            ('min_id', 'min_time'),
            ('max_id', 'max_time')]
        set_keys = set(kwargs.keys())
        for tup in max_of_ones:
            if tup[0] in set_keys and tup[1] in set_keys:
                raise TypeError('You can only use 1 of {0}, {1}'.format(tup[0], tup[1]))
        params.update(kwargs)
        uri = 'https://papertrailapp.com/api/v1/events/search.json'
        r = requests.get(uri, headers=self.headers, params=params)
        if r.status_code != 200:
            raise APIResponseError(r)
        else:
            return r.json()
