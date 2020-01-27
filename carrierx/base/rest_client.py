class RestConnection:
    def __init__(self, username='', password='', token='', base_url=''):
        self.auth = (username, password)
        self.auth_token = token
        self.base_url = base_url
        self.headers = {'Content-type': 'application/json'}

        if token:
            self.headers['Authorization'] = 'Bearer {0}'.format(self.auth_token)

    def __repr__(self):
        return '{0}({1!r}, {2!r}, {3!r}, {4!r})'.format(self.__class__.__name__, self.auth[0], self.auth[1], self.auth_token, self.base_url)


class RestClient:
    def __init__(self, connection):
        self.connection = connection

    def __repr__(self):
        return '{0}({1!r})'.format(self.__class__.__name__, self.connection)
