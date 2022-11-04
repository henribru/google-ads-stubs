from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v12.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v12.resources.types.ad_group_asset_set import AdGroupAssetSet

class AdGroupAssetSetOperation(proto.Message):
    create: AdGroupAssetSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AdGroupAssetSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupAssetSetResult(proto.Message):
    resource_name: str
    ad_group_asset_set: AdGroupAssetSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_asset_set: AdGroupAssetSet = ...
    ) -> None: ...

class MutateAdGroupAssetSetsRequest(proto.Message):
    customer_id: str
    operations: list[AdGroupAssetSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AdGroupAssetSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupAssetSetsResponse(proto.Message):
    results: list[MutateAdGroupAssetSetResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAdGroupAssetSetResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
