from enums.resource_names import ResourceNames
from enums.resource_types import ResourceTypes
from resources.resource import Resource

class CreateFileResource(Resource):
    def __init__(self, filename):
        super().__init__(ResourceNames.UZKRAUK_FAILA, ResourceTypes.DYNAMIC)
        # resource specific
        self.filename = filename
