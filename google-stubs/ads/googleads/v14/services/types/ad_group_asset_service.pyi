from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v14.resources.types.ad_group_asset import AdGroupAsset

_M = TypeVar("_M")

class AdGroupAssetOperation(proto.Message):
    update_mask: FieldMask
    create: AdGroupAsset
    update: AdGroupAsset
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AdGroupAsset = ...,
        update: AdGroupAsset = ...,
        remove: str = ...
    ) -> None: ...

class MutateAdGroupAssetResult(proto.Message):
    resource_name: str
    ad_group_asset: AdGroupAsset
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        ad_group_asset: AdGroupAsset = ...
    ) -> None: ...

class MutateAdGroupAssetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupAssetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AdGroupAssetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateAdGroupAssetsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupAssetResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateAdGroupAssetResult] = ...
    ) -> None: ...
