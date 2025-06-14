import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class LocalServicesLeadSurveyDissatisfiedReasonEnum(proto.Message):
    class SurveyDissatisfiedReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        OTHER_DISSATISFIED_REASON = 2
        GEO_MISMATCH = 3
        JOB_TYPE_MISMATCH = 4
        NOT_READY_TO_BOOK = 5
        SPAM = 6
        DUPLICATE = 7
        SOLICITATION = 8
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
