from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.call_tracking_display_location import (
    CallTrackingDisplayLocationEnum,
)
from google.ads.googleads.v16.enums.types.call_type import CallTypeEnum
from google.ads.googleads.v16.enums.types.google_voice_call_status import (
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
    call_tracking_display_location: (
        CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation
    )
    type_: CallTypeEnum.CallType
    call_status: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        caller_country_code: str = ...,
        caller_area_code: str = ...,
        call_duration_seconds: int = ...,
        start_call_date_time: str = ...,
        end_call_date_time: str = ...,
        call_tracking_display_location: CallTrackingDisplayLocationEnum.CallTrackingDisplayLocation = ...,
        type_: CallTypeEnum.CallType = ...,
        call_status: GoogleVoiceCallStatusEnum.GoogleVoiceCallStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "caller_country_code",
            "caller_area_code",
            "call_duration_seconds",
            "start_call_date_time",
            "end_call_date_time",
            "call_tracking_display_location",
            "type_",
            "call_status",
        ],
    ) -> bool: ...
