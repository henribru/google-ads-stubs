from collections.abc import MutableSequence
from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.campaign_group import CampaignGroup

class CampaignGroupOperation(proto.Message):
    update_mask: FieldMask
    create: CampaignGroup
    update: CampaignGroup
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: CampaignGroup = ...,
        update: CampaignGroup = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignGroupResult(proto.Message):
    resource_name: str
    campaign_group: CampaignGroup
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_group: CampaignGroup = ...
    ) -> None: ...

class MutateCampaignGroupsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignGroupOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignGroupOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignGroupsResponse(proto.Message):
    results: MutableSequence[MutateCampaignGroupResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[MutateCampaignGroupResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
