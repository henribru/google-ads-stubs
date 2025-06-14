import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListCustomerTypeCategoryEnum(proto.Message):
    class UserListCustomerTypeCategory(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ALL_CUSTOMERS: int
        PURCHASERS: int
        HIGH_VALUE_CUSTOMERS: int
        DISENGAGED_CUSTOMERS: int
        QUALIFIED_LEADS: int
        CONVERTED_LEADS: int
        PAID_SUBSCRIBERS: int
        LOYALTY_SIGN_UPS: int
        CART_ABANDONERS: int
        LOYALTY_TIER_1_MEMBERS: int
        LOYALTY_TIER_2_MEMBERS: int
        LOYALTY_TIER_3_MEMBERS: int
        LOYALTY_TIER_4_MEMBERS: int
        LOYALTY_TIER_5_MEMBERS: int
        LOYALTY_TIER_6_MEMBERS: int
        LOYALTY_TIER_7_MEMBERS: int
