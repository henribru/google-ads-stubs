from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class UserListCustomerTypeCategoryEnum(proto.Message):
    class UserListCustomerTypeCategory(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ALL_CUSTOMERS = 2
        PURCHASERS = 3
        HIGH_VALUE_CUSTOMERS = 4
        DISENGAGED_CUSTOMERS = 5
        QUALIFIED_LEADS = 6
        CONVERTED_LEADS = 7
        PAID_SUBSCRIBERS = 8
        LOYALTY_SIGN_UPS = 9
        CART_ABANDONERS = 10
        LOYALTY_TIER_1_MEMBERS = 11
        LOYALTY_TIER_2_MEMBERS = 12
        LOYALTY_TIER_3_MEMBERS = 13
        LOYALTY_TIER_4_MEMBERS = 14
        LOYALTY_TIER_5_MEMBERS = 15
        LOYALTY_TIER_6_MEMBERS = 16
        LOYALTY_TIER_7_MEMBERS = 17

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
