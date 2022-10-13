from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.customer_extension_setting import (
    CustomerExtensionSetting,
)

class CustomerExtensionSettingOperation(proto.Message):
    update_mask: FieldMask
    create: CustomerExtensionSetting
    update: CustomerExtensionSetting
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CustomerExtensionSetting = ...,
        update: CustomerExtensionSetting = ...,
        remove: str = ...
    ) -> None: ...

class MutateCustomerExtensionSettingResult(proto.Message):
    resource_name: str
    customer_extension_setting: CustomerExtensionSetting
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        customer_extension_setting: CustomerExtensionSetting = ...
    ) -> None: ...

class MutateCustomerExtensionSettingsRequest(proto.Message):
    customer_id: str
    operations: list[CustomerExtensionSettingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CustomerExtensionSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCustomerExtensionSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCustomerExtensionSettingResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCustomerExtensionSettingResult] = ...
    ) -> None: ...
