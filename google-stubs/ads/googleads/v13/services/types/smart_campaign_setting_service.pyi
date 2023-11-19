from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.enums.types.smart_campaign_not_eligible_reason import (
    SmartCampaignNotEligibleReasonEnum,
)
from google.ads.googleads.v13.enums.types.smart_campaign_status import (
    SmartCampaignStatusEnum,
)
from google.ads.googleads.v13.resources.types.smart_campaign_setting import (
    SmartCampaignSetting,
)

_M = TypeVar("_M")

class GetSmartCampaignStatusRequest(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class GetSmartCampaignStatusResponse(proto.Message):
    smart_campaign_status: SmartCampaignStatusEnum.SmartCampaignStatus
    not_eligible_details: SmartCampaignNotEligibleDetails
    eligible_details: SmartCampaignEligibleDetails
    paused_details: SmartCampaignPausedDetails
    removed_details: SmartCampaignRemovedDetails
    ended_details: SmartCampaignEndedDetails
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        smart_campaign_status: SmartCampaignStatusEnum.SmartCampaignStatus = ...,
        not_eligible_details: SmartCampaignNotEligibleDetails = ...,
        eligible_details: SmartCampaignEligibleDetails = ...,
        paused_details: SmartCampaignPausedDetails = ...,
        removed_details: SmartCampaignRemovedDetails = ...,
        ended_details: SmartCampaignEndedDetails = ...
    ) -> None: ...
    def __contains__(self, key: Literal["smart_campaign_status", "not_eligible_details", "eligible_details", "paused_details", "removed_details", "ended_details"]) -> bool: ...  # type: ignore[override]

class MutateSmartCampaignSettingResult(proto.Message):
    resource_name: str
    smart_campaign_setting: SmartCampaignSetting
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        smart_campaign_setting: SmartCampaignSetting = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "smart_campaign_setting"]) -> bool: ...  # type: ignore[override]

class MutateSmartCampaignSettingsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[SmartCampaignSettingOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[SmartCampaignSettingOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

class MutateSmartCampaignSettingsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateSmartCampaignSettingResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateSmartCampaignSettingResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]

class SmartCampaignEligibleDetails(proto.Message):
    last_impression_date_time: str
    end_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        last_impression_date_time: str = ...,
        end_date_time: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["last_impression_date_time", "end_date_time"]) -> bool: ...  # type: ignore[override]

class SmartCampaignEndedDetails(proto.Message):
    end_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        end_date_time: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["end_date_time"]) -> bool: ...  # type: ignore[override]

class SmartCampaignNotEligibleDetails(proto.Message):
    not_eligible_reason: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        not_eligible_reason: SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReason = ...
    ) -> None: ...
    def __contains__(self, key: Literal["not_eligible_reason"]) -> bool: ...  # type: ignore[override]

class SmartCampaignPausedDetails(proto.Message):
    paused_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        paused_date_time: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["paused_date_time"]) -> bool: ...  # type: ignore[override]

class SmartCampaignRemovedDetails(proto.Message):
    removed_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        removed_date_time: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["removed_date_time"]) -> bool: ...  # type: ignore[override]

class SmartCampaignSettingOperation(proto.Message):
    update: SmartCampaignSetting
    update_mask: FieldMask
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update: SmartCampaignSetting = ...,
        update_mask: FieldMask = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update", "update_mask"]) -> bool: ...  # type: ignore[override]
