from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v14.resources.types.asset_group import AssetGroup

_M = TypeVar("_M")

class AssetGroupOperation(proto.Message):
    update_mask: FieldMask
    create: AssetGroup
    update: AssetGroup
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AssetGroup = ...,
        update: AssetGroup = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetGroupResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...

class MutateAssetGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetGroupOperation]
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AssetGroupOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAssetGroupsResponse(proto.Message):
    results: MutableSequence[MutateAssetGroupResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAssetGroupResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
