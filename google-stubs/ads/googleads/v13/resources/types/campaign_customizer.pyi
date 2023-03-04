from typing import Any

import proto

from google.ads.googleads.v13.common.types.customizer_value import CustomizerValue
from google.ads.googleads.v13.enums.types.customizer_value_status import (
    CustomizerValueStatusEnum,
)

class CampaignCustomizer(proto.Message):
    resource_name: str
    campaign: str
    customizer_attribute: str
    status: CustomizerValueStatusEnum.CustomizerValueStatus
    value: CustomizerValue
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign: str = ...,
        customizer_attribute: str = ...,
        status: CustomizerValueStatusEnum.CustomizerValueStatus = ...,
        value: CustomizerValue = ...
    ) -> None: ...