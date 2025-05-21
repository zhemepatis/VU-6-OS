from enums.resource_names import ResourceNames
from enums.resource_types import ResourceTypes
from resources.resource import Resource

class SupervisorMemoryResource(Resource):
    def __init__(self):
        super().__init__(ResourceNames.SUPERVIZORINE, ResourceTypes.STATIC)