from enums.resource_names import ResourceNames
from resources.resource import Resource

class UserInputResource(Resource):
    def __init__(self):
        super().__init__(ResourceNames.VARTOTOJO_IVESTIS)
