from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.conversion_goal_campaign_config import (
    ConversionGoalCampaignConfig,
)

_M = TypeVar("_M")

class ConversionGoalCampaignConfigOperation(proto.Message):
    update_mask: FieldMask
    update: ConversionGoalCampaignConfig
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        update: ConversionGoalCampaignConfig = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "update"]) -> bool: ...  # type: ignore[override]

class MutateConversionGoalCampaignConfigResult(proto.Message):
    resource_name: str
    conversion_goal_campaign_config: ConversionGoalCampaignConfig
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        conversion_goal_campaign_config: ConversionGoalCampaignConfig = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "conversion_goal_campaign_config"]) -> bool: ...  # type: ignore[override]

class MutateConversionGoalCampaignConfigsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ConversionGoalCampaignConfigOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ConversionGoalCampaignConfigOperation] = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

class MutateConversionGoalCampaignConfigsResponse(proto.Message):
    results: MutableSequence[MutateConversionGoalCampaignConfigResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateConversionGoalCampaignConfigResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["results"]) -> bool: ...  # type: ignore[override]
