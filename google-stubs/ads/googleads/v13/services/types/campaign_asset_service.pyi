from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.campaign_asset import CampaignAsset

_M = TypeVar("_M")

class CampaignAssetOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignAsset
    update: CampaignAsset
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_asset: CampaignAsset = ...
    ) -> None: ...

class MutateCampaignAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignAssetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignAssetResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignAssetResult] = ...
    ) -> None: ...
