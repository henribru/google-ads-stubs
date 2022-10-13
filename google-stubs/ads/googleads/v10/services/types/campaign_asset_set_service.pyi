from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.campaign_asset_set import CampaignAssetSet

class CampaignAssetSetOperation(proto.Message):
    create: CampaignAssetSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CampaignAssetSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignAssetSetResult(proto.Message):
    resource_name: str
    campaign_asset_set: CampaignAssetSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_asset_set: CampaignAssetSet = ...
    ) -> None: ...

class MutateCampaignAssetSetsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignAssetSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignAssetSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignAssetSetsResponse(proto.Message):
    results: list[MutateCampaignAssetSetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateCampaignAssetSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
