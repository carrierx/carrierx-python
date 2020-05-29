from carrierx.resources.base import ItemResource, ListResource


class Message(ItemResource):
    wrapper = False
    endpoint_path = 'sms/messages'
    create_fields = (
        'from_did',
        'to_did',
        'message',
        'media_urls',
    )
    retrieve_fields = (
        'message_sid',
        'from_did',
        'to_did',
        'message',
        'date_created',
        'date_status_changed',
        'status'
    )
    update_fields = ()
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'message_sid'


class Messages(ListResource):
    wrapper = False
    endpoint_path = 'sms/messages'
    item_resource = Message
