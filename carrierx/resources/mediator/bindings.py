from carrierx.resources.base import ItemResource, ListResource


class Binding(ItemResource):
    wrapper = True
    endpoint_path = 'bindings'
    create_fields = (
        'name',
        'account_sid',
        'origination_did',
        'redirect_did',
        'reuse',
        'destination_did',
        'maximum_ttl',
        'wait_origination_did_ttl',
        'dtmf',
        'attributes',
    )
    retrieve_fields = (
        'binding_sid',
        'name',
        'account_sid',
        'date_created',
        'origination_did',
        'redirect_did',
        'destination_did',
        'maximum_ttl',
        'wait_origination_did_ttl',
        'dtmf',
        'attributes',
    )
    update_fields = create_fields
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'binding_sid'

    def getattr(self, name, default=None):
        for x in self.attributes:
            if x['key'] == name:
                return x['value']
        return default


class Bindings(ListResource):
    wrapper = True
    endpoint_path = 'bindings'
    item_resource = Binding
