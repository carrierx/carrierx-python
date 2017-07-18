from operator import itemgetter

from carrierx.resources.base import ItemResource, ListResource


class Container(ItemResource):
    endpoint_path = 'storage/containers'
    create_fields = (
        'name',
        'partner_sid',
        'unique',
        'parent_container_sid',
        'quota_count',
        'quota_bytes',
        'durability_class',
        'integer_key_1',
        'integer_key_2',
        'string_key_1',
        'string_key_2',
    )
    retrieve_fields = (
        'container_sid',
        'name',
        'partner_sid',
        'unique',
        'parent_container_sid',
        'quota_count',
        'quota_bytes',
        'durability_class',
        'integer_key_1',
        'integer_key_2',
        'string_key_1',
        'string_key_2',
        'total_bytes',
        'total_files',
        'available_files_percent',
        'available_bytes_percent',
    )
    update_fields = create_fields
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'container_sid'


class Containers(ListResource):
    endpoint_path = 'storage/containers'
    item_resource = Container
