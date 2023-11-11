from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.campaign_extension_setting import (
    CampaignExtensionSetting,
)

_M = TypeVar("_M")

class CampaignExtensionSettingOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignExtensionSetting
    update: CampaignExtensionSetting
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignExtensionSetting = ...,
        update: CampaignExtensionSetting = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignExtensionSettingResult(proto.Message):
    resource_name: str
    campaign_extension_setting: CampaignExtensionSetting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_extension_setting: CampaignExtensionSetting = ...
    ) -> None: ...

class MutateCampaignExtensionSettingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignExtensionSettingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignExtensionSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignExtensionSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignExtensionSettingResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignExtensionSettingResult] = ...
    ) -> None: ...
