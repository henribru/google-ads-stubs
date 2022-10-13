from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.campaign_customizer import (
    CampaignCustomizer,
)

class CampaignCustomizerOperation(proto.Message):
    create: CampaignCustomizer
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CampaignCustomizer = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignCustomizerResult(proto.Message):
    resource_name: str
    campaign_customizer: CampaignCustomizer
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_customizer: CampaignCustomizer = ...
    ) -> None: ...

class MutateCampaignCustomizersRequest(proto.Message):
    customer_id: str
    operations: list[CampaignCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignCustomizerOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignCustomizersResponse(proto.Message):
    results: list[MutateCampaignCustomizerResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCampaignCustomizerResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
