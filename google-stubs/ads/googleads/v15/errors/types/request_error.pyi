from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class RequestErrorEnum(proto.Message):
    class RequestError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        RESOURCE_NAME_MISSING = 3
        RESOURCE_NAME_MALFORMED = 4
        BAD_RESOURCE_ID = 17
        INVALID_CUSTOMER_ID = 16
        OPERATION_REQUIRED = 5
        RESOURCE_NOT_FOUND = 6
        INVALID_PAGE_TOKEN = 7
        EXPIRED_PAGE_TOKEN = 8
        INVALID_PAGE_SIZE = 22
        REQUIRED_FIELD_MISSING = 9
        IMMUTABLE_FIELD = 11
        TOO_MANY_MUTATE_OPERATIONS = 13
        CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT = 14
        CANNOT_MODIFY_FOREIGN_FIELD = 15
        INVALID_ENUM_VALUE = 18
        DEVELOPER_TOKEN_PARAMETER_MISSING = 19
        LOGIN_CUSTOMER_ID_PARAMETER_MISSING = 20
        VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN = 21
        CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS = 29
        CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS = 30
        INCONSISTENT_RETURN_SUMMARY_ROW_VALUE = 31
        TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED = 32
        RPC_DEADLINE_TOO_SHORT = 33
        UNSUPPORTED_VERSION = 38
        CLOUD_PROJECT_NOT_FOUND = 39

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
