from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class CustomerAcquisitionOptimizationModeEnum(proto.Message):
    class CustomerAcquisitionOptimizationMode(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        TARGET_ALL_EQUALLY = 2
        BID_HIGHER_FOR_NEW_CUSTOMER = 3
        TARGET_NEW_CUSTOMER = 4
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
