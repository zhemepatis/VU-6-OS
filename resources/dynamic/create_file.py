from enums.resource_names import ResourceNames
from resources.resource import Resource

class CreateFileResource(Resource):
    def __init__(self, filename):
        super().__init__(ResourceNames.UZKRAUK_FAILA)
        # resource specific
        self.filename = filename
