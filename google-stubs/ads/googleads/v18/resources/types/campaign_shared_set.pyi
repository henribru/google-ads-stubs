from google.ads.googleads.v18.enums.types.campaign_shared_set_status import CampaignSharedSetStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignSharedSet(proto.Message):
    resource_name: str
    campaign: str
    shared_set: str
    status: CampaignSharedSetStatusEnum.CampaignSharedSetStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., campaign: str = ..., shared_set: str = ..., status: CampaignSharedSetStatusEnum.CampaignSharedSetStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign", "shared_set", "status"]) -> bool: ...
