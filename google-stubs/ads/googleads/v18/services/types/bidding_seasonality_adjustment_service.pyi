import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import bidding_seasonality_adjustment as gagr_bidding_seasonality_adjustment
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateBiddingSeasonalityAdjustmentsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['BiddingSeasonalityAdjustmentOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class BiddingSeasonalityAdjustmentOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_bidding_seasonality_adjustment.BiddingSeasonalityAdjustment
    update: gagr_bidding_seasonality_adjustment.BiddingSeasonalityAdjustment
    remove: str

class MutateBiddingSeasonalityAdjustmentsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateBiddingSeasonalityAdjustmentsResult']

class MutateBiddingSeasonalityAdjustmentsResult(proto.Message):
    resource_name: str
    bidding_seasonality_adjustment: gagr_bidding_seasonality_adjustment.BiddingSeasonalityAdjustment
