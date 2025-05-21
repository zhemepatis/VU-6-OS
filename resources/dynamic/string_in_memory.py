from enums.resource_names import ResourceNames
from enums.resource_types import ResourceTypes
from resources.resource import Resource

class StringInMemoryResource(Resource):
    def __init__(self, line):
        super().__init__(ResourceNames.EILUTE_ATIMINTYJE, ResourceTypes.DYNAMIC)
        # resource specific
        self.line = line