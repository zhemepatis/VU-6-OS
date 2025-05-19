from enums.resource_names import ResourceNames
from resources.resource import Resource

class UserMemoryResource(Resource):
    def __init__(self):
        super().__init__(ResourceNames.PROCESORIUS)