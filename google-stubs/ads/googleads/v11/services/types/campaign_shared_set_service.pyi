from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v11.resources.types.campaign_shared_set import (
    CampaignSharedSet,
)

class CampaignSharedSetOperation(proto.Message):
    create: CampaignSharedSet
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CampaignSharedSet = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignSharedSetResult(proto.Message):
    resource_name: str
    campaign_shared_set: CampaignSharedSet
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_shared_set: CampaignSharedSet = ...
    ) -> None: ...

class MutateCampaignSharedSetsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignSharedSetOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignSharedSetOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignSharedSetsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCampaignSharedSetResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCampaignSharedSetResult] = ...
    ) -> None: ...
