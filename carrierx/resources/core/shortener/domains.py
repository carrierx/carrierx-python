from carrierx.resources.base import ItemResource, ListResource


class Domain(ItemResource):
    wrapper = False
    endpoint_path = 'shortener/domains'
    create_fields = (
        'domain_name',
        'partner_sid',
        'scope',
        'minimum_length',
        'not_found_page',
        'not_found_mode',
        'not_found_status_code',
        'expired_page',
        'expired_mode',
        'expired_status_code',
        'secure',
        'suffix_pattern'
    )
    retrieve_fields = (
        'domain_sid',
        'partner_sid',
        'domain_name',
        'scope',
        'minimum_length',
        'not_found_page',
        'not_found_mode',
        'not_found_status_code',
        'expired_page',
        'expired_mode',
        'expired_status_code',
        'secure',
        'suffix_pattern'
    )
    update_fields = create_fields
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'domain_sid'


class Domains(ListResource):
    endpoint_path = 'shortener/domains'
    item_resource = Domain
