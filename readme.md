python wrapper for the papertrail API

Example
=======
    >>> import pypertrail
    >>> pt = pypertrail.Pypertrail(ACCESS_TOKEN)
    >>> resp = pt.search_events('Critical error')
    >>> for event in resp['events']:
    ...     print event['message']

    >>> import time
    >>> hour_ago = time.time() - 3600
    >>> opts = {'min_time': hour_ago}
    >>> resp = pt.search_events('OutOfMemory', opts=opts)
