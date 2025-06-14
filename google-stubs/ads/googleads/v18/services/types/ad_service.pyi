import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import policy
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import ad as gagr_ad
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdOperation']
    partial_failure: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType
    validate_only: bool

class AdOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    policy_validation_parameter: policy.PolicyValidationParameter
    update: gagr_ad.Ad

class MutateAdsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdResult']

class MutateAdResult(proto.Message):
    resource_name: str
    ad: gagr_ad.Ad
