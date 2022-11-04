from typing import Any

import proto

from google.ads.googleads.v12.enums.types.conversion_action_category import (
    ConversionActionCategoryEnum,
)
from google.ads.googleads.v12.enums.types.conversion_origin import ConversionOriginEnum

class CampaignConversionGoal(proto.Message):
    resource_name: str
    campaign: str
    category: ConversionActionCategoryEnum.ConversionActionCategory
    origin: ConversionOriginEnum.ConversionOrigin
    biddable: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        category: ConversionActionCategoryEnum.ConversionActionCategory = ...,
        origin: ConversionOriginEnum.ConversionOrigin = ...,
        biddable: bool = ...
    ) -> None: ...
