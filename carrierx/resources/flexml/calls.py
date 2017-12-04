from carrierx.resources.base import ItemResource, ListResource


class Call(ItemResource):
    wrapper = False
    endpoint_path = 'calls'
    create_fields = (
        'calling_did',
        'called_did',
        'url',
        'method',
        'attributes',
    )
    retrieve_fields = ()
    update_fields = ()
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'call_sid'


class Calls(ListResource):
    wrapper = False
    endpoint_path = 'calls'
    item_resource = Call
