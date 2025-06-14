import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import campaign_customizer as gagr_campaign_customizer
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignCustomizersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignCustomizerOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignCustomizerOperation(proto.Message):
    create: gagr_campaign_customizer.CampaignCustomizer
    remove: str

class MutateCampaignCustomizersResponse(proto.Message):
    results: MutableSequence['MutateCampaignCustomizerResult']
    partial_failure_error: status_pb2.Status

class MutateCampaignCustomizerResult(proto.Message):
    resource_name: str
    campaign_customizer: gagr_campaign_customizer.CampaignCustomizer
