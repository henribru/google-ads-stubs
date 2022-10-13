from typing import Any

import proto

class PromotionExtensionDiscountModifierEnum(proto.Message):
    class PromotionExtensionDiscountModifier(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        UP_TO = 2
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
