from typing import Any

import proto

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
