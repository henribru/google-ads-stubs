from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status

from google.ads.googleads.v10.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v10.resources.types.campaign_experiment import (
    CampaignExperiment,
)

class CampaignExperimentOperation(proto.Message):
    update_mask: FieldMask
    update: CampaignExperiment
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        update: CampaignExperiment = ...,
        remove: str = ...
    ) -> None: ...

class CreateCampaignExperimentMetadata(proto.Message):
    campaign_experiment: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign_experiment: str = ...
    ) -> None: ...

class CreateCampaignExperimentRequest(proto.Message):
    customer_id: str
    campaign_experiment: CampaignExperiment
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        campaign_experiment: CampaignExperiment = ...,
        validate_only: bool = ...
    ) -> None: ...

class EndCampaignExperimentRequest(proto.Message):
    campaign_experiment: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign_experiment: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class GraduateCampaignExperimentRequest(proto.Message):
    campaign_experiment: str
    campaign_budget: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign_experiment: str = ...,
        campaign_budget: str = ...,
        validate_only: bool = ...
    ) -> None: ...

class GraduateCampaignExperimentResponse(proto.Message):
    graduated_campaign: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        graduated_campaign: str = ...
    ) -> None: ...

class ListCampaignExperimentAsyncErrorsRequest(proto.Message):
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

class ListCampaignExperimentAsyncErrorsResponse(proto.Message):
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

class MutateCampaignExperimentResult(proto.Message):
    resource_name: str
    campaign_experiment: CampaignExperiment
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_experiment: CampaignExperiment = ...
    ) -> None: ...

class MutateCampaignExperimentsRequest(proto.Message):
    customer_id: str
    operations: list[CampaignExperimentOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[CampaignExperimentOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignExperimentsResponse(proto.Message):
    partial_failure_error: Status
    results: list[MutateCampaignExperimentResult]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        partial_failure_error: Status = ...,
        results: list[MutateCampaignExperimentResult] = ...
    ) -> None: ...

class PromoteCampaignExperimentRequest(proto.Message):
    campaign_experiment: str
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        campaign_experiment: str = ...,
        validate_only: bool = ...
    ) -> None: ...
