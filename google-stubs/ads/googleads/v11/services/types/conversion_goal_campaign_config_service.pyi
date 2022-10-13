from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.conversion_goal_campaign_config import (
    ConversionGoalCampaignConfig,
)

class ConversionGoalCampaignConfigOperation(proto.Message):
    update_mask: FieldMask
    update: ConversionGoalCampaignConfig
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: ConversionGoalCampaignConfig = ...
    ) -> None: ...

class MutateConversionGoalCampaignConfigResult(proto.Message):
    resource_name: str
    conversion_goal_campaign_config: ConversionGoalCampaignConfig
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        conversion_goal_campaign_config: ConversionGoalCampaignConfig = ...
    ) -> None: ...

class MutateConversionGoalCampaignConfigsRequest(proto.Message):
    customer_id: str
    operations: list[ConversionGoalCampaignConfigOperation]
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ConversionGoalCampaignConfigOperation] = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateConversionGoalCampaignConfigsResponse(proto.Message):
    results: list[MutateConversionGoalCampaignConfigResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateConversionGoalCampaignConfigResult] = ...
    ) -> None: ...
