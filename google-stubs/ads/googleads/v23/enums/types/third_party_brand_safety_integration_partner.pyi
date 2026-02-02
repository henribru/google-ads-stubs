from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class ThirdPartyBrandSafetyIntegrationPartnerEnum(proto.Message):
    class ThirdPartyBrandSafetyIntegrationPartner(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DOUBLE_VERIFY = 2
        INTEGRAL_AD_SCIENCE = 3
        ZEFR = 4

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
