import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import policy
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import asset_group_signal as gagr_asset_group_signal
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAssetGroupSignalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AssetGroupSignalOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AssetGroupSignalOperation(proto.Message):
    exempt_policy_violation_keys: MutableSequence[policy.PolicyViolationKey]
    create: gagr_asset_group_signal.AssetGroupSignal
    remove: str

class MutateAssetGroupSignalsResponse(proto.Message):
    results: MutableSequence['MutateAssetGroupSignalResult']
    partial_failure_error: status_pb2.Status

class MutateAssetGroupSignalResult(proto.Message):
    resource_name: str
    asset_group_signal: gagr_asset_group_signal.AssetGroupSignal
