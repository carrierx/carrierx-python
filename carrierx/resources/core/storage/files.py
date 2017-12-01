from operator import itemgetter

from carrierx.resources.base import ItemResource, ListResource


class File(ItemResource):
    endpoint_path = 'storage/files'
    create_fields = (
        'name',
        'partner_sid',
        'container_sid',
        'parent_file_sid',
        'type',
        'file_access_name',
        'publish',
        'integer_key_1',
        'integer_key_2',
        'string_key_1',
        'string_key_2',
        'lifecycle_ttl',
        'lifecycle_action',
        'desired_format',
        'mime_type',
    )
    retrieve_fields = (
        'file_sid',
        'name',
        'partner_sid',
        'container_sid',
        'parent_file_sid',
        'type',
        'file_access_name',
        'publish',
        'integer_key_1',
        'integer_key_2',
        'string_key_1',
        'string_key_2',
        'lifecycle_ttl',
        'lifecycle_action',
        'desired_format',
        'mime_type',
        'file_bytes',
        'publish_uri',
        'date_modified',
        'content_format',
        'content_duration',
        'content_transcoding_progress',
    )
    update_fields = create_fields
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'file_sid'


class Files(ListResource):
    endpoint_path = 'storage/files'
    item_resource = File
