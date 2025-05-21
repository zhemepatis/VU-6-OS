from enums.resource_names import *
from enums.resource_types import *
from resources.resource import *

class ChannelDeviceResource(Resource):
    def __init__(self):
        super().__init__(ResourceNames.KANALU_IRENGINYS, ResourceTypes.STATIC)