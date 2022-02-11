from typing import Any

import proto

__protobuf__: Any

class OperationAccessDeniedErrorEnum(proto.Message):
    class OperationAccessDeniedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ACTION_NOT_PERMITTED: int
        CREATE_OPERATION_NOT_PERMITTED: int
        REMOVE_OPERATION_NOT_PERMITTED: int
        UPDATE_OPERATION_NOT_PERMITTED: int
        MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT: int
        OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE: int
        CREATE_AS_REMOVED_NOT_PERMITTED: int
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: int
        OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE: int
        MUTATE_NOT_PERMITTED_FOR_CUSTOMER: int
