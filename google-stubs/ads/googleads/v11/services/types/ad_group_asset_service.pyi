from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.ad_group_asset import AdGroupAsset

class AdGroupAssetOperation(proto.Message):
    update_mask: FieldMask
    create: AdGroupAsset
    update: AdGroupAsset
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AdGroupAsset = ...,
        update: AdGroupAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupAssetResult(proto.Message):
    resource_name: str
    ad_group_asset: AdGroupAsset
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_asset: AdGroupAsset = ...
    ) -> None: ...

class MutateAdGroupAssetsRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupAssetsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateAdGroupAssetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateAdGroupAssetResult] = ...
    ) -> None: ...
