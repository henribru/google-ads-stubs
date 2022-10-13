from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.resources.types.campaign_label import CampaignLabel

class CampaignLabelOperation(proto.Message):
    create: CampaignLabel
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CampaignLabel = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignLabelResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class MutateCampaignLabelsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignLabelOperation]
    partial_failure: bool
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignLabelOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateCampaignLabelsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCampaignLabelResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCampaignLabelResult] = ...
    ) -> None: ...
