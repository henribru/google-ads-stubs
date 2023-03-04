from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v13.common.types.offline_user_data import (
    CustomerMatchUserListMetadata,
    UserData,
)

class UploadUserDataRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[UserDataOperation]
    customer_match_user_list_metadata: CustomerMatchUserListMetadata
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[UserDataOperation] = ...,
        customer_match_user_list_metadata: CustomerMatchUserListMetadata = ...
    ) -> None: ...

class UploadUserDataResponse(proto.Message):
    upload_date_time: str
    received_operations_count: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        upload_date_time: str = ...,
        received_operations_count: int = ...
    ) -> None: ...

class UserDataOperation(proto.Message):
    create: UserData
    remove: UserData
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: UserData = ...,
        remove: UserData = ...
    ) -> None: ...
