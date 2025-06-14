from collections.abc import MutableSequence
from google.ads.googleads.v19.common.types.custom_parameter import CustomParameter
from collections.abc import MutableSequence
from collections.abc import MutableSequence
from google.ads.googleads.v19.enums.types.call_conversion_reporting_state import CallConversionReportingStateEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class CallFeedItem(proto.Message):
    phone_number: str
    country_code: str
    call_tracking_enabled: bool
    call_conversion_action: str
    call_conversion_tracking_disabled: bool
    call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., phone_number: str = ..., country_code: str = ..., call_tracking_enabled: bool = ..., call_conversion_action: str = ..., call_conversion_tracking_disabled: bool = ..., call_conversion_reporting_state: CallConversionReportingStateEnum.CallConversionReportingState = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["phone_number", "country_code", "call_tracking_enabled", "call_conversion_action", "call_conversion_tracking_disabled", "call_conversion_reporting_state"]) -> bool: ...
class CalloutFeedItem(proto.Message):
    callout_text: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., callout_text: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["callout_text"]) -> bool: ...
class SitelinkFeedItem(proto.Message):
    link_text: str
    line1: str
    line2: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[CustomParameter]
    final_url_suffix: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., link_text: str = ..., line1: str = ..., line2: str = ..., final_urls: MutableSequence[str] = ..., final_mobile_urls: MutableSequence[str] = ..., tracking_url_template: str = ..., url_custom_parameters: MutableSequence[CustomParameter] = ..., final_url_suffix: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["link_text", "line1", "line2", "final_urls", "final_mobile_urls", "tracking_url_template", "url_custom_parameters", "final_url_suffix"]) -> bool: ...
