from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class VanityPharmaTextEnum(proto.Message):
    class VanityPharmaText(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PRESCRIPTION_TREATMENT_WEBSITE_EN = 2
        PRESCRIPTION_TREATMENT_WEBSITE_ES = 3
        PRESCRIPTION_DEVICE_WEBSITE_EN = 4
        PRESCRIPTION_DEVICE_WEBSITE_ES = 5
        MEDICAL_DEVICE_WEBSITE_EN = 6
        MEDICAL_DEVICE_WEBSITE_ES = 7
        PREVENTATIVE_TREATMENT_WEBSITE_EN = 8
        PREVENTATIVE_TREATMENT_WEBSITE_ES = 9
        PRESCRIPTION_CONTRACEPTION_WEBSITE_EN = 10
        PRESCRIPTION_CONTRACEPTION_WEBSITE_ES = 11
        PRESCRIPTION_VACCINE_WEBSITE_EN = 12
        PRESCRIPTION_VACCINE_WEBSITE_ES = 13

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
