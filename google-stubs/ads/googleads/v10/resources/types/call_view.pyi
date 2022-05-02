import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    call_type as call_type,
    google_voice_call_status as google_voice_call_status,
)

__protobuf__: Incomplete

class CallView(proto.Message):
    resource_name: Incomplete
    caller_country_code: Incomplete
    caller_area_code: Incomplete
    call_duration_seconds: Incomplete
    start_call_date_time: Incomplete
    end_call_date_time: Incomplete
    call_tracking_display_location: Incomplete
    type_: Incomplete
    call_status: Incomplete
