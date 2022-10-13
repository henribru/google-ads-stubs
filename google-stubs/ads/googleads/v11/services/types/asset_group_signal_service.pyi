from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.asset_group_signal import AssetGroupSignal

class AssetGroupSignalOperation(proto.Message):
    create: AssetGroupSignal
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: AssetGroupSignal = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetGroupSignalResult(proto.Message):
    resource_name: str
    asset_group_signal: AssetGroupSignal
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group_signal: AssetGroupSignal = ...
    ) -> None: ...

class MutateAssetGroupSignalsRequest(proto.Message):
    customer_id: str
    operations: list[AssetGroupSignalOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AssetGroupSignalOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAssetGroupSignalsResponse(proto.Message):
    results: list[MutateAssetGroupSignalResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAssetGroupSignalResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
