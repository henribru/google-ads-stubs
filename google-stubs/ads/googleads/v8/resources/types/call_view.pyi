from typing import Any

import proto

from google.ads.googleads.v8.enums.types import (
    call_type as call_type,
    google_voice_call_status as google_voice_call_status,
)

__protobuf__: Any

class CallView(proto.Message):
    resource_name: Any
    caller_country_code: Any
    caller_area_code: Any
    call_duration_seconds: Any
    start_call_date_time: Any
    end_call_date_time: Any
    call_tracking_display_location: Any
    type_: Any
    call_status: Any
