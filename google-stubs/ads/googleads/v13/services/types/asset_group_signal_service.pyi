from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.asset_group_signal import AssetGroupSignal

_M = TypeVar("_M")

class AssetGroupSignalOperation(proto.Message):
    create: AssetGroupSignal
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        create: AssetGroupSignal = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetGroupSignalResult(proto.Message):
    resource_name: str
    asset_group_signal: AssetGroupSignal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group_signal: AssetGroupSignal = ...
    ) -> None: ...

class MutateAssetGroupSignalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetGroupSignalOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AssetGroupSignalOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAssetGroupSignalsResponse(proto.Message):
    results: MutableSequence[MutateAssetGroupSignalResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAssetGroupSignalResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
