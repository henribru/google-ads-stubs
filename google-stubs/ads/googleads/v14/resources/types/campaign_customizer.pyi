from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.common.types.customizer_value import CustomizerValue
from google.ads.googleads.v14.enums.types.customizer_value_status import (
    CustomizerValueStatusEnum,
)

_M = TypeVar("_M")

class CampaignCustomizer(proto.Message):
    resource_name: str
    campaign: str
    customizer_attribute: str
    status: CustomizerValueStatusEnum.CustomizerValueStatus
    value: CustomizerValue
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: str = ...,
        customizer_attribute: str = ...,
        status: CustomizerValueStatusEnum.CustomizerValueStatus = ...,
        value: CustomizerValue = ...
    ) -> None: ...
