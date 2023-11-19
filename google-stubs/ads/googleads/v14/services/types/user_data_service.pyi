from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.offline_user_data import (
    CustomerMatchUserListMetadata,
    UserData,
)

_M = TypeVar("_M")

class UploadUserDataRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[UserDataOperation]
    customer_match_user_list_metadata: CustomerMatchUserListMetadata
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[UserDataOperation] = ...,
        customer_match_user_list_metadata: CustomerMatchUserListMetadata = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "customer_match_user_list_metadata"]) -> bool: ...  # type: ignore[override]

class UploadUserDataResponse(proto.Message):
    upload_date_time: str
    received_operations_count: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        upload_date_time: str = ...,
        received_operations_count: int = ...
    ) -> None: ...
    def __contains__(self, key: Literal["upload_date_time", "received_operations_count"]) -> bool: ...  # type: ignore[override]

class UserDataOperation(proto.Message):
    create: UserData
    remove: UserData
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: UserData = ...,
        remove: UserData = ...
    ) -> None: ...
    def __contains__(self, key: Literal["create", "remove"]) -> bool: ...  # type: ignore[override]
