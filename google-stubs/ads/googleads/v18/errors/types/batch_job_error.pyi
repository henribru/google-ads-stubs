import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class BatchJobErrorEnum(proto.Message):
    class BatchJobError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        CANNOT_MODIFY_JOB_AFTER_JOB_STARTS_RUNNING = 2
        EMPTY_OPERATIONS = 3
        INVALID_SEQUENCE_TOKEN = 4
        RESULTS_NOT_READY = 5
        INVALID_PAGE_SIZE = 6
        CAN_ONLY_REMOVE_PENDING_JOB = 7
        CANNOT_LIST_RESULTS = 8
        ASSET_GROUP_AND_ASSET_GROUP_ASSET_TRANSACTION_FAILURE = 9
        ASSET_GROUP_LISTING_GROUP_FILTER_TRANSACTION_FAILURE = 10
        REQUEST_TOO_LARGE = 11
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
