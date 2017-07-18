from carrierx.resources.base import ItemResource, ListResource


class Did(ItemResource):
    wrapper = True
    endpoint_path = 'dids'
    create_fields = ()
    retrieve_fields = (
        'did_sid',
        'phonenumber',
        'account_sid',
        'country_code',
        'in_country_format',
        'international_format',
    )
    update_fields = ()
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'did_sid'


class Dids(ListResource):
    wrapper = True
    endpoint_path = 'dids'
    item_resource = Did
