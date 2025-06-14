from google.ads.googleads.v18.enums.types.user_list_customer_type_category import UserListCustomerTypeCategoryEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class UserListCustomerType(proto.Message):
    resource_name: str
    user_list: str
    customer_type_category: UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategory
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., user_list: str = ..., customer_type_category: UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategory = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "user_list", "customer_type_category"]) -> bool: ...
