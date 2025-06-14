from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.rpc.status_pb2 import Status
from google.ads.googleads.v20.enums.types.response_content_type import ResponseContentTypeEnum
from collections.abc import MutableSequence
from google.ads.googleads.v20.resources.types.ad_group_ad import AdGroupAd
from google.ads.googleads.v20.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v20.resources.types.ad_group_ad import AdGroupAd
from google.ads.googleads.v20.resources.types.ad_group_ad import AdGroupAd
from google.ads.googleads.v20.common.types.policy import PolicyValidationParameter
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupAdOperation(proto.Message):
    update_mask: FieldMask
    policy_validation_parameter: PolicyValidationParameter
    create: AdGroupAd
    update: AdGroupAd
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., update_mask: FieldMask = ..., policy_validation_parameter: PolicyValidationParameter = ..., create: AdGroupAd = ..., update: AdGroupAd = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "policy_validation_parameter", "create", "update", "remove"]) -> bool: ...
class AssetsWithFieldType(proto.Message):
    asset: str
    asset_field_type: AssetFieldTypeEnum.AssetFieldType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., asset: str = ..., asset_field_type: AssetFieldTypeEnum.AssetFieldType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["asset", "asset_field_type"]) -> bool: ...
class MutateAdGroupAdResult(proto.Message):
    resource_name: str
    ad_group_ad: AdGroupAd
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., ad_group_ad: AdGroupAd = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "ad_group_ad"]) -> bool: ...
class MutateAdGroupAdsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AdGroupAdOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., customer_id: str = ..., operations: MutableSequence[AdGroupAdOperation] = ..., partial_failure: bool = ..., validate_only: bool = ..., response_content_type: ResponseContentTypeEnum.ResponseContentType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...
class MutateAdGroupAdsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateAdGroupAdResult]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., partial_failure_error: Status = ..., results: MutableSequence[MutateAdGroupAdResult] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["partial_failure_error", "results"]) -> bool: ...
class RemoveAutomaticallyCreatedAssetsRequest(proto.Message):
    ad_group_ad: str
    assets_with_field_type: MutableSequence[AssetsWithFieldType]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., ad_group_ad: str = ..., assets_with_field_type: MutableSequence[AssetsWithFieldType] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["ad_group_ad", "assets_with_field_type"]) -> bool: ...
