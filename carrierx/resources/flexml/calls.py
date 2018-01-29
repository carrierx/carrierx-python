from carrierx.resources.base import ItemResource, ListResource


class Call(ItemResource):
    wrapper = False
    endpoint_path = 'calls'
    create_fields = (
        'calling_did',
        'called_did',
        'url',
        'method',
        'status_callback_url',
        'status_callback_method'
    )
    retrieve_fields = ('call_sid',
                       'account_sid',
                       'date_created',
                       'calling_did',
                       'called_did',
                       'url',
                       'method',
                       'status_callback_url',
                       'status_callback_method',
                       'delay',
                       'attributes'
                       )
    update_fields = ('status_callback_url', 'status_callback_method')
    fields = set(create_fields) | set(retrieve_fields) | set(update_fields)
    sid_field = 'call_sid'


class Calls(ListResource):
    wrapper = False
    endpoint_path = 'calls'
    item_resource = Call
