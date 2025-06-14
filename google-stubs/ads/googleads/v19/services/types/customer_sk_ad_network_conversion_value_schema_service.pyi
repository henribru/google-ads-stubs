from google.rpc.status_pb2 import Status
from google.ads.googleads.v19.resources.types.customer_sk_ad_network_conversion_value_schema import CustomerSkAdNetworkConversionValueSchema
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CustomerSkAdNetworkConversionValueSchemaOperation(proto.Message):
    update: CustomerSkAdNetworkConversionValueSchema
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update: CustomerSkAdNetworkConversionValueSchema = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update"]) -> bool: ...
class MutateCustomerSkAdNetworkConversionValueSchemaRequest(proto.Message):
    customer_id: str
    operation: CustomerSkAdNetworkConversionValueSchemaOperation
    validate_only: bool
    enable_warnings: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operation: CustomerSkAdNetworkConversionValueSchemaOperation = ..., validate_only: bool = ..., enable_warnings: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operation", "validate_only", "enable_warnings"]) -> bool: ...
class MutateCustomerSkAdNetworkConversionValueSchemaResponse(proto.Message):
    result: MutateCustomerSkAdNetworkConversionValueSchemaResult
    warning: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, result: MutateCustomerSkAdNetworkConversionValueSchemaResult = ..., warning: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["result", "warning"]) -> bool: ...
class MutateCustomerSkAdNetworkConversionValueSchemaResult(proto.Message):
    resource_name: str
    app_id: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., app_id: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "app_id"]) -> bool: ...
