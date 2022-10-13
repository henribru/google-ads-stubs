from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.resources.types.asset_group import AssetGroup

class AssetGroupOperation(proto.Message):
    update_mask: FieldMask
    create: AssetGroup
    update: AssetGroup
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AssetGroup = ...,
        update: AssetGroup = ...,
        remove: str = ...
    ) -> None: ...

class MutateAssetGroupResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateAssetGroupsRequest(proto.Message):
    customer_id: str
    operations: list[AssetGroupOperation]
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[AssetGroupOperation] = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAssetGroupsResponse(proto.Message):
    results: list[MutateAssetGroupResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[MutateAssetGroupResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
