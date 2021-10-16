from typing import Any

import proto

__protobuf__: Any

class CustomerMatchUploadKeyTypeEnum(proto.Message):
    class CustomerMatchUploadKeyType(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CONTACT_INFO: int
        CRM_ID: int
        MOBILE_ADVERTISING_ID: int
