from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v20.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.customer_asset_set import CustomerAssetSet
from google.ads.googleads.v20.resources.types.customer_asset_set import CustomerAssetSet
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerAssetSetOperation(proto.Message):
    create: CustomerAssetSet
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., create: CustomerAssetSet = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["create", "remove"]) -> bool: ...
class MutateCustomerAssetSetResult(proto.Message):
    resource_name: str
    customer_asset_set: CustomerAssetSet
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., customer_asset_set: CustomerAssetSet = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "customer_asset_set"]) -> bool: ...
class MutateCustomerAssetSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CustomerAssetSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[CustomerAssetSetOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateCustomerAssetSetsResponse(proto.Message):
    results: MutableSequence[MutateCustomerAssetSetResult]
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., results: MutableSequence[MutateCustomerAssetSetResult] = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["results", "partial_failure_error"]) -> bool: ...
