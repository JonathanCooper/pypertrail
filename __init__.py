import requests

class Pypertrail(object):
    def __init__(self, api_token):
        self.headers = {
            'X-Papertrail-Token': api_token,
            'User-Agent': 'https://github.com/JonathanCooper/pypertrail'
        }

    def search_events(self, search_string, opts=None):
        opts = opts or {}
        payload = {'q': search_string}
        payload.update(opts)
        uri = 'https://papertrailapp.com/api/v1/events/search.json'
        r = requests.get(uri, headers=self.headers, params=payload)
        return r.json()
