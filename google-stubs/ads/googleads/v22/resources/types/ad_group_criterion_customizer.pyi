from google.ads.googleads.v22.common.types.customizer_value import CustomizerValue
from google.ads.googleads.v22.enums.types.customizer_value_status import CustomizerValueStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdGroupCriterionCustomizer(proto.Message):
    resource_name: str
    ad_group_criterion: str
    customizer_attribute: str
    status: CustomizerValueStatusEnum.CustomizerValueStatus
    value: CustomizerValue
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., ad_group_criterion: str = ..., customizer_attribute: str = ..., status: CustomizerValueStatusEnum.CustomizerValueStatus = ..., value: CustomizerValue = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "ad_group_criterion", "customizer_attribute", "status", "value"]) -> bool: ...
