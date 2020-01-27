import json
import logging

import requests

from carrierx.base.rest_client import RestClient
from carrierx.exceptions import (
    ApiNotFoundException,
    ApiPermissionException,
    ApiServerError,
    ApiValueError,
)

logger = logging.getLogger()


def _validate_status_code(r):
    if r.status_code == 200:
        return
    if r.status_code == 201:
        return
    elif r.status_code == 403:
        raise ApiPermissionException()
    elif r.status_code == 404:
        raise ApiNotFoundException()
    elif r.status_code == 400:
        try:
            errors = json.loads(r.content.decode())['errors']
            raise ApiValueError(errors)
        except (ValueError, KeyError):
            # fall through to default error if error response cannot be parsed
            pass

    raise ApiServerError("Unexpected response from server: {0}: {1}".format(r.status_code, r.content))


class ItemResource(RestClient):
    wrapper = False

    def __init__(self, connection, data=None):
        super().__init__(connection)
        if data:
            for k in self.fields:
                setattr(self, k, data.get(k))
            self.clean()

    def __str__(self):
        fields = ['{0}={1!r}'.format(x, getattr(self, x)) for x in self.fields if getattr(self, x, None) is not None]
        buf = '{0}({1})'.format(self.__class__.__name__, ", ".join(fields))
        return buf

    def __repr__(self):
        return str(self)

    @classmethod
    def from_dict(cls, data):
        o = cls(None)
        for k in cls.fields:
            setattr(o, k, data.get(k))
        o.clean()
        return o

    def to_json(self):
        data = {}
        for k in self.fields:
            v = getattr(self, k, None)
            if v is not None:
                data[k] = v
        return json.dumps(data)

    def clean(self):
        return

    def update(self, **data):
        url = '{0}/{1}/{2}'.format(self.connection.base_url, self.endpoint_path, getattr(self, self.sid_field))

        for k in data.keys():
            if k not in self.update_fields:
                raise ApiValueError("Field {0} not allowed in update, must be in {1}".format(k, self.update_fields))

        request_args = {'url': url,
                        'headers': self.connection.headers,
                        'data': json.dumps(data)}

        if not self.connection.auth_token:
            request_args['auth'] = self.connection.auth

        r = requests.patch(**request_args)

        _validate_status_code(r)

        return r.content.decode()

    def delete(self):
        url = '{0}/{1}/{2}'.format(self.connection.base_url, self.endpoint_path, getattr(self, self.sid_field))

        request_args = {'url': url,
                        'headers': self.connection.headers}

        if not self.connection.auth_token:
            request_args['auth'] = self.connection.auth

        r = requests.delete(**request_args)

        _validate_status_code(r)

        return r.content.decode()


class ListResource(RestClient):
    LIST_LIMIT = 1000
    wrapper = False

    def create(self, **data):
        url = '{0}/{1}'.format(self.connection.base_url, self.endpoint_path)

        if data.get('instance'):
            instance = data['instance']
        else:
            for k in data.keys():
                if k not in self.item_resource.create_fields:
                    raise ApiValueError("Field {0} not allowed in create, must be in {1}".format(
                        k, self.item_resource.create_fields))

            instance = self.item_resource.from_dict(data)

        logger.debug("POST {0}: {1}: {2!r}".format(url, data, instance))

        request_args = {'url': url,
                        'headers': self.connection.headers,
                        'data': instance.to_json()}

        if not self.connection.auth_token:
            request_args['auth'] = self.connection.auth

        r = requests.post(**request_args)
        _validate_status_code(r)

        try:
            if self.wrapper:
                ser = r.json()['body']
            else:
                ser = r.json()
        except ValueError:
            raise ApiServerError("Unparseable response from server: {0}: {1}".format(r.status_code, r.content))
        return self.item_resource(self.connection, ser)

    def get(self, sid):
        url = '{0}/{1}/{2}'.format(self.connection.base_url, self.endpoint_path, sid)
        r = requests.get(
            url=url,
            auth=self.connection.auth,
            headers=self.connection.headers,
        )

        request_args = {'url': url, 'headers': self.connection.headers}

        if not self.connection.auth_token:
            request_args['auth'] = self.connection.auth

        r = requests.get(**request_args)

        _validate_status_code(r)
        try:
            if self.wrapper:
                data = r.json()['body']
            else:
                data = r.json()
        except ValueError:
            raise ApiServerError("Unparseable response from server: {0}: {1}".format(r.status_code, r.content))
        else:
            return self.item_resource(self.connection, data)

    def exists(self, filter=None):
        url = '{0}/{1}'.format(self.connection.base_url, self.endpoint_path)

        request_args = {
            'url': url,
            'headers': self.connection.headers,
            'params': {
                'offset': 0,
                'limit': 1,
                'includeFields': self.item_resource.sid_field,
                'filter': filter,
            }
        }

        if not self.connection.auth_token:
            request_args['auth'] = self.connection.auth

        r = requests.get(**request_args)
        _validate_status_code(r)

        try:
            if self.wrapper:
                data = r.json()['body']['total']
            else:
                data = r.json()['total']
        except ValueError:
            raise ApiServerError("Unparseable response from server: {0}: {1}".format(r.status_code, r.content))
        else:
            return data > 0

    def list(self, filter=None, offset=None, limit=None, order=None):
        if offset is None:
            offset = 0
        if limit is None:
            limit = self.LIST_LIMIT
        else:
            limit = min(limit, self.LIST_LIMIT)

        url = '{0}/{1}'.format(self.connection.base_url, self.endpoint_path)

        request_args = {
            'url': url,
            'headers': self.connection.headers,
            'params': {
                'offset': offset,
                'limit': limit,
                'filter': filter,
                'order': order,
            },
        }

        if not self.connection.auth_token:
            request_args['auth'] = self.connection.auth

        r = requests.get(**request_args)

        _validate_status_code(r)

        try:
            if self.wrapper:
                data = r.json()['body']['items']
            else:
                data = r.json()['items']
        except ValueError:
            raise ApiServerError("Unparseable response from server: {0}: {1}".format(r.status_code, r.content))
        else:
            return [self.item_resource(self.connection, x) for x in data]
