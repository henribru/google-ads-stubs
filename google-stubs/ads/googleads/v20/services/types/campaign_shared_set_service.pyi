import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v20.resources.types import campaign_shared_set as gagr_campaign_shared_set
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignSharedSetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignSharedSetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignSharedSetOperation(proto.Message):
    create: gagr_campaign_shared_set.CampaignSharedSet
    remove: str

class MutateCampaignSharedSetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignSharedSetResult']

class MutateCampaignSharedSetResult(proto.Message):
    resource_name: str
    campaign_shared_set: gagr_campaign_shared_set.CampaignSharedSet
