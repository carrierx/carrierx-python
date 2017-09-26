from carrierx.resources.base import ItemResource, ListResource


class Did(ItemResource):
    wrapper = False
    endpoint_path = 'dids'
    create_fields = ()
    retrieve_fields = (
        'did_sid',
        'phonenumber',
        'account_sid',
        'url',
        'method',
    )
    update_fields = ()
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'did_sid'


class Dids(ListResource):
    wrapper = False
    endpoint_path = 'dids'
    item_resource = Did
