import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class RegulatoryFeeTypeEnum(proto.Message):
    class RegulatoryFeeType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        AUSTRIA_DST_FEE = 2
        TURKIYE_REGULATORY_OPERATING_COST = 3
        UK_DST_FEE = 4
        SPAIN_REGULATORY_OPERATING_COST = 5
        FRANCE_REGULATORY_OPERATING_COST = 6
        ITALY_REGULATORY_OPERATING_COST = 7
        INDIA_REGULATORY_OPERATING_COST = 8
        POLAND_REGULATORY_OPERATING_COST = 9
        OPERATING_CHARGES = 10
        CANADA_DST_FEE = 11
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: NoReturn) -> bool: ...
