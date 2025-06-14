import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import user_list_customer_type_category

__protobuf__: Incomplete

class UserListCustomerType(proto.Message):
    resource_name: str
    user_list: str
    customer_type_category: user_list_customer_type_category.UserListCustomerTypeCategoryEnum.UserListCustomerTypeCategory
