from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v13.resources.types.campaign_customizer import (
    CampaignCustomizer,
)

_M = TypeVar("_M")

class CampaignCustomizerOperation(proto.Message):
    create: CampaignCustomizer
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        create: CampaignCustomizer = ...,
        remove: str = ...
    ) -> None: ...

class MutateCampaignCustomizerResult(proto.Message):
    resource_name: str
    campaign_customizer: CampaignCustomizer
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_customizer: CampaignCustomizer = ...
    ) -> None: ...

class MutateCampaignCustomizersRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignCustomizerOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[CampaignCustomizerOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...
    ) -> None: ...

class MutateCampaignCustomizersResponse(proto.Message):
    results: MutableSequence[MutateCampaignCustomizerResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[MutateCampaignCustomizerResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
