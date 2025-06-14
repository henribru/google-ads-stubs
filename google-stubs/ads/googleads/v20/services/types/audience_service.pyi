import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import audience as gagr_audience
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateAudiencesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['AudienceOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class MutateAudiencesResponse(proto.Message):
    results: MutableSequence['MutateAudienceResult']
    partial_failure_error: status_pb2.Status

class AudienceOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_audience.Audience
    update: gagr_audience.Audience

class MutateAudienceResult(proto.Message):
    resource_name: str
    audience: gagr_audience.Audience
