from google.ads.googleads.v22.common.types.criteria import SearchThemeInfo
from google.ads.googleads.v22.common.types.criteria import AudienceInfo
from collections.abc import MutableSequence
from google.ads.googleads.v22.enums.types.asset_group_signal_approval_status import AssetGroupSignalApprovalStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AssetGroupSignal(proto.Message):
    resource_name: str
    asset_group: str
    approval_status: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    disapproval_reasons: MutableSequence[str]
    audience: AudienceInfo
    search_theme: SearchThemeInfo
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., asset_group: str = ..., approval_status: AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus = ..., disapproval_reasons: MutableSequence[str] = ..., audience: AudienceInfo = ..., search_theme: SearchThemeInfo = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "asset_group", "approval_status", "disapproval_reasons", "audience", "search_theme"]) -> bool: ...
