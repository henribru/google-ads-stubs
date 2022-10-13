from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.campaign_asset import CampaignAsset

class CampaignAssetOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignAsset
    update: CampaignAsset
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignAsset = ...,
        update: CampaignAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignAssetResult(proto.Message):
    resource_name: str
    campaign_asset: CampaignAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_asset: CampaignAsset = ...
    ) -> None: ...

class MutateCampaignAssetsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignAssetsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCampaignAssetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCampaignAssetResult] = ...
    ) -> None: ...
