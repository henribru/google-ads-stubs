from google.ads.googleads.v20.enums.types.conversion_origin import ConversionOriginEnum
from google.ads.googleads.v20.enums.types.conversion_action_category import ConversionActionCategoryEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CampaignConversionGoal(proto.Message):
    resource_name: str
    campaign: str
    category: ConversionActionCategoryEnum.ConversionActionCategory
    origin: ConversionOriginEnum.ConversionOrigin
    biddable: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., campaign: str = ..., category: ConversionActionCategoryEnum.ConversionActionCategory = ..., origin: ConversionOriginEnum.ConversionOrigin = ..., biddable: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "campaign", "category", "origin", "biddable"]) -> bool: ...
