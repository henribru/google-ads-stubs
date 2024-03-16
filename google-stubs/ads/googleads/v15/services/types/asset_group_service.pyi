from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v15.resources.types.asset_group import AssetGroup

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
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create", "update", "remove"]
    ) -> bool: ...

class MutateAssetGroupResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name"]
    ) -> bool: ...

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
        validate_only: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operations", "validate_only"]
    ) -> bool: ...

class MutateAssetGroupsResponse(proto.Message):
    results: MutableSequence[MutateAssetGroupResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAssetGroupResult] = ...,
        partial_failure_error: Status = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["results", "partial_failure_error"]
    ) -> bool: ...
