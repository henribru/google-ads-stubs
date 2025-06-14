import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v18.resources.types import campaign_draft as gagr_campaign_draft
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignDraftsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignDraftOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class PromoteCampaignDraftRequest(proto.Message):
    campaign_draft: str
    validate_only: bool

class CampaignDraftOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign_draft.CampaignDraft
    update: gagr_campaign_draft.CampaignDraft
    remove: str

class MutateCampaignDraftsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignDraftResult']

class MutateCampaignDraftResult(proto.Message):
    resource_name: str
    campaign_draft: gagr_campaign_draft.CampaignDraft

class ListCampaignDraftAsyncErrorsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int

class ListCampaignDraftAsyncErrorsResponse(proto.Message):
    @property
    def raw_page(self): ...
    errors: MutableSequence[status_pb2.Status]
    next_page_token: str
