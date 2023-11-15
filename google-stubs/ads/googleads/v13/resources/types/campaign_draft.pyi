from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v13.enums.types.campaign_draft_status import (
    CampaignDraftStatusEnum,
)

_M = TypeVar("_M")

class CampaignDraft(proto.Message):
    resource_name: str
    draft_id: int
    base_campaign: str
    name: str
    draft_campaign: str
    status: CampaignDraftStatusEnum.CampaignDraftStatus
    has_experiment_running: bool
    long_running_operation: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        draft_id: int = ...,
        base_campaign: str = ...,
        name: str = ...,
        draft_campaign: str = ...,
        status: CampaignDraftStatusEnum.CampaignDraftStatus = ...,
        has_experiment_running: bool = ...,
        long_running_operation: str = ...
    ) -> None: ...
