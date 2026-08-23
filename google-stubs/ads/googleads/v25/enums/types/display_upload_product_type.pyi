from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class DisplayUploadProductTypeEnum(proto.Message):
    class DisplayUploadProductType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        HTML5_UPLOAD_AD = 2
        DYNAMIC_HTML5_EDUCATION_AD = 3
        DYNAMIC_HTML5_FLIGHT_AD = 4
        DYNAMIC_HTML5_HOTEL_RENTAL_AD = 5
        DYNAMIC_HTML5_JOB_AD = 6
        DYNAMIC_HTML5_LOCAL_AD = 7
        DYNAMIC_HTML5_REAL_ESTATE_AD = 8
        DYNAMIC_HTML5_CUSTOM_AD = 9
        DYNAMIC_HTML5_TRAVEL_AD = 10
        DYNAMIC_HTML5_HOTEL_AD = 11

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
