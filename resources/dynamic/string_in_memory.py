from enums.resource_names import ResourceNames
from resources.resource import Resource

class StringInMemoryResource(Resource):
    def __init__(self, line):
        super().__init__(ResourceNames.EILUTE_ATIMINTYJE)
        # resource specific
        self.line = line