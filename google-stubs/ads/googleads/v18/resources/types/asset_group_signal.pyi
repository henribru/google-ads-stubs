import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.common.types import criteria
from google.ads.googleads.v18.enums.types import asset_group_signal_approval_status
from typing import MutableSequence

__protobuf__: Incomplete

class AssetGroupSignal(proto.Message):
    resource_name: str
    asset_group: str
    approval_status: asset_group_signal_approval_status.AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatus
    disapproval_reasons: MutableSequence[str]
    audience: criteria.AudienceInfo
    search_theme: criteria.SearchThemeInfo
