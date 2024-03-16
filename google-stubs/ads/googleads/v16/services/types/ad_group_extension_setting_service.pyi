from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v16.resources.types.ad_group_extension_setting import (
    AdGroupExtensionSetting,
)

_M = TypeVar("_M")

class AdGroupExtensionSettingOperation(proto.Message):
    update_mask: FieldMask
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    create: AdGroupExtensionSetting
    update: AdGroupExtensionSetting
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
        create: AdGroupExtensionSetting = ...,
        update: AdGroupExtensionSetting = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "update_mask", "response_content_type", "create", "update", "remove"
        ],
    ) -> bool: ...

class MutateAdGroupExtensionSettingResult(proto.Message):
    resource_name: str
    ad_group_extension_setting: AdGroupExtensionSetting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_extension_setting: AdGroupExtensionSetting = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "ad_group_extension_setting"]
    ) -> bool: ...

class MutateAdGroupExtensionSettingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupExtensionSettingOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupExtensionSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["customer_id", "operations", "partial_failure", "validate_only"],
    ) -> bool: ...

class MutateAdGroupExtensionSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupExtensionSettingResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupExtensionSettingResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "results"]
    ) -> bool: ...
