from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.common.types.criteria import (
    AudienceInfo,
    LocalServiceIdInfo,
    SearchThemeInfo,
    VerticalAdsItemGroupRuleListInfo,
)
from google.ads.googleads.v25.enums.types.asset_group_signal_approval_status import (
    AssetGroupSignalApprovalStatusEnum,
)

_M = TypeVar("_M")

class AssetGroupSignal(proto.Message):
    resource_name: str
    asset_group: str
    approval_status: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    disapproval_reasons: MutableSequence[str]
    audience: AudienceInfo
    search_theme: SearchThemeInfo
    local_services_id: LocalServiceIdInfo
    vertical_ads_item_group_rule_list: VerticalAdsItemGroupRuleListInfo
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group: str = ...,
        approval_status: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus = ...,
        disapproval_reasons: MutableSequence[str] = ...,
        audience: AudienceInfo = ...,
        search_theme: SearchThemeInfo = ...,
        local_services_id: LocalServiceIdInfo = ...,
        vertical_ads_item_group_rule_list: VerticalAdsItemGroupRuleListInfo = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "asset_group",
            "approval_status",
            "disapproval_reasons",
            "audience",
            "search_theme",
            "local_services_id",
            "vertical_ads_item_group_rule_list",
        ],
    ) -> bool: ...
