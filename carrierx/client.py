from carrierx.base.rest_client import RestClient, RestConnection
from carrierx.resources import core
from carrierx.resources import mediator


class CoreClient(RestClient):
    def __init__(self, username, password, base_url="htts://api.carrierx.com/core/v2"):
        super().__init__(RestConnection(username, password, base_url))

        self.endpoints = core.Endpoints(self.connection)
        self.storage = lambda: None
        self.storage.containers = core.storage.Containers(self.connection)
        self.storage.files = core.storage.Files(self.connection)


class MediatorClient(RestClient):
    def __init__(self, username, password, base_url="htts://api.carrierx.com/mediator/v1"):
        super().__init__(RestConnection(username, password, base_url))

        self.bindings = mediator.Bindings(self.connection)
        self.dids = mediator.Dids(self.connection)

