class APIResponseError(Exception):
    def __init__(self, response):
        self.status_code = response.status_code
        self.message = response.text

    def __str__(self):
        return 'APIError, status_code: {0}, message: {1}'.format(self.status_code,
            self.message)
