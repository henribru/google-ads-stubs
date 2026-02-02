import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class LocalServicesLeadCreditIssuanceDecisionEnum(proto.Message):
    class CreditIssuanceDecision(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        SUCCESS_NOT_REACHED_THRESHOLD = 2
        SUCCESS_REACHED_THRESHOLD = 3
        FAIL_OVER_THRESHOLD = 4
        FAIL_NOT_ELIGIBLE = 5
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
