from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2
from google.rpc import status_pb2 as status_pb2

__protobuf__: Any

class GetCampaignDraftRequest(proto.Message):
    resource_name: Any

class MutateCampaignDraftsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any
    response_content_type: Any

class PromoteCampaignDraftRequest(proto.Message):
    campaign_draft: Any
    validate_only: Any

class CampaignDraftOperation(proto.Message):
    update_mask: Any
    create: Any
    update: Any
    remove: Any

class MutateCampaignDraftsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignDraftResult(proto.Message):
    resource_name: Any
    campaign_draft: Any

class ListCampaignDraftAsyncErrorsRequest(proto.Message):
    resource_name: Any
    page_token: Any
    page_size: Any

class ListCampaignDraftAsyncErrorsResponse(proto.Message):
    @property
    def raw_page(self): ...
    errors: Any
    next_page_token: Any
