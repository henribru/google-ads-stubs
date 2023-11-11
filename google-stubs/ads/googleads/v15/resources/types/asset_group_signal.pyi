from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v15.common.types.criteria import AudienceInfo, SearchThemeInfo
from google.ads.googleads.v15.enums.types.asset_group_signal_approval_status import (
    AssetGroupSignalApprovalStatusEnum,
)

class AssetGroupSignal(proto.Message):
    resource_name: str
    asset_group: str
    approval_status: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    disapproval_reasons: MutableSequence[str]
    audience: AudienceInfo
    search_theme: SearchThemeInfo
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        asset_group: str = ...,
        approval_status: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus = ...,
        disapproval_reasons: MutableSequence[str] = ...,
        audience: AudienceInfo = ...,
        search_theme: SearchThemeInfo = ...
    ) -> None: ...
