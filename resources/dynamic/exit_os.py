from enums.resource_names import ResourceNames
from resources.resource import Resource

class ExitOSResource(Resource):
    def __init__(self):
        super().__init__(ResourceNames.OS_PABAIGA)