from google.ads.googleads.v19.common.types.offline_user_data import UserData
from google.ads.googleads.v19.common.types.offline_user_data import UserData
from google.ads.googleads.v19.common.types.offline_user_data import CustomerMatchUserListMetadata
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class UploadUserDataRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[UserDataOperation]
    customer_match_user_list_metadata: CustomerMatchUserListMetadata
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[UserDataOperation] = ..., customer_match_user_list_metadata: CustomerMatchUserListMetadata = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "customer_match_user_list_metadata"]) -> bool: ...
class UploadUserDataResponse(proto.Message):
    upload_date_time: str
    received_operations_count: int
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, upload_date_time: str = ..., received_operations_count: int = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["upload_date_time", "received_operations_count"]) -> bool: ...
class UserDataOperation(proto.Message):
    create: UserData
    remove: UserData
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, create: UserData = ..., remove: UserData = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
