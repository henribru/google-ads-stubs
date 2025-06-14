import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import shared_set as gagr_shared_set
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateSharedSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['SharedSetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class SharedSetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_shared_set.SharedSet
    update: gagr_shared_set.SharedSet
    remove: str

class MutateSharedSetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateSharedSetResult']

class MutateSharedSetResult(proto.Message):
    resource_name: str
    shared_set: gagr_shared_set.SharedSet
