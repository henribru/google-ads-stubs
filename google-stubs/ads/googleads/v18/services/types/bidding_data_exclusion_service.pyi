import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import bidding_data_exclusion as gagr_bidding_data_exclusion
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateBiddingDataExclusionsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['BiddingDataExclusionOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class BiddingDataExclusionOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_bidding_data_exclusion.BiddingDataExclusion
    update: gagr_bidding_data_exclusion.BiddingDataExclusion
    remove: str

class MutateBiddingDataExclusionsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateBiddingDataExclusionsResult']

class MutateBiddingDataExclusionsResult(proto.Message):
    resource_name: str
    bidding_data_exclusion: gagr_bidding_data_exclusion.BiddingDataExclusion
