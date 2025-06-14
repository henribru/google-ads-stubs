import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import custom_parameter
from google.ads.googleads.v20.enums.types import call_conversion_reporting_state as gage_call_conversion_reporting_state
from typing import MutableSequence

__protobuf__: Incomplete

class CallFeedItem(proto.Message):
    phone_number: str
    country_code: str
    call_tracking_enabled: bool
    call_conversion_action: str
    call_conversion_tracking_disabled: bool
    call_conversion_reporting_state: gage_call_conversion_reporting_state.CallConversionReportingStateEnum.CallConversionReportingState

class CalloutFeedItem(proto.Message):
    callout_text: str

class SitelinkFeedItem(proto.Message):
    link_text: str
    line1: str
    line2: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    url_custom_parameters: MutableSequence[custom_parameter.CustomParameter]
    final_url_suffix: str
