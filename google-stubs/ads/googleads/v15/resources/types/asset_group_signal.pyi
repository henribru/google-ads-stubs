from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.criteria import AudienceInfo, SearchThemeInfo
from google.ads.googleads.v15.enums.types.asset_group_signal_approval_status import (
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
        ],
    ) -> bool: ...
