from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.campaign_draft import CampaignDraft

class CampaignDraftOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignDraft
    update: CampaignDraft
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignDraft = ...,
        update: CampaignDraft = ...,
        remove: str = ...
    ) -> None: ...

class ListCampaignDraftAsyncErrorsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        page_token: str = ...,
        page_size: int = ...
    ) -> None: ...

class ListCampaignDraftAsyncErrorsResponse(proto.Message):
    errors: list[Status]
    next_page_token: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        errors: list[Status] = ...,
        next_page_token: str = ...
    ) -> None: ...

class MutateCampaignDraftResult(proto.Message):
    resource_name: str
    campaign_draft: CampaignDraft
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_draft: CampaignDraft = ...
    ) -> None: ...

class MutateCampaignDraftsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignDraftOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignDraftOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignDraftsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCampaignDraftResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCampaignDraftResult] = ...
    ) -> None: ...

class PromoteCampaignDraftRequest(proto.Message):
    campaign_draft: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign_draft: str = ...,
        validate_only: bool = ...
    ) -> None: ...
