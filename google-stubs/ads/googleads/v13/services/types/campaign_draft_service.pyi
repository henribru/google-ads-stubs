from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.campaign_draft import CampaignDraft

_M = TypeVar("_M")

class CampaignDraftOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignDraft
    update: CampaignDraft
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: CampaignDraft = ...,
        update: CampaignDraft = ...,
        remove: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["update_mask", "create", "update", "remove"]) -> bool: ...  # type: ignore[override]

class ListCampaignDraftAsyncErrorsRequest(proto.Message):
    resource_name: str
    page_token: str
    page_size: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        page_token: str = ...,
        page_size: int = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "page_token", "page_size"]) -> bool: ...  # type: ignore[override]

class ListCampaignDraftAsyncErrorsResponse(proto.Message):
    errors: MutableSequence[Status]
    next_page_token: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        errors: MutableSequence[Status] = ...,
        next_page_token: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["errors", "next_page_token"]) -> bool: ...  # type: ignore[override]

class MutateCampaignDraftResult(proto.Message):
    resource_name: str
    campaign_draft: CampaignDraft
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign_draft: CampaignDraft = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "campaign_draft"]) -> bool: ...  # type: ignore[override]

class MutateCampaignDraftsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignDraftOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CampaignDraftOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure", "validate_only", "response_content_type"]) -> bool: ...  # type: ignore[override]

class MutateCampaignDraftsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignDraftResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignDraftResult] = ...
    ) -> None: ...
    def __contains__(self, key: Literal["partial_failure_error", "results"]) -> bool: ...  # type: ignore[override]

class PromoteCampaignDraftRequest(proto.Message):
    campaign_draft: str
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign_draft: str = ...,
        validate_only: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["campaign_draft", "validate_only"]) -> bool: ...  # type: ignore[override]
