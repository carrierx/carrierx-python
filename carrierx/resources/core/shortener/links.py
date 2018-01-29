from carrierx.resources.base import ItemResource, ListResource


class Link(ItemResource):
    endpoint_path = 'shortener/links'
    create_fields = (
        'domain_sid',
        'destination_url',
        'mode',
        'maximum_ttl',
        'short_name',
        'date_created'
    )
    retrieve_fields = (
        'link_sid',
        'domain_sid',
        'partner_sid',
        'date_created',
        'date_accessed',
        'url',
        'destination_url',
        'short_name',
        'mode',
        'maximum_ttl',
        'hits'
    )
    update_fields = create_fields
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'link_sid'


class Links(ListResource):
    endpoint_path = 'shortener/links'
    item_resource = Link
