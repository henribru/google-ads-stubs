from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.asset_field_type import AssetFieldTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class RemoveCampaignAutomaticallyCreatedAssetOperation(proto.Message):
    campaign: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, campaign: str = ..., asset: str = ..., field_type: AssetFieldTypeEnum.AssetFieldType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["campaign", "asset", "field_type"]) -> bool: ...
class RemoveCampaignAutomaticallyCreatedAssetRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[RemoveCampaignAutomaticallyCreatedAssetOperation]
    partial_failure: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operations: MutableSequence[RemoveCampaignAutomaticallyCreatedAssetOperation] = ..., partial_failure: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure"]) -> bool: ...
class RemoveCampaignAutomaticallyCreatedAssetResponse(proto.Message):
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error"]) -> bool: ...
