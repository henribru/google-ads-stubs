import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import campaign_budget as gagr_campaign_budget
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignBudgetsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignBudgetOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignBudgetOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign_budget.CampaignBudget
    update: gagr_campaign_budget.CampaignBudget
    remove: str

class MutateCampaignBudgetsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignBudgetResult']

class MutateCampaignBudgetResult(proto.Message):
    resource_name: str
    campaign_budget: gagr_campaign_budget.CampaignBudget
