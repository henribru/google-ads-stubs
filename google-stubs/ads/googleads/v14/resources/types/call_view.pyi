from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v14.enums.types.call_tracking_display_location import (
    CallTrackingDisplayLocationEnum,
)
from google.ads.googleads.v14.enums.types.call_type import CallTypeEnum
from google.ads.googleads.v14.enums.types.google_voice_call_status import (
    GoogleVoiceCallStatusEnum,
)

_M = TypeVar("_M")

class CallView(proto.Message):
    resource_name: str
    caller_country_code: str
    caller_area_code: str
    call_duration_seconds: int
    start_call_date_time: str
    end_call_date_time: str
    call_tracking_display_location: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    type_: CallTypeEnum.CallType
    call_status: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        caller_country_code: str = ...,
        caller_area_code: str = ...,
        call_duration_seconds: int = ...,
        start_call_date_time: str = ...,
        end_call_date_time: str = ...,
        call_tracking_display_location: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation = ...,
        type_: CallTypeEnum.CallType = ...,
        call_status: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus = ...
    ) -> None: ...
