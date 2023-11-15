from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.offline_user_data import (
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
