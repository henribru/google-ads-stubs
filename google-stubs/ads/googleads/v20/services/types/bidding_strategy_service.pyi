import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import bidding_strategy as gagr_bidding_strategy
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateBiddingStrategiesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['BiddingStrategyOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class BiddingStrategyOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_bidding_strategy.BiddingStrategy
    update: gagr_bidding_strategy.BiddingStrategy
    remove: str

class MutateBiddingStrategiesResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateBiddingStrategyResult']

class MutateBiddingStrategyResult(proto.Message):
    resource_name: str
    bidding_strategy: gagr_bidding_strategy.BiddingStrategy
