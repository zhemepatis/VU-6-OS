from enums.resource_names import ResourceNames
from resources.resource import Resource

class UserInput(Resource):
    def __init__(self, filename):
        super().__init__(ResourceNames.VARTOTOJO_IVESTIS)
