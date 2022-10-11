import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Incomplete

class MutateCampaignDraftsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete
    response_content_type: Incomplete

class PromoteCampaignDraftRequest(proto.Message):
    campaign_draft: Incomplete
    validate_only: Incomplete

class CampaignDraftOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    update: Incomplete
    remove: Incomplete

class MutateCampaignDraftsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateCampaignDraftResult(proto.Message):
    resource_name: Incomplete
    campaign_draft: Incomplete

class ListCampaignDraftAsyncErrorsRequest(proto.Message):
    resource_name: Incomplete
    page_token: Incomplete
    page_size: Incomplete

class ListCampaignDraftAsyncErrorsResponse(proto.Message):
    @property
    def raw_page(self): ...
    errors: Incomplete
    next_page_token: Incomplete
