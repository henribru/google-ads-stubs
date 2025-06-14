import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import ad_parameter as gagr_ad_parameter
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAdParametersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AdParameterOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class AdParameterOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_ad_parameter.AdParameter
    update: gagr_ad_parameter.AdParameter
    remove: str

class MutateAdParametersResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateAdParameterResult']

class MutateAdParameterResult(proto.Message):
    resource_name: str
    ad_parameter: gagr_ad_parameter.AdParameter
