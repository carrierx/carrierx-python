from operator import itemgetter

from carrierx.resources.base import ItemResource, ListResource


class Endpoint(ItemResource):
    TYPE_SYSTEM_GATEWAY = 'system_gateway'
    TYPE_THIRD_PARTY = 'third_party'
    TYPE_CONFERENCE = 'conference'
    TYPE_FLEXML = 'flexml'
    TYPE_MEDIATOR = 'mediator'

    endpoint_path = 'endpoints'
    create_fields = (
        'addresses',
        'attributes',
        'capacity',
        'name',
        'partner_sid',
        'transformations',
        'type',
    )
    retrieve_fields = (
        'endpoint_sid',
        'addresses',
        'attributes',
        'properties',
        'capacity',
        'name',
        'partner_sid',
        'transformations',
        'type',
        'voip_token',
    )
    update_fields = create_fields
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'endpoint_sid'

    def getattr(self, name, default=None):
        for x in self.attributes:
            if x['key'] == name:
                return x['value']
        return default


class Endpoints(ListResource):
    endpoint_path = 'endpoints'
    item_resource = Endpoint
