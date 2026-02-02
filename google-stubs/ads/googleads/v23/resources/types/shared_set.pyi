from google.ads.googleads.v23.enums.types.vertical_ads_item_vertical_type import VerticalAdsItemVerticalTypeEnum
from google.ads.googleads.v23.enums.types.shared_set_status import SharedSetStatusEnum
from google.ads.googleads.v23.enums.types.shared_set_type import SharedSetTypeEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class SharedSet(proto.Message):
    resource_name: str
    id: int
    type_: SharedSetTypeEnum.SharedSetType
    name: str
    status: SharedSetStatusEnum.SharedSetStatus
    member_count: int
    reference_count: int
    vertical_ads_item_vertical_type: VerticalAdsItemVerticalTypeEnum.VerticalAdsItemVerticalType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., id: int = ..., type_: SharedSetTypeEnum.SharedSetType = ..., name: str = ..., status: SharedSetStatusEnum.SharedSetStatus = ..., member_count: int = ..., reference_count: int = ..., vertical_ads_item_vertical_type: VerticalAdsItemVerticalTypeEnum.VerticalAdsItemVerticalType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "id", "type_", "name", "status", "member_count", "reference_count", "vertical_ads_item_vertical_type"]) -> bool: ...
